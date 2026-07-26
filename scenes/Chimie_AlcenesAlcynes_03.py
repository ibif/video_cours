"""
scenes/Chimie_AlcenesAlcynes_03.py — Chapitre 3 (1ereC, Chimie), scène 03.

Nomenclature des alcènes : méthode en 4 étapes (chaîne principale contenant
la double liaison, suffixe -ène + indice de position le plus petit possible,
numérotation donnant priorité à la double liaison, ramifications par ordre
alphabétique), avec deux exemples résolus (but-1-ène et 3-méthylpent-2-ène)
et un tableau des alcènes à connaître. Source : 1ereC/Chimie.pdf, ch.3, p.27.
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
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class NomenclatureAlcenes(NotionScene):
    def construct(self):
        titre = scene_title("3. Nomenclature des alcènes")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi une méthode dédiée --------------------------------
        intro = Text(
            _wrap(
                "Nommer un alcène ressemble à nommer un alcane, avec une "
                "différence essentielle : la double liaison doit toujours "
                "être repérée en priorité, aussi bien dans le choix de la "
                "chaîne principale que dans la numérotation.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nommer un alcène ressemble beaucoup à nommer un alcane, "
                "avec une différence essentielle : la double liaison doit "
                "toujours être repérée en priorité, aussi bien dans le "
                "choix de la chaîne principale que dans la numérotation "
                "des atomes de carbone."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : méthode en 4 étapes ---------------------
        methode = method_box(
            VGroup(
                Text("1. Repérer la chaîne principale : la plus longue chaîne", font_size=22),
                Text("   carbonée contenant obligatoirement la double liaison.", font_size=22),
                Text("2. Suffixe -ène, avec l'indice de position de la double", font_size=22),
                Text("   liaison le plus petit possible.", font_size=22),
                Text("3. Numéroter la chaîne en donnant la priorité à la", font_size=22),
                Text("   double liaison (indice le plus petit).", font_size=22),
                Text("4. Placer les ramifications par ordre alphabétique,", font_size=22),
                Text("   avec leur indice de position.", font_size=22),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.5,
        )
        methode.next_to(titre, DOWN, buff=0.35)
        _fit(methode, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "La méthode se déroule en quatre étapes. Un : repérer la "
                "chaîne principale, c'est-à-dire la plus longue chaîne "
                "carbonée contenant obligatoirement la double liaison. "
                "Deux : donner le suffixe ène, avec l'indice de position "
                "de la double liaison le plus petit possible. Trois : "
                "numéroter la chaîne en donnant la priorité à la double "
                "liaison, pour qu'elle porte l'indice le plus petit. "
                "Quatre : placer les ramifications éventuelles par ordre "
                "alphabétique, chacune avec son indice de position."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité 1 : but-1-ène ----------------------------------------
        exemple1 = example_box(
            VGroup(
                MathTex(r"CH_3-CH_2-CH=CH_2", font_size=30),
                MathTex(r"\underbrace{CH_3}_{4}-\underbrace{CH_2}_{3}-\underbrace{CH}_{2}=\underbrace{CH_2}_{1}", font_size=26),
                Text("Numérotation depuis la droite : la double liaison", font_size=20),
                Text("porte l'indice 1 le plus petit → but-1-ène", font_size=20, weight="BOLD"),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )
        exemple1.next_to(titre, DOWN, buff=0.35)
        _fit(exemple1, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Premier exemple résolu : la molécule C H trois, C H "
                "deux, C H, double liaison, C H deux. La chaîne compte "
                "quatre carbones : c'est un butène. En numérotant depuis "
                "la droite, la double liaison se retrouve entre les "
                "carbones un et deux, ce qui donne l'indice le plus "
                "petit possible, un. Le nom de cette molécule est donc "
                "but-un-ène."
            )
        ) as tracker:
            self.play(FadeIn(exemple1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple1))

        # --- Exemple traité 2 : 3-méthylpent-2-ène -------------------------------
        exemple2 = example_box(
            VGroup(
                MathTex(r"CH_3-CH=C(CH_3)-CH_2-CH_3", font_size=28),
                Text("Chaîne principale : 5 carbones (pentène)", font_size=20),
                Text("Double liaison en position 2 ; ramification méthyle", font_size=20),
                Text("en position 3 → 3-méthylpent-2-ène", font_size=20, weight="BOLD"),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )
        exemple2.next_to(titre, DOWN, buff=0.35)
        _fit(exemple2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Second exemple, un peu plus complexe : C H trois, "
                "double liaison C, portant un groupe méthyle, C H deux, "
                "C H trois. La chaîne principale la plus longue contenant "
                "la double liaison compte cinq carbones : c'est un "
                "pentène. En numérotant pour donner la priorité à la "
                "double liaison, celle-ci se retrouve en position deux, "
                "et le groupe méthyle en position trois. Le nom complet "
                "est donc trois-méthylpent-deux-ène."
            )
        ) as tracker:
            self.play(FadeIn(exemple2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple2))

        # --- À retenir : tableau des alcènes à connaître -------------------------
        entete = Text("Les premiers alcènes à connaître", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        tableau = VGroup(
            MathTex(r"C_2H_4 \; : \; \text{éthène (éthylène)}", font_size=26),
            MathTex(r"C_3H_6 \; : \; \text{propène}", font_size=26),
            MathTex(r"C_4H_8 \; : \; \text{but-1-ène / but-2-ène}", font_size=26),
            MathTex(r"C_5H_{10} \; : \; \text{pent-1-ène...}", font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        tableau.next_to(entete, DOWN, buff=0.4)
        _fit(tableau, entete.get_bottom()[1] - 0.4)

        groupe = VGroup(entete, tableau)

        with self.voiceover(
            text=(
                "Retenons les premiers alcènes de la série : C deux H "
                "quatre, l'éthène, aussi appelé éthylène ; C trois H six, "
                "le propène ; C quatre H huit, qui donne deux alcènes "
                "possibles, le but-un-ène et le but-deux-ène ; et C cinq "
                "H dix, dont le pent-un-ène. Ces noms serviront de base à "
                "toute la nomenclature organique."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(titre))
