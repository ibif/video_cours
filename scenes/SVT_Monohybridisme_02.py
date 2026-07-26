"""
scenes/SVT_Monohybridisme_02.py — Chapitre 4 (1ereD, SVT), scène 02.

§ 4.1 Les notions de base : caractère héréditaire, gène et allèles
(4.1.1-4.1.3) : définition du caractère héréditaire, gène/locus, allèles,
notation V/v, du gène aux gamètes, exemple des génotypes/gamètes possibles,
attention caractère acquis vs héréditaire. Source : 1ereD/SVT.pdf, pages
47-49.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class NotionsDeBaseCaractereGeneAlleles(NotionScene):
    def construct(self):
        titre = scene_title("4.1 — Caractère héréditaire, gène et allèles")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : qu'est-ce qu'un caractère héréditaire ? ------------------
        definition_car = definition_box(
            Text(
                _wrap(
                    "Un caractère héréditaire est une particularité d'un "
                    "individu (morphologique, physiologique ou "
                    "biochimique) qui peut être transmise à sa "
                    "descendance au cours de la reproduction.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        definition_car.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Qu'est-ce qu'un caractère héréditaire ? C'est une "
                "particularité d'un individu, morphologique, physiologique "
                "ou biochimique, qui peut être transmise à sa descendance au "
                "cours de la reproduction."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_car))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_car))

        exemples_car = _bullets(
            [
                "Végétaux : couleur des grains de maïs, couleur des "
                "fleurs, forme des graines de pois (lisses/ridées).",
                "Animaux : couleur du pelage, forme des oreilles, "
                "couleur des yeux.",
                "Homme : couleur de la peau, groupe sanguin, "
                "pigmentation normale ou albinisme.",
                "Chaque forme d'un caractère (ex. violette ou blanche) "
                "est appelée une modalité du caractère.",
            ],
            font_size=22,
            width=54,
        )
        exemples_car.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quelques exemples. Chez les végétaux : la couleur des "
                "grains de maïs, la couleur des fleurs, la forme des "
                "graines de pois, lisses ou ridées. Chez les animaux : la "
                "couleur du pelage, la forme des oreilles, la couleur des "
                "yeux. Chez l'Homme : la couleur de la peau, le groupe "
                "sanguin, la pigmentation normale ou l'albinisme. À "
                "l'échelle d'un même caractère, on observe souvent "
                "plusieurs formes : chaque forme, comme violette ou "
                "blanche pour la couleur de la fleur du pois, est appelée "
                "une modalité du caractère."
            )
        ) as tracker:
            self.play(FadeIn(exemples_car))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples_car))

        # --- Animation du raisonnement : gène, locus, allèles ------------------
        definition_gene = definition_box(
            Text(
                _wrap(
                    "Un gène est un fragment de chromosome (une portion "
                    "de la molécule d'ADN) qui commande l'expression "
                    "d'un caractère héréditaire. Le locus est la place "
                    "précise qu'occupe un gène sur un chromosome.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition_gene.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un gène est un fragment de chromosome, plus précisément "
                "une portion de la molécule d'ADN, qui commande "
                "l'expression d'un caractère héréditaire. La place précise "
                "qu'occupe un gène sur un chromosome s'appelle le locus."
            )
        ) as tracker:
            self.play(FadeIn(definition_gene))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_gene))

        definition_alleles = definition_box(
            Text(
                _wrap(
                    "Les allèles sont les différentes versions possibles "
                    "d'un même gène. Un individu diploïde possède deux "
                    "allèles par gène : l'un venu du père, l'autre venu "
                    "de la mère, portés par les deux chromosomes "
                    "homologues de la paire.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition_alleles.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les allèles sont les différentes versions possibles d'un "
                "même gène. Un individu diploïde possède ses chromosomes "
                "par paires de chromosomes homologues, portant les mêmes "
                "gènes aux mêmes locus. Pour chaque gène, il possède donc "
                "deux allèles : l'un situé sur le chromosome reçu du père, "
                "l'autre sur le chromosome reçu de la mère. Reprenons le "
                "maïs de l'introduction : le gène couleur du grain existe "
                "sous deux versions, violet et blanc — ce sont ses deux "
                "allèles."
            )
        ) as tracker:
            self.play(FadeIn(definition_alleles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_alleles))

        notation_titre = Text("Notation des allèles et des génotypes", font_size=27, color=YELLOW, weight="BOLD")
        notation_titre.next_to(titre, DOWN, buff=0.5)

        notation_txt = Text(
            _wrap(
                "Majuscule pour l'allèle dominant, minuscule pour "
                "l'allèle récessif ; les deux allèles d'un individu "
                "s'écrivent côte à côte, séparés par une barre oblique. "
                "Pour le maïs : V (violet) et v (blanc).",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        notation_txt.next_to(notation_titre, DOWN, buff=0.35)

        genotypes_possibles = MathTex(r"V/V \qquad V/v \qquad v/v", font_size=34, color=YELLOW)
        genotypes_possibles.next_to(notation_txt, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Par convention, on note un allèle par une lettre : une "
                "majuscule pour l'allèle qui s'impose, l'allèle dominant, "
                "une minuscule pour l'allèle qui s'efface, l'allèle "
                "récessif. Les deux allèles d'un individu s'écrivent côte à "
                "côte, séparés par une barre oblique. Pour le maïs, on note "
                "V l'allèle violet et v l'allèle blanc : un plant peut alors "
                "être V sur V, V sur v, ou v sur v."
            )
        ) as tracker:
            self.play(FadeIn(notation_titre))
            self.play(FadeIn(notation_txt))
            self.play(Write(genotypes_possibles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(notation_titre), FadeOut(notation_txt), FadeOut(genotypes_possibles))

        gametes_titre = Text("Du gène aux gamètes", font_size=27, color=YELLOW, weight="BOLD")
        gametes_titre.next_to(titre, DOWN, buff=0.5)

        gametes_txt = Text(
            _wrap(
                "À la méiose, les deux chromosomes de chaque paire se "
                "séparent : chaque gamète ne reçoit qu'un seul des deux "
                "allèles de chaque gène. C'est le cœur de toute la "
                "génétique de ce chapitre.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        gametes_txt.next_to(gametes_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Lors de la méiose, les deux chromosomes de chaque paire se "
                "séparent : chaque gamète ne reçoit qu'un seul chromosome "
                "de la paire, donc un seul des deux allèles de chaque gène. "
                "Un plant V sur V ne produit que des gamètes portant V ; un "
                "plant v sur v ne produit que des gamètes portant v ; un "
                "plant V sur v produit deux sortes de gamètes en quantités "
                "égales, la moitié portant V, l'autre moitié portant v. Ce "
                "point est le cœur de toute la génétique de ce chapitre : "
                "c'est lui qui explique les proportions observées dans les "
                "descendances."
            )
        ) as tracker:
            self.play(FadeIn(gametes_titre))
            self.play(FadeIn(gametes_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(gametes_titre), FadeOut(gametes_txt))

        # --- Exemple traité : génotypes possibles et gamètes produits ----------
        exemple = example_box(
            Text(
                _wrap(
                    "Pour le gène couleur du grain (allèles V et v), 3 "
                    "génotypes existent : V/V, V/v, v/v. Gamètes "
                    "produits : V/V -> 100% V ; v/v -> 100% v ; V/v -> "
                    "1/2 V et 1/2 v. Seul le génotype V/v produit deux "
                    "types de gamètes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dressons la liste complète des situations pour le gène "
                "couleur du grain de maïs, allèles V et v. Étape un : les "
                "génotypes possibles. Un plant possède deux allèles pris "
                "parmi V et v : il y a donc trois possibilités, V sur V, V "
                "sur v et v sur v. Étape deux : les gamètes produits par "
                "chacun. Le plant V sur V possède deux fois l'allèle V : "
                "cent pour cent de ses gamètes portent V. Le plant v sur v "
                "possède deux fois l'allèle v : cent pour cent de ses "
                "gamètes portent v. Le plant V sur v possède un allèle de "
                "chaque sorte : un demi de ses gamètes portent V et un demi "
                "portent v. Conclusion : il existe trois génotypes "
                "possibles, et seul le génotype V sur v produit deux types "
                "de gamètes. Retenez cette dernière phrase : elle sera "
                "utilisée dans tous les exercices du chapitre."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : vocabulaire de la section ------------------------------
        entete_vocab = Text("Vocabulaire à retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_vocab.next_to(titre, DOWN, buff=0.5)

        vocab = _bullets(
            [
                "Caractère héréditaire : particularité transmissible "
                "(ex. couleur du grain).",
                "Modalité : forme prise par un caractère (ex. violet ou "
                "blanc).",
                "Gène : portion de chromosome commandant un caractère.",
                "Locus : place du gène sur le chromosome.",
                "Allèles : versions différentes d'un même gène (ex. V "
                "et v).",
            ],
            font_size=21,
            width=54,
        )
        vocab.next_to(entete_vocab, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons le vocabulaire de cette première section. "
                "Caractère héréditaire : particularité transmissible aux "
                "descendants, par exemple la couleur du grain chez le "
                "maïs. Modalité : forme prise par un caractère, par exemple "
                "violet ou blanc. Gène : portion de chromosome commandant "
                "un caractère. Locus : place du gène sur le chromosome. "
                "Allèles : versions différentes d'un même gène, ici V et v."
            )
        ) as tracker:
            self.play(FadeIn(entete_vocab))
            self.play(FadeIn(vocab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_vocab), FadeOut(vocab))

        # --- Piège à éviter : caractère héréditaire vs caractère acquis --------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre caractère héréditaire et caractère "
                    "acquis. Un caractère acquis (musculature développée "
                    "par le sport, cicatrice, bronzage, langue parlée) ne "
                    "se transmet PAS aux descendants. Toujours vérifier "
                    "que le caractère étudié est bien héréditaire avant "
                    "de raisonner.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre caractère héréditaire et "
                "caractère acquis. Un caractère acquis est obtenu au cours "
                "de la vie, sous l'effet du milieu ou de l'activité de "
                "l'individu : musculature développée par le sport, "
                "cicatrice, bronzage, langue parlée. Un caractère acquis ne "
                "se transmet pas aux descendants : le fils d'un champion de "
                "lutte traditionnelle ne naît pas musclé. Seuls les "
                "caractères héréditaires, inscrits dans les chromosomes, se "
                "transmettent. C'est une erreur très fréquente dans les "
                "copies : avant de raisonner, toujours vérifier que le "
                "caractère étudié est bien héréditaire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
