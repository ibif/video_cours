"""
scenes/SVT_MeioseChromosomes_03.py — Chapitre 2 (1ereC, SVT), scène 03.

§ Interphase (réplication de l'ADN, Q→2Q) + Prophase I en détail
(condensation, synapsis, bivalents/tétrades, crossing-over aux chiasmas,
disparition de l'enveloppe nucléaire) + piège "une seule réplication pour
deux divisions".
Source : 1ereC/SVT.pdf, pages 14-15.
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
from shapes.boxes import definition_box, scene_title, warning_box

PATERNEL = "#B5651D"
MATERNEL = "#2E8B57"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _chromosome_1_chromatide(color=WHITE, height=1.2, width=0.2):
    barre = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    centromere = Dot(radius=0.05, color=YELLOW)
    centromere.move_to(barre.get_center())
    return VGroup(barre, centromere)


def _chromosome_2_chromatides(color=WHITE, height=1.2, width=0.2, gap=0.08):
    gauche = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    droite = gauche.copy()
    paire = VGroup(gauche, droite).arrange(RIGHT, buff=gap)
    centromere = Dot(radius=0.06, color=YELLOW)
    centromere.move_to(paire.get_center())
    return VGroup(gauche, droite, centromere)


class InterphaseEtProphaseI(NotionScene):
    def construct(self):
        titre = scene_title("2.2 — Interphase et prophase I")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : l'interphase, une seule réplication -----------------------
        interphase_txt = Text(
            _wrap(
                "Avant la méiose, la cellule mère effectue une interphase "
                "au cours de laquelle son ADN est répliqué (phase S). "
                "Chaque chromosome passe ainsi de 1 chromatide à 2 "
                "chromatides sœurs identiques.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        interphase_txt.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avant d'entrer en méiose, la cellule mère effectue une "
                "interphase, au cours de laquelle son ADN est répliqué. "
                "Chaque chromosome passe ainsi d'une chromatide à deux "
                "chromatides sœurs identiques."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(interphase_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interphase_txt))

        # --- Animation du raisonnement : Q -> 2Q --------------------------------
        avant = VGroup(_chromosome_1_chromatide(), _chromosome_1_chromatide()).arrange(RIGHT, buff=0.4)
        apres = VGroup(_chromosome_2_chromatides(), _chromosome_2_chromatides()).arrange(RIGHT, buff=0.4)
        fleche_txt = MathTex(r"\text{réplication}", font_size=20, color=YELLOW)
        bloc = VGroup(avant, fleche_txt, apres).arrange(RIGHT, buff=0.6)
        bloc.next_to(titre, DOWN, buff=1.0)

        label_avant = Text("2n=4 à 1 chromatide, ADN = Q", font_size=17, color=WHITE)
        label_avant.next_to(avant, DOWN, buff=0.35)
        label_apres = Text("2n=4 à 2 chromatides, ADN = 2Q", font_size=17, color=WHITE)
        label_apres.next_to(apres, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Avant l'interphase, la cellule possède deux n chromosomes "
                "à une chromatide, pour une quantité d'ADN notée Q. Après "
                "l'interphase, elle possède toujours deux n chromosomes, "
                "mais désormais à deux chromatides chacun, pour une "
                "quantité d'ADN doublée, deux Q."
            )
        ) as tracker:
            self.play(FadeIn(avant), FadeIn(label_avant))
            self.play(Write(fleche_txt))
            self.play(FadeIn(apres), FadeIn(label_apres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc), FadeOut(label_avant), FadeOut(label_apres))

        # --- Prophase I : condensation, synapsis, bivalent ----------------------
        sous_titre = Text("Prophase I — la phase la plus riche en événements", font_size=22, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        chr_p = _chromosome_2_chromatides(color=PATERNEL, height=1.3)
        chr_m = _chromosome_2_chromatides(color=MATERNEL, height=1.3)
        separes = VGroup(chr_p, chr_m).arrange(RIGHT, buff=0.9)
        separes.next_to(sous_titre, DOWN, buff=0.6)
        label_separes = Text("chromosomes homologues condensés, encore séparés", font_size=16, color=WHITE)
        label_separes.next_to(separes, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "En prophase I, les chromosomes se condensent, c'est-à-dire "
                "se spiralisent, et deviennent visibles. Voici les deux "
                "chromosomes homologues d'une paire, l'un d'origine "
                "paternelle, l'autre d'origine maternelle, encore séparés."
            )
        ) as tracker:
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(separes), FadeIn(label_separes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_separes))

        # Rapprochement -> bivalent (synapsis)
        bivalent_label = Text("synapsis : appariement intime -> BIVALENT (tétrade, 4 chromatides)", font_size=16, color=WHITE)
        bivalent_label.next_to(separes, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Les chromosomes homologues s'apparient alors intimement, "
                "deux à deux : c'est la synapsis. Chaque couple forme un "
                "bivalent — quarante-six chromosomes donnent ainsi "
                "vingt-trois bivalents chez l'être humain. Comme chaque "
                "chromosome comporte deux chromatides, un bivalent contient "
                "quatre chromatides : on parle aussi de tétrade."
            )
        ) as tracker:
            self.play(chr_p.animate.next_to(chr_m, LEFT, buff=0.05))
            self.play(FadeIn(bivalent_label))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bivalent_label))

        # Crossing-over : chiasma
        chiasma_dot = Dot(radius=0.06, color=YELLOW)
        chiasma_dot.move_to(VGroup(chr_p, chr_m).get_center() + DOWN * 0.15)
        ligne1 = Line(chr_p[1].get_bottom(), chr_m[0].get_bottom() + RIGHT * 0.02, color=YELLOW, stroke_width=2)
        ligne2 = Line(chr_m[0].get_top(), chr_p[1].get_top() + LEFT * 0.02, color=YELLOW, stroke_width=2)
        chiasma_label = Text("chiasma : point de crossing-over\n(échange entre chromatides non sœurs)", font_size=16, color=YELLOW)
        chiasma_label.next_to(separes, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Des crossing-over, ou enjambements, ont lieu : deux "
                "chromatides non sœurs d'un même bivalent se croisent au "
                "niveau de points appelés chiasmas, et échangent des "
                "segments d'ADN. Le chiasma est donc le point de croisement "
                "visible entre deux chromatides non sœurs de chromosomes "
                "homologues ; le crossing-over est l'échange réciproque de "
                "segments qui s'y produit."
            )
        ) as tracker:
            self.play(FadeIn(chiasma_dot), FadeIn(chiasma_label))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(separes), FadeOut(chiasma_dot), FadeOut(chiasma_label))

        # Disparition enveloppe nucléaire (texte)
        fin_prophase = Text(
            _wrap(
                "L'enveloppe nucléaire et le nucléole disparaissent ; le "
                "fuseau de division se forme.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        fin_prophase.next_to(sous_titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Pour finir, l'enveloppe nucléaire et le nucléole "
                "disparaissent, et le fuseau de division se forme : la "
                "cellule est prête pour la métaphase I."
            )
        ) as tracker:
            self.play(FadeIn(fin_prophase))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(fin_prophase))

        # --- Exemple traité : définition chiasma / crossing-over ---------------
        definition = definition_box(
            Text(
                _wrap(
                    "Chiasma : point de croisement visible entre deux "
                    "chromatides non sœurs de chromosomes homologues. "
                    "Crossing-over : échange réciproque de segments de "
                    "chromatides non sœurs, qui se produit au niveau des "
                    "chiasmas pendant la prophase I.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ces deux définitions précisément. Le chiasma est "
                "le point de croisement visible entre deux chromatides non "
                "sœurs de chromosomes homologues. Le crossing-over est "
                "l'échange réciproque de segments de chromatides non "
                "sœurs, qui se produit au niveau des chiasmas pendant la "
                "prophase I."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Piège à éviter : une seule réplication pour deux divisions --------
        piege = warning_box(
            VGroup(
                Text(
                    _wrap(
                        "Il n'y a qu'UNE SEULE réplication de l'ADN pour "
                        "DEUX divisions. Il n'y a pas de réplication entre "
                        "la méiose I et la méiose II.",
                        width=52,
                    ),
                    font_size=22,
                ),
                MathTex(r"Q \;\longrightarrow\; 2Q \;\;(\text{interphase, 1 seule fois})", font_size=24, color=WHITE),
            ).arrange(DOWN, buff=0.35),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter absolument : il n'y a qu'une seule "
                "réplication de l'ADN pour deux divisions. Il n'y a aucune "
                "réplication entre la méiose I et la méiose II — la "
                "quantité d'ADN ne fait que diminuer après l'interphase, "
                "elle ne double plus jamais."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
