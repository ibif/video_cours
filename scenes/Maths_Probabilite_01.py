"""
scenes/Maths_Probabilite_01.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 01.

§ Expérience aléatoire et univers Ω : définition d'une expérience
aléatoire (résultats connus mais imprévisibles), définition de l'univers
Ω (ensemble de tous les résultats possibles), issue/éventualité, notation
Card(Ω). Exemple résolu : lancer d'un dé cubique, Ω={1,2,3,4,5,6},
Card(Ω)=6.
Source : 1ereC/Maths.pdf, chapitre 12, pages 142-143.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _de_cubique() -> VGroup:
    """Petit schéma : les 6 faces d'un dé, alignées, comme issues de Ω."""
    faces = VGroup()
    for k in range(1, 7):
        carre = RoundedRectangle(width=0.8, height=0.8, corner_radius=0.08, color=WHITE, stroke_width=2)
        chiffre = MathTex(str(k), font_size=28, color=WHITE)
        chiffre.move_to(carre.get_center())
        faces.add(VGroup(carre, chiffre))
    faces.arrange(RIGHT, buff=0.25)
    return faces


class ExperienceAleatoireUnivers(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Expérience aléatoire et univers")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Lancer un dé, tirer une carte, faire tourner une roue : "
                "dans chacune de ces situations, on connaît à l'avance "
                "TOUS les résultats possibles, mais on ne peut pas prévoir "
                "avec certitude LEQUEL va se produire.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Lancer un dé, tirer une carte au hasard dans un jeu, "
                "faire tourner une roue de loterie : dans chacune de ces "
                "situations, on connaît à l'avance tous les résultats "
                "possibles, mais on ne peut pas prévoir avec certitude "
                "lequel d'entre eux va se produire. C'est tout l'objet de "
                "ce nouveau chapitre : les probabilités."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définitions ------------------------------------
        def_experience = definition_box(
            VGroup(
                Text("Expérience aléatoire", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "Une expérience est dite ALÉATOIRE lorsqu'on "
                        "connaît à l'avance tous ses résultats possibles, "
                        "mais qu'on ne peut pas prévoir avec certitude "
                        "lequel se produira, avant de la réaliser.",
                        width=46,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_experience.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une expérience est dite aléatoire lorsqu'on connaît à "
                "l'avance tous ses résultats possibles, mais qu'on ne peut "
                "pas prévoir avec certitude lequel d'entre eux va se "
                "produire, avant de la réaliser."
            )
        ) as tracker:
            self.play(FadeIn(def_experience))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_experience))

        def_univers = definition_box(
            VGroup(
                Text("Univers Ω d'une expérience aléatoire", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "L'univers, noté Ω (oméga), est l'ensemble de "
                        "TOUS les résultats possibles d'une expérience "
                        "aléatoire. Chaque élément de Ω est une ISSUE (ou "
                        "ÉVENTUALITÉ). On note Card(Ω) le nombre d'issues.",
                        width=46,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_univers.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'ensemble de tous les résultats possibles d'une "
                "expérience aléatoire s'appelle l'univers de cette "
                "expérience, noté Ω, la lettre grecque oméga. Chaque "
                "élément de Ω est appelé une issue, ou une éventualité. "
                "Le nombre d'issues se note Card de Ω, comme un cardinal "
                "d'ensemble, notion vue au chapitre précédent sur le "
                "dénombrement."
            )
        ) as tracker:
            self.play(FadeIn(def_univers))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_univers))

        # --- Exemple traité : lancer d'un dé cubique ------------------------
        enonce_de = Text(
            _wrap("Exemple résolu : on lance un dé cubique bien équilibré, à 6 faces numérotées de 1 à 6.", width=54),
            font_size=23,
        )
        enonce_de.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons l'exemple le plus simple : on lance un dé "
                "cubique bien équilibré, dont les 6 faces sont numérotées "
                "de 1 à 6."
            )
        ) as tracker:
            self.play(FadeIn(enonce_de))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_de))

        de = _de_cubique()
        de.next_to(titre, DOWN, buff=0.6)
        univers_de = MathTex(r"\Omega = \{1\,;\,2\,;\,3\,;\,4\,;\,5\,;\,6\}", font_size=30)
        univers_de.next_to(de, DOWN, buff=0.5)
        card_de = MathTex(r"\mathrm{Card}(\Omega) = 6", font_size=30, color=YELLOW)
        card_de.next_to(univers_de, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les six résultats possibles sont les six faces du dé. "
                "L'univers de cette expérience est donc Ω égale l'ensemble "
                "1, 2, 3, 4, 5, 6. Chacun de ces six chiffres est une "
                "issue. Le cardinal de Ω vaut 6 : il y a exactement six "
                "issues possibles."
            )
        ) as tracker:
            self.play(Write(de))
            self.play(Write(univers_de))
            self.play(FadeIn(card_de))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(de), FadeOut(univers_de), FadeOut(card_de))

        # --- Piège à éviter --------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Bien lister TOUTES les issues", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "Oublier une issue, ou en compter une deux fois, "
                        "fausse tout le calcul de Card(Ω) — et donc, comme "
                        "on le verra, toutes les probabilités qui en "
                        "découlent.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un piège à éviter dès à présent : oublier une issue, ou "
                "au contraire en compter une deux fois, fausse tout le "
                "calcul de Card de Ω — et par conséquent, comme nous le "
                "verrons bientôt, toutes les probabilités qui en "
                "découlent. Bien définir Ω est donc la toute première "
                "étape, indispensable, de tout exercice de probabilité."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
