"""
scenes/SVT_ExpressionGenetique_06.py — Chapitre 5 (1ereC, SVT), scène 06.

III. La transcription : définition, les 4 étapes, méthode "sens de
lecture" (ARNm 5'→3', ARN polymérase lit 3'→5'), Exemple résolu 3
(transcrire 3'-TACGGAATTCGA-5'), tableau résumé de la transcription.
Source : 1ereC/SVT.pdf, pages 47-48.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Ellipse,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"{i}. {_wrap(it, width=width)}", font_size=font_size, color=color) for i, it in enumerate(items, start=1)]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.7, row_gap=0.3):
    n_rows = len(cell_matrix)
    n_cols = len(cell_matrix[0])
    col_widths = [max(cell_matrix[r][c].width for r in range(n_rows)) for c in range(n_cols)]
    row_height = max(cell.height for row in cell_matrix for cell in row)
    col_x = []
    x = 0.0
    for c in range(n_cols):
        col_x.append(x)
        x += col_widths[c] + col_gap
    table = VGroup()
    y = 0.0
    for r in range(n_rows):
        for c in range(n_cols):
            cell = cell_matrix[r][c]
            cell.move_to([col_x[c] + cell.width / 2, y, 0])
            table.add(cell)
        y -= row_height + row_gap
    return table


class LaTranscription(NotionScene):
    def construct(self):
        titre = scene_title("III — La transcription : de l'ADN à l'ARNm")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition -------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La transcription est la synthèse d'une molécule d'ARNm "
                    "dont la séquence est complémentaire de celle de l'un "
                    "des deux brins d'ADN du gène, appelé brin transcrit "
                    "(ou brin matrice). Elle a lieu dans le noyau.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La transcription est la première grande étape de la "
                "synthèse des protéines. Par définition, la transcription "
                "est la synthèse d'une molécule d'ARN messager dont la "
                "séquence est complémentaire de celle de l'un des deux "
                "brins d'ADN du gène, appelé brin transcrit, ou brin "
                "matrice. Elle a lieu dans le noyau."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les 4 étapes + schéma ---------------------------------
        entete_etapes = Text("Les 4 étapes de la transcription", font_size=24, color=YELLOW, weight="BOLD")
        entete_etapes.next_to(titre, DOWN, buff=0.45)

        etapes = _bullets(
            [
                "Les deux brins d'ADN s'écartent localement au niveau du "
                "gène (rupture temporaire des liaisons hydrogène).",
                "L'ARN polymérase se fixe sur le brin transcrit et avance "
                "le long de celui-ci.",
                "Elle assemble des ribonucléotides libres par "
                "complémentarité : face à A → U, face à T → A, face à G → "
                "C, face à C → G.",
                "L'ARNm formé se détache et migre vers le cytoplasme ; les "
                "deux brins d'ADN se réassocient.",
            ],
            font_size=19,
            width=54,
        )
        etapes.next_to(entete_etapes, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La transcription se déroule en quatre étapes. Un : les "
                "deux brins d'ADN s'écartent localement au niveau du gène, "
                "par rupture temporaire des liaisons hydrogène. Deux : une "
                "enzyme, l'ARN polymérase, se fixe sur le brin transcrit et "
                "avance le long de celui-ci. Trois : l'ARN polymérase "
                "assemble des ribonucléotides libres du milieu, en "
                "appliquant la complémentarité : face à A, elle place U ; "
                "face à T, elle place A ; face à G, elle place C ; face à C, "
                "elle place G. Quatre : l'ARNm formé se détache et migre "
                "vers le cytoplasme ; les deux brins d'ADN se réassocient — "
                "la molécule d'ADN reste intacte, c'est une copie, pas un "
                "prélèvement."
            )
        ) as tracker:
            self.play(FadeIn(entete_etapes))
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_etapes), FadeOut(etapes))

        # --- Schéma : ARN polymérase en train de transcrire -----------------------
        adn_brin = Rectangle(width=8.5, height=0.35, fill_color="#4FC3F7", fill_opacity=0.5, stroke_color=WHITE)
        adn_label = Text("brin transcrit (matrice)", font_size=16, color=WHITE)
        adn_label.next_to(adn_brin, UP, buff=0.15)
        arn_pol = Ellipse(width=1.3, height=0.9, fill_color=YELLOW, fill_opacity=0.6, stroke_color=YELLOW)
        arn_pol.move_to(adn_brin.get_center() + LEFT * 1.5)
        arn_pol_label = Text("ARN\npolymérase", font_size=13, color="#1A1A1A", weight="BOLD")
        arn_pol_label.move_to(arn_pol.get_center())
        arnm_brin = Rectangle(width=3.5, height=0.3, fill_color=YELLOW, fill_opacity=0.7, stroke_color=YELLOW)
        arnm_brin.next_to(arn_pol, DOWN, buff=0.35).align_to(adn_brin, LEFT)
        arnm_label = Text("ARNm naissant", font_size=15, color=YELLOW)
        arnm_label.next_to(arnm_brin, DOWN, buff=0.1)
        sens_pol = Text("ARN polymérase lit le brin transcrit dans le sens 3'→5'", font_size=16, color=WHITE)
        sens_pol.next_to(adn_brin, DOWN, buff=1.1)
        fleche_pol = Arrow(RIGHT * 1.6, LEFT * 1.6, buff=0, color=YELLOW).scale(0.6)
        fleche_pol.next_to(adn_brin, UP, buff=0.55).align_to(adn_brin, RIGHT).shift(LEFT * 1.5)

        schema = VGroup(adn_brin, adn_label, arn_pol, arn_pol_label, arnm_brin, arnm_label, sens_pol)
        schema.next_to(titre, DOWN, buff=0.65)

        with self.voiceover(
            text=(
                "Voici comment se représenter cette machinerie : l'ARN "
                "polymérase avance le long du brin transcrit et laisse "
                "derrière elle un brin d'ARN messager naissant."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Méthode : sens de lecture ---------------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "L'ARNm est synthétisé dans le sens 5'→3', pendant que "
                    "l'ARN polymérase lit le brin transcrit dans le sens "
                    "3'→5'. Les deux brins sont donc lus en sens inverse "
                    "l'un de l'autre.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Point clé à retenir absolument : l'ARN messager est "
                "synthétisé dans le sens cinq prime vers trois prime, "
                "pendant que l'ARN polymérase lit le brin transcrit dans le "
                "sens trois prime vers cinq prime. Les deux brins sont donc "
                "lus en sens inverse l'un de l'autre."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple résolu 3 : transcrire un gène ---------------------------------
        enonce = MathTex(r"3'\text{-TACGGAATTCGA-}5'", font_size=28, color=WHITE)
        fleche_txt = Text("ARNm complémentaire, antiparallèle :", font_size=18, color=YELLOW)
        reponse = MathTex(r"5'\text{-AUGCCUUAAGCU-}3'", font_size=28, color="#4FC3F7")
        remarque = Text(
            _wrap(
                "La séquence de l'ARNm est identique à celle du brin non "
                "transcrit (brin codant), à ceci près que U remplace T.",
                width=48,
            ),
            font_size=18,
            color=WHITE,
        )
        calcul = VGroup(enonce, fleche_txt, reponse, remarque).arrange(DOWN, buff=0.3)

        exemple = example_box(calcul, box_width=11.5)
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu. On donne le brin transcrit : trois prime, "
                "T A C G G A A T T C G A, cinq prime. L'ARN messager est "
                "complémentaire et antiparallèle : on obtient cinq prime, A "
                "U G C C U U A A G C U, trois prime. On remarque que la "
                "séquence de l'ARNm est identique à celle du brin non "
                "transcrit, appelé brin codant, à ceci près que U remplace "
                "T."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : tableau résumé ---------------------------------------------
        entete_resume = Text("Résumé de la transcription", font_size=24, color=YELLOW, weight="BOLD")
        entete_resume.next_to(titre, DOWN, buff=0.5)

        resume_rows = [
            ("Lieu", "Noyau"),
            ("Matrice lue", "Brin transcrit d'ADN, lu 3'→5'"),
            ("Enzyme clé", "ARN polymérase"),
            ("Molécule produite", "ARNm, synthétisé 5'→3'"),
            ("Appariement", "A↔U, T↔A, G↔C, C↔G"),
            ("Sorte de copie", "Fidèle, réversible : l'ADN n'est pas consommé"),
        ]
        cell_matrix = [[Text(a, font_size=19, color=WHITE), Text(b, font_size=19, color=WHITE)] for a, b in resume_rows]
        tableau = _grid_table(cell_matrix, col_gap=0.6, row_gap=0.22)
        tableau.next_to(entete_resume, DOWN, buff=0.35)
        tableau.scale(0.8)

        with self.voiceover(
            text=(
                "Résumons. Lieu : le noyau. Matrice lue : le brin transcrit "
                "d'ADN, lu dans le sens trois prime vers cinq prime. Enzyme "
                "clé : l'ARN polymérase. Molécule produite : l'ARNm, "
                "synthétisé dans le sens cinq prime vers trois prime. Règle "
                "d'appariement : A avec U, T avec A, G avec C, C avec G. Et "
                "enfin, c'est une copie fidèle mais réversible : l'ADN n'est "
                "pas consommé par la transcription."
            )
        ) as tracker:
            self.play(FadeIn(entete_resume))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(entete_resume), FadeOut(tableau))
