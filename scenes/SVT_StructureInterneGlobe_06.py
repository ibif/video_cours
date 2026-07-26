"""
scenes/SVT_StructureInterneGlobe_06.py — Chapitre 7 (1ereC, SVT), scène 06.

§ II.3 Réflexion et réfraction des ondes sismiques (définition discontinuité
sismique) + propriété fondamentale (la vitesse augmente avec la
profondeur, changement brutal = discontinuité) + les zones d'ombre (schéma
de la propagation avec stations A/B/C, ondes S stoppées par le noyau
liquide, ondes P réfractées). Source : 1ereC/SVT.pdf, page 72-73.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
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


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ReflexionRefractionEtZonesOmbre(NotionScene):
    def construct(self):
        titre = scene_title("II.3 — Réflexion, réfraction et zones d'ombre")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : que se passe-t-il à la frontière de deux milieux ? -----
        intro = Text(
            _wrap(
                "Comme la lumière dans l'eau, une onde sismique change de "
                "comportement lorsqu'elle rencontre une surface séparant "
                "deux milieux de propriétés différentes.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Comme la lumière qui change de trajectoire en entrant dans "
                "l'eau, une onde sismique change de comportement lorsqu'elle "
                "rencontre une surface séparant deux milieux de propriétés "
                "différentes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définitions : réflexion, réfraction, discontinuité --------------
        definition = definition_box(
            Text(
                _wrap(
                    "Réflexion : une partie de l'énergie repart dans le "
                    "milieu d'origine (comme un écho). Réfraction : une "
                    "partie est transmise dans le second milieu avec un "
                    "changement de direction, car sa vitesse change "
                    "(lois de Snell-Descartes). Discontinuité sismique : "
                    "surface séparant deux enveloppes de propriétés "
                    "nettement différentes.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Lorsqu'une onde sismique rencontre une surface séparant "
                "deux milieux de propriétés différentes, deux phénomènes se "
                "combinent. La réflexion : une partie de son énergie repart "
                "dans le milieu d'origine, comme un écho. La réfraction : "
                "une partie est transmise dans le second milieu avec un "
                "changement de direction, car sa vitesse change, comme le "
                "décrivent les lois de Snell-Descartes. Une discontinuité "
                "sismique est une surface de l'intérieur du globe séparant "
                "deux enveloppes de propriétés physiques nettement "
                "différentes."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Propriété fondamentale -------------------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "La vitesse des ondes sismiques augmente globalement "
                    "avec la profondeur (croissance de la densité et de la "
                    "rigidité). Tout changement BRUTAL de vitesse traduit "
                    "une discontinuité, c'est-à-dire une surface de "
                    "séparation entre deux enveloppes de nature différente.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Propriété fondamentale à retenir : la vitesse des ondes "
                "sismiques augmente globalement avec la profondeur, du fait "
                "de la croissance de la densité et de la rigidité des "
                "roches. Mais tout changement brutal de cette vitesse "
                "traduit une discontinuité, c'est-à-dire une surface de "
                "séparation entre deux enveloppes de nature différente."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Animation du raisonnement : schéma des zones d'ombre -------------
        globe = Circle(radius=2.0, color="#595959", fill_color="#2B2B2B", fill_opacity=1.0)
        noyau_liquide = Circle(radius=0.85, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
        noyau_liquide.move_to(globe.get_center())

        foyer = Dot(globe.point_at_angle(1.5708), color=RED, radius=0.07)
        label_foyer = Text("Foyer", font_size=14, color=RED).next_to(foyer, UP, buff=0.1)

        station_a = Dot(globe.point_at_angle(1.9), color=YELLOW, radius=0.06)
        label_a = Text("A (proche)", font_size=13, color=YELLOW).next_to(station_a, UP, buff=0.1)
        onde_a = Line(foyer.get_center(), station_a.get_center(), color=YELLOW, stroke_width=2)
        note_a = Text("P et S directes reçues", font_size=12, color=YELLOW)
        note_a.next_to(station_a, RIGHT, buff=0.15).shift(UP * 0.15)

        station_b = Dot(globe.point_at_angle(3.6), color="#FF6B6B", radius=0.06)
        label_b = Text("B (zone d'ombre)", font_size=13, color="#FF6B6B").next_to(station_b, DOWN, buff=0.1)
        onde_b_bloquee = Line(foyer.get_center(), noyau_liquide.get_boundary_point(RIGHT), color="#FF6B6B", stroke_width=2)
        note_b = Text("Aucune onde directe", font_size=12, color="#FF6B6B")
        note_b.next_to(station_b, DOWN, buff=0.35)

        station_c = Dot(globe.point_at_angle(4.8), color="#4DABF7", radius=0.06)
        label_c = Text("C (lointaine)", font_size=13, color="#4DABF7").next_to(station_c, DOWN, buff=0.1)
        onde_c1 = Line(foyer.get_center(), noyau_liquide.get_boundary_point(DOWN), color="#4DABF7", stroke_width=2)
        onde_c2 = Line(noyau_liquide.get_boundary_point(DOWN), station_c.get_center(), color="#4DABF7", stroke_width=2)
        note_c = Text("Seule P réfractée reçue", font_size=12, color="#4DABF7")
        note_c.next_to(station_c, LEFT, buff=0.15).shift(DOWN * 0.2)

        schema = VGroup(
            globe, noyau_liquide, foyer, label_foyer,
            station_a, label_a, onde_a, note_a,
            station_b, label_b, onde_b_bloquee, note_b,
            station_c, label_c, onde_c1, onde_c2, note_c,
        )
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le mécanisme des zones d'ombre. Le foyer émet des "
                "ondes P et S dans toutes les directions. À la station A, "
                "proche, les ondes P et S directes sont toutes deux reçues "
                "normalement. Mais en s'éloignant, un noyau liquide se "
                "trouve sur le trajet des ondes : à la station B, dans la "
                "zone d'ombre, aucune onde directe n'arrive, ni P ni S, car "
                "la trajectoire est bloquée ou déviée. À la station C, plus "
                "lointaine encore, seule une onde P réfractée par le noyau "
                "parvient à être reçue : elle a changé de direction en "
                "traversant le milieu liquide."
            )
        ) as tracker:
            self.play(FadeIn(globe), FadeIn(noyau_liquide), FadeIn(foyer), FadeIn(label_foyer))
            self.play(FadeIn(station_a), FadeIn(label_a), FadeIn(onde_a), FadeIn(note_a))
            self.play(FadeIn(station_b), FadeIn(label_b), FadeIn(onde_b_bloquee), FadeIn(note_b))
            self.play(FadeIn(station_c), FadeIn(label_c), FadeIn(onde_c1), FadeIn(onde_c2), FadeIn(note_c))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : interpréter les enregistrements des 3 stations -
        exemple = example_box(
            Text(
                _wrap(
                    "La station A enregistre des ondes P et S. La station B "
                    "n'enregistre RIEN en onde directe. La station C "
                    "n'enregistre que des ondes P (réfractées, en retard). "
                    "Que peut-on en conclure sur l'intérieur du globe ?",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : la station A enregistre des ondes P et S. "
                "La station B n'enregistre rien en onde directe. La station "
                "C n'enregistre que des ondes P, réfractées et en retard. "
                "Que peut-on en conclure sur l'intérieur du globe ? "
                "L'absence totale d'ondes à la station B et la présence "
                "d'ondes P seules, déviées, à la station C, indiquent qu'un "
                "obstacle profond bloque les ondes S et dévie fortement les "
                "ondes P : c'est la signature d'un noyau qui se comporte "
                "comme un liquide."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Discontinuité = changement BRUTAL de vitesse des ondes (réflexion, réfraction, disparition).",
                "La vitesse augmente globalement avec la profondeur.",
                "Zone d'ombre = région où aucune onde directe n'arrive, révélant un obstacle profond.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : une discontinuité correspond à un changement "
                "brutal de la vitesse des ondes, par réflexion, réfraction "
                "ou disparition. La vitesse augmente globalement avec la "
                "profondeur. Et une zone d'ombre est une région où aucune "
                "onde directe n'arrive, ce qui révèle un obstacle profond "
                "dans la structure du globe."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Une « zone d'ombre » sismique ne signifie pas « zone "
                    "sans risque de séisme » : c'est seulement une région où "
                    "aucune onde DIRECTE issue d'un foyer donné n'arrive, à "
                    "cause d'un obstacle profond sur le trajet des ondes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : une zone d'ombre sismique ne "
                "signifie absolument pas une zone sans risque de séisme. "
                "C'est seulement une région où aucune onde directe issue "
                "d'un foyer donné n'arrive, à cause d'un obstacle profond "
                "sur le trajet des ondes, comme le noyau liquide."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
