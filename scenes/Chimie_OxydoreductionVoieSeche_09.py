"""
scenes/Chimie_OxydoreductionVoieSeche_09.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 09 (dernière).

Synthèse du chapitre : trois méthodes (déterminer un n.o., équilibrer une
réaction par voie sèche via les n.o., calculs de quantités de matière et
de masses), quatre pièges classiques, et l'essentiel à retenir.
Source : 1ereC/Chimie.pdf, chapitre 13, pages 124-133 (synthèse).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    UP,
    WHITE,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=20, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class MethodesPiegesEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("13.6 Méthodes, pièges à éviter et essentiel")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : annonce du bilan ---------------------------------------
        intro = Text(
            _wrap(
                "Terminons ce chapitre par trois méthodes pratiques, "
                "quatre pièges classiques à connaître, puis un "
                "récapitulatif complet.",
                width=54,
            ),
            font_size=23, color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce chapitre sur l'oxydoréduction par voie "
                "sèche par un bilan méthodologique : trois méthodes "
                "pratiques à maîtriser, quatre pièges classiques à "
                "éviter, puis un récapitulatif complet de l'essentiel à "
                "retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : méthode 1 ------------------------------------------
        methode1 = method_box(
            VGroup(
                Text("Déterminer le n.o. d'un élément :", font_size=21, weight="BOLD"),
                Text("1. Identifier le type d'entité (corps pur simple,", font_size=19),
                Text("   ion monoatomique, molécule, ion polyatomique).", font_size=19),
                Text("2. Appliquer les valeurs de référence (H = +I,", font_size=19),
                Text("   O = −II, sauf exceptions).", font_size=19),
                Text("3. Poser l'équation : somme des n.o. = charge", font_size=19),
                Text("   totale de l'entité, puis résoudre.", font_size=19),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=11.6,
        )
        methode1.next_to(titre, DOWN, buff=0.4)
        _fit(methode1, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Première méthode : déterminer le nombre d'oxydation d'un "
                "élément. Un : identifier le type d'entité, corps pur "
                "simple, ion monoatomique, molécule ou ion polyatomique. "
                "Deux : appliquer les valeurs de référence, l'hydrogène à "
                "plus un, l'oxygène à moins deux, sauf exceptions. Trois : "
                "poser l'équation, la somme des n.o. égale la charge "
                "totale de l'entité, puis résoudre pour l'élément "
                "recherché."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Raisonnement : méthode 2 ------------------------------------------
        methode2 = method_box(
            VGroup(
                Text("Équilibrer une réaction par voie sèche via les n.o. :", font_size=20, weight="BOLD"),
                Text("1. Calculer le n.o. de chaque élément avant/après.", font_size=19),
                Text("2. Repérer l'élément oxydé (n.o. ↑) et l'élément", font_size=19),
                Text("   réduit (n.o. ↓).", font_size=19),
                Text("3. Équilibrer le nombre d'électrons échangés en", font_size=19),
                Text("   ajustant les coefficients stœchiométriques.", font_size=19),
                Text("4. Vérifier la conservation de tous les atomes.", font_size=19),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.2,
        )
        methode2.next_to(titre, DOWN, buff=0.4)
        _fit(methode2, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Deuxième méthode : équilibrer une réaction par voie "
                "sèche grâce aux nombres d'oxydation. Un : calculer le "
                "n.o. de chaque élément avant et après réaction. Deux : "
                "repérer l'élément oxydé, dont le n.o. augmente, et "
                "l'élément réduit, dont le n.o. diminue. Trois : équilibrer "
                "le nombre d'électrons échangés en ajustant les "
                "coefficients stœchiométriques, exactement comme pour des "
                "demi-équations. Quatre : vérifier enfin la conservation "
                "de tous les atomes dans l'équation finale."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Exemple traité : méthode 3 -----------------------------------------
        methode3 = method_box(
            VGroup(
                Text("Calculs de quantités de matière et de masses :", font_size=21, weight="BOLD"),
                Text("1. Convertir masse ↔ quantité de matière : n = m / M.", font_size=19),
                Text("2. Utiliser les coefficients de l'équation-bilan", font_size=19),
                Text("   pour passer d'un réactif/produit à un autre.", font_size=19),
                Text("3. Reconvertir en masse si nécessaire (m = n × M).", font_size=19),
                Text("(Exemple type : calcul de la masse de fer produite", font_size=18),
                Text("à partir d'une masse d'hématite, scène précédente.)", font_size=18),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.4,
        )
        methode3.next_to(titre, DOWN, buff=0.4)
        _fit(methode3, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Troisième méthode : les calculs de quantités de matière "
                "et de masses. Un : convertir entre masse et quantité de "
                "matière grâce à n égale m sur M. Deux : utiliser les "
                "coefficients de l'équation-bilan pour passer d'un réactif "
                "ou d'un produit à un autre. Trois : reconvertir en masse "
                "si nécessaire, avec m égale n fois M. C'est exactement la "
                "méthode employée dans l'exemple de la scène précédente, "
                "pour calculer la masse de fer produite à partir d'une "
                "masse d'hématite."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- À retenir : les quatre pièges classiques ---------------------------
        pieges = warning_box(
            _bullets(
                [
                    "« Oxydation » ne veut pas dire « réaction avec du "
                    "dioxygène » : le critère est le transfert d'électrons.",
                    "Ne pas inverser oxydant/réducteur : n.o. qui augmente "
                    "= oxydé = réducteur ; n.o. qui diminue = réduit = "
                    "oxydant.",
                    "Un n.o. fractionnaire (ex : Fe dans Fe₃O₄, +8/3) est "
                    "une MOYENNE, pas le n.o. réel d'un seul atome.",
                    "Dans le haut fourneau, le réducteur direct du minerai "
                    "est le monoxyde de carbone CO, PAS directement le "
                    "carbone solide C.",
                ],
                width=44,
            ),
            box_width=12.6,
        )
        pieges.next_to(titre, DOWN, buff=0.35)
        _fit(pieges, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Récapitulons les quatre pièges classiques rencontrés "
                "dans ce chapitre. Premièrement, « oxydation » ne veut "
                "pas dire « réaction avec du dioxygène » : le seul "
                "critère est le transfert d'électrons. Deuxièmement, ne "
                "jamais inverser oxydant et réducteur : un n.o. qui "
                "augmente correspond à un élément oxydé, qui est le "
                "réducteur, et un n.o. qui diminue correspond à un "
                "élément réduit, qui est l'oxydant. Troisièmement, un n.o. "
                "fractionnaire, comme le plus huit tiers du fer dans Fe "
                "trois O quatre, est une moyenne, jamais le n.o. réel "
                "d'un seul atome. Et quatrièmement, dans le haut fourneau, "
                "le réducteur direct du minerai de fer est le monoxyde de "
                "carbone, et non directement le carbone solide."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges))

        # --- Piège à éviter / à retenir final : l'essentiel ---------------------
        essentiel = essentiel_box(
            VGroup(
                Text("Chapitre 13 : Oxydoréduction par voie sèche", font_size=21, weight="BOLD"),
                Text(
                    "• Voie sèche : transfert d'électrons entre réactifs "
                    "solides/gazeux, sans eau, amorcé par la chaleur.",
                    font_size=18,
                ),
                Text(
                    "• Le n.o. (chiffre romain signé) permet de repérer "
                    "oxydant et réducteur sans demi-équation.",
                    font_size=18,
                ),
                Text(
                    "• n.o. ↑ = oxydé = réducteur ; n.o. ↓ = réduit = "
                    "oxydant ; électrons cédés = électrons captés.",
                    font_size=18,
                ),
                Text(
                    "• Exemples clés : aluminothermie (2Al+Fe₂O₃), "
                    "CuO+H₂, CuO+C, réduction du minerai par CO.",
                    font_size=18,
                ),
                Text(
                    "• La sidérurgie (haut fourneau) réduit Fe₂O₃ en "
                    "fonte grâce au monoxyde de carbone CO.",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=13.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)
        _fit(essentiel, titre.get_bottom()[1] - 0.1)

        with self.voiceover(
            text=(
                "Voici l'essentiel à retenir de ce chapitre. La "
                "réaction par voie sèche est un transfert d'électrons "
                "entre réactifs solides ou gazeux, sans eau, amorcé par "
                "la chaleur. Le nombre d'oxydation, noté en chiffres "
                "romains signés, permet de repérer l'oxydant et le "
                "réducteur sans écrire de demi-équation : un n.o. qui "
                "augmente signale un élément oxydé, donc réducteur, un "
                "n.o. qui diminue signale un élément réduit, donc "
                "oxydant, et les électrons cédés égalent toujours les "
                "électrons captés. Retenez les exemples clés : "
                "l'aluminothermie, la réduction de CuO par le "
                "dihydrogène ou par le carbone, et la réduction du "
                "minerai de fer par le monoxyde de carbone dans le haut "
                "fourneau, cœur de la sidérurgie."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
