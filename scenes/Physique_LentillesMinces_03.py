"""
scenes/Physique_LentillesMinces_03.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 03.

§ Distance focale f' = OF' (mètres, algébrique) et vergence C = 1/f'
(dioptrie δ). Convergente : f' > 0, C > 0. Divergente : f' < 0, C < 0.
Exemple résolu : L1 (f'1 = +25 cm → C1 = +4 δ) et L2 (C2 = -2,5 δ →
f'2 = -40 cm, divergente).
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 2).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _lens_symbol(convergente: bool = True, height: float = 2.0, color=WHITE) -> VGroup:
    half = height / 2
    if convergente:
        haut = Arrow(ORIGIN, UP * half, buff=0, stroke_width=4, color=color)
        bas = Arrow(ORIGIN, DOWN * half, buff=0, stroke_width=4, color=color)
        return VGroup(haut, bas)
    inner = half * 0.5
    axe = Line(UP * inner, DOWN * inner, color=color, stroke_width=4)
    haut = Arrow(UP * half, UP * inner, buff=0, stroke_width=4, color=color)
    bas = Arrow(DOWN * half, DOWN * inner, buff=0, stroke_width=4, color=color)
    return VGroup(axe, haut, bas)


class DistanceFocaleVergence(NotionScene):
    def construct(self):
        titre = scene_title("Distance focale et vergence")
        titre.scale(0.46)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définitions --------------------------------------------------
        definitions = definition_box(
            VGroup(
                Text("Distance focale", font_size=23, weight="BOLD"),
                MathTex(r"f' = \overline{OF'}", font_size=28),
                Text("mesurée en mètres, c'est une grandeur algébrique.", font_size=20),
                Text("Vergence", font_size=23, weight="BOLD"),
                MathTex(r"C = \dfrac{1}{f'}", font_size=28),
                Text("mesurée en dioptries (symbole δ).", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=10.6,
        )
        definitions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La distance focale, notée f prime, est égale à la mesure "
                "algébrique O F prime. Elle s'exprime en mètres. La "
                "vergence, notée C, est l'inverse de la distance focale : "
                "C égale un sur f prime. Elle s'exprime en dioptries, de "
                "symbole delta."
            )
        ) as tracker:
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Raisonnement : signe selon le type, effet sur la convergence --------
        conv = VGroup(
            _lens_symbol(True, height=1.8),
            Text("convergente", font_size=19),
            MathTex(r"f' > 0 \quad C > 0", font_size=24, color=YELLOW),
        ).arrange(DOWN, buff=0.25)

        div = VGroup(
            _lens_symbol(False, height=1.8),
            Text("divergente", font_size=19),
            MathTex(r"f' < 0 \quad C < 0", font_size=24, color=YELLOW),
        ).arrange(DOWN, buff=0.25)

        deux = VGroup(conv, div).arrange(RIGHT, buff=2.0)
        deux.next_to(titre, DOWN, buff=0.6)

        note = Text(
            "Plus f' est petit (en valeur absolue), plus C est grand :",
            font_size=19,
        )
        note2 = Text("la lentille dévie fortement la lumière.", font_size=19)
        note_grp = VGroup(note, note2).arrange(DOWN, buff=0.1)
        note_grp.next_to(deux, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour une lentille convergente, f prime est positive, "
                "donc C est positive. Pour une lentille divergente, f "
                "prime est négative, donc C est négative également. Et "
                "plus f prime est petite en valeur absolue, plus la "
                "vergence C est grande : la lentille dévie alors fortement "
                "la lumière, c'est une lentille très puissante."
            )
        ) as tracker:
            self.play(Create(conv), Create(div))
            self.play(FadeIn(note_grp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(deux), FadeOut(note_grp))

        # --- Exemple résolu -------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Lentille L1 : f'1 = +25 cm = +0,25 m", font_size=20),
                MathTex(r"C_1 = \dfrac{1}{0{,}25} = +4\ \delta", font_size=25, color=YELLOW),
                Text("Lentille L2 : C2 = -2,5 δ", font_size=20),
                MathTex(r"f'_2 = \dfrac{1}{-2{,}5} = -0{,}40\ \text{m} = -40\ \text{cm}", font_size=25, color=YELLOW),
                Text("(L2 est donc une lentille divergente)", font_size=18),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu. La lentille L1 a une distance focale f "
                "prime 1 égale à plus 25 centimètres, soit plus 0,25 "
                "mètre. Sa vergence C1 vaut donc 1 divisé par 0,25, soit "
                "plus 4 dioptries. La lentille L2 a une vergence C2 égale "
                "à moins 2,5 dioptries. Sa distance focale f prime 2 vaut "
                "1 divisé par moins 2,5, soit moins 0,40 mètre, c'est-à-"
                "dire moins 40 centimètres : L2 est donc une lentille "
                "divergente."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"f' = \overline{OF'} \ (\text{m}) \qquad C = \dfrac{1}{f'} \ (\delta)", font_size=26),
                Text("Convergente : f' > 0, C > 0.   Divergente : f' < 0, C < 0.", font_size=19),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : f prime égale O F prime, en "
                "mètres, et C égale un sur f prime, en dioptries. "
                "Convergente : f prime et C positives. Divergente : f "
                "prime et C négatives."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• La vergence se calcule TOUJOURS avec f' exprimée", font_size=19),
                Text("   en MÈTRES, jamais en centimètres.", font_size=19),
                Text("   Exemple : f' = 40 cm donne C = 1/0,40 = 2,5 δ,", font_size=19),
                Text("   PAS C = 1/40 = 0,025 δ !", font_size=19, color=YELLOW),
                Text("• Ne jamais oublier le signe : une divergente garde", font_size=19),
                Text("   f' < 0 et C < 0 tout au long du calcul.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège très fréquent : la vergence se calcule toujours "
                "avec f prime exprimée en mètres, jamais en centimètres. "
                "Par exemple, pour f prime égale 40 centimètres, C vaut 1 "
                "divisé par 0,40, soit 2,5 dioptries, et surtout pas 1 "
                "divisé par 40. Et il ne faut jamais oublier le signe : "
                "une lentille divergente garde f prime négative et C "
                "négative tout au long du calcul."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
