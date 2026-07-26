"""
scenes/Chimie_OxydoreductionSolutionAqueuse_02.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 02.

§ Les couples oxydant/réducteur : couple Cu²⁺/Cu (double flèche), définition
générale Ox + n e⁻ ⇌ Red, tableau des couples usuels (Cu²⁺/Cu, Fe³⁺/Fe²⁺,
I₂/I⁻, MnO₄⁻/Mn²⁺, Cr₂O₇²⁻/Cr³⁺, S₄O₆²⁻/S₂O₃²⁻). Piège : ampholyte redox
(Fe²⁺ appartient à deux couples).
Source : 1ereC/Chimie.pdf, chapitre 9, page 87.
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
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class LesCouplesOxydantReducteur(NotionScene):
    def construct(self):
        titre = scene_title("9.2 Les couples oxydant/réducteur")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le couple Cu²⁺/Cu, une écriture réversible -------------------
        double_fleche = MathTex(r"Cu^{2+} + 2\,e^- \rightleftharpoons Cu", font_size=36, color=WHITE)
        double_fleche.next_to(titre, DOWN, buff=0.6)

        intro = Text(
            _wrap(
                "Le fer cède ses électrons aux ions cuivre : dans ce sens, "
                "la transformation Cu²⁺ → Cu est privilégiée. Mais on "
                "associe toujours les deux formes, oxydée et réduite, "
                "d'une même espèce en un COUPLE, noté avec une double "
                "flèche.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(double_fleche, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans l'expérience précédente, le fer cède ses électrons "
                "aux ions cuivre : dans ce sens, la transformation cuivre "
                "deux plus vers cuivre est privilégiée. Mais en chimie, on "
                "associe toujours la forme oxydée et la forme réduite d'une "
                "même espèce en un couple, noté avec une double flèche, "
                "pour rappeler que l'échange d'électrons est en principe "
                "réversible."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Write(double_fleche))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(double_fleche), FadeOut(intro))

        # --- Raisonnement : définition générale du couple --------------------------
        def_couple = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Un couple oxydant/réducteur, noté Ox/Red, est "
                        "formé d'une espèce oxydante Ox et de sa forme "
                        "réduite Red associée, liées par l'échange de n "
                        "électrons :",
                        width=46,
                    ),
                    font_size=22,
                ),
                MathTex(r"Ox + n\,e^- \rightleftharpoons Red", font_size=30, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.35),
        )
        def_couple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici la définition générale. Un couple oxydant sur "
                "réducteur, noté Ox sur Red, est formé d'une espèce "
                "oxydante, Ox, et de sa forme réduite associée, Red, liées "
                "par l'échange de n électrons : Ox, plus n électrons, est "
                "en équilibre avec Red."
            )
        ) as tracker:
            self.play(FadeIn(def_couple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_couple))

        # --- Exemple traité : tableau des couples usuels ---------------------------
        entete_tab = Text("Quelques couples usuels", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["Cu²⁺ / Cu", "2"],
            ["Fe³⁺ / Fe²⁺", "1"],
            ["I₂ / I⁻", "2"],
            ["MnO₄⁻ / Mn²⁺", "5"],
            ["Cr₂O₇²⁻ / Cr³⁺", "6"],
            ["S₄O₆²⁻ / S₂O₃²⁻", "2"],
        ]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=16, weight="BOLD") for c in ["couple Ox/Red", "n électrons"]],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 16},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.22,
            h_buff=0.4,
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

        groupe_tab = VGroup(entete_tab, table)

        with self.voiceover(
            text=(
                "Voici les couples oxydant/réducteur usuels que nous "
                "retrouverons tout au long de ce chapitre, avec le nombre "
                "d'électrons échangés dans chaque cas : cuivre deux plus "
                "sur cuivre, deux électrons ; fer trois plus sur fer deux "
                "plus, un électron ; diiode sur ion iodure, deux électrons ; "
                "ion permanganate sur manganèse deux plus, cinq électrons ; "
                "ion dichromate sur chrome trois plus, six électrons ; et "
                "enfin tétrathionate sur thiosulfate, deux électrons."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- À retenir : le couple est une association Ox/Red --------------------
        recap = definition_box(
            Text(
                _wrap(
                    "Retenir : à chaque couple correspond une seule "
                    "demi-équation Ox + n e⁻ ⇌ Red, caractérisée par le "
                    "nombre n d'électrons échangés — ce nombre n'est pas "
                    "toujours le même d'un couple à l'autre.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        recap.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : à chaque couple correspond une "
                "seule demi-équation, Ox plus n électrons en équilibre avec "
                "Red, caractérisée par le nombre n d'électrons échangés — "
                "ce nombre n'est pas le même d'un couple à l'autre, il "
                "dépend de la structure de l'espèce chimique."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : l'ampholyte redox -------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : une même espèce peut appartenir à DEUX "
                    "couples différents. L'ion Fe²⁺ est réducteur dans le "
                    "couple Fe²⁺/Fe, mais oxydant dans le couple Fe³⁺/Fe²⁺. "
                    "On dit qu'il est ampholyte redox — le rôle d'une "
                    "espèce dépend toujours du couple considéré.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Attention à un piège important : une même espèce peut "
                "appartenir à deux couples différents. L'ion fer deux plus "
                "est réducteur dans le couple fer deux plus sur fer, mais "
                "il devient oxydant dans le couple fer trois plus sur fer "
                "deux plus. On dit qu'il est ampholyte redox : le rôle "
                "d'une espèce, oxydant ou réducteur, dépend toujours du "
                "couple dans lequel on la considère."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
