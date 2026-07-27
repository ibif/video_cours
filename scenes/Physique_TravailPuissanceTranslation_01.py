"""
scenes/Physique_TravailPuissanceTranslation_01.py — Chapitre 1 « Travail et
puissance dans le cas d'un mouvement de translation » (1ereC, Physique),
scène 01.

§ Notion de travail d'une force constante : une force ne « travaille » que
si son point d'application se déplace et qu'elle possède une composante le
long de ce déplacement. Définition W_AB(F⃗) = F⃗·AB⃗ = F×AB×cos(α), unités
(N, m, J avec 1 J = 1 N × 1 m). Remarques : grandeur algébrique, dépend de
F, AB et α, nul si AB=0.
Source : 1ereC/Physique.pdf, chapitre 1, pages 4-12.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    YELLOW,
    Arc,
    FadeIn,
    FadeOut,
    MathTex,
    Square,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


FORCE_COLOR = "#DE7C1F"
DEPLACEMENT_COLOR = "#288073"


class TravailForceConstanteDefinition(NotionScene):
    def construct(self):
        titre = scene_title("Travail d'une force constante — définition")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation + figure ------------------------------------
        point_a = LEFT * 3 + DOWN * 0.5
        point_b = RIGHT * 1.5 + DOWN * 0.5
        objet = Square(side_length=0.7, color="#FFFFFF", fill_color="#3A3A3A", fill_opacity=0.9)
        objet.move_to(point_a)
        deplacement = Vector(point_b - point_a, color=DEPLACEMENT_COLOR)
        deplacement.shift(point_a)
        label_deplacement = MathTex(r"\overrightarrow{AB}", font_size=26, color=DEPLACEMENT_COLOR)
        label_deplacement.next_to(deplacement, DOWN, buff=0.15)

        force = Vector([1.6 * 0.766, 1.6 * 0.643, 0], color=FORCE_COLOR)
        force.shift(point_a)
        label_force = MathTex(r"\vec{F}", font_size=28, color=FORCE_COLOR)
        label_force.next_to(force.get_end(), UP, buff=0.1)

        arc_alpha = Arc(radius=0.7, start_angle=0, angle=0.7, color="#FFFFFF", stroke_width=2)
        arc_alpha.shift(point_a)
        label_alpha = MathTex(r"\alpha", font_size=24, color="#FFFFFF")
        label_alpha.move_to(point_a + [0.9 * 0.9, 0.9 * 0.32, 0])

        label_a = MathTex("A", font_size=26).next_to(point_a, DOWN + LEFT, buff=0.15)
        label_b = MathTex("B", font_size=26).next_to(point_b, DOWN + RIGHT, buff=0.15)

        figure = VGroup(
            objet, deplacement, label_deplacement, force, label_force,
            arc_alpha, label_alpha, label_a, label_b,
        )
        figure.move_to(ORIGIN).shift(DOWN * 0.3)

        mise_en_situation = Text(
            _wrap(
                "Une force ne « travaille » que si son point d'application "
                "se déplace, et seulement pour la partie de la force "
                "dirigée le long de ce déplacement.",
                width=54,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "En physique, une force ne travaille que si son point "
                "d'application se déplace réellement, et seulement pour la "
                "partie de cette force qui est dirigée le long du "
                "déplacement. Un ouvrier qui pousse de toutes ses forces sur "
                "un mur qui ne bouge pas ne fournit, au sens physique, aucun "
                "travail : rien ne se déplace. Regardons un objet qui se "
                "déplace du point A au point B, sous l'action d'une force F "
                "vecteur, qui fait un angle alpha avec ce déplacement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(figure))

        # --- Raisonnement : définition et unités ------------------------------------
        definition = definition_box(
            VGroup(
                Text("Travail d'une force constante", font_size=24, weight="BOLD"),
                MathTex(
                    r"W_{AB}(\vec{F}) = \vec{F}\cdot\overrightarrow{AB} = F \times AB \times \cos(\alpha)",
                    font_size=28,
                ),
                Text(
                    _wrap("α est l'angle entre la force F⃗ et le déplacement AB⃗.", width=48),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le travail de la force F vecteur, entre les points A et B, "
                "noté W indice A-B de F vecteur, est défini comme le produit "
                "scalaire de F vecteur par le vecteur déplacement A-B. Il "
                "s'exprime aussi F fois A-B fois cosinus de alpha, où alpha "
                "est l'angle entre la force et le déplacement."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        unites = definition_box(
            VGroup(
                Text("Unités", font_size=24, weight="BOLD"),
                MathTex(r"F \text{ en newton (N)}, \quad AB \text{ en mètre (m)}", font_size=26),
                MathTex(r"W \text{ en joule (J)} \ : \ 1\,J = 1\,N \times 1\,m", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        unites.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les unités doivent être cohérentes : la force s'exprime en "
                "newtons, la distance en mètres, et le travail obtenu "
                "s'exprime alors en joules, l'unité d'énergie. Un joule "
                "correspond exactement au travail d'une force d'un newton "
                "dont le point d'application se déplace d'un mètre dans sa "
                "propre direction."
            )
        ) as tracker:
            self.play(FadeIn(unites))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(unites))

        # --- Exemple traité ----------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text(
                    "Une force F = 50 N, colinéaire et de même sens que le",
                    font_size=22,
                ),
                Text("déplacement AB = 4 m (α = 0°).", font_size=22),
                MathTex(r"W_{AB}(\vec{F}) = 50 \times 4 \times \cos(0°) = 200\ J", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Prenons un exemple simple : une force de cinquante newtons, "
                "exactement colinéaire et de même sens que le déplacement de "
                "quatre mètres, donc avec un angle alpha nul. Le cosinus de "
                "zéro degré valant un, le travail vaut simplement cinquante "
                "fois quatre, soit deux cents joules."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                MathTex(r"W_{AB}(\vec{F}) = F \times AB \times \cos(\alpha)", font_size=28),
                Text(
                    _wrap(
                        "Le travail est une grandeur algébrique (positive, "
                        "négative ou nulle) : elle dépend de F, de AB et de "
                        "l'angle α. Il est nul si le point d'application ne "
                        "se déplace pas (AB = 0).",
                        width=54,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : le travail d'une force constante est une "
                "grandeur algébrique, qui peut être positive, négative, ou "
                "nulle. Il dépend de trois éléments : l'intensité de la "
                "force F, la longueur du déplacement A-B, et l'angle alpha "
                "entre les deux. En particulier, il est toujours nul si le "
                "point d'application de la force ne se déplace pas."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter -------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne jamais oublier le cosinus de α : W n'est PAS "
                    "simplement F×AB, sauf si la force est colinéaire au "
                    "déplacement (α = 0°). Une force appliquée sur un objet "
                    "immobile ne travaille jamais, même si elle est très "
                    "intense.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à deux pièges fréquents. D'abord, ne jamais "
                "oublier le cosinus de alpha dans la formule : le travail "
                "n'est égal au simple produit F fois A-B que lorsque la "
                "force est parfaitement colinéaire au déplacement. Ensuite, "
                "une force appliquée sur un objet qui reste immobile ne "
                "travaille jamais, quelle que soit son intensité."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
