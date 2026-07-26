"""
scenes/SVT_EchangesIonsSol_09.py — Chapitre 8 (1ereD, SVT), scène 09.

Clôture du chapitre : retour sur l'histoire d'Adama et de Konan (scène 01)
à la lumière de toute la notion étudiée, puis L'ESSENTIEL DU CHAPITRE.
Source : 1ereD/SVT.pdf, pages 103-113 (synthèse).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=50):
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


class SyntheseEchangesIonsSol(NotionScene):
    def construct(self):
        titre = scene_title("8 — Synthèse : les échanges d'ions au niveau du sol")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : retour sur Adama et Konan ------------------------------
        transition = Text(
            _wrap(
                "Nous pouvons à présent répondre complètement à la "
                "question posée au début du chapitre : pourquoi le maïs "
                "de Konan restait-il chétif, alors qu'Adama récoltait "
                "sur la parcelle voisine ?",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        transition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous pouvons à présent répondre complètement à la "
                "question posée au début de ce chapitre : pourquoi le "
                "maïs de Konan restait-il chétif, avec des feuilles "
                "jaunes, alors qu'Adama récoltait un maïs vigoureux sur la "
                "parcelle voisine, avec la même pluie ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(transition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(transition))

        # --- Exemple traité : la solution complète de l'énigme --------------
        solution = example_box(
            _bullets(
                [
                    "Sol de Konan : sableux, donc CEC faible -> peu de "
                    "sites d'adsorption sur le CAH.",
                    "Les cations apportés par la pluie et les engrais "
                    "(azote, potassium) sont lessivés au lieu d'être "
                    "retenus.",
                    "Peu de cations retenus = peu de cations échangés "
                    "contre les H+ de la racine = peu d'ions "
                    "disponibles pour l'absorption.",
                    "Résultat observé : nanisme et chlorose des vieilles "
                    "feuilles -> signature d'une carence en azote.",
                    "Solution : fumure organique pour augmenter l'humus "
                    "(donc la CEC), et fractionner les apports "
                    "d'engrais.",
                ],
                font_size=18,
                width=58,
            ),
            box_width=12.6,
        )
        solution.next_to(titre, DOWN, buff=0.4)
        _fit(solution, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Voici l'explication complète. Le sol de Konan est "
                "sableux, donc sa capacité d'échange de cations est "
                "faible : il offre peu de sites d'adsorption sur son "
                "complexe argilo-humique. Les cations apportés par la "
                "pluie et par les engrais, notamment l'azote et le "
                "potassium, sont donc lessivés au lieu d'être retenus. "
                "Peu de cations retenus, c'est peu de cations échangés "
                "contre les ions H+ libérés par la respiration des "
                "racines, donc peu d'ions réellement disponibles pour "
                "l'absorption. Résultat observé sur le terrain : un "
                "nanisme et une chlorose des vieilles feuilles, la "
                "signature typique d'une carence en azote. La solution "
                "pour Konan : apporter de la fumure organique pour "
                "augmenter l'humus, donc la CEC de son sol, et fractionner "
                "ses apports d'engrais plutôt que de tout épandre en une "
                "seule fois."
            )
        ) as tracker:
            self.play(FadeIn(solution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(solution))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (partie 1) ------------------
        essentiel_1 = essentiel_box(
            _bullets(
                [
                    "Le sol contient des particules minérales (sable, "
                    "limon, argile), de l'humus, de l'eau chargée d'ions "
                    "et de l'air, plus des organismes vivants.",
                    "L'argile et l'humus forment le complexe "
                    "argilo-humique (CAH), chargé négativement : "
                    "adsorbe les cations (Ca2+, Mg2+, K+, NH4+, H+) ; "
                    "les anions (NO3−...) ne sont pas retenus.",
                    "Le CO2 de la respiration racinaire fournit des H+ "
                    "qui libèrent les cations du complexe : mécanisme "
                    "central des échanges d'ions.",
                    "La CEC mesure la quantité de cations qu'un sol peut "
                    "retenir : plus elle est élevée, plus le sol "
                    "conserve sa fertilité.",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel_1.next_to(titre, DOWN, buff=0.35)
        _fit(essentiel_1, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre, en deux temps. D'abord, le "
                "sol : il contient des particules minérales, sable, limon "
                "et argile, de l'humus, de l'eau chargée d'ions et de "
                "l'air, plus de nombreux organismes vivants. L'argile et "
                "l'humus forment le complexe argilo-humique, chargé "
                "négativement : il adsorbe les cations, calcium, "
                "magnésium, potassium, ammonium et hydrogène ; les "
                "anions, comme le nitrate, ne sont pas retenus et sont "
                "lessivables. Le dioxyde de carbone de la respiration "
                "racinaire fournit des ions H+ qui libèrent les cations du "
                "complexe : c'est le mécanisme central des échanges "
                "d'ions au niveau du sol. Enfin, la capacité d'échange de "
                "cations, la CEC, mesure la quantité de cations qu'un sol "
                "peut retenir : plus elle est élevée, plus le sol "
                "conserve sa fertilité."
            )
        ) as tracker:
            self.play(FadeIn(essentiel_1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel_1))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (partie 2) ------------------
        essentiel_2 = essentiel_box(
            _bullets(
                [
                    "Éléments majeurs (N, P, K, Ca, Mg, S) et "
                    "oligo-éléments (Fe, Mn, B, Zn, Cu, Mo, Cl) : tous "
                    "indispensables ; chaque carence a ses symptômes "
                    "(chlorose, nécrose, nanisme).",
                    "Les cultures hydroponiques (solution de Knopp, "
                    "solutions déficientes vs témoin) prouvent le rôle "
                    "de chaque élément.",
                    "L'absorption se fait par les poils absorbants de la "
                    "zone pilifère ; elle est sélective et le plus "
                    "souvent active (ATP, transporteurs).",
                    "Les ions montent par le xylème (sève brute) "
                    "jusqu'aux feuilles, où ils entrent dans la "
                    "fabrication de la matière vivante.",
                    "La fumure minérale et organique restitue les "
                    "éléments exportés ; rotations avec légumineuses, "
                    "couverture du sol, chaulage et fumure raisonnée "
                    "préservent la fertilité des sols ivoiriens.",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel_2.next_to(titre, DOWN, buff=0.35)
        _fit(essentiel_2, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Ensuite, la nutrition minérale de la plante. Les "
                "éléments majeurs, azote, phosphore, potassium, calcium, "
                "magnésium, soufre, et les oligo-éléments, fer, "
                "manganèse, bore, zinc, cuivre, molybdène, chlore, sont "
                "tous indispensables ; chaque carence a ses symptômes "
                "propres, chlorose, nécrose ou nanisme. Les cultures "
                "hydroponiques, avec la solution de Knopp et des "
                "solutions déficientes comparées à un témoin, prouvent "
                "expérimentalement le rôle de chaque élément. "
                "L'absorption se fait par les poils absorbants de la zone "
                "pilifère ; elle est sélective et, le plus souvent, "
                "active, grâce à l'ATP de la respiration et à des "
                "transporteurs membranaires spécifiques. Les ions montent "
                "ensuite par le xylème, dans la sève brute, jusqu'aux "
                "feuilles, où ils entrent dans la fabrication de la "
                "matière vivante. Enfin, la fumure minérale et organique "
                "restitue au sol les éléments exportés par les récoltes ; "
                "la rotation avec des légumineuses, la couverture du sol, "
                "le chaulage et une fumure raisonnée préservent, sur le "
                "long terme, la fertilité des sols ivoiriens."
            )
        ) as tracker:
            self.play(FadeIn(essentiel_2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel_2))
