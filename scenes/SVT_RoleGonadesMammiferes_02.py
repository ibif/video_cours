"""
scenes/SVT_RoleGonadesMammiferes_02.py — Chapitre 1 (1ereC, SVT), scène 02.

L'appareil reproducteur mâle : schéma simplifié (vessie, prostate,
vésicules séminales, canal déférent, urètre, pénis, testicule dans le
scrotum, épididyme, glande de Cowper), trajet du spermatozoïde, tableau
des organes et de leur rôle. Source : 1ereC/SVT.pdf, pages 5-6.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Circle,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    MoveAlongPath,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=18, color=WHITE, width=30):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    return lines


class AppareilReproducteurMale(NotionScene):
    def construct(self):
        titre = scene_title("1.2 — L'appareil reproducteur mâle")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : présentation générale ----------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'appareil reproducteur mâle est l'ensemble des organes "
                    "qui produisent, font mûrir et acheminent les "
                    "spermatozoïdes jusqu'à l'extérieur du corps.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'appareil reproducteur mâle est l'ensemble des organes qui "
                "produisent les spermatozoïdes, les font mûrir, puis les "
                "acheminent jusqu'à l'extérieur du corps. Découvrons ses "
                "différents organes sur un schéma simplifié."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : construction du schéma --------------
        vessie = Circle(radius=0.4, color=WHITE, stroke_width=3)
        vessie.next_to(titre, DOWN, buff=0.7).shift(LEFT * 3.5)
        vessie_lbl = Text("vessie", font_size=15, color=WHITE).next_to(vessie, UP, buff=0.1)

        vesicule = Ellipse(width=0.7, height=0.35, color="#DE7C1F", fill_opacity=0.85)
        vesicule.next_to(vessie, RIGHT, buff=0.5).shift(DOWN * 0.1)
        vesicule_lbl = Text("vésicule séminale", font_size=13, color=WHITE).next_to(vesicule, UP, buff=0.1)

        prostate = Circle(radius=0.28, color="#A42A5A", fill_opacity=0.85)
        prostate.next_to(vesicule, RIGHT, buff=0.4).shift(DOWN * 0.2)
        prostate_lbl = Text("prostate", font_size=13, color=WHITE).next_to(prostate, UP, buff=0.1)

        cowper = Circle(radius=0.13, color="#288073", fill_opacity=0.85)
        cowper.next_to(prostate, RIGHT, buff=0.6).shift(DOWN * 0.5)
        cowper_lbl = Text("glande de Cowper", font_size=12, color=WHITE).next_to(cowper, UP, buff=0.1)

        urethre = Line(prostate.get_bottom(), cowper.get_center() + DOWN * 0.1, color=WHITE, stroke_width=3)
        penis = Rectangle(width=1.6, height=0.35, color=WHITE, stroke_width=3)
        penis.next_to(cowper, RIGHT, buff=0.1)
        penis_lbl = Text("pénis", font_size=15, color=WHITE).next_to(penis, UP, buff=0.1)
        urethre2 = Line(cowper.get_center(), penis.get_left(), color=WHITE, stroke_width=3)
        urethre_lbl = Text("urètre", font_size=13, color=YELLOW).next_to(urethre, DOWN, buff=0.1)

        scrotum = Ellipse(width=1.6, height=1.1, color=WHITE, stroke_width=2)
        scrotum.next_to(vessie, DOWN, buff=1.4)
        testicule = Ellipse(width=0.9, height=0.6, color="#1E5FA8", fill_opacity=0.85)
        testicule.move_to(scrotum.get_center() + DOWN * 0.1)
        testicule_lbl = Text("testicule", font_size=14, color=WHITE).next_to(testicule, DOWN, buff=0.35)
        scrotum_lbl = Text("scrotum", font_size=13, color=WHITE).next_to(scrotum, LEFT, buff=0.15)

        epididyme = Arc(radius=0.55, angle=2.4, start_angle=0.9, color="#B42E41", stroke_width=4)
        epididyme.move_to(testicule.get_center() + UP * 0.05)
        epididyme_lbl = Text("épididyme", font_size=12, color=WHITE).next_to(epididyme, RIGHT, buff=0.1)

        canal_deferent = Line(
            epididyme.get_top(), prostate.get_bottom() + DOWN * 0.3, color="#B42E41", stroke_width=3
        )
        canal_lbl = Text("canal déférent", font_size=12, color=WHITE).next_to(
            canal_deferent, LEFT, buff=0.1
        )

        schema = VGroup(
            vessie, vessie_lbl,
            vesicule, vesicule_lbl,
            prostate, prostate_lbl,
            cowper, cowper_lbl,
            urethre, urethre2, urethre_lbl,
            penis, penis_lbl,
            scrotum, scrotum_lbl,
            testicule, testicule_lbl,
            epididyme, epididyme_lbl,
            canal_deferent, canal_lbl,
        )
        schema.move_to(schema.get_center()).next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Au centre du schéma, le testicule, logé dans le scrotum, "
                "produit les spermatozoïdes. Juste au-dessus, l'épididyme, un "
                "tube enroulé, assure leur maturation et leur stockage. Le "
                "canal déférent transporte ensuite les spermatozoïdes vers "
                "l'urètre, en passant près de la vessie, où se trouvent les "
                "vésicules séminales et la prostate, deux glandes qui "
                "ajoutent leurs sécrétions. Les glandes de Cowper sécrètent "
                "un mucus lubrifiant juste avant l'urètre, qui traverse "
                "enfin le pénis, l'organe copulateur."
            )
        ) as tracker:
            self.play(FadeIn(scrotum), FadeIn(scrotum_lbl))
            self.play(FadeIn(testicule), FadeIn(testicule_lbl))
            self.play(FadeIn(epididyme), FadeIn(epididyme_lbl))
            self.play(FadeIn(canal_deferent), FadeIn(canal_lbl))
            self.play(FadeIn(vessie), FadeIn(vessie_lbl), FadeIn(vesicule), FadeIn(vesicule_lbl))
            self.play(FadeIn(prostate), FadeIn(prostate_lbl))
            self.play(FadeIn(cowper), FadeIn(cowper_lbl), FadeIn(urethre), FadeIn(urethre2), FadeIn(urethre_lbl))
            self.play(FadeIn(penis), FadeIn(penis_lbl))
            self.wait(tracker.get_remaining_duration())

        # --- Exemple traité : le trajet du spermatozoïde ----------------------
        trajet_lbl = Text("Trajet d'un spermatozoïde", font_size=20, color=YELLOW, weight="BOLD")
        trajet_lbl.next_to(schema, DOWN, buff=0.35)

        point = Dot(color=YELLOW, radius=0.09)
        point.move_to(testicule.get_center())

        chemin = VGroup(
            Line(testicule.get_center(), epididyme.get_top()),
            Line(epididyme.get_top(), canal_deferent.get_end()),
            Line(canal_deferent.get_end(), prostate.get_bottom()),
            Line(prostate.get_bottom(), cowper.get_center()),
            Line(cowper.get_center(), penis.get_right()),
        )

        with self.voiceover(
            text=(
                "Suivons le trajet d'un spermatozoïde : formé dans le "
                "testicule, il gagne l'épididyme où il termine sa "
                "maturation, puis emprunte le canal déférent, traverse la "
                "région de la prostate où se mélangent les sécrétions des "
                "glandes annexes, et parcourt enfin l'urètre jusqu'au bout "
                "du pénis lors de l'éjaculation."
            )
        ) as tracker:
            self.play(FadeIn(trajet_lbl), FadeIn(point))
            for segment in chemin:
                self.play(MoveAlongPath(point, segment), run_time=0.6)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(trajet_lbl), FadeOut(point))

        # --- À retenir : tableau des organes et de leur rôle -------------------
        entete_tab = Text("Tableau des organes", font_size=26, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        col1 = _bullets(
            [
                "Testicules : spermatozoïdes + testostérone",
                "Épididymes : maturation, stockage",
                "Canaux déférents : transport",
                "Vésicules séminales : liquide séminal",
                "Prostate : liquide nourricier alcalin",
            ],
            width=28,
        )
        col2 = _bullets(
            [
                "Glandes de Cowper : mucus lubrifiant",
                "Pénis : organe copulateur",
                "Urètre : urine ET éjaculation",
                "Scrotum : maintien à ≈ 35 °C",
            ],
            width=28,
        )
        tableau = VGroup(col1, col2).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        tableau.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résumons dans un tableau. Les testicules produisent les "
                "spermatozoïdes et la testostérone. Les épididymes assurent "
                "la maturation et le stockage. Les canaux déférents "
                "transportent les spermatozoïdes. Les vésicules séminales "
                "et la prostate sécrètent le liquide séminal nourricier. "
                "Les glandes de Cowper produisent un mucus lubrifiant. Le "
                "pénis est l'organe copulateur. L'urètre sert à la fois à "
                "l'urine et à l'éjaculation. Enfin, le scrotum maintient les "
                "testicules à une température d'environ trente-cinq degrés, "
                "légèrement inférieure à celle du corps."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(col1))
            self.play(FadeIn(col2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas le scrotum (le sac cutané qui contient "
                    "et régule la température) avec le testicule "
                    "(l'organe producteur, à l'intérieur). De même, "
                    "l'épididyme STOCKE les spermatozoïdes ; le canal "
                    "déférent les TRANSPORTE seulement.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre le scrotum, ce sac cutané qui "
                "contient les testicules et régule leur température, avec le "
                "testicule lui-même, l'organe producteur situé à "
                "l'intérieur. De même, l'épididyme stocke les "
                "spermatozoïdes, alors que le canal déférent se contente de "
                "les transporter."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
