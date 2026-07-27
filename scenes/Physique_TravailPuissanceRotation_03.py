"""
scenes/Physique_TravailPuissanceRotation_03.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 03.

§ Signe du moment (moment algébrique), sens positif conventionnel, règle
du tire-bouchon. Exemple résolu 2 : tige OA = 50 cm, F = 10 N, calcul du
moment pour α = 90°, 60°, 30°.
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
    Arc,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class SigneDuMomentTireBouchon(NotionScene):
    def construct(self):
        titre = scene_title("Signe du moment — règle du tire-bouchon")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Une même force peut faire tourner un solide dans un sens "
                "ou dans l'autre : comment traduire cela par un signe ?",
                width=54,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une force peut faire tourner un solide dans un sens, ou "
                "dans le sens opposé. Le moment d'une force n'est donc pas "
                "seulement une intensité : c'est une grandeur algébrique, "
                "affectée d'un signe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : convention de signe et tire-bouchon --------------
        defn = definition_box(
            VGroup(
                Text("Moment algébrique", font_size=23, weight="BOLD"),
                Text("On choisit d'abord un sens positif de rotation (arbitraire).", font_size=21),
                MathTex(r"\mathcal{M}_\Delta(\vec{F}) > 0 \ \text{si } \vec{F} \text{ tend à faire tourner dans le sens positif}", font_size=22),
                MathTex(r"\mathcal{M}_\Delta(\vec{F}) < 0 \ \text{sinon}", font_size=22),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        defn.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On commence toujours par choisir, arbitrairement, un sens "
                "positif de rotation. Le moment de la force est alors "
                "compté positivement si la force tend à faire tourner le "
                "solide dans ce sens positif, et négativement dans le cas "
                "contraire."
            )
        ) as tracker:
            self.play(FadeIn(defn))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(defn))

        # --- Règle du tire-bouchon (schéma) ------------------------------------
        centre = LEFT * 3.0 + DOWN * 0.3
        arc_sens = Arc(radius=1.1, start_angle=0.3, angle=4.5, arc_center=centre, color="#288073", stroke_width=5)
        fleche_sens = Vector(RIGHT * 0.35, color="#288073").move_to(arc_sens.point_from_proportion(0.98))
        axe_vertical = Vector(UP * 1.6, color=YELLOW).shift(centre)
        axe_label = MathTex(r"\Delta", font_size=28, color=YELLOW).next_to(axe_vertical, UP, buff=0.1)
        tire_bouchon = VGroup(arc_sens, fleche_sens, axe_vertical, axe_label, Dot(centre, color=WHITE, radius=0.05))
        tire_bouchon.scale(0.85)

        regle = VGroup(
            Text("Règle du tire-bouchon :", font_size=22, weight="BOLD"),
            Text("le tire-bouchon tourné dans le sens de rotation", font_size=20),
            Text("avance dans le sens du vecteur moment porté par l'axe.", font_size=20),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        regle.next_to(tire_bouchon, RIGHT, buff=0.7)

        with self.voiceover(
            text=(
                "La règle du tire-bouchon permet de visualiser ce sens : "
                "si l'on tourne un tire-bouchon dans le sens de la "
                "rotation observée, il avance le long de l'axe dans le "
                "sens du vecteur moment. C'est cette règle qui fixe, en "
                "trois dimensions, le lien entre le sens de rotation et le "
                "signe du moment."
            )
        ) as tracker:
            self.play(Create(tire_bouchon))
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tire_bouchon), FadeOut(regle))

        # --- Exemple résolu 2 : tige OA, calcul pour 3 angles -----------------
        exemple = example_box(
            VGroup(
                Text("Exemple 2 — tige OA = 50 cm, force F = 10 N appliquée en A :", font_size=21),
                MathTex(r"\mathcal{M}_\Delta(\vec{F}) = F \times OA \times \sin(\alpha)", font_size=25),
                MathTex(
                    r"\alpha = 90^\circ \Rightarrow \mathcal{M} = 10\times0{,}5\times1 = 5{,}0\ \text{N}\cdot\text{m}",
                    font_size=23,
                ),
                MathTex(
                    r"\alpha = 60^\circ \Rightarrow \mathcal{M} = 10\times0{,}5\times\sin(60^\circ) \approx 4{,}33\ \text{N}\cdot\text{m}",
                    font_size=23,
                ),
                MathTex(
                    r"\alpha = 30^\circ \Rightarrow \mathcal{M} = 10\times0{,}5\times\sin(30^\circ) = 2{,}5\ \text{N}\cdot\text{m}",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : une tige O A de cinquante centimètres, soumise "
                "en A à une force de dix newtons. Pour un angle alpha de "
                "quatre-vingt-dix degrés, le moment vaut cinq newton-"
                "mètre : c'est le maximum, la force est perpendiculaire à "
                "la tige. Pour soixante degrés, il vaut environ quatre "
                "virgule trente-trois newton-mètre. Et pour trente degrés, "
                "seulement deux virgule cinq newton-mètre. On voit bien "
                "que le moment est maximal quand la force est "
                "perpendiculaire à la tige, et diminue quand l'angle "
                "s'éloigne de quatre-vingt-dix degrés."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Le moment est une grandeur algébrique : on fixe un "
                    "sens positif AVANT de calculer, puis on affecte + ou "
                    "− selon le sens réel de rotation induit par la force. "
                    "La règle du tire-bouchon relie sens de rotation et "
                    "signe du moment.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : le moment est une grandeur algébrique. On "
                "fixe toujours un sens positif avant de calculer, puis on "
                "affecte le signe plus ou moins selon le sens réel de "
                "rotation induit par la force, la règle du tire-bouchon "
                "reliant sens de rotation et signe du moment."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : oublier de fixer le sens positif AVANT "
                    "d'affecter les signes conduit à des erreurs de signe "
                    "en cascade dans le théorème des moments (scène 7)."
                ),
                font_size=22,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : oublier de fixer le sens positif avant "
                "d'affecter les signes des différents moments. Cette étape "
                "préalable est indispensable, sinon toutes les erreurs de "
                "signe s'accumulent, en particulier plus tard, dans "
                "l'application du théorème des moments à l'équilibre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
