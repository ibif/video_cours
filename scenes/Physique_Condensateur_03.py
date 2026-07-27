"""
scenes/Physique_Condensateur_03.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 03.

§ 3. Charge à courant constant. Montage avec générateur de courant
constant. Observation u=f(t) : droite passant par l'origine. Relations
q=It et u=q/C=It/C (pente I/C).
Exemple résolu 1 : C=50 µF, I=10 µA → q(30 s)=300 µC, u=6 V, puis durée
pour u=12 V → t=60 s.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 3a).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Axes,
    Circle,
    Create,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _montage_courant_constant():
    """Boucle générateur de courant constant (cercle + flèche interne) —
    condensateur (deux traits verticaux), construit avec Line/Circle."""
    tl = UP * 1.0 + LEFT * 2.6
    tr = UP * 1.0 + RIGHT * 2.6
    bl = DOWN * 1.0 + LEFT * 2.6
    br = DOWN * 1.0 + RIGHT * 2.6

    fil_haut = Line(tl, tr, stroke_width=3, color=WHITE)
    fil_bas_g = Line(bl, br / 1, stroke_width=3, color=WHITE)  # replaced below
    fil_bas = Line(bl, br, stroke_width=3, color=WHITE)

    # Générateur de courant constant à gauche (cercle + flèche interne)
    gen_center = LEFT * 2.6
    gen = Circle(radius=0.38, color=YELLOW, stroke_width=3)
    gen.move_to(gen_center)
    fleche_gen = Arrow(
        gen_center + DOWN * 0.22, gen_center + UP * 0.22,
        buff=0, stroke_width=3, color=YELLOW, max_tip_length_to_length_ratio=0.4,
    )
    fil_g_haut = Line(tl, gen_center + UP * 0.38, stroke_width=3, color=WHITE)
    fil_g_bas = Line(gen_center + DOWN * 0.38, bl, stroke_width=3, color=WHITE)

    # Condensateur à droite (deux traits verticaux)
    plaque_1 = Line(UP * 0.4, DOWN * 0.4, stroke_width=6, color=WHITE).shift(RIGHT * 2.6 + LEFT * 0.15)
    plaque_2 = Line(UP * 0.4, DOWN * 0.4, stroke_width=6, color=WHITE).shift(RIGHT * 2.6 + RIGHT * 0.15)
    fil_d_haut = Line(tr, plaque_1.get_center() + UP * 0.4, stroke_width=3, color=WHITE)
    fil_d_bas = Line(plaque_2.get_center() + DOWN * 0.4, br, stroke_width=3, color=WHITE)

    label_I = Text("I", font_size=20, color=YELLOW).next_to(gen, LEFT, buff=0.15)
    label_C = Text("C", font_size=20, color=WHITE).next_to(VGroup(plaque_1, plaque_2), UP, buff=0.15)

    return VGroup(
        fil_haut, fil_bas, gen, fleche_gen, fil_g_haut, fil_g_bas,
        plaque_1, plaque_2, fil_d_haut, fil_d_bas, label_I, label_C,
    )


class ChargeCourantConstant(NotionScene):
    def construct(self):
        titre = scene_title("Charge d'un condensateur à courant constant")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Si l'on charge un condensateur avec un générateur qui "
                "délivre un courant constant I, comment la tension u à "
                "ses bornes évolue-t-elle au cours du temps ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Si l'on charge un condensateur avec un générateur qui "
                "délivre un courant constant I, comment la tension u à ses "
                "bornes évolue-t-elle au cours du temps ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : montage + relations q=It, u=It/C ------------------
        montage = _montage_courant_constant()
        montage.scale(0.85)
        montage.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le montage : un générateur de courant constant "
                "impose une intensité I fixe dans le circuit, qui charge le "
                "condensateur de capacité C."
            )
        ) as tracker:
            self.play(FadeIn(montage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(montage))

        relations = definition_box(
            VGroup(
                Text("Comme I est constant, la charge accumulée après une durée t est :", font_size=20),
                MathTex(r"q = I \, t", font_size=30),
                Text("Or u = q/C, donc la tension aux bornes du condensateur vaut :", font_size=20),
                MathTex(r"u = \dfrac{q}{C} = \dfrac{I}{C}\, t", font_size=30, color=YELLOW),
                Text("u = f(t) est une DROITE passant par l'origine, de pente I/C.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        relations.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Comme l'intensité I est constante, la charge accumulée "
                "après une durée t vaut simplement q égale I t. Or la "
                "tension aux bornes du condensateur vaut u égale q sur C, "
                "donc u égale I sur C, le tout multiplié par t. La courbe u "
                "en fonction de t est donc une droite passant par "
                "l'origine, de pente I sur C."
            )
        ) as tracker:
            self.play(FadeIn(relations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(relations))

        # --- Graphe u = f(t) -----------------------------------------------------
        axes = Axes(
            x_range=[0, 70, 10],
            y_range=[0, 14, 2],
            x_length=6.2,
            y_length=3.8,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.2)
        droite = axes.plot(lambda t: 0.2 * t, x_range=[0, 65], color=YELLOW)
        x_lab = MathTex("t\\ (\\text{s})", font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        y_lab = MathTex("u\\ (\\text{V})", font_size=22).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        pente_txt = MathTex(r"\text{pente} = \dfrac{I}{C}", font_size=24, color=YELLOW)
        pente_txt.next_to(axes, RIGHT, buff=0.5)

        graphe = VGroup(axes, droite, x_lab, y_lab)

        with self.voiceover(
            text=(
                "Sur le graphique, u en fonction de t est bien une droite "
                "qui part de l'origine : à l'instant zéro, le condensateur "
                "est déchargé, u est nul. Sa pente est constante et vaut I "
                "sur C."
            )
        ) as tracker:
            self.play(Create(axes), Write(x_lab), Write(y_lab))
            self.play(Create(droite), FadeIn(pente_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe), FadeOut(pente_txt))

        # --- Exemple résolu 1 ------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un condensateur C = 50 µF est chargé sous I = 10 µA constant.", font_size=20),
                MathTex(r"q(30\,\text{s}) = I t = 10 \times 30 = 300\ \mu\text{C}", font_size=25),
                MathTex(r"u = \dfrac{q}{C} = \dfrac{300}{50} = 6\ \text{V}", font_size=25),
                Text("Durée pour atteindre u = 12 V ?", font_size=20),
                MathTex(r"t = \dfrac{Cu}{I} = \dfrac{50 \times 12}{10} = 60\ \text{s}", font_size=25),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : un condensateur de cinquante microfarads "
                "est chargé sous un courant constant de dix microampères. "
                "Après trente secondes, la charge vaut I fois t, soit trois "
                "cents microcoulombs, ce qui donne une tension de six "
                "volts. Quelle durée faut-il pour atteindre douze volts ? "
                "En isolant t, on trouve C u sur I, soit soixante secondes."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"q = I t, \qquad u = \dfrac{q}{C} = \dfrac{I}{C}\, t", font_size=27),
                Text("u = f(t) : droite passant par l'origine, pente I/C.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : sous courant constant, q égale I t, "
                "et la tension u égale q sur C, soit I sur C fois t. La "
                "courbe u de t est donc une droite passant par l'origine, "
                "de pente I sur C."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Toujours convertir en unités du Système International", font_size=20),
                Text("   (µF → F, µA → A) avant tout calcul, sous peine d'erreur.", font_size=20),
                Text("• Cette droite n'existe QUE sous courant constant : dès qu'un", font_size=20),
                Text("   résistor intervient, l'évolution devient exponentielle (§ suivants).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Il faut toujours convertir les "
                "unités dans le Système International avant tout calcul : "
                "les microfarads en farads, les microampères en ampères. "
                "Et cette droite n'existe que sous courant constant : dès "
                "qu'un résistor intervient dans le montage, l'évolution "
                "devient exponentielle, comme nous le verrons plus loin."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
