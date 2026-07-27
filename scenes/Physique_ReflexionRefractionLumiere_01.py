"""
scenes/Physique_ReflexionRefractionLumiere_01.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 01.

§ Réflexion de la lumière : dispositif expérimental (demi-cercle gradué +
miroir plan), vocabulaire (rayon incident SI, point d'incidence I, normale
IN, rayon réfléchi IR, angle d'incidence i1, angle de réflexion i'1, plan
d'incidence), lois de Snell-Descartes de la réflexion (1ère loi : plan
d'incidence ; 2e loi : i'1 = i1), cas particuliers (incidence normale,
incidence rasante, réflexion spéculaire vs diffusion), exemple résolu
(rayon à 50° de la surface).
Source : 1ereC/Physique.pdf, pages 117-129.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREY,
    Angle,
    Create,
    DashedLine,
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
from shapes.boxes import definition_box, essentiel_box, example_box, theorem_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _reflexion_schema(i1_deg: float, center: np.ndarray = ORIGIN, t: float = 2.2, surf_half: float = 2.6):
    """
    Construit un schéma de réflexion : surface horizontale, normale
    pointillée, rayon incident SI (S en haut à gauche) et rayon réfléchi IR
    (R en haut à droite), avec i'1 = i1 (loi de la réflexion).
    Retourne (groupe_visuel, S, I, R) pour permettre l'ajout de labels.
    """
    i1 = np.radians(i1_deg)
    I = center

    surface = Line(I + LEFT * surf_half, I + RIGHT * surf_half, color=GREY, stroke_width=4)
    normale = DashedLine(I + DOWN * 1.0, I + UP * 1.9, color=WHITE, stroke_width=2)

    S = I + t * np.array([-np.sin(i1), np.cos(i1), 0])
    R = I + t * np.array([np.sin(i1), np.cos(i1), 0])

    rayon_incident = Line(S, I, color=YELLOW, stroke_width=4)
    rayon_reflechi = Line(I, R, color=YELLOW, stroke_width=4)
    point_I = Dot(I, color=WHITE, radius=0.06)

    groupe = VGroup(surface, normale, rayon_incident, rayon_reflechi, point_I)

    # Les arcs d'angle n'ont de sens que si i1 > 0 (sinon les trois droites
    # sont confondues et Angle() ne peut pas calculer d'intersection unique).
    if i1_deg > 1:
        seg_normale_haut = Line(I, I + UP * 0.7, color=WHITE, stroke_width=1)
        seg_incident = Line(I, S, color=YELLOW, stroke_width=1)
        seg_reflechi = Line(I, R, color=YELLOW, stroke_width=1)
        arc_i1 = Angle(seg_normale_haut, seg_incident, radius=0.55, color=BLUE)
        arc_i1p = Angle(seg_reflechi, seg_normale_haut, radius=0.55, color=BLUE)
        groupe.add(arc_i1, arc_i1p)

    return groupe, S, I, R


class ReflexionLoisSnellDescartes(NotionScene):
    def construct(self):
        titre = scene_title("Réflexion : expérience et lois de Snell-Descartes")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : dispositif expérimental ---------------------------------
        mise_en_situation = Text(
            _wrap(
                "Sur un banc d'optique, on envoie un rayon laser sur un "
                "miroir plan fixé au centre d'un disque gradué en degrés. "
                "Que devient ce rayon lorsqu'il touche le miroir ?",
                width=48,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        schema0, S0, I0, R0 = _reflexion_schema(35, center=DOWN * 0.6)
        schema0.next_to(mise_en_situation, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sur un banc d'optique, on envoie un rayon laser sur un "
                "miroir plan fixé au centre d'un disque gradué en degrés. "
                "Que devient ce rayon lorsqu'il touche le miroir ? On "
                "observe qu'il repart dans une autre direction bien "
                "précise : c'est le phénomène de réflexion."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(Create(schema0))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(schema0))

        # --- Raisonnement : vocabulaire du schéma ------------------------------
        schema, S, I, R = _reflexion_schema(35, center=LEFT * 2.6 + DOWN * 0.3)
        label_S = Text("S", font_size=22, color=WHITE).next_to(S, UP, buff=0.1)
        label_I = Text("I", font_size=22, color=WHITE).next_to(I, DOWN, buff=0.15)
        label_R = Text("R", font_size=22, color=WHITE).next_to(R, UP, buff=0.1)
        label_N = Text("N", font_size=22, color=WHITE).next_to(I + UP * 1.9, UP, buff=0.1)
        label_i1 = MathTex("i_1", font_size=24, color=BLUE).move_to(I + UP * 0.85 + LEFT * 0.45)
        label_i1p = MathTex("i_1'", font_size=24, color=BLUE).move_to(I + UP * 0.85 + RIGHT * 0.45)
        schema_legende = VGroup(schema, label_S, label_I, label_R, label_N, label_i1, label_i1p)
        schema_legende.move_to(LEFT * 3.0 + DOWN * 0.2)

        vocabulaire = VGroup(
            Text("SI : rayon incident", font_size=20),
            Text("I : point d'incidence", font_size=20),
            Text("IN : normale (⊥ à la surface en I)", font_size=20),
            Text("IR : rayon réfléchi", font_size=20),
            Text("i1 : angle d'incidence (SI, normale)", font_size=20),
            Text("i'1 : angle de réflexion (normale, IR)", font_size=20),
            Text("Plan d'incidence : plan contenant SI et IN", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        vocabulaire.next_to(schema_legende, RIGHT, buff=0.8)

        with self.voiceover(
            text=(
                "Fixons le vocabulaire. Le rayon SI qui arrive sur le "
                "miroir est le rayon incident. Le point I où il touche le "
                "miroir est le point d'incidence. La droite IN, "
                "perpendiculaire à la surface en I, est la normale. Le "
                "rayon IR qui repart est le rayon réfléchi. L'angle i1 "
                "entre le rayon incident et la normale est l'angle "
                "d'incidence, et l'angle i'1 entre la normale et le rayon "
                "réfléchi est l'angle de réflexion. Enfin, le plan "
                "d'incidence est le plan qui contient à la fois le rayon "
                "incident et la normale."
            )
        ) as tracker:
            self.play(Create(schema_legende))
            self.play(Write(vocabulaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_legende), FadeOut(vocabulaire))

        # --- Théorème : lois de Snell-Descartes de la réflexion ----------------
        loi = theorem_box(
            VGroup(
                Text("Lois de Snell-Descartes de la réflexion", font_size=22, weight="BOLD"),
                Text("1ère loi : le rayon incident, la normale et le rayon", font_size=20),
                Text("réfléchi sont coplanaires (tous les trois dans le plan", font_size=20),
                Text("d'incidence).", font_size=20),
                MathTex(r"\text{2e loi : } i_1' = i_1", font_size=28, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=12.0,
        )
        loi.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Ces observations se résument en deux lois de "
                "Snell-Descartes. Première loi : le rayon réfléchi est "
                "situé dans le plan d'incidence, c'est-à-dire le plan qui "
                "contient le rayon incident et la normale. Deuxième loi : "
                "l'angle de réflexion i'1 est égal à l'angle d'incidence "
                "i1."
            )
        ) as tracker:
            self.play(FadeIn(loi))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi))

        # --- Cas particuliers ----------------------------------------------------
        cas1_schema, _, cas1_I, _ = _reflexion_schema(0, center=LEFT * 3.6 + DOWN * 0.3, t=1.6, surf_half=1.3)
        cas1_label = Text("incidence normale (i1=0)", font_size=17).next_to(cas1_schema, DOWN, buff=0.25)

        cas2_schema, _, cas2_I, _ = _reflexion_schema(80, center=RIGHT * 0.4 + DOWN * 0.3, t=1.8, surf_half=1.6)
        cas2_label = Text("incidence rasante (i1→90°)", font_size=17).next_to(cas2_schema, DOWN, buff=0.25)

        cas_groupe = VGroup(
            VGroup(cas1_schema, cas1_label), VGroup(cas2_schema, cas2_label)
        )
        cas_groupe.next_to(titre, DOWN, buff=0.6)

        texte_diffusion = Text(
            _wrap(
                "Miroir lisse (poli) : rayons parallèles restent parallèles "
                "après réflexion — c'est la réflexion spéculaire. Surface "
                "rugueuse : les rayons repartent dans toutes les "
                "directions — c'est la diffusion.",
                width=48,
            ),
            font_size=19,
        )
        texte_diffusion.next_to(cas_groupe, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux cas particuliers méritent d'être notés. En incidence "
                "normale, le rayon arrive perpendiculairement à la "
                "surface, i1 vaut zéro, et le rayon repart sur lui-même. "
                "En incidence rasante, le rayon arrive presque "
                "parallèlement à la surface, i1 tend vers quatre-vingt-dix "
                "degrés. Notons aussi la différence entre une surface "
                "lisse et polie, qui donne une réflexion spéculaire où des "
                "rayons parallèles restent parallèles, et une surface "
                "rugueuse, qui provoque une diffusion : les rayons "
                "repartent dans toutes les directions."
            )
        ) as tracker:
            self.play(Create(cas1_schema), Write(cas1_label))
            self.play(Create(cas2_schema), Write(cas2_label))
            self.play(FadeIn(texte_diffusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_groupe), FadeOut(texte_diffusion))

        # --- Exemple résolu 1 -----------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un rayon arrive sur un miroir avec un angle de 50°", font_size=20),
                Text("mesuré PAR RAPPORT À LA SURFACE. Trouver i1, i'1", font_size=20),
                Text("et l'angle entre rayon incident et rayon réfléchi.", font_size=20),
                MathTex(r"i_1 = 90^\circ - 50^\circ = 40^\circ \qquad i_1' = i_1 = 40^\circ", font_size=24, color=YELLOW),
                MathTex(r"\text{angle (incident, réfléchi)} = i_1 + i_1' = 80^\circ", font_size=24, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.22),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. Un rayon arrive sur un miroir avec un "
                "angle de cinquante degrés mesuré par rapport à la "
                "surface, et non par rapport à la normale. Attention à ce "
                "piège classique : il faut d'abord convertir. L'angle "
                "d'incidence, mesuré depuis la normale, vaut donc "
                "quatre-vingt-dix moins cinquante, soit quarante degrés. "
                "Par la loi de la réflexion, l'angle de réflexion i'1 vaut "
                "aussi quarante degrés. L'angle total entre le rayon "
                "incident et le rayon réfléchi vaut la somme des deux, "
                "soit quatre-vingts degrés."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Rayon incident, normale et rayon réfléchi sont coplanaires.", font_size=20),
                MathTex(r"i_1' = i_1", font_size=28),
                Text("Spéculaire (surface lisse) vs diffusion (surface rugueuse).", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le rayon incident, la normale et "
                "le rayon réfléchi sont toujours coplanaires, et l'angle "
                "de réflexion est toujours égal à l'angle d'incidence. "
                "Une surface lisse donne une réflexion spéculaire, une "
                "surface rugueuse donne une diffusion."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Vérifier si l'angle donné est mesuré par rapport à la", font_size=20),
                Text("   SURFACE ou par rapport à la NORMALE : ce n'est jamais", font_size=20),
                Text("   la même valeur (elles sont complémentaires à 90°).", font_size=20),
                Text("• Les lois de Snell-Descartes utilisent toujours l'angle", font_size=20),
                Text("   par rapport à la normale.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : toujours vérifier si l'angle donné dans "
                "un énoncé est mesuré par rapport à la surface ou par "
                "rapport à la normale, car ce n'est jamais la même valeur, "
                "elles sont complémentaires à quatre-vingt-dix degrés. Les "
                "lois de Snell-Descartes s'appliquent toujours à l'angle "
                "mesuré depuis la normale."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
