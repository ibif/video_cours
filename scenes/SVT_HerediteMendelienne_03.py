"""
scenes/SVT_HerediteMendelienne_03.py — Chapitre 6 (1ereC, SVT), scène 03.

§ I.3-I.4 Génotype et phénotype (notation entre crochets), méthode
"le phénotype se voit, le génotype se déduit", homozygote et hétérozygote
(gamètes produits), rappel de la méiose. Source : 1ereC/SVT.pdf, page 58.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
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
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class GenotypePhenotype(NotionScene):
    def construct(self):
        titre = scene_title("6.3 — Génotype, phénotype, homozygote, hétérozygote")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : deux façons de décrire un individu -------------------------
        intro = Text(
            _wrap(
                "Un même individu peut être décrit de deux façons : par ce "
                "qu'on observe (son aspect), et par les allèles qu'il "
                "porte réellement dans ses chromosomes.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un même individu peut être décrit de deux façons "
                "complémentaires : par ce que l'on observe, son aspect, et "
                "par les allèles qu'il porte réellement dans ses "
                "chromosomes. La génétique distingue soigneusement ces deux "
                "notions."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : génotype, phénotype, méthode -----------
        def_geno = definition_box(
            VGroup(
                Text("Le génotype est l'ensemble des allèles que possède", font_size=23),
                Text("un individu pour un (ou plusieurs) gène(s).", font_size=23),
                MathTex(r"\text{Notation : } LL,\; Ll,\; ll", font_size=28, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.0,
        )
        def_geno.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le génotype est l'ensemble des allèles que possède un "
                "individu pour un ou plusieurs gènes considérés. Il "
                "s'écrit avec les lettres symbolisant les allèles : par "
                "exemple L L, L l, ou l l."
            )
        ) as tracker:
            self.play(FadeIn(def_geno))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_geno))

        def_pheno = definition_box(
            VGroup(
                Text("Le phénotype est l'ensemble des caractères", font_size=23),
                Text("observables d'un individu, résultant de l'expression", font_size=23),
                Text("de son génotype.", font_size=23),
                MathTex(r"\text{Notation : } [L],\; [l]", font_size=28, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.3,
        )
        def_pheno.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le phénotype est l'ensemble des caractères observables "
                "d'un individu, résultant de l'expression de son "
                "génotype, éventuellement modifiée par le milieu. On le "
                "note entre crochets : crochet L pour graine lisse, "
                "crochet l pour graine ridée."
            )
        ) as tracker:
            self.play(FadeIn(def_pheno))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_pheno))

        methode = method_box(
            Text(
                _wrap(
                    "Le phénotype se voit, le génotype ne se voit pas : il "
                    "se déduit des croisements. Deux individus peuvent "
                    "avoir le même phénotype sans avoir le même génotype : "
                    "une graine lisse peut être LL ou Ll.",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.3,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé, essentiel pour tout ce chapitre : le "
                "phénotype se voit, le génotype ne se voit pas, il se "
                "déduit des croisements. Deux individus peuvent avoir "
                "exactement le même phénotype sans avoir le même "
                "génotype : une graine lisse peut aussi bien être de "
                "génotype L L que de génotype L l."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : homozygote et hétérozygote -------------------------
        entete_ex = Text("Homozygote et hétérozygote", font_size=25, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        homo = VGroup(
            MathTex(r"LL \;\text{ou}\; ll", font_size=30, color=YELLOW),
            Text(
                _wrap(
                    "Homozygote (« race pure ») : deux allèles identiques. "
                    "Produit une seule sorte de gamètes.",
                    width=42,
                ),
                font_size=21,
            ),
        ).arrange(DOWN, buff=0.25)

        hetero = VGroup(
            MathTex(r"Ll", font_size=30, color=YELLOW),
            Text(
                _wrap(
                    "Hétérozygote (« hybride ») : deux allèles différents. "
                    "Produit deux sortes de gamètes en quantités égales : "
                    "1/2 L et 1/2 l.",
                    width=42,
                ),
                font_size=21,
            ),
        ).arrange(DOWN, buff=0.25)

        deux_cas = VGroup(homo, hetero).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        deux_cas.next_to(entete_ex, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un individu est homozygote pour un gène lorsqu'il "
                "possède deux allèles identiques, L L ou l l : on dit "
                "aussi qu'il est de race pure pour ce caractère, et il ne "
                "produit qu'une seule sorte de gamètes. Un individu est "
                "hétérozygote lorsqu'il possède deux allèles différents, "
                "L l : on dit aussi que c'est un hybride, et il produit "
                "deux sortes de gamètes en quantités égales, un demi de "
                "gamètes L et un demi de gamètes l."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(homo))
            self.play(FadeIn(hetero))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(deux_cas))

        # --- À retenir : rappel de la méiose --------------------------------------
        rappel = warning_box(
            Text(
                _wrap(
                    "Rappel (chapitre 2, la méiose) : lors de la formation "
                    "des gamètes, les deux chromosomes de chaque paire se "
                    "séparent. Chaque gamète, haploïde, ne reçoit donc "
                    "qu'un seul allèle de chaque gène. C'est la base de "
                    "tous les raisonnements de ce chapitre.",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.3,
        )
        rappel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un rappel essentiel, vu au chapitre sur la méiose : lors "
                "de la formation des gamètes, les deux chromosomes de "
                "chaque paire se séparent. Chaque gamète, haploïde, ne "
                "reçoit donc qu'un seul allèle de chaque gène, jamais "
                "deux. C'est ce fait cytologique qui fonde absolument tous "
                "les raisonnements que nous allons mener dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(rappel))
