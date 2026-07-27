"""
scenes/Maths_LimitesContinuite_04.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 04.

Opérations sur les limites (somme, produit, quotient) et les quatre formes
indéterminées.
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class OperationsSurLesLimites(NotionScene):
    def construct(self):
        titre = scene_title("Opérations sur les limites — formes indéterminées")
        titre.scale(0.5)
        titre.to_edge(UP)

        intro = Text(
            _wrap(
                "Quand f et g ont chacune une limite (finie ou infinie) en "
                "x0, on peut souvent en déduire la limite de f+g, f×g ou "
                "f/g... sauf dans quatre cas.",
                width=56,
            ),
            font_size=23,
        )
        intro.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Lorsque f et g ont chacune une limite, finie ou infinie, "
                "en x zéro, on peut souvent en déduire directement la "
                "limite de leur somme, de leur produit ou de leur quotient. "
                "Mais il existe quatre situations où cela ne fonctionne "
                "pas : ce sont les formes indéterminées."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Tableau somme -------------------------------------------------------
        tab_somme_titre = Text("Limite d'une somme f + g :", font_size=23, color="#288073", weight="BOLD")
        tab_somme_titre.next_to(titre, DOWN, buff=0.35)
        tab_somme = MathTex(
            r"""
            \begin{array}{|c|c|c|c|}
            \hline
            \lim f & \ell & \ell & +\infty \\
            \lim g & \ell' & +\infty \text{ ou } -\infty & +\infty \\
            \hline
            \lim (f+g) & \ell+\ell' & +\infty \text{ ou } -\infty & +\infty \\
            \hline
            \end{array}
            \qquad
            \begin{array}{|c|c|}
            \hline
            \lim f = +\infty,\ \lim g = -\infty & \text{F.I. } (+\infty)-\infty \\
            \hline
            \end{array}
            """,
            font_size=20,
        )
        tab_somme_box = property_box(VGroup(tab_somme), box_width=12.2)
        tab_somme_box.next_to(tab_somme_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Pour une somme, les cas se combinent naturellement : "
                "limite finie plus limite finie donne la somme des deux ; "
                "limite finie plus l'infini donne l'infini correspondant ; "
                "plus l'infini plus plus l'infini donne plus l'infini. Seul "
                "cas problématique : plus l'infini plus moins l'infini, "
                "c'est une forme indéterminée, notée plus l'infini moins "
                "l'infini."
            )
        ) as tracker:
            self.play(FadeIn(tab_somme_titre))
            self.play(FadeIn(tab_somme_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_somme_titre), FadeOut(tab_somme_box))

        # --- Tableau produit -------------------------------------------------------
        tab_produit_titre = Text("Limite d'un produit f × g :", font_size=23, color="#288073", weight="BOLD")
        tab_produit_titre.next_to(titre, DOWN, buff=0.35)
        tab_produit = MathTex(
            r"""
            \begin{array}{|c|c|c|}
            \hline
            \lim f & \ell \ (\ell\neq 0) & \pm\infty \\
            \lim g & \pm\infty & \pm\infty \\
            \hline
            \lim (f\times g) & \pm\infty \text{ (règle des signes)} & \pm\infty \text{ (règle des signes)} \\
            \hline
            \end{array}
            \qquad
            \begin{array}{|c|c|}
            \hline
            \lim f = 0,\ \lim g = \pm\infty & \text{F.I. } 0\times\infty \\
            \hline
            \end{array}
            """,
            font_size=19,
        )
        tab_produit_box = property_box(VGroup(tab_produit), box_width=12.2)
        tab_produit_box.next_to(tab_produit_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Pour un produit, on applique la règle des signes usuelle "
                "dès que l'une des deux limites est infinie et l'autre non "
                "nulle. Le cas problématique est celui où l'une des "
                "limites vaut zéro pendant que l'autre est infinie : c'est "
                "la forme indéterminée zéro fois l'infini."
            )
        ) as tracker:
            self.play(FadeIn(tab_produit_titre))
            self.play(FadeIn(tab_produit_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_produit_titre), FadeOut(tab_produit_box))

        # --- Tableau quotient -------------------------------------------------------
        tab_quotient_titre = Text("Limite d'un quotient f / g :", font_size=23, color="#288073", weight="BOLD")
        tab_quotient_titre.next_to(titre, DOWN, buff=0.35)
        tab_quotient = MathTex(
            r"""
            \begin{array}{|c|c|c|}
            \hline
            \lim f & \ell & \pm\infty \\
            \lim g & \ell' \neq 0 \text{ ou } \pm\infty & \ell' \neq 0 \\
            \hline
            \lim (f/g) & \ell/\ell' \text{ ou } 0 & \pm\infty \text{ (règle des signes)} \\
            \hline
            \end{array}
            """,
            font_size=20,
        )
        tab_quotient_box = property_box(VGroup(tab_quotient), box_width=11.5)
        tab_quotient_box.next_to(tab_quotient_titre, DOWN, buff=0.25)

        fi_quotient = MathTex(
            r"\dfrac{\pm\infty}{\pm\infty} \ \text{: F.I.} \qquad \dfrac{0}{0} \ \text{: F.I.}",
            font_size=26,
            color="#B42E41",
        )
        fi_quotient.next_to(tab_quotient_box, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Pour un quotient, dès que le dénominateur a une limite "
                "finie non nulle, tout se passe bien. Mais deux cas restent "
                "indéterminés : l'infini sur l'infini, et zéro sur zéro. Ce "
                "sont les deux dernières formes indéterminées à connaître."
            )
        ) as tracker:
            self.play(FadeIn(tab_quotient_titre))
            self.play(FadeIn(tab_quotient_box))
            self.play(Write(fi_quotient))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_quotient_titre), FadeOut(tab_quotient_box), FadeOut(fi_quotient))

        # --- Récapitulatif des 4 F.I. --------------------------------------------
        recap_titre = Text("Les quatre formes indéterminées :", font_size=25, color="#288073", weight="BOLD")
        recap_titre.next_to(titre, DOWN, buff=0.4)
        recap = MathTex(
            r"(+\infty)-\infty \qquad 0\times\infty \qquad \dfrac{\infty}{\infty} \qquad \dfrac{0}{0}",
            font_size=34,
        )
        recap.next_to(recap_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Récapitulons : les quatre formes indéterminées à toujours "
                "avoir en tête sont plus l'infini moins l'infini, zéro fois "
                "l'infini, l'infini sur l'infini, et zéro sur zéro. Face à "
                "l'une d'elles, il faut transformer l'expression avant de "
                "pouvoir conclure : c'est l'objet des méthodes des "
                "prochaines scènes."
            )
        ) as tracker:
            self.play(FadeIn(recap_titre))
            self.play(Write(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap_titre), FadeOut(recap))

        # --- Piège --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Face à une forme indéterminée, on ne peut RIEN conclure "
                    "directement : il faut transformer l'écriture (voir les "
                    "méthodes suivantes) avant de reprendre les tableaux "
                    "ci-dessus.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention : une forme indéterminée ne veut pas dire que la "
                "limite n'existe pas ni qu'elle vaut zéro ou l'infini — "
                "cela veut dire qu'on ne peut rien conclure sans transformer "
                "d'abord l'expression."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
