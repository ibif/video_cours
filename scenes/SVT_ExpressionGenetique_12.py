"""
scenes/SVT_ExpressionGenetique_12.py — Chapitre 5 (1ereC, SVT), scène 12.

VII.D-E. Étude de cas : la drépanocytose (définition, HbA vs HbS,
comparaison codon6/ARNm/acide aminé/conséquence, la mutation A→T,
conséquences en chaîne) + remarque contexte africain (hétérozygotes AS et
paludisme) + causes et caractère héréditaire des mutations.
Source : 1ereC/SVT.pdf, pages 52-53.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, RED, FadeIn, FadeOut, MathTex, Circle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
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


def _globule(deforme=False, color=RED):
    if not deforme:
        return Circle(radius=0.28, color=color, fill_color=color, fill_opacity=0.75, stroke_width=1)
    # Globule rouge déformé en "faucille" : approximé par un cercle aplati
    forme = Circle(radius=0.28, color=color, fill_color=color, fill_opacity=0.75, stroke_width=1)
    forme.stretch(0.45, dim=1).rotate(0.6)
    return forme


class EtudeDeCasDrepanocytose(NotionScene):
    def construct(self):
        titre = scene_title("VII.D — Étude de cas : la drépanocytose")
        titre.scale(0.6)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Appliquons tout ce que nous venons d'apprendre à un "
                "exemple réel et particulièrement important en Afrique "
                "subsaharienne : la drépanocytose."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : définition -----------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La drépanocytose (ou anémie falciforme) est une "
                    "maladie héréditaire du sang, fréquente en Afrique "
                    "subsaharienne (et donc en Côte d'Ivoire), due à une "
                    "mutation du gène codant la chaîne β de l'hémoglobine.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La drépanocytose, ou anémie falciforme, est une maladie "
                "héréditaire du sang, fréquente en Afrique subsaharienne, "
                "et donc en Côte d'Ivoire, due à une mutation du gène "
                "codant la chaîne bêta de l'hémoglobine."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : globules rouges sain / malade + tableau -----------------
        gr_sain = _globule(deforme=False, color=RED)
        label_sain = Text("HbA (sain) : globules ronds, souples", font_size=16, color=WHITE)
        bloc_sain = VGroup(gr_sain, label_sain).arrange(RIGHT, buff=0.25)

        gr_malade = _globule(deforme=True, color="#8B1A2B")
        label_malade = Text("HbS (malade) : globules en faucille", font_size=16, color=WHITE)
        bloc_malade = VGroup(gr_malade, label_malade).arrange(RIGHT, buff=0.25)

        globules = VGroup(bloc_sain, bloc_malade).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        globules.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'hémoglobine est la protéine des globules rouges qui "
                "transporte le dioxygène. Chez un individu sain, "
                "l'hémoglobine HbA donne des globules rouges ronds et "
                "souples. Chez un individu drépanocytaire, l'hémoglobine "
                "HbS déforme les globules rouges en faucilles, moins "
                "souples, qui circulent mal dans les petits vaisseaux."
            )
        ) as tracker:
            self.play(FadeIn(globules))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(globules))

        entete_tab = Text("Comparaison au niveau du 6e codon de la chaîne β", font_size=19, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        rows = [
            ("Individu sain (HbA)", "5'-GAG-3'", "5'-GAG-3'", "Ac. glutamique", "Globules ronds, souples"),
            ("Individu malade (HbS)", "5'-GTG-3'", "5'-GUG-3'", "Valine", "Globules en faucilles"),
        ]
        cell_matrix = [[
            Text("", font_size=14),
            Text("Codon 6\n(brin non transcrit)", font_size=14, color=YELLOW, weight="BOLD"),
            Text("Codon 6\n(ARNm)", font_size=14, color=YELLOW, weight="BOLD"),
            Text("6e acide\naminé", font_size=14, color=YELLOW, weight="BOLD"),
            Text("Conséquence", font_size=14, color=YELLOW, weight="BOLD"),
        ]]
        for nom, adn, arn, aa, conseq in rows:
            cell_matrix.append([
                Text(nom, font_size=14, color=WHITE),
                Text(adn, font_size=14, color=WHITE),
                Text(arn, font_size=14, color=WHITE),
                Text(aa, font_size=14, color=WHITE),
                Text(conseq, font_size=13, color=WHITE),
            ])
        tableau = _grid_table(cell_matrix, col_gap=0.35, row_gap=0.25)
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        tableau.scale(0.85)

        with self.voiceover(
            text=(
                "Comparons précisément les deux séquences, au niveau du "
                "sixième codon de la chaîne bêta. Chez l'individu sain, le "
                "codon non transcrit est G A G, l'ARNm porte le même codon "
                "G A G, ce qui donne l'acide glutamique, et des globules "
                "ronds et souples. Chez l'individu malade, le codon non "
                "transcrit est devenu G T G, l'ARNm porte donc G U G, ce "
                "qui donne la valine, et des globules déformés en "
                "faucilles."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- La mutation précise -----------------------------------------------------
        mutation = MathTex(
            r"\text{brin transcrit : } 3'\text{-CTC-}5' \;\longrightarrow\; 3'\text{-CAC-}5' \quad (\text{A} \rightarrow \text{T})",
            font_size=24,
            color=WHITE,
        )
        note_mutation = Text("1 seul codon changé, sur les 146 acides aminés de la chaîne β", font_size=17, color=WHITE)
        bloc_mutation = VGroup(mutation, note_mutation).arrange(DOWN, buff=0.3)
        bloc_mutation.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La mutation responsable est donc une substitution : un A "
                "devient un T sur le brin non transcrit — autrement dit, le "
                "brin transcrit passe de trois prime, C T C, cinq prime, à "
                "trois prime, C A C, cinq prime. Un seul nucléotide change, "
                "un seul codon est modifié, et un seul acide aminé change "
                "sur les cent quarante-six que compte la chaîne bêta."
            )
        ) as tracker:
            self.play(FadeIn(bloc_mutation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_mutation))

        # --- Propriété : conséquences en chaîne --------------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Substitution sur 1 nucléotide du gène → 1 acide aminé "
                    "changé (Glu → Val) → propriétés de la protéine "
                    "modifiées (HbS se solidifie en fibres sans O₂) → "
                    "globules rouges déformés en faucilles → anémie, "
                    "douleurs, atteintes des organes.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        propriete.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ce cas illustre parfaitement une propriété centrale de ce "
                "chapitre, les conséquences en chaîne : une substitution "
                "sur un seul nucléotide du gène entraîne le changement d'un "
                "seul acide aminé de l'hémoglobine, ce qui modifie les "
                "propriétés de la protéine — l'hémoglobine HbS se solidifie "
                "en fibres lorsque le dioxygène manque — ce qui déforme les "
                "globules rouges en faucilles, ce qui provoque anémie, "
                "douleurs et atteintes des organes. C'est le lien direct "
                "entre mutation, protéine modifiée, caractère modifié, et "
                "maladie héréditaire."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Remarque : contexte africain --------------------------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "La drépanocytose touche une fraction importante de la "
                    "population en Afrique de l'Ouest. Les porteurs d'un "
                    "seul gène muté (hétérozygotes « AS ») sont "
                    "généralement en bonne santé et présentent une "
                    "résistance partielle au paludisme, ce qui explique le "
                    "maintien de ce gène dans ces régions où le paludisme "
                    "sévit.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        remarque.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Une remarque importante sur le contexte africain : la "
                "drépanocytose touche une fraction importante de la "
                "population en Afrique de l'Ouest. Les porteurs d'un seul "
                "gène muté, dits hétérozygotes A S, sont généralement en "
                "bonne santé, et présentent une résistance partielle au "
                "paludisme — ce qui explique le maintien de ce gène dans "
                "les régions où le paludisme sévit."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- À retenir : causes et caractère héréditaire des mutations --------------
        entete_causes = Text("Causes et transmission des mutations", font_size=22, color=YELLOW, weight="BOLD")
        entete_causes.next_to(titre, DOWN, buff=0.5)
        causes = _bullets(
            [
                "Les mutations surviennent spontanément (erreurs de copie "
                "de l'ADN) ou sous l'effet d'agents mutagènes : "
                "rayonnements (UV, rayons X), substances chimiques, "
                "certains virus.",
                "Une mutation n'a de conséquence sur la descendance que si "
                "elle touche des cellules de la lignée germinale (gamètes "
                "ou cellules qui les produisent) : elle est alors "
                "transmissible aux générations suivantes.",
            ],
            font_size=19,
            width=54,
        )
        causes.next_to(entete_causes, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Terminons par les causes et le caractère héréditaire des "
                "mutations. Elles surviennent spontanément, par erreur de "
                "copie de l'ADN, ou sous l'effet d'agents mutagènes : "
                "rayonnements ultraviolets ou rayons X, certaines "
                "substances chimiques, certains virus. Mais une mutation "
                "n'a de conséquence sur la descendance que si elle touche "
                "des cellules qui participent à la reproduction, les "
                "gamètes ou les cellules qui les produisent : c'est ce "
                "qu'on appelle la lignée germinale. Ce n'est que dans ce cas "
                "qu'elle devient transmissible aux générations suivantes."
            )
        ) as tracker:
            self.play(FadeIn(entete_causes))
            self.play(FadeIn(causes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(entete_causes), FadeOut(causes))
