"""
scenes/Chimie_CorrosionProtectionMetaux_06.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 06.

§ 6. De la corrosion à la rouille : étapes et équation-bilan globale.
Étape 1 (Fe2+ + 2OH- → Fe(OH)2, précipité vert pâle), étape 2 (4Fe(OH)2 +
O2 + 2H2O → 4Fe(OH)3, brun), étape 3 (déshydratation en rouille Fe2O3,
xH2O). Équation-bilan globale 4Fe + 3O2 + 2xH2O → 2Fe2O3.xH2O. Exemple
résolu 1 : établir l'équation de la première étape en détail, avec
vérification de la conservation des charges et des éléments.
Source : 1ereC/Chimie.pdf, chapitre 15, page 148.
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
    ORANGE,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class DeLaCorrosionALaRouille(NotionScene):
    def construct(self):
        titre = scene_title("15.6 De la corrosion à la rouille : étapes et bilan")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Les ions Fe²⁺ et OH⁻ produits par la micropile ne "
                "forment pas directement la rouille : trois étapes "
                "successives, dans la goutte d'eau puis à l'air, "
                "conduisent au produit final brun roux.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les ions fer deux plus et les ions hydroxyde produits "
                "par la micropile de corrosion ne forment pas "
                "directement la rouille. Trois étapes successives, dans "
                "la goutte d'eau puis au contact de l'air, conduisent au "
                "produit final brun roux que l'on observe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : les trois étapes -------------------------------------
        entete_etapes = Text("Les trois étapes de la formation de la rouille", font_size=20, color=YELLOW, weight="BOLD")
        entete_etapes.next_to(titre, DOWN, buff=0.3)

        etape1_txt = Text("Étape 1 : précipité vert pâle", font_size=17, color=WHITE)
        etape1_eq = MathTex(r"Fe^{2+} + 2OH^{-} \longrightarrow Fe(OH)_2", font_size=24)
        etape1 = VGroup(etape1_txt, etape1_eq).arrange(DOWN, buff=0.15)

        etape2_txt = Text("Étape 2 : oxydation à l'air, précipité brun", font_size=17, color=WHITE)
        etape2_eq = MathTex(r"4Fe(OH)_2 + O_2 + 2H_2O \longrightarrow 4Fe(OH)_3", font_size=24)
        etape2 = VGroup(etape2_txt, etape2_eq).arrange(DOWN, buff=0.15)

        etape3_txt = Text("Étape 3 : déshydratation partielle en rouille", font_size=17, color=WHITE)
        etape3_eq = MathTex(r"2Fe(OH)_3 \longrightarrow Fe_2O_3, xH_2O + (3-x)H_2O", font_size=22)
        etape3 = VGroup(etape3_txt, etape3_eq).arrange(DOWN, buff=0.15)

        etapes = VGroup(etape1, etape2, etape3).arrange(DOWN, buff=0.35)
        etapes.next_to(entete_etapes, DOWN, buff=0.3)
        groupe_etapes = VGroup(entete_etapes, etapes)
        _fit(groupe_etapes, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Voici les trois étapes. Étape un : dans la goutte "
                "d'eau, les ions fer deux plus rencontrent les ions "
                "hydroxyde venus de la cathode, et précipitent en "
                "hydroxyde de fer deux, un solide vert pâle. Étape deux : "
                "ce précipité vert pâle est à son tour oxydé par le "
                "dioxygène de l'air, en présence d'eau, pour donner de "
                "l'hydroxyde de fer trois, un précipité brun. Étape "
                "trois : cet hydroxyde de fer trois se déshydrate "
                "partiellement pour former la rouille définitive, "
                "l'oxyde de fer trois hydraté."
            )
        ) as tracker:
            self.play(FadeIn(entete_etapes))
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_etapes))

        # --- Exemple traité : équation-bilan globale -----------------------------
        entete_bilan = Text("L'équation-bilan globale de la rouille", font_size=21, color=YELLOW, weight="BOLD")
        entete_bilan.next_to(titre, DOWN, buff=0.4)

        bilan = MathTex(
            r"4\,Fe + 3\,O_2 + 2x\,H_2O \;\longrightarrow\; 2\,Fe_2O_3, xH_2O",
            font_size=30, color=ORANGE,
        )
        bilan.next_to(entete_bilan, DOWN, buff=0.4)
        groupe_bilan = VGroup(entete_bilan, bilan)

        with self.voiceover(
            text=(
                "En combinant l'ensemble de ces étapes, on obtient "
                "l'équation-bilan globale de la corrosion humide du fer : "
                "quatre fer, plus trois dioxygène, plus deux x eau, "
                "donnent deux fois l'oxyde de fer trois hydraté. Cette "
                "équation résume, en une seule ligne, tout le mécanisme "
                "détaillé que nous venons de voir."
            )
        ) as tracker:
            self.play(FadeIn(entete_bilan))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_bilan))

        # --- À retenir : exemple résolu, vérification de l'étape 1 --------------
        exemple = example_box(
            VGroup(
                Text("Établir et vérifier l'équation de l'étape 1 :", font_size=20, weight="BOLD"),
                MathTex(r"Fe^{2+} + 2\,OH^{-} \longrightarrow Fe(OH)_2", font_size=24),
                Text("Charges : (+2) + 2×(−1) = 0 = charge de Fe(OH)2 ✓", font_size=18, color=GREEN),
                Text("Éléments : 1 Fe, 2 O, 2 H de chaque côté ✓", font_size=18, color=GREEN),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)
        _fit(exemple, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Vérifions en détail l'équation de la première étape. On "
                "part d'un ion fer deux plus et de deux ions hydroxyde, "
                "qui donnent l'hydroxyde de fer deux. Côté charges : plus "
                "deux, plus deux fois moins un, cela fait bien zéro, la "
                "charge du précipité neutre Fe-(O-H)-deux. Côté "
                "éléments : on retrouve bien un atome de fer, deux "
                "atomes d'oxygène et deux atomes d'hydrogène de chaque "
                "côté de la flèche. L'équation est équilibrée."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La rouille finale est Fe2O3, xH2O — un oxyde de fer "
                    "III hydraté, pas Fe(OH)2 ni Fe(OH)3, qui ne sont que "
                    "des intermédiaires de réaction, jamais le produit "
                    "final observé.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : la rouille finale que "
                "l'on observe est l'oxyde de fer trois hydraté, F-e-deux-"
                "O-trois, x H-deux-O. Les hydroxydes de fer deux et de "
                "fer trois ne sont que des intermédiaires de réaction, "
                "jamais le produit final réellement observé sur un objet "
                "rouillé."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
