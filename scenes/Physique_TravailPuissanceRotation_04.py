"""
scenes/Physique_TravailPuissanceRotation_04.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 04.

§ Moment d'un couple de forces : définition (directions parallèles, sens
contraires, droites d'action différentes, même intensité, résultante
nulle), exemples (volant, tournevis), théorème ℳ_C = F×d avec démonstration
(3 cas : axe entre les deux droites, axe à l'extérieur, droite d'action
passant par l'axe). Exemple résolu 3 : robinet de vanne à Abidjan.
Source : 1ereC/Physique.pdf, chapitre 2, pages 13-23.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class MomentCoupleDeForces(NotionScene):
    def construct(self):
        titre = scene_title("Moment d'un couple de forces")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : exemples du quotidien -------------------------------------
        enonce = Text(
            _wrap(
                "Pour tourner un volant, on tire d'une main et on pousse de "
                "l'autre : deux forces opposées, mais qui font tourner. "
                "Comment décrire leur effet ?",
                width=54,
            ),
            font_size=23,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour faire tourner un volant de voiture, ou pour serrer "
                "une vis avec un tournevis, on applique souvent deux "
                "forces opposées, avec les deux mains, ou avec deux "
                "doigts. Comment décrire l'effet de rotation de ce type "
                "particulier de système de forces ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Définition du couple -------------------------------------------------
        defn = definition_box(
            VGroup(
                Text("Couple de forces", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Deux forces F⃗ et −F⃗ : directions parallèles, sens "
                        "contraires, même intensité, droites d'action "
                        "DIFFÉRENTES (distantes de d) ⟹ résultante nulle."
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        defn.next_to(titre, DOWN, buff=0.4)

        centre = LEFT * 3.2 + DOWN * 1.7
        volant = Circle(radius=1.1, color=WHITE, stroke_width=3).move_to(centre)
        f1 = Vector(UP * 1.0, color="#DE7C1F").shift(centre + LEFT * 1.1)
        f2 = Vector(DOWN * 1.0, color="#B42E41").shift(centre + RIGHT * 1.1)
        f1_lbl = MathTex(r"\vec{F}", font_size=24, color="#DE7C1F").next_to(f1, LEFT, buff=0.1)
        f2_lbl = MathTex(r"-\vec{F}", font_size=24, color="#B42E41").next_to(f2, RIGHT, buff=0.1)
        schema = VGroup(volant, f1, f2, f1_lbl, f2_lbl, Dot(centre, color=YELLOW, radius=0.05))
        schema.scale(0.85)

        with self.voiceover(
            text=(
                "Un couple de forces, c'est exactement ce type de "
                "système : deux forces de directions parallèles, de sens "
                "contraires, de même intensité, mais dont les droites "
                "d'action sont différentes, séparées d'une distance d. "
                "Leur résultante vectorielle est nulle — le solide ne se "
                "déplace pas — mais leur effet de rotation, lui, est bien "
                "réel : c'est exactement ce qui se passe sur un volant."
            )
        ) as tracker:
            self.play(FadeIn(defn))
            self.play(Create(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(defn), FadeOut(schema))

        # --- Théorème + démonstration (3 cas) ------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Moment d'un couple", font_size=22, weight="BOLD"),
                MathTex(r"\mathcal{M}_C = F \times d \quad \text{(indépendant de la position de l'axe)}", font_size=25),
            ).arrange(DOWN, buff=0.2)
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résultat fondamental : le moment d'un couple vaut F fois "
                "d, où d est la distance entre les deux droites d'action, "
                "et ce résultat est totalement indépendant de la position "
                "de l'axe choisi. Démontrons-le en examinant trois "
                "positions possibles de l'axe."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        demo = VGroup(
            MathTex(
                r"\text{Axe entre les deux droites : } \mathcal{M}_C = F(d_1+d_2) = F\,d",
                font_size=22,
            ),
            MathTex(
                r"\text{Axe à l'extérieur : } \mathcal{M}_C = F\,d_1 - F\,d_2 = F(d_1-d_2) = F\,d",
                font_size=22,
            ),
            MathTex(
                r"\text{Droite d'action passant par l'axe : } \mathcal{M} = 0 \ \text{mais l'autre force compense : } \mathcal{M}_C = F\,d",
                font_size=20,
            ),
        ).arrange(DOWN, buff=0.32)
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier cas : l'axe est situé entre les deux droites "
                "d'action, à des distances d-un et d-deux. Les deux "
                "moments s'ajoutent, car les deux forces tendent à faire "
                "tourner dans le même sens : on obtient F fois d-un plus "
                "d-deux, soit F fois d. Deuxième cas : l'axe est à "
                "l'extérieur des deux droites. Les moments se "
                "soustraient, mais comme F et d-un sont plus grands, il "
                "reste F fois d-un moins d-deux, soit encore F fois d. "
                "Troisième cas : la droite d'action de l'une des forces "
                "passe exactement par l'axe. Son moment est nul, mais "
                "l'autre force, seule, a alors pour bras de levier "
                "exactement d : le résultat F fois d est donc toujours "
                "retrouvé, quelle que soit la position de l'axe."
            )
        ) as tracker:
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple résolu 3 : robinet de vanne à Abidjan ------------------------
        exemple = example_box(
            VGroup(
                Text("Exemple 3 — robinet de vanne à Abidjan :", font_size=21),
                Text("Deux mains exercent chacune F = 12 N, diamètre du volant D = 40 cm.", font_size=20),
                MathTex(r"\mathcal{M}_C = F \times D = 12 \times 0{,}40 = 4{,}8\ \text{N} \cdot \text{m}", font_size=26),
            ).arrange(DOWN, buff=0.28),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : pour ouvrir un robinet de vanne à Abidjan, un "
                "technicien exerce avec chaque main une force de douze "
                "newtons, sur un volant de quarante centimètres de "
                "diamètre. Les deux droites d'action sont donc séparées "
                "exactement du diamètre D. Le moment du couple vaut F fois "
                "D, soit douze fois zéro virgule quarante, c'est-à-dire "
                "quatre virgule huit newton-mètre."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Un couple : deux forces parallèles, opposées, même "
                    "intensité, droites d'action distinctes. Son moment "
                    "ℳ_C = F×d ne dépend pas de la position de l'axe.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : un couple est formé de deux forces "
                "parallèles, opposées, de même intensité, appliquées sur "
                "deux droites d'action distinctes. Son moment, ℳ indice C "
                "égale F fois d, ne dépend jamais de la position de "
                "l'axe."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : pour un couple, inutile de chercher la "
                    "position de l'axe — ℳ_C = F×d où d est la distance "
                    "entre les deux droites d'action (souvent le diamètre "
                    "pour un volant ou un pédalier)."
                ),
                font_size=21,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : face à un couple de forces, inutile de "
                "chercher la position exacte de l'axe pour calculer son "
                "moment. La formule ℳ indice C égale F fois d suffit, où "
                "d est la distance entre les deux droites d'action — "
                "souvent tout simplement le diamètre, pour un volant ou "
                "un pédalier."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
