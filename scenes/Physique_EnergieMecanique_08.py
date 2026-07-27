"""
scenes/Physique_EnergieMecanique_08.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 08.

Application : le pendule simple. Définition. Étude énergétique (tension
perpendiculaire, travail nul, seul le poids travaille → Em se conserve).
z=L(1-cosθ) référence position d'équilibre. Em=½mv²+mgL(1-cosθ)=constante.
Vitesse maximale au passage à l'équilibre : v_max=√(2gL(1-cosθ₀)). Symétrie
des oscillations (amplitude θ₀ des deux côtés en l'absence de frottement,
réalité : amortissement). Exemple résolu 5 : pendule m=100 g, L=0,8 m,
θ₀=60° → Em=0,4 J, v_max≈2,83 m/s.
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
"""

import textwrap

import numpy as np

from manim import (
    DEGREES,
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
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
from shapes.boxes import corrige_box, definition_box, essentiel_box, exercise_box, property_box, scene_title, warning_box

FIL_COLOR = "#A8A8A8"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _pendule(angle_deg: float):
    """Pendule simple : point de suspension O, fil de longueur L, masse au bout."""
    origine = ORIGIN
    angle_rad = angle_deg * DEGREES
    longueur = 2.0
    bout = origine + longueur * (np.sin(angle_rad) * RIGHT + (-np.cos(angle_rad)) * UP)
    fil = Line(origine, bout, color=FIL_COLOR, stroke_width=2)
    masse = Dot(bout, color=YELLOW, radius=0.15)
    support = Dot(origine, color=WHITE, radius=0.05)
    verticale = Line(origine, origine + DOWN * longueur, color=WHITE, stroke_width=1.5)
    arc_angle = Arc(radius=0.6, start_angle=-90 * DEGREES, angle=angle_rad, arc_center=origine, color=WHITE, stroke_width=2)
    return VGroup(verticale, fil, arc_angle, support, masse), bout, origine


class ApplicationPenduleSimple(NotionScene):
    def construct(self):
        titre = scene_title("Application : le pendule simple")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définition et schéma ---------------------------------------------
        pendule_group, bout, origine = _pendule(35)
        theta_label = MathTex(r"\theta", font_size=24).move_to(origine + DOWN * 0.9 + RIGHT * 0.25)
        l_label = MathTex("L", font_size=24).move_to((origine + bout) / 2 + LEFT * 0.3)
        schema = VGroup(pendule_group, theta_label, l_label)
        schema.scale(0.9).move_to(LEFT * 3.2)

        definition = definition_box(
            VGroup(
                Text("Pendule simple", font_size=21, weight="BOLD"),
                Text("Masse ponctuelle m au bout d'un fil", font_size=19),
                Text("inextensible, de longueur L, sans masse,", font_size=19),
                Text("fixé en un point O.", font_size=19),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=5.6,
        )
        definition.next_to(schema, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Étudions maintenant le pendule simple : une masse "
                "ponctuelle m, fixée à l'extrémité d'un fil inextensible et "
                "sans masse, de longueur L, dont l'autre extrémité est "
                "attachée en un point fixe O. On écarte le pendule d'un "
                "angle thêta zéro par rapport à la verticale, puis on le "
                "lâche."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(schema), FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(definition))

        # --- Raisonnement : étude énergétique --------------------------------------------
        etude = property_box(
            VGroup(
                Text("Forces : poids P⃗ et tension du fil T⃗", font_size=20),
                Text("T⃗ toujours ⊥ à la trajectoire : W(T⃗)=0", font_size=20),
                Text("→ seul le poids travaille : Em se conserve", font_size=20),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
            box_width=9.4,
        )
        etude.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux forces s'exercent sur la masse : son poids, et la "
                "tension du fil. Or cette tension est, à chaque instant, "
                "perpendiculaire à la trajectoire circulaire : son travail "
                "est donc nul. Seul le poids travaille : l'énergie "
                "mécanique du pendule se conserve."
            )
        ) as tracker:
            self.play(FadeIn(etude))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etude))

        altitude = MathTex(
            r"z = L\,(1 - \cos\theta) \quad \text{(référence : position d'équilibre)}",
            font_size=27,
        )
        altitude.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En prenant comme référence des altitudes la position "
                "d'équilibre, verticale, du pendule, l'altitude de la masse "
                "à un angle thêta s'écrit z égale L fois un moins cosinus "
                "thêta."
            )
        ) as tracker:
            self.play(Write(altitude))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(altitude))

        em_pendule = property_box(
            MathTex(
                r"E_m = \tfrac{1}{2}mv^2 + mgL(1-\cos\theta) = \text{constante}",
                font_size=27,
            ),
            box_width=9.8,
        )
        em_pendule.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'énergie mécanique du pendule s'écrit donc un demi m v "
                "carré plus m g L fois un moins cosinus thêta, et cette "
                "somme reste constante tout au long du mouvement."
            )
        ) as tracker:
            self.play(FadeIn(em_pendule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(em_pendule))

        vmax = MathTex(
            r"\text{Passage à l'équilibre } (\theta=0) : \quad v_{max} = \sqrt{2gL(1-\cos\theta_0)}",
            font_size=25,
            color=YELLOW,
        )
        vmax.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La vitesse est maximale au passage à la position "
                "d'équilibre, où thêta vaut zéro : elle vaut alors racine "
                "de deux g L fois un moins cosinus thêta zéro, thêta zéro "
                "étant l'amplitude initiale du lâcher."
            )
        ) as tracker:
            self.play(Write(vmax))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vmax))

        symetrie = warning_box(
            Text(
                _wrap(
                    "En l'absence de frottement, le pendule remonte à la "
                    "même amplitude θ₀ de chaque côté (oscillations "
                    "symétriques). En réalité, les frottements de l'air "
                    "amortissent peu à peu le mouvement.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.0,
        )
        symetrie.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Conséquence de cette conservation : en l'absence de "
                "frottement, le pendule remonte exactement à la même "
                "amplitude thêta zéro de chaque côté de l'équilibre — les "
                "oscillations sont parfaitement symétriques. Dans la "
                "réalité, les frottements de l'air amortissent "
                "progressivement le mouvement, et l'amplitude diminue au "
                "fil du temps."
            )
        ) as tracker:
            self.play(FadeIn(symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(symetrie))

        # --- Exemple traité : pendule numérique ------------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Un pendule simple de masse m=100 g et de longueur "
                    "L=0,8 m est lâché sans vitesse initiale avec une "
                    "amplitude θ₀=60°. Calculer Em et la vitesse maximale "
                    "vmax (g=10 N/kg).",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.0,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu. Un pendule simple de masse cent grammes "
                "et de longueur zéro virgule huit mètre est lâché sans "
                "vitesse initiale avec une amplitude de soixante degrés. "
                "Calculons son énergie mécanique et sa vitesse maximale."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc1 = MathTex(
            r"E_m = mgL(1-\cos\theta_0) = 0{,}1\times 10\times 0{,}8\times(1-\cos 60^\circ)",
            font_size=23,
        )
        calc2 = MathTex(
            r"E_m = 0{,}1\times 10\times 0{,}8\times 0{,}5 = 0{,}4\ \text{J}",
            font_size=26,
        )
        calc3 = MathTex(
            r"v_{max} = \sqrt{\dfrac{2E_m}{m}} = \sqrt{\dfrac{2\times0{,}4}{0{,}1}} \approx 2{,}83\ \text{m/s}",
            font_size=26,
            color=YELLOW,
        )
        calc = VGroup(calc1, calc2, calc3).arrange(DOWN, buff=0.3)
        calc.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'énergie mécanique, entièrement potentielle au moment du "
                "lâcher puisque la vitesse initiale est nulle, vaut m g L "
                "fois un moins cosinus soixante degrés, soit zéro virgule "
                "un fois dix fois zéro virgule huit fois zéro virgule cinq, "
                "c'est-à-dire zéro virgule quatre joule. La vitesse "
                "maximale, au passage à l'équilibre, vaut racine de deux "
                "fois l'énergie mécanique divisée par la masse, soit "
                "environ deux virgule quatre-vingt-trois mètres par "
                "seconde."
            )
        ) as tracker:
            self.play(Write(calc1))
            self.play(Write(calc2))
            self.play(Write(calc3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ---------------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                MathTex(r"E_m = \tfrac{1}{2}mv^2 + mgL(1-\cos\theta) = \text{constante}", font_size=25),
                Text("v maximale à l'équilibre, nulle aux amplitudes extrêmes.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=10.6,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : pour un pendule simple, l'énergie "
                "mécanique vaut un demi m v carré plus m g L fois un moins "
                "cosinus thêta, et reste constante. La vitesse est maximale "
                "à la position d'équilibre, et nulle aux amplitudes "
                "extrêmes du mouvement."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : z=L(1-cosθ) n'est PAS z=L·θ. Ne pas confondre "
                    "l'altitude verticale (en cosinus) avec la longueur "
                    "de l'arc parcouru sur la trajectoire circulaire.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : l'altitude z égale L fois un moins "
                "cosinus thêta n'est surtout pas L fois thêta. Il ne faut "
                "pas confondre l'altitude verticale, qui fait intervenir un "
                "cosinus, avec la longueur de l'arc parcouru sur la "
                "trajectoire circulaire du pendule."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
