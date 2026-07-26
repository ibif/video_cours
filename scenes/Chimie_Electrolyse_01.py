"""
scenes/Chimie_Electrolyse_01.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 01.

§ 1. Le phénomène d'électrolyse : expérience de découverte. Électrolyse
d'une solution de chlorure d'étain II (SnCl₂) entre deux électrodes de
graphite reliées à un générateur de tension continue réglable : pour
U < 1,4 V, rien ne se produit (pas de courant notable) ; pour U > 1,4 V,
un courant s'établit et l'on observe un dépôt gris d'étain métallique sur
une électrode et un dégagement de dichlore (odeur piquante, décoloration
du papier indigo) sur l'autre. Introduction de la tension de seuil et des
notions d'électrolyse et d'électrolyte.
Source : 1ereC/Chimie.pdf, chapitre 14, pages 134-135.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    LIGHT_GRAY,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_experience(depot=False, gaz=False):
    """Cuve à électrolyse (SnCl₂) avec deux électrodes de graphite reliées
    à un générateur de tension continue, construit uniquement avec des
    primitives Manim de base (Line, Rectangle, Circle, Arrow, VGroup)."""
    largeur, hauteur = 3.0, 1.9
    cuve = Rectangle(width=largeur, height=hauteur, color=LIGHT_GRAY, stroke_width=3)
    cuve.move_to([0, -0.9, 0])

    solution = Rectangle(width=largeur - 0.1, height=hauteur - 0.3, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
    solution.move_to(cuve.get_bottom() + UP * (hauteur - 0.3) / 2 + UP * 0.1)
    label_sol = Text("SnCl₂ (aq)", font_size=15, color=WHITE)
    label_sol.move_to(cuve.get_bottom() + UP * 0.3)

    electrode_g = Rectangle(width=0.22, height=hauteur + 0.5, fill_color=GRAY, fill_opacity=0.95, stroke_width=1)
    electrode_g.move_to(cuve.get_center() + LEFT * 0.9 + UP * 0.35)
    electrode_d = Rectangle(width=0.22, height=hauteur + 0.5, fill_color=GRAY, fill_opacity=0.95, stroke_width=1)
    electrode_d.move_to(cuve.get_center() + RIGHT * 0.9 + UP * 0.35)

    label_g = Text("graphite", font_size=13, color=WHITE)
    label_g.next_to(electrode_g, UP, buff=0.1)
    label_d = Text("graphite", font_size=13, color=WHITE)
    label_d.next_to(electrode_d, UP, buff=0.1)

    depot_gris = VGroup()
    if depot:
        for i in range(4):
            point = Circle(radius=0.045, fill_color=WHITE, fill_opacity=1, stroke_width=0)
            point.move_to(electrode_g.get_center() + [0.13, -0.55 + i * 0.25, 0])
            depot_gris.add(point)

    bulles = VGroup()
    if gaz:
        for i in range(5):
            b = Circle(radius=0.06, color=YELLOW, stroke_width=1.5)
            b.move_to(electrode_d.get_center() + [0.15 + 0.05 * (i % 2), -0.5 + i * 0.3, 0])
            bulles.add(b)

    # Générateur (symbole pile : longue barre fine = pôle +, courte barre
    # épaisse = pôle -) relié aux deux électrodes par des fils.
    barre_longue = Line([-0.18, 2.3, 0], [-0.18, 2.7, 0], color=WHITE, stroke_width=2)
    barre_courte = Line([0.18, 2.35, 0], [0.18, 2.65, 0], color=WHITE, stroke_width=6)
    generateur = VGroup(barre_longue, barre_courte)
    label_plus = Text("+", font_size=20, color=RED, weight="BOLD")
    label_plus.next_to(barre_longue, UP, buff=0.08)
    label_moins = Text("−", font_size=20, color=BLUE, weight="BOLD")
    label_moins.next_to(barre_courte, UP, buff=0.08)

    fil_g = Line(electrode_g.get_top(), [-0.18, 2.5, 0], color=YELLOW, stroke_width=2)
    fil_d = Line(electrode_d.get_top(), [0.18, 2.5, 0], color=YELLOW, stroke_width=2)

    return VGroup(
        cuve, solution, label_sol,
        electrode_g, electrode_d, label_g, label_d,
        depot_gris, bulles,
        generateur, label_plus, label_moins, fil_g, fil_d,
    )


class PhenomeneElectrolyseDecouverte(NotionScene):
    def construct(self):
        titre = scene_title("14.1 Le phénomène d'électrolyse : expérience de découverte")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : le protocole -----------------------------------------------
        schema = _schema_experience()
        schema.scale(1.0)
        schema.next_to(titre, DOWN, buff=0.5).shift(LEFT * 3.1)

        protocole = Text(
            _wrap(
                "On plonge deux électrodes de graphite dans une solution "
                "de chlorure d'étain II, et on les relie à un générateur "
                "de tension continue réglable.",
                width=34,
            ),
            font_size=21,
            color=WHITE,
        )
        protocole.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Découvrons un nouveau phénomène. On plonge deux "
                "électrodes de graphite, un matériau conducteur mais "
                "chimiquement inerte, dans une solution de chlorure "
                "d'étain deux, et on les relie à un générateur de tension "
                "continue dont on peut régler la valeur. Que va-t-il se "
                "passer selon la tension appliquée ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(schema))
            self.play(FadeIn(protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(protocole))

        # --- Raisonnement : U < 1,4 V puis U > 1,4 V -----------------------------
        entete_seuil = Text("On augmente progressivement la tension U", font_size=22, color=YELLOW, weight="BOLD")
        entete_seuil.next_to(titre, DOWN, buff=0.35)

        cas_faible = VGroup(
            MathTex(r"U < 1{,}4\ V", font_size=30, color=WHITE),
            Text("→ aucun courant notable, rien ne se produit", font_size=20, color=GRAY),
        ).arrange(DOWN, buff=0.2)

        cas_fort = VGroup(
            MathTex(r"U > 1{,}4\ V", font_size=30, color=WHITE),
            Text("→ un courant s'établit : dépôt gris d'étain sur une", font_size=20, color=GREEN),
            Text("électrode, dégagement de dichlore sur l'autre", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.2)

        cas = VGroup(cas_faible, cas_fort).arrange(DOWN, buff=0.5)
        cas.next_to(entete_seuil, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Si l'on augmente progressivement la tension U aux bornes "
                "du générateur, on constate ceci. Tant que U reste "
                "inférieure à un virgule quatre volt, rien ne se produit : "
                "aucun courant notable ne circule, malgré la tension "
                "appliquée. Mais dès que U dépasse un virgule quatre "
                "volt, un courant s'établit brusquement, et l'on observe "
                "un dépôt gris d'étain métallique sur une électrode, ainsi "
                "qu'un dégagement gazeux de dichlore, reconnaissable à son "
                "odeur piquante, sur l'autre électrode."
            )
        ) as tracker:
            self.play(FadeIn(entete_seuil))
            self.play(Write(cas_faible))
            self.play(Write(cas_fort))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_seuil), FadeOut(cas))

        # --- Exemple traité : observation finale (schéma avec dépôt + gaz) -------
        schema_final = _schema_experience(depot=True, gaz=True)
        schema_final.next_to(titre, DOWN, buff=0.5).shift(LEFT * 3.1)

        observations = _bullets(
            [
                "dépôt gris métallique (étain, Sn) sur l'électrode reliée "
                "au pôle négatif du générateur ;",
                "bulles de gaz jaune-vert (dichlore, Cl₂) sur l'électrode "
                "reliée au pôle positif ;",
                "ce seuil de 1,4 V est une TENSION DE SEUIL, en dessous de "
                "laquelle la transformation ne peut pas démarrer.",
            ],
            width=36,
        )
        observations.next_to(schema_final, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Regardons ce montage final de plus près. Un dépôt gris "
                "métallique d'étain apparaît sur l'électrode reliée au "
                "pôle négatif du générateur. Des bulles de gaz jaune-vert "
                "de dichlore se dégagent sur l'électrode reliée au pôle "
                "positif. Cette valeur de un virgule quatre volt est ce "
                "qu'on appelle une tension de seuil : en dessous de cette "
                "tension, la transformation chimique ne peut tout "
                "simplement pas démarrer, quel que soit le temps "
                "d'attente."
            )
        ) as tracker:
            self.play(FadeIn(schema_final))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_final), FadeOut(observations))

        # --- À retenir : définitions -------------------------------------------
        def_electrolyse = definition_box(
            Text(
                _wrap(
                    "Une électrolyse est une transformation chimique forcée, "
                    "provoquée par le passage d'un courant électrique imposé "
                    "par un générateur, et qui ne se produit pas "
                    "spontanément.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        def_electrolyse.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons deux définitions essentielles. Une électrolyse "
                "est une transformation chimique forcée, provoquée par le "
                "passage d'un courant électrique imposé par un générateur : "
                "sans ce courant, la transformation ne se produit "
                "spontanément."
            )
        ) as tracker:
            self.play(FadeIn(def_electrolyse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_electrolyse))

        def_electrolyte = definition_box(
            Text(
                _wrap(
                    "Un électrolyte est une solution (ou un liquide) "
                    "contenant des ions mobiles, capable de conduire le "
                    "courant électrique : c'est le milieu dans lequel se "
                    "déroule l'électrolyse.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        def_electrolyte.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un électrolyte, quant à lui, est une solution, ou un "
                "liquide, contenant des ions mobiles, capable de conduire "
                "le courant électrique : c'est le milieu dans lequel se "
                "déroule toute électrolyse. Dans notre expérience, "
                "l'électrolyte est la solution aqueuse de chlorure "
                "d'étain deux."
            )
        ) as tracker:
            self.play(FadeIn(def_electrolyte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_electrolyte), FadeOut(titre))
