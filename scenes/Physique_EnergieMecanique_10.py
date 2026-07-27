"""
scenes/Physique_EnergieMecanique_10.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 10.

Synthèse du chapitre : méthode pour résoudre un problème d'énergie
mécanique en 5 étapes, méthode pour vérifier la cohérence d'un résultat,
méthode pour le cas du pendule et des rotations, et pièges à éviter
(référence des altitudes, travail des frottements dépendant du chemin,
identification de ce qui se conserve).
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse : méthodes et pièges à éviter")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : objectif de la synthèse ---------------------------------------
        intro = Text(
            _wrap(
                "Terminons ce chapitre par une synthèse : les méthodes "
                "essentielles pour résoudre un problème d'énergie "
                "mécanique, puis les pièges classiques à éviter.",
                width=54,
            ),
            font_size=24,
        )
        intro.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Terminons ce chapitre sur l'énergie mécanique par une "
                "synthèse. Nous allons récapituler les méthodes "
                "essentielles pour résoudre un problème d'énergie "
                "mécanique, puis passer en revue les pièges les plus "
                "fréquents à éviter."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Méthode 1 : résoudre un problème d'énergie mécanique en 5 étapes --------
        methode1 = method_box(
            VGroup(
                Text("Résoudre un problème d'énergie mécanique :", font_size=21),
                Text("1. Définir le système et le référentiel.", font_size=20),
                Text("2. Faire le bilan des forces qui travaillent.", font_size=20),
                Text("3. Choisir une référence pour les énergies potentielles.", font_size=20),
                Text("4. Choisir la bonne loi : conservation ou non-conservation.", font_size=20),
                Text("5. Écrire l'équation d'énergie et isoler l'inconnue.", font_size=20),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.0,
        )
        methode1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première méthode, en cinq étapes, pour résoudre tout "
                "problème d'énergie mécanique. Un : définir précisément le "
                "système étudié et le référentiel. Deux : faire le bilan "
                "des forces qui travaillent réellement sur ce système. "
                "Trois : choisir une référence pour les énergies "
                "potentielles. Quatre : choisir la loi adaptée, "
                "conservation si aucune force non conservative ne "
                "travaille, non-conservation sinon. Cinq : écrire "
                "l'équation d'énergie correspondante, et isoler "
                "l'inconnue cherchée."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : vérifier la cohérence du résultat ---------------------------
        methode2 = method_box(
            VGroup(
                Text("Vérifier la cohérence d'un résultat :", font_size=21),
                Text("• Le radicande d'une racine carrée doit être ≥ 0.", font_size=20),
                Text("• Une hauteur de remontée ne dépasse jamais la hauteur", font_size=20),
                Text("   de départ (sauf apport d'énergie extérieure).", font_size=20),
                Text("• Énergie dissipée = chute d'énergie mécanique observée.", font_size=20),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.2,
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : vérifier systématiquement la cohérence "
                "du résultat obtenu. Le radicande d'une racine carrée doit "
                "toujours être positif ou nul. Une hauteur de remontée ne "
                "peut jamais dépasser la hauteur de départ, sauf si une "
                "énergie extérieure est apportée au système. Et l'énergie "
                "dissipée par frottement doit toujours correspondre "
                "exactement à la chute d'énergie mécanique observée."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Méthode 3 : cas du pendule et des rotations ------------------------------
        methode3 = method_box(
            VGroup(
                Text("Cas du pendule et des rotations :", font_size=21),
                MathTex(r"E_c = \tfrac{1}{2}J_\Delta \omega^2 \quad \text{(rotation)}", font_size=25),
                MathTex(r"z_G = L(1-\cos\theta) \quad \text{(pendule)}", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=9.0,
        )
        methode3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième méthode : pour un solide en rotation, utiliser "
                "l'énergie cinétique de rotation, un demi J delta oméga "
                "carré. Pour un pendule, ou tout mouvement circulaire "
                "vertical, exprimer l'altitude du centre de gravité sous la "
                "forme z G égale L fois un moins cosinus thêta, jamais "
                "L fois thêta directement."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Piège 1 : référence des altitudes ----------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège n°1 — Une fois choisie, la référence des "
                    "altitudes (Epp=0) ne doit JAMAIS changer en cours de "
                    "calcul. Fixez-la dès le départ et gardez-la jusqu'à "
                    "la fin du problème.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Premier piège classique : une fois choisie, la référence "
                "des altitudes, où l'énergie potentielle de pesanteur est "
                "nulle, ne doit jamais changer en cours de calcul. Fixez-la "
                "dès le départ, et gardez-la jusqu'à la toute fin du "
                "problème."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        # --- Piège 2 : travail des frottements dépend du chemin ----------------------
        piege2 = warning_box(
            VGroup(
                Text("Piège n°2 — Le travail des frottements dépend du chemin :", font_size=21),
                MathTex(r"W(\vec{f}) = -f\ell, \quad \ell = \text{longueur du trajet}", font_size=24),
                Text("Un aller-retour de longueur ℓ chacun donne -2fℓ, pas -fℓ.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.4,
        )
        piege2.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Deuxième piège classique : le travail des frottements "
                "dépend du chemin suivi. Il vaut moins f ℓ, où ℓ est la "
                "longueur réellement parcourue. Sur un aller-retour, où "
                "chaque trajet mesure ℓ, le travail total vaut moins deux f "
                "ℓ, et non pas moins f ℓ : ne l'oubliez jamais."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        # --- Piège 3 : bien identifier ce qui se conserve -----------------------------
        piege3 = warning_box(
            Text(
                _wrap(
                    "Piège n°3 — Em ne se conserve QUE si aucune force non "
                    "conservative ne travaille. Ne confondez pas avec Ec "
                    "ou Ep, qui varient individuellement même quand Em "
                    "est constante. Et n'oubliez jamais le ½ dans Ec=½mv².",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.4,
        )
        piege3.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Troisième piège, le plus important : l'énergie mécanique "
                "ne se conserve que si aucune force non conservative ne "
                "travaille. Ne confondez surtout pas cette conservation "
                "avec l'énergie cinétique ou l'énergie potentielle prises "
                "séparément, qui varient individuellement même quand "
                "l'énergie mécanique, elle, reste constante. Et, comme "
                "toujours, n'oubliez jamais le facteur un demi dans "
                "l'expression de l'énergie cinétique."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- À retenir : synthèse finale du chapitre ----------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Chapitre « Énergie mécanique » : Em=Ec+Ep. Sans force "
                    "non conservative (ou à travail nul) : Em=constante. "
                    "Avec frottements ou force motrice : "
                    "ΔEm=ΣW(forces non conservatives).",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre : l'énergie mécanique d'un "
                "système vaut la somme de son énergie cinétique et de son "
                "énergie potentielle. En l'absence de force non "
                "conservative, ou en présence uniquement de forces à "
                "travail nul, elle reste constante. Dès qu'apparaissent des "
                "frottements ou une force motrice, sa variation est égale "
                "à la somme des travaux de ces forces non conservatives. "
                "Ces principes s'appliquent à la chute libre, au pendule "
                "simple, comme à tout mouvement sur une piste."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
