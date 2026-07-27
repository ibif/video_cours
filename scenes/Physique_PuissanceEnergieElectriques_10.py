"""
scenes/Physique_PuissanceEnergieElectriques_10.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 10.

§ Maîtriser sa consommation électrique. Facteurs (puissance × durée).
Conseils pratiques (LED vs incandescence, éteindre les veilles, appareils
adaptés). Tableau des puissances usuelles des appareils domestiques (LED,
ventilateur, téléviseur, réfrigérateur, fer à repasser, bouilloire,
climatiseur, chauffe-eau).
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 7 fin).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MaitriserConsommation(NotionScene):
    def construct(self):
        titre = scene_title("Maîtriser sa consommation électrique")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Une facture d'électricité élevée n'est pas une fatalité : "
                "elle dépend directement de deux facteurs que l'on peut "
                "maîtriser. Lesquels, et quels gestes simples permettent de "
                "réduire durablement la consommation ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une facture d'électricité élevée n'est pas une fatalité : "
                "elle dépend directement de deux facteurs que l'on peut "
                "maîtriser. Lesquels, et quels gestes simples permettent de "
                "réduire durablement la consommation d'un foyer ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : les deux facteurs ----------------------------------
        facteurs = property_box(
            VGroup(
                Text("L'énergie consommée dépend de deux facteurs, W = Pt :", font_size=21, weight="BOLD"),
                MathTex(r"W = P \times t", font_size=30),
                Text("• la PUISSANCE de l'appareil utilisé (en W) ;", font_size=20),
                Text("• la DURÉE de fonctionnement (en h).", font_size=20),
                Text("Réduire l'un OU l'autre réduit l'énergie consommée.", font_size=20),
            ).arrange(DOWN, buff=0.18),
            box_width=11.4,
        )
        facteurs.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'énergie consommée, W égale P fois t, dépend uniquement "
                "de deux facteurs : la puissance de l'appareil utilisé, et "
                "la durée pendant laquelle il fonctionne. Réduire l'un ou "
                "l'autre de ces deux facteurs réduit directement l'énergie "
                "consommée, donc le montant de la facture."
            )
        ) as tracker:
            self.play(FadeIn(facteurs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(facteurs))

        conseils = method_box(
            VGroup(
                Text("Conseils pratiques pour réduire sa consommation :", font_size=21, weight="BOLD"),
                Text("• Préférer les ampoules LED (peu de puissance) aux", font_size=20),
                Text("   ampoules à incandescence (beaucoup de chaleur perdue).", font_size=20),
                Text("• Éteindre les veilles des appareils inutilisés.", font_size=20),
                Text("• Choisir des appareils à la puissance adaptée au besoin", font_size=20),
                Text("   réel (pas surdimensionnés).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        conseils.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici quelques conseils pratiques. Préférer les ampoules "
                "LED, de faible puissance, aux ampoules à incandescence, qui "
                "perdent l'essentiel de leur énergie en chaleur plutôt qu'en "
                "lumière. Éteindre systématiquement les veilles des "
                "appareils inutilisés, qui consomment en silence toute la "
                "journée. Et choisir des appareils dont la puissance est "
                "adaptée au besoin réel, sans les surdimensionner inutilement."
            )
        ) as tracker:
            self.play(FadeIn(conseils))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conseils))

        # --- Exemple : tableau des puissances usuelles ----------------------------
        col1 = VGroup(
            Text("Appareil", font_size=18, weight="BOLD"),
            Text("Ampoule LED", font_size=17),
            Text("Ventilateur", font_size=17),
            Text("Téléviseur", font_size=17),
            Text("Réfrigérateur", font_size=17),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        col2 = VGroup(
            Text("Puissance", font_size=18, weight="BOLD"),
            Text("≈ 10 W", font_size=17),
            Text("≈ 60 W", font_size=17),
            Text("≈ 120 W", font_size=17),
            Text("≈ 150 W", font_size=17),
        ).arrange(DOWN, buff=0.22)

        col3 = VGroup(
            Text("Appareil", font_size=18, weight="BOLD"),
            Text("Fer à repasser", font_size=17),
            Text("Bouilloire", font_size=17),
            Text("Climatiseur", font_size=17),
            Text("Chauffe-eau", font_size=17),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        col4 = VGroup(
            Text("Puissance", font_size=18, weight="BOLD"),
            Text("≈ 1000-1500 W", font_size=17),
            Text("≈ 2000 W", font_size=17),
            Text("≈ 1500-2500 W", font_size=17),
            Text("≈ 2000-3000 W", font_size=17),
        ).arrange(DOWN, buff=0.22)

        tableau = VGroup(
            VGroup(col1, col2).arrange(RIGHT, buff=0.35),
            VGroup(col3, col4).arrange(RIGHT, buff=0.35),
        ).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        tableau_box = example_box(tableau, box_width=12.6)
        tableau_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici un tableau des puissances usuelles des appareils "
                "domestiques. Les petits consommateurs : une ampoule LED "
                "autour de dix watts, un ventilateur autour de soixante "
                "watts, un téléviseur autour de cent vingt watts, un "
                "réfrigérateur autour de cent cinquante watts. Les gros "
                "consommateurs, ceux qui produisent de la chaleur ou du "
                "froid : un fer à repasser entre mille et mille cinq cents "
                "watts, une bouilloire autour de deux mille watts, un "
                "climatiseur entre mille cinq cents et deux mille cinq "
                "cents watts, et un chauffe-eau entre deux mille et trois "
                "mille watts."
            )
        ) as tracker:
            self.play(FadeIn(tableau_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_box))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"W = P \times t", font_size=28),
                Text("Les appareils de chauffe (fer, bouilloire, chauffe-eau,", font_size=20),
                Text("climatiseur) sont les plus gros postes de consommation.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'énergie consommée vaut toujours "
                "puissance fois durée. Les appareils qui chauffent ou "
                "refroidissent, comme le fer à repasser, la bouilloire, le "
                "chauffe-eau ou le climatiseur, sont de très loin les plus "
                "gros postes de consommation d'un foyer."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Un appareil « éteint » en veille consomme quand même :", font_size=20),
                Text("   toujours vérifier le débranchement pour une puissance", font_size=20),
                Text("   réellement nulle.", font_size=20),
                Text("• Ce n'est pas la tension qui coûte cher, c'est l'énergie", font_size=20),
                Text("   W = Pt : un petit appareil utilisé longtemps peut", font_size=20),
                Text("   consommer plus qu'un gros appareil utilisé peu.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.2,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Un appareil simplement mis en veille "
                "continue de consommer de l'énergie : seul un débranchement "
                "réel garantit une puissance nulle. Et il faut bien "
                "retenir que ce n'est jamais la tension qui coûte cher, "
                "c'est l'énergie W égale P t : un petit appareil utilisé "
                "très longtemps peut au final consommer davantage qu'un "
                "gros appareil utilisé brièvement."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
