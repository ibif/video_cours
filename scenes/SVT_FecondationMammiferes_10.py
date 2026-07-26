"""
scenes/SVT_FecondationMammiferes_10.py — Chapitre 4 (1ereC, SVT), scène 10.

Méthodes et astuces de fin de chapitre : ordre chronologique (moyen
mnémotechnique "Chacun Reçoit Facilement Bon Accord"), méthode de
détermination du sexe, méthode "vrais ou faux jumeaux", pièges à éviter,
puis L'ESSENTIEL DU CHAPITRE. Source : 1ereC/SVT.pdf, page 43.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _numbered(items, font_size=21, color="#1A1A1A", width=50):
    lines = VGroup(
        *[Text(f"{i+1}. {_wrap(it, width=width)}", font_size=font_size, color=color) for i, it in enumerate(items)]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class MethodesEtSyntheseFecondation(NotionScene):
    def construct(self):
        titre = scene_title("4.8 — Méthodes, astuces et essentiel du chapitre")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : ordre chronologique à maîtriser -------------------------------
        ordre = method_box(
            _numbered(
                [
                    "Rapport sexuel et dépôt du sperme dans le vagin.",
                    "Montée des spermatozoïdes (col → utérus → trompe) et "
                    "capacitation.",
                    "Rencontre dans le tiers externe de la trompe.",
                    "Réaction acrosomique et franchissement des "
                    "enveloppes.",
                    "Blocage de la polyspermie.",
                    "Amphimixie : fusion des noyaux, zygote diploïde.",
                ],
                font_size=19,
                width=48,
            ),
            box_width=12.6,
        )
        ordre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour clore ce chapitre, voici les méthodes et astuces à "
                "maîtriser pour vos devoirs de niveau. D'abord, l'ordre "
                "chronologique à toujours respecter pour décrire la "
                "fécondation : un, rapport sexuel et dépôt du sperme dans "
                "le vagin ; deux, montée des spermatozoïdes du col vers "
                "l'utérus puis la trompe, avec la capacitation ; trois, "
                "rencontre dans le tiers externe de la trompe ; quatre, "
                "réaction acrosomique et franchissement des enveloppes ; "
                "cinq, blocage de la polyspermie ; six, amphimixie, fusion "
                "des noyaux, zygote diploïde. Une étape oubliée ou dans le "
                "désordre coûte des points au devoir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(ordre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ordre))

        astuce = Text(
            _wrap(
                "Astuce — Moyen mnémotechnique : « Chacun Reçoit "
                "Facilement Bon Accord » : Capacitation → Réaction "
                "acrosomique → Franchissement des enveloppes → Blocage de "
                "la polyspermie → Amphimixie.",
                width=54,
            ),
            font_size=23,
            color=YELLOW,
        )
        astuce.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Pour retenir facilement ces cinq étapes centrales, "
                "utilisez ce moyen mnémotechnique : « Chacun Reçoit "
                "Facilement Bon Accord ». Chacun pour Capacitation, "
                "Reçoit pour Réaction acrosomique, Facilement pour "
                "Franchissement des enveloppes, Bon pour Blocage de la "
                "polyspermie, Accord pour Amphimixie."
            )
        ) as tracker:
            self.play(FadeIn(astuce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(astuce))

        # --- Raisonnement : méthode sexe + méthode jumeaux --------------------------
        methode_sexe = method_box(
            Text(
                _wrap(
                    "Méthode — Détermination du sexe : raisonnez en "
                    "tableau de croisement (échiquier). Lignes = ovules "
                    "(tous X), colonnes = spermatozoïdes (1/2 X, 1/2 Y). "
                    "Les cases donnent XX (fille) ou XY (garçon), "
                    "probabilité 1/2 chacune.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.4,
        )
        methode_sexe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour déterminer le sexe, raisonnez toujours en tableau "
                "de croisement, ou échiquier : en lignes, les ovules, "
                "tous porteurs d'un chromosome X ; en colonnes, les "
                "spermatozoïdes, la moitié porteurs d'un X, l'autre "
                "moitié d'un Y. Les cases donnent X X pour une fille, ou X "
                "Y pour un garçon, chacune avec une probabilité de un "
                "demi."
            )
        ) as tracker:
            self.play(FadeIn(methode_sexe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_sexe))

        methode_jumeaux = method_box(
            Text(
                _wrap(
                    "Méthode — Vrais ou faux jumeaux ? Une seule "
                    "question : combien d'ovules fécondés ? Un seul "
                    "ovule ⇒ vrais jumeaux (même sexe obligatoirement). "
                    "Deux ovules ⇒ faux jumeaux (sexe libre). Deux "
                    "jumeaux de sexes différents sont donc forcément des "
                    "faux jumeaux.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.4,
        )
        methode_jumeaux.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour distinguer vrais et faux jumeaux, posez-vous une "
                "seule question : combien d'ovules ont été fécondés ? Un "
                "seul ovule : ce sont des vrais jumeaux, obligatoirement "
                "du même sexe. Deux ovules : ce sont des faux jumeaux, de "
                "sexe libre. Deux jumeaux de sexes différents sont donc "
                "forcément des faux jumeaux."
            )
        ) as tracker:
            self.play(FadeIn(methode_jumeaux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_jumeaux))

        # --- Exemple traité : appliquer la méthode à un cas concret -----------------
        exemple_titre = Text("Exemple d'application", font_size=24, color=YELLOW, weight="BOLD")
        exemple_titre.next_to(titre, DOWN, buff=0.5)
        exemple = Text(
            _wrap(
                "Un couple a deux enfants nés le même jour, une fille et "
                "un garçon. Question : vrais ou faux jumeaux ? Réponse : "
                "des sexes différents, donc obligatoirement issus de deux "
                "ovules distincts fécondés par deux spermatozoïdes "
                "différents (l'un X, l'autre Y) : ce sont des FAUX "
                "jumeaux, même s'ils sont nés le même jour.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        exemple.next_to(exemple_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Appliquons ces méthodes à un cas concret. Un couple a "
                "deux enfants nés le même jour, une fille et un garçon. "
                "Vrais ou faux jumeaux ? Réponse : puisque leurs sexes "
                "sont différents, ils sont obligatoirement issus de deux "
                "ovules distincts, fécondés par deux spermatozoïdes "
                "différents, l'un porteur d'un X, l'autre d'un Y. Ce sont "
                "donc des faux jumeaux, même s'ils sont nés le même jour."
            )
        ) as tracker:
            self.play(FadeIn(exemple_titre))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_titre), FadeOut(exemple))

        # --- À retenir : les pièges à éviter, en synthèse ----------------------------
        pieges_titre = Text("Synthèse des pièges à éviter", font_size=24, color=YELLOW, weight="BOLD")
        pieges_titre.next_to(titre, DOWN, buff=0.45)
        pieges = warning_box(
            _bullets(
                [
                    "Fécondation (trompe) ≠ nidation (utérus).",
                    "Segmentation (mitoses du zygote) ≠ méiose (formation "
                    "des gamètes).",
                    "Capacitation (modification du spermatozoïde) ≠ "
                    "réaction acrosomique (libération d'enzymes).",
                    "Contraception (empêche la fécondation/nidation) ≠ "
                    "IVG (arrête une grossesse déjà installée).",
                    "Morula et blastocyste restent DIPLOÏDES (2n=46) : "
                    "la segmentation se fait par mitose. Seuls les "
                    "gamètes sont haploïdes.",
                ],
                font_size=18,
                color="#1A1A1A",
                width=48,
            ),
            box_width=12.6,
        )
        pieges.next_to(pieges_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Avant de conclure, une synthèse des pièges à éviter, "
                "tous déjà rencontrés dans ce chapitre. Ne confondez "
                "jamais fécondation, dans la trompe, et nidation, dans "
                "l'utérus. Ne confondez jamais segmentation, les mitoses "
                "du zygote, et méiose, la formation des gamètes. Ne "
                "confondez jamais capacitation, qui modifie le "
                "spermatozoïde, et réaction acrosomique, qui libère des "
                "enzymes. Ne confondez jamais contraception, qui empêche "
                "la fécondation ou la nidation, et IVG, qui arrête une "
                "grossesse déjà installée. Et rappelez-vous : la morula "
                "et le blastocyste restent diploïdes, à deux n, car la "
                "segmentation se fait par mitose ; seuls les gamètes sont "
                "haploïdes."
            )
        ) as tracker:
            self.play(FadeIn(pieges_titre))
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges_titre), FadeOut(pieges))

        # --- L'ESSENTIEL DU CHAPITRE (clôture) ---------------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Fécondation = union spermatozoïde + ovule → zygote "
                    "(2n), dans le TIERS EXTERNE de la trompe.",
                    "Trajet : montée des spermatozoïdes (col→utérus→"
                    "trompe, survie 24-72h) ; ovule capturé par le "
                    "pavillon (fécondabilité 12-24h).",
                    "5 étapes : capacitation → réaction acrosomique → "
                    "franchissement des enveloppes → blocage de la "
                    "polyspermie → amphimixie (n+n=2n).",
                    "La fécondation restaure la diploïdie et détermine le "
                    "sexe : le PÈRE fournit l'X ou l'Y déterminant.",
                    "Segmentation (mitoses, 2n conservé) : zygote → œuf "
                    "segmenté → morula → blastocyste, puis nidation "
                    "(J6-7) dans l'endomètre.",
                    "Vrais jumeaux (1 ovule, même sexe) ≠ faux jumeaux (2 "
                    "ovules, sexe libre).",
                    "Contraception, IVG, FIVETE : trois réalités "
                    "distinctes de la maîtrise scientifique de la "
                    "procréation, à ne jamais confondre.",
                ],
                font_size=17,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. La fécondation est "
                "l'union d'un spermatozoïde et d'un ovule, formant un "
                "zygote diploïde, dans le tiers externe de la trompe de "
                "Fallope, jamais dans l'utérus. Elle suppose la montée "
                "des spermatozoïdes, du col vers l'utérus puis la trompe, "
                "et la capture de l'ovule par le pavillon. Cinq étapes "
                "s'enchaînent : capacitation, réaction acrosomique, "
                "franchissement des enveloppes, blocage de la "
                "polyspermie, et amphimixie, où n plus n égale deux n. La "
                "fécondation restaure ainsi la diploïdie et détermine le "
                "sexe de l'embryon, le père fournissant le chromosome "
                "déterminant, X ou Y. Le zygote se divise ensuite par "
                "mitoses, en conservant deux n, jusqu'au blastocyste, qui "
                "se nide dans l'endomètre vers le sixième ou septième "
                "jour. Un seul ovule fécondé donne de vrais jumeaux, "
                "toujours de même sexe ; deux ovules fécondés donnent de "
                "faux jumeaux, de sexe libre. Enfin, contraception, IVG "
                "et FIVETE sont trois réalités bien distinctes de la "
                "maîtrise scientifique de la procréation, à connaître "
                "pour un comportement responsable."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
