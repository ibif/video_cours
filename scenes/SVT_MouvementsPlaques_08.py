"""
scenes/SVT_MouvementsPlaques_08.py — Chapitre 7 (1ereD, SVT), scène 08.

§ 7.4 Les manifestations des mouvements des plaques : séismes (foyer,
épicentre, répartition en ceintures), volcanisme (divergence vs
subduction), remarque sur les points chauds, formation des reliefs,
exemple du Japon comparé à la Côte d'Ivoire.
Source : 1ereD/SVT.pdf, pages 97-98.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


def _schema_foyer_epicentre():
    """Foyer en profondeur, épicentre en surface, ondes concentriques."""
    surface = Line(LEFT * 3.0, RIGHT * 3.0, color=WHITE, stroke_width=2)
    surface.move_to(UP * 1.0)

    foyer = Dot(point=[0, -0.6, 0], radius=0.09, color=RED)
    label_foyer = Text("foyer", font_size=15, color=RED)
    label_foyer.next_to(foyer, DOWN, buff=0.15)

    epicentre = Dot(point=[0, 1.0, 0], radius=0.08, color=YELLOW)
    label_epicentre = Text("épicentre", font_size=15, color=YELLOW)
    label_epicentre.next_to(epicentre, UP, buff=0.15)

    verticale = Line(foyer.get_center(), epicentre.get_center(), color=YELLOW, stroke_width=1.5)

    return VGroup(surface, foyer, label_foyer, epicentre, label_epicentre, verticale)


class ManifestationsMouvementsPlaques(NotionScene):
    def construct(self):
        titre = scene_title("7.4 — Les manifestations des mouvements")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : séisme, foyer, épicentre --------------------------------
        definition_seisme = definition_box(
            Text(
                _wrap(
                    "Un séisme est une vibration brutale du sol par rupture de "
                    "roches en profondeur quand les contraintes dépassent leur "
                    "résistance. Foyer = point de rupture ; épicentre = point "
                    "de surface à la verticale du foyer.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition_seisme.next_to(titre, DOWN, buff=0.5)

        schema_foyer = _schema_foyer_epicentre()
        schema_foyer.next_to(definition_seisme, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les mouvements des plaques se manifestent en surface de "
                "trois façons : les séismes, le volcanisme et les reliefs. "
                "Un séisme est une vibration brutale du sol, causée par la "
                "rupture de roches en profondeur, lorsque les contraintes "
                "accumulées dépassent leur résistance. Le foyer est le "
                "point de rupture, en profondeur ; l'épicentre est le point "
                "de surface situé exactement à la verticale du foyer."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_seisme))
            self.play(FadeIn(schema_foyer))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_seisme), FadeOut(schema_foyer))

        propriete_repartition = property_box(
            Text(
                _wrap(
                    "La carte des séismes n'est pas uniforme : les épicentres "
                    "dessinent des ceintures étroites coïncidant avec les "
                    "limites de plaques. L'intérieur des grandes plaques est "
                    "calme. Le long des subductions, les foyers sont de plus "
                    "en plus profonds (jusqu'à ~700 km) en s'éloignant de la "
                    "fosse.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        propriete_repartition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La carte mondiale des séismes n'est pas du tout uniforme : "
                "les épicentres dessinent des ceintures étroites, qui "
                "coïncident exactement avec les limites de plaques. "
                "L'intérieur des grandes plaques, lui, reste calme. Le long "
                "des zones de subduction, les foyers deviennent de plus en "
                "plus profonds, jusqu'à environ sept cents kilomètres, à "
                "mesure que l'on s'éloigne de la fosse."
            )
        ) as tracker:
            self.play(FadeIn(propriete_repartition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_repartition))

        # --- Animation du raisonnement : volcanisme, deux visages --------------
        entete_volc = Text("Le volcanisme : deux visages", font_size=25, color=YELLOW, weight="BOLD")
        entete_volc.next_to(titre, DOWN, buff=0.5)

        volc_bullets = _bullets(
            [
                "Volcanisme de divergence (dorsales, rifts) : laves "
                "basaltiques fluides, éruptions calmes (Islande, rift "
                "est-africain).",
                "Volcanisme de subduction : laves épaisses (andésites), "
                "éruptions explosives dangereuses (ceinture de feu du "
                "Pacifique).",
            ],
            font_size=22,
            width=52,
        )
        volc_bullets.next_to(entete_volc, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le volcanisme, lui, suit également les limites de "
                "plaques, mais avec deux visages bien différents. Le "
                "volcanisme de divergence, aux dorsales et aux rifts, "
                "produit des laves basaltiques fluides et des éruptions "
                "calmes, comme en Islande ou dans le rift est-africain. Le "
                "volcanisme de subduction, lui, produit des laves épaisses, "
                "les andésites, et des éruptions explosives dangereuses : "
                "c'est la ceinture de feu du Pacifique."
            )
        ) as tracker:
            self.play(FadeIn(entete_volc))
            self.play(FadeIn(volc_bullets))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_volc), FadeOut(volc_bullets))

        remarque_points_chauds = warning_box(
            Text(
                _wrap(
                    "Quelques volcans existent loin de toute limite (Hawaï, au "
                    "milieu de la plaque pacifique) : ce sont des points "
                    "chauds, remontées localisées de matériau très chaud "
                    "depuis le manteau profond. Ils ne remettent pas en cause "
                    "la théorie.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        remarque_points_chauds.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une exception vient confirmer la règle : quelques volcans "
                "existent loin de toute limite de plaque, comme à Hawaï, au "
                "beau milieu de la plaque pacifique. On les appelle des "
                "points chauds : ce sont des remontées localisées de "
                "matériau très chaud, provenant du manteau profond. Ils ne "
                "remettent absolument pas en cause la théorie de la "
                "tectonique des plaques."
            )
        ) as tracker:
            self.play(FadeIn(remarque_points_chauds))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_points_chauds))

        # --- Reliefs : rapide synthèse -----------------------------------------
        entete_relief = Text("La formation des reliefs", font_size=25, color=YELLOW, weight="BOLD")
        entete_relief.next_to(titre, DOWN, buff=0.5)
        relief_bullets = _bullets(
            [
                "Dorsales et fosses océaniques.",
                "Rifts continentaux.",
                "Arcs volcaniques (subduction).",
                "Chaînes de montagnes (collision).",
            ],
            font_size=22,
            width=52,
        )
        relief_bullets.next_to(entete_relief, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Enfin, les mouvements des plaques sculptent les grands "
                "reliefs du globe : les dorsales et les fosses océaniques, "
                "les rifts continentaux, les arcs volcaniques des zones de "
                "subduction, et les chaînes de montagnes issues des "
                "collisions. La topographie que nous observons est "
                "l'expression visible, en surface, de cette machine "
                "interne du globe."
            )
        ) as tracker:
            self.play(FadeIn(entete_relief))
            self.play(FadeIn(relief_bullets))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_relief), FadeOut(relief_bullets))

        # --- À retenir : exemple Japon vs Côte d'Ivoire -------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Le Japon est à la jonction de plusieurs plaques (plaque "
                    "pacifique en subduction sous l'Asie) ; la Côte d'Ivoire "
                    "est à l'intérieur de la plaque africaine. Aux limites "
                    "convergentes, contraintes et fusion → séismes et volcans "
                    "japonais. À l'intérieur d'une plaque, pas de contrainte "
                    "concentrée : la Côte d'Ivoire est épargnée.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi le Japon tremble-t-il, et pas la Côte d'Ivoire ? "
                "Le Japon se trouve à la jonction de plusieurs plaques, "
                "avec la plaque pacifique en subduction sous l'Asie ; la "
                "Côte d'Ivoire, elle, se trouve bien à l'intérieur de la "
                "plaque africaine. Aux limites convergentes, les fortes "
                "contraintes et la fusion des roches provoquent séismes et "
                "volcans japonais. À l'intérieur d'une plaque, au contraire, "
                "il n'y a pas de contrainte concentrée : voilà pourquoi la "
                "Côte d'Ivoire est épargnée."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(exemple))
