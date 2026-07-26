"""
scenes/Chimie_Benzene_03.py — Chapitre 4 (1ereC, Chimie), scène 03.

§ Les structures de Kekulé : cyclohexa-1,3,5-triène, les deux formes
mésomères équivalentes (hexagone à 3 doubles liaisons alternées), la
flèche de résonance ↔, et l'hybride de résonance (hexagone + cercle).
Schéma construit avec des primitives Manim de base uniquement (Line, Dot,
VGroup, Polygon) — aucune bibliothèque de chimie.
Source : 1ereC/Chimie.pdf, chapitre 4, page 37.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    ORIGIN,
    PI,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Circle,
    Dot,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _hex_vertices(center, radius=1.2, start_angle=PI / 2):
    pts = []
    for i in range(6):
        angle = start_angle + i * (PI / 3)
        pts.append(center + radius * np.array([np.cos(angle), np.sin(angle), 0.0]))
    return pts


def _kekule_hexagon(center, radius=1.2, double_positions=(0, 2, 4), color=WHITE):
    """Hexagone du cycle benzénique : 6 sommets = carbones, liaisons simples
    et doubles alternées selon `double_positions` (indices des côtés)."""
    vertices = _hex_vertices(center, radius)
    edges = VGroup()
    for i in range(6):
        p1, p2 = vertices[i], vertices[(i + 1) % 6]
        edges.add(Line(p1, p2, color=color, stroke_width=3))
        if i in double_positions:
            mid = (p1 + p2) / 2
            inward = (center - mid)
            inward = inward / np.linalg.norm(inward) * 0.16
            p1b = p1 + (p2 - p1) * 0.18 + inward
            p2b = p2 - (p2 - p1) * 0.18 + inward
            edges.add(Line(p1b, p2b, color=color, stroke_width=3))
    dots = VGroup(*[Dot(v, radius=0.055, color=color) for v in vertices])
    return VGroup(edges, dots)


def _hybride_hexagon(center, radius=1.2, color=YELLOW):
    """Hybride de résonance : hexagone à liaisons simples + cercle inscrit
    représentant la délocalisation des électrons π."""
    vertices = _hex_vertices(center, radius)
    edges = VGroup()
    for i in range(6):
        p1, p2 = vertices[i], vertices[(i + 1) % 6]
        edges.add(Line(p1, p2, color=color, stroke_width=3))
    dots = VGroup(*[Dot(v, radius=0.055, color=color) for v in vertices])
    cercle = Circle(radius=radius * 0.55, color=color, stroke_width=3).move_to(center)
    return VGroup(edges, dots, cercle)


class StructuresDeKekule(NotionScene):
    def construct(self):
        titre = scene_title("3. Les structures de Kekulé")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le cyclohexa-1,3,5-triène ---------------------------------
        enonce = Text(
            _wrap(
                "En 1865, le chimiste allemand Auguste Kekulé propose une "
                "première réponse : le benzène serait un cyclohexa-1,3,5-"
                "triène, un cycle à six carbones portant trois doubles "
                "liaisons alternées avec trois liaisons simples.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En dix-huit cent soixante-cinq, le chimiste allemand "
                "Auguste Kekulé propose une première réponse : le benzène "
                "serait un cyclohexa-un-trois-cinq-triène, c'est-à-dire un "
                "cycle à six carbones portant trois doubles liaisons "
                "alternées avec trois liaisons simples."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : les deux formes mésomères --------------
        entete = Text("Deux formes mésomères équivalentes", font_size=25, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        forme1 = _kekule_hexagon(LEFT * 3.3, double_positions=(0, 2, 4))
        forme2 = _kekule_hexagon(RIGHT * 3.3, double_positions=(1, 3, 5))
        fleche = MathTex(r"\longleftrightarrow", font_size=48, color=YELLOW)
        fleche.move_to((forme1.get_center() + forme2.get_center()) / 2)

        label1 = Text("forme 1", font_size=20, color=WHITE).next_to(forme1, DOWN, buff=0.3)
        label2 = Text("forme 2", font_size=20, color=WHITE).next_to(forme2, DOWN, buff=0.3)

        schema = VGroup(forme1, forme2, fleche, label1, label2)
        schema.next_to(entete, DOWN, buff=0.5)
        _fit(schema, entete.get_bottom()[1] - 0.4)

        groupe_schema = VGroup(entete, schema)

        with self.voiceover(
            text=(
                "Mais un problème se pose aussitôt : on peut placer les "
                "doubles liaisons de deux façons différentes, parfaitement "
                "équivalentes, selon qu'on les fait partir d'un sommet ou "
                "de l'autre. On obtient ainsi deux formes, dites "
                "mésomères, reliées par une flèche de résonance à deux "
                "pointes. Aucune des deux formes n'existe réellement "
                "isolément : ce ne sont que des représentations "
                "commodes, sur le papier, d'une seule et même molécule."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(forme1), FadeIn(label1))
            self.play(FadeIn(fleche))
            self.play(FadeIn(forme2), FadeIn(label2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : l'hybride de résonance -----------------------------
        entete2 = Text("L'hybride de résonance", font_size=25, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        hybride = _hybride_hexagon(ORIGIN, radius=1.4)
        label_h = Text("hexagone + cercle : représentation réelle", font_size=20, color=WHITE)
        label_h.next_to(hybride, DOWN, buff=0.35)
        groupe_hybride = VGroup(hybride, label_h)
        groupe_hybride.next_to(entete2, DOWN, buff=0.5)

        groupe3 = VGroup(entete2, groupe_hybride)

        with self.voiceover(
            text=(
                "La molécule réelle est donc un hybride de résonance : "
                "une structure unique, intermédiaire entre les deux "
                "formes de Kekulé, où les électrons ne sont associés à "
                "aucune liaison en particulier. On la représente "
                "classiquement par un hexagone portant un cercle "
                "inscrit, symbole du nuage électronique partagé par les "
                "six carbones."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(hybride))
            self.play(FadeIn(label_h))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe3))

        # --- À retenir ---------------------------------------------------------
        retenir = Text(
            _wrap(
                "À retenir : les formes de Kekulé sont deux écritures "
                "équivalentes d'une seule molécule ; la véritable "
                "structure du benzène est l'hybride de résonance "
                "(hexagone + cercle), qui explique pourquoi les 6 "
                "liaisons C–C sont identiques (140 pm).",
                width=50,
            ),
            font_size=24,
            color=WHITE,
        )
        retenir.next_to(titre, DOWN, buff=0.6)
        _fit(retenir, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : les formes de Kekulé sont deux "
                "écritures équivalentes d'une seule et même molécule. La "
                "véritable structure du benzène est l'hybride de "
                "résonance, représenté par un hexagone portant un cercle, "
                "et c'est cette structure unique qui explique pourquoi "
                "les six liaisons carbone-carbone sont toutes identiques, "
                "avec une longueur de cent quarante picomètres. Attention "
                "cependant : il ne faut jamais confondre l'hybride de "
                "résonance avec un mélange des deux formes de Kekulé — "
                "c'est une structure unique, pas une moyenne dans le "
                "temps."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
