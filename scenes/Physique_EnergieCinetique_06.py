"""
scenes/Physique_EnergieCinetique_06.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 06.

§ Application : distance de freinage. Établissement de d = mv²/(2f) (route
horizontale, forces perpendiculaires au déplacement de travail nul, travail
de la force de freinage W = -fd). Conclusion capitale de sécurité routière :
la distance de freinage est proportionnelle au CARRÉ de la vitesse.
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, § 5, partie 2).
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
    Create,
    DoubleArrow,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ApplicationFreinage(NotionScene):
    def construct(self):
        titre = scene_title("Application : distance de freinage")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : voiture qui freine sur route horizontale --------------------
        route = Line(LEFT * 4.5, RIGHT * 4.5, color=WHITE, stroke_width=2)
        a_pt = LEFT * 3.5
        b_pt = RIGHT * 1.0
        voiture = Polygon(
            a_pt + LEFT * 0.35, a_pt + RIGHT * 0.35,
            a_pt + RIGHT * 0.25 + UP * 0.35, a_pt + LEFT * 0.25 + UP * 0.35,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.6, stroke_width=2,
        )
        v_arrow = Arrow(a_pt + UP * 0.5, a_pt + UP * 0.5 + RIGHT * 1.0, color="#288073", buff=0)
        v_label = MathTex("v", font_size=24, color="#288073").next_to(v_arrow, UP, buff=0.05)
        f_arrow = Arrow(a_pt + UP * 0.18, a_pt + UP * 0.18 + LEFT * 0.7, color="#B42E41", buff=0)
        f_label = MathTex("f", font_size=22, color="#B42E41").next_to(f_arrow, DOWN, buff=0.05)
        d_fleche = DoubleArrow(a_pt + DOWN * 0.5, b_pt + DOWN * 0.5, buff=0, stroke_width=2, color=WHITE)
        d_label = MathTex("d", font_size=24).next_to(d_fleche, DOWN, buff=0.1)
        label_a = MathTex("A", font_size=22).next_to(a_pt, UP + LEFT, buff=0.3)
        label_b = MathTex("B", font_size=22).next_to(b_pt, RIGHT, buff=0.2)
        schema = VGroup(route, voiture, v_arrow, v_label, f_arrow, f_label, d_fleche, d_label, label_a, label_b)
        schema.next_to(titre, DOWN, buff=0.5)

        enonce = Text(
            _wrap(
                "Une voiture de masse m, roulant à vitesse v sur une route "
                "horizontale, freine jusqu'à l'arrêt (v_B = 0), sous "
                "l'effet d'une force de freinage f constante. Quelle "
                "distance de freinage d parcourt-elle ?",
                width=54,
            ),
            font_size=21,
        )
        enonce.next_to(schema, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Appliquons le théorème de l'énergie cinétique à un cas "
                "très concret : le freinage. Une voiture de masse m, "
                "roulant à la vitesse v sur une route horizontale, freine "
                "jusqu'à l'arrêt complet sous l'effet d'une force de "
                "freinage f, supposée constante. Quelle distance de "
                "freinage d parcourt-elle avant de s'arrêter ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(enonce))

        # --- Raisonnement : établissement de d = mv^2/(2f) -------------------------
        raisonnement = VGroup(
            Text("Sur route horizontale : poids et réaction normale sont", font_size=21),
            Text("perpendiculaires au déplacement → travail nul.", font_size=21),
            MathTex(r"\Delta E_c = E_{cB} - E_{cA} = 0 - \dfrac{1}{2}mv^2 = W(\vec{f}) = -f\,d", font_size=25),
            MathTex(r"\Longrightarrow\ d = \dfrac{mv^2}{2f}", font_size=32, color=YELLOW),
        ).arrange(DOWN, buff=0.28)
        raisonnement.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Sur une route horizontale, le poids et la réaction "
                "normale du sol sont perpendiculaires au déplacement : "
                "leur travail est nul. Seule la force de freinage f "
                "travaille, avec un travail négatif égal à moins f fois "
                "d, puisqu'elle s'oppose au mouvement. Le théorème de "
                "l'énergie cinétique donne alors : zéro moins un demi m v "
                "carré égale moins f d. On en déduit la distance de "
                "freinage : d égale m v carré, divisé par deux f."
            )
        ) as tracker:
            self.play(Write(raisonnement[0]))
            self.play(Write(raisonnement[1]))
            self.play(Write(raisonnement[2]))
            self.play(Write(raisonnement[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(raisonnement))

        # --- Formule encadrée --------------------------------------------------------
        formule = theorem_box(
            VGroup(
                Text("Distance de freinage", font_size=23, weight="BOLD"),
                MathTex(r"d = \dfrac{mv^2}{2f}", font_size=34),
            ).arrange(DOWN, buff=0.25),
        )
        formule.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici donc la formule à retenir pour la distance de "
                "freinage sur une route horizontale : d égale m v carré, "
                "divisé par deux f."
            )
        ) as tracker:
            self.play(FadeIn(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule))

        # --- Conclusion capitale : comparaison graphique x2 vitesse → x4 distance ---
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 9, 3],
            x_length=5.4,
            y_length=3.6,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.6)
        courbe = axes.plot(lambda v: v**2, x_range=[0, 3], color=YELLOW)
        x_lab = MathTex("v", font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        y_lab = MathTex("d", font_size=22).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        conclusion_texte = VGroup(
            Text("×2 la vitesse", font_size=22, color=YELLOW),
            Text("→ ×4 la distance", font_size=22, color=YELLOW),
            Text("de freinage !", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.1)
        conclusion_texte.next_to(axes, RIGHT, buff=0.5)
        graphe = VGroup(axes, courbe, x_lab, y_lab)

        with self.voiceover(
            text=(
                "Conclusion capitale pour la sécurité routière : la "
                "distance de freinage est proportionnelle au carré de la "
                "vitesse, exactement comme l'énergie cinétique. Doubler "
                "la vitesse ne double pas la distance de freinage : cela "
                "la multiplie par quatre. C'est pour cette raison qu'un "
                "excès de vitesse, même modéré, augmente considérablement "
                "le risque et la gravité d'un accident."
            )
        ) as tracker:
            self.play(Create(axes), Write(x_lab), Write(y_lab))
            self.play(Create(courbe))
            self.play(FadeIn(conclusion_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe), FadeOut(conclusion_texte))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"d = \dfrac{mv^2}{2f}", font_size=28),
                Text("Distance de freinage ∝ v² : ×2 la vitesse → ×4 la distance.", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la distance de freinage vaut m v "
                "carré sur deux f, et surtout, elle est proportionnelle "
                "au carré de la vitesse — doubler la vitesse multiplie "
                "cette distance par quatre, un réflexe de sécurité "
                "routière à ne jamais oublier."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
