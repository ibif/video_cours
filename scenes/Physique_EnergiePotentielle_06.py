"""
scenes/Physique_EnergiePotentielle_06.py — Chapitre 4 « Énergie potentielle »
(1ereC, Physique), scène 06.

Définition et expression de l'énergie potentielle élastique : établissement
via le théorème de l'énergie cinétique sur un solide relié à un ressort
horizontal (poids et réaction normale à travail nul), définition
Epe = ½kx² (référence : ressort non déformé, x=0), remarques (toujours
positive, symétrie étirement/compression), variation ΔEpe = -W_{A→B}(T⃗)
avec théorème, exemple résolu (fusil à flèche).
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


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


class DefinitionEpe(NotionScene):
    def construct(self):
        titre = scene_title("Énergie potentielle élastique")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : établissement --------------------------------------------------
        mur = Rectangle(width=0.3, height=1.0, color=WHITE, fill_color=WHITE, fill_opacity=1.0)
        mur.move_to(LEFT * 5.0)
        solide = Rectangle(width=0.6, height=0.6, color=YELLOW, fill_color=YELLOW, fill_opacity=1.0)
        solide.move_to(LEFT * 2.0)
        ressort = _spring(mur.get_right(), solide.get_left())
        table = Rectangle(width=6.5, height=0.05, color=WHITE, fill_color=WHITE, fill_opacity=1.0)
        table.next_to(VGroup(mur, solide), DOWN, buff=0)

        schema = VGroup(table, mur, ressort, solide)
        schema.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Considérons un solide posé sur une table horizontale sans "
                "frottement, relié à un ressort. Sur ce solide, deux forces "
                "verticales se compensent exactement : le poids, et la "
                "réaction normale de la table. Ni l'un ni l'autre ne "
                "travaille, puisqu'ils sont perpendiculaires au déplacement."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        etablissement = VGroup(
            Text("Théorème de l'énergie cinétique (poids et réaction : travail nul) :", font_size=21),
            MathTex(r"E_c(B) - E_c(A) = W_{A \to B}(\vec{T})", font_size=27),
            MathTex(
                r"E_c(B) - E_c(A) = \tfrac{1}{2}kx_A^2 - \tfrac{1}{2}kx_B^2",
                font_size=27,
            ),
            MathTex(
                r"E_c(B) + \tfrac{1}{2}kx_B^2 = E_c(A) + \tfrac{1}{2}kx_A^2",
                font_size=28,
                color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.3)
        etablissement.next_to(schema, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Seule la tension du ressort travaille : le théorème de "
                "l'énergie cinétique donne donc Ec de B moins Ec de A égale "
                "le travail de la tension, c'est-à-dire un demi k x indice "
                "A carré, moins un demi k x indice B carré. En regroupant "
                "les termes en A et les termes en B, on obtient, exactement "
                "comme pour la pesanteur, une quantité conservée : Ec plus "
                "un demi k x carré."
            )
        ) as tracker:
            self.play(Write(etablissement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(etablissement))

        # --- Définition -----------------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Énergie potentielle élastique (référence : ressort non déformé, x=0) :", font_size=21),
                MathTex(r"E_{pe} = \dfrac{1}{2}kx^2", font_size=34),
            ).arrange(DOWN, buff=0.3),
            box_width=10.8,
        )
        definition.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le terme un demi k x carré, associé à la déformation du "
                "ressort, est l'énergie potentielle élastique, notée Epe. "
                "Elle vaut un demi k x carré, la référence étant prise "
                "lorsque le ressort n'est pas déformé, c'est-à-dire pour x "
                "égal à zéro."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Remarques -------------------------------------------------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Epe est toujours positive ou nulle (elle dépend de "
                    "x², jamais de son signe) : elle a la même valeur pour "
                    "un étirement x ou une compression -x de même "
                    "intensité (symétrie étirement/compression).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        remarque.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Deux remarques. D'abord, Epe est toujours positive ou "
                "nulle, puisqu'elle dépend de x au carré, jamais du signe "
                "de x. Ensuite, cela entraîne une symétrie parfaite entre "
                "étirement et compression : un ressort étiré de x et un "
                "ressort comprimé de moins x stockent exactement la même "
                "énergie potentielle élastique."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Variation de Epe --------------------------------------------------------------
        variation = VGroup(
            MathTex(
                r"\Delta E_{pe} = E_{pe}(B) - E_{pe}(A) = -W_{A \to B}(\vec{T})",
                font_size=29,
            ),
            MathTex(
                r"\Delta E_{pe} = \tfrac{1}{2}kx_B^2 - \tfrac{1}{2}kx_A^2",
                font_size=28,
            ),
        ).arrange(DOWN, buff=0.4)
        variation.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Comme pour l'énergie potentielle de pesanteur, on montre "
                "de la même façon que la variation de l'énergie "
                "potentielle élastique entre A et B est égale à l'opposé "
                "du travail de la tension, soit un demi k x indice B "
                "carré, moins un demi k x indice A carré."
            )
        ) as tracker:
            self.play(Write(variation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(variation))

        # --- Exemple résolu : fusil à flèche -----------------------------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu : un fusil à flèche a un ressort de "
                "longueur à vide ℓ0=10 cm et de raideur k=200 N/m. On le "
                "comprime jusqu'à ℓ=6 cm. Calculer Epe emmagasinée.",
                width=54,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Exemple résolu. Un fusil à flèche jouet possède un "
                "ressort de longueur à vide 10 centimètres, et de raideur "
                "200 newtons par mètre. On le comprime jusqu'à une longueur "
                "de 6 centimètres. Calculons l'énergie potentielle "
                "élastique emmagasinée."
            )
        ) as tracker:
            self.play(Write(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul = example_box(
            VGroup(
                MathTex(r"x = \ell - \ell_0 = 6 - 10 = -4\ \text{cm} = -0{,}04\ \text{m}", font_size=25),
                MathTex(
                    r"E_{pe} = \dfrac{1}{2}kx^2 = \dfrac{1}{2}\times 200 \times (0{,}04)^2 = 0{,}16\ \text{J}",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=11.0,
        )
        calcul.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'allongement algébrique vaut x égale ℓ moins ℓ zéro, "
                "soit 6 moins 10, c'est-à-dire moins 4 centimètres, ou "
                "moins 0 virgule 04 mètre. L'énergie potentielle élastique "
                "vaut alors un demi fois 200 fois 0 virgule 04 au carré, "
                "soit 0 virgule 16 joule."
            )
        ) as tracker:
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul))

        detente = example_box(
            VGroup(
                Text("À la détente, le ressort revient à ℓ0 (x=0) :", font_size=21),
                MathTex(
                    r"W_{\text{tension}} = -\Delta E_{pe} = -(0 - 0{,}16) = 0{,}16\ \text{J}",
                    font_size=25,
                ),
                Text("Travail moteur : il propulse la flèche.", font_size=21, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
            box_width=11.2,
        )
        detente.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Lors de la détente, le ressort revient à sa longueur à "
                "vide, donc x final vaut zéro. Le travail de la tension "
                "vaut alors moins delta Epe, soit moins de zéro moins 0 "
                "virgule 16, c'est-à-dire plus 0 virgule 16 joule. Ce "
                "travail est moteur : c'est lui qui propulse la flèche. On "
                "vérifie bien la relation W égale moins delta Epe."
            )
        ) as tracker:
            self.play(FadeIn(detente))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(detente))

        # --- À retenir --------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Epe = ½kx² (référence : ressort non déformé), "
                    "toujours positive, symétrique en x. "
                    "ΔEpe=-W(tension). À la détente, le ressort restitue "
                    "son énergie potentielle en travail moteur.",
                    width=56,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : l'énergie potentielle élastique vaut un demi "
                "k x carré, la référence étant le ressort non déformé. "
                "Elle est toujours positive, et symétrique en x. Sa "
                "variation vaut moins le travail de la tension. À la "
                "détente, le ressort restitue l'énergie potentielle "
                "élastique emmagasinée sous forme de travail moteur."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
