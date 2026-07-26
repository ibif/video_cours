"""
scenes/Maths_GeneralitesFonctions_10.py — Chapitre 3 (1ereC, Maths), scène 10.

Fonction réciproque : méthode pratique pour la déterminer, symétrie des
courbes de f et f⁻¹ par rapport à la droite y = x, exemple traité.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ReciproqueMethodeExemple(NotionScene):
    def construct(self):
        titre = scene_title("Fonction réciproque : méthode et exemple")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : méthode pratique -----------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Pour déterminer f⁻¹ lorsque f est bijective de Df sur "
                    "F : 1) poser y = f(x) ; 2) résoudre cette équation "
                    "d'inconnue x, pour exprimer x en fonction de y ; "
                    "3) le résultat obtenu, en renommant y en x, donne "
                    "f⁻¹(x).",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode pratique pour déterminer f moins un, lorsque f "
                "est bijective de Df sur F : d'abord, on pose y égale f de "
                "x. Ensuite, on résout cette équation d'inconnue x, pour "
                "exprimer x en fonction de y. Enfin, en renommant y en x "
                "dans le résultat obtenu, on obtient l'expression de f "
                "moins un de x."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Animation du raisonnement : symétrie des courbes ------------------
        theo_symetrie = theorem_box(
            Text(
                _wrap(
                    "Les courbes de f et de f⁻¹, dans un repère "
                    "orthonormé, sont symétriques par rapport à la droite "
                    "d'équation y = x.",
                    width=52,
                ),
                font_size=23,
            ),
            box_width=8.6,
        )
        theo_symetrie.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Autre résultat important : dans un repère orthonormé, "
                "les courbes de f et de f moins un sont symétriques par "
                "rapport à la droite d'équation y égale x, la première "
                "bissectrice."
            )
        ) as tracker:
            self.play(FadeIn(theo_symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_symetrie))

        demo_symetrie = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                M(a\,;b) \in \mathcal{C}_f \ \Longleftrightarrow \ b = f(a) \ \Longleftrightarrow \ a = f^{-1}(b) \ \Longleftrightarrow \ M'(b\,;a) \in \mathcal{C}_{f^{-1}} \\
                \text{Or } M(a\,;b) \text{ et } M'(b\,;a) \text{ sont toujours symétriques par rapport à } (y=x)
                \end{array}
                """,
                font_size=22,
            ),
            box_width=11.4,
        )
        demo_symetrie.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Démonstration rapide : le point M de coordonnées a et b "
                "appartient à la courbe de f exactement quand b égale f de "
                "a, ce qui équivaut à a égale f moins un de b, c'est-à-"
                "dire exactement quand le point M prime de coordonnées b "
                "et a appartient à la courbe de f moins un. Or M et M "
                "prime, dont on a échangé les coordonnées, sont toujours "
                "symétriques par rapport à la droite y égale x."
            )
        ) as tracker:
            self.play(FadeIn(demo_symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_symetrie))

        # --- Exemple traité 11 -------------------------------------------------
        enonce_ex11a = Text(
            "Exemple 11a — f(x) = 3x − 1, bijection de ℝ sur ℝ",
            font_size=23,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex11a.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple 11 : soit f de x égale trois x moins un, "
                "bijection de ℝ sur ℝ. Déterminons f moins un."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex11a))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex11a))

        calcul_ex11a = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                y = 3x-1 \ \Longleftrightarrow \ x = \dfrac{y+1}{3} \ \Longrightarrow \ f^{-1}(x) = \dfrac{x+1}{3} \\
                \text{Vérification : } f\big(f^{-1}(x)\big) = 3 \cdot \dfrac{x+1}{3}-1 = x+1-1 = x \ \checkmark
                \end{array}
                """,
                font_size=25,
            ),
            box_width=9.7,
        )
        calcul_ex11a.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On pose y égale trois x moins un, on résout en x : x "
                "égale y plus un, le tout sur trois. Donc f moins un de x "
                "égale x plus un, sur trois. Vérifions : f de f moins un "
                "de x égale trois fois x plus un sur trois, moins un, soit "
                "x plus un moins un, c'est-à-dire x. La vérification "
                "fonctionne."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex11a))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex11a))

        enonce_ex11b = Text(
            "Exemple 11b — g(x) = x², bijection de [0;+∞[ sur [0;+∞[",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex11b.next_to(titre, DOWN, buff=0.5)

        calcul_ex11b = MathTex(
            r"y = x^2, \ x \geq 0 \ \Longleftrightarrow \ x = \sqrt{y} "
            r"\ \Longrightarrow \ g^{-1}(x) = \sqrt{x}",
            font_size=27,
        )
        calcul_ex11b.next_to(enonce_ex11b, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième cas : g de x égale x carré, bijection de zéro, "
                "plus l'infini, sur zéro, plus l'infini. On pose y égale x "
                "carré, avec x positif ou nul, ce qui donne x égale "
                "racine carrée de y. Donc g moins un de x égale racine "
                "carrée de x."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex11b))
            self.play(Write(calcul_ex11b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex11b), FadeOut(calcul_ex11b))

        # --- Figure : symétrie des courbes ---------------------------------
        axes = Axes(
            x_range=[-0.5, 3, 1],
            y_range=[-0.5, 3, 1],
            x_length=5.5,
            y_length=5.0,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(titre.get_center() + DOWN * 3.1)
        courbe_g = axes.plot(lambda x: x**2, x_range=[0, 1.73], color=YELLOW)
        courbe_ginv = axes.plot(lambda x: x**0.5, x_range=[0, 3], color="#59B4FF")
        droite_yx = DashedLine(axes.c2p(0, 0), axes.c2p(3, 3), color=WHITE, stroke_width=1.5)
        label_g = MathTex("g", font_size=24, color=YELLOW).next_to(axes.c2p(1.2, 1.44), UP, buff=0.1)
        label_ginv = MathTex("g^{-1}", font_size=24, color="#59B4FF").next_to(axes.c2p(2.2, 1.48), RIGHT, buff=0.1)
        schema = VGroup(axes, courbe_g, courbe_ginv, droite_yx, label_g, label_ginv)

        with self.voiceover(
            text=(
                "Sur cette figure, la courbe de g, en jaune, et celle de g "
                "moins un, en bleu, sont bien symétriques par rapport à la "
                "droite pointillée y égale x."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Méthode : poser y = f(x), résoudre en x, renommer. "
                    "Les courbes de f et f⁻¹ sont toujours symétriques par "
                    "rapport à la droite y = x.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : pour trouver f moins un, on pose y égale f de "
                "x, on résout en x, puis on renomme. Et géométriquement, "
                "les courbes de f et de f moins un sont toujours "
                "symétriques par rapport à la droite y égale x."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : si l'équation y = f(x) a plusieurs solutions "
                    "en x (par exemple avec un ±√), c'est que f n'est pas "
                    "bijective sur l'intervalle considéré — revoir le "
                    "domaine de départ.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : si, en résolvant y égale f de x, on trouve "
                "plusieurs solutions en x — par exemple avec un plus ou "
                "moins racine carrée — c'est que f n'est pas bijective sur "
                "l'intervalle considéré. Il faut alors revoir le domaine "
                "de départ avant de continuer."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
