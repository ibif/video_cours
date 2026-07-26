"""
scenes/SVT_Gametogenese_04.py — Chapitre 3 (1ereD, SVT), scène 04.

§ 3.3.1 La méiose : les deux divisions successives — méiose I détaillée
(prophase, métaphase, anaphase, télophase I) et méiose II, propriété du
résultat de la méiose, exemple à 2n=16 chromosomes, méthode pour retrouver
la formule chromosomique à chaque étape. Source : 1ereD/SVT.pdf, pages 34-36.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _chromosome_x(color=WHITE, size=0.45):
    """Schéma simplifié d'un chromosome à deux chromatides (forme en X)."""
    l1 = Line(UP * size, DOWN * size, color=color, stroke_width=6)
    l2 = Line(UP * size, DOWN * size, color=color, stroke_width=6)
    l1.rotate(0.35)
    l2.rotate(-0.35)
    centromere = Circle(radius=0.06, color=YELLOW, fill_opacity=1.0)
    return VGroup(l1, l2, centromere)


def _chromosome_bar(color=WHITE, size=0.4):
    """Schéma simplifié d'un chromosome à une seule chromatide (bâtonnet)."""
    return Line(UP * size, DOWN * size, color=color, stroke_width=7)


class MeioseDeuxDivisions(NotionScene):
    def construct(self):
        titre = scene_title("3.3.1 — La méiose : deux divisions successives")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition de la méiose --------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La méiose est une division cellulaire réductrice qui "
                    "comporte deux divisions successives (méiose I et "
                    "méiose II) précédées d'une seule réplication de "
                    "l'ADN. À partir d'une cellule diploïde à 2n=46, elle "
                    "produit quatre cellules haploïdes à n=23.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Comment une cellule diploïde peut-elle donner des cellules "
                "haploïdes ? C'est le rôle d'une division cellulaire "
                "particulière : la méiose, qui n'a lieu que dans les "
                "gonades, au cours de la gamétogenèse. La méiose est une "
                "division cellulaire réductrice qui comporte deux divisions "
                "successives, la méiose un et la méiose deux, précédées "
                "d'une seule réplication de l'ADN. À partir d'une cellule "
                "diploïde à deux n égale quarante-six chromosomes, elle "
                "produit quatre cellules haploïdes à n égale vingt-trois "
                "chromosomes. Avant la méiose, chaque chromosome a été "
                "recopié : il est formé de deux chromatides sœurs réunies "
                "par un centromère, avec l'aspect d'un X au microscope."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement 1 : méiose I --------------------------------------
        entete_m1 = Text("Méiose I (division réductionnelle)", font_size=25, color=YELLOW, weight="BOLD")
        entete_m1.next_to(titre, DOWN, buff=0.45)

        etapes_m1 = _bullets(
            [
                "Prophase I : les homologues s'apparient (bivalents) — "
                "un crossing-over peut se produire.",
                "Métaphase I : les bivalents se placent sur la plaque "
                "équatoriale, orientation indépendante et aléatoire.",
                "Anaphase I : les homologues se séparent et migrent aux "
                "pôles, chacun gardant ses deux chromatides.",
                "Télophase I : 2 cellules filles haploïdes (n), "
                "chromosomes encore à deux chromatides.",
            ],
            font_size=20,
            width=50,
        )
        etapes_m1.next_to(entete_m1, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La méiose un, ou première division, dite réductionnelle. "
                "En prophase un, les chromosomes homologues de chaque paire "
                "se rapprochent et s'accolent intimement : c'est "
                "l'appariement, qui forme des bivalents ; à ce moment peut "
                "se produire un crossing-over. En métaphase un, les "
                "bivalents se placent sur la plaque équatoriale de la "
                "cellule, avec une orientation indépendante et aléatoire "
                "pour chaque paire. En anaphase un, les deux chromosomes "
                "homologues de chaque paire se séparent et migrent vers les "
                "pôles opposés, chacun restant formé de ses deux "
                "chromatides. En télophase un, deux cellules filles se "
                "forment : elles sont haploïdes, mais leurs chromosomes "
                "comportent encore deux chromatides."
            )
        ) as tracker:
            self.play(FadeIn(entete_m1))
            self.play(FadeIn(etapes_m1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes_m1))

        # Petit schéma : une paire d'homologues qui s'apparie puis se sépare
        homo_pere = _chromosome_x(color=BLUE)
        homo_mere = _chromosome_x(color=RED)
        paire = VGroup(homo_pere, homo_mere).arrange(RIGHT, buff=0.15)
        paire.next_to(entete_m1, DOWN, buff=0.5).shift(LEFT * 3.3)
        label_paire = Text("Prophase I : bivalent (paire appariée)", font_size=18, color=WHITE)
        label_paire.next_to(paire, DOWN, buff=0.3)

        homo_pere2 = _chromosome_x(color=BLUE)
        homo_mere2 = _chromosome_x(color=RED)
        homo_pere2.next_to(entete_m1, DOWN, buff=0.5).shift(RIGHT * 2.0 + LEFT * 1.3)
        homo_mere2.next_to(entete_m1, DOWN, buff=0.5).shift(RIGHT * 4.0 + LEFT * 1.3)
        label_separes = Text("Anaphase I : homologues séparés\n(2 chromatides chacun)", font_size=18, color=WHITE)
        label_separes.next_to(VGroup(homo_pere2, homo_mere2), DOWN, buff=0.3)

        schema_m1 = VGroup(paire, label_paire, homo_pere2, homo_mere2, label_separes)

        with self.voiceover(
            text=(
                "Voici le schéma : à gauche, le bivalent formé par "
                "l'appariement des deux homologues en prophase un, l'un "
                "d'origine paternelle en bleu, l'autre d'origine maternelle "
                "en rouge. À droite, après l'anaphase un, les deux "
                "homologues sont séparés, chacun conservant encore ses deux "
                "chromatides."
            )
        ) as tracker:
            self.play(FadeIn(paire), FadeIn(label_paire))
            self.play(FadeIn(homo_pere2), FadeIn(homo_mere2), FadeIn(label_separes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_m1), FadeOut(schema_m1))

        # --- Raisonnement 2 : méiose II --------------------------------------
        entete_m2 = Text("Méiose II (division équationnelle)", font_size=25, color=YELLOW, weight="BOLD")
        entete_m2.next_to(titre, DOWN, buff=0.45)

        etapes_m2 = _bullets(
            [
                "Prophase II puis métaphase II : les chromosomes (deux "
                "chromatides) se placent à l'équateur de chaque cellule.",
                "Anaphase II : les deux chromatides sœurs de chaque "
                "chromosome se séparent.",
                "Télophase II : 4 cellules haploïdes (n), chromosomes "
                "désormais à une seule chromatide.",
            ],
            font_size=20,
            width=50,
        )
        etapes_m2.next_to(entete_m2, DOWN, buff=0.35)

        chrom_avant = _chromosome_x(color=GREEN)
        chrom_avant.next_to(entete_m2, DOWN, buff=3.2).shift(LEFT * 3.2)
        label_avant = Text("Avant l'anaphase II\n(2 chromatides)", font_size=17, color=WHITE)
        label_avant.next_to(chrom_avant, DOWN, buff=0.3)

        chrom_apres1 = _chromosome_bar(color=GREEN)
        chrom_apres2 = _chromosome_bar(color=GREEN)
        chrom_apres = VGroup(chrom_apres1, chrom_apres2).arrange(RIGHT, buff=0.5)
        chrom_apres.next_to(entete_m2, DOWN, buff=3.2).shift(RIGHT * 2.5)
        label_apres = Text("Après l'anaphase II\n(1 chromatide chacun)", font_size=17, color=WHITE)
        label_apres.next_to(chrom_apres, DOWN, buff=0.3)

        schema_m2 = VGroup(chrom_avant, label_avant, chrom_apres, label_apres)

        with self.voiceover(
            text=(
                "La méiose deux ressemble à une mitose. En prophase deux "
                "puis métaphase deux, les chromosomes, toujours à deux "
                "chromatides, se placent à l'équateur de chacune des deux "
                "cellules. En anaphase deux, les deux chromatides sœurs de "
                "chaque chromosome se séparent. En télophase deux, quatre "
                "cellules haploïdes se forment, dont les chromosomes sont "
                "désormais à une seule chromatide."
            )
        ) as tracker:
            self.play(FadeIn(entete_m2))
            self.play(FadeIn(etapes_m2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Le schéma le montre clairement : à gauche, un chromosome "
                "avant l'anaphase deux, encore formé de deux chromatides ; "
                "à droite, après l'anaphase deux, ces deux chromatides sont "
                "devenues deux chromosomes indépendants, à une seule "
                "chromatide chacun."
            )
        ) as tracker:
            self.play(FadeOut(etapes_m2))
            self.play(FadeIn(chrom_avant), FadeIn(label_avant))
            self.play(FadeIn(chrom_apres), FadeIn(label_apres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_m2), FadeOut(schema_m2))

        # --- Propriété : résultat de la méiose --------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Une cellule diploïde (2n chromosomes à deux "
                    "chromatides après réplication) donne, par méiose, "
                    "quatre cellules haploïdes à n chromosomes à une "
                    "chromatide. Le nombre de chromosomes est divisé par "
                    "deux : c'est pourquoi la méiose I est dite "
                    "« réductionnelle ».",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons cette propriété : une cellule diploïde, deux n "
                "chromosomes à deux chromatides après réplication, donne, "
                "par méiose, quatre cellules haploïdes, à n chromosomes à "
                "une chromatide. Le nombre de chromosomes est ainsi divisé "
                "par deux, c'est pourquoi la méiose un est dite "
                "réductionnelle."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple traité : cellule à 2n=16 ---------------------------------
        tableau_exemple = MathTex(
            r"""
            \begin{array}{lccc}
            \text{Étape} & \text{Cellules} & \text{Chromosomes} & \text{Chromatides} \\
            \text{Avant réplication} & 1 & 16\ (2n) & 1 \\
            \text{Après réplication} & 1 & 16\ (2n) & 2 \\
            \text{Fin méiose I} & 2 & 8\ (n) & 2 \\
            \text{Fin méiose II} & 4 & 8\ (n) & 1 \\
            \end{array}
            """,
            font_size=26,
            color=WHITE,
        )
        tableau_exemple.set(width=min(tableau_exemple.width, 10.5))

        exemple = example_box(tableau_exemple, box_width=11.5)
        exemple.next_to(titre, DOWN, buff=0.4)

        verif = Text(
            _wrap(
                "Vérification : 16 chromosomes × 2 chromatides = 32 "
                "chromatides au départ ; 4 cellules × 8 chromosomes × 1 "
                "chromatide = 32 chromatides à l'arrivée. La matière se "
                "conserve.",
                width=54,
            ),
            font_size=21,
            color=YELLOW,
        )
        verif.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Suivons le sort des chromosomes dans une cellule animale à "
                "deux n égale seize chromosomes qui entre en méiose. Avant "
                "réplication : une cellule, seize chromosomes, une "
                "chromatide. Après réplication, au début de la méiose un : "
                "toujours une cellule, seize chromosomes, mais deux "
                "chromatides. À la fin de la méiose un : deux cellules, "
                "huit chromosomes, deux chromatides. À la fin de la méiose "
                "deux : quatre cellules, huit chromosomes, une seule "
                "chromatide. Vérification : avant la méiose un, seize "
                "chromosomes à deux chromatides, soit trente-deux "
                "chromatides ; à la fin, quatre cellules à huit chromosomes "
                "à une chromatide, soit également trente-deux chromatides. "
                "La matière se conserve, tout est cohérent."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration() * 0.5)
            self.play(FadeIn(verif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(verif))

        # --- À retenir : méthode pour retrouver la formule --------------------
        methode = method_box(
            Text(
                _wrap(
                    "Pour ne jamais se tromper : 1) Avant la méiose I, "
                    "l'ADN a été répliqué mais le nombre de chromosomes "
                    "n'a pas changé — la cellule reste 2n (chromosomes à "
                    "deux chromatides). 2) Après la méiose I, le nombre de "
                    "chromosomes est divisé par deux — les cellules sont n "
                    "(encore deux chromatides). 3) Après la méiose II, les "
                    "chromatides se sont séparées — les cellules restent "
                    "n (une chromatide). En résumé : méiose I = on divise "
                    "les chromosomes par deux ; méiose II = on sépare les "
                    "chromatides.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour ne jamais se tromper dans un schéma de gamétogénèse, "
                "applique cette recette. Un : avant la méiose un, l'ADN a "
                "été répliqué, mais le nombre de chromosomes n'a pas "
                "changé, la cellule reste deux n, avec des chromosomes à "
                "deux chromatides. Deux : après la méiose un, le nombre de "
                "chromosomes est divisé par deux, les cellules sont n, avec "
                "des chromosomes encore à deux chromatides. Trois : après "
                "la méiose deux, les chromatides se sont séparées, les "
                "cellules restent n, mais à une seule chromatide. En "
                "résumé : méiose un, on divise les chromosomes par deux ; "
                "méiose deux, on sépare les chromatides."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège fréquent : croire qu'après la méiose I, les "
                    "chromosomes sont déjà réduits à une seule chromatide. "
                    "C'est faux : après la méiose I, les cellules sont "
                    "haploïdes (n) mais leurs chromosomes ont encore deux "
                    "chromatides — ce n'est qu'après la méiose II que "
                    "chaque chromosome passe à une seule chromatide.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent à éviter : croire qu'après la méiose un, "
                "les chromosomes sont déjà réduits à une seule chromatide. "
                "C'est faux : après la méiose un, les cellules sont "
                "haploïdes, mais leurs chromosomes possèdent encore deux "
                "chromatides ; ce n'est qu'après la méiose deux que chaque "
                "chromosome passe à une seule chromatide."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
