"""
scenes/SVT_ExpressionGenetique_11.py — Chapitre 5 (1ereC, SVT), scène 11.

VII.A-C. Les mutations : définition, les 3 types (substitution, insertion,
délétion) + tableau + effet sur le cadre de lecture, les 3 conséquences
d'une substitution (silencieuse, faux-sens, non-sens), et conséquences des
insertions/délétions (décalage du cadre de lecture).
Source : 1ereC/SVT.pdf, pages 51-52.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, RED, GREEN, FadeIn, FadeOut, MathTex, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


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


def _codon_row(codons, highlight_index=None, cell_w=1.0, cell_h=0.5, highlight_color=YELLOW):
    row = VGroup()
    for i, c in enumerate(codons):
        fill = highlight_color if i == highlight_index else "#1E5FA8"
        rect = Rectangle(width=cell_w, height=cell_h, fill_color=fill, fill_opacity=0.45, stroke_color=WHITE, stroke_width=1)
        txt = Text(c, font_size=14, color=WHITE, weight="BOLD")
        txt.move_to(rect.get_center())
        row.add(VGroup(rect, txt))
    row.arrange(RIGHT, buff=0.06)
    return row


class LesMutations(NotionScene):
    def construct(self):
        titre = scene_title("VII — Les mutations et leurs conséquences")
        titre.scale(0.6)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "L'ADN n'est pas figé : il peut subir des accidents. "
                "Étudions ces mutations, et leurs conséquences sur la "
                "protéine."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : définition + les 3 types -------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une mutation est une modification accidentelle et "
                    "héritable de la séquence des nucléotides de l'ADN. Si "
                    "elle touche un gène, elle peut modifier la protéine "
                    "correspondante et donc le caractère héréditaire.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une mutation est une modification accidentelle et "
                "héritable de la séquence des nucléotides de l'ADN. Si elle "
                "touche un gène, elle peut modifier la protéine "
                "correspondante, et donc le caractère héréditaire."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : tableau des 3 types de mutations ------------------------
        entete_tab = Text("Les trois types de mutations ponctuelles", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        rows = [
            ("Substitution", "Remplacement d'1 nucléotide par un autre", "1 seul codon modifié ; cadre inchangé"),
            ("Insertion", "Ajout d'1 (ou plusieurs) nucléotide(s)", "Décalage du cadre à partir de l'insertion"),
            ("Délétion", "Perte d'1 (ou plusieurs) nucléotide(s)", "Décalage du cadre à partir de la délétion"),
        ]
        cell_matrix = [[
            Text("Type", font_size=18, color=YELLOW, weight="BOLD"),
            Text("Description", font_size=18, color=YELLOW, weight="BOLD"),
            Text("Effet sur le cadre de lecture", font_size=18, color=YELLOW, weight="BOLD"),
        ]]
        for a, b, c in rows:
            cell_matrix.append([
                Text(a, font_size=17, color=WHITE, weight="BOLD"),
                Text(b, font_size=15, color=WHITE),
                Text(c, font_size=15, color=WHITE),
            ])
        tableau = _grid_table(cell_matrix, col_gap=0.4, row_gap=0.25)
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        tableau.scale(0.85)

        with self.voiceover(
            text=(
                "On distingue trois grands types de mutations ponctuelles, "
                "touchant un ou quelques nucléotides. La substitution : le "
                "remplacement d'un nucléotide par un autre — un seul codon "
                "est modifié, le cadre de lecture reste inchangé. "
                "L'insertion : l'ajout d'un ou plusieurs nucléotides — le "
                "cadre de lecture est décalé à partir du point d'insertion. "
                "La délétion : la perte d'un ou plusieurs nucléotides — le "
                "cadre de lecture est décalé à partir du point de perte."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Schéma : effet sur le cadre de lecture (insertion/délétion) -----------
        entete_cadre = Text("Effet visuel sur le cadre de lecture", font_size=20, color=YELLOW, weight="BOLD")
        entete_cadre.next_to(titre, DOWN, buff=0.45)

        normal = _codon_row(["AUG", "GGC", "UUU", "ACC"])
        label_normal = Text("normal :", font_size=15, color=WHITE).next_to(normal, LEFT, buff=0.2)
        ligne_normale = VGroup(label_normal, normal).arrange(RIGHT, buff=0.15)

        decale = _codon_row(["AUG", "GGG", "CUU", "UAC"], highlight_index=1, highlight_color=RED)
        label_decale = Text("après insertion :", font_size=15, color=WHITE).next_to(decale, LEFT, buff=0.2)
        ligne_decalee = VGroup(label_decale, decale).arrange(RIGHT, buff=0.15)

        schema_cadre = VGroup(ligne_normale, ligne_decalee).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        schema_cadre.next_to(entete_cadre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici pourquoi le décalage du cadre de lecture est si "
                "grave. En temps normal, l'ARNm se découpe en A U G, G G C, "
                "U U U, A C C. Si un seul nucléotide est inséré au tout "
                "début, tous les codons suivants se retrouvent décalés : G "
                "G G, C U U, U A C — des codons totalement différents, "
                "traduits en des acides aminés totalement différents."
            )
        ) as tracker:
            self.play(FadeIn(entete_cadre))
            self.play(FadeIn(schema_cadre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_cadre), FadeOut(schema_cadre))

        # --- Les 3 conséquences d'une substitution ----------------------------------
        entete_subst = Text("Les 3 conséquences possibles d'une substitution", font_size=20, color=YELLOW, weight="BOLD")
        entete_subst.next_to(titre, DOWN, buff=0.45)

        silencieuse = VGroup(
            Text("Silencieuse", font_size=18, color=GREEN, weight="BOLD"),
            MathTex(r"\text{GGA} \rightarrow \text{GGG}", font_size=20, color=WHITE),
            Text("même acide aminé (Gly)\nprotéine inchangée", font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.15)

        faux_sens = VGroup(
            Text("Faux-sens", font_size=18, color=YELLOW, weight="BOLD"),
            MathTex(r"\text{GAG} \rightarrow \text{GUG}", font_size=20, color=WHITE),
            Text("acide glutamique → valine\n1 acide aminé changé", font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.15)

        non_sens = VGroup(
            Text("Non-sens", font_size=18, color=RED, weight="BOLD"),
            MathTex(r"\text{UGG} \rightarrow \text{UGA}", font_size=20, color=WHITE),
            Text("Trp → Stop\nprotéine tronquée", font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.15)

        trois_cas = VGroup(silencieuse, faux_sens, non_sens).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        trois_cas.next_to(entete_subst, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Face à une substitution, trois cas sont possibles. La "
                "mutation silencieuse : le nouveau codon code le même acide "
                "aminé, car le code génétique est dégénéré — par exemple, G "
                "G A devient G G G, qui code toujours la glycine, la "
                "protéine est inchangée. La mutation faux-sens : le nouveau "
                "codon code un autre acide aminé — par exemple, G A G, "
                "acide glutamique, devient G U G, valine ; un seul acide "
                "aminé change dans la protéine, ce qui peut modifier sa "
                "fonction. La mutation non-sens : le nouveau codon devient "
                "un codon stop — par exemple, U G G, tryptophane, devient U "
                "G A, stop ; la traduction s'arrête prématurément, la "
                "protéine est tronquée, généralement non fonctionnelle."
            )
        ) as tracker:
            self.play(FadeIn(entete_subst))
            self.play(FadeIn(trois_cas))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_subst), FadeOut(trois_cas))

        # --- Piège / à retenir : gravité insertions/délétions ------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "L'ajout ou la perte d'un nucléotide décale le cadre de "
                    "lecture : à partir de la mutation, TOUS les codons "
                    "sont modifiés. La protéine est le plus souvent "
                    "totalement différente et non fonctionnelle — c'est "
                    "pourquoi une insertion ou une délétion (hors multiple "
                    "de 3) est généralement plus grave qu'une substitution.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenez bien cette différence de gravité. L'ajout ou la "
                "perte d'un nucléotide décale le cadre de lecture : à "
                "partir du point de la mutation, tous les codons sont "
                "modifiés, et la protéine est le plus souvent totalement "
                "différente et non fonctionnelle. C'est pourquoi les "
                "insertions et les délétions, sauf si elles portent sur un "
                "multiple de trois nucléotides, sont généralement bien plus "
                "graves qu'une simple substitution."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
