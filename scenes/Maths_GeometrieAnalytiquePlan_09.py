"""
scenes/Maths_GeometrieAnalytiquePlan_09.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 09.

§ Équation d'un cercle : théorème centre Ω(a;b), rayon r : (x-a)²+(y-b)²=r²
avec démonstration (définition par distance), forme développée
x²+y²+ux+vy+w=0. Méthode de complétion des carrés, discussion R>0 (cercle)
/ R=0 (point) / R<0 (ensemble vide). Cercle de diamètre [AB] : MA⃗·MB⃗=0.
Exemple résolu : x²+y²-4x+6y-12=0 → cercle centre Ω(2;-3), rayon 5.
Source : 1ereC/Maths.pdf, chapitre 14, pages 172-173.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, Circle, Create, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EquationCercle(NotionScene):
    def construct(self):
        titre = scene_title("Équation d'un cercle")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : théorème + démonstration ------------------------------------
        axes = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1], x_length=3.6, y_length=3.6,
            axis_config={"include_tip": False, "color": WHITE},
        ).move_to(LEFT * 3.6 + DOWN * 0.5)
        cercle_schema = Circle(radius=1.4, color="#1E5FA8").move_to(axes.get_center())
        centre = Dot(axes.get_center(), color="#DE7C1F")
        label_omega = MathTex(r"\Omega", font_size=24).next_to(centre, DOWN, buff=0.1)
        m_pt = axes.get_center() + [1.4 * 0.7, 1.4 * 0.7, 0]
        dot_m = Dot(m_pt, color=YELLOW)
        label_m = MathTex("M", font_size=22).next_to(dot_m, UP, buff=0.08)
        schema = VGroup(axes, cercle_schema, centre, label_omega, dot_m, label_m)

        theoreme = theorem_box(
            VGroup(
                MathTex(
                    r"\mathcal{C}(\Omega,r):\ \Omega(a;b),\ r>0",
                    font_size=25,
                ),
                MathTex(
                    r"M(x;y)\in\mathcal{C} \iff \Omega M = r \iff (x-a)^2+(y-b)^2=r^2",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=6.6,
        )
        theoreme.move_to(RIGHT * 3.2 + DOWN * 0.5)

        with self.voiceover(
            text=(
                "Un cercle de centre oméga, de coordonnées a et b, et de "
                "rayon r strictement positif, est l'ensemble des points M "
                "tels que la distance oméga-M soit égale à r. Puisque "
                "oméga-M égale racine de x moins a, au carré, plus y moins "
                "b, au carré, en élevant au carré, on obtient l'équation du "
                "cercle : x moins a, au carré, plus y moins b, au carré, "
                "égale r au carré."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(theoreme))

        forme_dev = definition_box(
            MathTex(
                r"(x-a)^2+(y-b)^2=r^2 \ \Longrightarrow\ x^2+y^2 \underbrace{-2a}_{u}x \underbrace{-2b}_{v}y "
                r"+\underbrace{(a^2+b^2-r^2)}_{w} = 0",
                font_size=23,
            ),
            box_width=11.4,
        )
        forme_dev.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En développant cette équation, on obtient une forme "
                "générale x carré plus y carré, plus u x, plus v y, plus w "
                "égale zéro, avec u égale moins 2a, v égale moins 2b, et w "
                "égale a carré plus b carré moins r carré."
            )
        ) as tracker:
            self.play(FadeIn(forme_dev))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(forme_dev))

        # --- Raisonnement : méthode de complétion des carrés ----------------------
        methode = method_box(
            VGroup(
                Text("Reconnaître x²+y²+ux+vy+w=0 : compléter les carrés", font_size=21, weight="BOLD"),
                MathTex(
                    r"x^2+ux = \left(x+\dfrac{u}{2}\right)^2-\dfrac{u^2}{4}"
                    r"\qquad y^2+vy = \left(y+\dfrac{v}{2}\right)^2-\dfrac{v^2}{4}",
                    font_size=22,
                ),
                MathTex(
                    r"\Rightarrow\ \left(x+\dfrac{u}{2}\right)^2 + \left(y+\dfrac{v}{2}\right)^2 = "
                    r"\underbrace{\dfrac{u^2+v^2}{4}-w}_{R}",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.2,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour reconnaître la nature de l'ensemble défini par x "
                "carré plus y carré plus u x plus v y plus w égale zéro, on "
                "complète le carré en x et le carré en y : x carré plus u x "
                "s'écrit x plus u sur 2, au carré, moins u carré sur 4, et "
                "de même pour y. On obtient alors x plus u sur 2, au carré, "
                "plus y plus v sur 2, au carré, égale un nombre R, qu'on "
                "appelle parfois le réalisant."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        discussion = definition_box(
            VGroup(
                MathTex(r"R = \dfrac{u^2+v^2}{4}-w", font_size=26),
                MathTex(
                    r"R>0 \Rightarrow \text{cercle de centre } \Omega\!\left(-\dfrac{u}{2};-\dfrac{v}{2}\right),\ "
                    r"\text{rayon } \sqrt{R}",
                    font_size=22,
                ),
                MathTex(r"R=0 \Rightarrow \{\Omega\} \ (\text{un seul point})", font_size=23),
                MathTex(r"R<0 \Rightarrow \varnothing \ (\text{ensemble vide})", font_size=23),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        discussion.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Trois cas se présentent alors, selon le signe de R. Si R "
                "est strictement positif, on a bien un cercle, de centre "
                "oméga moins u sur 2, moins v sur 2, et de rayon racine de "
                "R. Si R est nul, l'ensemble se réduit à un seul point, le "
                "centre oméga. Et si R est strictement négatif, l'ensemble "
                "est vide : aucun point ne vérifie l'équation."
            )
        ) as tracker:
            self.play(FadeIn(discussion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(discussion))

        # --- Cercle de diamètre [AB] ---------------------------------------------
        diametre = theorem_box(
            VGroup(
                Text("Cercle de diamètre [AB]", font_size=22, weight="BOLD"),
                MathTex(
                    r"M \in \mathcal{C}_{[AB]} \iff \overrightarrow{MA}\cdot\overrightarrow{MB} = 0"
                    r"\quad (\text{angle droit en } M)",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        diametre.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Cas particulier utile : le cercle de diamètre A-B est "
                "l'ensemble des points M tels que le produit scalaire de "
                "M-A et M-B soit nul, ce qui traduit simplement le fait que "
                "l'angle en M du triangle A-M-B est droit — c'est le "
                "théorème de l'angle inscrit dans un demi-cercle."
            )
        ) as tracker:
            self.play(FadeIn(diametre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(diametre))

        # --- Exemple traité ---------------------------------------------------
        exemple = example_box(
            MathTex(
                r"x^2+y^2-4x+6y-12=0"
                r"\\[5pt]"
                r"(x^2-4x)+(y^2+6y)-12=0"
                r"\\[4pt]"
                r"(x-2)^2-4+(y+3)^2-9-12=0"
                r"\\[4pt]"
                r"(x-2)^2+(y+3)^2 = 25 = 5^2"
                r"\\[4pt]"
                r"\Rightarrow\ \text{cercle } \Omega(2;-3),\ r=5",
                font_size=23,
            ),
            box_width=6.6,
        )
        cercle_ex = Circle(radius=1.5, color="#1E5FA8")
        centre_ex = Dot(cercle_ex.get_center(), color="#DE7C1F")
        label_ex = MathTex(r"\Omega(2;-3)", font_size=20).next_to(centre_ex, DOWN, buff=0.15)
        figure_ex = VGroup(cercle_ex, centre_ex, label_ex)
        figure_ex.move_to(LEFT * 3.4 + DOWN * 0.3)
        exemple.move_to(RIGHT * 3.2 + DOWN * 0.3)

        with self.voiceover(
            text=(
                "Exemple : reconnaissons l'ensemble x carré plus y carré "
                "moins 4x plus 6y moins 12 égale zéro. On regroupe les "
                "termes en x et en y, puis on complète les carrés : x moins "
                "2, au carré, moins 4, plus y plus 3, au carré, moins 9, "
                "moins 12 égale zéro. On obtient x moins 2, au carré, plus "
                "y plus 3, au carré, égale 25, soit 5 au carré. C'est donc "
                "le cercle de centre oméga, 2, moins 3, et de rayon 5."
            )
        ) as tracker:
            self.play(Create(figure_ex))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure_ex), FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(r"\mathcal{C}(\Omega,r):\ (x-a)^2+(y-b)^2=r^2", font_size=27),
                Text("R>0 : cercle    R=0 : point    R<0 : ensemble vide", font_size=21),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : l'équation d'un cercle de centre oméga a, b et "
                "de rayon r s'écrit x moins a au carré plus y moins b au "
                "carré égale r au carré. Face à x carré plus y carré plus u "
                "x plus v y plus w égale zéro, on complète toujours les "
                "carrés avant de conclure."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "x²+y²+ux+vy+w=0 n'est PAS toujours un cercle : il faut "
                    "impérativement calculer R et vérifier R>0 avant de "
                    "parler de centre et de rayon — sinon on décrit un "
                    "point isolé, ou rien du tout.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter absolument : une équation de la forme x "
                "carré plus y carré plus u x plus v y plus w égale zéro "
                "n'est pas toujours un cercle. Il faut impérativement "
                "calculer R et vérifier qu'il est strictement positif avant "
                "de parler de centre et de rayon, sous peine de décrire en "
                "réalité un point isolé, ou même rien du tout."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
