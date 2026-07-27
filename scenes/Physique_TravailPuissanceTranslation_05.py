"""
scenes/Physique_TravailPuissanceTranslation_05.py — Chapitre 1 « Travail et
puissance dans le cas d'un mouvement de translation » (1ereC, Physique),
scène 05.

§ Puissance moyenne P_m=W/Δt (watt), puissance instantanée d'une force
constante P=δW/δt=F⃗·v⃗=F×v×cos(α), cas particuliers (colinéaire même
sens : P=Fv motrice ; sens opposé : P=-Fv résistante ; perpendiculaire :
P=0). Exemple résolu 4 : camion à 54 km/h, F=1200 N colinéaire.
Source : 1ereC/Physique.pdf, chapitre 1, pages 4-12.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Vector,
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
    warning_box,
)


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


FORCE_COLOR = "#DE7C1F"
VITESSE_COLOR = YELLOW


class PuissanceMoyenneInstantanee(NotionScene):
    def construct(self):
        titre = scene_title("Puissance d'une force constante")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Deux moteurs peuvent fournir exactement le même travail, "
                "mais l'un plus vite que l'autre : la puissance mesure la "
                "rapidité à laquelle un travail est effectué.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux moteurs peuvent fournir exactement le même travail, "
                "mais l'un beaucoup plus vite que l'autre. La puissance est "
                "la grandeur physique qui mesure la rapidité avec laquelle "
                "un travail est effectué."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : puissance moyenne -----------------------------------------
        moyenne = definition_box(
            VGroup(
                Text("Puissance moyenne", font_size=23, weight="BOLD"),
                MathTex(r"P_m = \dfrac{W}{\Delta t}", font_size=30),
                MathTex(r"1\ W = 1\ J/s \ \ (\text{watt})", font_size=26, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        moyenne.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La puissance moyenne développée par une force, sur une "
                "durée delta t, est le rapport du travail W fourni pendant "
                "cette durée, sur la durée elle-même. Elle s'exprime en "
                "watts : un watt correspond à un travail d'un joule fourni "
                "en une seconde."
            )
        ) as tracker:
            self.play(FadeIn(moyenne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(moyenne))

        instantanee = definition_box(
            VGroup(
                Text("Puissance instantanée", font_size=23, weight="BOLD"),
                MathTex(
                    r"P = \dfrac{\delta W}{\delta t} = \vec{F}\cdot\vec{v} = F\times v \times \cos(\alpha)",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        instantanee.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La puissance instantanée, à un instant donné, est la "
                "limite de ce rapport sur une durée infiniment petite. Pour "
                "une force constante, elle se calcule directement comme le "
                "produit scalaire de la force par le vecteur vitesse : P "
                "égale F vecteur, scalaire v vecteur, soit F fois v fois "
                "cosinus de alpha, alpha étant l'angle entre la force et la "
                "vitesse."
            )
        ) as tracker:
            self.play(FadeIn(instantanee))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(instantanee))

        row1 = VGroup(
            Text("Même sens (α=0°)", font_size=21),
            MathTex(r"P = F\times v \ (>0,\ \text{motrice})", font_size=22),
        ).arrange(RIGHT, buff=0.5)
        row2 = VGroup(
            Text("Sens opposé (α=180°)", font_size=21),
            MathTex(r"P = -F\times v \ (<0,\ \text{résistante})", font_size=22),
        ).arrange(RIGHT, buff=0.5)
        row3 = VGroup(
            Text("Perpendiculaire (α=90°)", font_size=21),
            MathTex(r"P = 0", font_size=22),
        ).arrange(RIGHT, buff=0.5)
        cas = VGroup(row1, row2, row3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        cas_box = property_box(cas, box_width=11.5)
        cas_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Trois cas particuliers à connaître. Si la force et la "
                "vitesse sont colinéaires et de même sens, la puissance "
                "vaut F fois v, positive : elle est motrice. Si elles sont "
                "de sens opposés, la puissance vaut moins F fois v, "
                "négative : elle est résistante. Et si la force est "
                "perpendiculaire à la vitesse, la puissance est nulle."
            )
        ) as tracker:
            self.play(FadeIn(cas_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_box))

        # --- Exemple traité 4 : camion --------------------------------------------------
        camion = Rectangle(width=1.6, height=0.7, color="#FFFFFF", fill_color="#3A3A3A", fill_opacity=0.9)
        vitesse = Vector(RIGHT * 1.5, color=VITESSE_COLOR).next_to(camion, UP, buff=0.25)
        label_v = MathTex(r"\vec{v}", font_size=24, color=VITESSE_COLOR).next_to(vitesse, UP, buff=0.1)
        force = Vector(RIGHT * 1.5, color=FORCE_COLOR).next_to(camion, DOWN, buff=0.25)
        label_f = MathTex(r"\vec{F}", font_size=24, color=FORCE_COLOR).next_to(force, DOWN, buff=0.1)
        figure_camion = VGroup(camion, vitesse, label_v, force, label_f)
        figure_camion.move_to(ORIGIN).shift(DOWN * 0.3 + LEFT * 1.5)

        enonce = exercise_box(
            Text(
                _wrap(
                    "Un camion roule à vitesse constante de 54 km/h. Le "
                    "moteur exerce une force motrice F = 1200 N, colinéaire "
                    "et de même sens que la vitesse. Calculer la puissance "
                    "développée par cette force.",
                    width=44,
                ),
                font_size=21,
            ),
            box_width=8.0,
        )
        enonce.to_edge(RIGHT, buff=0.4).shift(UP * 0.3)

        with self.voiceover(
            text=(
                "Exemple résolu. Un camion roule à vitesse constante de "
                "cinquante-quatre kilomètres par heure. Le moteur exerce "
                "une force motrice de mille deux cents newtons, colinéaire "
                "et de même sens que la vitesse. Calculons la puissance "
                "développée par cette force."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.play(FadeIn(figure_camion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce), FadeOut(figure_camion))

        calc = corrige_box(
            VGroup(
                MathTex(r"v = 54\ km/h = \dfrac{54}{3{,}6} = 15\ m/s", font_size=25),
                MathTex(r"P = F\times v = 1200\times15 = 18\,000\ W = 18\ kW", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        calc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On convertit d'abord la vitesse en mètres par seconde : "
                "cinquante-quatre kilomètres par heure, divisé par trois "
                "virgule six, donne quinze mètres par seconde. La force et "
                "la vitesse étant colinéaires et de même sens, la puissance "
                "vaut simplement mille deux cents fois quinze, soit "
                "dix-huit mille watts, autrement dit dix-huit kilowatts."
            )
        ) as tracker:
            self.play(FadeIn(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                MathTex(
                    r"P_m = \dfrac{W}{\Delta t} \qquad P = \vec{F}\cdot\vec{v} = F\,v\,\cos(\alpha)",
                    font_size=26,
                ),
                Text(
                    _wrap(
                        "Toujours convertir la vitesse en m/s et la durée "
                        "en s avant de calculer.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : la puissance moyenne est le rapport du "
                "travail sur la durée, et la puissance instantanée d'une "
                "force constante vaut F vecteur scalaire v vecteur. Avant "
                "tout calcul, toujours convertir la vitesse en mètres par "
                "seconde et la durée en secondes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège classique : oublier de convertir km/h en m/s "
                    "(diviser par 3,6). Ne pas confondre puissance moyenne "
                    "(sur une durée) et puissance instantanée (à un instant "
                    "précis) : elles ne coïncident que si la vitesse est "
                    "constante.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège classique : oublier de convertir la vitesse de "
                "kilomètres par heure en mètres par seconde, en divisant "
                "par trois virgule six. Autre piège : ne pas confondre "
                "puissance moyenne, calculée sur une durée, et puissance "
                "instantanée, calculée à un instant précis. Elles ne "
                "coïncident que si le mouvement est uniforme."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
