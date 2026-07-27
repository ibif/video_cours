"""
scenes/Maths_LimitesContinuite_09.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 09.

Limites trigonométriques de référence : lim sin(x)/x = 1 en 0, avec
démonstration par comparaison d'aires sur le cercle trigonométrique.
Conséquences tan(x)/x → 1 et (1-cos x)/x² → 1/2. Exemples résolus 12, 13,
méthode générale sin(ax)/(bx) → a/b.
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Sector,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, theorem_box


class LimitesTrigonometriquesDeReference(NotionScene):
    def construct(self):
        titre = scene_title("Limites trigonométriques de référence")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème sin(x)/x → 1 --------------------------------------
        theo_sin = theorem_box(
            MathTex(r"\lim_{x\to 0} \dfrac{\sin x}{x} = 1", font_size=34),
            box_width=6.5,
        )
        theo_sin.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Théorème fondamental : la limite, quand x tend vers zéro, "
                "de sinus de x sur x, vaut un. C'est la limite "
                "trigonométrique de référence, à partir de laquelle on "
                "retrouve toutes les autres."
            )
        ) as tracker:
            self.play(FadeIn(theo_sin))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_sin))

        # --- Démonstration : comparaison d'aires sur le cercle trigonométrique --
        demo_titre = Text(
            "Démonstration — comparaison d'aires (0 < x < π/2) :",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        demo_titre.next_to(titre, DOWN, buff=0.35)

        # Figure géométrique : triangle OAM ⊂ secteur OAM ⊂ triangle OAT
        R = 2.2
        x_angle = 0.85  # angle en radians pour l'illustration
        import math

        O = ORIGIN
        A = RIGHT * R
        M = R * (math.cos(x_angle) * RIGHT + math.sin(x_angle) * UP)
        T = R * RIGHT + (R * math.tan(x_angle)) * UP

        cercle = Circle(radius=R, color=WHITE, stroke_width=1.5)
        tri_oam = Polygon(O, A, M, color="#B42E41", fill_color="#B42E41", fill_opacity=0.5, stroke_width=1)
        secteur = Sector(radius=R, angle=x_angle, start_angle=0, color="#DE7C1F", fill_opacity=0.35, stroke_width=1)
        tri_oat = Polygon(O, A, T, color="#288073", fill_opacity=0.0, stroke_width=2)
        segment_tangente = Line(A, T, color="#288073", stroke_width=3)
        segment_OM = Line(O, M, color=WHITE, stroke_width=1.5)
        segment_OT = Line(O, T, color=WHITE, stroke_width=1)
        pts = VGroup(
            Dot(O, radius=0.05, color=WHITE), Dot(A, radius=0.05, color=WHITE),
            Dot(M, radius=0.05, color=WHITE), Dot(T, radius=0.05, color=WHITE),
        )
        labels = VGroup(
            MathTex("O", font_size=22).next_to(O, DOWN + LEFT, buff=0.1),
            MathTex("A", font_size=22).next_to(A, DOWN, buff=0.12),
            MathTex("M", font_size=22, color="#B42E41").next_to(M, UP, buff=0.1),
            MathTex("T", font_size=22, color="#288073").next_to(T, RIGHT, buff=0.1),
            MathTex("x", font_size=20).move_to(O + 0.55 * (math.cos(x_angle / 2) * RIGHT + math.sin(x_angle / 2) * UP)),
        )
        figure = VGroup(cercle, secteur, tri_oam, tri_oat, segment_tangente, segment_OM, segment_OT, pts, labels)
        figure.scale(0.75)
        figure.next_to(demo_titre, DOWN, buff=0.25).shift(LEFT * 2.6)

        aires = MathTex(
            r"""
            \begin{array}{l}
            \mathcal{A}(OAM) = \dfrac{1}{2}\sin x\\[4pt]
            \mathcal{A}(\text{secteur } OAM) = \dfrac{1}{2}x\\[4pt]
            \mathcal{A}(OAT) = \dfrac{1}{2}\tan x
            \end{array}
            """,
            font_size=24,
        )
        aires.next_to(figure, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Plaçons-nous sur le cercle trigonométrique de rayon un, "
                "avec un angle x compris entre zéro et pi sur deux. Le "
                "triangle O-A-M, en rouge, est inclus dans le secteur "
                "circulaire O-A-M, en orange, lui-même inclus dans le "
                "triangle O-A-T, en vert, où T est le point de la tangente "
                "en A. Leurs aires respectives valent un demi sinus de x, "
                "un demi x, et un demi tangente de x."
            )
        ) as tracker:
            self.play(FadeIn(demo_titre))
            self.play(FadeIn(figure))
            self.play(Write(aires))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_titre), FadeOut(figure), FadeOut(aires))

        inegalites = MathTex(
            r"""
            \begin{array}{l}
            \dfrac{1}{2}\sin x \leq \dfrac{1}{2} x \leq \dfrac{1}{2}\tan x
            \ \Longrightarrow\ \sin x \leq x \leq \tan x\\[6pt]
            \text{On divise par } \sin x>0 :
            \quad 1 \leq \dfrac{x}{\sin x} \leq \dfrac{1}{\cos x}
            \ \Longrightarrow\ \cos x \leq \dfrac{\sin x}{x} \leq 1
            \end{array}
            """,
            font_size=26,
        )
        inegalites_box = theorem_box(inegalites, box_width=11.5)
        inegalites_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'inclusion des aires donne sinus de x inférieur ou égal à "
                "x, lui-même inférieur ou égal à tangente de x. En "
                "divisant par sinus de x, strictement positif, on obtient "
                "cosinus de x, inférieur ou égal à sinus de x sur x, "
                "lui-même inférieur ou égal à un. Or cosinus de x tend vers "
                "un quand x tend vers zéro : par le théorème des gendarmes, "
                "sinus de x sur x tend donc vers un."
            )
        ) as tracker:
            self.play(FadeIn(inegalites_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(inegalites_box))

        # --- Conséquences : tan(x)/x et (1-cos x)/x² -----------------------------
        consequences = theorem_box(
            MathTex(
                r"""
                \begin{array}{l}
                \lim_{x\to 0} \dfrac{\tan x}{x} = 1
                \quad \left(\text{car } \dfrac{\tan x}{x} = \dfrac{\sin x}{x}\times\dfrac{1}{\cos x}\right)\\[8pt]
                \lim_{x\to 0} \dfrac{1-\cos x}{x^2} = \dfrac{1}{2}
                \quad \left(\text{car } \dfrac{1-\cos x}{x^2} = \dfrac{1-\cos^2 x}{x^2(1+\cos x)}
                = \left(\dfrac{\sin x}{x}\right)^2\!\dfrac{1}{1+\cos x}\right)
                \end{array}
                """,
                font_size=22,
            ),
            box_width=12.0,
        )
        consequences.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux conséquences directes. La limite de tangente de x sur "
                "x, en zéro, vaut un, car tangente de x sur x s'écrit "
                "comme le produit de sinus de x sur x, et de un sur "
                "cosinus de x. La limite de un moins cosinus de x, sur x "
                "carré, en zéro, vaut un demi : on multiplie par la "
                "quantité conjuguée un plus cosinus de x, puis on utilise "
                "sinus carré plus cosinus carré égale un, pour faire "
                "réapparaître sinus de x sur x au carré."
            )
        ) as tracker:
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequences))

        # --- Exemples 12 et 13 : sin(3x)/x et sin(5x)/sin(2x) --------------------
        ex12_titre = Text("Exemple 12 — lim sin(3x)/x en x0 = 0 :", font_size=22, color=YELLOW, weight="BOLD")
        ex12_titre.next_to(titre, DOWN, buff=0.35)
        ex12_calc = MathTex(
            r"\dfrac{\sin(3x)}{x} = 3\times\dfrac{\sin(3x)}{3x}"
            r"\ \underset{x\to 0}{\longrightarrow}\ 3\times 1 = 3",
            font_size=26,
        )
        ex12_calc.next_to(ex12_titre, DOWN, buff=0.35)
        ex12_box = example_box(ex12_calc, box_width=9.5)
        ex12_box.next_to(ex12_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : sinus de trois x, sur x, en zéro. On fait "
                "apparaître sinus de trois x sur trois x, en multipliant "
                "par trois : ce quotient tend vers un, donc la limite "
                "cherchée vaut trois."
            )
        ) as tracker:
            self.play(FadeIn(ex12_titre))
            self.play(FadeIn(ex12_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex12_titre), FadeOut(ex12_box))

        ex13_titre = Text("Exemple 13 — lim sin(5x)/sin(2x) en x0 = 0 :", font_size=21, color=YELLOW, weight="BOLD")
        ex13_titre.next_to(titre, DOWN, buff=0.35)
        ex13_calc = MathTex(
            r"""
            \dfrac{\sin(5x)}{\sin(2x)} =
            \dfrac{\sin(5x)}{5x}\times\dfrac{2x}{\sin(2x)}\times\dfrac{5x}{2x}
            \ \underset{x\to 0}{\longrightarrow}\ 1\times 1\times \dfrac{5}{2} = \dfrac{5}{2}
            """,
            font_size=23,
        )
        ex13_calc.next_to(ex13_titre, DOWN, buff=0.35)
        ex13_box = example_box(ex13_calc, box_width=11.5)
        ex13_box.next_to(ex13_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : sinus de cinq x, sur sinus de deux x, en zéro. "
                "On fait apparaître les deux quotients de référence, sinus "
                "de cinq x sur cinq x, et deux x sur sinus de deux x, qui "
                "tendent chacun vers un ; il reste alors cinq x sur deux x, "
                "qui donne cinq demis. La méthode générale : sinus de a x "
                "sur b x tend vers a sur b, en zéro."
            )
        ) as tracker:
            self.play(FadeIn(ex13_titre))
            self.play(FadeIn(ex13_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex13_titre), FadeOut(ex13_box))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            MathTex(
                r"\lim_{x\to 0}\dfrac{\sin x}{x}=1 \qquad "
                r"\lim_{x\to 0}\dfrac{\tan x}{x}=1 \qquad "
                r"\lim_{x\to 0}\dfrac{1-\cos x}{x^2}=\dfrac{1}{2} \qquad "
                r"\lim_{x\to 0} \dfrac{\sin(ax)}{bx} = \dfrac{a}{b}",
                font_size=20,
            ),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : ces trois limites trigonométriques de "
                "référence, ainsi que la méthode générale sinus de a x sur "
                "b x qui tend vers a sur b, doivent être connues par cœur "
                "pour traiter rapidement tous les calculs de ce type."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
