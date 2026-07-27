"""
scenes/Maths_AnglesOrientesTrigonometrie_04.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 04.

§ Congruence modulo 2π, propriétés de la congruence, relation de Chasles
pour les angles orientés (admise) et ses conséquences (antisymétrie, angle
avec un vecteur opposé, vecteurs colinéaires). Exemple résolu : somme des
angles d'un triangle vaut π [2π] (démonstration en deux étapes).
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    BLUE,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    Polygon,
    Dot,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class CongruenceChasles(NotionScene):
    def construct(self):
        titre = scene_title("Congruence modulo 2π — relation de Chasles")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : congruence modulo 2 pi ----------------------------------
        def_congruence = definition_box(
            VGroup(
                Text("Congruence modulo 2π", font_size=25, weight="BOLD"),
                MathTex(r"x \equiv y \; [2\pi] \iff \exists\, k \in \mathbb{Z},\ x - y = k \times 2\pi", font_size=26),
                Text(
                    "On dit que x est congru à y modulo 2π.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=10,
        )
        def_congruence.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On dit qu'un réel x est congru à un réel y modulo deux "
                "pi, et on note x congru à y crochet deux pi fermé "
                "crochet, lorsqu'il existe un entier relatif k tel que x "
                "moins y égale k fois deux pi, c'est-à-dire lorsque x et y "
                "diffèrent d'un nombre entier de tours complets."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_congruence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_congruence))

        # --- Propriétés de la congruence ---------------------------------------
        proprietes_congr = property_box(
            VGroup(
                Text("Propriétés de la congruence", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "• Réflexivité : x ≡ x [2π]. "
                        "• Symétrie : si x ≡ y [2π] alors y ≡ x [2π]. "
                        "• Transitivité : si x ≡ y [2π] et y ≡ z [2π] alors "
                        "x ≡ z [2π]. "
                        "• Compatibilité avec l'addition : si x ≡ y [2π] "
                        "alors x+a ≡ y+a [2π] pour tout réel a.",
                        width=52,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        proprietes_congr.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Cette relation de congruence se comporte comme une "
                "égalité modulo deux pi : elle est réflexive, un réel est "
                "toujours congru à lui-même ; symétrique, si x est congru "
                "à y alors y est congru à x ; transitive, si x est congru "
                "à y et y congru à z alors x est congru à z ; et elle est "
                "compatible avec l'addition d'un même réel de chaque côté."
            )
        ) as tracker:
            self.play(FadeIn(proprietes_congr))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes_congr))

        # --- Relation de Chasles ------------------------------------------------
        chasles = property_box(
            VGroup(
                Text("Relation de Chasles (admise)", font_size=24, weight="BOLD"),
                MathTex(
                    r"(\vec{u}, \vec{v}) + (\vec{v}, \vec{w}) = (\vec{u}, \vec{w}) \; [2\pi]",
                    font_size=28,
                ),
                Text(
                    "Pour tous vecteurs non nuls u⃗, v⃗, w⃗ du plan.",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10,
        )
        chasles.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Propriété admise, fondamentale pour tout ce chapitre : la "
                "relation de Chasles pour les angles orientés. Pour tous "
                "vecteurs non nuls u vecteur, v vecteur, w vecteur, "
                "l'angle u vecteur v vecteur plus l'angle v vecteur "
                "w vecteur est congru, modulo deux pi, à l'angle "
                "u vecteur w vecteur."
            )
        ) as tracker:
            self.play(FadeIn(chasles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(chasles))

        # --- Conséquences --------------------------------------------------------
        consequences = property_box(
            VGroup(
                Text("Conséquences de la relation de Chasles", font_size=23, weight="BOLD"),
                MathTex(r"(\vec{v}, \vec{u}) = -(\vec{u}, \vec{v}) \; [2\pi] \quad \text{(antisymétrie)}", font_size=23),
                MathTex(r"(\vec{u}, -\vec{v}) = (\vec{u}, \vec{v}) + \pi \; [2\pi]", font_size=23),
                MathTex(r"(-\vec{u}, \vec{v}) = (\vec{u}, \vec{v}) + \pi \; [2\pi]", font_size=23),
                MathTex(r"(-\vec{u}, -\vec{v}) = (\vec{u}, \vec{v}) \; [2\pi]", font_size=23),
            ).arrange(DOWN, buff=0.22),
            box_width=9.5,
        )
        consequences.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "De cette relation découlent des conséquences très "
                "utiles. D'abord l'antisymétrie : l'angle v vecteur "
                "u vecteur est l'opposé de l'angle u vecteur v vecteur, "
                "modulo deux pi. Ensuite, changer un vecteur en son "
                "opposé ajoute pi à la mesure de l'angle : que l'on "
                "change u vecteur en son opposé, ou v vecteur en son "
                "opposé, on ajoute pi ; mais si l'on change les deux "
                "vecteurs en leurs opposés à la fois, l'angle ne change "
                "pas, car les deux pi ajoutés s'annulent modulo deux pi."
            )
        ) as tracker:
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequences))

        # --- Vecteurs colinéaires --------------------------------------------
        colineaires = property_box(
            VGroup(
                Text("Vecteurs colinéaires", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "u⃗ et v⃗ sont colinéaires de même sens si, et "
                        "seulement si, (u⃗, v⃗) = 0 [2π].",
                        width=44,
                    ),
                    font_size=21,
                ),
                Text(
                    _wrap(
                        "u⃗ et v⃗ sont colinéaires de sens contraires si, "
                        "et seulement si, (u⃗, v⃗) = π [2π].",
                        width=44,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        colineaires.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Enfin, ces angles orientés permettent de caractériser le "
                "colinéarité : deux vecteurs u vecteur et v vecteur non "
                "nuls sont colinéaires et de même sens si, et seulement "
                "si, leur angle orienté est congru à zéro modulo deux pi ; "
                "ils sont colinéaires de sens contraires si, et seulement "
                "si, leur angle orienté est congru à pi modulo deux pi."
            )
        ) as tracker:
            self.play(FadeIn(colineaires))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(colineaires))

        # --- Exemple résolu 3 : somme des angles d'un triangle -----------------
        A = [-1.6, -0.6, 0]
        B = [1.6, -0.6, 0]
        C = [-0.3, 1.3, 0]
        triangle = Polygon(A, B, C, color=WHITE, stroke_width=2)
        pts = VGroup(Dot(A, color=YELLOW), Dot(B, color=GREEN), Dot(C, color=BLUE))
        labels = VGroup(
            MathTex("A", font_size=24, color=YELLOW).next_to(A, DOWN + LEFT, buff=0.1),
            MathTex("B", font_size=24, color=GREEN).next_to(B, DOWN + RIGHT, buff=0.1),
            MathTex("C", font_size=24, color=BLUE).next_to(C, UP, buff=0.1),
        )
        figure = VGroup(triangle, pts, labels)
        figure.scale(0.9).to_edge(LEFT, buff=0.7).shift(DOWN * 0.3)

        enonce_ex = Text(
            _wrap(
                "Démontrer que, pour un triangle ABC quelconque, la somme "
                "des angles orientés vérifie (AB⃗,AC⃗)+(BC⃗,BA⃗)+(CA⃗,CB⃗) "
                "= π [2π].",
                width=38,
            ),
            font_size=20,
        )
        enonce_ex.to_edge(RIGHT, buff=0.4).shift(UP * 1.6)

        etape1 = MathTex(
            r"(\vec{AB}, \vec{AC}) + (\vec{BC}, \vec{BA}) + (\vec{CA}, \vec{CB})",
            font_size=22,
        )
        etape2 = MathTex(
            r"\underset{\text{Chasles}}{=} (\vec{AB}, \vec{AC}) + (\vec{BC}, \vec{BA})"
            r" + (\vec{CA}, \vec{BC}) + (\vec{BC}, \vec{CB})",
            font_size=19,
        )
        etape3 = MathTex(
            r"= (\vec{CA}, \vec{BA}) + (\vec{BC}, \vec{CB})"
            r" \;[2\pi]",
            font_size=20,
        )
        etapes = VGroup(etape1, etape2, etape3).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        etapes.next_to(enonce_ex, DOWN, buff=0.35)

        exemple = example_box(
            VGroup(
                Text(
                    "Étape 1 : (AB⃗,AB⃗) = 0, donc en insérant (AC⃗,AB⃗)+(AB⃗,AC⃗)=0 [2π]",
                    font_size=17,
                ),
                Text(
                    "on regroupe par Chasles la somme des trois angles du triangle en un seul angle plat.",
                    font_size=17,
                ),
                Text(
                    "Étape 2 : (AB⃗,AC⃗)+(BC⃗,BA⃗)+(CA⃗,CB⃗) = (BA⃗,BC⃗)+(CB⃗,CA⃗)+(AC⃗,AB⃗) = π [2π]",
                    font_size=17,
                ),
                Text(
                    "car (u⃗,v⃗)+(v⃗,-u⃗) = (u⃗,-u⃗) = π [2π] par Chasles appliquée deux fois.",
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.2),
            box_width=8.2,
        )
        exemple.to_edge(RIGHT, buff=0.3).shift(DOWN * 0.6)

        with self.voiceover(
            text=(
                "Exemple résolu. Démontrons que, pour un triangle A B C "
                "quelconque, la somme des angles orientés du triangle vaut "
                "toujours pi, modulo deux pi. Première étape : en "
                "appliquant deux fois la relation de Chasles, on regroupe "
                "l'angle A-B, A-C, l'angle B-C, B-A, et l'angle C-A, C-B "
                "en un unique angle orienté entre deux vecteurs opposés. "
                "Deuxième étape : un angle orienté entre un vecteur et son "
                "opposé vaut toujours pi, modulo deux pi, d'après la "
                "conséquence vue plus haut. On conclut donc que la somme "
                "des trois angles orientés d'un triangle vaut toujours pi, "
                "modulo deux pi — c'est le résultat bien connu de la somme "
                "des angles d'un triangle, retrouvé ici avec les angles "
                "orientés."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.play(FadeIn(enonce_ex))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(enonce_ex), FadeOut(exemple), FadeOut(titre))
