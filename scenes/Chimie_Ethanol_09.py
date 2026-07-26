"""
scenes/Chimie_Ethanol_09.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 09.

§ 6. Tests de reconnaissance des alcools + éthylotest. Tableau des tests
(KMnO₄ acidifié → décoloration si oxydable ; DNPH → composé carbonylé ;
réactif de Schiff → aldéhyde uniquement ; papier pH → acide). Stratégie
d'identification de la classe en 3 étapes (pas de décoloration=tertiaire ;
décoloration+Schiff positif=primaire ; décoloration+Schiff négatif=
secondaire). Principe de l'éthylotest (dichromate orange → chrome III
vert).
Source : 1ereC/Chimie.pdf, chapitre 7, page 73.
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
from shapes.boxes import scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class TestsReconnaissanceAlcoolsEthylotest(NotionScene):
    def construct(self):
        titre = scene_title("7.6 Tests de reconnaissance des alcools")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi des tests de reconnaissance ? ----------------------
        intro = Text(
            _wrap(
                "Pour reconnaître un alcool et déterminer sa classe, on "
                "réalise une oxydation ménagée, puis on caractérise le "
                "produit formé à l'aide de réactifs spécifiques.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour reconnaître un alcool et déterminer sa classe, on "
                "réalise une oxydation ménagée, puis on caractérise le "
                "produit formé à l'aide de réactifs spécifiques. "
                "Découvrons ces tests de reconnaissance."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : tableau des tests --------------------------------------
        entete_tab = Text("Réactifs et tests de reconnaissance", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["KMnO₄ acidifié (violet)", "alcool oxydable\n(primaire/secondaire)", "décoloration : le violet\ndisparaît"],
            ["DNPH", "composé carbonylé\n(aldéhyde/cétone)", "précipité\njaune-orangé"],
            ["Réactif de Schiff", "aldéhyde uniquement", "coloration\nrose-violette"],
            ["Papier pH", "acide carboxylique", "vire au rouge\n(pH<7)"],
        ]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=14, weight="BOLD") for c in ["Réactif / test", "Espèce recherchée", "Observation positive"]],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 13, "line_spacing": 0.8},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.2,
            h_buff=0.28,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(entete_tab, DOWN, buff=0.3)
        _fit(table, entete_tab.get_bottom()[1] - 0.3)
        table.next_to(entete_tab, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici les principaux réactifs. Le permanganate de "
                "potassium acidifié, violet, recherche un alcool "
                "oxydable, primaire ou secondaire : sa décoloration, le "
                "violet qui disparaît, est le signe positif. La D-N-P-H "
                "recherche un composé carbonylé, aldéhyde ou cétone : un "
                "précipité jaune-orangé apparaît. Le réactif de Schiff ne "
                "recherche que l'aldéhyde : il donne une coloration "
                "rose-violette. Le papier pH recherche un acide "
                "carboxylique : il vire au rouge."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table))

        # --- Exemple traité : stratégie d'identification en 3 étapes ------------
        entete_strategie = Text("Stratégie d'identification de la classe d'un alcool", font_size=19, color=YELLOW, weight="BOLD")
        entete_strategie.next_to(titre, DOWN, buff=0.35)

        etapes = VGroup(
            Text("1. Pas de décoloration au KMnO₄ → alcool TERTIAIRE.", font_size=19, color=WHITE),
            Text("2. Décoloration + réactif de Schiff positif → alcool PRIMAIRE (donne un aldéhyde).", font_size=19, color=WHITE),
            Text("3. Décoloration + réactif de Schiff négatif → alcool SECONDAIRE (donne une cétone).", font_size=19, color=WHITE),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        etapes.next_to(entete_strategie, DOWN, buff=0.35)
        _fit(VGroup(entete_strategie, etapes), entete_strategie.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "On en déduit une stratégie en trois étapes pour "
                "identifier la classe d'un alcool inconnu. Étape un : si "
                "le permanganate acidifié ne se décolore pas, l'alcool "
                "n'est pas oxydé, c'est un alcool tertiaire. Étape deux : "
                "si le permanganate se décolore et que le produit fait "
                "rosir le réactif de Schiff, c'est un aldéhyde, donc "
                "l'alcool de départ est primaire. Étape trois : si le "
                "permanganate se décolore mais que le réactif de Schiff "
                "reste négatif, c'est une cétone, donc l'alcool de départ "
                "est secondaire."
            )
        ) as tracker:
            self.play(FadeIn(entete_strategie))
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_strategie), FadeOut(etapes))

        # --- À retenir : le principe de l'éthylotest (warning_box) ----------------
        ethylotest = warning_box(
            VGroup(
                Text(
                    _wrap(
                        "Les éthylotests utilisés par les forces de "
                        "l'ordre reposent sur un test d'oxydation : les "
                        "vapeurs d'éthanol de l'air expiré réduisent les "
                        "ions dichromate (oranges) en ions chrome III "
                        "(verts).",
                        width=48,
                    ),
                    font_size=21,
                ),
                MathTex(r"Cr_2O_7^{2-}\ (\text{orange}) \;\longrightarrow\; Cr^{3+}\ (\text{vert})", font_size=24, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=12.2,
        )
        ethylotest.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une application bien connue de ces tests d'oxydation : "
                "l'éthylotest, utilisé par les forces de l'ordre. Les "
                "vapeurs d'éthanol contenues dans l'air expiré réduisent "
                "les ions dichromate, de couleur orange, en ions chrome "
                "trois plus, de couleur verte. Ce changement de couleur "
                "révèle la présence d'alcool dans l'air expiré."
            )
        ) as tracker:
            self.play(FadeIn(ethylotest))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ethylotest))

        # --- Piège à éviter : préciser réactif ET observation ----------------------
        piege = warning_box(
            Text(
                _wrap(
                    "En rédigeant un test de reconnaissance, préciser à "
                    "la fois le réactif ET l'observation (ex. « le "
                    "réactif de Schiff rosit »). Écrire simplement « test "
                    "de Schiff positif » sans décrire l'observation coûte "
                    "des points en devoir.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter, très fréquent en devoir : lorsqu'on "
                "rédige un test de reconnaissance, il faut préciser à la "
                "fois le réactif utilisé et l'observation obtenue, par "
                "exemple « le réactif de Schiff rosit ». Écrire "
                "simplement « test de Schiff positif », sans décrire "
                "l'observation, coûte des points en devoir de niveau."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
