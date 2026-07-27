"""
scenes/Physique_EnergiePotentielle_08.py — Chapitre 4 « Énergie potentielle »
(1ereC, Physique), scène 08.

Synthèse du chapitre : méthodes (calculer une énergie potentielle de
pesanteur, calculer une variation d'énergie potentielle de pesanteur,
travailler avec un ressort) et pièges à éviter (référence vs variation,
conversions d'unités, confusion des états initial/final).
Source : 1ereC/Physique.pdf, chapitre 4, pages 34-42.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse : méthodes et pièges à éviter")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : objectif de la synthèse ------------------------------------------
        intro = Text(
            _wrap(
                "Récapitulons les méthodes à connaître pour calculer une "
                "énergie potentielle, puis les pièges classiques à éviter "
                "sur ce chapitre.",
                width=54,
            ),
            font_size=25,
        )
        intro.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par une synthèse. Nous allons "
                "récapituler les trois méthodes essentielles à connaître "
                "pour calculer une énergie potentielle, puis passer en "
                "revue les pièges les plus fréquents à éviter."
            )
        ) as tracker:
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Méthode 1 : calculer une énergie potentielle de pesanteur -----------------
        methode1 = method_box(
            VGroup(
                Text("Calculer une énergie potentielle de pesanteur :", font_size=22),
                Text("1. Choisir une référence (Epp=0).", font_size=21),
                Text("2. Orienter l'axe vertical vers le haut.", font_size=21),
                Text("3. Repérer l'altitude z du système.", font_size=21),
                Text("4. Convertir les unités (SI).", font_size=21),
                MathTex(r"5.\; E_{pp} = mgz", font_size=27),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=8.6,
        )
        methode1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première méthode : calculer une énergie potentielle de "
                "pesanteur. On choisit d'abord une référence où Epp vaut "
                "zéro, on oriente l'axe vertical vers le haut, on repère "
                "l'altitude z du système, on convertit toutes les données "
                "dans le système international, puis on applique Epp égale "
                "m g z."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : calculer une variation d'énergie potentielle -------------------
        methode2 = method_box(
            VGroup(
                Text("Calculer une variation d'énergie potentielle :", font_size=22),
                MathTex(r"\Delta E_{pp} = mg\,(z_B - z_A)", font_size=27),
                Text("(état final B moins état initial A)", font_size=20),
                Text("Contrôler le signe selon montée/descente,", font_size=21),
                Text("puis en déduire le travail du poids : W=-ΔEpp.", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=9.6,
        )
        methode2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième méthode : calculer une variation d'énergie "
                "potentielle. On applique delta Epp égale m g fois z "
                "indice B moins z indice A, toujours l'état final moins "
                "l'état initial. On contrôle ensuite la cohérence du signe "
                "obtenu selon que le système monte ou descend, avant d'en "
                "déduire, si besoin, le travail du poids par la relation W "
                "égale moins delta Epp."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Méthode 3 : travailler avec un ressort --------------------------------------
        methode3 = method_box(
            VGroup(
                Text("Travailler avec un ressort :", font_size=22),
                MathTex(r"x = \ell - \ell_0 \; \text{(allongement algébrique)}", font_size=25),
                MathTex(r"E_{pe} = \dfrac{1}{2}kx^2 \; \text{(toujours} \geq 0\text{)}", font_size=27),
                Text("Travail de la tension : W=½kxA²-½kxB²", font_size=21),
            ).arrange(DOWN, buff=0.3),
            box_width=9.8,
        )
        methode3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième méthode : travailler avec un ressort. On "
                "calcule d'abord l'allongement algébrique x, égal à ℓ "
                "moins ℓ zéro. On applique ensuite Epe égale un demi k x "
                "carré, toujours positive ou nulle. Et si besoin, on "
                "calcule le travail de la tension avec la formule vue "
                "précédemment."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Piège 1 : référence vs variation -----------------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège n°1 — La valeur de Epp dépend de la référence "
                    "choisie, mais SA VARIATION n'en dépend jamais. Si "
                    "l'énoncé change de référence, ne refaites jamais un "
                    "calcul de variation : le résultat est identique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Premier piège classique : la valeur de Epp dépend de la "
                "référence choisie, mais sa variation, elle, n'en dépend "
                "jamais. Si un énoncé change de référence en cours de "
                "route, il est inutile — et même une perte de temps — de "
                "refaire un calcul de variation : le résultat sera "
                "rigoureusement identique."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        # --- Piège 2 : conversions ------------------------------------------------------------
        piege2 = warning_box(
            Text(
                _wrap(
                    "Piège n°2 — Les conversions d'unités : une masse "
                    "donnée en grammes doit être convertie en kilogrammes, "
                    "un allongement donné en centimètres doit être "
                    "converti en mètres, avant tout calcul.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege2.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Deuxième piège classique : les conversions d'unités. Une "
                "masse donnée en grammes doit impérativement être "
                "convertie en kilogrammes, et un allongement donné en "
                "centimètres doit être converti en mètres, avant "
                "d'appliquer la moindre formule."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        # --- Piège 3 : confusion des états initial/final --------------------------------------
        piege3formule = MathTex(
            r"\Delta E_p = E_p(B) - E_p(A) = -W_{A \to B}(\vec{F})",
            font_size=27,
        )
        piege3 = warning_box(
            VGroup(
                Text(
                    "Piège n°3 — Confusion des états : dans cette relation,",
                    font_size=22,
                ),
                piege3formule,
                Text(
                    "A est TOUJOURS l'état initial, B l'état final. Les "
                    "échanger change tous les signes ! Faites un schéma "
                    "avec l'axe Oz avant tout calcul.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.4,
        )
        piege3.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Troisième piège, sans doute le plus fréquent : la "
                "confusion des états initial et final. Dans la relation "
                "delta Ep égale Ep de B moins Ep de A, égale moins le "
                "travail de la force de A vers B, A désigne toujours l'état "
                "initial, et B l'état final. Les échanger inverse tous les "
                "signes du calcul ! Le réflexe à avoir : toujours faire un "
                "schéma avec l'axe Oz orienté, avant même de commencer le "
                "moindre calcul."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- À retenir : synthèse finale ------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Chapitre « Énergie potentielle » : Epp=mgz (référence "
                    "arbitraire), Epe=½kx² (référence : ressort non "
                    "déformé). Pour toute force conservative : "
                    "ΔEp=-W(F). Seules les variations d'énergie "
                    "potentielle ont un sens physique absolu.",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre : l'énergie potentielle de "
                "pesanteur vaut m g z, à une référence arbitraire près, et "
                "l'énergie potentielle élastique vaut un demi k x carré, "
                "avec pour référence le ressort non déformé. Pour toute "
                "force conservative, la variation de l'énergie potentielle "
                "associée vaut l'opposé du travail de cette force. Et par "
                "dessus tout, retenez que seules les variations d'énergie "
                "potentielle ont un sens physique absolu."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
