"""
scenes/Maths_EtudeGraphiqueFonctions_09.py — Chapitre 11 (1ereC, Maths), scène 09.

Intersections de courbes (méthode f(x) = g(x)), intersection courbe /
asymptote (jamais la verticale), lectures graphiques (image, résolution
graphique f(x) = k, f(x) ≥ k, f(x) = g(x), signe de f), corollaire du
théorème des valeurs intermédiaires (unicité de solution).
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class IntersectionsLecturesGraphiques(NotionScene):
    def construct(self):
        titre = scene_title("Intersections de courbes et lectures graphiques")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Étape 7 (suite) : exploiter la courbe une fois tracée",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fois la courbe tracée, on peut l'exploiter : trouver "
                "les points d'intersection avec une autre courbe, ou lire "
                "directement des informations sur le graphique, sans "
                "calcul supplémentaire."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Méthode intersection de deux courbes ---------------------------
        methode_intersection = method_box(
            MathTex(
                r"M(x\,;y) \in C_f \cap C_g \ \Longleftrightarrow \ "
                r"f(x)=g(x) \ \text{ et } \ y=f(x)",
                font_size=27,
            ),
            box_width=10.5,
        )
        methode_intersection.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode : un point M de coordonnées x et y appartient à "
                "l'intersection de Cf et de Cg si et seulement si f de x "
                "égale g de x, et y égale f de x. On résout donc d'abord "
                "l'équation f de x égale g de x, puis on calcule l'image "
                "pour chaque solution trouvée."
            )
        ) as tracker:
            self.play(FadeIn(methode_intersection))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_intersection))

        # --- Intersection courbe / asymptote ---------------------------------
        theo_asymptote = theorem_box(
            Text(
                _wrap(
                    "Intersection Cf ∩ asymptote : même méthode f(x) = "
                    "équation de l'asymptote — SAUF pour l'asymptote "
                    "verticale, que la courbe ne coupe jamais (f n'y est "
                    "pas définie).",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        theo_asymptote.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'intersection de la courbe avec une asymptote se traite "
                "avec la même méthode : on résout f de x égale l'équation "
                "de l'asymptote. Mais attention, ceci ne s'applique jamais "
                "à l'asymptote verticale, que la courbe ne peut pas couper, "
                "puisque f n'y est justement pas définie."
            )
        ) as tracker:
            self.play(FadeIn(theo_asymptote))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_asymptote))

        # --- Exemple : intersection de deux courbes -----------------------
        enonce_ex1 = Text(
            "Exemple — intersection de f(x) = x² et g(x) = x + 2",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : cherchons les points d'intersection entre f de "
                "x égale x carré, et g de x égale x plus deux."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex1))

        calcul_ex1 = example_box(
            MathTex(
                r"""
                x^2=x+2 \ \Longleftrightarrow \ x^2-x-2=0
                \ \Longleftrightarrow \ x=-1 \text{ ou } x=2 \\
                \Longrightarrow \ A(-1\,;1) \text{ et } B(2\,;4)
                """,
                font_size=27,
            ),
            box_width=9.5,
        )
        calcul_ex1.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On résout x carré égale x plus deux, soit x carré moins x "
                "moins deux égale zéro, qui a pour solutions x égale moins "
                "un et x égale deux. Les points d'intersection sont donc A "
                "de coordonnées moins un, un, et B de coordonnées deux, "
                "quatre."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex1))

        axes = Axes(
            x_range=[-3, 4, 1], y_range=[-1, 6, 2], x_length=6.5, y_length=4.0,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(titre.get_center() + DOWN * 3.3)
        courbe_f = axes.plot(lambda x: x**2, x_range=[-2.5, 2.5], color="#1E90FF")
        droite_g = axes.plot(lambda x: x + 2, x_range=[-3, 4], color="#DE7C1F")
        pt_A = Dot(axes.c2p(-1, 1), color=YELLOW)
        pt_B = Dot(axes.c2p(2, 4), color=YELLOW)
        schema = VGroup(axes, courbe_f, droite_g, pt_A, pt_B)

        with self.voiceover(
            text=(
                "Sur le graphique, ces deux points correspondent bien aux "
                "endroits où la parabole et la droite se croisent."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Lectures graphiques ----------------------------------------------
        lectures = example_box(
            MathTex(
                r"""
                \begin{array}{ll}
                \text{Lire } f(a) & \text{abscisse } a \to \text{ordonnée du point de } C_f \\
                \text{Résoudre } f(x)=k & \text{abscisses des points de } C_f \text{ à hauteur } y=k \\
                \text{Résoudre } f(x)\geq k & \text{abscisses où } C_f \text{ est au-dessus de } y=k \\
                \text{Signe de } f(x) & \text{position de } C_f \text{ par rapport à } (Ox)
                \end{array}
                """,
                font_size=21,
            ),
            box_width=11.6,
        )
        lectures.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fois la courbe disponible, on peut tout lire "
                "graphiquement, sans nouveau calcul. Pour lire f de a : on "
                "part de l'abscisse a et on remonte jusqu'à la courbe. Pour "
                "résoudre f de x égale k : on cherche les abscisses des "
                "points de la courbe situés à la hauteur y égale k. Pour f "
                "de x supérieur ou égal à k : on repère où la courbe est "
                "au-dessus de cette hauteur. Et pour le signe de f : on "
                "regarde si la courbe est au-dessus ou en dessous de l'axe "
                "des abscisses."
            )
        ) as tracker:
            self.play(FadeIn(lectures))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(lectures))

        # --- Corollaire TVI ---------------------------------------------------
        theo_tvi = theorem_box(
            Text(
                _wrap(
                    "Corollaire du TVI : si f est continue et strictement "
                    "monotone sur I, alors pour tout k, l'équation f(x) = k "
                    "a AU PLUS une solution dans I (une seule si k est "
                    "atteint).",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        theo_tvi.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un dernier théorème très utile, corollaire du théorème "
                "des valeurs intermédiaires : si f est continue et "
                "strictement monotone sur un intervalle I, alors pour tout "
                "réel k appartenant à l'intervalle image, l'équation f de x "
                "égale k admet une unique solution dans I. Cela justifie "
                "qu'une lecture graphique donne bien une réponse unique sur "
                "chaque branche monotone."
            )
        ) as tracker:
            self.play(FadeIn(theo_tvi))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_tvi))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Intersection Cf∩Cg : résoudre f(x) = g(x). Jamais "
                    "d'intersection avec l'asymptote verticale. Lectures "
                    "graphiques : projeter sur les axes. Sur un intervalle "
                    "de monotonie stricte, f(x) = k a au plus une solution.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : pour toute intersection de courbes, on résout "
                "f de x égale g de x. On ne coupe jamais l'asymptote "
                "verticale. Les lectures graphiques se ramènent toujours à "
                "une projection sur les axes. Et sur un intervalle de "
                "monotonie stricte, l'équation f de x égale k a au plus "
                "une solution."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : sur un intervalle où f n'est PAS monotone, une "
                    "lecture graphique f(x) = k peut donner plusieurs "
                    "solutions — toujours vérifier le tableau de variation "
                    "avant de conclure à l'unicité.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Piège à éviter : sur un intervalle où f n'est pas "
                "monotone, une lecture graphique f de x égale k peut très "
                "bien donner plusieurs solutions. Il faut toujours "
                "vérifier le tableau de variation avant de conclure "
                "hâtivement à l'unicité d'une solution."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
