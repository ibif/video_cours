"""
scenes/Maths_Barycentre_03.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 03.

§ L'ensemble des barycentres de deux points distincts A et B est la droite
(AB) : théorème avec démonstration par double inclusion, cas particuliers
A=bar{(A,1),(B,0)} et B=bar{(A,0),(B,1)}.
Source : 1ereC/Maths.pdf, chapitre 4, page 43.
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
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class EnsembleDesBarycentres(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Ensemble des barycentres de A et B")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------
        question = Text(
            _wrap(
                "En faisant varier α et β (avec α+β≠0), le barycentre G "
                "décrit un ensemble de points. Quel est cet ensemble ?",
                width=52,
            ),
            font_size=26,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons vu que pour chaque couple de coefficients alpha "
                "et bêta de somme non nulle, on obtient un barycentre G. En "
                "faisant varier alpha et bêta, G se déplace : quel est "
                "l'ensemble de tous les points ainsi obtenus ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : théorème + démonstration -------------------------
        enonce = MathTex(
            r"A \neq B \ \Rightarrow\ \big\{\, \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\} \ /\ \alpha+\beta\neq 0 \,\big\} = (AB)",
            font_size=24,
        )
        theoreme = theorem_box(enonce)
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le théorème : si A est différent de B, l'ensemble "
                "des barycentres de A et B, quand alpha et bêta parcourent "
                "les réels de somme non nulle, est exactement la droite "
                "A-B, la droite passant par A et B."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        inclusion1_titre = Text("1) Tout barycentre de A et B appartient à (AB)", font_size=24, color=YELLOW)
        inclusion1_titre.next_to(titre, DOWN, buff=0.4)
        inclusion1_calc = MathTex(
            r"\overrightarrow{AG} = \dfrac{\beta}{\alpha+\beta}\,\overrightarrow{AB}"
            r"\ \Rightarrow\ \overrightarrow{AG} \text{ colinéaire à } \overrightarrow{AB}"
            r"\ \Rightarrow\ G \in (AB)",
            font_size=26,
        )
        inclusion1_calc.next_to(inclusion1_titre, DOWN, buff=0.4)
        groupe1 = VGroup(inclusion1_titre, inclusion1_calc)

        with self.voiceover(
            text=(
                "Démontrons cette égalité d'ensembles par double inclusion. "
                "D'abord, tout barycentre G de A et B appartient à la "
                "droite A-B : on sait que le vecteur A-G est égal à bêta "
                "sur alpha plus bêta, fois le vecteur A-B ; ce vecteur "
                "A-G est donc colinéaire au vecteur A-B, ce qui signifie "
                "précisément que G appartient à la droite A-B."
            )
        ) as tracker:
            self.play(FadeIn(inclusion1_titre))
            self.play(Write(inclusion1_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        inclusion2_titre = Text("2) Tout point de (AB) est un barycentre de A et B", font_size=24, color=YELLOW)
        inclusion2_titre.next_to(titre, DOWN, buff=0.4)
        inclusion2_calc = VGroup(
            MathTex(r"M \in (AB) \ \Rightarrow\ \exists\, k\in\mathbb{R}\ /\ \overrightarrow{AM} = k\,\overrightarrow{AB}", font_size=25),
            MathTex(r"\text{Posons } \alpha = 1-k,\ \beta = k \quad (\alpha+\beta = 1 \neq 0)", font_size=25),
            MathTex(r"\dfrac{\beta}{\alpha+\beta}\,\overrightarrow{AB} = k\,\overrightarrow{AB} = \overrightarrow{AM}"
                     r"\ \Rightarrow\ M = \mathrm{bar}\{(A,1-k)\,;\,(B,k)\}", font_size=24),
        ).arrange(DOWN, buff=0.35)
        inclusion2_calc.next_to(inclusion2_titre, DOWN, buff=0.4)
        groupe2 = VGroup(inclusion2_titre, inclusion2_calc)

        with self.voiceover(
            text=(
                "Réciproquement, prenons un point M quelconque de la droite "
                "A-B : il existe un réel k tel que le vecteur A-M soit égal "
                "à k fois le vecteur A-B. Posons alors alpha égale un moins "
                "k, et bêta égale k : leur somme vaut un, donc non nulle. "
                "On retrouve exactement le vecteur A-M avec la formule du "
                "barycentre : M est donc le barycentre de A pondéré par "
                "un moins k, et B pondéré par k. Tout point de la droite "
                "A-B est bien un barycentre de A et B, ce qui achève la "
                "démonstration."
            )
        ) as tracker:
            self.play(FadeIn(inclusion2_titre))
            self.play(Write(inclusion2_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- Exemple traité : balayage de la droite ---------------------------
        a_pt = LEFT * 4
        b_pt = LEFT * 4 + RIGHT * 3
        axe = Line(LEFT * 5.5, RIGHT * 4, color=WHITE)

        pts = VGroup()
        for k, nom, coul in [
            (-0.5, "k=-0.5", "#B42E41"),
            (0.0, "A", YELLOW),
            (0.5, "milieu (k=0.5)", "#288073"),
            (1.0, "B", YELLOW),
            (1.5, "k=1.5", "#B42E41"),
        ]:
            pt = a_pt + k * (b_pt - a_pt)
            pts.add(_dot_label(pt, nom if nom in ("A", "B") else "", dot_color=coul))

        legende = Text(
            "k < 0  |  0 ≤ k ≤ 1 (dans [AB])  |  k > 1",
            font_size=20,
        )
        figure = VGroup(axe, pts)
        figure.scale(0.85).move_to(UP * 0.3 + DOWN * 1.2)
        legende.next_to(figure, DOWN, buff=0.5)

        cas_particuliers = MathTex(
            r"k=0 \Rightarrow M=A=\mathrm{bar}\{(A,1)\,;\,(B,0)\}"
            r"\quad k=1 \Rightarrow M=B=\mathrm{bar}\{(A,0)\,;\,(B,1)\}",
            font_size=22,
        )
        cas_particuliers.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Concrètement, quand k parcourt les réels, M balaie toute "
                "la droite A-B : pour k entre zéro et un, M est dans le "
                "segment A-B ; pour k négatif ou k supérieur à un, M est à "
                "l'extérieur du segment, mais reste sur la droite. Deux cas "
                "particuliers à connaître : pour k égal zéro, M est "
                "confondu avec A, c'est-à-dire A égale bar de A-un et "
                "B-zéro ; pour k égal un, M est confondu avec B, c'est-à-"
                "dire B égale bar de A-zéro et B-un."
            )
        ) as tracker:
            self.play(FadeIn(cas_particuliers))
            self.play(Create(figure), FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_particuliers), FadeOut(figure), FadeOut(legende))

        # --- À retenir ---------------------------------------------------------
        retenir = theorem_box(
            Text(
                "L'ensemble des barycentres de deux points distincts A et B est la droite (AB) tout entière.",
                font_size=24,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : l'ensemble des barycentres de deux points "
                "distincts A et B est exactement la droite A-B, sans "
                "exception."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Un barycentre n'est pas forcément dans le segment "
                    "[AB] : tout point de la droite (AB), même à "
                    "l'extérieur du segment, est un barycentre de A et B "
                    "pour des coefficients bien choisis (éventuellement "
                    "négatifs).",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas croire qu'un barycentre est toujours "
                "situé entre les deux points : tout point de la droite "
                "A-B, même à l'extérieur du segment A-B, est un barycentre "
                "de A et B, pour des coefficients bien choisis, "
                "éventuellement négatifs."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
