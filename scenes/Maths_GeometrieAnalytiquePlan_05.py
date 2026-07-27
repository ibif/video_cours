"""
scenes/Maths_GeometrieAnalytiquePlan_05.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 05.

§ Équation cartésienne d'une droite définie par un point et un vecteur
directeur. Définition du vecteur directeur. Théorème : équation
β(x-xA)-α(y-yA)=0, avec démonstration, forme ax+by+c=0. Théorème
réciproque : l'ensemble des points vérifiant ax+by+c=0 (avec (a;b)≠(0;0))
est une droite de vecteur directeur u(-b;a), avec démonstration. Moyen
mnémotechnique.
Source : 1ereC/Maths.pdf, chapitre 14, pages 168-169.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, Create, Dot, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EquationCartesienneDroite(NotionScene):
    def construct(self):
        titre = scene_title("Équation cartésienne d'une droite")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé : vecteur directeur -------------------------------------------
        a_pt = LEFT * 3 + DOWN * 0.5
        u_end = a_pt + RIGHT * 2 + UP * 1.2
        droite = Line(a_pt + LEFT * 1.5 + DOWN * 0.9, a_pt + RIGHT * 3.5 + UP * 2.1, color=WHITE)
        vecteur_u = Arrow(a_pt, u_end, buff=0, color=YELLOW, stroke_width=4)
        pa = VGroup(Dot(a_pt, color="#DE7C1F"), MathTex("A", font_size=26).next_to(a_pt, DOWN, buff=0.15))
        label_u = MathTex(r"\vec{u}", font_size=28, color=YELLOW).next_to(vecteur_u, UP, buff=0.1)
        label_d = MathTex("(D)", font_size=26).next_to(droite.get_end(), UP, buff=0.1)
        schema = VGroup(droite, vecteur_u, pa, label_u, label_d)
        schema.move_to(LEFT * 3.2 + DOWN * 0.2)

        definition = definition_box(
            VGroup(
                Text("Vecteur directeur", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "Un vecteur non nul u est un vecteur directeur de "
                        "(D) si (D) est la droite passant par A et de "
                        "direction u : M∈(D) ⟺ AM⃗ et u colinéaires.",
                        width=40,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=6.6,
        )
        definition.move_to(RIGHT * 3.4 + DOWN * 0.2)

        with self.voiceover(
            text=(
                "Une droite (D) peut être définie par un point A et un "
                "vecteur non nul u, appelé vecteur directeur : (D) est "
                "alors l'ensemble des points M tels que le vecteur A-M "
                "soit colinéaire à u. Cherchons à traduire cette condition "
                "en une équation reliant x et y."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(definition))

        # --- Raisonnement : théorème + démonstration -----------------------------
        theoreme = theorem_box(
            VGroup(
                MathTex(
                    r"A(x_A;y_A),\ \vec{u}(\alpha;\beta) \ (\vec{u}\neq\vec{0})",
                    font_size=26,
                ),
                MathTex(
                    r"M(x;y) \in (D) \iff \beta(x-x_A) - \alpha(y-y_A) = 0",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.28),
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le théorème : si A a pour coordonnées x-A, y-A, et u "
                "pour coordonnées alpha, bêta, alors un point M de "
                "coordonnées x, y appartient à la droite (D) si et "
                "seulement si bêta fois x moins x-A, moins alpha fois y "
                "moins y-A, est égal à zéro. Démontrons ce résultat grâce "
                "au déterminant."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        demo = VGroup(
            MathTex(
                r"M \in (D) \iff \overrightarrow{AM} \text{ et } \vec{u} \text{ colinéaires}"
                r"\iff \det(\overrightarrow{AM},\vec{u}) = 0",
                font_size=25,
            ),
            MathTex(
                r"\overrightarrow{AM}(x-x_A\,;\,y-y_A)",
                font_size=25,
            ),
            MathTex(
                r"\det(\overrightarrow{AM},\vec{u}) = (x-x_A)\beta - \alpha(y-y_A)",
                font_size=25,
            ),
            MathTex(
                r"\Rightarrow\ M \in (D) \iff \beta(x-x_A)-\alpha(y-y_A) = 0",
                font_size=27,
                color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.3)
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "M appartient à (D) si et seulement si le vecteur A-M est "
                "colinéaire à u, c'est-à-dire si leur déterminant est nul. "
                "Le vecteur A-M a pour coordonnées x moins x-A, et y moins "
                "y-A. Le déterminant vaut alors x moins x-A, fois bêta, "
                "moins alpha fois y moins y-A. En annulant cette "
                "expression, on retrouve exactement l'équation annoncée."
            )
        ) as tracker:
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        forme_generale = definition_box(
            VGroup(
                MathTex(
                    r"\beta x - \alpha y + (\alpha y_A - \beta x_A) = 0",
                    font_size=27,
                ),
                MathTex(
                    r"\text{On pose } a=\beta,\ b=-\alpha,\ c=\alpha y_A-\beta x_A"
                    r"\ \Rightarrow\ ax+by+c=0",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        forme_generale.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En développant, on obtient bêta x moins alpha y, plus une "
                "constante, égale zéro. En posant a égale bêta, b égale "
                "moins alpha, et c cette constante, on retrouve la forme "
                "générale que vous connaissez : a x plus b y plus c égale "
                "zéro. Toute droite possède donc une équation cartésienne "
                "de cette forme."
            )
        ) as tracker:
            self.play(FadeIn(forme_generale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(forme_generale))

        # --- Théorème réciproque --------------------------------------------------
        reciproque = theorem_box(
            VGroup(
                Text("Réciproque", font_size=23, weight="BOLD"),
                MathTex(
                    r"(a;b)\neq(0;0) \ \Rightarrow\ \{M(x;y)\ /\ ax+by+c=0\} \text{ est une droite}",
                    font_size=25,
                ),
                MathTex(
                    r"\text{de vecteur directeur } \vec{u}(-b\,;\,a)",
                    font_size=26,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        reciproque.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Réciproquement, dès que a et b ne sont pas simultanément "
                "nuls, l'ensemble des points M vérifiant a x plus b y plus "
                "c égale zéro est une droite, et cette droite admet pour "
                "vecteur directeur le vecteur u de coordonnées moins b et "
                "a. On le vérifie en remarquant que a fois moins b, plus b "
                "fois a, vaut toujours zéro : ce vecteur convient "
                "systématiquement."
            )
        ) as tracker:
            self.play(FadeIn(reciproque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reciproque))

        # --- Exemple / moyen mnémotechnique ---------------------------------------
        mnemo = method_box(
            VGroup(
                Text("Moyen mnémotechnique", font_size=23, weight="BOLD"),
                MathTex(
                    r"(D):ax+by+c=0 \ \longrightarrow\ \vec{u}(-b\,;\,a)",
                    font_size=27,
                ),
                Text(
                    _wrap("« On échange les coefficients a et b, et on change un signe. »", width=44),
                    font_size=22,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=8.5,
        )
        mnemo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour lire directement un vecteur directeur sur une "
                "équation a x plus b y plus c égale zéro, retenez ce moyen "
                "mnémotechnique : on échange les coefficients a et b, et on "
                "change un seul des deux signes. On obtient ainsi "
                "immédiatement le vecteur directeur, moins b et a."
            )
        ) as tracker:
            self.play(FadeIn(mnemo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mnemo))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(r"(D): ax+by+c=0 \quad (a;b)\neq(0;0)", font_size=27),
                MathTex(r"\vec{u}(-b\,;\,a) \text{ est un vecteur directeur de } (D)", font_size=26),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : toute droite du plan a une équation "
                "cartésienne de la forme a x plus b y plus c égale zéro, "
                "avec a et b non simultanément nuls, et le vecteur moins b, "
                "a est toujours un vecteur directeur de cette droite."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Une équation cartésienne de droite n'est jamais unique "
                    "(on peut multiplier a, b, c par n'importe quel réel non "
                    "nul) : 2x+3y-1=0 et 4x+6y-2=0 représentent la MÊME "
                    "droite. Ne cherchez donc pas « l'» équation, mais UNE "
                    "équation.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à connaître : une équation cartésienne de droite "
                "n'est jamais unique. On peut multiplier a, b et c par "
                "n'importe quel réel non nul sans changer la droite "
                "représentée : 2x plus 3y moins 1 égale zéro, et 4x plus 6y "
                "moins 2 égale zéro, décrivent exactement la même droite. "
                "Ne cherchez donc jamais « l'» équation, mais « une » "
                "équation possible."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
