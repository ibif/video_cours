"""
scenes/Physique_TravailPuissanceTranslation_07.py — Chapitre 1 « Travail et
puissance dans le cas d'un mouvement de translation » (1ereC, Physique),
scène 07.

§ Rendement d'une machine r = Pu/Pt = Wu/Wt, toujours compris entre 0 et 1
(souvent exprimé en %). Exemple résolu 5 : treuil électrique Pt=250 W,
Pu=200 W.
Source : 1ereC/Physique.pdf, chapitre 1, pages 4-12.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, Arrow, FadeIn, FadeOut, MathTex, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import (
    corrige_box,
    definition_box,
    essentiel_box,
    exercise_box,
    scene_title,
    warning_box,
)


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class RendementMachine(NotionScene):
    def construct(self):
        titre = scene_title("Rendement d'une machine")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------------
        machine = Rectangle(width=2.2, height=1.4, color="#FFFFFF", fill_color="#3A3A3A", fill_opacity=0.9)
        entree = Arrow(machine.get_left() + LEFT * 1.3, machine.get_left(), color=YELLOW, buff=0)
        sortie_utile = Arrow(machine.get_right(), machine.get_right() + RIGHT * 1.5, color="#288073", buff=0)
        sortie_perdue = Arrow(machine.get_bottom(), machine.get_bottom() + DOWN * 1.2, color="#B42E41", buff=0)
        label_pt = MathTex(r"P_t", font_size=24, color=YELLOW).next_to(entree, LEFT, buff=0.1)
        label_pu = MathTex(r"P_u", font_size=24, color="#288073").next_to(sortie_utile, RIGHT, buff=0.1)
        label_perdue = MathTex(r"P_{\text{perdue}}", font_size=22, color="#B42E41").next_to(
            sortie_perdue, DOWN, buff=0.1
        )
        figure = VGroup(machine, entree, sortie_utile, sortie_perdue, label_pt, label_pu, label_perdue)
        figure.move_to(DOWN * 0.3)

        mise_en_situation = Text(
            _wrap(
                "Aucune machine ne restitue toute l'énergie qu'elle reçoit "
                ": une partie se perd toujours, le plus souvent sous forme "
                "de chaleur due aux frottements.",
                width=54,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Aucune machine ne restitue la totalité de l'énergie "
                "qu'elle reçoit : une partie se perd toujours, le plus "
                "souvent sous forme de chaleur due aux frottements "
                "internes. Le rendement mesure la part réellement utile de "
                "cette énergie."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(figure))

        # --- Raisonnement : définition -----------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Rendement d'une machine", font_size=23, weight="BOLD"),
                MathTex(r"r = \dfrac{P_u}{P_t} = \dfrac{W_u}{W_t}", font_size=30),
                Text(
                    "Pu, Wu : puissance/travail UTILE — Pt, Wt : puissance/travail TOTAL(E)",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le rendement r d'une machine est le rapport de la "
                "puissance utile P-u, celle réellement exploitée, sur la "
                "puissance totale P-t, celle réellement reçue par la "
                "machine. On peut calculer ce même rapport avec les "
                "travaux, W-u sur W-t, sur une même durée."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        propriete = warning_box(
            MathTex(
                r"0 < r \le 1 \quad \text{(ou } 0\%<r\le100\%\text{)}",
                font_size=28,
            ),
            box_width=8.5,
        )
        propriete.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le rendement est toujours compris entre zéro et un, "
                "puisque l'énergie utile ne peut jamais dépasser l'énergie "
                "totale reçue. On l'exprime souvent en pourcentage, entre "
                "zéro et cent pour cent."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple traité 5 : treuil électrique ----------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Un treuil électrique reçoit une puissance totale "
                    "Pt = 250 W et fournit une puissance utile Pu = 200 W "
                    "pour soulever une charge. Calculer son rendement et la "
                    "puissance perdue.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. Un treuil électrique reçoit une puissance "
                "totale de deux cent cinquante watts, et fournit une "
                "puissance utile de deux cents watts pour soulever une "
                "charge. Calculons son rendement, ainsi que la puissance "
                "perdue."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc = corrige_box(
            VGroup(
                MathTex(r"r = \dfrac{P_u}{P_t} = \dfrac{200}{250} = 0{,}80 = 80\%", font_size=27, color=YELLOW),
                MathTex(r"P_{\text{perdue}} = P_t - P_u = 250-200 = 50\ W", font_size=26),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        calc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le rendement vaut deux cents divisé par deux cent "
                "cinquante, soit zéro virgule quatre-vingts, c'est-à-dire "
                "quatre-vingts pour cent. La puissance perdue, elle, se "
                "calcule directement par différence : deux cent cinquante "
                "moins deux cents, soit cinquante watts, dissipés "
                "essentiellement sous forme de chaleur."
            )
        ) as tracker:
            self.play(FadeIn(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            MathTex(r"r = \dfrac{P_u}{P_t} = \dfrac{W_u}{W_t}, \quad 0<r\le1", font_size=28),
            box_width=8.5,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : le rendement est le rapport de l'utile sur le "
                "total, en puissance comme en travail, et il reste toujours "
                "compris entre zéro et un."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le rendement (un nombre sans dimension, entre 0 et 1) "
                    "n'est PAS la puissance perdue (exprimée en watts) : "
                    "ce sont deux grandeurs différentes, ne pas les "
                    "confondre ni les additionner entre elles.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège fréquent : le rendement, un simple nombre sans "
                "dimension compris entre zéro et un, n'est pas la puissance "
                "perdue, qui elle s'exprime en watts. Ce sont deux "
                "grandeurs de nature différente, à ne jamais confondre ni "
                "additionner entre elles."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
