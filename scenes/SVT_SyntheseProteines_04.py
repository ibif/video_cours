"""
scenes/SVT_SyntheseProteines_04.py — Chapitre 5 (1ereD, SVT), scène 04.

§ 5.2.3 Utiliser le tableau du code génétique : méthode en 4 étapes,
exemple traité (traduire 5'-AUG AAG UUU UAA-3'), attention au piège du
cadre de lecture. Source : 1ereD/SVT.pdf, page 67.
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
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, warning_box

BASE_COLORS = {"A": GREEN, "U": RED, "G": BLUE, "C": ORANGE, "T": MAROON}


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _codon(codon: str, font_size: int = 34) -> VGroup:
    lettres = VGroup(
        *[Text(base, font_size=font_size, color=BASE_COLORS.get(base, WHITE), weight="BOLD") for base in codon]
    )
    lettres.arrange(RIGHT, buff=0.04)
    return lettres


class TraduireAvecLeTableau(NotionScene):
    def construct(self):
        titre = scene_title("5.2.3 — Traduire un ARNm avec le tableau")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------
        intro = Text(
            _wrap(
                "Une fois le tableau du code génétique disponible, comment "
                "l'utiliser pour trouver la protéine correspondant à un "
                "ARNm donné ?",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Maintenant que nous connaissons le tableau du code "
                "génétique, comment l'utiliser concrètement pour trouver la "
                "protéine correspondant à un ARN messager donné ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- À retenir : méthode en 4 étapes -------------------------------
        methode = method_box(
            _bullets(
                [
                    "Étape 1 : repérer le codon d'initiation AUG et "
                    "découper la suite en codons (groupes de 3 lettres) à "
                    "partir de lui.",
                    "Étape 2 : pour chaque codon, lire dans le tableau "
                    "l'acide aminé correspondant.",
                    "Étape 3 : enchaîner les acides aminés dans l'ordre "
                    "des codons.",
                    "Étape 4 : s'arrêter au premier codon STOP (UAA, UAG "
                    "ou UGA) : il n'ajoute aucun acide aminé, il termine "
                    "la chaîne.",
                ],
                font_size=21,
                width=52,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la méthode, en quatre étapes. Étape un : repérer le "
                "codon d'initiation A U G et découper la suite en codons, "
                "des groupes de trois lettres, à partir de lui. Étape deux "
                ": pour chaque codon, lire dans le tableau l'acide aminé "
                "correspondant. Étape trois : enchaîner les acides aminés "
                "dans l'ordre des codons. Étape quatre : s'arrêter au "
                "premier codon STOP, U A A, U A G ou U G A : il n'ajoute "
                "aucun acide aminé, il termine la chaîne."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : traduire l'ARNm --------------------------
        entete_ex = Text("Exemple : traduire l'ARNm", font_size=27, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        message = VGroup(
            Text("5'-", font_size=32, color=WHITE),
            _codon("AUG"), _codon("AAG"), _codon("UUU"), _codon("UAA"),
            Text("-3'", font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.25)
        message.next_to(entete_ex, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Traduisons l'ARN messager suivant : cinq prime, A U G, "
                "A A G, U U U, U A A, trois prime."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(message))
            self.wait(tracker.get_remaining_duration())

        codons = message[1:5]
        traduction_lignes = VGroup(
            Text("Met", font_size=28, color=WHITE, weight="BOLD"),
            Text("Lys", font_size=28, color=WHITE, weight="BOLD"),
            Text("Phe", font_size=28, color=WHITE, weight="BOLD"),
            Text("STOP", font_size=28, color=YELLOW, weight="BOLD"),
        )
        for aa, codon in zip(traduction_lignes, codons):
            aa.next_to(codon, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On découpe en codons : A U G, A A G, U U U, U A A. A U G "
                "donne méthionine, Met. A A G donne lysine, Lys. U U U "
                "donne phénylalanine, Phe. U A A est un codon STOP : on "
                "arrête."
            )
        ) as tracker:
            for aa in traduction_lignes:
                self.play(FadeIn(aa))
            self.wait(tracker.get_remaining_duration())

        conclusion = Text(
            "Protéine obtenue : Met - Lys - Phe (3 acides aminés)",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        conclusion.next_to(traduction_lignes, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La protéine fabriquée comporte donc trois acides aminés : "
                "méthionine, lysine, phénylalanine."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_ex), FadeOut(message), FadeOut(traduction_lignes), FadeOut(conclusion)
        )

        # --- Exemple traité : example_box récapitulatif ---------------------
        exemple = example_box(
            Text(
                _wrap(
                    "5'-AUG AAG UUU UAA-3'. AUG -> Met ; AAG -> Lys ; "
                    "UUU -> Phe ; UAA -> STOP (arrêt). Protéine : Met, "
                    "Lys, Phe (3 acides aminés).",
                    width=52,
                ),
                font_size=23,
            ),
            box_width=11.5,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Récapitulons cet exemple : à partir de l'ARN messager A U "
                "G, A A G, U U U, U A A, on obtient une protéine de trois "
                "acides aminés, méthionine, lysine, phénylalanine, le "
                "codon STOP marquant la fin sans ajouter d'acide aminé."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Piège à éviter : le cadre de lecture ---------------------------
        piege_titre = Text("Piège : le cadre de lecture", font_size=27, color=YELLOW, weight="BOLD")
        piege_titre.next_to(titre, DOWN, buff=0.5)

        bon_cadre = VGroup(
            Text("Bon cadre :", font_size=20, color=WHITE),
            _codon("AUG", font_size=26), _codon("UUU", font_size=26), Text("G", font_size=26, color=BASE_COLORS["G"], weight="BOLD"),
        ).arrange(RIGHT, buff=0.2)
        bon_lecture = Text("→ Met, Phe...", font_size=20, color=WHITE)
        bon_lecture.next_to(bon_cadre, RIGHT, buff=0.3)
        ligne_bonne = VGroup(bon_cadre, bon_lecture)

        mauvais_cadre = VGroup(
            Text("Décalé d'1 lettre :", font_size=20, color=WHITE),
            Text("A", font_size=26, color=BASE_COLORS["A"], weight="BOLD"),
            _codon("UGU", font_size=26), Text("U", font_size=26, color=BASE_COLORS["U"], weight="BOLD"),
        ).arrange(RIGHT, buff=0.2)
        mauvais_lecture = Text("→ Cys... (faux !)", font_size=20, color=RED)
        mauvais_lecture.next_to(mauvais_cadre, RIGHT, buff=0.3)
        ligne_mauvaise = VGroup(mauvais_cadre, mauvais_lecture)

        comparaison = VGroup(ligne_bonne, ligne_mauvaise).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        comparaison.next_to(piege_titre, DOWN, buff=0.4)

        piege_texte = warning_box(
            Text(
                _wrap(
                    "Le ribosome commence toujours au codon AUG : c'est "
                    "lui qui fixe le cadre de lecture. Si l'on décale la "
                    "lecture d'une seule lettre, tout change. Dans les "
                    "exercices, découpez toujours à partir du AUG "
                    "indiqué.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        piege_texte.next_to(comparaison, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : le découpage en codons "
                "doit commencer au bon endroit. Par exemple, la suite A U "
                "G U U U G se lit A U G puis U U U, soit méthionine puis "
                "phénylalanine ; mais en décalant la lecture d'une seule "
                "lettre, on lirait U G U, soit cystéine, ce qui est faux. "
                "En réalité, le ribosome commence toujours au codon A U G "
                ": c'est lui qui fixe le cadre de lecture. Dans les "
                "exercices, découpez toujours à partir du A U G indiqué."
            )
        ) as tracker:
            self.play(FadeIn(piege_titre))
            self.play(FadeIn(comparaison))
            self.play(FadeIn(piege_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege_titre), FadeOut(comparaison), FadeOut(piege_texte))
