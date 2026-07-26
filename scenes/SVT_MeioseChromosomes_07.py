"""
scenes/SVT_MeioseChromosomes_07.py — Chapitre 2 (1ereC, SVT), scène 07.

§ Le brassage intrachromosomique : crossing-over en prophase I, chromatides
non sœurs, chromosomes recombinés (schéma avant/après) + conséquence sur la
descendance d'un couple (calcul 2²³ × 2²³ ≈ 7×10¹³ zygotes possibles).
Source : 1ereC/SVT.pdf, page 18.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title

PATERNEL = "#B5651D"
MATERNEL = "#2E8B57"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _chromatide(color, height=1.2, width=0.2, split_at=None, split_color=None):
    """Une chromatide simple ; si split_at (0..1) est fourni, la portion du
    haut (au-dessus de split_at * height) est colorée avec split_color pour
    représenter un segment échangé lors d'un crossing-over."""
    if split_at is None:
        return Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    haut_h = height * (1 - split_at)
    bas_h = height * split_at
    haut = Rectangle(width=width, height=haut_h, fill_color=split_color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    bas = Rectangle(width=width, height=bas_h, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    VGroup(haut, bas).arrange(DOWN, buff=0)
    return VGroup(haut, bas)


class BrassageIntrachromosomique(NotionScene):
    def construct(self):
        titre = scene_title("2.5 — Le brassage intrachromosomique")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : le crossing-over échange des segments ----------------------
        enonce = Text(
            _wrap(
                "En prophase I, au sein de chaque bivalent, des "
                "crossing-over échangent des segments entre chromatides "
                "NON SŒURS (une chromatide paternelle et une chromatide "
                "maternelle). Les points d'échange sont les chiasmas.",
                width=56,
            ),
            font_size=22,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En prophase I, au sein de chaque bivalent, des "
                "crossing-over échangent des segments entre chromatides non "
                "sœurs — une chromatide du chromosome paternel et une "
                "chromatide du chromosome maternel. Les points d'échange "
                "sont les chiasmas."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : avant / après crossing-over ------------
        avant_titre = Text("Avant le crossing-over", font_size=19, color=YELLOW, weight="BOLD")
        chr_p = VGroup(_chromatide(PATERNEL), _chromatide(PATERNEL)).arrange(RIGHT, buff=0.08)
        chr_m = VGroup(_chromatide(MATERNEL), _chromatide(MATERNEL)).arrange(RIGHT, buff=0.08)
        bivalent_avant = VGroup(chr_p, chr_m).arrange(RIGHT, buff=0.05)
        centromere_p = Dot(radius=0.05, color=YELLOW).move_to(chr_p.get_center())
        centromere_m = Dot(radius=0.05, color=YELLOW).move_to(chr_m.get_center())
        chiasma = Dot(radius=0.06, color=WHITE).move_to((chr_p[1].get_center() + chr_m[0].get_center()) / 2)
        chiasma_label = Text("chiasma", font_size=14, color=WHITE)
        chiasma_label.next_to(chiasma, DOWN, buff=0.15)

        bloc_avant = VGroup(avant_titre, VGroup(bivalent_avant, centromere_p, centromere_m, chiasma, chiasma_label))
        bloc_avant[1].next_to(bloc_avant[0], DOWN, buff=0.3)
        bloc_avant.next_to(titre, DOWN, buff=0.7)
        bloc_avant.to_edge(LEFT, buff=1.3)

        with self.voiceover(
            text=(
                "Voici un bivalent avant crossing-over : deux chromosomes "
                "homologues, chacun à deux chromatides. Les chromatides "
                "intérieures, l'une paternelle, l'autre maternelle, se "
                "croisent au niveau d'un chiasma."
            )
        ) as tracker:
            self.play(FadeIn(bloc_avant))
            self.wait(tracker.get_remaining_duration())

        # Après crossing-over : segment échangé sur les 2 chromatides internes
        apres_titre = Text("Après le crossing-over", font_size=19, color=YELLOW, weight="BOLD")
        chromatide_p1 = _chromatide(PATERNEL)
        chromatide_p2_recombinee = _chromatide(PATERNEL, split_at=0.5, split_color=MATERNEL)
        chromatide_m1_recombinee = _chromatide(MATERNEL, split_at=0.5, split_color=PATERNEL)
        chromatide_m2 = _chromatide(MATERNEL)

        col_p = VGroup(chromatide_p1, chromatide_p2_recombinee).arrange(RIGHT, buff=0.08)
        col_m = VGroup(chromatide_m1_recombinee, chromatide_m2).arrange(RIGHT, buff=0.08)
        bivalent_apres = VGroup(col_p, col_m).arrange(RIGHT, buff=0.05)

        label_recombine = Text("chromatides RECOMBINÉES\n(un fragment paternel + un fragment maternel)", font_size=13, color=WHITE)
        label_recombine.next_to(bivalent_apres, DOWN, buff=0.3)

        bloc_apres = VGroup(apres_titre, VGroup(bivalent_apres, label_recombine))
        bloc_apres[1].next_to(bloc_apres[0], DOWN, buff=0.3)
        bloc_apres.next_to(titre, DOWN, buff=0.7)
        bloc_apres.to_edge(RIGHT, buff=1.1)

        with self.voiceover(
            text=(
                "Après le crossing-over, les deux chromatides centrales "
                "sont recombinées : chacune porte à la fois un fragment "
                "d'origine paternelle et un fragment d'origine maternelle. "
                "Ce sont des chromosomes mixtes, qui n'existaient ni chez le "
                "père ni chez la mère."
            )
        ) as tracker:
            self.play(FadeIn(bloc_apres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_avant), FadeOut(bloc_apres))

        # --- Exemple traité : conséquence sur les gamètes -----------------------
        consequence = Text(
            _wrap(
                "Conséquence : après crossing-over, certaines chromatides "
                "sont recombinées. Les gamètes qui en héritent reçoivent des "
                "chromosomes « mixtes » qui n'existaient ni chez le père ni "
                "chez la mère.",
                width=56,
            ),
            font_size=22,
            color=WHITE,
        )
        consequence.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La conséquence est essentielle : après crossing-over, "
                "certaines chromatides sont recombinées, et les gamètes qui "
                "en héritent reçoivent des chromosomes mixtes, inédits, qui "
                "n'existaient ni chez le père ni chez la mère."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- À retenir : point clé sur le nombre de gamètes -----------------------
        point_cle = method_box(
            Text(
                _wrap(
                    "Les crossing-over rendent le nombre de types de "
                    "gamètes bien supérieur à 2ⁿ : il devient pratiquement "
                    "illimité.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.6,
        )
        point_cle.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé : les crossing-over rendent le nombre "
                "de types de gamètes bien supérieur à deux puissance n ; il "
                "devient pratiquement illimité."
            )
        ) as tracker:
            self.play(FadeIn(point_cle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(point_cle))

        # --- Conséquence sur la descendance d'un couple --------------------------
        descendance_titre = Text("Conséquence sur la descendance d'un couple", font_size=22, color=YELLOW, weight="BOLD")
        descendance_titre.next_to(titre, DOWN, buff=0.5)

        calcul = MathTex(
            r"2^{23} \times 2^{23} = 2^{46} \approx 7\times10^{13}",
            font_size=32,
            color=WHITE,
        )
        calcul.next_to(descendance_titre, DOWN, buff=0.4)

        texte_calcul = Text(
            _wrap(
                "Soit environ 70 000 milliards de zygotes génétiquement "
                "différents possibles pour un couple, sans même compter les "
                "crossing-over ! Deux enfants d'un même couple (hors vrais "
                "jumeaux) ne sont donc jamais génétiquement identiques.",
                width=54,
            ),
            font_size=20,
            color=WHITE,
        )
        texte_calcul.next_to(calcul, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Chez l'être humain, un homme peut produire plus de deux "
                "puissance vingt-trois types de spermatozoïdes, et une femme "
                "plus de deux puissance vingt-trois types d'ovules. Le "
                "nombre de zygotes génétiquement différents qu'un couple "
                "peut engendrer est donc supérieur à deux puissance "
                "vingt-trois fois deux puissance vingt-trois, soit deux "
                "puissance quarante-six, environ sept fois dix puissance "
                "treize : soit environ soixante-dix mille milliards de "
                "possibilités, sans même compter les crossing-over ! C'est "
                "pourquoi deux enfants d'un même couple, hors vrais jumeaux, "
                "ne sont jamais génétiquement identiques."
            )
        ) as tracker:
            self.play(FadeIn(descendance_titre))
            self.play(Write(calcul))
            self.play(FadeIn(texte_calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(descendance_titre), FadeOut(calcul), FadeOut(texte_calcul))
