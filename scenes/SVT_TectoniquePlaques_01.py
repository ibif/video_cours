"""
scenes/SVT_TectoniquePlaques_01.py — Chapitre 8 (1ereC, SVT), scène 01.

I. Le découpage de la lithosphère en plaques.
§A Rappel des enveloppes du globe (lithosphère/asthénosphère, définition de
la lithosphère) ; §B les plaques lithosphériques (définition, 7 grandes
plaques + plaques secondaires, remarques : une plaque peut porter
continent+océan, la Côte d'Ivoire repose sur la plaque africaine, les
limites ne coïncident pas avec les côtes) ; point clé méthode : les
plaques glissent sur l'asthénosphère, elles ne flottent pas sur un océan
de magma. Source : 1ereC/SVT.pdf, pages 84-85.
"""

import textwrap

from manim import (
    BLUE_D,
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class DecoupageLithosphereEnPlaques(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 8 — Les mouvements des plaques")
        titre.scale(0.62)
        titre.to_edge(UP)

        sous_titre = Text(
            "I. Le découpage de la lithosphère en plaques", font_size=27, color=YELLOW, weight="BOLD"
        )
        sous_titre.next_to(titre, DOWN, buff=0.45)

        self.play(Write(titre))
        self.play(FadeIn(sous_titre))

        # --- Énoncé : rappel des enveloppes du globe -----------------------
        rappel = Text(
            _wrap(
                "Rappel : la Terre est formée d'enveloppes concentriques "
                "(croûte, manteau, noyau). Du point de vue mécanique, on "
                "distingue la lithosphère, enveloppe externe rigide, et "
                "l'asthénosphère, en dessous, ductile et déformable.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        rappel.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Rappelons d'abord la structure du globe. La Terre est "
                "formée d'enveloppes concentriques : la croûte, le manteau "
                "et le noyau. Mais du point de vue de leur rigidité "
                "mécanique, on distingue plutôt deux couches : la "
                "lithosphère, l'enveloppe externe rigide, et "
                "l'asthénosphère, juste en dessous, une couche ductile, "
                "capable de se déformer très lentement."
            )
        ) as tracker:
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel))

        # --- Schéma : coupe lithosphère / asthénosphère ---------------------
        litho = Rectangle(width=8.0, height=0.9, fill_color=ORANGE, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1)
        astheno = Rectangle(width=8.0, height=1.6, fill_color=BLUE_D, fill_opacity=0.55, stroke_color=WHITE, stroke_width=1)
        astheno.next_to(litho, DOWN, buff=0)

        label_litho = Text("Lithosphère (rigide) : 80 à 150 km", font_size=20, color=WHITE)
        label_litho.move_to(litho.get_center())

        label_astheno = Text("Asthénosphère (ductile) : ~100-350 km", font_size=20, color=WHITE)
        label_astheno.move_to(astheno.get_center())

        coupe = VGroup(litho, astheno, label_litho, label_astheno)
        coupe.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La lithosphère comprend la croûte et la partie supérieure "
                "rigide du manteau ; elle est épaisse de quatre-vingts à "
                "cent cinquante kilomètres. Elle repose sur l'asthénosphère, "
                "partie du manteau supérieur, solide mais ductile, capable "
                "de s'écouler très lentement, sur des millions d'années."
            )
        ) as tracker:
            self.play(Create(litho), FadeIn(label_litho))
            self.play(Create(astheno), FadeIn(label_astheno))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coupe))

        definition_litho = definition_box(
            Text(
                _wrap(
                    "Lithosphère : enveloppe rigide externe du globe, "
                    "constituée de la croûte et de la partie supérieure "
                    "rigide du manteau (manteau lithosphérique). Elle "
                    "repose sur l'asthénosphère, zone ductile du manteau "
                    "supérieur sur laquelle elle peut glisser.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition_litho.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la définition : la lithosphère est l'enveloppe "
                "rigide externe du globe terrestre, constituée de la croûte "
                "et de la partie supérieure rigide du manteau. Elle repose "
                "sur l'asthénosphère, zone ductile du manteau supérieur, "
                "sur laquelle elle peut glisser."
            )
        ) as tracker:
            self.play(FadeIn(definition_litho))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_litho))

        # --- Animation du raisonnement : les plaques lithosphériques -------
        entete_plaques = Text("Les plaques lithosphériques", font_size=27, color=YELLOW, weight="BOLD")
        entete_plaques.next_to(sous_titre, DOWN, buff=0.5)

        morcellement = Text(
            _wrap(
                "La lithosphère n'est pas continue comme la coquille d'un "
                "œuf : elle est morcelée en une douzaine de fragments "
                "rigides, les plaques lithosphériques, séparées par des "
                "zones actives (séismes, volcans).",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        morcellement.next_to(entete_plaques, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La lithosphère n'est pas continue, comme le serait la "
                "coquille d'un œuf : elle est morcelée en une douzaine de "
                "fragments rigides, appelés plaques lithosphériques, "
                "séparés par des zones actives où se concentrent les "
                "séismes et les volcans."
            )
        ) as tracker:
            self.play(FadeIn(entete_plaques))
            self.play(FadeIn(morcellement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_plaques), FadeOut(morcellement))

        definition_plaque = definition_box(
            Text(
                _wrap(
                    "Plaque lithosphérique : fragment rigide de la "
                    "lithosphère, délimité par des zones actives (dorsales, "
                    "fosses océaniques, failles transformantes), qui se "
                    "déplace à la surface du globe à la vitesse de quelques "
                    "centimètres par an.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition_plaque.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une plaque lithosphérique est donc un fragment rigide de "
                "la lithosphère, délimité par des zones actives, dorsales, "
                "fosses océaniques ou failles transformantes, qui se "
                "déplace à la surface du globe à la vitesse de quelques "
                "centimètres par an."
            )
        ) as tracker:
            self.play(FadeIn(definition_plaque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_plaque))

        # --- Les 7 grandes plaques + plaques secondaires --------------------
        entete_liste = Text("Les grandes plaques", font_size=27, color=YELLOW, weight="BOLD")
        entete_liste.next_to(sous_titre, DOWN, buff=0.5)

        grandes = _bullets(
            [
                "7 grandes plaques : africaine, eurasiatique, pacifique, "
                "nord-américaine, sud-américaine, antarctique, "
                "australienne (indo-australienne).",
                "Plaques secondaires : Nazca, Cocos, caraïbe, arabique, "
                "des Philippines, de Scotia, etc.",
            ],
            font_size=22,
            width=52,
        )
        grandes.next_to(entete_liste, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On distingue sept grandes plaques : la plaque africaine, "
                "l'eurasiatique, la pacifique, la nord-américaine, la "
                "sud-américaine, l'antarctique et l'australienne, aussi "
                "appelée indo-australienne. À côté d'elles existent des "
                "plaques secondaires, plus petites, comme celles de Nazca, "
                "des Cocos, la plaque caraïbe, arabique, des Philippines ou "
                "de Scotia."
            )
        ) as tracker:
            self.play(FadeIn(entete_liste))
            self.play(FadeIn(grandes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_liste), FadeOut(grandes))

        # --- Exemple traité : la Côte d'Ivoire sur la plaque africaine -----
        remarques = warning_box(
            _bullets(
                [
                    "Une plaque peut porter un continent, un océan, ou les "
                    "deux : la plaque africaine porte l'Afrique et la "
                    "moitié orientale de l'Atlantique ; la plaque pacifique "
                    "est presque entièrement océanique.",
                    "La Côte d'Ivoire, comme tout le continent africain, "
                    "repose sur la plaque africaine.",
                    "Les limites des plaques ne coïncident pas avec les "
                    "côtes : elles passent au milieu des océans (dorsales) "
                    "ou le long de certaines côtes (fosses).",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.2,
        )
        remarques.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Trois remarques importantes. D'abord, une plaque peut "
                "porter un continent, un océan, ou les deux à la fois : la "
                "plaque africaine porte l'Afrique et la moitié orientale de "
                "l'océan Atlantique, tandis que la plaque pacifique est "
                "presque entièrement océanique. Ensuite, la Côte d'Ivoire, "
                "comme l'ensemble du continent africain, repose sur la "
                "plaque africaine. Enfin, les limites des plaques ne "
                "coïncident pas avec les côtes des continents : elles "
                "passent au milieu des océans, au niveau des dorsales, ou "
                "le long de certaines côtes, au niveau des fosses."
            )
        ) as tracker:
            self.play(FadeIn(remarques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarques))

        # --- Schéma : les plaques glissent sur l'asthénosphère --------------
        litho2 = Rectangle(width=8.0, height=0.7, fill_color=ORANGE, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1)
        astheno2 = Rectangle(width=8.0, height=1.3, fill_color=BLUE_D, fill_opacity=0.55, stroke_color=WHITE, stroke_width=1)
        astheno2.next_to(litho2, DOWN, buff=0)
        fleche_glisse = Arrow(start=LEFT * 3, end=RIGHT * 3, color=YELLOW, buff=0, stroke_width=4)
        fleche_glisse.next_to(litho2, UP, buff=0.15)
        schema_glisse = VGroup(litho2, astheno2, fleche_glisse)
        schema_glisse.next_to(sous_titre, DOWN, buff=0.5)

        # --- À retenir : point clé méthode ----------------------------------
        point_cle = method_box(
            Text(
                _wrap(
                    "Point clé : les plaques ne « flottent » pas sur un "
                    "océan de magma liquide. Elles glissent sur "
                    "l'asthénosphère, un manteau solide mais ductile qui se "
                    "déforme très lentement, comme un fluide extrêmement "
                    "visqueux, sur des millions d'années.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        point_cle.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un point clé à retenir, car c'est un piège fréquent : les "
                "plaques ne flottent pas sur un océan de magma liquide. "
                "Elles glissent sur l'asthénosphère, un manteau qui reste "
                "solide, mais ductile, qui se déforme très lentement, comme "
                "un fluide extrêmement visqueux, à l'échelle de millions "
                "d'années."
            )
        ) as tracker:
            self.play(Create(litho2), Create(astheno2))
            self.play(Create(fleche_glisse))
            self.wait(0.3)
            self.play(FadeIn(point_cle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_glisse), FadeOut(point_cle), FadeOut(titre), FadeOut(sous_titre))
