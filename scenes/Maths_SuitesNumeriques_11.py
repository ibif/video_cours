"""
scenes/Maths_SuitesNumeriques_11.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 11.

Notions de limites de suites : définition intuitive, limites de référence,
opérations et comparaison (admis), théorème de comparaison et théorème des
gendarmes (admis). Exemple résolu 11 (deux cas).
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class NotionsLimitesSuites(NotionScene):
    def construct(self):
        titre = scene_title("Notions de limites de suites")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition intuitive -----------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    "(un) a pour limite +∞ si un devient aussi grand que l'on\n"
                    "veut dès que n est assez grand (idem pour -∞).",
                    font_size=21,
                ),
                Text(
                    "(un) a pour limite ℓ (finie) si un se rapproche d'aussi\n"
                    "près que l'on veut de ℓ dès que n est assez grand.",
                    font_size=21,
                ),
                Text(
                    "Une suite qui n'a pas de limite finie est dite divergente.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.2),
            box_width=11.2,
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Définition intuitive : une suite u indice n a pour limite "
                "plus l'infini si ses termes deviennent aussi grands que "
                "l'on veut, dès que n est pris assez grand — et de même "
                "pour moins l'infini. Elle a pour limite un réel ℓ si ses "
                "termes se rapprochent d'aussi près que l'on veut de ℓ, "
                "dès que n est assez grand. Une suite qui n'a pas de "
                "limite finie est dite divergente."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Théorème : limites de référence -----------------------------------------
        theo_ref = theorem_box(
            VGroup(
                Text("Limites de référence, quand n tend vers +∞ :", font_size=21, weight="BOLD"),
                MathTex(r"n\to+\infty, \ \ n^2\to+\infty, \ \ \sqrt{n}\to+\infty", font_size=24),
                MathTex(r"\dfrac{1}{n}\to 0, \quad \dfrac{1}{n^2}\to 0, \quad q^n\to 0 \ (|q|<1)", font_size=24),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        theo_ref.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Théorème : quelques limites de référence à connaître par "
                "cœur. n, n carré, et racine de n tendent tous vers plus "
                "l'infini. Un sur n, et un sur n carré, tendent vers zéro. "
                "Et q puissance n tend vers zéro dès que la valeur absolue "
                "de q est strictement inférieure à un."
            )
        ) as tracker:
            self.play(FadeIn(theo_ref))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_ref))

        # --- Théorème : opérations et comparaison (admis) -----------------------------
        theo_operations = theorem_box(
            VGroup(
                Text(
                    "Les limites de sommes, produits, quotients de suites\n"
                    "s'obtiennent comme pour les fonctions (théorèmes admis).",
                    font_size=21,
                ),
                Text(
                    "Formes indéterminées à traiter au cas par cas :\n"
                    "∞ - ∞ et 0 × ∞ (entre autres).",
                    font_size=21,
                    weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        theo_operations.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les limites de sommes, de produits et de quotients de "
                "suites s'obtiennent avec les mêmes règles que pour les "
                "fonctions, admises sans démonstration. Attention "
                "toutefois aux formes indéterminées, notamment plus "
                "l'infini moins l'infini, et zéro fois l'infini, qu'il "
                "faut lever au cas par cas, en général par factorisation."
            )
        ) as tracker:
            self.play(FadeIn(theo_operations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_operations))

        # --- Théorème de comparaison + gendarmes (admis) -------------------------------
        theo_comparaison = theorem_box(
            VGroup(
                Text("Comparaison (admis) :", font_size=21, weight="BOLD"),
                MathTex(r"u_n\geq v_n \text{ et } v_n\to+\infty \ \Longrightarrow\ u_n\to+\infty", font_size=22),
                Text("Théorème des gendarmes (admis) :", font_size=21, weight="BOLD"),
                MathTex(r"v_n\leq u_n\leq w_n \text{ et } v_n,w_n\to\ell \ \Longrightarrow\ u_n\to\ell", font_size=22),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        theo_comparaison.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux théorèmes admis, très utiles. Le théorème de "
                "comparaison : si u indice n est toujours supérieur ou "
                "égal à v indice n, et que v indice n tend vers plus "
                "l'infini, alors u indice n tend aussi vers plus l'infini. "
                "Le théorème des gendarmes : si u indice n est encadré "
                "entre v indice n et w indice n, et que ces deux suites "
                "tendent vers la même limite ℓ, alors u indice n tend "
                "aussi vers ℓ."
            )
        ) as tracker:
            self.play(FadeIn(theo_comparaison))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_comparaison))

        # --- Exemple résolu 11 ------------------------------------------------------
        ex11_titre = Text(
            "Exemple 11 :",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        ex11_titre.next_to(titre, DOWN, buff=0.35)
        ex11_a = example_box(
            MathTex(
                r"""
                a)\ u_n = \dfrac{2n+3}{n+1} = \dfrac{2+3/n}{1+1/n}
                \ \underset{n\to+\infty}{\longrightarrow}\ \dfrac{2}{1} = 2
                """,
                font_size=23,
            ),
            box_width=11.0,
        )
        ex11_a.next_to(ex11_titre, DOWN, buff=0.25)
        ex11_b = example_box(
            MathTex(
                r"""
                b)\ v_n = n^2-5n = n^2\left(1-\dfrac{5}{n}\right)
                \ \underset{n\to+\infty}{\longrightarrow}\ +\infty
                \ \ (\text{FI levée par factorisation})
                """,
                font_size=22,
            ),
            box_width=11.6,
        )
        ex11_b.next_to(ex11_a, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : a, u indice n égale deux n plus trois, sur n "
                "plus un. En factorisant par n en haut et en bas, on "
                "obtient deux plus trois sur n, sur un plus un sur n, qui "
                "tend vers deux sur un, soit deux, quand n tend vers plus "
                "l'infini. b, v indice n égale n carré moins cinq n, une "
                "forme indéterminée du type l'infini moins l'infini. En "
                "factorisant par le terme dominant, n carré, on obtient n "
                "carré fois, un moins cinq sur n, qui tend vers plus "
                "l'infini."
            )
        ) as tracker:
            self.play(FadeIn(ex11_titre))
            self.play(FadeIn(ex11_a))
            self.play(FadeIn(ex11_b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex11_titre), FadeOut(ex11_a), FadeOut(ex11_b))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Limites de référence à connaître par cœur. Devant une "
                    "forme indéterminée (∞-∞ ou 0×∞), factoriser par le "
                    "terme dominant avant de conclure.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : les limites de référence doivent être connues "
                "par cœur. Face à une forme indéterminée, le réflexe est "
                "presque toujours le même : factoriser par le terme "
                "dominant, en haut comme en bas, avant de conclure."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : ne jamais conclure trop vite sur une forme "
                    "∞-∞ ou 0×∞ « au feeling » — ces formes sont "
                    "indéterminées et exigent toujours une transformation "
                    "algébrique avant de connaître la vraie limite.",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : il ne faut jamais conclure trop "
                "rapidement, au feeling, sur une forme du type plus "
                "l'infini moins l'infini, ou zéro fois l'infini. Ces "
                "formes sont, par définition, indéterminées : elles "
                "exigent toujours une transformation algébrique, comme "
                "une factorisation, avant de pouvoir connaître la "
                "véritable limite."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
