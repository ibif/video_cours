"""
scenes/Physique_EnergiePotentielleElectrostatique_02.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 02.

Travail de la force électrostatique dans un champ uniforme :
W_A→B(F⃗)=F⃗·AB⃗=qE⃗·AB⃗, démonstration complète de l'indépendance du chemin
suivi (chemin direct vs chemin brisé via la relation de Chasles,
généralisation à tout chemin polygonal/courbe), définition d'une force
conservative, la force électrostatique est conservative (comme le poids).
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class TravailForceElectrostatiqueChampUniforme(NotionScene):
    def construct(self):
        titre = scene_title("Travail de la force électrostatique")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : le théorème --------------------------------------------------
        theoreme = theorem_box(
            MathTex(
                r"W_{A \to B}(\vec{F}) = \vec{F} \cdot \vec{AB} = q\,\vec{E} \cdot \vec{AB}",
                font_size=30,
            ),
            box_width=9.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Une charge q placée dans un champ électrostatique uniforme "
                "E subit une force électrique F, égale à q E, constante en "
                "tout point. Le travail de cette force lorsque la charge se "
                "déplace du point A au point B vaut F fois AB, c'est-à-dire "
                "q E fois AB, en produit scalaire."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(theoreme.animate.scale(0.7).to_corner(UP + RIGHT).shift(DOWN * 0.2))

        # --- Raisonnement : indépendance du chemin, démonstration ------------------
        point_a = Dot(LEFT * 4.2 + DOWN * 1.6, color=WHITE, radius=0.08)
        point_b = Dot(RIGHT * 1.0 + UP * 1.4, color=WHITE, radius=0.08)
        point_c = Dot(LEFT * 0.5 + DOWN * 1.8, color=WHITE, radius=0.08)
        label_a = MathTex("A", font_size=28).next_to(point_a, DOWN, buff=0.15)
        label_b = MathTex("B", font_size=28).next_to(point_b, UP, buff=0.15)
        label_c = MathTex("C", font_size=28).next_to(point_c, DOWN, buff=0.15)

        chemin_direct = Line(point_a.get_center(), point_b.get_center(), color=YELLOW)
        chemin_ac = Line(point_a.get_center(), point_c.get_center(), color=WHITE)
        chemin_cb = Line(point_c.get_center(), point_b.get_center(), color=WHITE)

        force_fleche = Arrow(
            point_a.get_center() + UP * 0.3,
            point_a.get_center() + UP * 0.3 + RIGHT * 0.9,
            color=YELLOW,
            buff=0,
            stroke_width=3,
        )
        label_f = MathTex(r"\vec{F}", font_size=26, color=YELLOW).next_to(force_fleche, UP, buff=0.1)

        schema = VGroup(
            point_a, point_b, label_a, label_b, chemin_direct, force_fleche, label_f
        )
        schema.next_to(titre, DOWN, buff=1.0).to_edge(LEFT, buff=0.8)

        with self.voiceover(
            text=(
                "Démontrons que ce travail ne dépend pas du chemin suivi "
                "entre A et B, mais seulement de la position de ces deux "
                "points. Traçons d'abord le chemin direct de A vers B."
            )
        ) as tracker:
            self.play(FadeIn(point_a), Write(label_a))
            self.play(FadeIn(point_b), Write(label_b))
            self.play(Create(chemin_direct))
            self.play(FadeIn(force_fleche), Write(label_f))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Imaginons maintenant un chemin brisé, passant par un point "
                "intermédiaire C quelconque : d'abord de A vers C, puis de "
                "C vers B."
            )
        ) as tracker:
            self.play(FadeIn(point_c), Write(label_c))
            self.play(Create(chemin_ac), Create(chemin_cb))
            self.wait(tracker.get_remaining_duration())

        demo1 = MathTex(
            r"W_{A \to C}(\vec{F}) + W_{C \to B}(\vec{F}) = \vec{F} \cdot \vec{AC} + \vec{F} \cdot \vec{CB}",
            font_size=24,
        )
        demo2 = MathTex(
            r"= \vec{F} \cdot (\vec{AC} + \vec{CB}) = \vec{F} \cdot \vec{AB}",
            font_size=24,
        )
        demo3 = MathTex(
            r"\text{(relation de Chasles : } \vec{AC} + \vec{CB} = \vec{AB}\text{)}",
            font_size=22,
            color=YELLOW,
        )
        demo = VGroup(demo1, demo2, demo3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        demo.next_to(schema, RIGHT, buff=0.6).align_to(schema, UP)

        with self.voiceover(
            text=(
                "Le travail total sur ce chemin brisé vaut la somme des "
                "deux travaux partiels : F fois AC, plus F fois CB. Comme F "
                "est une force constante, on peut factoriser : F fois la "
                "somme des vecteurs AC et CB. Or, la relation de Chasles "
                "nous dit que AC plus CB est exactement égal à AB. On "
                "retrouve donc F fois AB, c'est-à-dire exactement le "
                "travail du chemin direct !"
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.wait(tracker.get_remaining_duration())

        generalisation = Text(
            _wrap(
                "Ce raisonnement se répète pour tout chemin brisé "
                "(polygonal), quel que soit le nombre de points "
                "intermédiaires, et se généralise à tout chemin courbe, "
                "assimilable à une infinité de petits segments : le "
                "travail ne dépend que de A et B, jamais du trajet suivi.",
                width=52,
            ),
            font_size=21,
        )
        generalisation.next_to(demo, DOWN, buff=0.5, aligned_edge=LEFT)

        with self.voiceover(
            text=(
                "Ce raisonnement se répète à l'identique pour un chemin "
                "brisé comportant autant de points intermédiaires que l'on "
                "veut, et se généralise à tout chemin courbe, que l'on peut "
                "toujours découper en une infinité de petits segments "
                "rectilignes. Conclusion : le travail de la force "
                "électrostatique ne dépend que des points de départ A et "
                "d'arrivée B, jamais du trajet réellement suivi entre les "
                "deux."
            )
        ) as tracker:
            self.play(Write(generalisation))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(schema),
            FadeOut(label_c),
            FadeOut(point_c),
            FadeOut(chemin_ac),
            FadeOut(chemin_cb),
            FadeOut(demo),
            FadeOut(generalisation),
        )

        # --- Définition : force conservative ----------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une force est dite conservative lorsque le travail "
                    "qu'elle exerce entre deux points A et B ne dépend pas "
                    "du chemin suivi pour aller de A à B, mais seulement "
                    "de la position de ces deux points.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.2,
        )
        definition.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "On dit qu'une force est conservative lorsque son travail "
                "entre deux points A et B ne dépend pas du chemin suivi, "
                "mais uniquement de la position de ces deux points. C'est "
                "exactement ce que nous venons de démontrer pour la force "
                "électrostatique."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        conclusion = Text(
            _wrap(
                "La force électrostatique est donc une force conservative, "
                "tout comme le poids, déjà rencontré au chapitre "
                "précédent.",
                width=52,
            ),
            font_size=25,
        )
        conclusion.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "La force électrostatique est donc, elle aussi, une force "
                "conservative — tout comme le poids, que nous avions déjà "
                "étudié au chapitre précédent sur l'énergie potentielle de "
                "pesanteur. Cette propriété va nous permettre de définir "
                "une énergie potentielle électrostatique, exactement selon "
                "la même démarche."
            )
        ) as tracker:
            self.play(Write(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion), FadeOut(theoreme))

        # --- À retenir ----------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "W_A→B(F⃗)=qE⃗·AB⃗ (champ uniforme). Ce travail ne dépend "
                    "pas du chemin suivi (démontré par la relation de "
                    "Chasles), seulement des points A et B : la force "
                    "électrostatique est conservative, comme le poids.",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : dans un champ uniforme, le travail de la "
                "force électrostatique vaut q E fois AB. Ce travail ne "
                "dépend pas du chemin suivi, comme nous l'avons démontré "
                "grâce à la relation de Chasles, mais uniquement des "
                "points de départ et d'arrivée : la force électrostatique "
                "est donc conservative, exactement comme le poids."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
