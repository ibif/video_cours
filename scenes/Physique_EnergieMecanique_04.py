"""
scenes/Physique_EnergieMecanique_04.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 04.

Forces conservatives / non conservatives et démonstration de la
conservation de l'énergie mécanique : définitions (poids, tension de
ressort = conservatives ; frottements = non conservative, pas d'énergie
potentielle associée), cas particulier de la réaction normale (travail nul,
ne modifie pas Em). Démonstration complète sur un solide glissant sans
frottement sur un plan incliné : Em(A)=Em(B).
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Polygon,
    Square,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, property_box, scene_title, theorem_box, warning_box

POIDS_COLOR = "#1E5FA8"
REACTION_COLOR = "#288073"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _plan_incline():
    """Plan incliné triangulaire, angle d'inclinaison visible, sans frottement."""
    base = Polygon(
        LEFT * 2.2 + DOWN * 1.3,
        RIGHT * 2.2 + DOWN * 1.3,
        RIGHT * 2.2 + UP * 1.1,
        color=WHITE,
        fill_color="#3A3A3A",
        fill_opacity=0.6,
    )
    return base


class ForcesConservativesDemonstration(NotionScene):
    def construct(self):
        titre = scene_title("Forces conservatives et démonstration")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : deux catégories de forces --------------------------------------
        intro = Text(
            _wrap(
                "Pourquoi l'énergie mécanique se conserve-t-elle en chute "
                "libre ? La réponse tient à la nature de la force en jeu : "
                "le poids est une force dite CONSERVATIVE.",
                width=54,
            ),
            font_size=23,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi l'énergie mécanique se conserve-t-elle en chute "
                "libre ? La réponse tient à la nature même de la force en "
                "jeu : le poids appartient à une catégorie particulière de "
                "forces, dites forces conservatives."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définitions : conservative / non conservative ---------------------------
        def_conservative = definition_box(
            VGroup(
                Text("Force CONSERVATIVE", font_size=21, weight="BOLD"),
                Text("Son travail ne dépend pas du chemin suivi ;", font_size=19),
                Text("une énergie potentielle lui est associée.", font_size=19),
                Text("Exemples : poids, tension d'un ressort.", font_size=19),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=6.4,
        )
        def_non_conservative = property_box(
            VGroup(
                Text("Force NON conservative", font_size=21, weight="BOLD"),
                Text("Son travail dépend du chemin suivi ;", font_size=19),
                Text("AUCUNE énergie potentielle associée.", font_size=19),
                Text("Exemple : les frottements.", font_size=19),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=6.4,
        )
        deux_defs = VGroup(def_conservative, def_non_conservative).arrange(RIGHT, buff=0.4)
        deux_defs.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une force est dite conservative si son travail ne dépend "
                "pas du chemin suivi, seulement des positions de départ et "
                "d'arrivée : c'est le cas du poids, ou de la tension d'un "
                "ressort. On peut alors lui associer une énergie "
                "potentielle. À l'inverse, une force est dite non "
                "conservative si son travail dépend du chemin parcouru : "
                "c'est le cas des frottements, auxquels on n'associe aucune "
                "énergie potentielle."
            )
        ) as tracker:
            self.play(FadeIn(def_conservative))
            self.play(FadeIn(def_non_conservative))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(deux_defs))

        # --- Cas particulier : réaction normale ---------------------------------------
        cas_particulier = warning_box(
            Text(
                _wrap(
                    "Cas particulier : la réaction normale d'un support "
                    "(perpendiculaire au déplacement) a un travail NUL. "
                    "Sans être « conservative », elle ne modifie donc "
                    "jamais Em.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.0,
        )
        cas_particulier.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un cas particulier mérite d'être signalé : la réaction "
                "normale d'un support, perpendiculaire au déplacement, "
                "a systématiquement un travail nul. Sans être à proprement "
                "parler une force conservative, elle ne modifie donc "
                "jamais l'énergie mécanique du système."
            )
        ) as tracker:
            self.play(FadeIn(cas_particulier))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_particulier))

        # --- Raisonnement : démonstration complète (plan incliné sans frottement) ----
        plan = _plan_incline().scale(0.75)
        point_a = plan.get_vertices()[2] + LEFT * 0.3 + DOWN * 0.15
        point_b = plan.get_vertices()[0] + RIGHT * 0.3 + UP * 0.15
        solide_a = Square(side_length=0.3, color=YELLOW, fill_color=YELLOW, fill_opacity=0.9).move_to(point_a)
        solide_b = Square(side_length=0.3, color=YELLOW, fill_color=YELLOW, fill_opacity=0.4).move_to(point_b)
        poids_vec = Vector(DOWN * 0.6, color=POIDS_COLOR).next_to(solide_a, DOWN, buff=0.05)
        reaction_vec = Vector(UP * 0.5 + RIGHT * 0.15, color=REACTION_COLOR).next_to(solide_a, UP, buff=0.05)
        label_a = MathTex("A", font_size=22).next_to(solide_a, LEFT, buff=0.15)
        label_b = MathTex("B", font_size=22).next_to(solide_b, UP, buff=0.15)
        schema = VGroup(plan, solide_a, solide_b, poids_vec, reaction_vec, label_a, label_b)
        schema.scale(0.85).move_to(LEFT * 3.2 + DOWN * 0.3)

        setup = property_box(
            VGroup(
                Text("Solide sur plan incliné SANS frottement", font_size=20, weight="BOLD"),
                Text("(glisse de A vers B)", font_size=18),
                Text("Forces : poids P⃗ et réaction normale R⃗", font_size=18),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            box_width=5.2,
        )
        setup.next_to(schema, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Démontrons maintenant la conservation de l'énergie "
                "mécanique dans un cas général. Considérons un solide qui "
                "glisse sans frottement le long d'un plan incliné, de A "
                "vers B. Deux forces s'exercent sur lui : le poids, et la "
                "réaction normale du plan."
            )
        ) as tracker:
            self.play(FadeIn(schema), FadeIn(setup))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(setup))

        demo1 = MathTex(
            r"E_c(B) - E_c(A) = W_{AB}(\vec{P}) + W_{AB}(\vec{R})",
            font_size=27,
        )
        demo2 = MathTex(
            r"W_{AB}(\vec{R}) = 0 \quad \text{(réaction} \perp \text{déplacement)}",
            font_size=27,
        )
        demo3 = MathTex(
            r"W_{AB}(\vec{P}) = E_{pp}(A) - E_{pp}(B)",
            font_size=27,
        )
        demo = VGroup(demo1, demo2, demo3).arrange(DOWN, buff=0.32)
        demo.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le théorème de l'énergie cinétique donne : E c de B moins "
                "E c de A égale le travail du poids plus le travail de la "
                "réaction. Or le travail de la réaction est nul, puisqu'elle "
                "est perpendiculaire au déplacement. Et le travail du "
                "poids, force conservative, s'écrit comme l'opposé de la "
                "variation d'énergie potentielle : E p p de A moins E p p "
                "de B."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        conclusion = theorem_box(
            VGroup(
                MathTex(r"E_c(B) - E_c(A) = E_{pp}(A) - E_{pp}(B)", font_size=27),
                MathTex(r"E_c(A) + E_{pp}(A) = E_c(B) + E_{pp}(B)", font_size=27),
                MathTex(r"\boxed{E_m(A) = E_m(B)}", font_size=30, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En remplaçant, on obtient E c de B moins E c de A égale E "
                "p p de A moins E p p de B. En regroupant les termes de A "
                "d'un côté et ceux de B de l'autre, on retrouve exactement "
                "la même structure qu'en chute libre : l'énergie mécanique "
                "en A est égale à l'énergie mécanique en B. La démonstration "
                "est donc générale, dès lors que seules des forces "
                "conservatives, ou à travail nul, travaillent."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- À retenir -------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Forces conservatives (poids, tension de ressort) : "
                    "énergie potentielle associée. Forces à travail nul "
                    "(réaction normale) : ne modifient jamais Em. "
                    "Frottements : NON conservatifs, pas d'Ep associée.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : les forces conservatives, comme le "
                "poids ou la tension d'un ressort, ont une énergie "
                "potentielle associée. Les forces à travail nul, comme la "
                "réaction normale, ne modifient jamais l'énergie mécanique. "
                "Les frottements, en revanche, sont des forces non "
                "conservatives, sans énergie potentielle associée."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : ne pas oublier la réaction normale dans le "
                    "bilan des forces sous prétexte que son travail est "
                    "nul — elle doit apparaître dans le bilan, seul son "
                    "travail est nul.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=10.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : il ne faut pas oublier la réaction "
                "normale dans le bilan des forces sous prétexte que son "
                "travail est nul. Elle doit toujours apparaître dans "
                "l'inventaire des forces ; c'est seulement son travail qui "
                "est nul, pas son existence."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
