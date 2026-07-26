"""
scenes/SVT_HerediteMendelienne_06.py — Chapitre 6 (1ereC, SVT), scène 06.

§ III.3-III.4 Deuxième expérience (croisement des hybrides F1 entre eux,
F2 : 3/4-1/4 avec les chiffres réels 5474/7324 et 1850/7324), deuxième
loi de Mendel (disjonction des allèles), et interprétation
chromosomique (4 combinaisons équiprobables). Source : 1ereC/SVT.pdf,
page 60.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Create,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class DisjonctionDesAlleles(NotionScene):
    def construct(self):
        titre = scene_title("6.6 — F2 : la disjonction des allèles")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : F1 x F1 --------------------------------------------------
        intro = Text(
            _wrap(
                "Mendel laisse ensuite les plants F1 (Ll) se féconder "
                "entre eux. Que va-t-il se passer en deuxième génération, "
                "notée F2 ?",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Mendel laisse ensuite les plants F un, tous L l, se "
                "féconder entre eux. Que va-t-il se passer en deuxième "
                "génération, notée F deux ? L'allèle ridée, l, a-t-il "
                "vraiment disparu ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les chiffres réels de Mendel -----------
        entete_chiffres = Text("Les résultats de Mendel sur 7324 graines", font_size=23, color=YELLOW, weight="BOLD")
        entete_chiffres.next_to(titre, DOWN, buff=0.5)

        resultats = _bullets(
            [
                "5474 graines lisses, soit environ 3/4 de la "
                "descendance.",
                "1850 graines ridées, soit environ 1/4 de la "
                "descendance.",
            ],
            font_size=24,
            width=48,
        )
        resultats.next_to(entete_chiffres, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En deuxième génération, sur sept mille trois cent "
                "vingt-quatre graines récoltées, Mendel obtient : cinq "
                "mille quatre cent soixante-quatorze graines lisses, soit "
                "environ trois quarts de la descendance ; et mille huit "
                "cent cinquante graines ridées, soit environ un quart de "
                "la descendance. Le caractère ridée, disparu en F un, "
                "réapparaît donc en F deux !"
            )
        ) as tracker:
            self.play(FadeIn(entete_chiffres))
            self.play(FadeIn(resultats))
            self.wait(tracker.get_remaining_duration())

        verif = MathTex(
            r"\dfrac{5474}{7324} \approx 0{,}747 \approx \dfrac{3}{4}"
            r"\qquad\qquad"
            r"\dfrac{1850}{7324} \approx 0{,}253 \approx \dfrac{1}{4}",
            font_size=28,
            color=WHITE,
        )
        verif.next_to(resultats, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Vérifions ce rapport : cinq mille quatre cent "
                "soixante-quatorze sur sept mille trois cent vingt-quatre "
                "est environ égal à zéro virgule sept cent quarante-sept, "
                "soit environ trois quarts. Et mille huit cent cinquante "
                "sur sept mille trois cent vingt-quatre est environ égal "
                "à zéro virgule deux cent cinquante-trois, soit environ un "
                "quart. Le caractère ridée était donc resté présent, "
                "masqué, chez les hybrides F un."
            )
        ) as tracker:
            self.play(Write(verif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_chiffres), FadeOut(resultats), FadeOut(verif))

        # --- Exemple traité : interprétation chromosomique -----------------------
        entete_interp = Text("Interprétation chromosomique", font_size=23, color=YELLOW, weight="BOLD")
        entete_interp.next_to(titre, DOWN, buff=0.5)

        cases = VGroup(
            *[Rectangle(width=1.6, height=0.9, stroke_color=WHITE, stroke_width=2) for _ in range(4)]
        ).arrange(RIGHT, buff=0.3)
        cases.next_to(entete_interp, DOWN, buff=0.6)

        labels = ["LL", "Ll", "lL", "ll"]
        textes = VGroup()
        for case, lab in zip(cases, labels):
            t = MathTex(lab, font_size=30, color=YELLOW)
            t.move_to(case.get_center())
            textes.add(t)

        equiprob = Text("4 combinaisons équiprobables (1/4 chacune)", font_size=20, color=WHITE)
        equiprob.next_to(cases, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici l'interprétation chromosomique de ce résultat. "
                "Chaque gamète F un reçoit, lors de la méiose, soit "
                "l'allèle L, soit l'allèle l, avec la même probabilité, "
                "un demi. La fécondation réunit ensuite au hasard un "
                "gamète mâle et un gamète femelle : d'où quatre "
                "combinaisons possibles, L L, L l, l L et l l, toutes "
                "également probables, chacune avec une chance sur quatre "
                "de se produire."
            )
        ) as tracker:
            self.play(FadeIn(entete_interp))
            self.play(Create(cases))
            self.play(Write(textes))
            self.play(FadeIn(equiprob))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_interp), FadeOut(cases), FadeOut(textes), FadeOut(equiprob))

        # --- À retenir : la deuxième loi de Mendel --------------------------------
        loi2 = theorem_box(
            Text(
                _wrap(
                    "Deuxième loi de Mendel (loi de disjonction des "
                    "allèles, ou « pureté des gamètes ») : les deux "
                    "allèles d'un gène se séparent lors de la formation "
                    "des gamètes, qui ne transportent chacun qu'un seul "
                    "allèle. Au hasard des fécondations, le croisement "
                    "d'hybrides F1 entre eux donne en F2 les proportions "
                    "3/4 de phénotype dominant et 1/4 de phénotype "
                    "récessif.",
                    width=50,
                ),
                font_size=21,
            ),
            box_width=11.5,
        )
        loi2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On énonce ainsi la deuxième loi de Mendel, la loi de "
                "disjonction des allèles, aussi appelée loi de pureté des "
                "gamètes : les deux allèles d'un gène se séparent lors de "
                "la formation des gamètes, qui ne transportent chacun "
                "qu'un seul allèle. Au hasard des fécondations, le "
                "croisement d'hybrides F un entre eux donne, en F deux, "
                "les proportions trois quarts de phénotype dominant et un "
                "quart de phénotype récessif."
            )
        ) as tracker:
            self.play(FadeIn(loi2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(loi2))
