"""
scenes/SVT_Gametogenese_05.py — Chapitre 3 (1ereD, SVT), scène 05.

§ 3.3.2-3.3.3 Le crossing-over et le brassage génétique (brassage inter- et
intrachromosomique, propriété 2^n, exemple des zygotes ≈7×10^13) puis
méiose et mitose : ne pas confondre (tableau comparatif, piège anaphase
I/II). Source : 1ereD/SVT.pdf, pages 36-38.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    ORANGE,
    ORIGIN,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class BrassageGenetiqueMeioseMitose(NotionScene):
    def construct(self):
        titre = scene_title("3.3.2-3.3.3 — Brassage génétique ; méiose vs mitose")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le brassage interchromosomique -------------------------
        intro = Text(
            _wrap(
                "La méiose ne se contente pas de diviser le nombre de "
                "chromosomes par deux : elle brasse le patrimoine "
                "héréditaire, si bien que les quatre cellules obtenues ne "
                "sont jamais identiques entre elles.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La méiose ne se contente pas de diviser le nombre de "
                "chromosomes par deux : elle brasse le patrimoine "
                "héréditaire, si bien que les quatre cellules obtenues ne "
                "sont jamais identiques entre elles."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        entete_inter = Text("Brassage interchromosomique", font_size=25, color=YELLOW, weight="BOLD")
        entete_inter.next_to(titre, DOWN, buff=0.45)

        explication_inter = Text(
            _wrap(
                "En métaphase I, chaque paire d'homologues s'oriente au "
                "hasard, indépendamment des autres paires. Pour une "
                "cellule à 2n=4 (deux paires), il y a déjà 2²=4 "
                "répartitions possibles.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        explication_inter.next_to(entete_inter, DOWN, buff=0.35)

        # Schéma : deux orientations possibles pour 2 paires (2n=4)
        def _paire(color1, color2):
            c1 = Circle(radius=0.16, color=color1, fill_opacity=0.9)
            c2 = Circle(radius=0.16, color=color2, fill_opacity=0.9)
            return VGroup(c1, c2).arrange(RIGHT, buff=0.1)

        orient_a = VGroup(_paire(BLUE, BLUE), _paire(RED, RED)).arrange(DOWN, buff=0.35)
        orient_b = VGroup(
            VGroup(Circle(radius=0.16, color=BLUE, fill_opacity=0.9), Circle(radius=0.16, color=RED, fill_opacity=0.9)).arrange(RIGHT, buff=0.1),
            VGroup(Circle(radius=0.16, color=RED, fill_opacity=0.9), Circle(radius=0.16, color=BLUE, fill_opacity=0.9)).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.35)
        schema_orient = VGroup(orient_a, orient_b).arrange(RIGHT, buff=1.5)
        schema_orient.next_to(explication_inter, DOWN, buff=0.4)
        label_orient = Text("Deux orientations possibles parmi\nles 2² = 4 répartitions", font_size=18, color=YELLOW)
        label_orient.next_to(schema_orient, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Premier mécanisme : le brassage interchromosomique, entre "
                "chromosomes. En métaphase un, chaque paire d'homologues "
                "s'oriente au hasard : le chromosome d'origine paternelle "
                "et le chromosome d'origine maternelle d'une même paire se "
                "répartissent indépendamment de ceux des autres paires. "
                "Pour une cellule à deux n égale quatre, c'est-à-dire deux "
                "paires, il y a déjà deux puissance deux égale quatre "
                "répartitions possibles."
            )
        ) as tracker:
            self.play(FadeIn(entete_inter))
            self.play(FadeIn(explication_inter))
            self.play(FadeIn(schema_orient), FadeIn(label_orient))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_inter), FadeOut(explication_inter), FadeOut(schema_orient), FadeOut(label_orient))

        # --- Propriété : nombre de gamètes différents ------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Une espèce à n paires de chromosomes peut produire, "
                    "sans même compter les crossing-overs, 2^n types de "
                    "gamètes génétiquement différents. Chez l'être humain "
                    "(n=23) : 2^23=8 388 608 types de spermatozoïdes ou "
                    "d'ovules différents.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On en tire une propriété générale : une espèce à n paires "
                "de chromosomes peut produire, sans même compter les "
                "crossing-overs, deux puissance n types de gamètes "
                "génétiquement différents. Chez l'être humain, n égale "
                "vingt-trois : deux puissance vingt-trois égale huit "
                "millions trois cent quatre-vingt-huit mille six cent huit "
                "types de spermatozoïdes ou d'ovules différents."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Raisonnement : brassage intrachromosomique -----------------------
        entete_intra = Text("Brassage intrachromosomique (crossing-over)", font_size=23, color=YELLOW, weight="BOLD")
        entete_intra.next_to(titre, DOWN, buff=0.45)

        # Schéma : deux chromatides qui échangent un segment (chiasma)
        avant1 = VGroup(
            Line(UP * 0.5, DOWN * 0.5, color=BLUE, stroke_width=7),
            Line(UP * 0.5, DOWN * 0.5, color=RED, stroke_width=7),
        ).arrange(RIGHT, buff=0.2)
        avant1.next_to(entete_intra, DOWN, buff=0.5).shift(LEFT * 3.2)
        label_avant_co = Text("Avant : chromatides\nnon recombinées", font_size=16, color=WHITE)
        label_avant_co.next_to(avant1, DOWN, buff=0.25)

        # Après crossing-over : segments échangés (couleur mixte en bas)
        seg1_haut = Line(UP * 0.5, ORIGIN, color=BLUE, stroke_width=7)
        seg1_bas = Line(ORIGIN, DOWN * 0.5, color=RED, stroke_width=7)
        chrom1_apres = VGroup(seg1_haut, seg1_bas)
        seg2_haut = Line(UP * 0.5, ORIGIN, color=RED, stroke_width=7)
        seg2_bas = Line(ORIGIN, DOWN * 0.5, color=BLUE, stroke_width=7)
        chrom2_apres = VGroup(seg2_haut, seg2_bas)
        apres1 = VGroup(chrom1_apres, chrom2_apres).arrange(RIGHT, buff=0.2)
        apres1.next_to(entete_intra, DOWN, buff=0.5).shift(RIGHT * 2.8)
        label_apres_co = Text("Après : chiasma et\néchange de fragments", font_size=16, color=WHITE)
        label_apres_co.next_to(apres1, DOWN, buff=0.25)

        schema_co = VGroup(avant1, label_avant_co, apres1, label_apres_co)

        with self.voiceover(
            text=(
                "Second mécanisme : le brassage intrachromosomique, à "
                "l'intérieur d'un chromosome. En prophase un, les "
                "chromatides des deux homologues accolés peuvent se "
                "croiser en des points appelés chiasmas et échanger des "
                "fragments : c'est le crossing-over, ou enjambement. Les "
                "chromosomes transmis au gamète sont alors recombinés : ils "
                "portent un mélange des informations d'origine paternelle "
                "et maternelle. Ce second brassage multiplie encore "
                "considérablement la diversité."
            )
        ) as tracker:
            self.play(FadeIn(entete_intra))
            self.play(FadeIn(avant1), FadeIn(label_avant_co))
            self.play(FadeIn(apres1), FadeIn(label_apres_co))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_intra), FadeOut(schema_co))

        # --- Exemple traité : zygotes possibles d'un couple --------------------
        exemple = example_box(
            Text(
                _wrap(
                    "1) Le père produit 2^23=8 388 608 types de "
                    "spermatozoïdes. 2) La mère produit 2^23=8 388 608 "
                    "types d'ovules. 3) Chaque rencontre est un tirage au "
                    "sort parmi 2^23×2^23=2^46=70 368 744 177 664≈7,0×10^13. "
                    "Un couple peut engendrer environ 70 000 milliards "
                    "d'enfants génétiquement différents, sans compter les "
                    "crossing-overs.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Calculons le nombre de zygotes différents qu'un couple "
                "humain peut engendrer, en ne tenant compte que du brassage "
                "interchromosomique. Un : le père peut produire deux "
                "puissance vingt-trois, soit huit millions trois cent "
                "quatre-vingt-huit mille six cent huit types de "
                "spermatozoïdes. Deux : la mère peut produire le même "
                "nombre de types d'ovules. Trois : chaque rencontre "
                "spermatozoïde-ovule est un tirage au sort parmi toutes les "
                "combinaisons possibles, soit deux puissance vingt-trois "
                "fois deux puissance vingt-trois, égale deux puissance "
                "quarante-six, environ soixante-dix mille milliards. Un "
                "même couple peut donc engendrer environ soixante-dix mille "
                "milliards d'enfants génétiquement différents, sans compter "
                "les crossing-overs. C'est pourquoi deux enfants d'une même "
                "fratrie, hors vrais jumeaux, ne se ressemblent jamais "
                "totalement."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : tableau méiose vs mitose -------------------------------
        entete_tab = Text("Méiose ou mitose ? Le tableau comparatif", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        mitose_col = VGroup(
            Text("Mitose", font_size=22, color=BLUE, weight="BOLD"),
            Text("Lieu : toutes les cellules\nsomatiques", font_size=17, color=WHITE),
            Text("Divisions : 1", font_size=17, color=WHITE),
            Text("Cellules filles : 2", font_size=17, color=WHITE),
            Text("Formule : 2n → 2n\n(conservée)", font_size=17, color=WHITE),
            Text("Résultat : cellules\nidentiques", font_size=17, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        meiose_col = VGroup(
            Text("Méiose", font_size=22, color=ORANGE, weight="BOLD"),
            Text("Lieu : gonades\n(gamétogénèse)", font_size=17, color=WHITE),
            Text("Divisions : 2 successives", font_size=17, color=WHITE),
            Text("Cellules filles : 4", font_size=17, color=WHITE),
            Text("Formule : 2n → n\n(divisée par deux)", font_size=17, color=WHITE),
            Text("Résultat : cellules\ntoutes différentes", font_size=17, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        tableau = VGroup(mitose_col, meiose_col).arrange(RIGHT, buff=1.3, aligned_edge=UP)
        tableau.next_to(entete_tab, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résumons dans un tableau pour ne plus jamais confondre "
                "méiose et mitose. Le lieu : la mitose a lieu dans toutes "
                "les cellules somatiques, la méiose uniquement dans les "
                "gonades, au cours de la gamétogénèse. Le nombre de "
                "divisions : une seule pour la mitose, deux successives "
                "pour la méiose. Le nombre de cellules filles : deux pour "
                "la mitose, quatre pour la méiose. La formule "
                "chromosomique : conservée, deux n vers deux n, pour la "
                "mitose ; divisée par deux, deux n vers n, pour la méiose. "
                "Et les cellules obtenues : identiques à la cellule mère "
                "pour la mitose ; toutes différentes, grâce au brassage, "
                "pour la méiose."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(mitose_col))
            self.play(FadeIn(meiose_col))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège à éviter : anaphase I ≠ anaphase II --------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Erreur classique des élèves : écrire qu'en anaphase I "
                    "« les chromatides se séparent ». C'est faux : en "
                    "anaphase I, ce sont les chromosomes homologues qui se "
                    "séparent (chacun garde ses deux chromatides) ; la "
                    "séparation des chromatides sœurs n'a lieu qu'en "
                    "anaphase II.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Erreur classique des élèves : écrire qu'en anaphase un, "
                "les chromatides se séparent. C'est faux : en anaphase un, "
                "ce sont les chromosomes homologues qui se séparent, chacun "
                "gardant ses deux chromatides ; la séparation des "
                "chromatides sœurs n'a lieu qu'en anaphase deux."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
