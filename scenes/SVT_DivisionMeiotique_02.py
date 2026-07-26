"""
scenes/SVT_DivisionMeiotique_02.py — Chapitre 2 (1ereD, SVT), scène 02.

§ 2.1 Les chromosomes et la formule chromosomique d'une espèce :
chromosome simple/dédoublé (visuel), chromosomes homologues, vocabulaire
(bivalent, enjambement, gamète), caryotype / diploïde / haploïde, tableau
des espèces, exemple du cacaoyer, méthode de lecture d'un caryotype.
Source : 1ereD/SVT.pdf, pages 18-20.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    MAROON,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.7, row_gap=0.3):
    """
    Construit un tableau à partir d'une matrice de Mobjects déjà créés
    (Text, MathTex, peu importe le mélange). Contrairement à un simple
    VGroup(*colonnes).arrange(...) par colonne indépendante, la hauteur de
    ligne est ICI commune à tout le tableau : chaque ligne est positionnée
    à un y fixe (indépendant du contenu), ce qui évite le décalage
    vertical cumulatif entre colonnes de nature différente (Text vs
    MathTex, ou lignes à accents/hauteurs de police légèrement variables).
    """
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


def _chromosome(color, dedouble=True, height=1.1, width=0.24, gap=0.08):
    """Schéma simple d'un chromosome : bâtonnet(s) + centromère (point)."""
    if not dedouble:
        rect = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
        dot = Dot(radius=0.055, color=YELLOW)
        dot.move_to(rect.get_center())
        return VGroup(rect, dot)
    left = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    right = left.copy()
    paire = VGroup(left, right).arrange(RIGHT, buff=gap)
    dot = Dot(radius=0.06, color=YELLOW)
    dot.move_to(paire.get_center())
    return VGroup(left, right, dot)


