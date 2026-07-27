"""
scenes/Maths_EtudeGraphiqueFonctions_08.py — Chapitre 11 (1ereC, Maths), scène 08.

Fonctions irrationnelles simples (domaine, dérivée (√u)' = u'/(2√u), piège
de la demi-tangente verticale, exemple f(x) = √(x²-4)) et fonctions
trigonométriques simples (démarche périodicité → parité → dérivée, exemple
f(x) = sin(2x)).
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

import numpy as np

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class FonctionsIrrationnellesTrigonometriques(NotionScene):
    def construct(self):
        titre = scene_title("Fonctions irrationnelles et trigonométriques simples")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Deux dernières familles : racine carrée et trigonométrie",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons le tour des familles de fonctions avec deux cas "
                "particuliers : les fonctions irrationnelles, contenant une "
                "racine carrée, et les fonctions trigonométriques simples."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Fonctions irrationnelles : domaine et dérivée -------------------
        def_irrationnelle = definition_box(
            MathTex(
                r"f(x) = \sqrt{u(x)} \ , \quad D_f = \{x \, / \, u(x) \geq 0\}"
                r"\ , \quad f'(x) = \dfrac{u'(x)}{2\sqrt{u(x)}}",
                font_size=27,
            ),
            box_width=11.4,
        )
        def_irrationnelle.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour une fonction irrationnelle f de x égale racine de u "
                "de x, le domaine est l'ensemble des x où u de x est "
                "positif ou nul. La dérivée vaut u prime de x, sur deux "
                "racine de u de x — formule à connaître par cœur."
            )
        ) as tracker:
            self.play(FadeIn(def_irrationnelle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_irrationnelle))

        piege_tangente = warning_box(
            Text(
                _wrap(
                    "Piège : là où u(x) = 0, le dénominateur 2√u(x) "
                    "s'annule, donc f n'est PAS dérivable en ce point — la "
                    "courbe présente une demi-tangente verticale.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        piege_tangente.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fondamental : là où u de x s'annule, le dénominateur "
                "deux racine de u de x s'annule aussi, donc f n'est pas "
                "dérivable en ce point précis. La courbe présente alors une "
                "demi-tangente verticale, pas un point anguleux ordinaire."
            )
        ) as tracker:
            self.play(FadeIn(piege_tangente))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_tangente))

        # --- Exemple : f(x) = √(x²-4) ------------------------------------------
        enonce_ex1 = Text(
            "Exemple — f(x) = √(x²-4)",
            font_size=27,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : étudions f de x égale racine de x carré moins "
                "quatre."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex1))

        calcul_ex1a = example_box(
            MathTex(
                r"""
                x^2-4\geq0 \ \Longleftrightarrow \ x\leq-2 \text{ ou } x\geq2
                \ \Longrightarrow \
                D_f = \left]-\infty\,;-2\right]\cup\left[2\,;+\infty\right[
                """,
                font_size=24,
            ),
            box_width=11.4,
        )
        calcul_ex1a.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le domaine impose x carré moins quatre positif ou nul, "
                "c'est-à-dire x inférieur ou égal à moins deux, ou x "
                "supérieur ou égal à deux. Df est donc la réunion de deux "
                "demi-droites."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex1a))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex1a))

        calcul_ex1b = example_box(
            MathTex(
                r"D_f \text{ symétrique} \ ,\ f(-x)=\sqrt{(-x)^2-4}=\sqrt{x^2-4}=f(x)"
                r"\ \Longrightarrow \ f \text{ paire}",
                font_size=24,
            ),
            box_width=11.4,
        )
        calcul_ex1b.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ce domaine est symétrique par rapport à zéro, et f de "
                "moins x égale racine de moins x au carré moins quatre, "
                "identique à f de x : la fonction est paire. On réduit "
                "donc l'étude à x supérieur ou égal à deux."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex1b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex1b))

        calcul_ex1c = example_box(
            MathTex(
                r"""
                \sqrt{x^2-4}-x = \dfrac{-4}{\sqrt{x^2-4}+x}
                \ \xrightarrow[x\to+\infty]{} \ 0
                \ \Longrightarrow \ y=x \text{ asymptote oblique en } +\infty
                """,
                font_size=22,
            ),
            box_width=11.6,
        )
        calcul_ex1c.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En plus l'infini, la quantité conjuguée montre que racine "
                "de x carré moins quatre, moins x, tend vers zéro : la "
                "droite y égale x est asymptote oblique en plus l'infini, "
                "et par symétrie, y égale moins x l'est en moins l'infini."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex1c))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex1c))

        calcul_ex1d = example_box(
            Text(
                _wrap(
                    "En x = 2 : u(2) = 0, donc f n'est pas dérivable en 2 "
                    "— la courbe présente une demi-tangente verticale au "
                    "point (2 ; 0).",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        calcul_ex1d.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En x égale deux, u de x s'annule, donc f n'est pas "
                "dérivable en ce point : la courbe présente une "
                "demi-tangente verticale au point de coordonnées deux et "
                "zéro, exactement le piège annoncé plus tôt."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex1d))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex1d))

        axes = Axes(
            x_range=[-6, 6, 2], y_range=[0, 5, 1], x_length=7.0, y_length=3.3,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(titre.get_center() + DOWN * 3.4)

        def g(x):
            return (x**2 - 4) ** 0.5

        courbe_droite = axes.plot(g, x_range=[2, 5.6], color="#1E90FF")
        courbe_gauche = axes.plot(g, x_range=[-5.6, -2], color="#1E90FF")
        asym1 = axes.plot(lambda x: x, x_range=[0, 6], color=YELLOW)
        asym2 = axes.plot(lambda x: -x, x_range=[-6, 0], color=YELLOW)
        schema = VGroup(axes, courbe_droite, courbe_gauche, asym1, asym2)

        with self.voiceover(
            text=(
                "Voici la courbe : deux branches symétriques par rapport à "
                "l'axe des ordonnées, chacune avec une demi-tangente "
                "verticale à son extrémité, se rapprochant des deux "
                "asymptotes obliques."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Fonctions trigonométriques : démarche ---------------------------
        methode_trigo = method_box(
            Text(
                _wrap(
                    "Démarche pour une fonction trigonométrique : d'abord "
                    "la périodicité (réduire à un intervalle de longueur "
                    "T), puis la parité sur cet intervalle réduit, puis "
                    "seulement ensuite la dérivée sur le domaine réduit.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        methode_trigo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour une fonction trigonométrique, l'ordre change "
                "légèrement : on cherche d'abord la périodicité, pour "
                "réduire l'étude à un intervalle de longueur T. Puis, sur "
                "cet intervalle réduit, on cherche une parité éventuelle. "
                "C'est seulement ensuite qu'on étudie la dérivée, sur ce "
                "domaine déjà bien réduit."
            )
        ) as tracker:
            self.play(FadeIn(methode_trigo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_trigo))

        # --- Exemple : f(x) = sin(2x) -------------------------------------------
        enonce_ex2 = Text(
            "Exemple — f(x) = sin(2x)",
            font_size=27,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : étudions f de x égale sinus de deux x, définie "
                "sur ℝ."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex2))

        calcul_ex2a = example_box(
            MathTex(
                r"f(x+\pi) = \sin(2x+2\pi) = \sin(2x) = f(x)"
                r"\ \Longrightarrow \ \text{période } \pi",
                font_size=27,
            ),
            box_width=10.5,
        )
        calcul_ex2a.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "f de x plus pi égale sinus de deux x plus deux pi, égale "
                "sinus de deux x, égale f de x : la fonction est périodique "
                "de période pi. On réduit donc l'étude à un intervalle de "
                "longueur pi."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex2a))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex2a))

        calcul_ex2b = example_box(
            MathTex(
                r"f(-x) = \sin(-2x) = -\sin(2x) = -f(x)"
                r"\ \Longrightarrow \ f \text{ impaire, étude sur } "
                r"\left[0\,;\dfrac{\pi}{2}\right]",
                font_size=25,
            ),
            box_width=11.4,
        )
        calcul_ex2b.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "f de moins x égale sinus de moins deux x, égale moins "
                "sinus de deux x, égale moins f de x : la fonction est "
                "impaire. Combinée à la période pi, l'étude se réduit à "
                "l'intervalle zéro, pi sur deux."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex2b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex2b))

        calcul_ex2c = example_box(
            MathTex(
                r"f'(x) = 2\cos(2x) \ \geq 0 \ \text{ sur } "
                r"\left[0\,;\dfrac{\pi}{4}\right]"
                r"\ \Longrightarrow \ f \text{ croissante puis décroissante}",
                font_size=25,
            ),
            box_width=11.4,
        )
        calcul_ex2c.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La dérivée vaut deux cosinus de deux x, positive sur zéro, "
                "pi sur quatre, puis négative sur pi sur quatre, pi sur "
                "deux : f croît jusqu'à son maximum un, puis redécroît "
                "jusqu'à zéro."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex2c))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex2c))

        axes2 = Axes(
            x_range=[-3.4, 3.4, 1], y_range=[-1.3, 1.3, 1], x_length=8.0, y_length=3.2,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes2.move_to(titre.get_center() + DOWN * 3.4)

        courbe2 = axes2.plot(lambda x: np.sin(2 * x), x_range=[-3.4, 3.4], color="#1E90FF")
        schema2 = VGroup(axes2, courbe2)

        with self.voiceover(
            text=(
                "On trace d'abord la portion sur zéro, pi sur deux, puis on "
                "complète par symétrie centrale pour l'imparité, et enfin "
                "par translations successives de pi grâce à la "
                "périodicité, pour obtenir la courbe complète sur ℝ."
            )
        ) as tracker:
            self.play(FadeIn(schema2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema2))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Irrationnelle : Df par u(x) ≥ 0, (√u)' = u'/(2√u), "
                    "pas dérivable où u s'annule (demi-tangente verticale). "
                    "Trigonométrique : période d'abord, puis parité, puis "
                    "dérivée sur le domaine réduit, puis tracé par "
                    "symétrie/translations.",
                    width=58,
                ),
                font_size=21,
            ),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : pour une fonction irrationnelle, le domaine "
                "vient de u de x positif ou nul, la dérivée est u prime "
                "sur deux racine de u, et f n'est pas dérivable là où u "
                "s'annule. Pour une fonction trigonométrique, on cherche "
                "toujours la période en premier, puis la parité, puis la "
                "dérivée sur le domaine ainsi réduit, avant de compléter "
                "le tracé par symétries et translations."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : oublier de vérifier la dérivabilité aux bornes "
                    "du domaine d'une racine, ou étudier la dérivée d'une "
                    "fonction trigonométrique AVANT d'avoir réduit le "
                    "domaine par période et parité — travail inutilement "
                    "long et source d'erreurs.",
                    width=58,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Piège à éviter : oublier de vérifier la dérivabilité aux "
                "bornes du domaine d'une racine carrée, ou étudier la "
                "dérivée d'une fonction trigonométrique avant même d'avoir "
                "réduit le domaine par la période et la parité — un travail "
                "inutilement long, et souvent source d'erreurs de signe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
