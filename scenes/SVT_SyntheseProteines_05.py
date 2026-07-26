"""
scenes/SVT_SyntheseProteines_05.py — Chapitre 5 (1ereD, SVT), scène 05.

§ 5.3 La transcription : définition et localisation, brin transcrit /
brin non transcrit, règles de complémentarité ADN -> ARN, les trois
étapes (ouverture, élongation, terminaison), exemple d'écriture de
l'ARNm à partir d'un brin transcrit, méthode en 4 étapes, attention aux
deux erreurs fréquentes. Source : 1ereD/SVT.pdf, pages 68-70.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    MAROON,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, property_box, scene_title, warning_box

BASE_COLORS = {"A": GREEN, "U": RED, "G": BLUE, "C": ORANGE, "T": MAROON}


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _base_seq(seq: str, font_size: int = 30) -> VGroup:
    """Une séquence de bases = un VGroup de Text séparés (1 par base), pour
    pouvoir mettre en évidence ou colorer chaque base sans indexer un long
    Text (voir CLAUDE.md, correctif 4)."""
    lettres = VGroup(
        *[Text(base, font_size=font_size, color=BASE_COLORS.get(base, WHITE), weight="BOLD") for base in seq]
    )
    lettres.arrange(RIGHT, buff=0.12)
    return lettres


class LaTranscription(NotionScene):
    def construct(self):
        titre = scene_title("5.3 — La transcription")
        titre.scale(0.75)
        titre.to_edge(UP)

        # --- Énoncé : définition et vocabulaire -----------------------------
        def_transcription = definition_box(
            Text(
                _wrap(
                    "La transcription est la synthèse d'une molécule "
                    "d'ARN messager (ARNm) à partir d'un gène : la recopie "
                    "de l'information du gène en langage ARN. Chez les "
                    "cellules à noyau, elle a lieu dans le noyau. L'ARNm "
                    "sort ensuite dans le cytoplasme, où il sera traduit.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_transcription.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La transcription est la synthèse d'une molécule d'ARN "
                "messager à partir d'un gène, c'est-à-dire la recopie de "
                "l'information du gène en langage ARN. Chez les cellules à "
                "noyau, les eucaryotes, elle a lieu dans le noyau. L'ARNm "
                "fabriqué sort ensuite dans le cytoplasme, où il sera "
                "traduit."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_transcription))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_transcription))

        vocab_brins = Text(
            _wrap(
                "Un gène est formé de deux brins d'ADN complémentaires. "
                "Le brin transcrit (ou matrice) sert de modèle, lu de 3' "
                "vers 5'. L'ARNm est complémentaire du brin transcrit : "
                "il a donc la même séquence que le brin non transcrit, "
                "sauf que U remplace T.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        vocab_brins.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un gène est formé de deux brins d'ADN complémentaires. "
                "Pendant la transcription, un seul brin sert de modèle : "
                "c'est le brin transcrit, ou brin matrice, qui est lu dans "
                "le sens trois prime vers cinq prime. L'autre brin est le "
                "brin non transcrit. L'ARNm fabriqué est complémentaire du "
                "brin transcrit ; il a donc la même séquence que le brin "
                "non transcrit, à ceci près que U remplace T."
            )
        ) as tracker:
            self.play(FadeIn(vocab_brins))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vocab_brins))

        # --- Raisonnement : règles + les 3 étapes (schéma) ------------------
        regles = property_box(
            Text(
                _wrap(
                    "Règles de complémentarité ADN -> ARN : A(ADN) avec "
                    "U(ARN) ; T(ADN) avec A(ARN) ; G(ADN) avec C(ARN) ; "
                    "C(ADN) avec G(ARN). L'enzyme qui réalise cet "
                    "assemblage est l'ARN polymérase ; l'ARNm est "
                    "synthétisé dans le sens 5' vers 3'.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        regles.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pendant la transcription, chaque base du brin transcrit "
                "reçoit la base complémentaire en version ARN : A de l'ADN "
                "s'apparie avec U de l'ARN ; T de l'ADN s'apparie avec A de "
                "l'ARN ; G de l'ADN s'apparie avec C de l'ARN ; C de l'ADN "
                "s'apparie avec G de l'ARN. L'enzyme qui réalise cet "
                "assemblage est l'ARN polymérase ; l'ARNm est synthétisé "
                "dans le sens cinq prime vers trois prime."
            )
        ) as tracker:
            self.play(FadeIn(regles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regles))

        # Schéma simplifié : deux brins d'ADN qui s'écartent, ARN polymérase
        # (cercle) qui avance, ARNm qui s'allonge derrière elle.
        brin_haut = Line(LEFT * 4.5, RIGHT * 4.5, color=BLUE, stroke_width=6)
        brin_bas = Line(LEFT * 4.5, RIGHT * 4.5, color=MAROON, stroke_width=6)
        brins = VGroup(brin_haut, brin_bas).arrange(DOWN, buff=0.5)
        brins.next_to(titre, DOWN, buff=0.8)

        label_transcrit = Text("brin transcrit", font_size=16, color=MAROON)
        label_transcrit.next_to(brin_bas, DOWN, buff=0.15).align_to(brin_bas, LEFT)
        label_non_transcrit = Text("brin non transcrit", font_size=16, color=BLUE)
        label_non_transcrit.next_to(brin_haut, UP, buff=0.15).align_to(brin_haut, LEFT)

        polymerase = Circle(radius=0.35, color=YELLOW, fill_color=YELLOW, fill_opacity=0.8)
        polymerase.move_to(brins.get_left() + RIGHT * 0.5)
        label_poly = Text("ARN polymérase", font_size=16, color=YELLOW)
        label_poly.next_to(polymerase, UP, buff=0.5)

        arnm = Line(brins.get_left() + RIGHT * 0.5, brins.get_left() + RIGHT * 0.5, color=GREEN, stroke_width=6)
        arnm.shift(DOWN * 0.25)

        schema = VGroup(brins, label_transcrit, label_non_transcrit, polymerase, label_poly, arnm)

        with self.voiceover(
            text=(
                "La transcription se déroule en trois temps. Ouverture : "
                "l'ARN polymérase se fixe sur le gène et écarte localement "
                "les deux brins d'ADN, créant une petite bulle de "
                "transcription."
            )
        ) as tracker:
            self.play(FadeIn(brins), FadeIn(label_transcrit), FadeIn(label_non_transcrit))
            self.play(FadeIn(polymerase), FadeIn(label_poly))
            self.wait(tracker.get_remaining_duration())

        arnm_final = Line(
            brins.get_left() + RIGHT * 0.5, brins.get_right() + LEFT * 0.5, color=GREEN, stroke_width=6
        )
        arnm_final.shift(DOWN * 1.2)
        label_arnm = Text("ARNm en cours de synthèse", font_size=16, color=GREEN)
        label_arnm.next_to(arnm_final, DOWN, buff=0.15)

        with self.voiceover(
            text=(
                "Élongation : l'enzyme avance le long du brin transcrit et "
                "assemble les ribonucléotides complémentaires les uns après "
                "les autres ; l'ARNm s'allonge derrière elle."
            )
        ) as tracker:
            self.play(
                polymerase.animate.move_to(brins.get_right() + LEFT * 0.5),
                label_poly.animate.next_to(brins.get_right() + LEFT * 0.5, UP, buff=0.5),
                FadeIn(arnm_final),
                FadeIn(label_arnm),
                run_time=2.5,
            )
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Terminaison : arrivée à la fin du gène, l'enzyme se "
                "détache, l'ARNm est libéré et les deux brins d'ADN se "
                "réassocient. Chez les eucaryotes, l'ARNm subit encore une "
                "petite maturation avant de sortir du noyau."
            )
        ) as tracker:
            self.play(FadeOut(polymerase), FadeOut(label_poly))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(arnm_final), FadeOut(label_arnm))

        # --- Exemple traité : écrire l'ARNm à partir du brin transcrit ------
        entete_ex = Text("Exemple : brin transcrit -> ARNm", font_size=25, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        brin_transcrit_seq = "TACGCTAATTCG"
        arnm_seq = "AUGCGAUUAAGC"

        ligne_adn = VGroup(
            Text("3'-", font_size=28, color=WHITE), _base_seq(brin_transcrit_seq, font_size=28), Text("-5'", font_size=28, color=WHITE)
        ).arrange(RIGHT, buff=0.15)
        ligne_adn.next_to(entete_ex, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le brin transcrit d'un gène comporte la séquence trois "
                "prime, T A C G C T A A T T C G, cinq prime. Écrivons "
                "l'ARNm produit."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(ligne_adn))
            self.wait(tracker.get_remaining_duration())

        ligne_arn = VGroup(
            Text("5'-", font_size=28, color=WHITE), _base_seq(arnm_seq, font_size=28), Text("-3'", font_size=28, color=WHITE)
        ).arrange(RIGHT, buff=0.15)
        ligne_arn.next_to(ligne_adn, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On remplace chaque base par sa complémentaire en version "
                "ARN, en respectant l'ordre : T donne A, A donne U, C donne "
                "G, G donne C, C donne G, T donne A, A donne U, A donne U, "
                "T donne A, T donne A, C donne G, G donne C. L'ARNm obtenu "
                "est cinq prime, A U G C G A U U A A G C, trois prime. On "
                "remarque qu'il commence par A U G : le signal de départ de "
                "la traduction sera présent."
            )
        ) as tracker:
            self.play(Write(ligne_arn))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(ligne_adn), FadeOut(ligne_arn))

        exemple_box_recap = example_box(
            Text(
                _wrap(
                    "Brin transcrit : 3'-TACGCTAATTCG-5'. ARNm produit : "
                    "5'-AUGCGAUUAAGC-3'. Il commence par AUG : le signal "
                    "de départ de la traduction est présent.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        exemple_box_recap.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Récapitulons : à partir du brin transcrit, on obtient "
                "l'ARNm cinq prime A U G C G A U U A A G C trois prime, qui "
                "commence bien par le codon A U G."
            )
        ) as tracker:
            self.play(FadeIn(exemple_box_recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_box_recap))

        # --- À retenir : méthode en 4 étapes ---------------------------------
        methode = method_box(
            _bullets(
                [
                    "Étape 1 : vérifier que l'énoncé donne bien le brin "
                    "transcrit (sinon, écrire d'abord son complémentaire).",
                    "Étape 2 : recopier la séquence dans l'ordre, en "
                    "remplaçant chaque base : A avec U, T avec A, G avec "
                    "C, C avec G.",
                    "Étape 3 : vérifier qu'il n'y a aucun T dans le "
                    "résultat (l'ARN n'en contient jamais).",
                    "Étape 4 : regrouper par paquets de trois lettres "
                    "pour préparer la traduction.",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Pour passer du brin transcrit à l'ARNm sans erreur, "
                "procédez en quatre étapes. Un : vérifiez que l'énoncé "
                "donne bien le brin transcrit, sinon écrivez d'abord son "
                "complémentaire. Deux : recopiez la séquence dans l'ordre, "
                "en remplaçant chaque base par sa complémentaire, A avec U, "
                "T avec A, G avec C, C avec G. Trois : vérifiez qu'il n'y a "
                "aucun T dans le résultat, car dans un ARN, la base T "
                "n'existe pas. Quatre : regroupez par paquets de trois "
                "lettres pour préparer la traduction."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : les deux erreurs fréquentes --------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Deux erreurs fréquentes : 1) garder des T dans "
                    "l'ARNm, alors que l'ARN contient toujours U à la "
                    "place de T ; 2) transcrire le mauvais brin, ce qui "
                    "donne un message et donc une protéine complètement "
                    "faux. Lisez toujours l'énoncé avec soin pour savoir "
                    "quel brin est le brin transcrit.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux erreurs sont particulièrement fréquentes. Garder des "
                "T dans l'ARNm : c'est faux, l'ARN contient toujours U à la "
                "place de T. Transcrire le mauvais brin : si l'on utilise "
                "le brin non transcrit comme modèle, on obtient un message "
                "complètement différent, et donc une protéine fausse. "
                "Lisez toujours l'énoncé avec soin pour savoir quel brin "
                "est le brin transcrit."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
