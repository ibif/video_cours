"""
scenes/SVT_SyntheseProteines_06.py — Chapitre 5 (1ereD, SVT), scène 06.

§ 5.4 La traduction : les 4 acteurs (ARNm, ribosome, ARNt, acides
aminés), définition ARNt/anticodon, les trois étapes (initiation,
élongation, terminaison), remarque sur les polyribosomes, exemple complet
ADN -> ARNm -> protéine, méthode en 4 étapes, attention à ne pas confondre
codon et anticodon. Source : 1ereD/SVT.pdf, pages 70-73.
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
    Ellipse,
    FadeIn,
    FadeOut,
    Text,
    Triangle,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box

BASE_COLORS = {"A": GREEN, "U": RED, "G": BLUE, "C": ORANGE, "T": MAROON}


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _base_seq(seq: str, font_size: int = 28) -> VGroup:
    lettres = VGroup(
        *[Text(base, font_size=font_size, color=BASE_COLORS.get(base, WHITE), weight="BOLD") for base in seq]
    )
    lettres.arrange(RIGHT, buff=0.1)
    return lettres


def _codon(codon: str, font_size: int = 28) -> VGroup:
    lettres = VGroup(
        *[Text(base, font_size=font_size, color=BASE_COLORS.get(base, WHITE), weight="BOLD") for base in codon]
    )
    lettres.arrange(RIGHT, buff=0.04)
    return lettres


def _arnt(anticodon: str, acide_amine: str) -> VGroup:
    """Schéma simplifié d'un ARNt : triangle + anticodon en bas, acide
    aminé attaché en haut."""
    corps = Triangle(color=WHITE, fill_color="#444444", fill_opacity=1).scale(0.35)
    corps.rotate(180 * 3.14159 / 180)
    anticodon_txt = _codon(anticodon, font_size=18)
    anticodon_txt.next_to(corps, DOWN, buff=0.08)
    aa_dot = Circle(radius=0.18, color=YELLOW, fill_color=YELLOW, fill_opacity=1)
    aa_dot.next_to(corps, UP, buff=0.05)
    aa_txt = Text(acide_amine, font_size=14, color="#1A1A1A", weight="BOLD")
    aa_txt.move_to(aa_dot.get_center())
    return VGroup(corps, anticodon_txt, aa_dot, aa_txt)


class LaTraduction(NotionScene):
    def construct(self):
        titre = scene_title("5.4 — La traduction")
        titre.scale(0.8)
        titre.to_edge(UP)

        # --- Énoncé : les 4 acteurs de la traduction -------------------------
        entete_acteurs = Text("Les 4 acteurs de la traduction", font_size=27, color=YELLOW, weight="BOLD")
        entete_acteurs.next_to(titre, DOWN, buff=0.5)

        acteurs = _bullets(
            [
                "L'ARNm : apporte le message à traduire, codon par codon.",
                "Le ribosome : « machine » de fabrication, lit l'ARNm et "
                "assemble les acides aminés.",
                "Les ARNt (ARN de transfert) : « traducteurs », chacun "
                "transporte un acide aminé précis et possède un "
                "anticodon.",
                "Les acides aminés : matière première de la protéine "
                "(énergie fournie par l'ATP).",
            ],
            font_size=21,
            width=52,
        )
        acteurs.next_to(entete_acteurs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La traduction a lieu dans le cytoplasme, sur des petits "
                "organites appelés ribosomes. Quatre acteurs sont "
                "indispensables. L'ARNm, qui apporte le message à "
                "traduire, codon par codon. Le ribosome, formé d'une "
                "grande et d'une petite sous-unité, qui est la machine de "
                "fabrication : il lit l'ARNm et assemble les acides "
                "aminés. Les ARNt, ou ARN de transfert, qui sont les "
                "traducteurs : chaque ARNt transporte un acide aminé "
                "précis et possède un anticodon complémentaire d'un codon "
                "de l'ARNm. Et les acides aminés, matière première de la "
                "protéine, présents dans le cytoplasme, l'énergie "
                "nécessaire étant fournie par l'ATP."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_acteurs))
            self.play(FadeIn(acteurs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_acteurs), FadeOut(acteurs))

        def_arnt = definition_box(
            Text(
                _wrap(
                    "Un ARNt (ARN de transfert) est une petite molécule "
                    "d'ARN repliée avec deux sites : un anticodon, triplet "
                    "complémentaire d'un codon de l'ARNm, et un point "
                    "d'attachement pour l'acide aminé correspondant. Une "
                    "enzyme spécifique charge chaque ARNt avec le bon "
                    "acide aminé.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_arnt.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un ARNt, ou ARN de transfert, est une petite molécule "
                "d'ARN repliée qui possède deux sites : d'un côté, un "
                "anticodon, triplet de trois bases complémentaire d'un "
                "codon de l'ARNm ; de l'autre, un point d'attachement pour "
                "l'acide aminé correspondant. Une enzyme spécifique charge "
                "chaque ARNt avec le bon acide aminé : c'est ce qui "
                "garantit que le codon et l'acide aminé se correspondent "
                "toujours correctement."
            )
        ) as tracker:
            self.play(FadeIn(def_arnt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_arnt))

        # --- Raisonnement : les 3 étapes (schéma ribosome) --------------------
        ribosome = Ellipse(width=3.2, height=1.6, color=WHITE, fill_color="#555555", fill_opacity=1)
        ribosome.next_to(titre, DOWN, buff=1.2)

        arnm_ligne = VGroup(_codon("AUG"), _codon("UUU"), _codon("GGC"), _codon("UAA")).arrange(RIGHT, buff=0.35)
        arnm_ligne.next_to(ribosome, DOWN, buff=0.9)
        label_arnm_schema = Text("ARNm", font_size=16, color=WHITE).next_to(arnm_ligne, LEFT, buff=0.3)

        with self.voiceover(
            text=(
                "La traduction se déroule en trois étapes. Initiation : le "
                "ribosome se fixe sur l'ARNm au niveau du codon "
                "d'initiation A U G. Un premier ARNt, portant la "
                "méthionine et l'anticodon U A C, vient se placer en face "
                "de ce codon."
            )
        ) as tracker:
            self.play(FadeIn(ribosome), FadeIn(arnm_ligne), FadeIn(label_arnm_schema))
            arnt1 = _arnt("UAC", "Met")
            arnt1.next_to(arnm_ligne[0], UP, buff=0.15)
            self.play(FadeIn(arnt1))
            self.wait(tracker.get_remaining_duration())

        chaine_aa = VGroup()
        with self.voiceover(
            text=(
                "Élongation : un deuxième ARNt, dont l'anticodon est "
                "complémentaire du codon suivant, entre dans le ribosome "
                "avec son acide aminé. Une liaison peptidique se forme "
                "entre les deux acides aminés. Le premier ARNt, désormais "
                "vide, sort, le ribosome avance d'un codon, et le cycle "
                "recommence : la chaîne polypeptidique s'allonge, acide "
                "aminé après acide aminé."
            )
        ) as tracker:
            arnt2 = _arnt("AAA", "Phe")
            arnt2.next_to(arnm_ligne[1], UP, buff=0.15)
            self.play(FadeIn(arnt2))
            self.play(FadeOut(arnt1))
            arnt3 = _arnt("CCG", "Gly")
            arnt3.next_to(arnm_ligne[2], UP, buff=0.15)
            self.play(FadeIn(arnt3))
            self.play(FadeOut(arnt2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Terminaison : lorsque le ribosome atteint un codon STOP, "
                "aucun ARNt ne peut s'y fixer. La chaîne polypeptidique "
                "est libérée, le ribosome se sépare de l'ARNm. La chaîne "
                "se replie ensuite dans l'espace pour devenir une protéine "
                "fonctionnelle."
            )
        ) as tracker:
            self.play(FadeOut(arnt3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ribosome), FadeOut(arnm_ligne), FadeOut(label_arnm_schema))

        remarque_poly = warning_box(
            Text(
                _wrap(
                    "Les polyribosomes : sur un même ARNm, plusieurs "
                    "ribosomes peuvent travailler en même temps, à la "
                    "queue leu leu. Chacun fabrique un exemplaire de la "
                    "protéine, ce qui permet une production rapide en "
                    "grande quantité (ex : hémoglobine dans les jeunes "
                    "globules rouges).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        remarque_poly.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une remarque importante : sur un même ARNm, plusieurs "
                "ribosomes peuvent travailler en même temps, à la queue "
                "leu leu, on parle de polyribosome. Chacun fabrique un "
                "exemplaire de la protéine, ce qui permet à la cellule de "
                "produire rapidement de grandes quantités d'une même "
                "protéine, par exemple de l'hémoglobine dans les jeunes "
                "globules rouges."
            )
        ) as tracker:
            self.play(FadeIn(remarque_poly))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_poly))

        # --- Exemple traité : ADN -> ARNm -> protéine, exemple complet -------
        entete_ex = Text("Exemple complet : ADN -> ARNm -> protéine", font_size=23, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        brin = VGroup(Text("3'-", font_size=26, color=WHITE), _base_seq("TACAAACCGATT", font_size=26), Text("-5'", font_size=26, color=WHITE)).arrange(RIGHT, buff=0.12)
        brin.next_to(entete_ex, DOWN, buff=0.45)
        label_brin = Text("brin transcrit", font_size=16, color=WHITE).next_to(brin, LEFT, buff=0.3)

        with self.voiceover(
            text=(
                "Reprenons l'exemple complet. Le brin transcrit d'un petit "
                "gène est trois prime, T A C A A A C C G A T T, cinq "
                "prime. Déterminons la protéine fabriquée."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(brin), FadeIn(label_brin))
            self.wait(tracker.get_remaining_duration())

        arnm = VGroup(Text("5'-", font_size=26, color=WHITE), _base_seq("AUGUUUGGCUAA", font_size=26), Text("-3'", font_size=26, color=WHITE)).arrange(RIGHT, buff=0.12)
        arnm.next_to(brin, DOWN, buff=0.5)
        label_arnm = Text("ARNm (transcription)", font_size=16, color=WHITE).next_to(arnm, LEFT, buff=0.3)

        with self.voiceover(
            text=(
                "Étape 1, la transcription : on écrit l'ARNm complémentaire "
                "du brin transcrit. On obtient l'ARNm cinq prime, A U G U "
                "U U G G C U A A, trois prime."
            )
        ) as tracker:
            self.play(Write(arnm), FadeIn(label_arnm))
            self.wait(tracker.get_remaining_duration())

        traduction = Text("Met - Phe - Gly (STOP)", font_size=26, color=YELLOW, weight="BOLD")
        traduction.next_to(arnm, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étape 2, la traduction : on découpe en codons, A U G, U U "
                "U, G G C, U A A. A U G code méthionine, U U U code "
                "phénylalanine, G G C code glycine, U A A est un codon "
                "STOP. Conclusion : la protéine fabriquée comporte trois "
                "acides aminés, méthionine, phénylalanine, glycine."
            )
        ) as tracker:
            self.play(FadeIn(traduction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(brin), FadeOut(label_brin), FadeOut(arnm), FadeOut(label_arnm), FadeOut(traduction))

        # --- À retenir : méthode en 4 étapes -----------------------------------
        methode = method_box(
            _bullets(
                [
                    "Étape 1 : identifier le brin transcrit dans l'énoncé.",
                    "Étape 2 : écrire l'ARNm (A-U, T-A, G-C, C-G ; aucun T "
                    "dans le résultat).",
                    "Étape 3 : découper l'ARNm en codons à partir de AUG.",
                    "Étape 4 : traduire chaque codon et conclure par la "
                    "liste ordonnée des acides aminés (le codon STOP "
                    "termine la chaîne sans ajouter d'acide aminé).",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Pour résoudre un exercice complet d'ADN vers protéine, "
                "procédez en quatre étapes. Un : identifier le brin "
                "transcrit dans l'énoncé. Deux : écrire l'ARNm, avec les "
                "complémentarités A-U, T-A, G-C, C-G, sans aucun T dans le "
                "résultat. Trois : découper l'ARNm en codons à partir de A "
                "U G. Quatre : traduire chaque codon et conclure par la "
                "liste ordonnée des acides aminés, sans oublier de "
                "préciser que le codon STOP termine la chaîne sans ajouter "
                "d'acide aminé."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : codon vs anticodon ------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Codon et anticodon : ne pas confondre. Le codon se "
                    "trouve sur l'ARNm ; l'anticodon se trouve sur "
                    "l'ARNt. Ils sont complémentaires. Exemple : au codon "
                    "5'-GGC-3' correspond l'anticodon 3'-CCG-5'. Le "
                    "tableau du code génétique ne s'utilise qu'avec les "
                    "codons de l'ARNm.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre codon et anticodon. Le codon "
                "se trouve sur l'ARNm ; l'anticodon se trouve sur l'ARNt. "
                "Ils sont complémentaires l'un de l'autre. Par exemple, au "
                "codon cinq prime G G C trois prime correspond l'anticodon "
                "trois prime C C G cinq prime. Une erreur classique "
                "consiste à chercher l'anticodon dans le tableau du code "
                "génétique : le tableau ne s'utilise qu'avec les codons de "
                "l'ARNm."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
