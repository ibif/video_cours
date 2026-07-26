"""
scenes/SVT_MouvementsPlaques_10.py — Chapitre 7 (1ereD, SVT), scène 10.

Clôture du chapitre : retour sur le fil conducteur (Grand-Bassam, le
puzzle des continents), puis L'ESSENTIEL DU CHAPITRE en synthèse finale.
Source : 1ereD/SVT.pdf, pages 90-99 (synthèse de fin de chapitre).
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class SyntheseMouvementsPlaques(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 7 — Synthèse : les plaques en mouvement")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : retour sur le fil conducteur -----------------------------
        retour = Text(
            _wrap(
                "Revenons à Grand-Bassam. Les côtes d'Afrique et d'Amérique "
                "du Sud s'emboîtent, le Mésosaure relie leurs fossiles, la "
                "dorsale médio-atlantique crache des laves en leur milieu : "
                "ce ne sont pas des hasards, mais les traces d'un seul et "
                "même mécanisme, la tectonique des plaques.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        retour.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Revenons à notre point de départ, sur la plage de "
                "Grand-Bassam. Les côtes d'Afrique et d'Amérique du Sud "
                "s'emboîtent, les fossiles du Mésosaure relient les deux "
                "continents, et la dorsale médio-atlantique crache des "
                "laves en plein milieu de l'océan qui les sépare "
                "aujourd'hui. Nous savons désormais que ce ne sont pas des "
                "hasards : ce sont les traces d'un seul et même mécanisme, "
                "la tectonique des plaques."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(retour))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retour))

        # --- Animation du raisonnement : les grandes étapes de la démonstration
        entete_fil = Text("Le fil de la démonstration", font_size=26, color=YELLOW, weight="BOLD")
        entete_fil.next_to(titre, DOWN, buff=0.55)

        fil = _bullets(
            [
                "La lithosphère rigide, découpée en plaques, glisse sur "
                "l'asthénosphère ductile.",
                "Paléomagnétisme et âge des fonds océaniques prouvent "
                "l'expansion, à quelques cm/an.",
                "Trois types de limites : divergence, convergence "
                "(subduction ou collision), coulissage.",
                "La convection mantellique, aidée des forces gravitaires, "
                "est le moteur de l'ensemble.",
            ],
            font_size=22,
            width=52,
        )
        fil.next_to(entete_fil, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Récapitulons le fil de la démonstration. La lithosphère, "
                "rigide, est découpée en plaques qui glissent sur "
                "l'asthénosphère, ductile. Le paléomagnétisme et l'âge des "
                "fonds océaniques prouvent que ces plaques s'écartent "
                "réellement, à raison de quelques centimètres par an. Trois "
                "types de limites organisent leurs mouvements : la "
                "divergence, la convergence, en subduction ou en collision, "
                "et le coulissage. Et le moteur de tout cet ensemble est la "
                "convection mantellique, aidée par les forces gravitaires "
                "aux dorsales et aux zones de subduction."
            )
        ) as tracker:
            self.play(FadeIn(entete_fil))
            self.play(FadeIn(fil))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_fil), FadeOut(fil))

        # --- Exemple traité : la Côte d'Ivoire, toujours en zone stable --------
        rappel_ci = Text(
            _wrap(
                "Et la Côte d'Ivoire dans tout cela ? Toujours au cœur de "
                "la plaque africaine, loin de toute limite active : c'est "
                "précisément cette position qui explique son calme "
                "sismique et volcanique, à l'opposé du Japon ou des Andes.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        rappel_ci.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Et la Côte d'Ivoire dans tout cela ? Elle reste toujours "
                "au cœur de la plaque africaine, loin de toute limite "
                "active. C'est précisément cette position qui explique son "
                "calme sismique et volcanique, à l'opposé de pays comme le "
                "Japon ou les pays andins, situés eux en pleine limite de "
                "plaques."
            )
        ) as tracker:
            self.play(FadeIn(rappel_ci))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel_ci))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) -----------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "La Terre : croûte, manteau, noyau ; mécaniquement, "
                    "lithosphère rigide (croûte+manteau supérieur, ~100 km) "
                    "sur asthénosphère ductile.",
                    "La lithosphère est découpée en plaques (africaine, "
                    "pacifique, eurasiatique...) qui se déplacent de "
                    "quelques cm/an ; la Côte d'Ivoire est en zone stable.",
                    "L'expansion océanique est prouvée par le "
                    "paléomagnétisme (bandes symétriques) et l'âge des "
                    "fonds (nul à l'axe, jamais plus de 200 Ma).",
                    "Vitesse d'expansion : v=d/t, avec 1 km=10^5 cm et "
                    "1 Ma=10^6 ans ; multiplier par 2 pour l'écartement "
                    "total.",
                    "Divergence : lithosphère créée par accrétion (rift "
                    "est-africain = océan en formation).",
                    "Convergence : lithosphère détruite par subduction "
                    "(Andes, Japon) ou déformée par collision (Himalaya).",
                    "Transformante : coulissage (San Andreas), ni création "
                    "ni destruction, séismes superficiels.",
                    "Séismes et volcans dessinent les limites de plaques ; "
                    "l'intérieur des plaques est stable.",
                    "Moteur : convection mantellique, aidée par poussée "
                    "gravitaire des dorsales et traction des plaques "
                    "plongeantes.",
                    "Bilan nul : la surface créée aux dorsales égale la "
                    "surface détruite en subduction — rayon terrestre "
                    "constant.",
                ],
                font_size=17,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        # Garde-fou : si le contenu (10 points) dépasse la hauteur visible du
        # cadre malgré le petit corps de police, on réduit l'échelle globale
        # de la boîte pour qu'elle tienne entièrement à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. La Terre est formée de "
                "croûte, de manteau et de noyau ; mécaniquement, une "
                "lithosphère rigide, croûte plus manteau supérieur, "
                "environ cent kilomètres, repose sur une asthénosphère "
                "ductile. La lithosphère est découpée en plaques, "
                "africaine, pacifique, eurasiatique et bien d'autres, qui "
                "se déplacent de quelques centimètres par an ; la Côte "
                "d'Ivoire est en zone stable. L'expansion océanique est "
                "prouvée par le paléomagnétisme, avec ses bandes "
                "symétriques, et par l'âge des fonds océaniques, nul à "
                "l'axe et jamais supérieur à deux cents millions d'années. "
                "La vitesse d'expansion se calcule par v égale d sur t, "
                "avec un kilomètre égale dix puissance cinq centimètres et "
                "un million d'années égale dix puissance six ans, puis on "
                "multiplie par deux pour obtenir l'écartement total. Aux "
                "limites divergentes, de la lithosphère est créée par "
                "accrétion, comme dans le rift est-africain. Aux limites "
                "convergentes, de la lithosphère est détruite par "
                "subduction, comme aux Andes ou au Japon, ou déformée par "
                "collision, comme à l'Himalaya. Aux limites transformantes, "
                "les plaques coulissent, comme à San Andreas, sans "
                "création ni destruction, avec des séismes superficiels. "
                "Séismes et volcans dessinent les limites de plaques, "
                "tandis que l'intérieur des plaques reste stable. Le "
                "moteur de tout ce système est la convection mantellique, "
                "aidée par la poussée gravitaire des dorsales et la "
                "traction des plaques plongeantes. Enfin, le bilan global "
                "est nul : la surface créée aux dorsales égale la surface "
                "détruite en subduction, et le rayon de la Terre reste "
                "constant."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
