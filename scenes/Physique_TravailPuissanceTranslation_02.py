"""
scenes/Physique_TravailPuissanceTranslation_02.py — Chapitre 1 « Travail et
puissance dans le cas d'un mouvement de translation » (1ereC, Physique),
scène 02.

§ Signe du travail selon l'angle α (tableau cos α), travail moteur /
résistant / nul, conséquence sur le poids et la réaction normale sur un
support horizontal, théorème d'indépendance du chemin suivi pour une force
constante (décomposition en déplacements élémentaires). Exemple résolu 1 :
ouvrier tirant une caisse à Bouaké (F=20 N à 60°, AB=10 m).
Source : 1ereC/Physique.pdf, chapitre 1, pages 4-12.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    DashedLine,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import (
    corrige_box,
    definition_box,
    essentiel_box,
    exercise_box,
    property_box,
    scene_title,
    theorem_box,
    warning_box,
)


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


RESISTANT_COLOR = "#B42E41"


class TravailMoteurResistantNul(NotionScene):
    def construct(self):
        titre = scene_title("Travail moteur, résistant, nul")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le signe dépend de l'angle -----------------------------------
        rappel = Text(
            _wrap(
                "Le travail W = F×AB×cos(α) change de signe selon l'angle "
                "α : il traduit si la force aide, freine, ou n'influence "
                "pas du tout le mouvement.",
                width=56,
            ),
            font_size=23,
        )
        rappel.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le travail d'une force constante, W égale F fois A-B fois "
                "cosinus de alpha, change de signe selon l'angle alpha entre "
                "la force et le déplacement. Ce signe traduit si la force "
                "aide le mouvement, le freine, ou reste sans effet sur lui."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel))

        # --- Raisonnement : tableau des signes --------------------------------------
        row1 = VGroup(
            MathTex(r"0 \le \alpha < 90°", font_size=24),
            Text("travail MOTEUR", font_size=22, color=GREEN, weight="BOLD"),
            MathTex(r"\cos(\alpha) > 0", font_size=24),
        ).arrange(RIGHT, buff=0.6)
        row2 = VGroup(
            MathTex(r"\alpha = 90°", font_size=24),
            Text("travail NUL", font_size=22, color=WHITE, weight="BOLD"),
            MathTex(r"\cos(\alpha) = 0", font_size=24),
        ).arrange(RIGHT, buff=0.6)
        row3 = VGroup(
            MathTex(r"90° < \alpha \le 180°", font_size=24),
            Text("travail RÉSISTANT", font_size=22, color=RESISTANT_COLOR, weight="BOLD"),
            MathTex(r"\cos(\alpha) < 0", font_size=24),
        ).arrange(RIGHT, buff=0.6)
        tableau = VGroup(row1, row2, row3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        tableau_box = property_box(tableau, box_width=11.5)
        tableau_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Si l'angle alpha est compris entre zéro et quatre-vingt-dix "
                "degrés, le cosinus est positif : le travail est moteur, il "
                "favorise le mouvement. Si alpha vaut exactement quatre-"
                "vingt-dix degrés, le cosinus est nul : le travail est nul, "
                "la force n'a aucun effet sur la vitesse. Et si alpha est "
                "compris entre quatre-vingt-dix et cent-quatre-vingts "
                "degrés, le cosinus est négatif : le travail est résistant, "
                "il s'oppose au mouvement."
            )
        ) as tracker:
            self.play(FadeIn(tableau_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_box))

        consequence = definition_box(
            VGroup(
                Text("Conséquence importante", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "Sur un support horizontal, le poids et la réaction "
                        "normale sont perpendiculaires au déplacement "
                        "(α = 90°) : leur travail est TOUJOURS NUL.",
                        width=48,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        consequence.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Conséquence importante à retenir : lorsqu'un objet se "
                "déplace sur un support horizontal, le poids et la réaction "
                "normale du support sont tous les deux perpendiculaires au "
                "déplacement. Leur angle alpha vaut donc quatre-vingt-dix "
                "degrés, et leur travail est toujours nul, quelle que soit "
                "la distance parcourue."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- Théorème d'indépendance du chemin ---------------------------------------
        point_a = LEFT * 4 + DOWN * 0.8
        point_b = RIGHT * 2 + UP * 0.3
        p1 = LEFT * 2 + UP * 1.2
        p2 = ORIGIN + DOWN * 1.2
        chemin = VGroup(
            Line(point_a, p1, color=YELLOW),
            Line(p1, p2, color=YELLOW),
            Line(p2, point_b, color=YELLOW),
        )
        trajet_direct = DashedLine(point_a, point_b, color=WHITE)
        label_a = MathTex("A", font_size=26).next_to(point_a, LEFT, buff=0.15)
        label_b = MathTex("B", font_size=26).next_to(point_b, RIGHT, buff=0.15)
        figure_chemin = VGroup(chemin, trajet_direct, label_a, label_b)
        figure_chemin.scale(0.85).move_to(ORIGIN).shift(DOWN * 0.2)

        theoreme = theorem_box(
            VGroup(
                Text(
                    "Pour une force constante F⃗, le travail ne dépend pas",
                    font_size=22,
                ),
                Text("du chemin suivi, seulement des positions A et B :", font_size=22),
                MathTex(
                    r"W_{\text{chemin}}(\vec{F}) = W_{AB}(\vec{F}) = \vec{F}\cdot\overrightarrow{AB}",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.2),
            box_width=11.0,
        )
        theoreme.to_edge(UP, buff=1.0)

        with self.voiceover(
            text=(
                "Un résultat essentiel : pour une force constante, le "
                "travail entre deux points A et B ne dépend pas du chemin "
                "suivi pour aller de l'un à l'autre. On peut le voir en "
                "découpant n'importe quel trajet en une succession de "
                "petits déplacements élémentaires : la somme de tous ces "
                "petits travaux se recompose exactement en F vecteur, fois "
                "le vecteur A-B direct, quel que soit le détour emprunté."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.play(FadeIn(figure_chemin))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme), FadeOut(figure_chemin))

        # --- Exemple traité : ouvrier à Bouaké ---------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "À Bouaké, un ouvrier tire une caisse posée au sol avec "
                    "une force F = 20 N faisant un angle de 60° avec le sol "
                    "horizontal. La caisse avance de AB = 10 m. Calculer le "
                    "travail de la force F, du poids, et de la réaction "
                    "normale du sol.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. À Bouaké, un ouvrier tire une caisse posée "
                "au sol à l'aide d'une corde qui fait un angle de soixante "
                "degrés avec le sol horizontal, avec une force de vingt "
                "newtons. La caisse avance de dix mètres sur le sol. "
                "Calculons le travail de la force F, celui du poids, et "
                "celui de la réaction normale du sol."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc = corrige_box(
            VGroup(
                MathTex(r"W_{AB}(\vec{F}) = 20 \times 10 \times \cos(60°) = 100\ J \ (\text{moteur})", font_size=25),
                MathTex(r"W_{AB}(\vec{P}) = 0 \ \text{(poids} \perp \text{déplacement)}", font_size=25),
                MathTex(r"W_{AB}(\vec{R}) = 0 \ \text{(réaction} \perp \text{déplacement)}", font_size=25),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )
        calc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour la force F, le travail vaut vingt fois dix fois "
                "cosinus de soixante degrés, soit cent joules : c'est un "
                "travail moteur, positif. Le poids et la réaction normale du "
                "sol, eux, sont perpendiculaires au déplacement horizontal : "
                "leur travail est nul dans les deux cas."
            )
        ) as tracker:
            self.play(FadeIn(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Moteur (0≤α<90°, W>0), nul (α=90°, W=0), résistant "
                    "(90°<α≤180°, W<0). Le travail d'une force constante ne "
                    "dépend que des positions de départ et d'arrivée, jamais "
                    "du chemin parcouru.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : travail moteur quand l'angle est aigu, nul à "
                "quatre-vingt-dix degrés, résistant quand l'angle est obtus. "
                "Et surtout, pour une force constante, le travail ne dépend "
                "jamais du chemin parcouru, seulement des positions de "
                "départ et d'arrivée."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "« Travail moteur » ne signifie pas « force dans le sens "
                    "du mouvement apparent » : c'est le SIGNE du travail qui "
                    "compte, calculé avec l'angle réel α entre F⃗ et AB⃗, "
                    "jamais deviné à l'œil.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à éviter : ne jamais deviner à l'œil si un travail "
                "est moteur ou résistant. C'est le signe du calcul, avec "
                "l'angle réel alpha entre la force et le déplacement, qui "
                "tranche, jamais une impression visuelle sur le sens "
                "apparent du mouvement."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
