"""
scenes/Chimie_OxydoreductionSolutionAqueuse_07.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 07.

§ Étude de quelques couples usuels — couleurs : tableau des couleurs
(MnO₄⁻ violet/Mn²⁺ incolore, Cr₂O₇²⁻ orange/Cr³⁺ verte, I₂ brune/I⁻
incolore, S₄O₆²⁻/S₂O₃²⁻ incolores, Fe³⁺ jaune/Fe²⁺ verdâtre, Cu²⁺
bleue/Cu métal rouge) et observation caractéristique de chaque réaction.
Source : 1ereC/Chimie.pdf, chapitre 9, page 91.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORANGE,
    PURPLE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class CouleursDesCouplesUsuels(NotionScene):
    def construct(self):
        titre = scene_title("9.7 Étude de quelques couples usuels — couleurs")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi les couleurs comptent en chimie -----------------------
        intro = Text(
            _wrap(
                "En solution aqueuse, oxydant et réducteur d'un même "
                "couple ont souvent des couleurs très différentes : c'est "
                "un outil précieux pour SUIVRE une réaction d'œil nu, sans "
                "aucun appareil.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En solution aqueuse, l'oxydant et le réducteur d'un même "
                "couple ont souvent des couleurs très différentes. C'est un "
                "outil précieux en chimie : cela permet de suivre "
                "l'avancement d'une réaction d'oxydoréduction à l'œil nu, "
                "sans aucun appareil de mesure."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : le tableau des couleurs -----------------------------------
        entete_tab = Text("Couleurs des couples usuels", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["MnO₄⁻", "violet", "Mn²⁺", "incolore"],
            ["Cr₂O₇²⁻", "orange", "Cr³⁺", "vert"],
            ["I₂", "brun", "I⁻", "incolore"],
            ["S₄O₆²⁻", "incolore", "S₂O₃²⁻", "incolore"],
            ["Fe³⁺", "jaune", "Fe²⁺", "vert pâle"],
            ["Cu²⁺", "bleu", "Cu (métal)", "rouge"],
        ]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=15, weight="BOLD") for c in ["oxydant", "couleur", "réducteur", "couleur"]],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 15},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.2,
            h_buff=0.35,
        )
        table.get_col_labels().set_color(YELLOW)
        couleurs_cellules = [
            PURPLE, WHITE, WHITE, WHITE,
            ORANGE, WHITE, GREEN, WHITE,
            "#7A4A1E", WHITE, WHITE, WHITE,
            WHITE, WHITE, WHITE, WHITE,
            YELLOW, WHITE, GREEN, WHITE,
            BLUE, WHITE, RED, WHITE,
        ]
        for entree, couleur in zip(table.get_entries_without_labels(), couleurs_cellules):
            entree.set_color(couleur)
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
                "Voici les couleurs à connaître par cœur. L'ion "
                "permanganate est violet, réduit en ion manganèse deux "
                "plus incolore. L'ion dichromate est orange, réduit en ion "
                "chrome trois plus vert. Le diiode est brun, réduit en ion "
                "iodure incolore. Le tétrathionate et le thiosulfate sont "
                "tous deux incolores. L'ion fer trois plus est jaune, "
                "réduit en ion fer deux plus vert pâle. Et l'ion cuivre "
                "deux plus est bleu, réduit en cuivre métallique rouge."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Exemple traité : observations caractéristiques ---------------------------
        entete_obs = Text("Observation caractéristique de chaque réaction", font_size=21, color=YELLOW, weight="BOLD")
        entete_obs.next_to(titre, DOWN, buff=0.35)

        observations = _bullets(
            [
                "titrage au permanganate : la solution reste violette dès "
                "le premier excès (décoloration → coloration persistante) ;",
                "dichromate + iodure : virage net de l'orange vers le "
                "vert, avec apparition de diiode brun ;",
                "diiode + thiosulfate : décoloration progressive du brun "
                "vers l'incolore ;",
                "fer III + cuivre : la solution jaune pâlit et verdit ;",
                "fer + sulfate de cuivre : décoloration du bleu, dépôt "
                "rouge de cuivre.",
            ],
            width=52,
        )
        observations.next_to(entete_obs, DOWN, buff=0.35)
        groupe_obs = VGroup(entete_obs, observations)
        _fit(groupe_obs, titre.get_bottom()[1] - 0.35)
        groupe_obs.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Ces couleurs permettent de repérer précisément la fin "
                "d'une réaction. Lors d'un titrage au permanganate, la "
                "solution reste violette dès le premier excès de réactif : "
                "c'est le repère de fin de dosage. Entre dichromate et "
                "iodure, on observe un virage net de l'orange vers le "
                "vert, avec apparition de diiode brun. Entre diiode et "
                "thiosulfate, une décoloration progressive du brun vers "
                "l'incolore. Entre fer trois plus et cuivre, la solution "
                "jaune pâlit et verdit. Et dans notre expérience initiale, "
                "entre le fer et le sulfate de cuivre, on observe la "
                "décoloration du bleu accompagnée du dépôt rouge de "
                "cuivre."
            )
        ) as tracker:
            self.play(FadeIn(entete_obs))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_obs))

        # --- À retenir : la couleur, un indicateur qualitatif -------------------------
        recap = property_box(
            Text(
                _wrap(
                    "Retenir : la couleur d'une espèce redox est un "
                    "indicateur qualitatif précieux, mais jamais une "
                    "preuve suffisante à elle seule — seule la "
                    "demi-équation électronique prouve rigoureusement "
                    "l'échange d'électrons.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        recap.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ceci : la couleur d'une espèce redox est un "
                "indicateur qualitatif précieux pour suivre une réaction, "
                "mais ce n'est jamais une preuve suffisante à elle seule — "
                "seule la demi-équation électronique prouve rigoureusement "
                "l'échange d'électrons."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : couleur incolore ne veut pas dire absence -------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : « incolore » ne signifie pas « absent » ! Les "
                    "ions Mn²⁺, I⁻, S₂O₃²⁻ et S₄O₆²⁻ sont bien présents en "
                    "solution malgré leur absence de couleur — l'incolore "
                    "est une couleur comme une autre, pas une preuve de "
                    "disparition de la matière.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)
        _fit(piege, titre.get_bottom()[1] - 0.5)

        with self.voiceover(
            text=(
                "Attention à un piège important : incolore ne signifie pas "
                "absent. Les ions manganèse deux plus, iodure, thiosulfate "
                "et tétrathionate sont bien présents en solution malgré "
                "leur absence de couleur — l'incolore est une couleur comme "
                "une autre, ce n'est pas une preuve de disparition de la "
                "matière."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
