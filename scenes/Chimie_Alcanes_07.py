"""
scenes/Chimie_Alcanes_07.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 07.

§ 5. Isomérie de chaîne : définition, exemple résolu 3 (C₄H₁₀ : butane et
2-méthylpropane), exemple résolu 4 (C₅H₁₂ : les 3 isomères), tableau du
nombre d'isomères croissant (C₄ à C₁₀), propriété « isomères = corps
différents ». Source : 1ereC/Chimie.pdf, pages 19-20.
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
    MathTex,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class IsomerieDeChaine(NotionScene):
    def construct(self):
        titre = scene_title("5. L'isomérie de chaîne")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition des isomères de chaîne --------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Des isomères de chaîne sont des composés qui "
                    "possèdent la même formule brute mais des formules "
                    "semi-développées différentes (des squelettes "
                    "carbonés différents).",
                    width=48,
                ),
                font_size=24,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Des isomères de chaîne sont des composés qui possèdent la "
                "même formule brute, mais des formules semi-développées "
                "différentes, c'est-à-dire des squelettes carbonés "
                "différents."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement + exemple traité : C₄H₁₀, deux isomères ---------------
        entete_c4 = MathTex(r"C_4H_{10} \; : \; 2\ \text{isomères de chaîne}", font_size=30, color=YELLOW)
        entete_c4.next_to(titre, DOWN, buff=0.4)

        isomeres_c4 = VGroup(
            VGroup(
                MathTex(r"CH_3-CH_2-CH_2-CH_3", font_size=26, color=WHITE),
                Text("butane (linéaire)", font_size=18, color=WHITE),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                MathTex(r"CH_3-CH(CH_3)-CH_3", font_size=26, color=WHITE),
                Text("2-méthylpropane (ramifié)", font_size=18, color=WHITE),
            ).arrange(DOWN, buff=0.2),
        ).arrange(DOWN, buff=0.5)
        isomeres_c4.next_to(entete_c4, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Premier exemple : l'alcane de formule brute C-4, H-10 "
                "possède deux isomères de chaîne. D'une part, C-H-3, "
                "C-H-2, C-H-2, C-H-3, le butane, à chaîne linéaire. "
                "D'autre part, C-H-3, C-H parenthèse C-H-3 fermée "
                "parenthèse, C-H-3, le deux-méthylpropane, à chaîne "
                "ramifiée."
            )
        ) as tracker:
            self.play(FadeIn(entete_c4))
            self.play(Write(isomeres_c4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_c4), FadeOut(isomeres_c4))

        # --- Exemple traité : C₅H₁₂, trois isomères -------------------------------
        entete_c5 = MathTex(r"C_5H_{12} \; : \; 3\ \text{isomères de chaîne}", font_size=28, color=YELLOW)
        entete_c5.next_to(titre, DOWN, buff=0.35)

        isomeres_c5 = VGroup(
            VGroup(
                MathTex(r"CH_3-CH_2-CH_2-CH_2-CH_3", font_size=22, color=WHITE),
                Text("pentane", font_size=16, color=WHITE),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                MathTex(r"CH_3-CH(CH_3)-CH_2-CH_3", font_size=22, color=WHITE),
                Text("2-méthylbutane", font_size=16, color=WHITE),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                MathTex(r"C(CH_3)_4", font_size=22, color=WHITE),
                Text("2,2-diméthylpropane", font_size=16, color=WHITE),
            ).arrange(DOWN, buff=0.15),
        ).arrange(DOWN, buff=0.35)
        isomeres_c5.next_to(entete_c5, DOWN, buff=0.4)
        _fit(VGroup(entete_c5, isomeres_c5), entete_c5.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Second exemple : l'alcane C-5, H-12 possède trois "
                "isomères de chaîne. Le pentane, à chaîne linéaire ; le "
                "deux-méthylbutane, avec un méthyle en position deux ; et "
                "le deux-virgule-deux-diméthylpropane, où deux méthyles "
                "occupent tous deux la position deux d'une chaîne de "
                "seulement trois carbones."
            )
        ) as tracker:
            self.play(FadeIn(entete_c5))
            self.play(Write(isomeres_c5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_c5), FadeOut(isomeres_c5))

        # --- Exemple traité : tableau du nombre d'isomères croissant ------------
        entete_tab = Text("Le nombre d'isomères croît très vite avec n", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["C₄H₁₀", "C₅H₁₂", "C₆H₁₄", "C₇H₁₆", "C₈H₁₈", "C₁₀H₂₂"],
            ["2", "3", "5", "9", "18", "75"],
        ]
        table = Table(
            rows,
            row_labels=[Text("formule brute", font_size=15), Text("isomères", font_size=15)],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 18},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.3,
            h_buff=0.4,
        )
        table.get_entries().set_color(WHITE)
        table.get_row_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(entete_tab, DOWN, buff=0.35)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = table.get_top()[1] - _bas_visible
        if table.height > _hauteur_dispo:
            table.scale(_hauteur_dispo / table.height, about_point=table.get_top())
        _largeur_dispo = config.frame_width - 0.6
        if table.width > _largeur_dispo:
            table.scale(_largeur_dispo / table.width, about_point=table.get_top())
        table.next_to(entete_tab, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le nombre d'isomères de chaîne croît très vite avec le "
                "nombre de carbones : deux pour C-4, H-10 ; trois pour "
                "C-5, H-12 ; cinq pour C-6, H-14 ; neuf pour C-7, H-16 ; "
                "dix-huit pour C-8, H-18 ; et déjà soixante-quinze pour "
                "C-10, H-22 !"
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table))

        # --- À retenir : propriété des isomères ----------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Des isomères de chaîne sont des corps DIFFÉRENTS : "
                    "ils ont des propriétés physiques différentes (points "
                    "d'ébullition, densités…). D'où l'importance d'une "
                    "nomenclature précise.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ceci : des isomères de chaîne sont des corps "
                "différents. Ils ont des propriétés physiques "
                "différentes, comme le point d'ébullition ou la densité. "
                "C'est précisément pourquoi une nomenclature précise est "
                "indispensable."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : ne pas compter deux fois le même isomère ----------
        piege = example_box(
            Text(
                _wrap(
                    "En cherchant tous les isomères, un même squelette "
                    "peut apparaître « retourné » ou « lu à l'envers » "
                    "dans le dessin : ce n'est PAS un nouvel isomère. "
                    "Nommez chaque squelette trouvé : si deux dessins "
                    "reçoivent le même nom, c'est qu'ils sont identiques.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention en cherchant tous les isomères d'une formule "
                "brute : un même squelette peut apparaître retourné, ou "
                "lu à l'envers, dans le dessin — ce n'est pas un nouvel "
                "isomère. La méthode sûre consiste à nommer chaque "
                "squelette trouvé : si deux dessins reçoivent le même "
                "nom, c'est qu'ils représentent la même molécule."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
