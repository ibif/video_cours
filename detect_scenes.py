"""
.github/scripts/detect_scenes.py — Détermine automatiquement :
  - le mode d'exécution (smoke-test / rendu-hd-final / manuel)
  - la liste des scènes à rendre
  - la série (1ereC / 1ereD) et la matière (Maths, Physique, etc.) du
    chapitre concerné, extraites du nom du tag git

Convention de tag OBLIGATOIRE pour un rendu HD final :
    chapitre__<Serie>__<Matiere>__<NomChapitre>
    ex : chapitre__1ereC__Maths__Derivation

⚠️ <Matiere> doit être EXACTEMENT le nom du PDF source sans extension
(ex: "Maths" pour 1ereC/Maths.pdf), pas une abréviation différente — c'est
ce qui permet d'écrire automatiquement la vidéo dans le bon répertoire.
"""

import glob
import json
import os
import sys


def main() -> None:
    event_name = os.environ.get("EVENT_NAME", "")
    ref_type = os.environ.get("REF_TYPE", "")
    ref_name = os.environ.get("REF_NAME", "")
    manual_chapitres = os.environ.get("MANUAL_CHAPITRES", "")
    actor = os.environ.get("ACTOR", "")
    diff = os.environ.get("FICHIERS_DIFF", "")

    mode = "smoke-test"
    serie = ""
    matiere = ""
    chapitre_nom = ""
    scenes: list[str] = []

    if event_name == "workflow_dispatch" and manual_chapitres.strip():
        mode = "manuel"
        chapitre_nom = "manuel"
        scenes = [s.strip() for s in manual_chapitres.split(",") if s.strip()]

    elif ref_type == "tag" and ref_name.startswith("chapitre__"):
        parts = ref_name.split("__")
        if len(parts) != 4:
            print(
                f"::error::Tag '{ref_name}' invalide. Format attendu : "
                "chapitre__<Serie>__<Matiere>__<NomChapitre> "
                "(ex: chapitre__1ereC__Maths__Derivation)",
                file=sys.stderr,
            )
            sys.exit(1)

        _, serie, matiere, chapitre_nom = parts
        motif = f"scenes/{matiere}_{chapitre_nom}_*.py"
        scenes = sorted(
            os.path.basename(f)[: -len(".py")] for f in glob.glob(motif)
        )

        if not scenes:
            print(
                f"::error::Aucune scène trouvée pour le motif '{motif}'. "
                "Vérifie que le tag correspond bien aux noms de fichiers "
                "dans scenes/ (convention Matiere_NomChapitre_NN.py, avec "
                "Matiere identique au nom du PDF source).",
                file=sys.stderr,
            )
            sys.exit(1)

        mode = "rendu-hd-final"

    elif actor.endswith("[bot]"):
        # Évite de redéclencher un smoke-test inutile sur le commit que le
        # pipeline lui-même pousse (ajout de la vidéo dans Serie/Matiere/).
        mode = "smoke-test"
        scenes = []

    else:
        # Push normal → uniquement les scènes modifiées/ajoutées (diff git
        # calculé par l'étape précédente du workflow, une ligne par fichier)
        scenes = sorted(
            {
                os.path.basename(line.strip())[: -len(".py")]
                for line in diff.splitlines()
                if line.strip()
            }
        )

    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"mode={mode}\n")
        f.write(f"serie={serie}\n")
        f.write(f"matiere={matiere}\n")
        f.write(f"chapitre_nom={chapitre_nom}\n")
        f.write(f"scenes={json.dumps(scenes)}\n")

    print(f"mode={mode} serie={serie} matiere={matiere} "
          f"chapitre_nom={chapitre_nom} scenes={scenes}")


if __name__ == "__main__":
    main()
