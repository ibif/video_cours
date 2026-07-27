"""
scenes/Physique_TravailPuissanceRotation_05.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 05.

§ Travail d'une force dont le moment est constant : travail élémentaire
δW = ℳΔ(F⃗)×δθ avec démonstration (δℓ = Rδθ), théorème pour une rotation
finie W = ℳΔ(F⃗)×Δθ (moteur/résistant selon le signe), travail d'un couple
W_C = ℳ_C×Δθ. Exemple résolu 4 : manivelle de treuil, 5 tours.
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
    Line,
    MathTex,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class TravailForceMomentConstant(NotionScene):
    def construct(self):
        titre = scene_title("Travail d'une force de moment constant")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Un ouvrier tourne une manivelle : quel travail fournit-il "
                "pendant que la manivelle parcourt un angle donné ?",
                width=54,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un ouvrier tourne la manivelle d'un treuil, avec une "
                "force dont le moment reste constant. Quel travail cette "
                "force fournit-elle pendant que la manivelle balaie un "
                "certain angle ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : démonstration δW = ℳΔθ ------------------------------
        centre = LEFT * 3.2 + DOWN * 0.5
        manivelle = Line(centre, centre + RIGHT * 1.6, color=WHITE, stroke_width=5)
        arc_dtheta = Arc(radius=1.6, start_angle=0, angle=0.5, arc_center=centre, color="#288073", stroke_width=4)
        point_a = centre + RIGHT * 1.6
        force = Vector(UP * 1.0, color="#DE7C1F").shift(point_a)
        f_label = MathTex(r"\vec{F}", font_size=24, color="#DE7C1F").next_to(force, RIGHT, buff=0.1)
        r_label = MathTex(r"R", font_size=22, color=WHITE).next_to(manivelle, DOWN, buff=0.15)
        schema = VGroup(manivelle, arc_dtheta, force, f_label, r_label, Dot(centre, color=YELLOW, radius=0.05))
        schema.scale(0.85)

        demo = VGroup(
            MathTex(r"\delta\ell = R\,\delta\theta \quad \text{(arc parcouru par A)}", font_size=23),
            MathTex(r"\delta W = F\cos(\varphi)\,\delta\ell = F\cos(\varphi)\,R\,\delta\theta", font_size=23),
            MathTex(r"F\cos(\varphi)\,R = F\times d = \mathcal{M}_\Delta(\vec{F}) \ \Rightarrow\ \delta W = \mathcal{M}_\Delta(\vec{F})\,\delta\theta", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.28)
        demo.next_to(schema, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Pendant une rotation élémentaire delta thêta, le point "
                "d'application A, situé à la distance R de l'axe, parcourt "
                "un petit arc delta ℓ égal à R fois delta thêta. Le "
                "travail élémentaire de la force vaut F fois cosinus de "
                "phi, fois delta ℓ, où phi est l'angle entre la force et "
                "le déplacement. Or F fois cosinus phi fois R n'est autre "
                "que F fois le bras de levier d, c'est-à-dire exactement "
                "le moment de la force. On obtient donc delta W égale "
                "ℳ delta de F, fois delta thêta."
            )
        ) as tracker:
            self.play(Create(schema))
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(demo))

        # --- Théorème pour une rotation finie ------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Travail d'une force de moment constant", font_size=22, weight="BOLD"),
                MathTex(r"W = \mathcal{M}_\Delta(\vec{F}) \times \Delta\theta \quad (\Delta\theta \ \text{en radians})", font_size=27),
                Text("Moteur si W et Δθ ont même signe, résistant sinon.", font_size=20),
                MathTex(r"\text{Pour un couple : } W_C = \mathcal{M}_C \times \Delta\theta", font_size=24),
            ).arrange(DOWN, buff=0.24),
            box_width=10.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En intégrant sur une rotation finie, on obtient le "
                "théorème : le travail W est égal au moment ℳ delta de F, "
                "multiplié par la variation d'angle delta thêta, exprimée "
                "en radians. Ce travail est moteur si le moment et delta "
                "thêta ont le même signe, résistant sinon. Pour un couple "
                "de forces, la même relation s'écrit W indice C égale "
                "ℳ indice C fois delta thêta."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 4 : manivelle de treuil, 5 tours ---------------------
        exemple = example_box(
            VGroup(
                Text("Exemple 4 — manivelle de treuil, couple constant ℳ_C = 8 N·m :", font_size=20),
                Text("L'ouvrier fait tourner la manivelle de 5 tours complets.", font_size=20),
                MathTex(r"\Delta\theta = 5 \times 2\pi = 10\pi \ \text{rad}", font_size=25),
                MathTex(r"W_C = \mathcal{M}_C \times \Delta\theta = 8 \times 10\pi = 80\pi \approx 251\ \text{J}", font_size=25),
            ).arrange(DOWN, buff=0.28),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : un ouvrier actionne la manivelle d'un treuil "
                "avec un couple constant de huit newton-mètre, sur cinq "
                "tours complets. L'angle balayé vaut cinq fois deux pi, "
                "soit dix pi radians. Le travail fourni vaut alors "
                "ℳ indice C fois delta thêta, c'est-à-dire huit fois dix "
                "pi, soit quatre-vingts pi, environ deux cent cinquante et "
                "un joules."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "δW = ℳΔ(F⃗)×δθ et, pour une rotation finie, "
                    "W = ℳΔ(F⃗)×Δθ (Δθ en radians). Pour un couple : "
                    "W_C = ℳ_C×Δθ.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : le travail élémentaire vaut delta W égale le "
                "moment fois delta thêta, et pour une rotation finie, W "
                "égale le moment fois delta thêta, l'angle étant toujours "
                "exprimé en radians. Pour un couple, W indice C égale "
                "ℳ indice C fois delta thêta."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : Δθ doit être en radians dans W = ℳΔθ, jamais "
                    "en tours ni en degrés — convertir d'abord (1 tour = "
                    "2π rad)."
                ),
                font_size=22,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : dans la formule W égale ℳ fois delta "
                "thêta, l'angle doit impérativement être exprimé en "
                "radians, jamais en tours ni en degrés. Il faut donc "
                "toujours convertir un nombre de tours en radians, en "
                "multipliant par deux pi, avant d'appliquer la formule."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
