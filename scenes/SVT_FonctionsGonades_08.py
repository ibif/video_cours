"""
scenes/SVT_FonctionsGonades_08.py — Chapitre 1 (1ereD, SVT), scène 08.

§ 1.4.3 La puberté, mise en route des gonades + exemple du dosage de
testostérone chez 4 sujets + méthode d'interprétation d'un dosage
hormonal + piège sur les hormones "propres à un sexe".
Source : 1ereD/SVT.pdf, pages 14-15.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LaPubertyMiseEnRouteDesGonades(NotionScene):
    def construct(self):
        titre = scene_title("1.4.3 — La puberté, mise en route des gonades")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : avant / à la puberté ------------------------------------
        avant = VGroup(
            Text("Avant la puberté", font_size=24, color=WHITE, weight="BOLD"),
            Text("Gonades au repos :\nni gamètes, ni hormones", font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.25)

        apres = VGroup(
            Text("À la puberté", font_size=24, color=WHITE, weight="BOLD"),
            Text(
                "Filles : 10-12 ans\nGarçons : 12-14 ans\nGamétogenèse + hormones\nen quantité",
                font_size=20,
                color=WHITE,
            ),
        ).arrange(DOWN, buff=0.25)

        chaine = VGroup(avant, apres).arrange(RIGHT, buff=1.6)
        chaine.next_to(titre, DOWN, buff=0.7)
        fleche = Arrow(avant.get_right(), apres.get_left(), buff=0.2, color=YELLOW)

        with self.voiceover(
            text=(
                "Avant la puberté, les gonades sont au repos : ni gamètes, ni "
                "sécrétions hormonales importantes. À la puberté, vers dix à "
                "douze ans chez les filles et douze à quatorze ans chez les "
                "garçons, les gonades s'activent : la gamétogenèse démarre et "
                "les hormones sont déversées en quantité, déclenchant les "
                "transformations visibles du corps."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(avant))
            self.play(FadeIn(fleche))
            self.play(FadeIn(apres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(chaine), FadeOut(fleche))

        # --- Raisonnement : le chef d'orchestre (aperçu) -----------------------
        commande = Text(
            _wrap(
                "Ce qui commande cette mise en route - le cerveau, par "
                "l'intermédiaire de l'hypothalamus et de l'hypophyse - fera "
                "l'objet d'une étude ultérieure.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        commande.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Ce qui commande cette mise en route, c'est le cerveau, par "
                "l'intermédiaire de l'hypothalamus et de l'hypophyse : ce "
                "mécanisme fera l'objet d'une étude ultérieure, dans un "
                "chapitre consacré au contrôle hormonal."
            )
        ) as tracker:
            self.play(FadeIn(commande))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(commande))

        # --- Exemple traité : dosage de testostérone chez 4 sujets --------------
        exemple = example_box(
            Text(
                _wrap(
                    "Testostérone sanguine (ng/mL) : garçon de 8 ans = 0,2 ; "
                    "homme de 25 ans = 6,5 ; homme castré = 0,3 ; homme "
                    "vasectomisé = 6,3. L'adulte a un taux ~32 fois "
                    "supérieur à l'enfant. Le castré a un taux voisin de "
                    "l'enfant. Le vasectomisé a un taux quasi normal "
                    "(6,3/6,5 ≈ 0,97).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On dose la testostérone sanguine chez quatre sujets : un "
                "garçon de huit ans, à zéro virgule deux nanogrammes par "
                "millilitre ; un homme de vingt-cinq ans, à six virgule cinq "
                "; un homme de vingt-cinq ans castré à la suite d'un "
                "accident, à zéro virgule trois ; et un homme de vingt-cinq "
                "ans vasectomisé, à six virgule trois. L'homme adulte présente "
                "un taux environ trente-deux fois supérieur à celui du "
                "garçon. Le castré a un taux voisin de celui de l'enfant. Le "
                "sujet vasectomisé a un taux quasi normal."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        conclusion_ex = Text(
            _wrap(
                "Conclusion : la testostérone est produite par les "
                "testicules à partir de la puberté et libérée dans le "
                "sang ; sa sécrétion ne dépend pas des voies génitales.",
                width=52,
            ),
            font_size=22,
            color=YELLOW,
        )
        conclusion_ex.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Conclusion : le taux sanguin élevé est lié à la présence des "
                "testicules et à l'âge adulte, pas à la perméabilité des "
                "canaux. La testostérone est produite par les testicules à "
                "partir de la puberté et libérée dans le sang ; sa sécrétion "
                "ne dépend pas des voies génitales."
            )
        ) as tracker:
            self.play(FadeIn(conclusion_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(conclusion_ex))

        # --- À retenir : méthode d'interprétation d'un dosage hormonal -----------
        methode = method_box(
            Text(
                _wrap(
                    "Étape 1 : repérer la molécule dosée et le liquide "
                    "prélevé. Étape 2 : comparer les valeurs entre sujets, "
                    "en calculant un rapport si possible. Étape 3 : relier "
                    "chaque variation à la présence/absence de la gonade, "
                    "à l'âge ou au traitement subi. Étape 4 : conclure sur "
                    "l'origine de l'hormone et son rôle.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Pour interpréter un dosage hormonal, quatre étapes. Étape "
                "un : repérer la molécule dosée et le liquide prélevé, "
                "généralement le sang. Étape deux : comparer les valeurs "
                "entre les sujets, en calculant un rapport si possible. Étape "
                "trois : relier chaque variation à la présence ou à "
                "l'absence de la gonade, à l'âge ou au traitement subi. Étape "
                "quatre : conclure sur l'origine de l'hormone et son rôle."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : les hormones ne sont pas propres à un sexe ---------
        piege = warning_box(
            Text(
                _wrap(
                    "Les œstrogènes ne sont pas « l'hormone de la femme », "
                    "ni la testostérone « celle de l'homme » : les deux "
                    "sexes produisent les deux familles d'hormones, à des "
                    "taux très différents. Autre piège : les hormones "
                    "n'arrivent jamais par les trompes ou les canaux "
                    "déférents - toujours par les vaisseaux sanguins.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention : les œstrogènes ne sont pas l'hormone de la "
                "femme, ni la testostérone celle de l'homme. Les deux sexes "
                "produisent les deux familles d'hormones, mais à des taux "
                "très différents. Autre piège fréquent : ne dites jamais que "
                "les hormones arrivent à l'utérus par les trompes, ou au "
                "pénis par les canaux déférents ; elles y arrivent toujours "
                "par les vaisseaux sanguins."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
