"""
scenes/SVT_Gametogenese_09.py — Chapitre 3 (1ereD, SVT), scène 09.

Clôture du chapitre : L'ESSENTIEL DU CHAPITRE (synthèse des points clés :
gamétogénèse, méiose, brassage, spermatogenèse, ovogenèse, structures des
gamètes, contrôle hormonal FSH/LH). Source : 1ereD/SVT.pdf, page 46.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=18, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    return lines


class SyntheseGametogenese(NotionScene):
    def construct(self):
        titre = scene_title("L'essentiel du chapitre — La gamétogénèse")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : rappel du fil conducteur -----------------------------------
        intro = Text(
            _wrap(
                "Nous avons répondu aux trois questions du départ : les "
                "gamètes viennent des gonades, où la méiose les fabrique "
                "en réduisant et en brassant les chromosomes, et les "
                "quantités diffèrent parce que la spermatogenèse est "
                "continue tandis que l'ovogenèse est cyclique.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Nous avons maintenant répondu aux trois questions posées "
                "au début du chapitre. Les cellules reproductrices "
                "viennent des gonades, testicules et ovaires ; elles s'y "
                "forment grâce à la méiose, qui réduit de moitié le nombre "
                "de chromosomes tout en brassant le patrimoine héréditaire "
                "; et les quantités produites diffèrent tant parce que la "
                "spermatogenèse est continue, alors que l'ovogenèse est "
                "cyclique et fortement limitée par le stock de follicules."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement + exemple + à retenir : synthèse en boîte essentiel ---
        essentiel = essentiel_box(
            _bullets(
                [
                    "Gamétogénèse : formation des gamètes — spermatogenèse "
                    "(tubes séminifères) et ovogenèse (follicules).",
                    "Gamètes haploïdes (n=23) ; fécondation rétablit la "
                    "diploïdie (n+n=2n=46) dans la cellule œuf.",
                    "Méiose : 2 divisions — méiose I sépare les homologues, "
                    "méiose II sépare les chromatides. 1 cellule 2n → 4 "
                    "cellules n.",
                    "Brassage inter- et intrachromosomique (crossing-over) "
                    "-> 2^23=8 388 608 types de gamètes par individu.",
                    "Spermatogenèse (4 phases) : 1 spermatocyte I → 4 "
                    "spermatozoïdes. Ovogenèse (division inégale) : 1 "
                    "ovocyte I → 1 ovule + 3 globules polaires.",
                    "Spermatozoïde (60 µm) : tête (noyau+acrosome), col, "
                    "pièce intermédiaire, flagelle. Ovule (120 µm) : "
                    "vitellus + zone pellucide.",
                    "Spermatogenèse continue dès la puberté (~70 j) ; "
                    "ovogenèse discontinue, 2 blocages (prophase I, "
                    "métaphase II levé si fécondation).",
                    "Stock folliculaire : ~2 millions à la naissance, "
                    "400 000 à la puberté, <500 ovulés dans une vie.",
                    "Hormones : FSH (Sertoli / croissance des follicules), "
                    "LH (Leydig → testostérone / pic déclenchant "
                    "l'ovulation), rétrocontrôle par les gonades.",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si les 9 points débordent du cadre visible malgré le
        # petit corps de police, on réduit l'échelle globale de la boîte
        # (ancrage en haut) pour qu'elle tienne entièrement à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. La gamétogénèse est la "
                "formation des gamètes : la spermatogenèse dans les tubes "
                "séminifères des testicules, l'ovogenèse dans les "
                "follicules des ovaires. Les gamètes sont haploïdes, n "
                "égale vingt-trois chez l'homme ; la fécondation rétablit "
                "la diploïdie, n plus n égale deux n égale quarante-six, "
                "dans la cellule œuf. La méiose comporte deux divisions : "
                "la méiose un sépare les chromosomes homologues, la méiose "
                "deux sépare les chromatides sœurs ; une cellule à deux n "
                "donne quatre cellules à n. En prophase un, les homologues "
                "s'apparient en bivalents, et un crossing-over peut "
                "échanger des fragments : ce double brassage, "
                "interchromosomique et intrachromosomique, donne deux "
                "puissance vingt-trois, soit huit millions trois cent "
                "quatre-vingt-huit mille six cent huit types de gamètes par "
                "individu, bien davantage en réalité. La spermatogenèse "
                "comporte quatre phases, multiplication, accroissement, "
                "maturation, différenciation ; un spermatocyte du premier "
                "ordre donne quatre spermatozoïdes. L'ovogenèse, par "
                "divisions inégales, ne donne qu'un ovule et trois globules "
                "polaires par ovocyte du premier ordre. Le spermatozoïde, "
                "soixante micromètres, comporte une tête avec noyau et "
                "acrosome, un col, une pièce intermédiaire riche en "
                "mitochondries, et un flagelle ; l'ovule, cent vingt "
                "micromètres, comporte un vitellus riche en réserves "
                "entouré de la zone pellucide. La spermatogenèse est "
                "continue dès la puberté, avec un cycle d'environ soixante-"
                "dix jours ; l'ovogenèse est discontinue, commencée avant "
                "la naissance, avec deux blocages de la méiose, en prophase "
                "un puis en métaphase deux, levé seulement en cas de "
                "fécondation. Le stock folliculaire passe d'environ deux "
                "millions d'ovocytes à la naissance à quatre cent mille à "
                "la puberté, et moins de cinq cents seront finalement "
                "ovulés au cours de la vie. Enfin, deux hormones "
                "contrôlent la gamétogénèse : la FSH, qui stimule les "
                "cellules de Sertoli et la croissance des follicules, et la "
                "LH, qui stimule les cellules de Leydig, productrices de "
                "testostérone, et déclenche le pic d'ovulation ; les "
                "hormones des gonades exercent en retour un rétrocontrôle "
                "sur l'hypophyse."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
