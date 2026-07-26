"""
scenes/Chimie_Alcanes_10.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 10.

§ 7. Propriétés chimiques : introduction (paraffines, peu réactifs) +
§ 7.1 combustion complète (définition, équation-bilan générale avec
vérification de l'équilibrage), exemple résolu 5 (équilibrer la
combustion du butane), exemple résolu 6 (situation type SIR : formule
brute à partir de n(CO₂)/n(alcane)). Source : 1ereC/Chimie.pdf,
pages 21-22.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, definition_box, exercise_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class CombustionComplete(NotionScene):
    def construct(self):
        titre = scene_title("7. Propriétés chimiques : la combustion complète")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : les alcanes, des « paraffines » peu réactives -------------
        intro = Text(
            _wrap(
                "Les alcanes sont des molécules peu réactives à "
                "température ordinaire : leur ancien nom, « paraffines », "
                "vient du latin parum affinis, « peu d'affinité ». Ils "
                "ne réagissent pratiquement pas avec les acides, les "
                "bases ni les oxydants courants. Leurs deux grandes "
                "réactions sont la combustion et la substitution.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les alcanes sont des molécules peu réactives à "
                "température ordinaire : leur ancien nom, paraffines, "
                "vient du latin parum affinis, qui signifie peu "
                "d'affinité. Ils ne réagissent pratiquement pas avec les "
                "acides, les bases, ni les oxydants courants. Leurs deux "
                "grandes réactions sont la combustion et la substitution. "
                "Commençons par la combustion complète."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition + équation-bilan générale ----------------
        definition = definition_box(
            Text(
                _wrap(
                    "La combustion complète d'un alcane dans un excès de "
                    "dioxygène produit du dioxyde de carbone et de l'eau, "
                    "avec un important dégagement de chaleur (réaction "
                    "exothermique).",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La combustion complète d'un alcane dans un excès de "
                "dioxygène produit du dioxyde de carbone et de l'eau, "
                "avec un important dégagement de chaleur : c'est une "
                "réaction exothermique."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        equation_generale = property_box(
            MathTex(
                r"C_nH_{2n+2} + \dfrac{3n+1}{2}O_2 \rightarrow n\,CO_2 + (n+1)H_2O",
                font_size=30,
                color="#1A1A1A",
            ),
            box_width=11.5,
        )
        equation_generale.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'équation-bilan générale de la combustion complète "
                "s'écrit : C indice n, H indice deux n plus deux, plus "
                "trois n plus un, le tout divisé par deux, dioxygène, "
                "donne n dioxyde de carbone plus n plus un eau."
            )
        ) as tracker:
            self.play(FadeIn(equation_generale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation_generale))

        entete_verif = Text("Vérification de l'équilibrage", font_size=22, color=YELLOW, weight="BOLD")
        entete_verif.next_to(titre, DOWN, buff=0.4)

        verifs = VGroup(
            MathTex(r"\text{Carbone : } n = n \; \checkmark", font_size=25, color=WHITE),
            MathTex(r"\text{Hydrogène : } 2n+2 = 2(n+1) = 2n+2 \; \checkmark", font_size=25, color=WHITE),
            MathTex(r"\text{Oxygène : } 2\times\dfrac{3n+1}{2} = 3n+1 = 2n+(n+1) \; \checkmark", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        verifs.next_to(entete_verif, DOWN, buff=0.4)
        _fit(VGroup(entete_verif, verifs), entete_verif.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Vérifions l'équilibrage, élément par élément. Le "
                "carbone : n à gauche, n à droite, c'est bon. "
                "L'hydrogène : deux n plus deux à gauche, deux fois n "
                "plus un, soit deux n plus deux à droite, c'est bon. "
                "L'oxygène : deux fois trois n plus un sur deux, soit "
                "trois n plus un à gauche, contre deux n plus n plus un, "
                "soit aussi trois n plus un à droite. L'équation est bien "
                "équilibrée."
            )
        ) as tracker:
            self.play(FadeIn(entete_verif))
            self.play(Write(verifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_verif), FadeOut(verifs))

        # --- Exemple traité 1 : équilibrer la combustion du butane ---------------
        enonce5 = exercise_box(
            Text("Équilibrons la combustion complète du butane C₄H₁₀.", font_size=24),
            box_width=9.5,
        )
        enonce5.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : équilibrons la combustion complète du "
                "butane, C-4, H-10."
            )
        ) as tracker:
            self.play(FadeIn(enonce5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce5))

        resolution5 = corrige_box(
            VGroup(
                MathTex(r"n=4 \;\Rightarrow\; \dfrac{3n+1}{2} = \dfrac{13}{2}", font_size=27, color="#1A1A1A"),
                MathTex(r"C_4H_{10} + \dfrac{13}{2}O_2 \rightarrow 4\,CO_2 + 5\,H_2O", font_size=26, color="#1A1A1A"),
                Text("Coefficients entiers (×2) :", font_size=20),
                MathTex(r"2\,C_4H_{10} + 13\,O_2 \rightarrow 8\,CO_2 + 10\,H_2O", font_size=26, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=11.5,
        )
        resolution5.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avec n égal quatre, on a trois n plus un sur deux égal "
                "treize sur deux, d'où : butane plus treize sur deux "
                "dioxygène donne quatre dioxyde de carbone plus cinq eau. "
                "Si l'on préfère des coefficients entiers, on multiplie "
                "tout par deux : deux butane plus treize dioxygène donne "
                "huit dioxyde de carbone plus dix eau."
            )
        ) as tracker:
            self.play(FadeIn(resolution5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution5))

        # --- Exemple traité 2 : situation type SIR, formule brute par CO₂ ------
        enonce6 = exercise_box(
            Text(
                _wrap(
                    "La combustion complète de 0,2 mol d'un alcane A "
                    "produit 0,8 mol de dioxyde de carbone. Déterminons "
                    "la formule brute de A.",
                    width=42,
                ),
                font_size=22,
            ),
            box_width=9.5,
        )
        enonce6.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Second exemple, une situation type SIR : la combustion "
                "complète de zéro virgule deux mole d'un alcane A produit "
                "zéro virgule huit mole de dioxyde de carbone. "
                "Déterminons la formule brute de A."
            )
        ) as tracker:
            self.play(FadeIn(enonce6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce6))

        resolution6 = corrige_box(
            VGroup(
                MathTex(r"\dfrac{n(CO_2)}{n(A)} = n = \dfrac{0{,}8}{0{,}2} = 4", font_size=28, color="#1A1A1A"),
                Text("A a pour formule brute C₄H₁₀ (butane ou 2-méthylpropane).", font_size=22),
            ).arrange(DOWN, buff=0.4),
            box_width=10.5,
        )
        resolution6.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "D'après l'équation-bilan générale, une mole d'alcane "
                "donne n moles de dioxyde de carbone, donc n égale le "
                "rapport n de C-O-2 sur n de A, soit zéro virgule huit "
                "divisé par zéro virgule deux, égale quatre. L'alcane A a "
                "donc pour formule brute C-4, H-10 : c'est le butane, ou "
                "son isomère, le deux-méthylpropane."
            )
        ) as tracker:
            self.play(FadeIn(resolution6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution6))

        # --- Piège à éviter : coefficient fractionnaire n'est pas une erreur ---
        piege = warning_box(
            Text(
                _wrap(
                    "Dans l'équation de combustion, le coefficient "
                    "(3n+1)/2 peut être fractionnaire (ex. 13/2 pour le "
                    "butane) : ce n'est PAS une erreur. On peut multiplier "
                    "tous les coefficients par 2 pour n'avoir que des "
                    "entiers, mais jamais un seul coefficient isolé.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : dans l'équation de combustion, le "
                "coefficient trois n plus un sur deux peut être "
                "fractionnaire, comme treize sur deux pour le butane. Ce "
                "n'est pas une erreur. On peut multiplier tous les "
                "coefficients par deux pour n'obtenir que des entiers, "
                "mais jamais un seul coefficient isolé : l'équation "
                "doit rester cohérente dans son ensemble."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
