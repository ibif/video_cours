"""
scenes/Physique_TravailPuissanceRotation_06.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 06.

§ Puissance d'une force en rotation : P = δW/δt = ℳΔ(F⃗)×ω (démonstration
via δθ/δt = ω), puissance d'un couple P_C = ℳ_C×ω, puissance moyenne
P_m = W/Δt si moment non constant, lien avec la translation
P = ℳΔ(F⃗)×ω = F×R×ω = F×v (retrouve P = F⃗·v⃗). Exemple résolu 5 :
bétonnière.
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
    Rotate,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class PuissanceForceRotation(NotionScene):
    def construct(self):
        titre = scene_title("Puissance d'une force en rotation")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Un moteur fait tourner une bétonnière : à quel rythme "
                "fournit-il de l'énergie ? C'est la puissance.",
                width=54,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un moteur fait tourner le tambour d'une bétonnière. Le "
                "travail qu'il fournit nous renseigne sur l'énergie "
                "totale dépensée, mais pas sur la rapidité de cette "
                "dépense : c'est le rôle de la puissance."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : démonstration P = ℳω ---------------------------------
        demo = VGroup(
            MathTex(r"P = \dfrac{\delta W}{\delta t}", font_size=27),
            MathTex(r"\delta W = \mathcal{M}_\Delta(\vec{F})\,\delta\theta \ \Rightarrow\ P = \mathcal{M}_\Delta(\vec{F})\,\dfrac{\delta\theta}{\delta t}", font_size=25),
            MathTex(r"\dfrac{\delta\theta}{\delta t} = \omega \ \Rightarrow\ P = \mathcal{M}_\Delta(\vec{F}) \times \omega", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Par définition, la puissance instantanée est P égale "
                "delta W sur delta t. Comme le travail élémentaire vaut "
                "ℳ delta de F fois delta thêta, on obtient P égale ℳ "
                "delta de F fois delta thêta sur delta t. Or delta thêta "
                "sur delta t n'est autre que la vitesse angulaire oméga. "
                "On aboutit donc à P égale ℳ delta de F fois oméga."
            )
        ) as tracker:
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Théorème + lien avec la translation ----------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Puissance d'une force en rotation", font_size=22, weight="BOLD"),
                MathTex(r"P = \mathcal{M}_\Delta(\vec{F}) \times \omega \quad \text{(en W)} \qquad P_C = \mathcal{M}_C \times \omega \ \text{(couple)}", font_size=23),
                Text("Moment non constant : puissance moyenne Pm = W / Δt.", font_size=20),
                MathTex(r"P = \mathcal{M}_\Delta(\vec{F})\,\omega = (F\times R)\,\omega = F\times(R\omega) = F\times v", font_size=22),
            ).arrange(DOWN, buff=0.24),
            box_width=11.2,
        )
        theoreme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La puissance d'une force en rotation vaut donc son "
                "moment multiplié par la vitesse angulaire, et pour un "
                "couple, P indice C égale ℳ indice C fois oméga. Si le "
                "moment n'est pas constant, on utilise la puissance "
                "moyenne, P indice m égale W sur delta t. On peut aussi "
                "retrouver le lien avec la translation : ℳ fois oméga "
                "s'écrit F fois R, fois oméga, soit F fois R oméga, "
                "c'est-à-dire F fois v, exactement la formule de la "
                "puissance en translation."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Schéma bétonnière (tambour tournant) ---------------------------------
        centre = LEFT * 3.0 + DOWN * 0.4
        tambour = Circle(radius=1.2, color="#595959", stroke_width=4).move_to(centre)
        pale = Vector(RIGHT * 1.2, color="#DE7C1F").shift(centre)
        schema = VGroup(tambour, pale, Dot(centre, color=WHITE, radius=0.05))
        schema.scale(0.85)

        with self.voiceover(
            text=(
                "Sur la bétonnière, le tambour tourne autour de son axe "
                "sous l'effet du couple moteur : plus la vitesse de "
                "rotation est élevée, plus la puissance fournie est "
                "grande, à couple égal."
            )
        ) as tracker:
            self.play(Create(schema))
            self.play(Rotate(pale, angle=2.4, about_point=centre, run_time=1.5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple résolu 5 : bétonnière -----------------------------------------
        exemple = example_box(
            VGroup(
                Text("Exemple 5 — bétonnière, couple moteur ℳ_C = 20 N·m :", font_size=21),
                Text("Vitesse de rotation n = 30 tr/min.", font_size=20),
                MathTex(r"\omega = \dfrac{2\pi n}{60} = \dfrac{2\pi \times 30}{60} = \pi \approx 3{,}14\ \text{rad/s}", font_size=24),
                MathTex(r"P_C = \mathcal{M}_C \times \omega = 20 \times \pi \approx 62{,}8\ \text{W}", font_size=25),
            ).arrange(DOWN, buff=0.28),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : le tambour d'une bétonnière est entraîné par "
                "un couple moteur de vingt newton-mètre, à trente tours "
                "par minute. On convertit d'abord en radians par seconde "
                ": oméga égale deux pi n sur soixante, soit deux pi fois "
                "trente sur soixante, c'est-à-dire pi, environ trois "
                "virgule quatorze radians par seconde. La puissance vaut "
                "alors ℳ indice C fois oméga, soit vingt fois pi, environ "
                "soixante-deux virgule huit watts."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "P = ℳΔ(F⃗)×ω (couple : P_C = ℳ_C×ω), avec ω en rad/s. "
                    "On retrouve P = F×v en revenant à la translation.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : la puissance en rotation vaut le moment fois "
                "la vitesse angulaire, avec oméga toujours en radians par "
                "seconde. Pour un couple, on utilise ℳ indice C. Cette "
                "formule redonne exactement P égale F fois v lorsqu'on "
                "revient à un point matériel en translation."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège -------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : dans P = ℳω, la vitesse de rotation n (en "
                    "tr/min) doit toujours être convertie en ω (rad/s) — "
                    "sinon la puissance calculée est fausse par un facteur "
                    "2π/60."
                ),
                font_size=21,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : dans la formule P égale ℳ fois oméga, "
                "la vitesse de rotation, souvent donnée en tours par "
                "minute sur les plaques signalétiques des moteurs, doit "
                "impérativement être convertie en radians par seconde "
                "avant le calcul, sous peine d'obtenir un résultat faux "
                "d'un facteur deux pi sur soixante."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
