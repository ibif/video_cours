"""
scenes/SVT_HerediteMendelienne_05.py — Chapitre 6 (1ereC, SVT), scène 05.

§ III.1-III.2 Le monohybridisme, la démarche de Mendel (pourquoi le
pois), la première expérience (croisement de lignées pures P : [L]x[l],
F1 uniforme) et la première loi de Mendel (uniformité des hybrides de
F1). Source : 1ereC/SVT.pdf, pages 59-60.
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
    Create,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _pois(color, label, font_size=20):
    graine = Circle(radius=0.35, color=color, fill_color=color, fill_opacity=0.85)
    texte = Text(label, font_size=font_size, color=WHITE)
    texte.next_to(graine, DOWN, buff=0.15)
    return VGroup(graine, texte)


class Monohybridisme(NotionScene):
    def construct(self):
        titre = scene_title("6.5 — Le monohybridisme : Mendel et le pois")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : la définition du monohybridisme ----------------------------
        def_mono = definition_box(
            Text(
                _wrap(
                    "Le monohybridisme est l'étude de la transmission d'un "
                    "seul caractère héréditaire au cours de croisements "
                    "entre des individus qui diffèrent par ce caractère.",
                    width=50,
                ),
                font_size=24,
            ),
            box_width=11.3,
        )
        def_mono.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le monohybridisme est l'étude de la transmission d'un "
                "seul caractère héréditaire au cours de croisements entre "
                "des individus qui diffèrent par ce caractère. C'est "
                "exactement ce que Mendel a mis en place avec ses pois de "
                "senteur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_mono))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_mono))

        # --- Animation du raisonnement : pourquoi le pois -------------------------
        entete_pois = Text("Pourquoi Mendel a-t-il choisi le pois ?", font_size=24, color=YELLOW, weight="BOLD")
        entete_pois.next_to(titre, DOWN, buff=0.5)

        raisons = _bullets(
            [
                "Plante à reproduction rapide et à nombreux descendants.",
                "Existe en variétés de race pure bien distinctes "
                "(graines lisses/ridées, fleurs violettes/blanches, "
                "gousses vertes/jaunes...).",
                "Fleur fermée, se féconde elle-même, mais on peut "
                "réaliser des croisements contrôlés en déposant du "
                "pollen d'une variété sur le pistil d'une autre variété "
                "émasculée.",
            ],
            font_size=22,
            width=52,
        )
        raisons.next_to(entete_pois, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Mendel choisit le pois de senteur pour trois raisons "
                "précises. C'est d'abord une plante à reproduction rapide "
                "et à nombreux descendants, ce qui permet de compter de "
                "grands effectifs. Elle existe ensuite en variétés de "
                "race pure bien distinctes : graines lisses ou ridées, "
                "fleurs violettes ou blanches, gousses vertes ou jaunes. "
                "Enfin, sa fleur, fermée, se féconde habituellement "
                "elle-même, mais Mendel pouvait réaliser des croisements "
                "contrôlés en déposant lui-même du pollen d'une variété "
                "sur le pistil d'une autre variété, préalablement "
                "émasculée."
            )
        ) as tracker:
            self.play(FadeIn(entete_pois))
            self.play(FadeIn(raisons))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pois), FadeOut(raisons))

        # --- Exemple traité : la première expérience ------------------------------
        entete_exp = Text("1ère expérience : croisement de lignées pures", font_size=23, color=YELLOW, weight="BOLD")
        entete_exp.next_to(titre, DOWN, buff=0.5)

        p_lisse = _pois(YELLOW, "[L] lisse\n(LL)")
        p_ride = _pois("#7a5230", "[l] ridée\n(ll)")
        croix = MathTex(r"\times", font_size=36, color=WHITE)
        p_parents = VGroup(p_lisse, croix, p_ride).arrange(RIGHT, buff=0.6)
        p_label = Text("P (parents, race pure) :", font_size=20, color=WHITE)
        ligne_p = VGroup(p_label, p_parents).arrange(RIGHT, buff=0.4)
        ligne_p.next_to(entete_exp, DOWN, buff=0.5)

        genotype_p = MathTex(r"P : \; LL \;\times\; ll", font_size=30, color=YELLOW)
        genotype_p.next_to(ligne_p, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Mendel croise des pois de race pure à graines lisses "
                "avec des pois de race pure à graines ridées. En "
                "notation, cela s'écrit : parents, crochet L croisé avec "
                "crochet l, soit en génotypes, L L croisé avec l l."
            )
        ) as tracker:
            self.play(FadeIn(entete_exp))
            self.play(Create(p_lisse), FadeIn(p_label), Write(croix), Create(p_ride))
            self.play(Write(genotype_p))
            self.wait(tracker.get_remaining_duration())

        f1_ligne = VGroup(
            Text("F1 :", font_size=20, color=WHITE),
            _pois(YELLOW, "[L] lisse"),
            _pois(YELLOW, "[L] lisse"),
            _pois(YELLOW, "[L] lisse"),
            Text("...", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.4)
        f1_ligne.next_to(genotype_p, DOWN, buff=0.6)

        f1_genotype = MathTex(r"F_1 : \; 100\%\; Ll,\; \text{tous } [L]", font_size=28, color=YELLOW)
        f1_genotype.next_to(f1_ligne, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Tous les descendants de la première génération, notée F "
                "un, ont des graines lisses : la génération F un est "
                "uniforme. L'allèle lisse, L, est donc dominant ; "
                "l'allèle ridée, l, qui a apparemment disparu en F un, est "
                "récessif."
            )
        ) as tracker:
            self.play(FadeIn(f1_ligne))
            self.play(Write(f1_genotype))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_exp),
            FadeOut(ligne_p),
            FadeOut(genotype_p),
            FadeOut(f1_ligne),
            FadeOut(f1_genotype),
        )

        # --- À retenir : la première loi de Mendel --------------------------------
        loi1 = theorem_box(
            Text(
                _wrap(
                    "Première loi de Mendel (loi d'uniformité des hybrides "
                    "de F1) : le croisement de deux individus de race pure "
                    "différant par un caractère donne une F1 homogène : "
                    "tous les individus sont des hybrides présentant le "
                    "phénotype de l'allèle dominant.",
                    width=50,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        loi1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On énonce ainsi la première loi de Mendel, la loi "
                "d'uniformité des hybrides de F un : le croisement de "
                "deux individus de race pure différant par un caractère "
                "donne une première génération homogène ; tous les "
                "individus sont des hybrides, présentant le phénotype de "
                "l'allèle dominant."
            )
        ) as tracker:
            self.play(FadeIn(loi1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(loi1))
