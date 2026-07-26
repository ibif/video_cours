"""
scenes/SVT_FecondationMammiferes_04.py — Chapitre 4 (1ereC, SVT), scène 04.

§ 3.3 Le franchissement des enveloppes de l'ovule en 3 étapes (cumulus
oophorus/couronne radiée, zone pellucide avec reconnaissance spécifique
d'espèce, membrane vitelline avec fusion et pénétration) + schéma (Figure 2).
Source : 1ereC/SVT.pdf, pages 37-38.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _schema_ovule():
    """Ovule et ses trois enveloppes concentriques (Figure 2) : cumulus
    oophorus (cellules folliculaires, cercle en pointillé le plus large),
    zone pellucide (anneau intermédiaire), membrane vitelline / cytoplasme
    (disque plein central avec le noyau femelle n)."""
    cumulus = Circle(radius=1.7, color="#CFA6E3", stroke_width=2, stroke_opacity=0.6)
    cellules_cumulus = VGroup(
        *[Dot(radius=0.05, color="#CFA6E3").move_to(cumulus.point_at_angle(a)) for a in [i * 0.55 for i in range(12)]]
    )
    zone_pellucide = Circle(radius=1.25, color="#74458C", stroke_width=3)
    cytoplasme = Circle(radius=0.85, color="#FDF0E0", fill_color="#FDF0E0", fill_opacity=0.9, stroke_width=2)
    noyau_femelle = Dot(radius=0.12, color="#DE7C1F")
    label_noyau = Text("n", font_size=18, color="#1A1A1A", weight="BOLD")
    label_noyau.move_to(noyau_femelle.get_center())

    schema = VGroup(cumulus, cellules_cumulus, zone_pellucide, cytoplasme, noyau_femelle, label_noyau)
    return schema, cumulus, zone_pellucide, cytoplasme


def _spermatozoide():
    tete = Circle(radius=0.13, color=WHITE, fill_color=WHITE, fill_opacity=0.9, stroke_width=1)
    flagelle = Line(tete.get_left(), tete.get_left() + LEFT * 0.7, color=WHITE, stroke_width=2)
    return VGroup(tete, flagelle)


class FranchissementEnveloppesOvule(NotionScene):
    def construct(self):
        titre = scene_title("4.3.3 — Le franchissement des enveloppes de l'ovule")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : les 3 enveloppes à traverser --------------------------------
        intro = _bullets(
            [
                "1. Le cumulus oophorus et la couronne radiée : cellules "
                "folliculaires entourant l'ovule.",
                "2. La zone pellucide : membrane glycoprotéique.",
                "3. La membrane vitelline : membrane plasmique de "
                "l'ovocyte lui-même.",
            ],
            font_size=23,
            width=52,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour atteindre le noyau de l'ovule, le spermatozoïde doit "
                "traverser successivement trois enveloppes. Un : le "
                "cumulus oophorus et la couronne radiée, des cellules "
                "folliculaires qui entourent l'ovule. Deux : la zone "
                "pellucide, une membrane glycoprotéique. Trois : la "
                "membrane vitelline, la membrane plasmique de l'ovocyte "
                "lui-même."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : traversée pas à pas ----------------------
        schema, cumulus, zone_pellucide, cytoplasme = _schema_ovule()
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.55)

        sperm = _spermatozoide()
        sperm.next_to(schema, LEFT, buff=1.4)

        label_etape = Text("1. Approche du spermatozoïde", font_size=17, color=YELLOW)
        label_etape.next_to(schema, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici l'ovule et ses enveloppes concentriques : en violet "
                "clair, le cumulus oophorus et la couronne radiée ; en "
                "violet plus soutenu, la zone pellucide ; au centre, la "
                "membrane vitelline et le cytoplasme, contenant le noyau "
                "femelle, haploïde. Le spermatozoïde s'approche."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(sperm), FadeIn(label_etape))
            self.wait(tracker.get_remaining_duration())

        label_etape2 = Text("2. Réaction acrosomique : enzymes libérées", font_size=17, color=YELLOW)
        label_etape2.next_to(schema, DOWN, buff=0.4)
        pos_cumulus = cumulus.get_center() + LEFT * 1.2

        with self.voiceover(
            text=(
                "Au contact du cumulus oophorus, la réaction acrosomique "
                "se déclenche : les enzymes libérées, dont l'hyaluronidase, "
                "désagrègent le ciment qui lie les cellules folliculaires "
                "entre elles, ouvrant un passage à travers le cumulus "
                "oophorus et la couronne radiée."
            )
        ) as tracker:
            self.play(sperm.animate.move_to(pos_cumulus), FadeOut(label_etape), FadeIn(label_etape2))
            self.wait(tracker.get_remaining_duration())

        label_etape3 = Text("3. Franchissement de la zone pellucide", font_size=17, color=YELLOW)
        label_etape3.next_to(schema, DOWN, buff=0.4)
        pos_zp = zone_pellucide.get_center() + LEFT * 0.85

        with self.voiceover(
            text=(
                "Le spermatozoïde atteint ensuite la zone pellucide : les "
                "enzymes digèrent un étroit canal dans cette membrane "
                "glycoprotéique. Des récepteurs spécifiques présents sur "
                "la zone pellucide reconnaissent le spermatozoïde de la "
                "MÊME espèce : la fécondation est donc spécifique, un "
                "spermatozoïde d'une autre espèce ne peut pas la "
                "franchir."
            )
        ) as tracker:
            self.play(sperm.animate.move_to(pos_zp), FadeOut(label_etape2), FadeIn(label_etape3))
            self.wait(tracker.get_remaining_duration())

        label_etape4 = Text("4. Pénétration dans le cytoplasme de l'ovule", font_size=17, color=YELLOW)
        label_etape4.next_to(schema, DOWN, buff=0.4)
        pos_cyto = cytoplasme.get_center() + LEFT * 0.4

        with self.voiceover(
            text=(
                "Enfin, la membrane de la tête du spermatozoïde fusionne "
                "avec la membrane vitelline : la tête et le flagelle du "
                "spermatozoïde pénètrent dans le cytoplasme de l'ovule. "
                "Les mitochondries du flagelle, elles, dégénèrent sur "
                "place."
            )
        ) as tracker:
            self.play(sperm.animate.move_to(pos_cyto).scale(0.6), FadeOut(label_etape3), FadeIn(label_etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(sperm), FadeOut(label_etape4))

        # --- Exemple traité : la spécificité d'espèce ------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "La reconnaissance par la zone pellucide est "
                    "spécifique de l'espèce : un spermatozoïde de chien "
                    "déposé sur un ovule humain in vitro ne peut pas "
                    "franchir sa zone pellucide, faute de récepteurs "
                    "compatibles. C'est un obstacle naturel à "
                    "l'hybridation entre espèces différentes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un exemple pour bien comprendre la spécificité de cette "
                "reconnaissance : un spermatozoïde de chien, déposé sur un "
                "ovule humain in vitro, ne peut pas franchir sa zone "
                "pellucide, faute de récepteurs compatibles. C'est un "
                "obstacle naturel à l'hybridation entre espèces "
                "différentes."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : les 3 étapes en un coup d'œil -----------------------------
        recap_titre = Text("À retenir : les 3 étapes du franchissement", font_size=24, color=YELLOW, weight="BOLD")
        recap_titre.next_to(titre, DOWN, buff=0.5)
        recap = _bullets(
            [
                "Cumulus oophorus / couronne radiée : enzymes acrosomiques "
                "désagrègent le ciment intercellulaire.",
                "Zone pellucide : digestion d'un canal + reconnaissance "
                "spécifique de l'espèce par les récepteurs.",
                "Membrane vitelline : fusion des membranes, pénétration de "
                "la tête et du flagelle, mitochondries dégénèrent.",
            ],
            font_size=21,
            width=52,
        )
        recap.next_to(recap_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résumons les trois étapes du franchissement. Cumulus "
                "oophorus et couronne radiée : les enzymes acrosomiques "
                "désagrègent le ciment intercellulaire. Zone pellucide : "
                "digestion d'un canal et reconnaissance spécifique de "
                "l'espèce par les récepteurs. Membrane vitelline : fusion "
                "des membranes, pénétration de la tête et du flagelle, "
                "puis dégénérescence des mitochondries du flagelle."
            )
        ) as tracker:
            self.play(FadeIn(recap_titre))
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap_titre), FadeOut(recap))

        # --- Piège à éviter : les mitochondries du père ne sont pas transmises ----
        piege = warning_box(
            Text(
                _wrap(
                    "On pourrait croire que les mitochondries du "
                    "spermatozoïde sont transmises à l'enfant : c'est "
                    "FAUX. Elles dégénèrent lors de la pénétration. Les "
                    "mitochondries du zygote proviennent TOUTES de "
                    "l'ovule, donc de la mère.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à un piège subtil : on pourrait croire que les "
                "mitochondries du spermatozoïde sont transmises à "
                "l'enfant. C'est faux : elles dégénèrent lors de la "
                "pénétration. Toutes les mitochondries du zygote "
                "proviennent de l'ovule, donc de la mère uniquement."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
