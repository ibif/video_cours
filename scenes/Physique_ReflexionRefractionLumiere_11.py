"""
scenes/Physique_ReflexionRefractionLumiere_11.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 11.

§ Tableau récapitulatif du chapitre : synthèse des formules (réflexion
i'1=i1, indice n=c/v, réfraction n1 sin i1 = n2 sin i2, angle limite
sin λ = n2/n1, condition de réflexion totale, déplacement latéral d'une
lame à faces parallèles).
Source : 1ereC/Physique.pdf, pages 117-129.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class TableauRecapitulatifChapitre(NotionScene):
    def construct(self):
        titre = scene_title("Tableau récapitulatif du chapitre")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : parcours du chapitre --------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Ce chapitre a couvert la réflexion, le miroir plan, la "
                "réfraction, la réflexion totale et ses applications, "
                "ainsi que la lame à faces parallèles. Rassemblons "
                "toutes les formules essentielles.",
                width=56,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce chapitre a couvert la réflexion, le miroir plan, la "
                "réfraction, la réflexion totale et ses applications, "
                "ainsi que la lame à faces parallèles. Rassemblons "
                "maintenant toutes les formules essentielles dans un "
                "tableau récapitulatif."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Tableau 1 : réflexion et indice --------------------------------------------
        bloc1 = VGroup(
            Text("Réflexion", font_size=20, weight="BOLD"),
            MathTex(r"i_1' = i_1", font_size=26),
        ).arrange(DOWN, buff=0.2)
        bloc2 = VGroup(
            Text("Indice de réfraction", font_size=20, weight="BOLD"),
            MathTex(r"n = \dfrac{c}{v} \ \geq 1", font_size=26),
        ).arrange(DOWN, buff=0.2)
        ligne1 = VGroup(bloc1, bloc2).arrange(RIGHT, buff=1.2)
        ligne1_box = property_box(ligne1, box_width=11.6)
        ligne1_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour la réflexion, l'angle de réflexion i'1 est égal à "
                "l'angle d'incidence i1. L'indice de réfraction absolu n "
                "vaut c sur v, et il est toujours supérieur ou égal à un."
            )
        ) as tracker:
            self.play(FadeIn(ligne1_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ligne1_box))

        # --- Tableau 2 : réfraction et angle limite -------------------------------------
        bloc3 = VGroup(
            Text("Réfraction (Snell-Descartes)", font_size=20, weight="BOLD"),
            MathTex(r"n_1 \sin i_1 = n_2 \sin i_2", font_size=26),
        ).arrange(DOWN, buff=0.2)
        bloc4 = VGroup(
            Text("Angle limite", font_size=20, weight="BOLD"),
            MathTex(r"\sin \lambda = \dfrac{n_2}{n_1} \ (n_1 > n_2)", font_size=26),
        ).arrange(DOWN, buff=0.2)
        ligne2 = VGroup(bloc3, bloc4).arrange(RIGHT, buff=1.0)
        ligne2_box = property_box(ligne2, box_width=12.2)
        ligne2_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La loi de Snell-Descartes de la réfraction s'écrit n1 "
                "sinus i1 égale n2 sinus i2. L'angle limite lambda, "
                "défini uniquement quand n1 est supérieur à n2, vérifie "
                "sinus de lambda égale n2 sur n1."
            )
        ) as tracker:
            self.play(FadeIn(ligne2_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ligne2_box))

        # --- Tableau 3 : réflexion totale et lame à faces parallèles -------------------
        bloc5 = VGroup(
            Text("Réflexion totale", font_size=20, weight="BOLD"),
            MathTex(r"n_1 > n_2 \ \text{ET} \ i_1 > \lambda", font_size=24),
        ).arrange(DOWN, buff=0.2)
        bloc6 = VGroup(
            Text("Lame à faces parallèles", font_size=20, weight="BOLD"),
            MathTex(r"i_1' = i_1 \ , \quad d = e\dfrac{\sin(i_1-i_2)}{\cos i_2}", font_size=22),
        ).arrange(DOWN, buff=0.2)
        ligne3 = VGroup(bloc5, bloc6).arrange(RIGHT, buff=1.0)
        ligne3_box = property_box(ligne3, box_width=12.4)
        ligne3_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La réflexion totale se produit si, et seulement si, n1 "
                "est supérieur à n2 et l'angle d'incidence i1 est "
                "supérieur à l'angle limite. Enfin, pour une lame à "
                "faces parallèles, le rayon émergent est parallèle au "
                "rayon incident, i'1 égale i1, mais déplacé "
                "latéralement d'une distance d égale e fois sinus de i1 "
                "moins i2, sur cosinus de i2."
            )
        ) as tracker:
            self.play(FadeIn(ligne3_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ligne3_box))

        # --- Synthèse finale complète ----------------------------------------------------
        synthese = essentiel_box(
            VGroup(
                Text("Toutes les formules du chapitre", font_size=23, weight="BOLD"),
                MathTex(r"i_1' = i_1 \quad ; \quad n = \dfrac{c}{v} \quad ; \quad n_1 \sin i_1 = n_2 \sin i_2", font_size=22),
                MathTex(r"\sin \lambda = \dfrac{n_2}{n_1} \quad ; \quad \text{réflexion totale} \Leftrightarrow n_1>n_2 \ \text{et} \ i_1 > \lambda", font_size=20, color=YELLOW),
                MathTex(r"\text{lame} : \quad i_1' = i_1 \ , \quad d = e\dfrac{\sin(i_1-i_2)}{\cos i_2}", font_size=22),
            ).arrange(DOWN, buff=0.24),
            box_width=12.8,
        )
        synthese.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici donc l'ensemble des formules à connaître par "
                "cœur pour ce chapitre : la loi de la réflexion, la "
                "définition de l'indice de réfraction, la loi de "
                "Snell-Descartes de la réfraction, l'angle limite, la "
                "condition de réflexion totale, et enfin les deux "
                "propriétés de la lame à faces parallèles."
            )
        ) as tracker:
            self.play(FadeIn(synthese))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(synthese), FadeOut(titre))
