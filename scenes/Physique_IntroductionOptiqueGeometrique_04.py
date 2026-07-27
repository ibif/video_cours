"""
scenes/Physique_IntroductionOptiqueGeometrique_04.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 04.

§ 3. Propagation rectiligne de la lumière (expérience des cartons percés),
rayon lumineux (modèle géométrique, matérialisable par de la fumée ou de
la poussière) et faisceaux lumineux (divergent, convergent, parallèle).
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 3).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    GRAY,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _experience_cartons(alignes: bool) -> VGroup:
    """Trois cartons percés alignés (ou non) devant une lampe, avec un œil
    à l'autre bout qui voit — ou ne voit pas — la lumière."""
    lampe = Dot(LEFT * 4.0, color=YELLOW, radius=0.13)
    label_lampe = Text("lampe", font_size=15, color=WHITE).next_to(lampe, DOWN, buff=0.15)

    decalages = [0.0, 0.0, 0.0] if alignes else [0.0, 0.35, -0.15]
    cartons = VGroup()
    trous = VGroup()
    for i, x in enumerate([-2.0, -0.3, 1.4]):
        carton = Rectangle(width=0.15, height=1.8, color=GRAY, fill_color=GRAY, fill_opacity=0.9)
        carton.move_to(RIGHT * x + UP * decalages[i])
        trou = Dot(carton.get_center(), color=WHITE, radius=0.06)
        cartons.add(carton)
        trous.add(trou)

    oeil_x = 3.0
    oeil = Circle(radius=0.22, color=WHITE).move_to(RIGHT * oeil_x)
    label_oeil = Text("œil", font_size=15, color=WHITE).next_to(oeil, DOWN, buff=0.15)

    elements = VGroup(lampe, label_lampe, cartons, trous, oeil, label_oeil)

    if alignes:
        rayon = Line(lampe.get_center(), oeil.get_center(), color=YELLOW, stroke_width=2)
        elements.add(rayon)
    else:
        rayon = Line(lampe.get_center(), trous[0].get_center(), color=YELLOW, stroke_width=2)
        elements.add(rayon)

    return elements


def _faisceau(kind: str) -> VGroup:
    """Trois mini-schémas : faisceau divergent, convergent, parallèle."""
    if kind == "divergent":
        source = Dot(ORIGIN, color=YELLOW, radius=0.08)
        rayons = VGroup(
            *[
                Line(ORIGIN, 1.4 * d, color=YELLOW, stroke_width=2)
                for d in [RIGHT + UP * 0.5, RIGHT + UP * 0.15, RIGHT, RIGHT + DOWN * 0.15, RIGHT + DOWN * 0.5]
            ]
        )
        label = Text("divergent", font_size=16, color=WHITE)
        groupe = VGroup(source, rayons)
    elif kind == "convergent":
        cible = Dot(RIGHT * 1.4, color=YELLOW, radius=0.08)
        rayons = VGroup(
            *[
                Line(LEFT * 0.0 + d, cible.get_center(), color=YELLOW, stroke_width=2)
                for d in [UP * 0.5, UP * 0.15, ORIGIN, DOWN * 0.15, DOWN * 0.5]
            ]
        )
        label = Text("convergent", font_size=16, color=WHITE)
        groupe = VGroup(rayons, cible)
    else:
        rayons = VGroup(
            *[
                Line(LEFT * 0.0 + UP * y, RIGHT * 1.4 + UP * y, color=YELLOW, stroke_width=2)
                for y in [0.5, 0.15, -0.15, -0.5]
            ]
        )
        label = Text("parallèle", font_size=16, color=WHITE)
        groupe = VGroup(rayons)

    label.next_to(groupe, DOWN, buff=0.3)
    return VGroup(groupe, label)


