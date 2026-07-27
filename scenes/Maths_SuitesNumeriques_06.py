"""
scenes/Maths_SuitesNumeriques_06.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 06.

Suites arithmétiques : définition, propriété caractéristique, moyenne
arithmétique, théorème du terme général (avec démonstration complète par
récurrence) et sens de variation. Exemple résolu 6.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import (
    definition_box,
    essentiel_box,
    example_box,
    property_box,
    scene_title,
    theorem_box,
    warning_box,
)


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SuitesArithmetiques(NotionScene):
    def construct(self):
        titre = scene_title("Suites arithmétiques — définition et terme général")
        titre.scale(0.44)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition ----------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    "(un) est arithmétique de raison r s'il existe un réel r tel\n"
                    "que, pour tout n :",
                    font_size=22,
                ),
                MathTex(r"u_{n+1} = u_n + r", font_size=32),
                Text(
                    "Propriété caractéristique : la différence entre deux termes\n"
                    "consécutifs est toujours constante, égale à r.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une suite u indice n est arithmétique de raison r s'il "
                "existe un réel r tel que, pour tout entier n, u indice n "
                "plus un égale u indice n plus r. Autrement dit : on passe "
                "d'un terme au suivant en ajoutant toujours la même "
                "quantité r. C'est la propriété caractéristique des "
                "suites arithmétiques : une différence constante entre "
                "deux termes consécutifs."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Moyenne arithmétique ---------------------------------------------------
        moyenne = property_box(
            VGroup(
                Text(
                    "Si a, b, c sont trois termes consécutifs d'une suite\n"
                    "arithmétique, b est la moyenne arithmétique de a et c :",
                    font_size=21,
                ),
                MathTex(r"2b = a+c", font_size=30),
            ).arrange(DOWN, buff=0.25),
            box_width=10.2,
        )
        moyenne.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Propriété de la moyenne arithmétique : si a, b, c sont "
                "trois termes consécutifs d'une suite arithmétique, alors "
                "b est la moyenne arithmétique de a et de c, c'est-à-dire "
                "que deux fois b égale a plus c. Cela vient directement du "
                "fait que b moins a et c moins b valent tous les deux r."
            )
        ) as tracker:
            self.play(FadeIn(moyenne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(moyenne))

        # --- Théorème : terme général ------------------------------------------------
        theo_terme = theorem_box(
            VGroup(
                MathTex(r"u_n = u_0 + nr", font_size=32),
                MathTex(r"u_n = u_p + (n-p)r", font_size=32),
            ).arrange(DOWN, buff=0.25),
            box_width=8.5,
        )
        theo_terme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Théorème du terme général : pour une suite arithmétique "
                "de raison r, u indice n égale u zéro plus n fois r. Plus "
                "généralement, en partant d'un terme quelconque u indice "
                "p : u indice n égale u indice p plus, n moins p, fois r."
            )
        ) as tracker:
            self.play(FadeIn(theo_terme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_terme))

        # --- Démonstration par récurrence -------------------------------------------
        demo_titre = Text(
            "Démonstration de un = u0 + nr, par récurrence sur n :",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        demo_titre.next_to(titre, DOWN, buff=0.35)
        demo_init = MathTex(
            r"\text{Initialisation : } u_0 = u_0+0\times r \ \text{ vraie.}",
            font_size=24,
        )
        demo_init.next_to(demo_titre, DOWN, buff=0.3)
        demo_heredite = VGroup(
            MathTex(
                r"\text{Hérédité : on suppose } u_n=u_0+nr \text{ pour un } n \text{ fixé.}",
                font_size=24,
            ),
            MathTex(
                r"u_{n+1} = u_n+r = (u_0+nr)+r = u_0+(n+1)r",
                font_size=26,
            ),
            Text(
                "La propriété est donc vraie au rang n+1.",
                font_size=22,
            ),
        ).arrange(DOWN, buff=0.2)
        demo_heredite.next_to(demo_init, DOWN, buff=0.3)
        demo_concl = Text(
            "Conclusion : la propriété est vraie pour tout n (principe de récurrence).",
            font_size=21,
        )
        demo_concl.next_to(demo_heredite, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Démontrons ce résultat par récurrence sur n. "
                "Initialisation : au rang zéro, u zéro égale u zéro plus "
                "zéro fois r, ce qui est évidemment vrai. Hérédité : on "
                "suppose la propriété vraie à un rang n fixé, c'est-à-dire "
                "u indice n égale u zéro plus n r. Alors u indice n plus "
                "un égale u indice n plus r, donc, par hypothèse, u zéro "
                "plus n r plus r, soit u zéro plus n plus un fois r. La "
                "propriété est donc vraie au rang n plus un. D'après le "
                "principe de récurrence, elle est vraie pour tout entier "
                "n."
            )
        ) as tracker:
            self.play(FadeIn(demo_titre))
            self.play(FadeIn(demo_init))
            self.play(FadeIn(demo_heredite))
            self.play(FadeIn(demo_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(demo_titre), FadeOut(demo_init), FadeOut(demo_heredite), FadeOut(demo_concl)
        )

        # --- Théorème : sens de variation ---------------------------------------------
        theo_variation = theorem_box(
            VGroup(
                Text("Sens de variation d'une suite arithmétique de raison r :", font_size=22, weight="BOLD"),
                MathTex(r"r>0 \Longrightarrow (u_n) \text{ croissante}", font_size=26),
                MathTex(r"r<0 \Longrightarrow (u_n) \text{ décroissante}", font_size=26),
                MathTex(r"r=0 \Longrightarrow (u_n) \text{ constante}", font_size=26),
            ).arrange(DOWN, buff=0.2),
            box_width=10.0,
        )
        theo_variation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le sens de variation d'une suite arithmétique se lit "
                "directement sur le signe de sa raison r. Si r est "
                "strictement positif, la suite est croissante. Si r est "
                "strictement négatif, elle est décroissante. Et si r est "
                "nul, la suite est constante."
            )
        ) as tracker:
            self.play(FadeIn(theo_variation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_variation))

        # --- Exemple résolu 6 ----------------------------------------------------
        ex6_titre = Text(
            "Exemple 6 — suite arithmétique avec u2 = 7 et u6 = 19 :",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        ex6_titre.next_to(titre, DOWN, buff=0.35)
        ex6_calc = example_box(
            MathTex(
                r"""
                u_6 = u_2+4r \Longrightarrow 19=7+4r \Longrightarrow r=3
                \qquad u_0=u_2-2r=7-6=1
                """,
                font_size=22,
            ),
            box_width=11.4,
        )
        ex6_calc.next_to(ex6_titre, DOWN, buff=0.25)
        ex6_concl = MathTex(
            r"u_n = 1+3n \qquad u_{15} = 1+45 = 46",
            font_size=27,
        )
        ex6_concl.next_to(ex6_calc, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : une suite arithmétique vérifie u deux égale "
                "sept et u six égale dix-neuf. Comme u six égale u deux "
                "plus quatre r, on obtient dix-neuf égale sept plus quatre "
                "r, donc r égale trois. On en déduit u zéro égale u deux "
                "moins deux r, soit sept moins six, égale un. La formule "
                "du terme général est donc u indice n égale un plus trois "
                "n, et u quinze égale un plus quarante-cinq, soit "
                "quarante-six."
            )
        ) as tracker:
            self.play(FadeIn(ex6_titre))
            self.play(FadeIn(ex6_calc))
            self.play(FadeIn(ex6_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex6_titre), FadeOut(ex6_calc), FadeOut(ex6_concl))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Suite arithmétique : un+1 = un + r (différence "
                    "constante). un = u0 + nr = up + (n-p)r. Sens de "
                    "variation donné par le signe de r.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : une suite arithmétique avance toujours du "
                "même pas r. Son terme général se calcule directement à "
                "partir de n'importe quel terme connu, et son sens de "
                "variation dépend uniquement du signe de r."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                "Piège : un = up + (n-p)r, pas (n-p+1)r ni nr si p ≠ 0 — "
                "compter précisément le nombre de « pas » de raison r "
                "entre le rang p et le rang n.",
                font_size=21,
            ),
            box_width=11.4,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : dans la formule u indice n égale u "
                "indice p plus, n moins p, fois r, il faut bien compter le "
                "nombre exact de pas de raison r entre le rang p et le "
                "rang n — une erreur d'un cran dans ce décompte est très "
                "fréquente."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
