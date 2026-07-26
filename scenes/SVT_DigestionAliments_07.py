"""
scenes/SVT_DigestionAliments_07.py — Chapitre 12 (1ereD, SVT), scène 07.

§ 12.4.3 La digestion chimique dans l'intestin grêle : bile (émulsion,
sans enzyme), suc pancréatique (amylase, trypsine, lipase), suc intestinal
(entérokinase, peptidases, maltase, saccharase, lactase), tableau bilan
famille d'aliments → enzymes → nutriments finaux, propriétés des enzymes
digestives.
Source : 1ereD/SVT.pdf, pages 160-161.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _cell(text: str, x: float, y: float, font_size=15, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


class DigestionChimiqueIntestinGrele(NotionScene):
    def construct(self):
        titre = scene_title("12.4.3 — Digestion chimique : intestin grêle")
        titre.scale(0.56)
        titre.to_edge(UP)

        # --- Énoncé : trois sucs se mélangent au chyme -----------------------
        intro = Text(
            _wrap("Le duodénum reçoit trois sucs qui se mélangent au chyme acide.", width=54),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(text="Le duodénum reçoit trois sucs qui se mélangent au chyme acide venu de l'estomac.") as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : la bile ------------------------------
        bile = definition_box(
            Text(
                _wrap(
                    "La bile (0,5 à 1 L/j), produite par le foie et "
                    "déversée par la vésicule biliaire, ne contient pas "
                    "d'enzyme. Ses sels biliaires réalisent l'émulsion des "
                    "graisses : les grosses gouttes lipidiques sont "
                    "dispersées en gouttelettes fines, ce qui multiplie la "
                    "surface d'attaque des lipases. Alcaline, elle "
                    "neutralise aussi le chyme acide.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        bile.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La bile, zéro virgule cinq à un litre par jour, produite "
                "par le foie, est déversée par la vésicule biliaire. Elle "
                "ne contient pas d'enzyme. Ses sels biliaires réalisent "
                "l'émulsion des graisses : les grosses gouttes lipidiques "
                "sont dispersées en gouttelettes très fines, ce qui "
                "multiplie énormément la surface d'attaque pour les "
                "lipases. La bile, alcaline, participe aussi à la "
                "neutralisation du chyme acide."
            )
        ) as tracker:
            self.play(FadeIn(bile))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bile))

        # --- Le suc pancréatique -----------------------------------------------
        entete_pancreas = Text("Le suc pancréatique et ses 3 enzymes", font_size=24, color=YELLOW, weight="BOLD")
        entete_pancreas.next_to(titre, DOWN, buff=0.45)

        reaction_amylase = MathTex(
            r"\text{amidon restant} \xrightarrow{\;\text{amylase pancr.}\;} \text{maltose}", font_size=26, color=WHITE
        )
        reaction_trypsine = MathTex(
            r"\text{prot\'eines, polypeptides} \xrightarrow{\;\text{trypsine}\;} \text{peptides}", font_size=26, color=WHITE
        )
        reaction_lipase = MathTex(
            r"\text{graisses \'emulsionn\'ees} \xrightarrow{\;\text{lipase}\;} \text{acides gras} + \text{glyc\'erol}",
            font_size=26, color=WHITE,
        )
        reactions = VGroup(reaction_amylase, reaction_trypsine, reaction_lipase).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        reactions.next_to(entete_pancreas, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le suc pancréatique, un à un litre et demi par jour, "
                "contient des bicarbonates qui neutralisent l'acidité du "
                "chyme, et trois grandes enzymes : l'amylase pancréatique, "
                "qui achève la transformation de l'amidon restant en "
                "maltose ; la trypsine, sécrétée sous forme inactive, le "
                "trypsinogène, activée par l'entérokinase du suc "
                "intestinal, qui découpe protéines et polypeptides en "
                "peptides ; et la lipase pancréatique, l'enzyme "
                "essentielle de la digestion des graisses, qui découpe les "
                "graisses émulsionnées en acides gras et glycérol."
            )
        ) as tracker:
            self.play(FadeIn(entete_pancreas))
            self.play(Write(reaction_amylase))
            self.play(Write(reaction_trypsine))
            self.play(Write(reaction_lipase))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pancreas), FadeOut(reactions))

        # --- Le suc intestinal ----------------------------------------------------
        entete_intestinal = Text("Le suc intestinal achève le travail", font_size=24, color=YELLOW, weight="BOLD")
        entete_intestinal.next_to(titre, DOWN, buff=0.45)

        intestinal_bullets = _bullets(
            [
                "Entérokinase : active le trypsinogène en trypsine.",
                "Peptidases : découpent les peptides en acides aminés.",
                "Maltase : sépare le maltose en 2 glucoses.",
                "Saccharase : découpe le saccharose en glucose + fructose.",
                "Lactase : découpe le lactose en glucose + galactose.",
            ],
            font_size=20,
            width=52,
        )
        intestinal_bullets.next_to(entete_intestinal, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le suc intestinal, environ deux litres par jour, sécrété "
                "par les glandes de la paroi de l'intestin grêle, achève "
                "le travail : l'entérokinase active le trypsinogène en "
                "trypsine ; les peptidases découpent les peptides en "
                "acides aminés ; la maltase sépare le maltose en deux "
                "glucoses ; la saccharase découpe le saccharose, le sucre "
                "de table, en glucose et fructose ; la lactase découpe le "
                "lactose, le sucre du lait, en glucose et galactose."
            )
        ) as tracker:
            self.play(FadeIn(entete_intestinal))
            self.play(FadeIn(intestinal_bullets))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_intestinal), FadeOut(intestinal_bullets))

        # --- Exemple traité : tableau bilan -------------------------------------
        entete_tab = Text("Bilan de la digestion chimique", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.to_edge(UP).shift(DOWN * 1.0)

        x_famille, x_enz, x_nutr = -6.6, -2.6, 2.6
        rows_data = [
            ("Famille d'aliments", "Enzymes successives", "Nutriments finaux"),
            ("Amidon", "amylases + maltase", "glucose"),
            ("Saccharose, lactose", "saccharase, lactase", "glucose, fructose,\ngalactose"),
            ("Protéines", "pepsine, trypsine,\npeptidases", "acides aminés"),
            ("Graisses", "bile (émulsion) + lipases", "acides gras, glycérol"),
            ("Eau, sels, vitamines", "aucune", "absorbés tels quels"),
        ]
        row_ys = [2.9, 2.0, 1.0, -0.1, -1.2, -2.1]

        table_rows = VGroup()
        for i, (fam, enz, nutr) in enumerate(rows_data):
            bold = i == 0
            color = YELLOW if bold else WHITE
            fs = 16 if bold else 15
            row = VGroup(
                _cell(fam, x_famille, row_ys[i], font_size=fs, color=color, bold=bold),
                _cell(enz, x_enz, row_ys[i], font_size=fs, color=color, bold=bold),
                _cell(nutr, x_nutr, row_ys[i], font_size=fs, color=color, bold=bold),
            )
            table_rows.add(row)

        with self.voiceover(
            text=(
                "Voici le bilan de la digestion chimique. L'amidon, "
                "attaqué par les amylases puis la maltase, donne du "
                "glucose. Le saccharose et le lactose, attaqués par la "
                "saccharase et la lactase, donnent glucose, fructose et "
                "galactose. Les protéines, attaquées par la pepsine, la "
                "trypsine puis les peptidases, donnent des acides aminés. "
                "Les graisses, émulsionnées par la bile puis attaquées par "
                "les lipases, donnent acides gras et glycérol. L'eau, les "
                "sels minéraux et les vitamines, eux, sont absorbés sans "
                "transformation."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            for row in table_rows:
                self.play(FadeIn(row), run_time=0.5)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table_rows))

        # --- À retenir : propriétés des enzymes digestives ------------------------
        proprietes = property_box(
            Text(
                _wrap(
                    "1. Les enzymes sont des protéines, catalyseurs "
                    "biologiques : elles accélèrent les réactions sans "
                    "être consommées. 2. Chaque enzyme est spécifique d'un "
                    "substrat. 3. Leur action dépend de la température : "
                    "maximale vers 37°C, ralentie au froid, dénaturée "
                    "(détruite) à haute température. 4. Leur action dépend "
                    "du pH : la pepsine exige un milieu acide, les autres "
                    "un milieu neutre à basique.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.0,
        )
        proprietes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir, les propriétés des enzymes digestives. "
                "Premièrement, les enzymes sont des protéines qui jouent "
                "le rôle de catalyseurs biologiques : elles accélèrent les "
                "réactions sans être consommées par ces réactions. "
                "Deuxièmement, chaque enzyme est spécifique d'un substrat "
                ": l'amylase n'agit que sur l'amidon, la pepsine que sur "
                "les protéines, la lipase que sur les graisses. "
                "Troisièmement, l'action d'une enzyme dépend de la "
                "température : elle est maximale vers trente-sept degrés, "
                "ralentie au froid, et l'enzyme est détruite de façon "
                "irréversible à haute température, on dit qu'elle est "
                "dénaturée. Quatrièmement, l'action d'une enzyme dépend du "
                "pH : la pepsine exige un milieu acide, tandis que "
                "l'amylase salivaire et les enzymes pancréatiques et "
                "intestinales préfèrent un milieu neutre ou légèrement "
                "basique."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(proprietes))