class ChromosomesEtFormuleChromosomique(NotionScene):
    def construct(self):
        titre = scene_title("2.1 — Chromosomes et formule chromosomique")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : chromosome simple / dédoublé --------------------------
        chr_simple = _chromosome(BLUE, dedouble=False)
        label_simple = Text("(a) non dédoublé\n1 chromatide", font_size=18, color=WHITE)
        label_simple.next_to(chr_simple, DOWN, buff=0.25)
        bloc_simple = VGroup(chr_simple, label_simple)

        chr_double = _chromosome(BLUE, dedouble=True)
        label_double = Text("(b) dédoublé\n2 chromatides sœurs", font_size=18, color=WHITE)
        label_double.next_to(chr_double, DOWN, buff=0.25)
        bloc_double = VGroup(chr_double, label_double)

        homologues = VGroup(_chromosome(BLUE, dedouble=True), _chromosome(MAROON, dedouble=True))
        homologues.arrange(RIGHT, buff=0.35)
        label_homologues = Text("(c) paire d'homologues\ndédoublés", font_size=18, color=WHITE)
        label_homologues.next_to(homologues, DOWN, buff=0.25)
        bloc_homologues = VGroup(homologues, label_homologues)

        schema = VGroup(bloc_simple, bloc_double, bloc_homologues).arrange(RIGHT, buff=1.1)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Avant de suivre la méiose étape par étape, il faut bien "
                "connaître son acteur principal : le chromosome. Un "
                "chromosome est une structure du noyau, constituée d'une "
                "longue molécule d'ADN associée à des protéines, et qui porte "
                "les gènes. Il possède un point d'étranglement appelé "
                "centromère, auquel se fixent les filaments du fuseau lors "
                "des divisions. Un chromosome est dit non dédoublé, ou "
                "simple, lorsqu'il est formé d'une seule chromatide, donc "
                "d'une seule molécule d'ADN. Après la réplication de l'ADN, "
                "il est dit dédoublé : il est alors formé de deux chromatides "
                "sœurs identiques, accolées au niveau du centromère."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(bloc_simple))
            self.play(FadeIn(bloc_double))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Deux chromosomes homologues, comme ici l'un d'origine "
                "paternelle en bleu et l'autre d'origine maternelle en "
                "bordeaux, peuvent eux aussi être dédoublés. Retiens bien ce "
                "point fondamental : même dédoublé, un chromosome reste un "
                "seul chromosome, car il ne possède qu'un seul centromère."
            )
        ) as tracker:
            self.play(FadeIn(bloc_homologues))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Piège immédiat : la règle d'or ----------------------------------
        piege_centromere = warning_box(
            Text(
                _wrap(
                    "On compte les chromosomes en comptant les centromères, "
                    "pas les chromatides. Un chromosome dédoublé = 1 "
                    "centromère = 1 seul chromosome, qui possède 2 "
                    "chromatides. Voir deux bâtonnets accolés et dire "
                    "« deux chromosomes » est l'erreur la plus fréquente.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        piege_centromere.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "C'est l'erreur la plus fréquente en classe : sur un schéma, "
                "voir deux bâtonnets accolés et compter deux chromosomes. "
                "Règle d'or à ne jamais oublier : on compte les chromosomes "
                "en comptant les centromères, pas les chromatides. Un "
                "chromosome dédoublé égale un seul centromère, donc un seul "
                "chromosome, qui possède deux chromatides."
            )
        ) as tracker:
            self.play(FadeIn(piege_centromere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_centromere))

        # --- Raisonnement : homologues + vocabulaire -------------------------
        definition_homologues = definition_box(
            Text(
                _wrap(
                    "Deux chromosomes sont homologues lorsqu'ils ont la même "
                    "taille, la même forme et portent les mêmes gènes aux "
                    "mêmes emplacements (locus). L'un est d'origine "
                    "paternelle, l'autre d'origine maternelle. Ils peuvent "
                    "porter des versions différentes d'un même gène, "
                    "appelées allèles.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition_homologues.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans une cellule, deux chromosomes sont dits homologues "
                "lorsqu'ils ont la même taille, la même forme, avec la même "
                "position du centromère, et portent les mêmes gènes aux "
                "mêmes emplacements, appelés locus. L'un des deux provient du "
                "père, il est d'origine paternelle ; l'autre provient de la "
                "mère, il est d'origine maternelle. Les deux homologues "
                "peuvent porter des versions différentes d'un même gène : ces "
                "versions s'appellent des allèles. C'est exactement la "
                "situation des enfants de Mamadou et Affoué : chacun a reçu, "
                "pour chaque paire, un chromosome du père et un chromosome de "
                "la mère."
            )
        ) as tracker:
            self.play(FadeIn(definition_homologues))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_homologues))

        entete_vocab = Text("Vocabulaire à maîtriser", font_size=26, color=YELLOW, weight="BOLD")
        entete_vocab.next_to(titre, DOWN, buff=0.5)
        vocab = _bullets(
            [
                "Bivalent (ou tétrade) : les deux homologues dédoublés "
                "accolés en 1ère division, soit 4 chromatides.",
                "Enjambement (crossing-over) : échange de segments entre "
                "deux chromatides non sœurs, en prophase I.",
                "Gamète : cellule reproductrice (spermatozoïde ou ovule).",
            ],
            width=50,
        )
        vocab.next_to(entete_vocab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Trois mots de vocabulaire à maîtriser dès maintenant. Le "
                "bivalent, ou tétrade : c'est l'ensemble formé par deux "
                "chromosomes homologues dédoublés accolés pendant la première "
                "division de la méiose, il contient donc quatre chromatides. "
                "L'enjambement, ou crossing-over : c'est un échange de "
                "segments entre deux chromatides non sœurs de deux "
                "homologues, pendant la prophase I. Et le gamète : la "
                "cellule reproductrice, spermatozoïde ou ovule chez l'être "
                "humain."
            )
        ) as tracker:
            self.play(FadeIn(entete_vocab))
            self.play(FadeIn(vocab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_vocab), FadeOut(vocab))

        # --- Caryotype, diploïde, haploïde + tableau des espèces -------------
        definition_caryotype = definition_box(
            Text(
                _wrap(
                    "Le caryotype est la présentation ordonnée des "
                    "chromosomes d'une cellule, classés par paires "
                    "d'homologues et par taille décroissante. Une cellule "
                    "diploïde (2n) possède les chromosomes par paires ; une "
                    "cellule haploïde (n) n'en possède qu'un seul "
                    "exemplaire de chaque sorte.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition_caryotype.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le caryotype est la présentation ordonnée de l'ensemble des "
                "chromosomes d'une cellule, classés par paires d'homologues "
                "et par taille décroissante. Une cellule qui possède les "
                "chromosomes par paires est dite diploïde, on note sa formule "
                "chromosomique deux n. Une cellule qui ne possède qu'un seul "
                "exemplaire de chaque sorte de chromosome est dite haploïde, "
                "on note sa formule n. Chez l'être humain, deux n égale "
                "quarante-six : vingt-trois paires de chromosomes, dont "
                "vingt-deux paires d'autosomes et une paire de gonosomes. Les "
                "gamètes, eux, sont haploïdes : n égale vingt-trois."
            )
        ) as tracker:
            self.play(FadeIn(definition_caryotype))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_caryotype))

        entete_tab = Text("Formule chromosomique de quelques espèces", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        species = [
            ("Être humain", "46", "23"),
            ("Maïs", "20", "10"),
            ("Cacaoyer", "20", "10"),
            ("Riz", "24", "12"),
            ("Mil", "14", "7"),
            ("Drosophile", "8", "4"),
        ]
        cell_matrix = [[
            Text("Espèce", font_size=20, color=YELLOW, weight="BOLD"),
            Text("2n", font_size=20, color=YELLOW, weight="BOLD"),
            Text("n", font_size=20, color=YELLOW, weight="BOLD"),
        ]]
        for nom, two, one in species:
            cell_matrix.append([
                Text(nom, font_size=20, color=WHITE),
                MathTex(f"2n={two}", font_size=22, color=WHITE),
                MathTex(f"n={one}", font_size=22, color=WHITE),
            ])
        tableau = _grid_table(cell_matrix, col_gap=0.6, row_gap=0.24)
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        tableau.scale(0.85)

        with self.voiceover(
            text=(
                "Le nombre deux n est caractéristique de chaque espèce. Chez "
                "l'être humain, deux n égale quarante-six. Chez le maïs et le "
                "cacaoyer, si important dans l'économie ivoirienne, deux n "
                "égale vingt. Chez le riz, deux n égale vingt-quatre ; chez le "
                "mil, deux n égale quatorze ; et chez la drosophile, la "
                "mouche du vinaigre bien connue en génétique, deux n égale "
                "huit."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : le cacaoyer -------------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Le caryotype du cacaoyer montre 20 chromosomes. Étape 1 : "
                    "caryotype d'une cellule ordinaire -> 2n=20. Étape 2 : "
                    "les chromosomes vont par paires -> 20÷2=10 paires "
                    "d'homologues. Étape 3 : un gamète (grain de pollen) est "
                    "haploïde -> il reçoit n=10 chromosomes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons le cacaoyer, arbre emblématique des plantations de "
                "l'ouest ivoirien. Son caryotype montre vingt chromosomes. "
                "Quelle est sa formule diploïde ? Combien de paires "
                "d'homologues possède-t-il ? Et combien de chromosomes "
                "contient un grain de pollen ? Étape 1 : le caryotype vient "
                "d'une cellule ordinaire, diploïde : la formule s'écrit deux n "
                "égale vingt. Étape 2 : les chromosomes vont par paires, le "
                "nombre de paires est vingt divisé par deux, soit dix paires. "
                "Étape 3 : un gamète est haploïde, il ne reçoit qu'un seul "
                "chromosome de chaque paire, donc n égale dix chromosomes."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : méthode de lecture d'un caryotype --------------------
        methode = method_box(
            _bullets(
                [
                    "Compte tous les chromosomes présents : ce total est 2n.",
                    "Associe les chromosomes deux par deux (même taille, même "
                    "centromère) : chaque couple est une paire d'homologues.",
                    "Le nombre de paires obtenu donne n.",
                    "Vérifie la cohérence : 2n est pair, et n=2n/2.",
                ],
                font_size=21,
                width=52,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour exploiter le caryotype d'une espèce inconnue, procède "
                "toujours dans le même ordre. Un : compte tous les "
                "chromosomes présents, ce total est deux n. Deux : associe les "
                "chromosomes deux par deux, même taille, même position du "
                "centromère : chaque couple formé est une paire d'homologues. "
                "Trois : le nombre de paires obtenu donne n. Quatre : vérifie "
                "la cohérence, chez une espèce à reproduction sexuée, deux n "
                "est un nombre pair et n égale deux n sur deux."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
