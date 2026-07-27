"""
scenes/Physique_EnergieCinetique_03.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 03.

§ Moments d'inertie usuels : établissement simple du cerceau (J_Δ=MR²),
tableau des moments d'inertie usuels (point matériel/anneau, cylindre
plein/disque, sphère, tige axe central, tige axe extrémité). Remarques :
dépendance à la position de l'axe (facteur 4 pour la tige), cerceau > disque
à masse/rayon égaux.
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, § 3).
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
from shapes.boxes import essentiel_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MomentsInertieUsuels(NotionScene):
    def construct(self):
        titre = scene_title("Moments d'inertie usuels")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : cas du cerceau, toute la masse à distance R -----------------
        centre = LEFT * 3.0 + DOWN * 0.2
        cerceau = Circle(radius=1.3, color=YELLOW, stroke_width=4).move_to(centre)
        axe = Dot(centre, color=WHITE, radius=0.06)
        rayon_ligne = Line(centre, centre + RIGHT * 1.3, color=WHITE, stroke_width=2)
        r_label = MathTex("R", font_size=24).next_to(rayon_ligne.get_center(), UP, buff=0.1)
        schema = VGroup(cerceau, axe, rayon_ligne, r_label)
        schema.move_to(LEFT * 3.2)

        mise_en_situation = Text(
            _wrap(
                "Un cerceau de masse M et de rayon R tourne autour de son "
                "axe central. Toute sa masse est concentrée à la même "
                "distance R de l'axe.",
                width=42,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(schema, RIGHT, buff=0.7)

        with self.voiceover(
            text=(
                "Établissons le premier moment d'inertie usuel : celui "
                "d'un cerceau de masse M et de rayon R, tournant autour de "
                "son axe central. Sa particularité : toute sa masse est "
                "concentrée exactement à la même distance R de l'axe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(mise_en_situation))

        # --- Raisonnement : J_Delta = M R^2 ---------------------------------------
        raisonnement = VGroup(
            MathTex(r"J_\Delta = \sum_i m_i r_i^2 = \sum_i m_i R^2 = R^2 \sum_i m_i", font_size=27),
            MathTex(r"\Longrightarrow\ J_\Delta = M R^2", font_size=32, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        raisonnement.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Comme chaque élément de masse m indice i est à la même "
                "distance R de l'axe, on peut sortir R carré de la somme : "
                "J delta égale R carré fois la somme des m indice i, "
                "c'est-à-dire R carré fois la masse totale M. On obtient "
                "ainsi J delta égale M R carré pour le cerceau."
            )
        ) as tracker:
            self.play(Write(raisonnement[0]))
            self.play(Write(raisonnement[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(raisonnement))

        # --- Tableau des moments d'inertie usuels ----------------------------------
        lignes = [
            ("Point matériel / anneau (rayon R)", r"J_\Delta = M R^2"),
            ("Cylindre plein / disque (rayon R)", r"J_\Delta = \dfrac{1}{2} M R^2"),
            ("Sphère pleine (rayon R)", r"J_\Delta = \dfrac{2}{5} M R^2"),
            ("Tige, axe central perpendiculaire", r"J_\Delta = \dfrac{1}{12} M \ell^2"),
            ("Tige, axe à l'extrémité", r"J_\Delta = \dfrac{1}{3} M \ell^2"),
        ]
        table = VGroup(*[
            VGroup(
                Text(nom, font_size=19),
                MathTex(formule, font_size=25),
            ).arrange(RIGHT, buff=0.5)
            for nom, formule in lignes
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        tableau_box = property_box(table, box_width=12.6)
        tableau_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le tableau des moments d'inertie usuels, à connaître "
                "par cœur. Un point matériel ou un anneau de rayon R : J "
                "delta égale M R carré. Un cylindre plein ou un disque de "
                "rayon R : un demi M R carré. Une sphère pleine de rayon "
                "R : deux cinquièmes M R carré. Une tige de longueur ℓ, "
                "pour un axe central perpendiculaire : un douzième M ℓ "
                "carré. Et la même tige, mais pour un axe passant par son "
                "extrémité : un tiers M ℓ carré."
            )
        ) as tracker:
            self.play(FadeIn(tableau_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_box))

        # --- Remarques : dépendance à l'axe et comparaison cerceau/disque ---------
        remarques = warning_box(
            VGroup(
                Text("• Le moment d'inertie dépend de la POSITION de l'axe :", font_size=20),
                Text("   pour une même tige, il y a un facteur 4 entre l'axe", font_size=20),
                Text("   central (1/12 Mℓ²) et l'axe à l'extrémité (1/3 Mℓ²).", font_size=20),
                Text("• À masse M et rayon R égaux, un cerceau (MR²) a un", font_size=20),
                Text("   moment d'inertie plus grand qu'un disque (½MR²) :", font_size=20),
                Text("   sa masse est plus éloignée de l'axe.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.4,
        )
        remarques.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux remarques essentielles. D'abord, le moment d'inertie "
                "dépend de la position de l'axe, pas seulement de la forme "
                "du solide : pour une même tige, il y a un facteur quatre "
                "entre l'axe central, un douzième M ℓ carré, et l'axe à "
                "l'extrémité, un tiers M ℓ carré. Ensuite, à masse M et "
                "rayon R égaux, un cerceau a un moment d'inertie plus "
                "grand qu'un disque, car sa masse est concentrée plus loin "
                "de l'axe de rotation."
            )
        ) as tracker:
            self.play(FadeIn(remarques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarques))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "Anneau/point : MR². Disque/cylindre : ½MR². "
                        "Sphère : (2/5)MR². Tige (centre) : (1/12)Mℓ². "
                        "Tige (extrémité) : (1/3)Mℓ². Le moment d'inertie "
                        "dépend du solide ET de la position de l'axe.",
                        width=56,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : anneau ou point, M R carré ; "
                "disque ou cylindre, un demi M R carré ; sphère, deux "
                "cinquièmes M R carré ; tige par son centre, un douzième M "
                "ℓ carré ; tige par son extrémité, un tiers M ℓ carré. "
                "Dans tous les cas, le moment d'inertie dépend à la fois "
                "du solide et de la position exacte de l'axe."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
