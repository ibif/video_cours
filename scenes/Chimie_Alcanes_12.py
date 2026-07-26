"""
scenes/Chimie_Alcanes_12.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 12.

§ 7.3 La réaction de substitution : chloration du méthane (définition,
réaction photochimique, les 4 équations successives CH₄→CH₃Cl→CH₂Cl₂→
CHCl₃→CCl₄ avec HCl, notion de radicaux libres) + § 7.4 mécanisme
simplifié en 3 phases (initiation / propagation / terminaison).
Source : 1ereC/Chimie.pdf, pages 22-23.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    ORANGE,
    GREEN,
    RED,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class SubstitutionChlorationMethane(NotionScene):
    def construct(self):
        titre = scene_title("7. La réaction de substitution : chloration du méthane")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : définition de la substitution ------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une réaction de substitution est une réaction au "
                    "cours de laquelle un atome (ou un groupe d'atomes) "
                    "d'une molécule est remplacé par un autre atome (ou "
                    "groupe d'atomes).",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une réaction de substitution est une réaction au cours "
                "de laquelle un atome, ou un groupe d'atomes, d'une "
                "molécule est remplacé par un autre atome, ou un autre "
                "groupe d'atomes. Voyons l'exemple de la chloration du "
                "méthane."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les 4 équations successives de chloration -----------
        entete_eq = Text("Sous la lumière : substitutions successives", font_size=20, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.35)

        eq1 = MathTex(r"CH_4 + Cl_2 \xrightarrow{\text{lumière}} CH_3Cl + HCl", font_size=24, color=WHITE)
        eq2 = MathTex(r"CH_3Cl + Cl_2 \xrightarrow{\text{lumière}} CH_2Cl_2 + HCl", font_size=24, color=WHITE)
        eq3 = MathTex(r"CH_2Cl_2 + Cl_2 \xrightarrow{\text{lumière}} CHCl_3 + HCl", font_size=24, color=WHITE)
        eq4 = MathTex(r"CHCl_3 + Cl_2 \xrightarrow{\text{lumière}} CCl_4 + HCl", font_size=24, color=WHITE)
        equations = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        equations.next_to(entete_eq, DOWN, buff=0.35)
        _fit(equations, entete_eq.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Sous l'action de la lumière, on parle de réaction "
                "photochimique, le dichlore réagit avec le méthane : "
                "chaque atome de chlore se substitue à un atome "
                "d'hydrogène. Il se forme successivement quatre produits "
                "chlorés, avec un dégagement de chlorure d'hydrogène à "
                "chaque étape : d'abord le monochlorométhane, puis le "
                "dichlorométhane, puis le trichlorométhane, ou "
                "chloroforme, et enfin le tétrachlorométhane. En "
                "pratique, on obtient un mélange des quatre produits."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(eq1))
            self.play(Write(eq2))
            self.play(Write(eq3))
            self.play(Write(eq4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(equations))

        # --- Exemple traité : notion de radical libre + mécanisme en 3 phases ---
        radical = Text(
            _wrap(
                "La réaction est dite radicalaire : elle fait intervenir "
                "des radicaux libres — espèces très réactives portant un "
                "électron célibataire, notées avec un point : Cl•, CH₃•.",
                width=52,
            ),
            font_size=23,
            color=WHITE,
        )
        radical.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Cette réaction est dite radicalaire : elle fait "
                "intervenir des espèces très réactives, porteuses d'un "
                "électron célibataire, appelées radicaux libres, et "
                "notées avec un point, comme chlore-point ou "
                "C-H-3-point."
            )
        ) as tracker:
            self.play(FadeIn(radical))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(radical))

        entete_meca = Text("Mécanisme simplifié en 3 phases", font_size=23, color=YELLOW, weight="BOLD")
        entete_meca.next_to(titre, DOWN, buff=0.35)

        # phase 1 : initiation
        boite1 = Rectangle(width=3.4, height=1.5, color=ORANGE, stroke_width=3)
        titre1 = Text("1. Initiation", font_size=18, color=ORANGE, weight="BOLD")
        eq_init = MathTex(r"Cl_2 \xrightarrow{\text{lumière}} 2\,Cl^{\bullet}", font_size=20, color=WHITE)
        contenu1 = VGroup(titre1, eq_init).arrange(DOWN, buff=0.2).move_to(boite1.get_center())
        bloc1 = VGroup(boite1, contenu1)

        # phase 2 : propagation
        boite2 = Rectangle(width=3.8, height=1.5, color=GREEN, stroke_width=3)
        titre2 = Text("2. Propagation", font_size=18, color=GREEN, weight="BOLD")
        eq_prop1 = MathTex(r"Cl^{\bullet}+CH_4 \rightarrow HCl+CH_3^{\bullet}", font_size=16, color=WHITE)
        eq_prop2 = MathTex(r"CH_3^{\bullet}+Cl_2 \rightarrow CH_3Cl+Cl^{\bullet}", font_size=16, color=WHITE)
        contenu2 = VGroup(titre2, eq_prop1, eq_prop2).arrange(DOWN, buff=0.15).move_to(boite2.get_center())
        bloc2 = VGroup(boite2, contenu2)

        # phase 3 : terminaison
        boite3 = Rectangle(width=3.4, height=1.5, color=RED, stroke_width=3)
        titre3 = Text("3. Terminaison", font_size=18, color=RED, weight="BOLD")
        eq_term = MathTex(r"Cl^{\bullet}+Cl^{\bullet} \rightarrow Cl_2", font_size=20, color=WHITE)
        contenu3 = VGroup(titre3, eq_term).arrange(DOWN, buff=0.2).move_to(boite3.get_center())
        bloc3 = VGroup(boite3, contenu3)

        fleche_a = Arrow(bloc1.get_right(), bloc2.get_left(), color=WHITE, buff=0.15)
        fleche_b = Arrow(bloc2.get_right(), bloc3.get_left(), color=WHITE, buff=0.15)

        trois_phases = VGroup(bloc1, fleche_a, bloc2, fleche_b, bloc3).arrange(RIGHT, buff=0.3)
        trois_phases.next_to(entete_meca, DOWN, buff=0.45)
        _fit(trois_phases, entete_meca.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "La chloration du méthane se déroule en trois phases. "
                "Phase un, l'initiation : sous l'effet de la lumière, la "
                "molécule de dichlore se scinde en deux radicaux chlore. "
                "Phase deux, la propagation, une réaction en chaîne : le "
                "radical chlore arrache un hydrogène au méthane, formant "
                "du chlorure d'hydrogène et un radical méthyle ; ce "
                "radical méthyle réagit à son tour avec le dichlore, "
                "formant du chlorométhane et régénérant le radical "
                "chlore. Tant qu'il reste des réactifs, la chaîne se "
                "poursuit. Phase trois, la terminaison : deux radicaux se "
                "recombinent, par exemple deux radicaux chlore qui "
                "reforment du dichlore, et la chaîne s'arrête."
            )
        ) as tracker:
            self.play(FadeIn(entete_meca))
            self.play(FadeIn(bloc1))
            self.play(FadeIn(fleche_a), FadeIn(bloc2))
            self.play(FadeIn(fleche_b), FadeIn(bloc3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_meca), FadeOut(trois_phases))

        # --- À retenir : méthode condensée du mécanisme --------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Initiation : rupture de Cl₂ sous la lumière (2 "
                    "radicaux). Propagation : le radical Cl• arrache un H "
                    "à l'alcane (→ HCl), le radical alkyle formé réagit "
                    "avec Cl₂ (→ produit chloré + régénère Cl•) : la "
                    "chaîne s'entretient elle-même. Terminaison : deux "
                    "radicaux se recombinent, la chaîne s'arrête.",
                    width=52,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons la méthode : à l'initiation, la lumière casse "
                "le dichlore en deux radicaux. À la propagation, le "
                "radical chlore arrache un hydrogène à l'alcane pour "
                "former du chlorure d'hydrogène, le radical formé réagit "
                "avec le dichlore pour donner le produit chloré et "
                "régénérer un radical chlore : la chaîne s'entretient "
                "elle-même. À la terminaison, deux radicaux se "
                "recombinent et la chaîne s'arrête."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : sous-produit HCl, pas Cl₂ --------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le sous-produit de la substitution est le chlorure "
                    "d'hydrogène HCl, PAS du dichlore Cl₂. Et il faut "
                    "autant de molécules Cl₂ que d'atomes H remplacés : "
                    "pour passer de CH₄ à CCl₄, il faut 4 Cl₂ (une par "
                    "étape).",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : le sous-produit de la substitution est le "
                "chlorure d'hydrogène, H-C-l, et non du dichlore. Et il "
                "faut autant de molécules de dichlore que d'atomes "
                "d'hydrogène remplacés : pour passer du méthane au "
                "tétrachlorométhane, il faut quatre molécules de "
                "dichlore, une à chaque étape."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
