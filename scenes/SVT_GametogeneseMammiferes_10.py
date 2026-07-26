"""
scenes/SVT_GametogeneseMammiferes_10.py — Chapitre 3 (1ereC, SVT), scène 10.

Méthodes et astuces : les trois méthodes (restituer les étapes en 4
temps, ne jamais confondre les deux blocages avec le moyen mnémotechnique
« Prophase Puberté, Métaphase Mariage », analyser un spermogramme) ; les
quatre pièges classiques ; puis L'ESSENTIEL DU CHAPITRE, en clôture.
Source : 1ereC/SVT.pdf, pages 32-33 (synthèse de fin de chapitre).
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class MethodesEtEssentielDuChapitre(NotionScene):
    def construct(self):
        titre = scene_title("3.10 — Méthodes, pièges et essentiel du chapitre")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : méthode 1, restituer les étapes en 4 temps -----------------
        methode1 = method_box(
            Text(
                _wrap(
                    "Pour toute question « Décrire la spermatogenèse / "
                    "l'ovogenèse », répondre TOUJOURS en 4 temps : "
                    "1) localisation (tubule séminifère / follicule "
                    "ovarique) ; 2) étapes nommées dans l'ordre, avec la "
                    "ploïdie de chaque cellule ; 3) bilan quantitatif "
                    "(1→4 spz ; 1→1 ovule + globules polaires) ; "
                    "4) rythme (continu/cyclique) et période d'activité.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.4,
        )
        methode1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici trois méthodes à mobiliser systématiquement. "
                "Méthode un : restituer les étapes de la gamétogénèse. "
                "Pour toute question décrire la spermatogenèse ou "
                "l'ovogenèse, répondre toujours selon le même plan en "
                "quatre temps. Un : la localisation, tubule séminifère ou "
                "follicule ovarique. Deux : les étapes nommées dans "
                "l'ordre, avec la ploïdie de chaque cellule, deux n ou n. "
                "Trois : le bilan quantitatif, un spermatocyte premier "
                "donnant quatre spermatozoïdes, un ovocyte premier donnant "
                "un ovule et des globules polaires. Quatre : le rythme, "
                "continu ou cyclique, et la période d'activité. Une "
                "réponse qui mélange les étapes, par exemple placer la "
                "spermiogenèse avant la méiose, est lourdement pénalisée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Animation du raisonnement : méthode 2, les deux blocages ------------
        methode2 = method_box(
            Text(
                _wrap(
                    "Ne jamais confondre les deux blocages de "
                    "l'ovogenèse : vie fœtale → blocage en prophase I "
                    "— puberté, à chaque cycle → fin de la méiose I — "
                    "blocage en métaphase II (ovulation) → achèvement "
                    "SI fécondation. Mnémotechnique : « Prophase "
                    "Puberté, Métaphase Mariage (rencontre) » — le "
                    "premier blocage saute à la puberté, le second ne "
                    "saute que lors de la rencontre avec le "
                    "spermatozoïde.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.4,
        )
        methode2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Méthode deux : ne jamais confondre les deux blocages de "
                "l'ovogenèse. Retenons la chronologie : dès la vie "
                "fœtale, blocage en prophase de méiose un ; à la puberté, "
                "à chaque cycle, la méiose un s'achève enfin ; survient "
                "alors un second blocage, en métaphase de méiose deux, au "
                "moment de l'ovulation ; l'achèvement complet n'a lieu que "
                "s'il y a fécondation. Moyen mnémotechnique : prophase "
                "puberté, métaphase mariage, pour rencontre. Le premier "
                "blocage saute à la puberté, le second ne saute que lors "
                "de la rencontre avec le spermatozoïde."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Exemple traité : méthode 3, analyser un spermogramme ---------------
        methode3 = method_box(
            Text(
                _wrap(
                    "Analyser un spermogramme : confronter chaque "
                    "paramètre aux valeurs de référence, puis nommer "
                    "l'anomalie par son terme médical exact — "
                    "oligospermie (nombre), asthénospermie (mobilité), "
                    "tératospermie (formes), azoospermie (absence). "
                    "Conclure en reliant le défaut à l'étape de la "
                    "spermatogenèse concernée (ex : défaut de "
                    "mitochondries → asthénospermie).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.4,
        )
        methode3.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Méthode trois : analyser un spermogramme. Confronter "
                "chaque paramètre aux valeurs de référence, puis nommer "
                "l'anomalie par son terme médical exact : oligospermie "
                "pour le nombre, asthénospermie pour la mobilité, "
                "tératospermie pour les formes, azoospermie pour "
                "l'absence totale. Conclure sur la fécondité en reliant le "
                "défaut observé à l'étape de la spermatogenèse concernée : "
                "par exemple, un défaut de mitochondries dans la pièce "
                "intermédiaire explique une asthénospermie, car "
                "l'énergie manque pour faire battre le flagelle."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Pièges à éviter : les 4 confusions classiques -----------------------
        entete_pieges = Text("Les 4 pièges classiques", font_size=25, color=YELLOW, weight="BOLD")
        entete_pieges.next_to(titre, DOWN, buff=0.4)

        pieges = warning_box(
            _bullets(
                [
                    "1) Confondre ovocyte et ovule : la cellule expulsée "
                    "à l'ovulation est un ovocyte II bloqué en métaphase "
                    "II, pas un ovule terminé.",
                    "2) Croire que la méiose produit 4 gamètes dans les "
                    "deux sexes : chez la femelle, 3 des 4 cellules sont "
                    "des globules polaires qui dégénèrent.",
                    "3) Inverser acrosome et vitellus : l'acrosome est "
                    "au spermatozoïde, le vitellus est à l'ovule ; la "
                    "zone pellucide entoure toujours l'ovule.",
                    "4) Confondre puberté et début de la multiplication : "
                    "chez l'homme, tout commence à la puberté ; chez la "
                    "femme, multiplication et 1er blocage sont "
                    "prénataux, la puberté ne fait que reprendre la "
                    "méiose.",
                ],
                font_size=18,
                width=50,
            ),
            box_width=12.6,
        )
        pieges.next_to(entete_pieges, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Récapitulons les quatre pièges classiques à éviter à "
                "tout prix. Premier piège : confondre ovocyte et ovule ; "
                "la cellule expulsée à l'ovulation est un ovocyte de "
                "second ordre, bloqué en métaphase deux, pas un ovule "
                "terminé. Deuxième piège : croire que la méiose produit "
                "quatre gamètes dans les deux sexes ; chez la femelle, "
                "trois des quatre cellules sont des globules polaires qui "
                "dégénèrent. Troisième piège : inverser acrosome et "
                "vitellus ; l'acrosome appartient au spermatozoïde, le "
                "vitellus appartient à l'ovule, et la zone pellucide "
                "entoure toujours l'ovule. Quatrième piège : confondre "
                "puberté et début de la multiplication ; chez l'homme, "
                "tout commence à la puberté, mais chez la femme, la "
                "multiplication des ovogonies et le premier blocage sont "
                "prénataux, la puberté ne faisant que reprendre la "
                "méiose. Question classique de devoir de niveau !"
            )
        ) as tracker:
            self.play(FadeIn(entete_pieges))
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pieges), FadeOut(pieges))

        # --- L'ESSENTIEL DU CHAPITRE (clôture) -------------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Gamétogénèse : formation des gamètes haploïdes (n) "
                    "à partir des cellules germinales diploïdes (2n) des "
                    "gonades — spermatogenèse (testicules) / ovogenèse "
                    "(ovaires).",
                    "Spermatogenèse : 4 phases (multiplication, "
                    "croissance, méiose, spermiogenèse) ; 1 spermatocyte "
                    "I → 4 spermatozoïdes ; continue, ~70-75 j, de la "
                    "puberté à la vieillesse.",
                    "Ovogenèse : multiplication fœtale (unique), "
                    "blocage en prophase I, reprise cyclique à la "
                    "puberté, 2e blocage en métaphase II ; 1 ovocyte I "
                    "→ 1 ovule + globules polaires dégénérés ; "
                    "discontinue, jusqu'à la ménopause.",
                    "Spermatozoïde : tête (noyau + acrosome), pièce "
                    "intermédiaire (mitochondries), flagelle "
                    "(locomotion) — cellule du voyage.",
                    "Ovule : membrane, cytoplasme/vitellus, noyau, zone "
                    "pellucide, couronne radiée — cellule des réserves.",
                    "Fécondité : spermogramme (normes OMS) pour "
                    "l'homme ; ovulation, trompes, utérus pour la "
                    "femme ; IST non traitées = 1re cause évitable "
                    "d'infécondité.",
                ],
                font_size=17,
                width=52,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si le contenu dépasse la hauteur visible du cadre,
        # on réduit l'échelle globale de la boîte pour qu'elle tienne
        # entièrement à l'écran (pattern SVT_FonctionsGonades_09.py).
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. La gamétogénèse forme des "
                "gamètes haploïdes à partir des cellules germinales "
                "diploïdes des gonades : spermatogenèse dans les "
                "testicules, ovogenèse dans les ovaires. La "
                "spermatogenèse comporte quatre phases, multiplication, "
                "croissance, méiose et spermiogenèse ; un spermatocyte "
                "premier donne quatre spermatozoïdes, en continu, de la "
                "puberté à la vieillesse, en environ soixante-dix à "
                "soixante-quinze jours. L'ovogenèse débute par une "
                "multiplication uniquement fœtale, se bloque en prophase "
                "un, reprend à chaque cycle à partir de la puberté, se "
                "bloque une seconde fois en métaphase deux ; un ovocyte "
                "premier ne donne qu'un seul ovule et des globules "
                "polaires dégénérés, de façon discontinue, jusqu'à la "
                "ménopause. Le spermatozoïde, cellule du voyage, associe "
                "tête, pièce intermédiaire et flagelle ; l'ovule, cellule "
                "des réserves, associe membrane, cytoplasme chargé de "
                "vitellus, noyau, zone pellucide et couronne radiée. "
                "Enfin, la fécondité s'évalue par le spermogramme chez "
                "l'homme, et par l'ovulation, les trompes et l'utérus chez "
                "la femme ; les infections sexuellement transmissibles non "
                "traitées restent la première cause évitable "
                "d'infécondité."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
