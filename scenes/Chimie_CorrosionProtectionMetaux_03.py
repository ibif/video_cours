"""
scenes/Chimie_CorrosionProtectionMetaux_03.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 03.

§ 3. Conclusion des expériences témoins + facteurs aggravants. property_box
de la condition nécessaire et suffisante (eau ET dioxygène simultanément).
Facteurs qui accélèrent la corrosion : eau salée / air marin (lagune
Ébrié), chaleur, pollution acide, rayures, contact avec un métal moins
réducteur.
Source : 1ereC/Chimie.pdf, chapitre 15, page 146.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


class ConclusionExperiencesFacteursAggravants(NotionScene):
    def construct(self):
        titre = scene_title("15.3 Conclusion des expériences et facteurs aggravants")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : rappel des trois résultats -------------------------------
        rappel = Text(
            _wrap(
                "Seul le tube réunissant eau ET air a rouillé ; les deux "
                "autres, où l'un des deux manquait, sont restés intacts. "
                "Qu'en conclure sur les conditions de la corrosion du "
                "fer ?",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        rappel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappelons les trois résultats obtenus : seul le tube "
                "réunissant à la fois de l'eau et de l'air a laissé le "
                "clou rouiller ; les deux autres tubes, où l'un des deux "
                "facteurs manquait, sont restés parfaitement intacts. "
                "Qu'en conclure sur les conditions réelles de la "
                "corrosion du fer ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel))

        # --- Raisonnement / à retenir : la condition nécessaire ----------------
        conclusion = property_box(
            VGroup(
                Text("La corrosion du fer nécessite la présence simultanée :", font_size=22, weight="BOLD"),
                Text("— de l'eau (ou de l'humidité de l'air) ;", font_size=21),
                Text("— du dioxygène (dissous dans l'eau ou de l'air).", font_size=21),
                Text("L'absence de l'un des deux suffit à empêcher la rouille.", font_size=20),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.4,
        )
        conclusion.next_to(titre, DOWN, buff=0.4)
        _fit(conclusion, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "On peut conclure avec certitude : la corrosion du fer "
                "nécessite la présence simultanée de l'eau, ou de "
                "l'humidité de l'air, et du dioxygène, qu'il soit dissous "
                "dans l'eau ou présent dans l'air. L'absence de l'un "
                "seul de ces deux facteurs suffit à empêcher totalement "
                "la formation de la rouille."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Exemple traité : facteurs qui aggravent la corrosion --------------
        entete_facteurs = Text("Des facteurs qui accélèrent la corrosion", font_size=22, color=YELLOW, weight="BOLD")
        entete_facteurs.next_to(titre, DOWN, buff=0.35)

        facteurs = _bullets(
            [
                "eau salée, air marin (ex : lagune Ébrié à Abidjan) — les ions dissous accélèrent le phénomène",
                "chaleur — accélère toute réaction chimique",
                "pollution acide (pluies acides, fumées industrielles)",
                "rayures ou fissures dans un revêtement protecteur",
                "contact avec un métal moins réducteur que le fer",
            ],
            font_size=20,
        )
        facteurs.next_to(entete_facteurs, DOWN, buff=0.35)
        groupe_facteurs = VGroup(entete_facteurs, facteurs)
        _fit(groupe_facteurs, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Une fois ces deux conditions réunies, plusieurs facteurs "
                "aggravent encore la vitesse de la corrosion. L'eau "
                "salée ou l'air marin, comme celui de la lagune Ébrié à "
                "Abidjan, accélère fortement le phénomène grâce aux ions "
                "dissous. La chaleur accélère toute réaction chimique. "
                "La pollution acide, comme les pluies acides ou les "
                "fumées industrielles, joue le même rôle. Une rayure ou "
                "une fissure dans un revêtement protecteur crée un point "
                "d'entrée pour l'eau et l'air. Enfin, le contact avec un "
                "métal moins réducteur que le fer favorise également sa "
                "corrosion, comme nous le verrons plus loin avec les "
                "micropiles."
            )
        ) as tracker:
            self.play(FadeIn(entete_facteurs))
            self.play(FadeIn(facteurs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_facteurs))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Un facteur aggravant (chaleur, sel…) accélère la "
                    "corrosion mais ne la déclenche pas seul : sans eau "
                    "ET sans dioxygène présents ensemble, aucune corrosion "
                    "n'a lieu, quelle que soit la température.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre condition nécessaire et "
                "facteur aggravant : la chaleur ou le sel accélèrent la "
                "corrosion, mais ne la déclenchent jamais seuls. Sans "
                "eau et sans dioxygène réunis en même temps, il ne peut "
                "y avoir aucune corrosion, quelle que soit par ailleurs "
                "la température."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
