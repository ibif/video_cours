"""
scenes/Maths_Barycentre_12.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 12 (dernière).

§ Synthèse du chapitre : 6 fiches méthode, 3 pièges à éviter, astuce
« moyennes scolaires = barycentre », essentiel à retenir final.
Source : 1ereC/Maths.pdf, chapitre 4, pages 50-51.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesEtEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Méthodes, pièges et essentiel")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : introduction de la synthèse -------------------------------
        intro = Text(
            _wrap(
                "Nous avons parcouru tout le chapitre du barycentre. "
                "Faisons maintenant la synthèse des méthodes-clés, des "
                "pièges à éviter, et de l'essentiel à retenir.",
                width=54,
            ),
            font_size=25,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons parcouru tout le chapitre du barycentre, de "
                "l'existence et l'unicité jusqu'aux lignes de niveau. "
                "Faisons à présent la synthèse : les méthodes-clés à "
                "maîtriser, les pièges à éviter, et l'essentiel à "
                "retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : 6 fiches méthode ------------------------------------
        methodes = [
            (
                "Construire bar{(A,α) ; (B,β)}",
                r"\overrightarrow{AG}=\dfrac{\beta}{\alpha+\beta}\,\overrightarrow{AB}",
                "Calculer le coefficient de position sur (AB), puis placer G.",
            ),
            (
                "Construire un barycentre de 3 points",
                r"\text{réduction vectorielle } \textbf{ou} \text{ barycentres partiels}",
                "Directement par réduction, ou en 2 étapes via l'associativité.",
            ),
            (
                "Réduire α MA⃗+β MB⃗+γ MC⃗",
                r"=(\alpha+\beta+\gamma)\,\overrightarrow{MG}",
                "Vérifier d'abord que α+β+γ≠0.",
            ),
            (
                "Démontrer un alignement",
                r"K=\mathrm{bar}\{(I,x)\,;\,(J,y)\} \ \Rightarrow\ K\in(IJ)",
                "Exprimer un point comme barycentre des deux autres.",
            ),
            (
                "Démontrer un concours",
                r"\text{un même } G,\ 3 \text{ regroupements différents}",
                "Chaque regroupement place G sur une droite différente.",
            ),
            (
                "Lignes de niveau",
                r"a\,MA^2+b\,MB^2=k \ \text{ ou } \ \dfrac{MA}{MB}=k",
                "Identifier a+b (ou k=1) pour choisir : ∅, point, cercle, droite.",
            ),
        ]

        for num, (titre_methode, formule, astuce) in enumerate(methodes, start=1):
            contenu = VGroup(
                Text(f"{num}. {titre_methode}", font_size=24, weight="BOLD"),
                MathTex(formule, font_size=24),
                Text(_wrap(astuce, width=46), font_size=20),
            ).arrange(DOWN, buff=0.22)
            fiche = method_box(contenu)
            fiche.next_to(titre, DOWN, buff=0.5)

            with self.voiceover(text=f"Méthode {num} : {titre_methode}. {astuce}") as tracker:
                self.play(FadeIn(fiche))
                self.wait(tracker.get_remaining_duration())

            self.play(FadeOut(fiche))

        # --- Pièges à éviter : 3 rappels ----------------------------------------
        pieges = [
            "Toujours vérifier que la somme des coefficients est non nulle avant d'affirmer l'existence d'un barycentre.",
            "Le barycentre n'est pas toujours situé entre les points : selon le signe des coefficients, il peut être à l'extérieur du segment.",
            "Associativité mal appliquée : avant de regrouper deux points en un barycentre partiel de coefficient m, vérifier que la somme des deux coefficients regroupés vaut bien m et est non nulle.",
        ]
        for num, texte in enumerate(pieges, start=1):
            contenu = Text(_wrap(f"Piège {num} : {texte}", width=48), font_size=22)
            piege_box = warning_box(contenu)
            piege_box.next_to(titre, DOWN, buff=0.5)

            with self.voiceover(text=texte) as tracker:
                self.play(FadeIn(piege_box))
                self.wait(tracker.get_remaining_duration())

            self.play(FadeOut(piege_box))

        # --- Exemple traité : astuce moyennes scolaires -------------------------
        astuce_contenu = VGroup(
            Text("Astuce : une moyenne pondérée est un barycentre !", font_size=24, weight="BOLD"),
            MathTex(
                r"\text{Moyenne} = \dfrac{c_1 n_1+c_2 n_2+\cdots}{c_1+c_2+\cdots}"
                r"\ \longleftrightarrow\ x_G=\dfrac{\alpha x_A+\beta x_B}{\alpha+\beta}",
                font_size=22,
            ),
            Text(
                _wrap(
                    "Les notes jouent le rôle des abscisses, les "
                    "coefficients des devoirs jouent le rôle des masses "
                    "α, β… du barycentre.",
                    width=46,
                ),
                font_size=20,
            ),
        ).arrange(DOWN, buff=0.25)
        astuce_box = method_box(astuce_contenu)
        astuce_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une dernière astuce, pour boucler la boucle avec notre "
                "mise en situation du tout début du chapitre : une "
                "moyenne pondérée scolaire EST un barycentre ! La "
                "formule, notes multipliées par leurs coefficients, "
                "divisée par la somme des coefficients, est exactement "
                "la formule des coordonnées d'un barycentre : les notes "
                "jouent le rôle des abscisses, et les coefficients des "
                "devoirs jouent le rôle des masses alpha, bêta, du "
                "barycentre."
            )
        ) as tracker:
            self.play(FadeIn(astuce_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(astuce_box))

        # --- À retenir : essentiel du chapitre -----------------------------------
        essentiel_contenu = VGroup(
            Text("L'ESSENTIEL DU CHAPITRE « BARYCENTRE »", font_size=22, weight="BOLD"),
            MathTex(r"\alpha+\cdots\neq 0 \ \Rightarrow\ \exists !\ G,\ \textstyle\sum \alpha_i\overrightarrow{GA_i}=\vec 0", font_size=21),
            MathTex(r"\textstyle\sum\alpha_i\overrightarrow{MA_i} = \big(\textstyle\sum\alpha_i\big)\overrightarrow{MG}", font_size=21),
            MathTex(r"x_G=\dfrac{\sum \alpha_i x_{A_i}}{\sum\alpha_i}\ \ (\text{idem } y_G)"
                     r"\qquad \text{homogénéité, associativité}", font_size=20),
            Text("Alignement / concours par barycentres · lignes de niveau : ∅, point, cercle ou droite.", font_size=18),
        ).arrange(DOWN, buff=0.22)
        essentiel = essentiel_box(essentiel_contenu)
        essentiel.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour conclure, l'essentiel du chapitre sur le "
                "barycentre. Dès que la somme des coefficients est non "
                "nulle, il existe un unique barycentre G, caractérisé par "
                "la somme nulle des vecteurs pondérés G-A-i. Pour tout "
                "point M, la somme pondérée des vecteurs M-A-i se réduit "
                "à la somme des coefficients, fois le vecteur M-G. Les "
                "coordonnées de G s'obtiennent par moyenne pondérée, "
                "grâce à l'homogénéité et à l'associativité. Enfin, le "
                "barycentre permet de démontrer alignements et concours, "
                "et de décrire les lignes de niveau : l'ensemble vide, un "
                "point, un cercle, ou une droite."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
