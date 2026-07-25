"""
scenes/SVT_SyntheseProteines_02.py — Chapitre 5 (1ereD, SVT), scène 02.

§ 5.1 Du gène à la protéine : rappel protéine = chaîne d'acides aminés,
définition du gène, remarque historique « un gène, une enzyme », le dogme
central de la biologie moléculaire, exemple de la tyrosinase et de
l'albinisme, attention à la démarche caractère -> protéine -> gène.
Source : 1ereD/SVT.pdf, pages 63-65.
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
    Arrow,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class DuGeneALaProteine(NotionScene):
    def construct(self):
        titre = scene_title("5.1 — Du gène à la protéine")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : rappel protéine = chaîne d'acides aminés ------------
        def_proteine = definition_box(
            Text(
                _wrap(
                    "Une protéine est une grande molécule formée par "
                    "l'enchaînement, dans un ordre précis, de petites "
                    "molécules appelées acides aminés. Il existe 20 sortes "
                    "d'acides aminés. L'ordre dans lequel ils s'enchaînent "
                    "constitue la séquence de la protéine : c'est elle qui "
                    "détermine sa forme dans l'espace, et donc sa fonction.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        def_proteine.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappelons ce qu'est une protéine. Une protéine est une "
                "grande molécule formée par l'enchaînement, dans un ordre "
                "précis, de petites molécules appelées acides aminés. Il "
                "existe vingt sortes d'acides aminés. L'ordre dans lequel "
                "ils s'enchaînent constitue la séquence de la protéine : "
                "c'est elle qui détermine la forme de la protéine dans "
                "l'espace, et donc sa fonction."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_proteine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_proteine))

        exemples_proteines = _bullets(
            [
                "Hémoglobine (globules rouges) : transporte le dioxygène.",
                "Amylase de la salive : digère l'amidon du riz, de l'attiéké.",
                "Kératine : constitue les cheveux et les ongles.",
                "Anticorps : défendent l'organisme contre les microbes.",
                "Insuline : 51 acides aminés. Une chaîne d'hémoglobine : "
                "146 acides aminés.",
            ],
            width=52,
        )
        exemples_proteines.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Les protéines sont partout dans notre vie quotidienne. "
                "L'hémoglobine, contenue dans les globules rouges, "
                "transporte le dioxygène dans le sang. L'amylase de la "
                "salive est une enzyme qui commence la digestion de "
                "l'amidon du riz ou de l'attiéké. La kératine constitue les "
                "cheveux et les ongles. Les anticorps défendent l'organisme "
                "contre les microbes. Une protéine peut comporter de "
                "quelques dizaines à plusieurs milliers d'acides aminés : "
                "l'insuline en comporte cinquante et un, une chaîne "
                "d'hémoglobine en comporte cent quarante-six. Avec vingt "
                "sortes d'acides aminés, le nombre d'enchaînements "
                "possibles est immense : c'est ce qui explique l'immense "
                "diversité des protéines."
            )
        ) as tracker:
            self.play(FadeIn(exemples_proteines))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples_proteines))

        # --- Raisonnement : le gène et le dogme central --------------------
        def_gene = definition_box(
            Text(
                _wrap(
                    "Un gène est un fragment d'ADN qui contient "
                    "l'information nécessaire à la fabrication d'une "
                    "chaîne polypeptidique (une chaîne d'acides aminés). "
                    "Chaque gène occupe une place précise, appelée locus, "
                    "sur un chromosome. L'information est portée par la "
                    "séquence de ses nucléotides.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        def_gene.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "D'où vient l'ordre des acides aminés dans une protéine ? "
                "Ce n'est pas le hasard : cet ordre est écrit dans l'ADN des "
                "chromosomes, sous forme de messages appelés gènes. Un gène "
                "est un fragment d'ADN qui contient l'information "
                "nécessaire à la fabrication d'une chaîne polypeptidique. "
                "Chaque gène occupe une place précise, appelée locus, sur "
                "un chromosome. L'information du gène est portée par la "
                "séquence de ses nucléotides, c'est-à-dire l'ordre des "
                "bases A, T, G, C le long du brin."
            )
        ) as tracker:
            self.play(FadeIn(def_gene))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_gene))

        remarque_histoire = warning_box(
            Text(
                _wrap(
                    "Un peu d'histoire. Dès 1909, Archibald Garrod soupçonne "
                    "un lien entre hérédité et enzymes. En 1941, Beadle et "
                    "Tatum montrent qu'un gène abîmé entraîne la perte "
                    "d'une seule enzyme : hypothèse « un gène, une "
                    "enzyme », devenue « un gène, une chaîne "
                    "polypeptidique » (prix Nobel 1958).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        remarque_histoire.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un peu d'histoire. Dès 1909, le médecin anglais Archibald "
                "Garrod observe que certaines maladies familiales sont des "
                "erreurs innées du métabolisme, et soupçonne un lien entre "
                "hérédité et enzymes. En 1941, les Américains George Beadle "
                "et Edward Tatum, en travaillant sur une moisissure du "
                "pain, montrent qu'un gène abîmé par rayonnement entraîne "
                "toujours la perte d'une seule enzyme. Ils formulent alors "
                "l'hypothèse célèbre : un gène, une enzyme, devenue "
                "ensuite un gène, une chaîne polypeptidique. Cette "
                "découverte a été récompensée par le prix Nobel en mille "
                "neuf cent cinquante-huit."
            )
        ) as tracker:
            self.play(FadeIn(remarque_histoire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_histoire))

        # --- Le dogme central : property_box + schéma flèches --------------
        dogme = property_box(
            Text(
                _wrap(
                    "Le dogme central : l'information génétique circule "
                    "dans un sens précis. 1) La transcription : l'ADN d'un "
                    "gène est recopié en ARN messager, dans le noyau. 2) "
                    "La traduction : l'ARNm est lu dans le cytoplasme pour "
                    "assembler les acides aminés et former la protéine. "
                    "L'ADN se duplique aussi avant chaque division : la "
                    "réplication.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        dogme.next_to(titre, DOWN, buff=0.45)

        adn_txt = Text("ADN", font_size=28, color=YELLOW, weight="BOLD")
        arnm_txt = Text("ARNm", font_size=28, color=WHITE, weight="BOLD")
        prot_txt = Text("Protéine", font_size=28, color=ORANGE, weight="BOLD")
        chaine = VGroup(adn_txt, arnm_txt, prot_txt).arrange(RIGHT, buff=1.6)
        chaine.next_to(dogme, DOWN, buff=0.5)
        fleche1 = Arrow(adn_txt.get_right(), arnm_txt.get_left(), buff=0.15, color=WHITE)
        fleche2 = Arrow(arnm_txt.get_right(), prot_txt.get_left(), buff=0.15, color=WHITE)
        label1 = Text("transcription", font_size=18, color=WHITE).next_to(fleche1, UP, buff=0.1)
        label2 = Text("traduction", font_size=18, color=WHITE).next_to(fleche2, UP, buff=0.1)
        schema = VGroup(chaine, fleche1, fleche2, label1, label2)

        with self.voiceover(
            text=(
                "Le gène est dans le noyau, mais les protéines sont "
                "fabriquées dans le cytoplasme. L'information doit donc "
                "voyager. En 1958, Francis Crick résume le sens de "
                "circulation de l'information génétique dans la cellule : "
                "c'est le dogme central de la biologie moléculaire. "
                "Première étape, la transcription : l'information d'un "
                "gène est recopiée sous forme d'une molécule d'ARN "
                "messager, dans le noyau. Deuxième étape, la traduction : "
                "l'ARNm est lu dans le cytoplasme pour assembler les "
                "acides aminés dans le bon ordre et former la protéine. "
                "L'information passe donc de l'ADN à l'ARN, puis de l'ARN à "
                "la protéine. De plus, l'ADN est capable de se dupliquer "
                "avant chaque division cellulaire : c'est la réplication."
            )
        ) as tracker:
            self.play(FadeIn(dogme))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(dogme), FadeOut(schema))

        # --- Exemple traité : la tyrosinase et la couleur de la peau -------
        exemple = example_box(
            Text(
                _wrap(
                    "La mélanine (pigment de la peau) est fabriquée grâce à "
                    "la tyrosinase, une enzyme. Un individu albinos a un "
                    "gène de la tyrosinase modifié : il ne permet plus de "
                    "fabriquer une enzyme active. Sans tyrosinase active, "
                    "pas de mélanine, donc une peau dépourvue de pigment.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons un exemple. La mélanine, pigment qui donne sa "
                "couleur à la peau et protège du soleil, est fabriquée "
                "grâce à une enzyme appelée tyrosinase. Certaines personnes "
                "naissent albinos : leur peau et leurs cheveux sont très "
                "clairs. Comment l'expliquer avec la relation gène-"
                "protéine ? La tyrosinase est une protéine : sa fabrication "
                "est donc commandée par un gène. Chez une personne albinos, "
                "le gène de la tyrosinase est modifié : l'information "
                "qu'il porte ne permet plus de fabriquer une enzyme active. "
                "Sans tyrosinase active, la mélanine n'est pas produite, et "
                "la peau reste dépourvue de pigment. On retrouve la chaîne "
                "complète : gène modifié, puis enzyme inactive, puis "
                "absence de pigment, et enfin caractère visible."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir / piège : la démarche de raisonnement ---------------
        demarche = warning_box(
            Text(
                _wrap(
                    "Ce qu'il faut retenir de la démarche : pour expliquer "
                    "un caractère observable (couleur, maladie, groupe "
                    "sanguin...), on remonte toujours la même chaîne : le "
                    "caractère dépend d'une protéine, qui dépend d'un "
                    "gène. Toute explication doit suivre cet ordre "
                    "logique : gène -> protéine -> caractère.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        demarche.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons bien la démarche. Quand on explique un caractère "
                "observable, une couleur, une maladie, un groupe sanguin, "
                "on remonte toujours la même chaîne : le caractère dépend "
                "d'une protéine, qui dépend d'un gène. Toute l'explication "
                "doit suivre cet ordre logique, du gène vers la protéine, "
                "puis vers le caractère."
            )
        ) as tracker:
            self.play(FadeIn(demarche))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(demarche))
