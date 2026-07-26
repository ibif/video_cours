"""
scenes/SVT_EcosystemeAgroIndustriel_07.py — Chapitre 11 (1ereC, SVT), scène 07.

§ 3.2-3.3 La chaîne alimentaire (définition + exemple à 5 maillons de la
savane de Lamto) et le réseau alimentaire (définition + exemple construit
avec plusieurs chaînes croisées, notion d'omnivore pour la pintade), puis
méthode « plus le réseau est complexe, plus l'écosystème est stable ».
Source : 1ereC/SVT.pdf, pages 123-124.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _maillon(texte, couleur=WHITE, font_size=19):
    return Text(texte, font_size=font_size, color=couleur, weight="BOLD")


def _chaine(especes, couleur=WHITE, font_size=19):
    """Construit une VGroup 'espèce -> espèce -> ...' avec des flèches."""
    groupe = VGroup()
    labels = [_maillon(e, couleur, font_size) for e in especes]
    labels_group = VGroup(*labels).arrange(RIGHT, buff=0.75)
    fleches = VGroup()
    for i in range(len(labels) - 1):
        f = Arrow(labels[i].get_right(), labels[i + 1].get_left(), buff=0.08, color=YELLOW, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        fleches.add(f)
    groupe.add(labels_group, fleches)
    return groupe


class ChaineEtReseauAlimentaire(NotionScene):
    def construct(self):
        titre = scene_title("3.2-3.3 — Chaîne et réseau alimentaires")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : la chaîne alimentaire ----------------------------------
        chaine_def = definition_box(
            Text(
                _wrap(
                    "Une chaîne alimentaire est une suite d'êtres vivants "
                    "dans laquelle chacun se nourrit de celui qui le "
                    "précède. Le premier maillon est toujours un "
                    "producteur ; la flèche indique le sens du transfert "
                    "de matière et d'énergie (« est mangé par »).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        chaine_def.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une chaîne alimentaire est une suite d'êtres vivants dans "
                "laquelle chacun se nourrit de celui qui le précède. Le "
                "premier maillon est toujours un producteur, et la flèche "
                "indique le sens du transfert de matière et d'énergie, "
                "c'est-à-dire est mangé par."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(chaine_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(chaine_def))

        # --- Raisonnement : la chaîne de la savane de Lamto ------------------
        chaine_titre = Text("Exemple dans la savane de Lamto", font_size=23, color=YELLOW, weight="BOLD")
        chaine_titre.next_to(titre, DOWN, buff=0.5)

        chaine = _chaine(["Herbes", "Sauterelle", "Crapaud", "Serpent", "Aigle"], font_size=18)
        chaine.scale(0.9)
        chaine.next_to(chaine_titre, DOWN, buff=0.5)

        niveaux = Text("(P)        (C1)          (C2)          (C3)         (C4)", font_size=16, color="#AAAAAA")
        niveaux.next_to(chaine, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple dans la savane de Lamto : les herbes sont mangées "
                "par la sauterelle, mangée par le crapaud, mangé par le "
                "serpent, mangé lui-même par l'aigle. Soit, en niveaux "
                "trophiques : producteur, consommateur premier, deuxième, "
                "troisième, puis quatrième. Une chaîne compte rarement "
                "plus de quatre à six maillons — nous verrons pourquoi "
                "dans la partie sur les flux d'énergie."
            )
        ) as tracker:
            self.play(FadeIn(chaine_titre))
            self.play(Write(chaine))
            self.play(FadeIn(niveaux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(chaine_titre), FadeOut(chaine), FadeOut(niveaux))

        # --- Exemple traité : le réseau alimentaire ---------------------------
        reseau_def = definition_box(
            Text(
                _wrap(
                    "Un réseau alimentaire est l'ensemble des chaînes "
                    "alimentaires interconnectées d'un écosystème : dans "
                    "la réalité, un animal mange plusieurs proies et est "
                    "mangé par plusieurs prédateurs.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        reseau_def.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Dans la réalité, un animal mange plusieurs proies et est "
                "mangé par plusieurs prédateurs : les chaînes se croisent "
                "et forment un réseau alimentaire, ou réseau trophique, "
                "c'est-à-dire l'ensemble des chaînes alimentaires "
                "interconnectées d'un écosystème."
            )
        ) as tracker:
            self.play(FadeIn(reseau_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reseau_def))

        # Schéma du réseau : herbes / sauterelle / rat / pintade / crapaud /
        # lézard / serpent / aigle, avec les flèches de prédation observées.
        herbes = _maillon("Herbes", "#66BB6A", 17)
        sauterelle = _maillon("Sauterelle", WHITE, 17)
        rat = _maillon("Rat des champs", WHITE, 17)
        pintade = _maillon("Pintade", YELLOW, 17)
        crapaud = _maillon("Crapaud", WHITE, 17)
        lezard = _maillon("Lézard", WHITE, 17)
        serpent = _maillon("Serpent", WHITE, 17)
        aigle = _maillon("Aigle", "#FF7043", 17)

        ligne_p = VGroup(herbes).move_to(UP * 1.6)
        ligne_c1 = VGroup(sauterelle, rat, pintade).arrange(RIGHT, buff=1.0).move_to(UP * 0.55)
        ligne_c2 = VGroup(crapaud, lezard).arrange(RIGHT, buff=1.2).move_to(DOWN * 0.55)
        ligne_c3 = VGroup(serpent, aigle).arrange(RIGHT, buff=1.6).move_to(DOWN * 1.6)

        herbes.move_to(ligne_p)

        especes = VGroup(ligne_p, ligne_c1, ligne_c2, ligne_c3)

        liens = [
            (herbes, sauterelle), (herbes, rat), (herbes, pintade),
            (sauterelle, crapaud), (sauterelle, lezard), (sauterelle, pintade),
            (crapaud, serpent), (lezard, serpent),
            (rat, serpent), (rat, aigle),
            (pintade, serpent),
            (serpent, aigle),
        ]
        fleches = VGroup(
            *[Arrow(a.get_bottom(), b.get_top(), buff=0.08, color=YELLOW, stroke_width=1.5, max_tip_length_to_length_ratio=0.15) for a, b in liens]
        )

        reseau = VGroup(fleches, especes)
        reseau.scale(0.85)
        reseau.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici un réseau construit dans la savane. Les herbes sont "
                "mangées par la sauterelle, le rat des champs et la "
                "pintade. La sauterelle est mangée par le crapaud, le "
                "lézard et la pintade. Le crapaud et le lézard sont "
                "mangés par le serpent. Le rat des champs est mangé par le "
                "serpent et par l'aigle. La pintade est mangée par le "
                "serpent. Et le serpent est mangé par l'aigle."
            )
        ) as tracker:
            self.play(FadeIn(especes))
            self.play(FadeIn(fleches))
            self.wait(tracker.get_remaining_duration())

        # --- Zoom sur l'omnivorie de la pintade --------------------------------
        omnivore_note = Text(
            "La pintade mange herbes (C1) ET sauterelles (C2) : omnivore, 2 niveaux trophiques",
            font_size=17,
            color="#FFD54F",
            weight="BOLD",
        )
        omnivore_note.next_to(reseau, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Remarquez la pintade : elle mange à la fois les herbes, "
                "un producteur, ce qui en fait un consommateur primaire ; "
                "et la sauterelle, un consommateur primaire, ce qui en "
                "fait alors un consommateur secondaire. Elle occupe donc "
                "plusieurs niveaux trophiques : c'est un animal au régime "
                "mixte, un omnivore."
            )
        ) as tracker:
            self.play(FadeIn(omnivore_note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reseau), FadeOut(omnivore_note))

        # --- À retenir : point clé ----------------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Plus le réseau est complexe (beaucoup d'espèces, "
                    "beaucoup de liens), plus l'écosystème est stable : si "
                    "une proie disparaît, le prédateur peut se rabattre "
                    "sur une autre. C'est un argument majeur pour la "
                    "préservation de la biodiversité.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé à retenir : plus le réseau est complexe, "
                "beaucoup d'espèces et beaucoup de liens, plus "
                "l'écosystème est stable. Si une proie vient à disparaître, "
                "le prédateur peut se rabattre sur une autre. C'est un "
                "argument majeur pour la préservation de la biodiversité."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
