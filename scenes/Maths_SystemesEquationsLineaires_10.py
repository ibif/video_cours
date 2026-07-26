"""
scenes/Maths_SystemesEquationsLineaires_10.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 10 (synthèse
finale du chapitre).

§ Méthodes et astuces : choisir la bonne méthode de résolution, toujours
vérifier, mener le pivot de Gauss proprement, décrire une infinité de
solutions avec un paramètre λ. Pièges de synthèse : diviser par une
expression contenant un paramètre m sans vérifier qu'elle est non nulle ;
déterminant nul ≠ « pas de solution » ; signe des diagonales montantes de
Sarrus.
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW, RED

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MethodesAstucesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse — Méthodes, astuces et pièges à éviter")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Ce chapitre a présenté plusieurs méthodes de résolution : "
                "substitution, combinaison linéaire, pivot de Gauss, "
                "formules de Cramer. Terminons par une synthèse : comment "
                "choisir la bonne méthode, et quels sont les pièges à "
                "éviter absolument.",
                width=58,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce chapitre a présenté plusieurs méthodes de résolution : "
                "la substitution, la combinaison linéaire, le pivot de "
                "Gauss, et les formules de Cramer. Terminons par une "
                "synthèse : comment choisir la bonne méthode selon le "
                "système, et quels sont les pièges à éviter absolument."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : méthode "choisir la bonne méthode" ---------------------
        choix = VGroup(
            Text("• Un coefficient vaut 1 ou -1 → SUBSTITUTION.", font_size=22),
            Text("• Coefficients « opposables » par un facteur simple", font_size=22),
            Text("   → COMBINAISON LINÉAIRE.", font_size=22),
            Text("• Système 3×3 quelconque, sans piste évidente → PIVOT DE GAUSS.", font_size=22),
            Text("• Discussion selon un paramètre, ou système répété → CRAMER.", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        choix_box = method_box(choix, box_width=12.3)
        choix_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comment choisir sa méthode ? Si une inconnue a pour "
                "coefficient un ou moins un dans une équation, la "
                "substitution est la plus rapide. Si les coefficients "
                "peuvent être rendus opposés par un facteur simple, la "
                "combinaison linéaire est efficace. Pour un système 3×3 "
                "quelconque, sans piste évidente, le pivot de Gauss est la "
                "méthode la plus sûre et la plus systématique. Enfin, "
                "quand il faut discuter selon un paramètre, ou résoudre "
                "plusieurs systèmes ayant la même partie gauche, les "
                "formules de Cramer, qui donnent directement les formules "
                "de x, y (et z), sont les plus adaptées."
            )
        ) as tracker:
            self.play(FadeIn(choix_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(choix_box))

        # --- Méthode : toujours vérifier + décrire une infinité de solutions -------
        verif_texte = VGroup(
            Text("• Vérifier la solution dans TOUTES les équations", font_size=22),
            Text("   de départ, jamais une seule.", font_size=22),
            Text("• Infinité de solutions : introduire un paramètre λ", font_size=22),
            Text("   (souvent la dernière inconnue du pivot de Gauss).", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        verif_box = method_box(verif_texte, box_width=12.0)
        verif_box.next_to(titre, DOWN, buff=0.35)
        exemple_lambda = MathTex(
            r"\mathcal{S} = \{(8+\lambda\,;\,-2-3\lambda\,;\,\lambda),\ \lambda\in\mathbb{R}\}",
            font_size=22,
            color=YELLOW,
        )
        exemple_lambda.next_to(verif_box, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Deux réflexes à garder toujours en tête. D'abord, vérifier "
                "systématiquement la solution trouvée dans toutes les "
                "équations de départ, jamais une seule. Ensuite, pour "
                "décrire une infinité de solutions, on introduit un "
                "paramètre lambda, souvent la dernière inconnue obtenue par "
                "le pivot de Gauss, comme dans cet exemple déjà rencontré : "
                "l'ensemble des solutions huit plus lambda, moins deux "
                "moins trois lambda, lambda, pour lambda réel quelconque."
            )
        ) as tracker:
            self.play(FadeIn(verif_box))
            self.play(FadeIn(exemple_lambda))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(verif_box), FadeOut(exemple_lambda))

        # --- Pièges de synthèse (1) : division par un paramètre --------------------
        piege1_texte = Text(
            "Ne JAMAIS diviser par une expression contenant un\n"
            "paramètre m sans vérifier d'abord qu'elle est non nulle.",
            font_size=22,
        )
        piege1_ex = MathTex(
            r"x = \dfrac{3}{m-1} \quad \text{valide SEULEMENT si } m\neq 1",
            font_size=24,
            color=RED,
        )
        piege1 = VGroup(piege1_texte, piege1_ex).arrange(DOWN, buff=0.3)
        piege1_box = warning_box(piege1, box_width=12.0)
        piege1_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premier piège de synthèse, très classique dès qu'un "
                "système dépend d'un paramètre m : ne jamais diviser par "
                "une expression contenant m sans avoir d'abord vérifié "
                "qu'elle est non nulle. Par exemple, x égale trois sur, m "
                "moins un, n'est valide que si m est différent de un : le "
                "cas m égale un doit toujours être traité séparément."
            )
        ) as tracker:
            self.play(FadeIn(piege1_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1_box))

        # --- Pièges de synthèse (2) : D=0 et Sarrus --------------------------------
        piege2_texte = Text(
            "Déterminant nul ≠ « pas de solution » : D=0 signifie seulement\n"
            "« pas de solution unique ». Il faut résoudre le système\n"
            "directement (Gauss) pour trancher entre aucune solution et\n"
            "une infinité.",
            font_size=21,
        )
        piege2_box = warning_box(piege2_texte, box_width=12.3)
        piege2_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deuxième piège de synthèse, déjà rencontré deux fois dans "
                "ce chapitre : un déterminant nul ne signifie jamais "
                "« aucune solution ». Il signifie seulement « pas de "
                "solution unique ». Il faut toujours résoudre le système "
                "directement, en général avec le pivot de Gauss, pour "
                "trancher entre aucune solution et une infinité de "
                "solutions."
            )
        ) as tracker:
            self.play(FadeIn(piege2_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2_box))

        # --- Pièges de synthèse (3) : signe de Sarrus ---------------------------------
        piege3_texte = Text(
            "Dans la règle de Sarrus, les diagonales MONTANTES sont TOUJOURS\n"
            "précédées d'un signe moins. Si une vérification (par exemple\n"
            "avec Dx, Dy, Dz) échoue, recalculer D en premier : c'est\n"
            "l'erreur la plus fréquente du chapitre.",
            font_size=21,
        )
        piege3_box = warning_box(piege3_texte, box_width=12.3)
        piege3_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège de synthèse : dans la règle de Sarrus, les "
                "diagonales montantes sont toujours précédées d'un signe "
                "moins. Si une vérification ne tombe pas juste, par exemple "
                "avec D indice x, D indice y ou D indice z, c'est souvent "
                "ce signe qui a été oublié : recalculez D en premier, "
                "c'est l'erreur la plus fréquente de tout ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(piege3_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3_box))

        # --- L'essentiel à retenir (synthèse finale du chapitre) ------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "2×2 : substitution, combinaison, ou Cramer avec "
                        "D=ab'-a'b. 3×3 : substitution, pivot de Gauss, ou "
                        "Cramer avec Sarrus. D≠0 → solution unique. Sinon, "
                        "résoudre directement pour trancher entre aucune "
                        "solution et une infinité.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.26),
            box_width=12.2,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de ce chapitre : pour un système "
                "2×2, on choisit entre substitution, combinaison linéaire, "
                "ou les formules de Cramer avec D égale a b prime moins a "
                "prime b. Pour un système 3×3, on choisit entre "
                "substitution, pivot de Gauss, ou Cramer avec la règle de "
                "Sarrus. Dans tous les cas, un déterminant non nul donne "
                "une solution unique ; sinon, il faut toujours résoudre "
                "directement le système pour trancher entre aucune "
                "solution et une infinité de solutions."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
