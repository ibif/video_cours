"""
scenes/SVT_ExpressionGenetique_10.py — Chapitre 5 (1ereC, SVT), scène 10.

V.C + VI. Bilan comparatif transcription/traduction (tableau), Exemple
résolu 5 (chaîne complète de détermination : brin transcrit →
ARNm → codons → protéine), et méthode de calcul des tailles de molécules
(3n+3 nucléotides pour une protéine de n acides aminés).
Source : 1ereC/SVT.pdf, pages 50-51.
"""

import textwrap

from manim import DOWN, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


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


class BilanTranscriptionTraduction(NotionScene):
    def construct(self):
        titre = scene_title("Bilan : transcription et traduction")
        titre.scale(0.6)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Nous connaissons maintenant les deux étapes de la synthèse "
                "des protéines. Comparons-les dans un tableau de synthèse, "
                "puis suivons ensemble la chaîne complète, du gène à la "
                "protéine."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Raisonnement : tableau comparatif ------------------------------------
        rows = [
            ("Lieu", "Noyau", "Cytoplasme (ribosomes)"),
            ("Départ", "ADN (brin transcrit)", "ARNm"),
            ("Produit", "ARNm", "Chaîne polypeptidique"),
            ("Machine clé", "ARN polymérase", "Ribosome"),
            ("Langue d'arrivée", "Nucléotidique", "Acides aminés"),
            ("Reconnaissance", "Complémentarité des bases", "Codon ↔ anticodon"),
            ("Sens de lecture", "3'→5' (brin transcrit)", "5'→3' (ARNm)"),
        ]
        cell_matrix = [[
            Text("Caractère", font_size=18, color=YELLOW, weight="BOLD"),
            Text("Transcription", font_size=18, color=YELLOW, weight="BOLD"),
            Text("Traduction", font_size=18, color=YELLOW, weight="BOLD"),
        ]]
        for a, b, c in rows:
            cell_matrix.append([
                Text(a, font_size=16, color=WHITE),
                Text(b, font_size=16, color=WHITE),
                Text(c, font_size=16, color=WHITE),
            ])
        tableau = _grid_table(cell_matrix, col_gap=0.45, row_gap=0.2)
        tableau.next_to(titre, DOWN, buff=0.5)
        tableau.scale(0.8)

        with self.voiceover(
            text=(
                "Voici le bilan des deux étapes. Le lieu : la transcription "
                "a lieu dans le noyau, la traduction dans le cytoplasme, aux "
                "ribosomes. Le point de départ : l'ADN, précisément le brin "
                "transcrit, pour la transcription ; l'ARNm pour la "
                "traduction. Le produit : l'ARNm d'un côté, la chaîne "
                "polypeptidique de l'autre. La machine clé : l'ARN "
                "polymérase, puis le ribosome. La langue d'arrivée : "
                "toujours nucléotidique pour la transcription, mais le "
                "langage des acides aminés pour la traduction. Les éléments "
                "de reconnaissance : la complémentarité des bases, puis "
                "l'appariement codon-anticodon. Et le sens de lecture de la "
                "matrice : trois prime vers cinq prime pour le brin "
                "transcrit, cinq prime vers trois prime pour l'ARNm."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Exemple résolu 5 : chaîne complète de détermination ------------------
        enonce = MathTex(r"3'\text{-TACCCGAAATGGATT-}5'", font_size=24, color=WHITE)
        etape1_txt = Text("Étape 1 — Transcription :", font_size=17, color=YELLOW)
        etape1 = MathTex(r"5'\text{-AUGGGCUUUACCUAA-}3'", font_size=24, color="#4FC3F7")
        etape2_txt = Text("Étape 2 — Découpage en codons :", font_size=17, color=YELLOW)
        etape2 = MathTex(r"\text{AUG} \mid \text{GGC} \mid \text{UUU} \mid \text{ACC} \mid \text{UAA}", font_size=22, color="#4FC3F7")
        etape3_txt = Text("Étape 3 — Traduction :", font_size=17, color=YELLOW)
        etape3 = Text("Met — Gly — Phé — Thr — Stop", font_size=22, color="#4FC3F7", weight="BOLD")
        resultat = Text("Protéine : Met—Gly—Phé—Thr (4 acides aminés)", font_size=19, color=WHITE)

        calcul = VGroup(enonce, etape1_txt, etape1, etape2_txt, etape2, etape3_txt, etape3, resultat).arrange(DOWN, buff=0.22)

        exemple = example_box(calcul, box_width=11.5)
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu : suivons la chaîne complète de "
                "détermination. On donne un fragment du brin transcrit d'un "
                "gène : trois prime, T A C C C G A A A T G G A T T, cinq "
                "prime. Étape un, la transcription : l'ARNm complémentaire "
                "s'écrit cinq prime, A U G G G C U U U A C C U A A, trois "
                "prime. Étape deux, le découpage en codons : A U G, G G C, "
                "U U U, A C C, U A A. Étape trois, la traduction, à l'aide "
                "de la table du code génétique : méthionine, glycine, "
                "phénylalanine, thréonine, stop. La protéine formée est "
                "donc méthionine-glycine-phénylalanine-thréonine, soit "
                "quatre acides aminés."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : méthode de calcul des tailles ----------------------------
        formule = MathTex(r"\text{ARNm} \geq 3n + 3 \ \text{nucléotides} \quad (n \text{ codons} + 1 \text{ codon stop})", font_size=26, color=WHITE)
        application = MathTex(r"n = 150 \;\Rightarrow\; 3 \times 150 + 3 = 453 \ \text{nucléotides}", font_size=26, color=YELLOW)
        methode = method_box(
            VGroup(formule, application).arrange(DOWN, buff=0.35),
            box_width=11.5,
        )
        methode.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Méthode de calcul des tailles de molécules, à retenir. "
                "Pour une protéine de n acides aminés, l'ARNm comporte au "
                "minimum trois n plus trois nucléotides : n codons, plus un "
                "codon stop. Le gène, c'est-à-dire le brin transcrit, "
                "comporte au minimum le même nombre de nucléotides. Par "
                "exemple, une protéine de cent cinquante acides aminés est "
                "codée par un ARNm d'au moins trois fois cent cinquante plus "
                "trois, soit quatre cent cinquante-trois nucléotides."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
