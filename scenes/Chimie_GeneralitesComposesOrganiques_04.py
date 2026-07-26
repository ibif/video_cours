"""
scenes/Chimie_GeneralitesComposesOrganiques_04.py — Chapitre 1 (1ereC, Chimie), scène 04.

§ 2.2, 2.3 Mise en évidence de l'azote (chauffage avec soude concentrée,
dégagement de NH3, test au papier pH) et cas de l'oxygène (pas de test
direct, décelé par différence lors de l'analyse quantitative).
Source : 1ereC/Chimie.pdf, page 6.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREEN,
    GRAY,
    FadeIn,
    FadeOut,
    Arrow,
    Rectangle,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class MiseEnEvidenceAzoteEtOxygene(NotionScene):
    def construct(self):
        titre = scene_title("2.2-2.3 — L'azote et le cas de l'oxygène")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : peut-on aussi détecter l'azote ? -------------------------
        intro = Text(
            _wrap(
                "Le carbone et l'hydrogène se mettent en évidence par "
                "combustion. Mais comment repérer l'azote, lorsqu'il est "
                "présent dans un composé organique ?",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le carbone et l'hydrogène se mettent en évidence par "
                "combustion. Mais comment repérer l'azote, lorsqu'il est "
                "présent dans un composé organique ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : chauffage à la soude, dégagement NH3 --
        entete = Text("Expérience : chauffage avec la soude concentrée", font_size=22, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        tube = Rectangle(width=1.8, height=1.1, color=WHITE, stroke_width=3)
        tube_texte = Text("composé\n+ soude conc.\nchauffage", font_size=14, color=WHITE)
        tube_texte.move_to(tube.get_center())
        bloc_tube = VGroup(tube, tube_texte)

        fleche = Arrow(LEFT * 0.4, RIGHT * 0.4, color=WHITE, buff=0)
        gaz = MathTex(r"NH_3", font_size=34, color=GREEN)
        gaz_label = Text("gaz, odeur piquante", font_size=15, color=GREEN)
        bloc_gaz = VGroup(gaz, gaz_label).arrange(DOWN, buff=0.15)

        fleche2 = Arrow(LEFT * 0.4, RIGHT * 0.4, color=WHITE, buff=0)
        papier = Rectangle(width=1.0, height=1.4, color=WHITE, stroke_width=3, fill_color=BLUE, fill_opacity=0.5)
        papier_label = Text("papier pH\nrouge → bleu", font_size=15, color=BLUE)
        bloc_papier = VGroup(papier, papier_label).arrange(DOWN, buff=0.15)

        schema = VGroup(bloc_tube, fleche, bloc_gaz, fleche2, bloc_papier).arrange(RIGHT, buff=0.4, aligned_edge=UP)
        schema.next_to(entete, DOWN, buff=0.5)
        _fit(schema, entete.get_bottom()[1] - 0.4)

        groupe_schema = VGroup(entete, schema)

        with self.voiceover(
            text=(
                "On chauffe le composé organique avec de la soude "
                "concentrée, ou de la chaux sodée. Si le composé contient "
                "de l'azote, il se dégage de l'ammoniac, gaz d'odeur "
                "piquante, qui bleuit le papier pH humide, ou le papier de "
                "tournesol rouge."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(bloc_tube))
            self.play(FadeIn(fleche), FadeIn(bloc_gaz))
            self.play(FadeIn(fleche2), FadeIn(bloc_papier))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : rappel de la conclusion de l'expérience ----------
        exemple = example_box(
            Text(
                _wrap(
                    "Un papier pH humide placé au-dessus du tube à essai "
                    "vire du rouge au bleu dès qu'un gaz à odeur piquante "
                    "se dégage : c'est un test caractéristique de "
                    "l'ammoniac NH₃, donc de la présence de l'azote dans "
                    "le composé chauffé.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En pratique, un papier pH humide placé au-dessus du tube "
                "à essai vire du rouge au bleu dès qu'un gaz à odeur "
                "piquante se dégage : c'est le test caractéristique de "
                "l'ammoniac, qui révèle la présence de l'azote dans le "
                "composé chauffé."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir / pièges : le cas particulier de l'oxygène --------------
        piege = warning_box(
            Text(
                _wrap(
                    "Il n'existe pas, au niveau du lycée, de test direct "
                    "simple de l'élément oxygène dans un composé "
                    "organique. Sa présence est décelée par différence "
                    "lors de l'analyse quantitative (voir la suite du "
                    "chapitre).",
                    width=48,
                ),
                font_size=25,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un point important à retenir : contrairement au carbone, "
                "à l'hydrogène et à l'azote, il n'existe pas, au niveau du "
                "lycée, de test direct simple de l'élément oxygène dans un "
                "composé organique. Sa présence sera décelée par "
                "différence, lors de l'analyse élémentaire quantitative, "
                "que nous allons étudier maintenant."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
