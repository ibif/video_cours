"""
scenes/SVT_GametogeneseMammiferes_09.py — Chapitre 3 (1ereC, SVT), scène 09.

Les notions de fécondité : définitions (fécondité, fertilité,
fécondabilité, fécond/infécond/stérile) ; le spermogramme (tableau des
valeurs OMS et anomalies) ; causes d'infécondité masculine et féminine ;
période de fécondité et contraception (contexte ivoirien : IST non
traitées, dépistage).
Source : 1ereC/SVT.pdf, pages 31-33.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class NotionsDeFecondite(NotionScene):
    def construct(self):
        titre = scene_title("3.9 — Les notions de fécondité")
        titre.scale(0.72)
        titre.to_edge(UP)

        # --- Énoncé : définitions -------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La fécondité est l'aptitude d'un individu ou d'un "
                    "couple à se reproduire, c'est-à-dire à produire des "
                    "gamètes fonctionnels capables de donner une "
                    "descendance — à distinguer de la fertilité, qui "
                    "mesure la réalisation effective de naissances. "
                    "Fécondabilité : probabilité de conception par cycle "
                    "(~20-25 % chez un couple jeune et fertile).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La fécondité est l'aptitude d'un individu ou d'un couple "
                "à se reproduire, c'est-à-dire à produire des gamètes "
                "fonctionnels capables de donner une descendance. Elle se "
                "distingue de la fertilité, qui mesure la réalisation "
                "effective de naissances dans une population. On appelle "
                "fécondabilité la probabilité de conception par cycle, "
                "environ vingt à vingt-cinq pour cent chez un couple jeune "
                "et fertile. Un individu capable de procréer est dit "
                "fécond ; incapable de procréer de façon durable, il est "
                "dit infécond, ou stérile si c'est définitif."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : le spermogramme ---------------------------
        entete_sperm = Text("Le spermogramme (normes OMS)", font_size=23, color=YELLOW, weight="BOLD")
        entete_sperm.next_to(titre, DOWN, buff=0.4)

        spermogramme = _bullets(
            [
                "Volume de l'éjaculat ≥1,5 mL — sinon : hypospermie",
                "Concentration ≥15-20 millions/mL — sinon : "
                "oligospermie",
                "Nombre total par éjaculat ≥39 millions — sinon : "
                "oligospermie sévère",
                "Mobilité ≥32 % de spermatozoïdes mobiles — sinon : "
                "asthénospermie",
                "Formes normales ≥4 % — sinon : tératospermie",
                "Absence totale de spermatozoïdes : azoospermie "
                "(stérilité)",
            ],
            font_size=19,
            width=50,
        )
        spermogramme.next_to(entete_sperm, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "La fécondité masculine est évaluée par le spermogramme, "
                "un examen qui analyse un échantillon de sperme selon les "
                "normes de l'Organisation mondiale de la santé. Le volume "
                "de l'éjaculat doit être supérieur ou égal à un virgule "
                "cinq millilitre, sinon on parle d'hypospermie. La "
                "concentration doit atteindre au moins quinze à vingt "
                "millions de spermatozoïdes par millilitre, sinon "
                "c'est une oligospermie. Le nombre total par éjaculat doit "
                "dépasser trente-neuf millions. La mobilité doit concerner "
                "au moins trente-deux pour cent des spermatozoïdes, sinon "
                "c'est une asthénospermie. Les formes normales doivent "
                "représenter au moins quatre pour cent, sinon c'est une "
                "tératospermie. Et l'absence totale de spermatozoïdes est "
                "appelée azoospermie, une cause de stérilité."
            )
        ) as tracker:
            self.play(FadeIn(entete_sperm))
            self.play(FadeIn(spermogramme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_sperm), FadeOut(spermogramme))

        # --- Raisonnement (suite) : causes d'infécondité --------------------------
        entete_causes = Text("Causes d'infécondité", font_size=23, color=YELLOW, weight="BOLD")
        entete_causes.next_to(titre, DOWN, buff=0.4)

        causes_m_titre = Text("Chez l'homme", font_size=20, color=YELLOW, weight="BOLD")
        causes_m = _bullets(
            [
                "Troubles de la spermatogenèse : cryptorchidie, "
                "varicocèle, infections (oreillons), chaleur/toxiques.",
                "Obstacles sur les voies excrétrices (ligature, "
                "infection des canaux déférents).",
                "Troubles hormonaux : FSH/LH ou testostérone "
                "insuffisantes.",
            ],
            font_size=16,
            width=32,
        )
        causes_m_bloc = VGroup(causes_m_titre, causes_m).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        causes_f_titre = Text("Chez la femme", font_size=20, color=YELLOW, weight="BOLD")
        causes_f = _bullets(
            [
                "Troubles de l'ovulation : anovulation, syndrome des "
                "ovaires polykystiques (SOPK).",
                "Âge : fécondité en baisse après 35 ans (stock "
                "épuisé, risque accru de trisomie 21).",
                "Obstructions tubaires (IST non traitées), "
                "endométriose, malformations utérines.",
            ],
            font_size=16,
            width=32,
        )
        causes_f_bloc = VGroup(causes_f_titre, causes_f).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        deux_causes = VGroup(causes_m_bloc, causes_f_bloc).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        deux_causes.next_to(entete_causes, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les grandes causes d'infécondité masculine sont les "
                "troubles de la spermatogenèse, cryptorchidie, "
                "varicocèle, infections comme les oreillons après la "
                "puberté, exposition à la chaleur ou à des toxiques ; les "
                "obstacles sur les voies excrétrices ; et les troubles "
                "hormonaux. La fécondité féminine exige, elle, une "
                "ovulation régulière, des trompes perméables, un utérus "
                "apte à accueillir l'embryon et un stock folliculaire "
                "suffisant. Les causes fréquentes sont les troubles de "
                "l'ovulation, l'âge, la fécondité diminuant nettement "
                "après trente-cinq ans, les obstructions tubaires, "
                "souvent dues aux infections génitales non traitées, "
                "l'endométriose et les malformations utérines."
            )
        ) as tracker:
            self.play(FadeIn(entete_causes))
            self.play(FadeIn(causes_m_bloc), FadeIn(causes_f_bloc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_causes), FadeOut(deux_causes))

        # --- Exemple traité : analyse d'un spermogramme ---------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Spermogramme d'un patient : concentration = 8 "
                    "millions/mL (norme ≥15-20) → oligospermie. "
                    "Mobilité = 18 % (norme ≥32 %) → asthénospermie. "
                    "Formes normales = 5 % (norme ≥4 %) → normal. "
                    "Conclusion : double anomalie (nombre + mobilité), "
                    "compatible avec une fécondité réduite, à confirmer "
                    "par un second examen.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Analysons un exemple. Le spermogramme d'un patient donne "
                "une concentration de huit millions de spermatozoïdes par "
                "millilitre, en dessous de la norme de quinze à vingt "
                "millions : c'est une oligospermie. Sa mobilité est de "
                "dix-huit pour cent, en dessous de la norme de trente-deux "
                "pour cent : c'est une asthénospermie. En revanche, ses "
                "formes normales atteignent cinq pour cent, au-dessus de "
                "la norme de quatre pour cent : ce paramètre est normal. "
                "Conclusion : ce patient présente une double anomalie, sur "
                "le nombre et sur la mobilité, compatible avec une "
                "fécondité réduite, à confirmer par un second examen."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : période de fécondité et contraception --------------------
        retenir = property_box(
            _bullets(
                [
                    "Femme : fenêtre féconde du cycle ≈5-6 jours "
                    "(spermatozoïdes viables 3-5 j, ovule viable 12-24 h).",
                    "Homme : fécondité permanente de la puberté à un "
                    "âge avancé.",
                    "Contraception : pilule (bloque l'ovulation), "
                    "préservatif (empêche la rencontre + protège des "
                    "IST), stérilet, vasectomie/ligature des trompes.",
                ],
                font_size=19,
                width=50,
            ),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons la période de fécondité et son lien avec la "
                "contraception. Chez la femme, la période féconde du "
                "cycle dure environ cinq à six jours, car les "
                "spermatozoïdes survivent trois à cinq jours dans les "
                "voies génitales et l'ovule ne vit que douze à "
                "vingt-quatre heures. Chez l'homme, la fécondité est "
                "permanente, de la puberté à un âge avancé. La "
                "connaissance de ce rythme fonde les méthodes de "
                "contraception : la pilule bloque l'ovulation, le "
                "préservatif empêche la rencontre des gamètes tout en "
                "protégeant des infections sexuellement transmissibles, "
                "et le stérilet, la vasectomie ou la ligature des trompes "
                "sont des méthodes complémentaires."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter : santé publique, contexte ivoirien -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Point de santé publique : les IST non traitées "
                    "(chlamydiae, gonococcies) sont une cause évitable "
                    "majeure d'infécondité, par obstruction des trompes "
                    "chez la femme et des canaux déférents chez l'homme. "
                    "Le dépistage et le traitement précoce, ainsi que "
                    "l'usage du préservatif, protègent la fécondité "
                    "future.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un point de santé publique à ne jamais négliger : les "
                "infections sexuellement transmissibles non traitées, "
                "chlamydiae, gonococcies, sont une cause évitable majeure "
                "d'infécondité, par obstruction des trompes chez la femme "
                "et des canaux déférents chez l'homme. Le dépistage et le "
                "traitement précoce, ainsi que l'usage du préservatif, "
                "protègent la fécondité future."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