class PropagationRectiligneRayonsFaisceaux(NotionScene):
    def construct(self):
        titre = scene_title("Propagation rectiligne : rayons et faisceaux")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Comment vérifier que la lumière se propage bien en ligne "
                "droite ? Une expérience simple avec trois cartons percés "
                "suffit.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comment vérifier que la lumière se propage bien en ligne "
                "droite ? Une expérience simple, avec trois cartons "
                "percés d'un trou, suffit à le montrer."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : expérience + propriété -----------------------------
        exp_alignes = _experience_cartons(alignes=True)
        exp_alignes.scale(0.85)
        exp_alignes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Lorsque les trois trous des cartons sont parfaitement "
                "alignés, l'œil placé de l'autre côté voit la lumière de "
                "la lampe."
            )
        ) as tracker:
            self.play(FadeIn(exp_alignes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exp_alignes))

        exp_non_alignes = _experience_cartons(alignes=False)
        exp_non_alignes.scale(0.85)
        exp_non_alignes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mais dès qu'un seul trou est décalé, la lumière est "
                "arrêtée par le carton et l'œil ne voit plus rien. Cela "
                "prouve que la lumière s'est propagée en ligne droite "
                "entre la lampe et l'œil."
            )
        ) as tracker:
            self.play(FadeIn(exp_non_alignes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exp_non_alignes))

        propriete = property_box(
            Text(
                "Dans un milieu TRANSPARENT et HOMOGÈNE, la lumière se\n"
                "propage en ligne droite.",
                font_size=20,
            ),
            box_width=10.6,
        )
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On retient la propriété fondamentale : dans un milieu "
                "transparent et homogène, la lumière se propage en ligne "
                "droite."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Définitions rayon / faisceau --------------------------------------
        definition_rayon = definition_box(
            VGroup(
                Text("Un RAYON LUMINEUX est un modèle géométrique (une", font_size=19),
                Text("ligne droite) : il n'a pas d'existence matérielle réelle,", font_size=19),
                Text("mais on peut le matérialiser avec de la fumée ou de", font_size=19),
                Text("la poussière en suspension dans l'air.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        definition_rayon.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un rayon lumineux est un modèle géométrique, une simple "
                "ligne droite : il n'a pas d'existence matérielle réelle. "
                "On peut cependant le matérialiser avec de la fumée ou de "
                "la poussière en suspension dans l'air, qui diffusent la "
                "lumière le long de son trajet."
            )
        ) as tracker:
            self.play(FadeIn(definition_rayon))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_rayon))

        definition_faisceau = definition_box(
            Text(
                "Un FAISCEAU LUMINEUX est un ensemble de rayons lumineux.\n"
                "Il peut être divergent, convergent ou parallèle.",
                font_size=20,
            ),
            box_width=10.8,
        )
        definition_faisceau.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un faisceau lumineux est un ensemble de rayons lumineux. "
                "On en distingue trois types : divergent, convergent, ou "
                "parallèle."
            )
        ) as tracker:
            self.play(FadeIn(definition_faisceau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_faisceau))

        # --- Exemple traité : les trois types de faisceaux ----------------------
        div = _faisceau("divergent")
        conv = _faisceau("convergent")
        par = _faisceau("parallèle")
        groupe = VGroup(div, conv, par).arrange(RIGHT, buff=1.0)
        groupe.next_to(titre, DOWN, buff=0.7)

        exemple = example_box(
            Text(
                "Ampoule nue = divergent · loupe qui concentre la lumière\n"
                "= convergent · rayons du Soleil ou phare lointain = parallèle.",
                font_size=17,
            ),
            box_width=10.6,
        )
        exemple.next_to(groupe, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une ampoule nue émet un faisceau divergent : les rayons "
                "s'écartent depuis la source. Une loupe qui concentre la "
                "lumière du Soleil en un point produit un faisceau "
                "convergent. Et les rayons du Soleil, ou la lumière d'un "
                "phare très lointain, forment un faisceau que l'on "
                "considère parallèle."
            )
        ) as tracker:
            self.play(FadeIn(groupe))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(exemple))

        # --- À retenir ----------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Milieu transparent ET homogène → propagation rectiligne.", font_size=19),
                Text("Rayon lumineux = modèle géométrique (ligne droite).", font_size=19),
                Text("Faisceau : divergent, convergent ou parallèle.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Dans un milieu transparent et "
                "homogène, la lumière se propage en ligne droite. Le "
                "rayon lumineux est un modèle géométrique. Et un faisceau "
                "peut être divergent, convergent ou parallèle."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter -----------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne jamais dire que la lumière se propage \"toujours\"", font_size=19),
                Text("   en ligne droite : c'est vrai UNIQUEMENT dans un", font_size=19),
                Text("   milieu transparent ET homogène.", font_size=19),
                Text("• Un changement de milieu (air → eau, par exemple)", font_size=19),
                Text("   dévie le rayon : c'est la réfraction (chapitre", font_size=19),
                Text("   suivant), ou un mirage dans un milieu non homogène.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Attention à ne jamais dire que la lumière se propage "
                "toujours en ligne droite : c'est vrai uniquement dans un "
                "milieu transparent et homogène. Un changement de milieu, "
                "comme passer de l'air à l'eau, dévie le rayon : c'est la "
                "réfraction, que nous étudierons au chapitre suivant, ou "
                "encore un mirage lorsque le milieu n'est pas homogène."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
