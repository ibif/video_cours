"""
scenes/Physique_EnergieMecanique_07.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 07.

Application : chute libre (loi complète). Em=mgh=constante en chute libre
(seul le poids travaille). Vitesse à l'altitude z : v=√(2g(h-z)), vitesse
au sol v_sol=√(2gh) (loi de Torricelli). Cas général avec vitesse initiale.
Exemple résolu 4 : mangue 150 g tombe de h=6 m → Em=9 J, v_sol≈11 m/s,
altitude où Ec=Ep : z=h/2=3 m (résultat général : mi-hauteur en chute
libre sans vitesse initiale).
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    DashedLine,
    Dot,
    DoubleArrow,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, exercise_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ApplicationChuteLibre(NotionScene):
    def construct(self):
        titre = scene_title("Application : la chute libre")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : loi complète en chute libre -------------------------------------
        haut = UP * 1.5 + LEFT * 3.5
        bas = DOWN * 1.5 + LEFT * 3.5
        chute_ligne = DashedLine(haut, bas, color=WHITE, stroke_width=2)
        fruit = Dot(haut, color=YELLOW, radius=0.13)
        h_fleche = DoubleArrow(haut + RIGHT * 0.7, bas + RIGHT * 0.7, buff=0, stroke_width=2, color=WHITE)
        h_label = MathTex("h", font_size=26).next_to(h_fleche, RIGHT, buff=0.12)
        sol = DashedLine(bas + LEFT * 0.6, bas + RIGHT * 1.7, color=WHITE, stroke_width=2)
        schema = VGroup(chute_ligne, fruit, h_fleche, h_label, sol)
        schema.move_to(LEFT * 3.0)

        intro = Text(
            _wrap(
                "En chute libre, seul le poids travaille : la conservation "
                "de l'énergie mécanique s'applique intégralement. "
                "Reprenons ce cas en détail.",
                width=40,
            ),
            font_size=21,
        )
        intro.next_to(schema, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "En chute libre, seul le poids s'exerce sur le système : la "
                "loi de conservation de l'énergie mécanique s'applique "
                "donc intégralement. Reprenons ce cas fondamental, dans "
                "toute sa généralité."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(schema), FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(intro))

        # --- Raisonnement : Em=mgh=constante, puis v(z) et v_sol -----------------------
        em_const = property_box(
            VGroup(
                Text("Origine au sol, chute d'une hauteur h, sans vitesse initiale :", font_size=20),
                MathTex(r"E_m = E_{pp}(\text{sommet}) = mgh = \text{constante}", font_size=27),
            ).arrange(DOWN, buff=0.22),
            box_width=10.4,
        )
        em_const.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En prenant l'origine des altitudes au sol, et pour une "
                "chute d'une hauteur h sans vitesse initiale, l'énergie "
                "mécanique est constante, et égale à l'énergie potentielle "
                "au sommet, soit m g h."
            )
        ) as tracker:
            self.play(FadeIn(em_const))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(em_const))

        vitesse_z = MathTex(
            r"E_m = \tfrac{1}{2}mv(z)^2 + mgz = mgh \ \Longrightarrow\ v(z) = \sqrt{2g(h - z)}",
            font_size=25,
        )
        vitesse_sol = MathTex(
            r"z = 0 \ \Longrightarrow\ v_{sol} = \sqrt{2gh} \quad \text{(loi de Torricelli)}",
            font_size=27,
            color=YELLOW,
        )
        vitesses = VGroup(vitesse_z, vitesse_sol).arrange(DOWN, buff=0.4)
        vitesses.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "À une altitude z quelconque, l'énergie mécanique s'écrit "
                "un demi m v de z au carré plus m g z, égale m g h. On en "
                "déduit v de z égale racine de deux g fois h moins z. Au "
                "niveau du sol, où z est nul, on retrouve la vitesse "
                "d'impact v sol égale racine de deux g h, connue sous le "
                "nom de loi de Torricelli."
            )
        ) as tracker:
            self.play(Write(vitesse_z))
            self.play(Write(vitesse_sol))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vitesses))

        cas_general = property_box(
            Text(
                _wrap(
                    "Cas général (vitesse initiale v₀ non nulle) : "
                    "Em=½mv₀²+mgh=constante, la même méthode s'applique "
                    "avec v₀ au lieu de 0.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=10.6,
        )
        cas_general.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Cas plus général : si le mobile part avec une vitesse "
                "initiale v zéro non nulle, la même méthode s'applique, en "
                "remplaçant simplement zéro par v zéro au carré dans le "
                "calcul de l'énergie mécanique initiale."
            )
        ) as tracker:
            self.play(FadeIn(cas_general))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_general))

        # --- Exemple traité : mangue --------------------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Une mangue de masse 150 g tombe en chute libre, sans "
                    "vitesse initiale, d'une hauteur h=6 m. Calculer Em, "
                    "la vitesse au sol, puis l'altitude où Ec=Ep (g=10 N/kg).",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu. Une mangue de masse cent cinquante "
                "grammes tombe en chute libre, sans vitesse initiale, "
                "d'une hauteur de six mètres. Calculons son énergie "
                "mécanique, sa vitesse au sol, puis l'altitude à laquelle "
                "l'énergie cinétique égale l'énergie potentielle."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc1 = MathTex(r"E_m = mgh = 0{,}15\times 10\times 6 = 9\ \text{J}", font_size=26)
        calc2 = MathTex(r"v_{sol} = \sqrt{2\times 10\times 6} \approx 10{,}95 \approx 11\ \text{m/s}", font_size=26)
        calc3 = MathTex(r"E_c = E_p \ \Longrightarrow\ E_p = \tfrac{E_m}{2} = mgz \ \Longrightarrow\ z = \dfrac{h}{2} = 3\ \text{m}", font_size=25, color=YELLOW)
        calc = VGroup(calc1, calc2, calc3).arrange(DOWN, buff=0.3)
        calc.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'énergie mécanique vaut zéro virgule quinze fois dix fois "
                "six, soit neuf joules. La vitesse au sol vaut racine de "
                "deux fois dix fois six, soit environ onze mètres par "
                "seconde. Enfin, quand Ec égale Ep, chacune vaut la moitié "
                "de l'énergie mécanique, donc m g z égale la moitié de m g "
                "h, ce qui donne z égale h sur deux, soit trois mètres : "
                "exactement à mi-hauteur de la chute."
            )
        ) as tracker:
            self.play(Write(calc1))
            self.play(Write(calc2))
            self.play(Write(calc3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ---------------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                MathTex(r"v_{sol} = \sqrt{2gh} \quad \text{(loi de Torricelli)}", font_size=26),
                Text("Sans vitesse initiale : Ec=Ep exactement à mi-hauteur (z=h/2).", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons deux résultats essentiels : la vitesse au sol "
                "vaut racine de deux g h, c'est la loi de Torricelli. Et, "
                "sans vitesse initiale, l'énergie cinétique égale "
                "l'énergie potentielle exactement à mi-hauteur de la "
                "chute — un résultat général, valable quelle que soit la "
                "hauteur de départ."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : le résultat « mi-hauteur » ne vaut QUE sans "
                    "vitesse initiale et sans frottement. Avec v₀≠0, il "
                    "faut refaire le calcul complet, pas appliquer z=h/2 "
                    "aveuglément.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter : le résultat de la mi-hauteur ne vaut que "
                "sans vitesse initiale et sans frottement. Si la vitesse "
                "initiale n'est pas nulle, il faut refaire le calcul "
                "complet à partir de la conservation de l'énergie "
                "mécanique, et non appliquer aveuglément z égale h sur "
                "deux."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
