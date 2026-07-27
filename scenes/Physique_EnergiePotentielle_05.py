"""
scenes/Physique_EnergiePotentielle_05.py — Chapitre 4 « Énergie potentielle »
(1ereC, Physique), scène 05.

Énergie potentielle élastique : rappel de la tension d'un ressort (loi de
Hooke T=k|x|, x=ℓ-ℓ₀ allongement algébrique) et établissement du travail de
la tension entre A et B, W_{A→B}(T⃗) = ½kx_A² - ½kx_B² (intégration
δW=-kx dx). Propriété : ce travail ne dépend que des allongements initial
et final.
Source : 1ereC/Physique.pdf, chapitre 4, pages 34-42.
"""

import textwrap

import numpy as np
from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    VMobject,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _spring(start, end, coils=8, amplitude=0.22, color=ORANGE):
    """Ressort dessiné comme une ligne en zigzag entre deux points."""
    start = np.array(start, dtype=float)
    end = np.array(end, dtype=float)
    direction = end - start
    length = np.linalg.norm(direction)
    unit = direction / length if length > 0 else np.array([1.0, 0.0, 0.0])
    normal = np.array([-unit[1], unit[0], 0.0])
    n = coils * 2
    points = [start]
    for i in range(1, n):
        t = i / n
        offset = amplitude * (1 if i % 2 == 1 else -1)
        points.append(start + unit * length * t + normal * offset)
    points.append(end)
    spring = VMobject(color=color, stroke_width=3)
    spring.set_points_as_corners(points)
    return spring


class TravailTensionRessort(NotionScene):
    def construct(self):
        titre = scene_title("Travail de la tension d'un ressort")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : rappel de la loi de Hooke -----------------------------------
        mur = Rectangle(width=0.3, height=1.2, color=WHITE, fill_color=WHITE, fill_opacity=1.0)
        mur.move_to(LEFT * 5.2)
        solide = Rectangle(width=0.7, height=0.7, color=YELLOW, fill_color=YELLOW, fill_opacity=1.0)
        solide.move_to(LEFT * 1.5)
        ressort = _spring(mur.get_right(), solide.get_left())

        long_naturelle = MathTex(r"\ell_0", font_size=26).next_to(ressort, UP, buff=0.5)

        schema = VGroup(mur, ressort, solide, long_naturelle)
        schema.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Rappelons la loi de Hooke. Un ressort de longueur à vide "
                "ℓ zéro est fixé à un mur, et relié à un solide. Lorsqu'on "
                "étire ou comprime le ressort, il exerce sur le solide une "
                "force de rappel, appelée tension."
            )
        ) as tracker:
            self.play(FadeIn(mur), Write(ressort), FadeIn(solide), Write(long_naturelle))
            self.wait(tracker.get_remaining_duration())

        solide_etire = solide.copy().shift(RIGHT * 1.3)
        ressort_etire = _spring(mur.get_right(), solide_etire.get_left())
        allongement = MathTex(r"x = \ell - \ell_0", font_size=26, color=YELLOW)
        allongement.next_to(ressort_etire, UP, buff=0.5)

        with self.voiceover(
            text=(
                "On étire le ressort jusqu'à la longueur ℓ. On appelle "
                "allongement algébrique la quantité x, égale à ℓ moins ℓ "
                "zéro : x est positif si le ressort est étiré, négatif "
                "s'il est comprimé."
            )
        ) as tracker:
            self.play(FadeOut(ressort), FadeOut(long_naturelle))
            self.play(solide.animate.move_to(solide_etire.get_center()), Write(ressort_etire))
            self.play(Write(allongement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mur), FadeOut(solide), FadeOut(ressort_etire), FadeOut(allongement))

        loi_hooke = definition_box(
            MathTex(r"T = k \, |x|", font_size=34),
            box_width=6.5,
        )
        loi_hooke.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "La loi de Hooke donne l'intensité de cette tension : T "
                "égale k fois la valeur absolue de x, où k est la raideur "
                "du ressort, exprimée en newtons par mètre."
            )
        ) as tracker:
            self.play(FadeIn(loi_hooke))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi_hooke))

        # --- Raisonnement : établissement du travail de la tension -------------------
        question = Text(
            _wrap(
                "La tension n'est pas constante : elle dépend de x. Quel "
                "est alors le travail de la tension quand le ressort passe "
                "de l'allongement xA à l'allongement xB ?",
                width=54,
            ),
            font_size=24,
        )
        question.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Contrairement au poids, la tension du ressort n'est pas "
                "une force constante : son intensité dépend de "
                "l'allongement x, qui varie pendant le mouvement. Quel est "
                "alors le travail de cette tension, lorsque le ressort "
                "passe d'un allongement x indice A à un allongement x "
                "indice B ?"
            )
        ) as tracker:
            self.play(Write(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        etape1 = MathTex(r"\vec{T} = -kx\,\vec{u}_x \quad \Rightarrow \quad \delta W = \vec{T}\cdot d\vec{\ell} = -kx\,dx", font_size=27)
        etape2 = MathTex(
            r"W_{A \to B}(\vec{T}) = \int_{x_A}^{x_B} -kx\,dx = \left[-\dfrac{1}{2}kx^2\right]_{x_A}^{x_B}",
            font_size=27,
        )
        etape3 = MathTex(
            r"W_{A \to B}(\vec{T}) = \dfrac{1}{2}kx_A^2 - \dfrac{1}{2}kx_B^2",
            font_size=30,
            color=YELLOW,
        )
        demo = VGroup(etape1, etape2, etape3).arrange(DOWN, buff=0.45)
        demo.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Établissons ce travail. La tension s'écrit T vecteur "
                "égale moins k x fois le vecteur unitaire de l'axe. Le "
                "travail élémentaire lors d'un petit déplacement d ℓ vaut "
                "donc moins k x d x. En intégrant entre x indice A et x "
                "indice B, on obtient le travail total de la tension : "
                "menant, après calcul de la primitive, à un demi k x "
                "indice A carré, moins un demi k x indice B carré."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Propriété -----------------------------------------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Le travail de la tension entre A et B ne dépend que "
                    "des allongements initial xA et final xB : il ne "
                    "dépend pas du chemin suivi entre les deux états.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.2,
        )
        propriete.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Propriété essentielle : ce travail de la tension ne "
                "dépend que des allongements initial et final, x indice A "
                "et x indice B. Il ne dépend absolument pas de la façon "
                "dont on est passé de l'un à l'autre."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Loi de Hooke : T=k|x|, avec x=ℓ-ℓ0 (allongement "
                    "algébrique). Travail de la tension entre A et B : "
                    "W(T)=½kxA²-½kxB². Ce travail ne dépend que des états "
                    "initial et final.",
                    width=56,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : la loi de Hooke donne T égale k fois la "
                "valeur absolue de x, avec x égal à ℓ moins ℓ zéro. Le "
                "travail de la tension entre A et B vaut un demi k x "
                "indice A carré, moins un demi k x indice B carré, et ne "
                "dépend que des allongements initial et final. Cette "
                "propriété va nous permettre, dans la scène suivante, de "
                "définir l'énergie potentielle élastique."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
