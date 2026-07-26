"""
scenes/SVT_EchangesIonsSol_05.py — Chapitre 8 (1ereD, SVT), scène 05.

§ 8.2.3 Mise en évidence expérimentale : les cultures sur solutions
nutritives. Solution de Knopp, méthode du protocole hydroponique en 4
étapes, résultats classiques par carence, exemple d'identification de
l'élément manquant (magnésium), attention aux 4 pièges du protocole.
Source : 1ereD/SVT.pdf, pages 108-109.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class CulturesSurSolutionsNutritives(NotionScene):
    def construct(self):
        titre = scene_title("8.2.3 — Cultures sur solutions nutritives")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : la culture hydroponique et la solution de Knopp -----
        intro = Text(
            _wrap(
                "Comment prouver expérimentalement le rôle de chaque "
                "élément minéral ? En cultivant des plantes hors sol, "
                "dans de l'eau additionnée de sels minéraux dosés : la "
                "culture hydroponique.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment prouver expérimentalement le rôle de chaque "
                "élément minéral ? En cultivant des plantes hors sol, dans "
                "de l'eau additionnée de sels minéraux dosés avec "
                "précision : c'est la culture hydroponique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        knopp = property_box(
            _bullets(
                [
                    "Nitrate de calcium Ca(NO3)2 : 1 g",
                    "Nitrate de potassium KNO3 : 0,25 g",
                    "Phosphate monopotassique KH2PO4 : 0,25 g",
                    "Sulfate de magnésium MgSO4 : 0,25 g",
                    "Chlorure ferrique FeCl3 : quelques gouttes",
                    "(le tout pour 1 litre d'eau distillée)",
                ],
                font_size=20,
                width=52,
            ),
            box_width=11.8,
        )
        knopp.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une solution nutritive classique est la solution de "
                "Knopp, préparée pour un litre d'eau distillée : un "
                "gramme de nitrate de calcium, zéro virgule vingt-cinq "
                "gramme de nitrate de potassium, zéro virgule vingt-cinq "
                "gramme de phosphate monopotassique, zéro virgule "
                "vingt-cinq gramme de sulfate de magnésium, et quelques "
                "gouttes de chlorure ferrique."
            )
        ) as tracker:
            self.play(FadeIn(knopp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(knopp))

        # --- Raisonnement : méthode du protocole en 4 étapes ---------------
        protocole = method_box(
            _bullets(
                [
                    "1. Préparer la solution complète (Knopp), eau "
                    "distillée.",
                    "2. Préparer des solutions déficientes, chacune "
                    "privée d'un seul élément.",
                    "3. Placer une plantule identique par flacon opaque "
                    "(racines à l'obscurité), solution aérée.",
                    "4. Renouveler régulièrement, observer 3-4 semaines. "
                    "Le témoin (solution complète) sert de référence.",
                ],
                font_size=20,
                width=54,
            ),
            box_width=12.0,
        )
        protocole.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici le protocole en quatre étapes. Étape un : préparer "
                "la solution complète, la solution de Knopp, avec de "
                "l'eau distillée. Étape deux : préparer des solutions "
                "déficientes, chacune privée d'un seul élément. Étape "
                "trois : placer dans chaque flacon une plantule "
                "identique, maintenue par un tampon de coton, dans un "
                "flacon opaque pour garder les racines à l'obscurité, "
                "avec une solution aérée. Étape quatre : renouveler "
                "régulièrement la solution, et observer pendant trois à "
                "quatre semaines. Le flacon témoin, avec la solution "
                "complète, sert de référence pour comparer tous les "
                "autres."
            )
        ) as tracker:
            self.play(FadeIn(protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(protocole))

        # Schéma simple : rangée de flacons (rectangles) opaques avec plantule
        flacons = VGroup()
        noms = ["Témoin", "Sans N", "Sans P", "Sans K", "Sans Mg"]
        for nom in noms:
            corps = Rectangle(width=0.9, height=1.3, color=GREEN, fill_color=GREEN, fill_opacity=0.15)
            tige = Line(corps.get_top(), corps.get_top() + UP * 0.5, color=GREEN, stroke_width=3)
            label = Text(nom, font_size=15, color=WHITE).next_to(corps, DOWN, buff=0.1)
            flacons.add(VGroup(corps, tige, label))
        flacons.arrange(RIGHT, buff=0.5)
        flacons.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "On obtient ainsi une série de flacons à comparer : un "
                "témoin avec la solution complète, et plusieurs flacons, "
                "chacun privé d'un seul élément - azote, phosphore, "
                "potassium, magnésium."
            )
        ) as tracker:
            self.play(FadeIn(flacons))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(flacons))

        # --- Résultats classiques (à retenir) -------------------------------
        resultats = property_box(
            _bullets(
                [
                    "Témoin : croissance normale.",
                    "Sans azote : nanisme et chlorose.",
                    "Sans phosphore : feuillage violacé, croissance "
                    "retardée.",
                    "Sans potassium : bordures nécrosées.",
                    "Sans magnésium : chlorose internervaire.",
                ],
                font_size=20,
                width=52,
            ),
            box_width=11.8,
        )
        resultats.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les résultats classiques de cette expérience sont "
                "toujours les mêmes. Le témoin a une croissance normale. "
                "Sans azote : nanisme et chlorose. Sans phosphore : un "
                "feuillage violacé et une croissance retardée. Sans "
                "potassium : des bordures de feuilles nécrosées. Sans "
                "magnésium : une chlorose internervaire."
            )
        ) as tracker:
            self.play(FadeIn(resultats))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resultats))

        # --- Exemple traité : identifier l'élément manquant -----------------
        exemple = example_box(
            Text(
                _wrap(
                    "Une plantule de maïs sur solution sans étiquette : "
                    "après 3 semaines, plus petite que le témoin, "
                    "vieilles feuilles jaunissent, nervures restent "
                    "vertes. Symptômes = nanisme + chlorose internervaire "
                    "des vieilles feuilles = signature du magnésium "
                    "(l'azote donne une chlorose uniforme du limbe). "
                    "Conclusion : solution privée de magnésium.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Appliquons cette grille de lecture. Une plantule de maïs "
                "pousse sur une solution dont l'étiquette a été perdue. "
                "Après trois semaines, elle est plus petite que le "
                "témoin, et ses vieilles feuilles jaunissent alors que "
                "les nervures restent vertes. Quel élément manque ? Les "
                "symptômes, un nanisme associé à une chlorose "
                "internervaire des vieilles feuilles, forment la "
                "signature typique de la carence en magnésium - l'azote, "
                "lui, aurait donné une chlorose uniforme de tout le "
                "limbe. Conclusion : cette solution était privée de "
                "magnésium."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Piège à éviter : les 4 pièges du protocole ---------------------
        pieges = warning_box(
            _bullets(
                [
                    "Utiliser l'eau du robinet (contient déjà des ions "
                    "qui faussent la carence).",
                    "Oublier le flacon témoin (aucune référence, aucune "
                    "conclusion possible).",
                    "Laisser les flacons transparents (lumière -> "
                    "algues ; racines ont besoin d'obscurité).",
                    "Oublier d'aérer (racines respirent mal, absorption "
                    "chute).",
                ],
                font_size=20,
                width=54,
            ),
            box_width=11.8,
        )
        pieges.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à quatre pièges classiques de ce protocole. "
                "Premier piège : utiliser de l'eau du robinet au lieu "
                "d'eau distillée, car elle contient déjà des ions qui "
                "faussent la carence étudiée. Deuxième piège : oublier le "
                "flacon témoin, sans lequel aucune conclusion n'est "
                "possible. Troisième piège : laisser les flacons "
                "transparents, la lumière favorisant le développement "
                "d'algues alors que les racines ont besoin d'obscurité. "
                "Quatrième piège : oublier d'aérer la solution, ce qui "
                "empêche les racines de respirer et fait chuter "
                "l'absorption."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(pieges))
