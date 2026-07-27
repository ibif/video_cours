"""
scenes/Physique_TravailPuissanceRotation_01.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 01.

§ Rappels sur le mouvement de rotation : abscisse angulaire θ(t), vitesse
angulaire ω = dθ/dt, rotation uniforme ω = Δθ/Δt = 2π/T = 2πf, conversion
tr/min → rad/s, vitesse linéaire v = Rω. Exemple résolu 1 : grande aiguille
d'une horloge à Yamoussoukro.
Source : 1ereC/Physique.pdf, chapitre 2, pages 13-23.
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
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Rotate,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class RappelsMouvementRotation(NotionScene):
    def construct(self):
        titre = scene_title("Rappels sur le mouvement de rotation")
        titre.scale(0.52)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Un solide en rotation autour d'un axe fixe : comment "
                "repérer sa position, et à quelle vitesse tourne-t-il ?",
                width=56,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant de parler de travail ou de puissance, rappelons "
                "comment on décrit un mouvement de rotation autour d'un "
                "axe fixe : comment repérer la position du solide, et "
                "comment définir sa vitesse de rotation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : abscisse angulaire et vitesse angulaire ----------
        centre = LEFT * 3.3 + DOWN * 0.3
        cercle = Circle(radius=1.4, color=WHITE, stroke_width=2).move_to(centre)
        axe = Dot(centre, color=YELLOW, radius=0.06)
        aiguille = Vector(RIGHT * 1.4, color="#DE7C1F").shift(centre)
        theta_label = MathTex(r"\theta(t)", font_size=28, color=YELLOW)
        theta_label.next_to(cercle, UP, buff=0.15)
        schema = VGroup(cercle, axe, aiguille)

        defn = definition_box(
            VGroup(
                Text("Abscisse angulaire et vitesse angulaire", font_size=23, weight="BOLD"),
                MathTex(r"\theta(t) \ \text{en radians (rad)} \qquad 2\pi\ \text{rad} = 1\ \text{tour}", font_size=26),
                MathTex(r"\omega = \dfrac{d\theta}{dt} \ \text{ en rad/s (rotation uniforme : } \omega = \dfrac{\Delta\theta}{\Delta t}\text{)}", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=6.6,
        )
        defn.next_to(titre, DOWN, buff=0.4).shift(RIGHT * 3.0)

        with self.voiceover(
            text=(
                "La position angulaire du solide est repérée par "
                "l'abscisse angulaire thêta de t, exprimée en radians : "
                "un tour complet correspond à deux pi radians. La vitesse "
                "angulaire oméga est la dérivée de thêta par rapport au "
                "temps, exprimée en radians par seconde. Pour une rotation "
                "uniforme, elle vaut simplement delta thêta sur delta t."
            )
        ) as tracker:
            self.play(Create(schema), Write(theta_label))
            self.play(FadeIn(defn))
            self.play(Rotate(aiguille, angle=1.2, about_point=centre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(theta_label), FadeOut(defn))

        # --- Relations période / fréquence / vitesse linéaire -----------------
        relations = definition_box(
            VGroup(
                Text("Rotation uniforme : période, fréquence, vitesse linéaire", font_size=22, weight="BOLD"),
                MathTex(r"\omega = \dfrac{2\pi}{T} = 2\pi f \qquad \omega(\text{rad/s}) = \dfrac{2\pi\,n}{60}\ (n\ \text{en tr/min})", font_size=25),
                MathTex(r"v = R\,\omega \quad \text{(vitesse linéaire d'un point à la distance } R \text{ de l'axe)}", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        relations.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Pour une rotation uniforme, oméga vaut aussi deux pi sur "
                "la période T, ou deux pi fois la fréquence f. Si la "
                "vitesse de rotation n est donnée en tours par minute, on "
                "convertit avec oméga égale deux pi n sur soixante. Enfin, "
                "un point situé à la distance R de l'axe se déplace à la "
                "vitesse linéaire v égale R fois oméga."
            )
        ) as tracker:
            self.play(FadeIn(relations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(relations))

        # --- Exemple résolu 1 : aiguille d'horloge à Yamoussoukro -------------
        exemple = example_box(
            VGroup(
                Text("Exemple 1 — grande aiguille d'une horloge à Yamoussoukro :", font_size=21),
                Text("Longueur ℓ = 1,2 m, période T = 3600 s (1 heure).", font_size=20),
                MathTex(r"\omega = \dfrac{2\pi}{T} = \dfrac{2\pi}{3600} \approx 1{,}745\times10^{-3}\ \text{rad/s}", font_size=24),
                MathTex(r"v = \ell\,\omega \approx 1{,}2 \times 1{,}745\times10^{-3} \approx 2{,}1\times10^{-3}\ \text{m/s}", font_size=24),
            ).arrange(DOWN, buff=0.28),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : la grande aiguille d'une horloge à Yamoussoukro "
                "mesure un mètre vingt, et fait un tour complet en une "
                "heure, soit trois mille six cents secondes. Sa vitesse "
                "angulaire vaut deux pi sur trois mille six cents, environ "
                "un virgule sept cent quarante-cinq fois dix puissance "
                "moins trois radians par seconde. La vitesse linéaire de "
                "la pointe de l'aiguille est alors v égale ℓ fois oméga, "
                "soit environ deux virgule un fois dix puissance moins "
                "trois mètres par seconde — extrêmement lent."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "θ(t) en radians repère la rotation ; ω = dθ/dt (rad/s) "
                    "est la vitesse angulaire. Rotation uniforme : "
                    "ω = 2π/T = 2πf. Un point à la distance R de l'axe a "
                    "pour vitesse linéaire v = Rω.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : thêta de t, en radians, repère la rotation ; "
                "oméga, en radians par seconde, est la vitesse angulaire, "
                "avec oméga égale deux pi sur T en rotation uniforme. Tout "
                "point situé à la distance R de l'axe a pour vitesse "
                "linéaire v égale R fois oméga."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : ne jamais mélanger degrés et radians dans les "
                    "formules. Un tour = 2π rad = 360°, pas 2π degrés. "
                    "Convertir n (tr/min) en ω (rad/s) avant tout calcul."
                ),
                font_size=22,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : ne jamais mélanger degrés et radians "
                "dans une formule de physique. Un tour complet vaut deux "
                "pi radians, soit trois cent soixante degrés — ce n'est "
                "pas deux pi degrés. Et si la vitesse de rotation est "
                "donnée en tours par minute, il faut toujours la convertir "
                "en radians par seconde avant tout calcul de travail ou de "
                "puissance."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
