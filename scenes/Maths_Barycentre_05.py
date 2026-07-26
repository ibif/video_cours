"""
scenes/Maths_Barycentre_05.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 05.

§ Existence et unicité du barycentre de trois points pondérés (théorème
avec démonstration), définition du barycentre de trois points pondérés,
exemple résolu 4 (construction de G=bar{(A,3),(B,-2),(C,1)} par réduction
vectorielle).
Source : 1ereC/Maths.pdf, chapitre 4, page 44.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class ExistenceUniciteTroisPoints(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Existence et unicité (3 points)")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------
        question = Text(
            _wrap(
                "Le résultat vu pour deux points se généralise-t-il à "
                "trois points pondérés A-α, B-β, C-γ ?",
                width=52,
            ),
            font_size=26,
        )
        question.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Peut-on généraliser à trois points le résultat "
                "d'existence et d'unicité vu pour deux points ? Considérons "
                "trois points pondérés : A-alpha, B-bêta et C-gamma."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : théorème + démonstration -------------------------
        enonce_theoreme = VGroup(
            MathTex(r"\alpha+\beta+\gamma \neq 0", font_size=27),
            MathTex(r"\exists !\ G \ /\ \alpha\,\overrightarrow{GA}+\beta\,\overrightarrow{GB}+\gamma\,\overrightarrow{GC} = \vec{0}", font_size=28),
        ).arrange(DOWN, buff=0.3)
        theoreme = theorem_box(enonce_theoreme)
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le théorème se généralise exactement de la même manière : "
                "si alpha plus bêta plus gamma est non nul, il existe un "
                "unique point G tel que alpha G-A, plus bêta G-B, plus "
                "gamma G-C, soit égal au vecteur nul."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        etapes = VGroup(
            MathTex(r"\overrightarrow{GB}=\overrightarrow{GA}+\overrightarrow{AB}, \quad \overrightarrow{GC}=\overrightarrow{GA}+\overrightarrow{AC}", font_size=24),
            MathTex(r"\alpha\,\overrightarrow{GA}+\beta(\overrightarrow{GA}+\overrightarrow{AB})+\gamma(\overrightarrow{GA}+\overrightarrow{AC}) = \vec{0}", font_size=24),
            MathTex(r"(\alpha+\beta+\gamma)\,\overrightarrow{GA} = -\beta\,\overrightarrow{AB}-\gamma\,\overrightarrow{AC}", font_size=25),
            MathTex(
                r"\overrightarrow{AG} = \dfrac{\beta\,\overrightarrow{AB}+\gamma\,\overrightarrow{AC}}{\alpha+\beta+\gamma}"
                r"\quad (\alpha+\beta+\gamma \neq 0)",
                font_size=27,
                color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.3)
        etapes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La démonstration suit exactement la même méthode que pour "
                "deux points : on exprime G-B et G-C en fonction de G-A "
                "grâce à Chasles, on regroupe les termes en G-A, puis on "
                "isole le vecteur A-G, puisque alpha plus bêta plus gamma "
                "est non nul. On obtient le vecteur A-G égal à bêta A-B "
                "plus gamma A-C, le tout divisé par alpha plus bêta plus "
                "gamma. Cette égalité définit un unique point G : c'est à "
                "la fois l'existence et l'unicité."
            )
        ) as tracker:
            self.play(Write(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes))

        def_barycentre3 = definition_box(
            VGroup(
                Text("Barycentre de trois points pondérés", font_size=24, weight="BOLD"),
                MathTex(
                    r"\alpha+\beta+\gamma \neq 0 \ \Rightarrow\ G = \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\,;\,(C,\gamma)\}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        def_barycentre3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce point G est appelé le barycentre des trois points "
                "pondérés A-alpha, B-bêta et C-gamma, et se note G égale "
                "bar, ouvre accolade, A virgule alpha, B virgule bêta, C "
                "virgule gamma, ferme accolade."
            )
        ) as tracker:
            self.play(FadeIn(def_barycentre3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_barycentre3))

        # --- Exemple traité : exemple résolu 4 ---------------------------------
        donnees_ex4 = MathTex(r"G = \mathrm{bar}\{(A,3)\,;\,(B,-2)\,;\,(C,1)\}", font_size=27)
        calcul_ex4 = MathTex(
            r"\overrightarrow{AG} = \dfrac{-2\,\overrightarrow{AB}+1\,\overrightarrow{AC}}{3-2+1} "
            r"= -\overrightarrow{AB}+\dfrac{1}{2}\,\overrightarrow{AC}",
            font_size=25,
        )
        contenu_ex4 = VGroup(donnees_ex4, calcul_ex4).arrange(DOWN, buff=0.35)
        exemple4 = example_box(contenu_ex4)
        exemple4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : construisons G égal au barycentre de "
                "A-trois, B-moins deux et C-un. On applique directement la "
                "formule de réduction : le vecteur A-G est égal à moins "
                "deux A-B, plus un A-C, le tout divisé par trois moins deux "
                "plus un, c'est-à-dire deux. On obtient A-G égale moins le "
                "vecteur A-B, plus un demi le vecteur A-C."
            )
        ) as tracker:
            self.play(FadeIn(exemple4))
            self.wait(tracker.get_remaining_duration())

        a_pt = LEFT * 3.2
        b_pt = LEFT * 3.2 + RIGHT * 2.2 + UP * 1.6
        c_pt = LEFT * 3.2 + RIGHT * 3.6 + DOWN * 1.4
        g_pt = a_pt + (-1) * (b_pt - a_pt) + 0.5 * (c_pt - a_pt)

        pa = _dot_label(a_pt, "A")
        pb = _dot_label(b_pt, "B")
        pc = _dot_label(c_pt, "C", label_dir=DOWN)
        pg = _dot_label(g_pt, "G", dot_color="#288073", label_dir=DOWN)
        triangle = VGroup(Line(a_pt, b_pt), Line(b_pt, c_pt), Line(c_pt, a_pt), pa, pb, pc, pg)
        triangle.scale(0.8).next_to(exemple4, DOWN, buff=0.5)

        self.play(Create(triangle))
        self.wait(1)
        self.play(FadeOut(exemple4), FadeOut(triangle))

        # --- À retenir -----------------------------------------------------------
        retenir = theorem_box(
            MathTex(
                r"\alpha+\beta+\gamma \neq 0 \ \Longrightarrow\ \exists !\ G = \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\,;\,(C,\gamma)\}",
                font_size=26,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : dès que la somme des trois coefficients est "
                "non nulle, le barycentre de trois points pondérés existe "
                "et est unique, exactement comme pour deux points."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas oublier de vérifier α+β+γ≠0 avant de parler du "
                    "barycentre de trois points : cette condition porte "
                    "sur la somme des TROIS coefficients, pas seulement "
                    "deux d'entre eux.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à bien vérifier que la somme des trois "
                "coefficients, alpha plus bêta plus gamma, est non nulle "
                "avant de parler du barycentre : il ne suffit pas que deux "
                "coefficients seulement aient une somme non nulle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
