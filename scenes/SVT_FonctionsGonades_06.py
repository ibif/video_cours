"""
scenes/SVT_FonctionsGonades_06.py — Chapitre 1 (1ereD, SVT), scène 06.

§ 1.3.4 Comparaison des deux gamétogenèses : tableau comparatif, exemple
du calcul de rendement (3200 vs 800), méthode de dénombrement, pièges de
la gamétogenèse, remarque sur la cryptorchidie.
Source : 1ereD/SVT.pdf, pages 12-13.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

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


class ComparaisonDesDeuxGametogeneses(NotionScene):
    def construct(self):
        titre = scene_title("1.3.4 — Comparaison des deux gamétogenèses")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : introduction ------------------------------------------
        intro = Text(
            _wrap(
                "La spermatogenèse et l'ovogenèse produisent toutes deux "
                "des gamètes par méiose, mais leur déroulement diffère "
                "profondément. Comparons-les critère par critère.",
                width=54,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La spermatogenèse et l'ovogenèse produisent toutes deux des "
                "gamètes par méiose, mais leur déroulement diffère "
                "profondément. Comparons-les critère par critère."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : tableau comparatif -------------------------------
        criteres = ["Lieu", "Début", "Fin", "Rythme", "Gamètes / cellule mère", "Production totale", "Méiose"]
        spermato = [
            "Tubes séminifères",
            "Puberté",
            "Âge avancé",
            "Continu",
            "4 spermatozoïdes",
            "~100 millions / jour",
            "Sans interruption",
        ]
        ovo = [
            "Follicules ovariens",
            "Avant la naissance",
            "Ménopause (~50 ans)",
            "Cyclique (~28 jours)",
            "1 ovule + polaires",
            "~450-500 dans une vie",
            "Bloquée 2 fois",
        ]

        col_crit = VGroup(Text("Critère", font_size=20, color=YELLOW, weight="BOLD"))
        col_sperm = VGroup(Text("Spermatogenèse", font_size=20, color=YELLOW, weight="BOLD"))
        col_ovo = VGroup(Text("Ovogenèse", font_size=20, color=YELLOW, weight="BOLD"))

        for c, s, o in zip(criteres, spermato, ovo):
            col_crit.add(Text(c, font_size=18, color=WHITE))
            col_sperm.add(Text(s, font_size=18, color=WHITE))
            col_ovo.add(Text(o, font_size=18, color=WHITE))

        col_crit.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        col_sperm.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        col_ovo.arrange(DOWN, aligned_edge=LEFT, buff=0.28)

        tableau = VGroup(col_crit, col_sperm, col_ovo).arrange(RIGHT, buff=0.7, aligned_edge=UP)
        tableau.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La spermatogenèse se déroule dans les tubes séminifères, "
                "débute à la puberté et se poursuit jusqu'à un âge avancé, de "
                "façon continue, avec quatre spermatozoïdes produits par "
                "cellule mère et environ cent millions par jour, sans "
                "interruption de la méiose. L'ovogenèse, elle, se déroule "
                "dans les follicules ovariens ; son stock est constitué avant "
                "la naissance, et elle s'arrête à la ménopause, vers "
                "cinquante ans ; elle est cyclique, sur un rythme d'environ "
                "vingt-huit jours, ne fournit qu'un seul ovule par cellule "
                "mère, pour un total d'environ quatre cent cinquante à cinq "
                "cents dans toute une vie, et sa méiose est bloquée à deux "
                "reprises."
            )
        ) as tracker:
            self.play(FadeIn(col_crit))
            self.play(FadeIn(col_sperm))
            self.play(FadeIn(col_ovo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Exemple traité : calcul de rendement -----------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "À partir de 800 spermatocytes I et 800 ovocytes I : "
                    "chaque spermatocyte I donne 4 spermatozoïdes, donc "
                    "800×4=3200 spermatozoïdes. Chaque ovocyte I donne 1 "
                    "ovule et 2 globules polaires, donc 800 ovules et "
                    "1600 globules polaires. La méiose femelle sacrifie "
                    "les trois quarts de ses produits pour concentrer les "
                    "réserves dans un seul ovule.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Calculons le rendement à partir de huit cents spermatocytes "
                "premiers et huit cents ovocytes premiers. Un spermatocyte "
                "premier donne quatre spermatozoïdes : huit cents fois quatre "
                "égale trois mille deux cents spermatozoïdes. Un ovocyte "
                "premier donne un ovule et deux globules polaires : huit "
                "cents ovules et mille six cents globules polaires. "
                "Conclusion : huit cents cellules mères fournissent trois "
                "mille deux cents gamètes mâles fonctionnels, contre "
                "seulement huit cents gamètes femelles fonctionnels."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        methode = method_box(
            Text(
                _wrap(
                    "Étape 1 : repérer la cellule qui entre en méiose "
                    "(spermatocyte I ou ovocyte I, 2n=46). Étape 2 : "
                    "appliquer le bilan - 1 cellule mâle donne 4 gamètes "
                    "fonctionnels, 1 cellule femelle donne 1 seul gamète "
                    "fonctionnel. Étape 3 : multiplier par le nombre de "
                    "cellules mères, puis conclure par une phrase rédigée.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour dénombrer les gamètes issus de la méiose : étape un, "
                "repérer la cellule qui entre en méiose, spermatocyte premier "
                "ou ovocyte premier, à deux n égale quarante-six chromosomes. "
                "Étape deux, appliquer le bilan de la méiose : chez le mâle, "
                "une cellule mère donne quatre gamètes fonctionnels ; chez la "
                "femelle, une seule cellule mère donne un seul gamète "
                "fonctionnel. Étape trois, multiplier par le nombre de "
                "cellules mères, puis conclure par une phrase rédigée."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- À retenir : la cryptorchidie, preuve naturelle -------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Chez certains nouveau-nés, un testicule ne descend pas "
                    "dans les bourses (cryptorchidie). Soumis à 37°C, il ne "
                    "produit pas de spermatozoïdes, mais ses cellules de "
                    "Leydig continuent de sécréter la testostérone : "
                    "l'enfant devient un homme stérile mais aux caractères "
                    "sexuels normaux. Preuve naturelle de l'indépendance "
                    "des deux fonctions.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une remarque intéressante : chez certains nouveau-nés, un "
                "testicule ne descend pas dans les bourses, c'est la "
                "cryptorchidie. Soumis à trente-sept degrés, ce testicule ne "
                "produit pas de spermatozoïdes, mais ses cellules de Leydig "
                "continuent de sécréter la testostérone : l'enfant devient un "
                "homme stérile, mais aux caractères sexuels normaux. Cette "
                "situation naturelle confirme l'indépendance des deux "
                "fonctions et l'exigence de température de la "
                "spermatogenèse."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Piège à éviter : les pièges de la gamétogenèse --------------------
        entete_piege = Text("Les pièges de la gamétogenèse", font_size=26, color=YELLOW, weight="BOLD")
        entete_piege.next_to(titre, DOWN, buff=0.5)

        pieges = _bullets(
            [
                "La méiose ne fabrique pas de chromosomes, elle les "
                "répartit : 2n=46 donne n=23, jamais 46.",
                "L'ovogenèse ne produit pas quatre ovules : un seul "
                "gamète fonctionnel par ovocyte I.",
                "Le stock de follicules ne se renouvelle pas : il est "
                "fixé avant la naissance.",
                "Un spermatozoïde n'est pas créé en quelques secondes : "
                "sa fabrication dure environ 70 jours.",
            ],
            width=48,
        )
        pieges.next_to(entete_piege, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quatre pièges à éviter absolument. La méiose ne fabrique pas "
                "de chromosomes, elle les répartit : une spermatogonie à deux "
                "n égale quarante-six donne des spermatozoïdes à n égale "
                "vingt-trois, jamais quarante-six. L'ovogenèse ne produit pas "
                "quatre ovules : un seul gamète fonctionnel est obtenu par "
                "ovocyte premier. Le stock de follicules de la femme ne se "
                "renouvelle pas : il est constitué avant la naissance. Enfin, "
                "un spermatozoïde n'est pas créé en quelques secondes : sa "
                "fabrication a duré environ soixante-dix jours."
            )
        ) as tracker:
            self.play(FadeIn(entete_piege))
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(entete_piege), FadeOut(pieges))
