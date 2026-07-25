"""
scenes/SVT_SyntheseProteines_03.py — Chapitre 5 (1ereD, SVT), scène 03.

§ 5.2.1-5.2.2 Le code génétique : pourquoi des mots de trois lettres
(raisonnement 4^1, 4^2, 4^3), définition codon / code génétique, extrait
du tableau du code génétique (une douzaine de codons, pas les 64 cases),
les quatre propriétés du code, remarque sur les codons particuliers
AUG / STOP. Source : 1ereD/SVT.pdf, pages 65-67.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    MAROON,
    ORANGE,
    RED,
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
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box

# Code couleur des bases, utilisé dans toutes les scènes du chapitre pour
# faciliter le repérage visuel des nucléotides.
BASE_COLORS = {"A": GREEN, "U": RED, "G": BLUE, "C": ORANGE, "T": MAROON}


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _codon(codon: str, font_size: int = 30) -> VGroup:
    """Un codon = un VGroup de lettres séparées (une par base), colorées."""
    lettres = VGroup(
        *[Text(base, font_size=font_size, color=BASE_COLORS.get(base, WHITE), weight="BOLD") for base in codon]
    )
    lettres.arrange(RIGHT, buff=0.04)
    return lettres


class LeCodeGenetique(NotionScene):
    def construct(self):
        titre = scene_title("5.2 — Le code génétique")
        titre.scale(0.75)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi trois lettres ? ------------------------------
        intro = Text(
            _wrap(
                "L'ARNm est écrit avec 4 « lettres » : A, U, G, C. Il faut "
                "pourtant coder 20 acides aminés. Combien de lettres par "
                "« mot » du code ?",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le message de l'ARN messager est écrit avec quatre "
                "lettres seulement : les bases A, U, G, C. Or il faut coder "
                "vingt acides aminés différents. Cherchons combien de "
                "lettres doit comporter chaque mot du code."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        calc1 = MathTex(r"4^1 = 4 \text{ possibilités} < 20 \quad \text{insuffisant}", font_size=32, color=WHITE)
        calc2 = MathTex(r"4^2 = 16 \text{ possibilités} < 20 \quad \text{insuffisant}", font_size=32, color=WHITE)
        calc3 = MathTex(r"4^3 = 64 \text{ possibilités} \geq 20 \quad \text{suffisant}", font_size=32, color=YELLOW)
        calculs = VGroup(calc1, calc2, calc3).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        calculs.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Des mots d'une seule lettre donnent quatre puissance un, "
                "soit quatre possibilités : insuffisant, car quatre est "
                "inférieur à vingt. Des mots de deux lettres donnent quatre "
                "puissance deux, soit seize possibilités : encore "
                "insuffisant. Des mots de trois lettres donnent quatre "
                "puissance trois, soit soixante-quatre possibilités : "
                "suffisant, car soixante-quatre est supérieur ou égal à "
                "vingt. La cellule utilise donc des mots de trois lettres."
            )
        ) as tracker:
            self.play(Write(calc1))
            self.play(Write(calc2))
            self.play(Write(calc3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calculs))

        # --- Raisonnement : définition codon / code génétique --------------
        def_codon = definition_box(
            Text(
                _wrap(
                    "Un codon est une suite de trois nucléotides "
                    "consécutifs de l'ARNm. Le code génétique est "
                    "l'ensemble des correspondances entre les 64 codons "
                    "possibles et les acides aminés (ou les signaux "
                    "d'arrêt). Chaque codon désigne un seul acide aminé "
                    "(ou un signal).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        def_codon.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un codon est une suite de trois nucléotides consécutifs de "
                "l'ARNm. Le code génétique est l'ensemble des "
                "correspondances entre les soixante-quatre codons possibles "
                "et les acides aminés, ou les signaux d'arrêt. Chaque codon "
                "désigne un seul acide aminé, ou un seul signal."
            )
        ) as tracker:
            self.play(FadeIn(def_codon))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_codon))

        # --- Exemple : extrait du tableau du code génétique -----------------
        entete_tab = Text(
            "Extrait du tableau du code génétique", font_size=25, color=YELLOW, weight="BOLD"
        )
        entete_tab.next_to(titre, DOWN, buff=0.5)

        correspondances = [
            ("UUU", "Phe"), ("UUA", "Leu"), ("UCU", "Ser"),
            ("UAU", "Tyr"), ("UAA", "STOP"), ("UGA", "STOP"),
            ("AUG", "Met (init.)"), ("AAG", "Lys"),
            ("GGC", "Gly"), ("CAA", "Gln"),
        ]
        lignes = VGroup()
        for codon, aa in correspondances:
            fleche = Text("→", font_size=24, color=WHITE)
            aa_txt = Text(aa, font_size=24, color=YELLOW if aa == "STOP" else WHITE)
            ligne = VGroup(_codon(codon, font_size=24), fleche, aa_txt).arrange(RIGHT, buff=0.25)
            lignes.add(ligne)
        col1 = VGroup(*lignes[:5]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        col2 = VGroup(*lignes[5:]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        tableau = VGroup(col1, col2).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        tableau.next_to(entete_tab, DOWN, buff=0.4)

        note_tab = Text(
            "(le tableau complet compte 64 codons — voir le manuel)",
            font_size=18,
            color=WHITE,
        )
        note_tab.next_to(tableau, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici un extrait utile du tableau du code génétique : "
                "U U U et U U C donnent la phénylalanine ; U U A et U U G "
                "donnent la leucine ; les codons commençant par U C donnent "
                "la sérine ; U A U et U A C donnent la tyrosine ; U A A, "
                "U A G et U G A sont des codons STOP, sans acide aminé ; "
                "A U G donne la méthionine et sert aussi de codon "
                "d'initiation ; A A G donne la lysine ; G G C donne la "
                "glycine ; C A A donne la glutamine. Le tableau complet "
                "comporte soixante-quatre codons : il serait illisible à "
                "l'écran, mais il figure entièrement dans votre manuel."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.play(FadeIn(note_tab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau), FadeOut(note_tab))

        # --- À retenir : les quatre propriétés du code ----------------------
        proprietes = property_box(
            _bullets(
                [
                    "Universel : un même codon désigne le même acide aminé "
                    "chez presque tous les êtres vivants (AUG = Met "
                    "partout).",
                    "Dégénéré : plusieurs codons peuvent désigner le même "
                    "acide aminé (la leucine a 6 codons). 61 codons codent "
                    "un acide aminé, 3 sont des STOP.",
                    "Sans ponctuation : les codons se suivent sans "
                    "séparation, lecture continue.",
                    "Sans chevauchement : chaque nucléotide appartient à "
                    "un seul codon.",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.2,
        )
        proprietes.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le code génétique possède quatre propriétés à connaître. "
                "Il est universel : un même codon désigne le même acide "
                "aminé chez presque tous les êtres vivants, de la bactérie "
                "à l'Homme ; A U G code la méthionine partout, ce qui est "
                "une preuve de la parenté de tous les êtres vivants. Il est "
                "dégénéré : plusieurs codons différents peuvent désigner un "
                "même acide aminé, par exemple la leucine possède six "
                "codons ; sur soixante-quatre codons, soixante et un "
                "désignent des acides aminés et trois sont des codons "
                "STOP. Il est sans ponctuation : les codons se suivent sans "
                "séparation, la lecture est continue du début à la fin du "
                "message. Il est sans chevauchement : chaque nucléotide "
                "appartient à un seul codon, après avoir lu un codon, la "
                "cellule passe aux trois nucléotides suivants."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Remarque : les codons particuliers -----------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Les codons particuliers : AUG a un double rôle, il "
                    "code la méthionine ET sert de codon d'initiation, "
                    "signal de départ de la traduction. UAA, UAG et UGA "
                    "sont les trois codons STOP : ils ne codent aucun "
                    "acide aminé, ils commandent l'arrêt de la fabrication "
                    "de la protéine.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux remarques sur les codons particuliers. A U G a un "
                "double rôle : il code la méthionine, et il sert de codon "
                "d'initiation, c'est-à-dire de signal de départ de la "
                "traduction. U A A, U A G et U G A sont les trois codons "
                "STOP : ils ne codent aucun acide aminé, ils commandent "
                "l'arrêt de la fabrication de la protéine."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(remarque))
