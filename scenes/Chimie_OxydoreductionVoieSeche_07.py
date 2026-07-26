"""
scenes/Chimie_OxydoreductionVoieSeche_07.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 07.

§ 4 (fin). Réduction des oxydes métalliques : aluminothermie (thermite
Al + Fe₂O₃, très exothermique, > 1500 °C), application à la soudure des
rails. Réduction de CuO par H₂ (dispositif, dépôt rouge-orangé, eau
condensée). Réduction de CuO par le carbone (dépôt cuivre + CO₂ trouble
l'eau de chaux).
Source : 1ereC/Chimie.pdf, chapitre 13, pages 130-131.
"""

import textwrap

from manim import (
    DOWN,
    GRAY,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _schema_thermite():
    """Schéma simplifié d'une réaction aluminothermique : creuset conique
    d'où jaillissent des étincelles et une coulée de fer liquide,
    construit avec des primitives Manim de base (Polygon, Line, Circle,
    VGroup) — aucune bibliothèque externe."""
    creuset = Polygon(
        [-0.7, 0.5, 0], [-0.4, -0.5, 0], [0.4, -0.5, 0], [0.7, 0.5, 0],
        fill_color=GRAY, fill_opacity=0.3, stroke_color=WHITE, stroke_width=2,
    )
    etincelles = VGroup(*[
        Circle(radius=0.05, fill_color=YELLOW, fill_opacity=1, stroke_width=0).move_to(
            [0.35 * ((-1) ** i), 0.7 + 0.25 * (i % 3), 0]
        )
        for i in range(7)
    ])
    coulee = Polygon(
        [-0.15, -0.5, 0], [0.15, -0.5, 0], [0.05, -1.1, 0], [-0.05, -1.1, 0],
        fill_color=ORANGE, fill_opacity=1, stroke_width=0,
    )
    flaque = Circle(radius=0.18, fill_color=ORANGE, fill_opacity=1, stroke_width=0)
    flaque.stretch(0.4, dim=1)
    flaque.move_to([0, -1.15, 0])
    return VGroup(creuset, etincelles, coulee, flaque)


def _schema_reduction_h2(stade="chauffe"):
    """Dispositif de réduction de CuO par H₂ : tube à essai incliné
    contenant la poudre noire CuO chauffée, traversé par un courant de
    H₂, avec un col recourbé où se condense l'eau formée. Construit avec
    des primitives Manim de base (Line, Rectangle, Circle, VGroup)."""
    tube = Line([-1.6, -0.3, 0], [1.0, 0.5, 0], color=WHITE, stroke_width=3)
    tube_bas = Line([-1.6, -0.55, 0], [1.0, 0.25, 0], color=WHITE, stroke_width=3)
    fond_tube = Line([-1.6, -0.55, 0], [-1.6, -0.3, 0], color=WHITE, stroke_width=3)

    poudre_color = GRAY if stade == "chauffe" else ORANGE
    poudre = Rectangle(width=0.9, height=0.2, fill_color=poudre_color, fill_opacity=1, stroke_width=0)
    poudre.move_to([-1.1, -0.42, 0])
    poudre.rotate(0.28)

    arrivee_h2 = Line([1.0, 0.5, 0], [1.0, 0.25, 0], color=WHITE, stroke_width=3)
    fleche_h2 = Line([1.7, 0.37, 0], [1.05, 0.37, 0], color="#288073", stroke_width=3)
    label_h2 = Text("H₂", font_size=16, color="#288073")
    label_h2.next_to(fleche_h2, RIGHT, buff=0.1)

    gouttelettes = VGroup()
    if stade == "condense":
        for i in range(3):
            g = Circle(radius=0.04, fill_color="#4FA3D1", fill_opacity=0.9, stroke_width=0)
            g.move_to([-0.2 + 0.35 * i, 0.15 + 0.02 * i, 0])
            gouttelettes.add(g)

    flamme = VGroup()
    if stade == "chauffe":
        f = Polygon(
            [-1.1, -0.75, 0], [-0.95, -1.05, 0], [-1.1, -1.25, 0],
            [-1.25, -1.05, 0],
            fill_color=ORANGE, fill_opacity=0.9, stroke_width=0,
        )
        flamme.add(f)

    label_depot = Text("dépôt rouge-orangé (Cu)" if stade == "condense" else "poudre noire CuO", font_size=14, color=WHITE)
    label_depot.next_to(poudre, DOWN, buff=0.35)

    return VGroup(tube, tube_bas, fond_tube, poudre, arrivee_h2, fleche_h2, label_h2, gouttelettes, flamme, label_depot)


class ReductionOxydesMetalliques(NotionScene):
    def construct(self):
        titre = scene_title("13.4 Réduction des oxydes métalliques")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : la question de la métallurgie -------------------------
        intro = Text(
            _wrap(
                "Comment récupérer un métal pur à partir de son oxyde ? "
                "Il faut un réducteur assez puissant pour lui arracher "
                "l'oxygène. Trois réducteurs usuels : l'aluminium, le "
                "dihydrogène, et le carbone.",
                width=56,
            ),
            font_size=23, color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment récupérer un métal pur à partir de son oxyde ? "
                "Il faut un réducteur assez puissant pour lui arracher son "
                "oxygène : l'oxyde métallique va alors être réduit. Trois "
                "réducteurs usuels sont employés en métallurgie : "
                "l'aluminium, le dihydrogène, et le carbone."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : l'aluminothermie ---------------------------------
        def_thermite = definition_box(
            Text(
                _wrap(
                    "L'ALUMINOTHERMIE (réaction de la thermite) est la "
                    "réduction TRÈS EXOTHERMIQUE d'un oxyde métallique par "
                    "l'aluminium, qui libère le métal à l'état LIQUIDE "
                    "(température supérieure à 1500 °C).",
                    width=32,
                ),
                font_size=19,
            ),
            box_width=6.6,
        )

        schema_thermite = _schema_thermite()
        equation_thermite = MathTex(r"2\,Al + Fe_2O_3 \longrightarrow Al_2O_3 + 2\,Fe", font_size=26)

        groupe_thermite = VGroup(def_thermite, VGroup(schema_thermite, equation_thermite).arrange(DOWN, buff=0.35))
        groupe_thermite.arrange(RIGHT, buff=0.7)
        groupe_thermite.next_to(titre, DOWN, buff=0.35)
        _fit(groupe_thermite, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "L'aluminothermie, ou réaction de la thermite, est la "
                "réduction très exothermique d'un oxyde métallique par "
                "l'aluminium, qui libère le métal à l'état liquide, à une "
                "température supérieure à mille cinq cents degrés. Avec "
                "l'oxyde de fer trois, l'équation s'écrit : deux Al plus "
                "Fe deux O trois, donne Al deux O trois plus deux Fe. "
                "Cette réaction est utilisée sur le terrain pour souder "
                "les rails de chemin de fer : le fer liquide produit "
                "comble directement le joint entre deux rails."
            )
        ) as tracker:
            self.play(FadeIn(def_thermite))
            self.play(FadeIn(schema_thermite))
            self.play(Write(equation_thermite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_thermite))

        # --- Exemple traité : réduction de CuO par H2 ------------------------
        entete_h2 = Text("Réduction de CuO par le dihydrogène", font_size=21, color=YELLOW, weight="BOLD")
        entete_h2.next_to(titre, DOWN, buff=0.35)

        schema_chauffe = _schema_reduction_h2("chauffe")
        schema_condense = _schema_reduction_h2("condense")
        schema_chauffe.next_to(entete_h2, DOWN, buff=0.4)
        schema_condense.move_to(schema_chauffe)

        equation_h2 = MathTex(r"CuO + H_2 \longrightarrow Cu + H_2O", font_size=28)
        equation_h2.next_to(schema_chauffe, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le dispositif de réduction de l'oxyde de cuivre par "
                "le dihydrogène. On chauffe la poudre noire de CuO dans un "
                "tube incliné, tout en y faisant circuler un courant de "
                "dihydrogène. Peu à peu, la poudre noire devient un dépôt "
                "rouge-orangé de cuivre métallique, et des gouttelettes "
                "d'eau se condensent sur les parois froides du tube. "
                "L'équation s'écrit : CuO plus H deux, donne Cu plus H "
                "deux O."
            )
        ) as tracker:
            self.play(FadeIn(entete_h2))
            self.play(FadeIn(schema_chauffe))
            self.wait(0.4)
            self.play(FadeIn(equation_h2))
            self.wait(0.4)
            self.play(FadeOut(schema_chauffe), FadeIn(schema_condense))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_h2), FadeOut(schema_condense), FadeOut(equation_h2))

        # --- Exemple traité (suite) : réduction de CuO par le carbone ---------
        entete_c = Text("Réduction de CuO par le carbone", font_size=21, color=YELLOW, weight="BOLD")
        entete_c.next_to(titre, DOWN, buff=0.35)

        equation_c = MathTex(r"2\,CuO + C \longrightarrow 2\,Cu + CO_2", font_size=28)
        equation_c.next_to(entete_c, DOWN, buff=0.5)

        obs_c = _bullets(
            [
                "Un dépôt de cuivre métallique (rouge) se forme, comme "
                "avec H₂ ;",
                "le CO₂ dégagé trouble l'eau de chaux "
                "(précipité blanc de CaCO₃), preuve de sa présence.",
            ],
            width=48,
        )
        obs_c.next_to(equation_c, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On peut aussi réduire l'oxyde de cuivre en chauffant un "
                "mélange de poudre de CuO et de carbone : deux CuO plus C, "
                "donne deux Cu plus CO deux. Là encore, un dépôt de cuivre "
                "métallique rouge se forme. Et cette fois, le dioxyde de "
                "carbone dégagé trouble l'eau de chaux, en formant un "
                "précipité blanc de carbonate de calcium : c'est la "
                "preuve caractéristique de sa présence."
            )
        ) as tracker:
            self.play(FadeIn(entete_c))
            self.play(Write(equation_c))
            self.play(FadeIn(obs_c))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_c), FadeOut(equation_c), FadeOut(obs_c))

        # --- À retenir : principe commun ---------------------------------------
        retenir = property_box(
            Text(
                _wrap(
                    "Principe commun : dans les trois cas (Al, H₂, C), "
                    "c'est l'OXYDE MÉTALLIQUE qui est RÉDUIT (le métal "
                    "gagne des électrons, son n.o. diminue) et le "
                    "réducteur (Al, H₂ ou C) qui est OXYDÉ.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons le principe commun à ces trois réactions : dans "
                "chaque cas, c'est l'oxyde métallique qui est réduit — le "
                "métal qu'il contient gagne des électrons, son n.o. "
                "diminue — tandis que le réducteur employé, aluminium, "
                "dihydrogène ou carbone, est lui-même oxydé."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas inverser les rôles : c'est le MÉTAL DE L'OXYDE "
                    "(Fe, Cu…) qui est réduit, et le RÉDUCTEUR AJOUTÉ "
                    "(Al, H₂, C) qui est oxydé — pas l'inverse.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas inverser les rôles : c'est le métal "
                "contenu dans l'oxyde de départ, fer ou cuivre par "
                "exemple, qui est réduit, et le réducteur ajouté, "
                "aluminium, dihydrogène ou carbone, qui est oxydé — "
                "jamais l'inverse."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
