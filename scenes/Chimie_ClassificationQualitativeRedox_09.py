"""
scenes/Chimie_ClassificationQualitativeRedox_09.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 09 (dernière scène du chapitre).

Synthèse méthodologique et pièges à éviter. Deux `method_box` : (1)
construire une classification à partir d'expériences + appliquer la règle
du gamma en 4 étapes, (2) calculer une variation de masse lors d'un dépôt
métallique. Trois `warning_box` : inverser oxydant fort/réducteur fort
dans un même couple ; oublier qu'un métal ne réagit pas avec ses propres
ions ; généraliser l'action des acides à tous les acides (HNO₃, cas de
PbCl₂ insoluble qui bloque la réaction du plomb). `essentiel_box` finale
récapitulant tout le chapitre.
Source : 1ereC/Chimie.pdf, chapitre 10, pages 94-101 (synthèse).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
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


class MethodesPiegesEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("10.5 Méthodes, pièges à éviter et essentiel")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        intro = Text(
            _wrap(
                "Avant de clore ce chapitre, reprenons les méthodes clés à "
                "maîtriser, les pièges les plus fréquents, puis l'essentiel "
                "à retenir dans son ensemble.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant de clore ce chapitre, reprenons les méthodes clés à "
                "maîtriser, les pièges les plus fréquents, puis l'essentiel "
                "à retenir dans son ensemble."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : méthode 1, classification + règle du gamma ----------
        methode1 = method_box(
            VGroup(
                Text("Méthode — construire une classification, puis l'utiliser :", font_size=19, weight="BOLD"),
                Text("1. Comparer les métaux deux à deux par l'expérience.", font_size=18),
                Text("2. Classer par pouvoir réducteur (transitivité).", font_size=18),
                Text("3. Placer les deux couples à comparer sur l'échelle.", font_size=18),
                Text("4. Tracer le γ : oxydant du haut → réducteur du bas,", font_size=18),
                Text("   puis écrire l'équation bilan dans ce sens.", font_size=18),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.8,
        )
        methode1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Première méthode à maîtriser : construire une "
                "classification, puis l'utiliser. On compare d'abord les "
                "métaux deux à deux par l'expérience, puis on les classe "
                "par pouvoir réducteur en utilisant la transitivité. Pour "
                "prévoir une réaction entre deux couples donnés, on les "
                "place sur l'échelle, on trace le gamma de l'oxydant du "
                "haut vers le réducteur du bas, puis on écrit l'équation "
                "bilan dans ce sens."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : variation de masse lors d'un dépôt ----------------------
        methode2 = method_box(
            VGroup(
                Text("Méthode — variation de masse lors d'un dépôt métallique :", font_size=19, weight="BOLD"),
                Text("1. Écrire l'équation bilan et repérer les nombres", font_size=18),
                Text("   stœchiométriques du métal déposé et du réactif.", font_size=18),
                Text("2. Calculer n(réactif consommé), en déduire n(dépôt)", font_size=18),
                Text("   par proportionnalité stœchiométrique.", font_size=18),
                MathTex(r"\Delta m = n_{d\acute{e}p\hat{o}t} \times M_{m\acute{e}tal}", font_size=24, color=ORANGE),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.8,
        )
        methode2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deuxième méthode : calculer une variation de masse lors "
                "d'un dépôt métallique, par exemple le dépôt de cuivre sur "
                "une lame de fer. On écrit d'abord l'équation bilan, et on "
                "repère les nombres stœchiométriques du métal déposé et du "
                "réactif consommé. On calcule la quantité de matière du "
                "réactif consommé, on en déduit la quantité de matière "
                "déposée par proportionnalité stœchiométrique, puis la "
                "variation de masse s'obtient en multipliant cette "
                "quantité de matière par la masse molaire du métal déposé."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Pièges à éviter (3 warning_box successives) -------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 : dans un même couple Ox/Red, ne pas inverser qui "
                    "est l'oxydant et qui est le réducteur — l'oxydant est "
                    "toujours celui qui CAPTE des électrons (Cu²⁺), le "
                    "réducteur celui qui en CÈDE (Cu).",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Premier piège fréquent : dans un même couple oxydant "
                "réducteur, ne pas inverser qui est l'oxydant et qui est le "
                "réducteur. L'oxydant est toujours celui qui capte des "
                "électrons, par exemple les ions cuivre deux plus ; le "
                "réducteur est celui qui en cède, ici le cuivre métal."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            Text(
                _wrap(
                    "Piège 2 : un métal ne réagit jamais avec ses PROPRES ions "
                    "(Cu dans Cu²⁺ : rien ne se passe). La règle du gamma ne "
                    "s'applique qu'entre deux couples DIFFÉRENTS.",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième piège fréquent : un métal ne réagit jamais avec "
                "ses propres ions. Du cuivre plongé dans une solution "
                "d'ions cuivre deux plus, comme dans notre toute première "
                "expérience, ne donne strictement rien. La règle du gamma "
                "ne s'applique qu'entre deux couples différents."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            VGroup(
                Text(
                    "Piège 3 : ne pas généraliser l'action des acides à TOUS",
                    font_size=18,
                ),
                Text(
                    "les acides. HNO₃ attaque Cu via NO₃⁻ (pas via H₃O⁺). Le",
                    font_size=18,
                ),
                Text(
                    "plomb, pourtant plus réducteur que H₂, réagit très peu",
                    font_size=18,
                ),
                Text(
                    "avec HCl : le PbCl₂ formé, insoluble, bloque la réaction.",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=12.8,
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège fréquent : ne pas généraliser l'action des "
                "acides à tous les acides. L'acide nitrique attaque le "
                "cuivre grâce aux ions nitrate, pas grâce aux ions oxonium. "
                "Autre exception à connaître : le plomb, pourtant plus "
                "réducteur que le dihydrogène d'après la classification, "
                "réagit en réalité très peu avec l'acide chlorhydrique, "
                "car le chlorure de plomb formé est insoluble et vient "
                "recouvrir le métal, bloquant la poursuite de la réaction."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- À retenir : essentiel du chapitre ------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("• Un métal réagit avec les ions d'un métal moins réducteur.", font_size=18),
                Text("• Réaction spontanée : Ox fort + Red fort → Red faible + Ox faible.", font_size=18),
                Text("• Classement usuel : Mg>Zn>Fe>Ni>Sn>Pb>H₂>Cu>Ag>Au (réducteur ↓).", font_size=18),
                Text("• Règle du gamma : oxydant du haut réagit avec réducteur du bas.", font_size=18),
                Text("• Applications : acides sur métaux, métallurgie, protection,", font_size=18),
                Text("  cimentation du cuivre.", font_size=18),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
            box_width=13.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de ce chapitre. Un métal réagit avec "
                "les ions d'un métal moins réducteur que lui. Une réaction "
                "spontanée met en jeu l'oxydant le plus fort et le "
                "réducteur le plus fort présents : oxydant fort, plus "
                "réducteur fort, donne réducteur faible, plus oxydant "
                "faible. Le classement usuel, par pouvoir réducteur "
                "décroissant, est : magnésium, zinc, fer, nickel, étain, "
                "plomb, dihydrogène, cuivre, argent, or. La règle du gamma "
                "permet de prévoir une réaction : l'oxydant du couple placé "
                "en haut réagit avec le réducteur du couple placé en bas. "
                "Enfin, cette classification trouve des applications "
                "essentielles : l'action des acides sur les métaux, la "
                "métallurgie, la protection des métaux contre la "
                "corrosion, et la cimentation du cuivre."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
