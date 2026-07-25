"""
scenes/SVT_SyntheseProteines_07.py — Chapitre 5 (1ereD, SVT), scène 07.

§ 5.5.1-5.5.2 Les mutations : définition (mutation, allèle), héréditaire
ou non (cellule somatique / cellule reproductrice), les trois types de
mutation (substitution, délétion, insertion) et leurs conséquences,
exemple traité de classement d'une mutation (CAA -> UAA).
Source : 1ereD/SVT.pdf, pages 73-74.
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
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box

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
    lettres = VGroup(
        *[Text(base, font_size=font_size, color=BASE_COLORS.get(base, WHITE), weight="BOLD") for base in codon]
    )
    lettres.arrange(RIGHT, buff=0.04)
    return lettres


class LesMutations(NotionScene):
    def construct(self):
        titre = scene_title("5.5 — Les mutations")
        titre.scale(0.8)
        titre.to_edge(UP)

        # --- Énoncé : définition mutation / allèle ---------------------------
        def_mutation = definition_box(
            Text(
                _wrap(
                    "Une mutation est une modification de la séquence des "
                    "nucléotides de l'ADN. Une mutation qui touche un gène "
                    "peut modifier la protéine correspondante et donc un "
                    "caractère de l'individu. Les différentes versions "
                    "d'un même gène, produites par les mutations, "
                    "s'appellent des allèles.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_mutation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une mutation est une modification de la séquence des "
                "nucléotides de l'ADN. Une mutation qui touche un gène peut "
                "modifier la protéine correspondante et donc un caractère "
                "de l'individu. Les différentes versions d'un même gène, "
                "produites par les mutations au cours de l'évolution, "
                "s'appellent des allèles."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_mutation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_mutation))

        heredite = warning_box(
            Text(
                _wrap(
                    "Héréditaire ou non ? Une mutation survenue dans une "
                    "cellule du corps (cellule somatique) ne touche que "
                    "l'individu ; seule une mutation présente dans les "
                    "cellules reproductrices (gamètes ou leurs "
                    "précurseurs) peut être transmise à la descendance.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        heredite.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une mutation est-elle toujours héréditaire ? Non. Une "
                "mutation survenue dans une cellule du corps, une cellule "
                "somatique, ne touche que l'individu. Seule une mutation "
                "présente dans les cellules reproductrices, les gamètes ou "
                "leurs précurseurs, peut être transmise à la descendance."
            )
        ) as tracker:
            self.play(FadeIn(heredite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(heredite))

        # --- Raisonnement : les trois types de mutation (tableau) -----------
        entete_tab = Text("Les trois types de mutation", font_size=27, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        col_type = VGroup(
            Text("Type", font_size=20, color=YELLOW, weight="BOLD"),
            Text("Substitution", font_size=19, color=WHITE),
            Text("Délétion", font_size=19, color=WHITE),
            Text("Insertion", font_size=19, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        col_def = VGroup(
            Text("Ce qui se passe", font_size=20, color=YELLOW, weight="BOLD"),
            Text(_wrap("une base est remplacée par une autre", width=26), font_size=18, color=WHITE),
            Text(_wrap("une base est perdue", width=26), font_size=18, color=WHITE),
            Text(_wrap("une base est ajoutée", width=26), font_size=18, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        col_cons = VGroup(
            Text("Conséquence", font_size=20, color=YELLOW, weight="BOLD"),
            Text(_wrap("silencieuse, faux-sens ou non-sens", width=26), font_size=18, color=WHITE),
            Text(_wrap("décalage du cadre de lecture", width=26), font_size=18, color=WHITE),
            Text(_wrap("décalage du cadre de lecture", width=26), font_size=18, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        tableau = VGroup(col_type, col_def, col_cons).arrange(RIGHT, buff=0.7, aligned_edge=UP)
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        tableau.scale(0.92)

        with self.voiceover(
            text=(
                "Il existe trois types de mutation. La substitution : une "
                "base est remplacée par une autre ; la conséquence peut "
                "être silencieuse, si l'acide aminé reste le même, "
                "faux-sens, si un acide aminé est changé, ou non-sens, si "
                "un codon STOP apparaît. La délétion : une base est "
                "perdue ; tous les codons suivants sont alors décalés, "
                "c'est le décalage du cadre de lecture. L'insertion : une "
                "base est ajoutée ; elle provoque, elle aussi, un décalage "
                "du cadre de lecture pour tous les codons suivants."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : classer une mutation --------------------------
        entete_ex = Text("Exemple : classer une mutation", font_size=25, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        arnm_normal = VGroup(
            Text("Normal :", font_size=20, color=WHITE),
            _codon("AUG", font_size=26), _codon("UUC", font_size=26), _codon("CAA", font_size=26), _codon("GCU", font_size=26),
        ).arrange(RIGHT, buff=0.25)
        arnm_mute = VGroup(
            Text("Muté :", font_size=20, color=WHITE),
            _codon("AUG", font_size=26), _codon("UUC", font_size=26), _codon("UAA", font_size=26), _codon("GCU", font_size=26),
        ).arrange(RIGHT, buff=0.25)
        sequences = VGroup(arnm_normal, arnm_mute).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        sequences.next_to(entete_ex, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un ARNm normal contient la suite A U G, U U C, C A A, G C "
                "U. Après mutation, on lit A U G, U U C, U A A, G C U. "
                "Décrivons cette mutation et sa conséquence."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(sequences))
            self.wait(tracker.get_remaining_duration())

        analyse = example_box(
            Text(
                _wrap(
                    "Les 2 premiers codons sont inchangés. Le 3e codon "
                    "passe de CAA à UAA : une seule base a changé (C -> "
                    "U) = substitution. CAA code Gln ; UAA est un codon "
                    "STOP : la traduction s'arrête (protéine tronquée, "
                    "Met-Phe au lieu de Met-Phe-Gln-Ala). C'est une "
                    "substitution non-sens.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        analyse.next_to(sequences, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On compare codon par codon : A U G et U U C sont "
                "inchangés ; le troisième codon est passé de C A A à U A "
                "A, la première base, C, a été remplacée par U, c'est donc "
                "une substitution. Normalement, C A A code la glutamine ; "
                "U A A est un codon STOP. La traduction s'arrête donc "
                "prématurément : la protéine obtenue est raccourcie, "
                "méthionine, phénylalanine seulement, au lieu de "
                "méthionine, phénylalanine, glutamine, alanine. Une telle "
                "substitution qui crée un codon STOP est dite non-sens ; "
                "elle est en général grave car la protéine tronquée ne "
                "fonctionne plus."
            )
        ) as tracker:
            self.play(FadeIn(analyse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(sequences), FadeOut(analyse))

        # --- À retenir : méthode de classement --------------------------------
        methode = method_box(
            _bullets(
                [
                    "Comparer les deux séquences codon par codon pour "
                    "repérer la ou les bases changées.",
                    "1 base changée sans ajout/perte -> substitution "
                    "(silencieuse, faux-sens ou non-sens selon le nouvel "
                    "acide aminé).",
                    "1 base perdue ou ajoutée -> délétion ou insertion : "
                    "tout le cadre de lecture en aval est décalé.",
                    "Toujours traduire les deux versions pour comparer les "
                    "deux protéines obtenues.",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Pour classer une mutation, procédez ainsi. Comparez les "
                "deux séquences codon par codon pour repérer la ou les "
                "bases changées. Si une seule base a changé sans qu'aucune "
                "base ne soit ajoutée ou perdue, c'est une substitution, "
                "silencieuse, faux-sens ou non-sens selon le nouvel acide "
                "aminé obtenu. Si une base a été perdue ou ajoutée, c'est "
                "une délétion ou une insertion : tout le cadre de lecture "
                "en aval est alors décalé. Traduisez toujours les deux "
                "versions pour comparer les deux protéines obtenues."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : substitution vs délétion/insertion --------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre la gravité des trois types : une "
                    "substitution ne modifie qu'un seul codon (parfois "
                    "aucun changement, si elle est silencieuse). Une "
                    "délétion ou une insertion, elles, décalent le cadre "
                    "de lecture : TOUS les codons suivants sont modifiés, "
                    "ce qui est en général bien plus grave.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre la gravité des trois types de "
                "mutation. Une substitution ne modifie qu'un seul codon, et "
                "elle est parfois même sans effet, si elle est "
                "silencieuse. Une délétion ou une insertion, elles, "
                "décalent le cadre de lecture : tous les codons suivants "
                "sont modifiés, ce qui est en général bien plus grave pour "
                "la protéine."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
