"""
scenes/Chimie_Alcanes_06.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 06.

§ 4. Les cyclanes (cycloalcanes) : définition, formule générale CₙH₂ₙ,
nomenclature (préfixe cyclo), exemples cyclopropane / cyclobutane /
cyclopentane / cyclohexane, cyclanes ramifiés, et le piège
CₙH₂ₙ ≠ CₙH₂ₙ₊₂. Source : 1ereC/Chimie.pdf, page 19.
"""

import textwrap

import numpy as np
from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _cycle(n, rayon=0.55, font_size=22, label=""):
    sommets = [
        np.array([rayon * np.cos(2 * np.pi * k / n + np.pi / 2), rayon * np.sin(2 * np.pi * k / n + np.pi / 2), 0])
        for k in range(n)
    ]
    atomes = VGroup(*[MathTex("C", font_size=font_size, color=BLUE).move_to(p) for p in sommets])
    liaisons = VGroup(*[Line(sommets[k], sommets[(k + 1) % n], color=WHITE, stroke_width=3) for k in range(n)])
    etiquette = Text(label, font_size=16, color=YELLOW)
    schema = VGroup(liaisons, atomes)
    groupe = VGroup(schema, etiquette).arrange(DOWN, buff=0.3)
    return groupe


class CyclanesCycloalcanes(NotionScene):
    def construct(self):
        titre = scene_title("4. Les cyclanes (cycloalcanes)")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition du cyclane --------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Les cyclanes (ou cycloalcanes) sont des hydrocarbures "
                    "saturés dont toutes les liaisons C–C sont des "
                    "liaisons simples et dont la chaîne carbonée se "
                    "referme sur elle-même (cycle).",
                    width=48,
                ),
                font_size=24,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les cyclanes, ou cycloalcanes, sont des hydrocarbures "
                "saturés dont toutes les liaisons carbone-carbone sont des "
                "liaisons simples, et dont la chaîne carbonée se referme "
                "sur elle-même : on parle de cycle."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : formule générale CₙH₂ₙ -------------------------------
        formule = property_box(
            MathTex(r"C_nH_{2n} \quad (n \geq 3)", font_size=34, color="#1A1A1A"),
        )
        formule.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Leur formule brute générale est C indice n, H indice deux "
                "n, avec n supérieur ou égal à trois : la fermeture du "
                "cycle fait perdre deux atomes d'hydrogène par rapport à "
                "un alcane linéaire de même n."
            )
        ) as tracker:
            self.play(FadeIn(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule))

        # --- Exemple traité : les 4 cyclanes usuels + nomenclature --------------
        entete_ex = Text("Nomenclature : préfixe « cyclo » + nom de l'alcane", font_size=20, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.35)

        c3 = _cycle(3, label="cyclopropane\nC₃H₆")
        c4 = _cycle(4, label="cyclobutane\nC₄H₈")
        c5 = _cycle(5, label="cyclopentane\nC₅H₁₀")
        c6 = _cycle(6, label="cyclohexane\nC₆H₁₂")

        quatre_cycles = VGroup(c3, c4, c5, c6).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        quatre_cycles.next_to(entete_ex, DOWN, buff=0.5)
        _fit(quatre_cycles, entete_ex.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Le nom d'un cyclane non ramifié s'obtient en faisant "
                "précéder du préfixe cyclo le nom de l'alcane linéaire "
                "correspondant. Voici les quatre plus simples : le "
                "cyclopropane, C-3, H-6 ; le cyclobutane, C-4, H-8 ; le "
                "cyclopentane, C-5, H-10 ; et le cyclohexane, C-6, H-12."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(quatre_cycles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(quatre_cycles))

        entete_ram = Text("Cyclanes ramifiés : mêmes règles, cycle numéroté", font_size=21, color=YELLOW, weight="BOLD")
        entete_ram.next_to(titre, DOWN, buff=0.4)

        exemples_ram = VGroup(
            Text("méthylcyclobutane", font_size=24, color=WHITE),
            Text("1-éthyl-2-méthylcyclopentane", font_size=24, color=WHITE),
            Text("1,3-diméthylcyclohexane", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        exemples_ram.next_to(entete_ram, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Pour les cyclanes ramifiés, on applique les mêmes règles "
                "que pour les alcanes ramifiés, en numérotant le cycle de "
                "façon à donner les indices les plus petits aux "
                "substituants : méthylcyclobutane, un-éthyl-deux-"
                "méthylcyclopentane, ou encore un-virgule-trois-"
                "diméthylcyclohexane."
            )
        ) as tracker:
            self.play(FadeIn(entete_ram))
            self.play(FadeIn(exemples_ram))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ram), FadeOut(exemples_ram))

        # --- À retenir : différence structurelle avec les alcanes --------------
        propriete = property_box(
            Text(
                _wrap(
                    "Un cyclane à n carbones a toujours 2 atomes "
                    "d'hydrogène de moins qu'un alcane à n carbones : "
                    "CₙH₂ₙ contre CₙH₂ₙ₊₂. C'est la fermeture du cycle qui "
                    "« consomme » ces deux hydrogènes.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ceci : un cyclane à n carbones possède toujours "
                "deux atomes d'hydrogène de moins qu'un alcane à n "
                "carbones. C'est précisément la fermeture du cycle qui "
                "consomme ces deux atomes d'hydrogène."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : CₙH₂ₙ n'est PAS un alcane -------------------------
        piege = warning_box(
            MathTex(
                r"\text{Un cyclane en } C_nH_{2n} \text{ n'est PAS un alcane } C_nH_{2n+2} !",
                font_size=27,
                color="#1A1A1A",
            ),
            box_width=11.5,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        exemple_piege = Text(
            "Ne dites jamais « le cyclohexane est C₆H₁₄ » : c'est C₆H₁₂ !",
            font_size=22,
            color=WHITE,
        )
        exemple_piege.next_to(piege, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention, piège classique : un cyclane de formule C "
                "indice n, H indice deux n, ne vérifie pas la formule des "
                "alcanes, C indice n, H indice deux n plus deux. Ne dites "
                "donc jamais que le cyclohexane est C-6, H-14 : c'est "
                "C-6, H-12."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.play(FadeIn(exemple_piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(exemple_piege), FadeOut(titre))
