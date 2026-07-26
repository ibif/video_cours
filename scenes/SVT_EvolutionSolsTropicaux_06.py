"""
scenes/SVT_EvolutionSolsTropicaux_06.py — Chapitre 9 (1ereD, SVT), scène 06.

§ 9.5.1-9.5.2 Le lessivage (éluviation/illuviation) et la ferralitisation —
définitions, les 5 étapes détaillées de la ferralitisation, le
cuirassement / la latérite. Source : 1ereD/SVT.pdf, pages 121-123.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    ORANGE,
    Arrow,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LessivageEtFerralitisation(NotionScene):
    def construct(self):
        titre = scene_title("9.5 — Lessivage et ferralitisation")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : définition du lessivage ---------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le lessivage : entraînement vers le bas, par l'eau, "
                    "des particules fines (argiles) et des éléments "
                    "solubles (Ca, Mg, K, Na, silice). Le départ depuis "
                    "l'horizon supérieur = éluviation ; le dépôt plus bas = "
                    "illuviation. D'autant plus intense que pluies "
                    "abondantes et températures élevées : cause profonde "
                    "de l'appauvrissement naturel des sols tropicaux.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le lessivage est l'entraînement, vers le bas, par l'eau, "
                "des particules fines comme les argiles, et des éléments "
                "solubles, calcium, magnésium, potassium, sodium, silice. "
                "Le départ de ces éléments depuis l'horizon supérieur "
                "s'appelle l'éluviation ; leur dépôt plus bas s'appelle "
                "l'illuviation. Ce processus est d'autant plus intense que "
                "les pluies sont abondantes et les températures élevées : "
                "c'est la cause profonde de l'appauvrissement naturel des "
                "sols tropicaux."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma éluviation/illuviation ------
        entete_schema = Text("Éluviation et illuviation", font_size=25, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.4)

        horizon_a = Rectangle(width=2.6, height=0.9, fill_color="#5B3A29", fill_opacity=1.0, stroke_color=WHITE)
        horizon_b = Rectangle(width=2.6, height=0.9, fill_color="#B5451B", fill_opacity=1.0, stroke_color=WHITE)
        pile = VGroup(horizon_a, horizon_b).arrange(DOWN, buff=0)
        label_a = Text("A (éluviation :\ndépart)", font_size=17, color=WHITE)
        label_a.next_to(horizon_a, LEFT, buff=0.3)
        label_b = Text("B (illuviation :\ndépôt)", font_size=17, color=WHITE)
        label_b.next_to(horizon_b, LEFT, buff=0.3)
        fleche = Arrow(
            horizon_a.get_bottom() + [0.6, 0.3, 0],
            horizon_b.get_top() + [0.6, -0.15, 0],
            color=YELLOW,
            stroke_width=4,
            buff=0,
        )
        label_fleche = Text("argiles, Ca, Mg, K, Na, silice", font_size=15, color=YELLOW)
        label_fleche.next_to(fleche, RIGHT, buff=0.2)

        schema = VGroup(pile, label_a, label_b, fleche, label_fleche)
        schema.next_to(entete_schema, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Sur ce schéma, l'horizon A perd ses particules fines et "
                "ses éléments solubles, entraînés par l'eau qui percole : "
                "c'est l'éluviation. Ces éléments, argiles, calcium, "
                "magnésium, potassium, sodium, silice, se déposent plus "
                "bas, dans l'horizon B : c'est l'illuviation. À force de "
                "lessivage, l'horizon A s'appauvrit tandis que l'horizon B "
                "s'enrichit."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(pile), FadeIn(label_a), FadeIn(label_b))
            self.play(FadeIn(fleche), FadeIn(label_fleche))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(schema))

        # --- Exemple traité : la ferralitisation en 5 étapes -------------------
        ferralitisation_def = definition_box(
            Text(
                _wrap(
                    "La ferralitisation : processus d'évolution sous "
                    "climat tropical humide. Hydrolyse intense des "
                    "minéraux ; lessivage presque total des bases (Ca, Mg, "
                    "K, Na) et d'une grande partie de la silice ; "
                    "accumulation résiduelle des oxydes de fer (Fe2O3) et "
                    "d'aluminium (Al2O3), qui colorent en rouge/ocre ; "
                    "formation d'argile kaolinite.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        ferralitisation_def.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le processus dominant en zone forestière humide est la "
                "ferralitisation. Sous climat tropical humide, l'hydrolyse "
                "des minéraux est intense ; le lessivage emporte presque "
                "toutes les bases, calcium, magnésium, potassium, sodium, "
                "et une grande partie de la silice ; les oxydes de fer et "
                "d'aluminium, peu solubles, s'accumulent et colorent le sol "
                "en rouge ou en ocre ; il se forme surtout de l'argile "
                "kaolinite."
            )
        ) as tracker:
            self.play(FadeIn(ferralitisation_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ferralitisation_def))

        entete_etapes = Text("Les 5 étapes de la ferralitisation", font_size=24, color=YELLOW, weight="BOLD")
        entete_etapes.next_to(titre, DOWN, buff=0.4)

        etapes = _bullets(
            [
                "Chaleur + eau acidulée hydrolysent les silicates.",
                "Les bases sont lessivées en premier, puis une partie de la silice.",
                "Fer et aluminium, peu solubles, restent et s'oxydent : sol rouge/ocre.",
                "L'argile dominante est la kaolinite, qui retient mal les nutriments.",
                "Si l'horizon B est exposé en surface (érosion de A) et subit l'alternance humectation-dessiccation, il durcit irréversiblement en cuirasse latéritique.",
            ],
            font_size=19,
            width=52,
        )
        etapes.next_to(entete_etapes, DOWN, buff=0.35)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = etapes.get_top()[1] - _bas_visible
        if etapes.height > _hauteur_dispo:
            etapes.scale(_hauteur_dispo / etapes.height, about_point=etapes.get_top())

        with self.voiceover(
            text=(
                "Détaillons les cinq étapes de la ferralitisation. Un, la "
                "chaleur et l'eau acidulée hydrolysent les silicates. Deux, "
                "les bases sont lessivées en premier, puis une partie de la "
                "silice. Trois, le fer et l'aluminium, peu solubles, "
                "restent sur place et s'oxydent : c'est l'enrichissement "
                "résiduel, qui donne le sol rouge ou ocre. Quatre, "
                "l'argile dominante qui se forme est la kaolinite, qui "
                "retient mal les nutriments. Cinq, si l'horizon B, riche en "
                "fer, se retrouve exposé en surface, par exemple après "
                "l'érosion de l'horizon A, et subit l'alternance "
                "d'humectation et de dessiccation, il durcit "
                "irréversiblement en une carapace, la latérite ou cuirasse "
                "latéritique. Ce cuirassement est fréquent dans le Nord et "
                "le Centre de la Côte d'Ivoire."
            )
        ) as tracker:
            self.play(FadeIn(entete_etapes))
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_etapes), FadeOut(etapes))

        # --- À retenir : schéma du cuirassement --------------------------------
        entete_cuirasse = Text("Le cuirassement", font_size=25, color=YELLOW, weight="BOLD")
        entete_cuirasse.next_to(titre, DOWN, buff=0.45)

        sol_normal = Text("Horizon B enfoui\n→ reste meuble", font_size=18, color=WHITE)
        cuirasse_exposee = Rectangle(
            width=2.6, height=0.7, fill_color=ORANGE, fill_opacity=1.0, stroke_color=WHITE
        )
        label_cuirasse = Text("Horizon B exposé\n→ durcit en cuirasse", font_size=18, color=WHITE)
        label_cuirasse.next_to(cuirasse_exposee, DOWN, buff=0.2)
        groupe_cuirasse = VGroup(sol_normal, VGroup(cuirasse_exposee, label_cuirasse)).arrange(RIGHT, buff=1.2)
        groupe_cuirasse.next_to(entete_cuirasse, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : tant que l'horizon B riche en fer "
                "reste enfoui sous l'horizon A, il demeure meuble. Mais dès "
                "qu'il est mis à nu, par exemple après un défrichement qui "
                "expose le sol à l'érosion, l'alternance des saisons "
                "sèches et humides le fait durcir de façon irréversible en "
                "une cuirasse de latérite, impénétrable à la houe — comme "
                "la dalle observée par Ibrahim à Korhogo."
            )
        ) as tracker:
            self.play(FadeIn(entete_cuirasse))
            self.play(FadeIn(sol_normal))
            self.play(FadeIn(cuirasse_exposee), FadeIn(label_cuirasse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_cuirasse), FadeOut(groupe_cuirasse))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre lessivage et ferralitisation : le "
                    "lessivage est le transport des éléments par l'eau "
                    "(un mécanisme) ; la ferralitisation est le processus "
                    "global, propre au climat tropical humide, qui combine "
                    "hydrolyse intense, lessivage des bases et "
                    "accumulation résiduelle du fer et de l'aluminium.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre lessivage et ferralitisation. "
                "Le lessivage est un mécanisme, le transport des éléments "
                "par l'eau. La ferralitisation est le processus global, "
                "propre au climat tropical humide, qui combine une "
                "hydrolyse intense, le lessivage des bases, et "
                "l'accumulation résiduelle du fer et de l'aluminium."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
