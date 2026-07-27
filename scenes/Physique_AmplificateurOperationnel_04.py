"""
scenes/Physique_AmplificateurOperationnel_04.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 04.

§ 4. Chronogrammes du comparateur et applications. Méthode : tracer Ue(t)
et la droite Uref sur les mêmes axes, repérer les instants de
basculement, puis tracer le palier de sortie correspondant. Exemple :
Uref = 2 V (constant), Ue(t) = 4·sin(2πft) (f = 1 Hz), Vsat = 12 V →
signal de sortie rectangulaire qui bascule à chaque intersection.
Applications : thermostat, commande d'éclairage, détection de seuil.
Source : 1ereC/Physique.pdf, pages 99-107 (§ 4).
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _chronogrammes():
    """Deux graphes empilés : Ue(t) sinusoïdale + droite Uref (haut), et
    le signal de sortie Vs(t) en créneaux qui en résulte (bas)."""
    f = 1.0
    uref = 2.0

    axes_e = Axes(
        x_range=[0, 2, 0.5],
        y_range=[-5, 5, 5],
        x_length=6.6,
        y_length=2.2,
        axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
    )
    ue_courbe = axes_e.plot(lambda t: 4 * np.sin(2 * np.pi * f * t), x_range=[0, 2], color=YELLOW)
    uref_droite = axes_e.plot(lambda t: uref, x_range=[0, 2], color=ORANGE)
    label_ue = MathTex("U_e(t)", font_size=20, color=YELLOW).next_to(axes_e, UP, buff=0.1).align_to(axes_e, LEFT)
    label_uref = MathTex("U_{ref}", font_size=18, color=ORANGE).next_to(
        axes_e.c2p(2, uref), RIGHT, buff=0.1
    )

    # Instants de basculement : 4 sin(2π t) = 2  →  sin(2π t) = 0,5
    # → 2π t = π/6 + 2kπ  ou  2π t = 5π/6 + 2kπ
    t1 = (np.pi / 6) / (2 * np.pi)
    t2 = (5 * np.pi / 6) / (2 * np.pi)
    t3 = t1 + 1
    t4 = t2 + 1

    axes_s = Axes(
        x_range=[0, 2, 0.5],
        y_range=[-14, 14, 14],
        x_length=6.6,
        y_length=2.2,
        axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
    )
    axes_s.next_to(axes_e, DOWN, buff=0.7)

    vsat = 12
    paliers = [(0, t1, -vsat), (t1, t2, vsat), (t2, t3, -vsat), (t3, t4, vsat), (t4, 2, -vsat)]
    vs_courbe = VGroup()
    for t_debut, t_fin, niveau in paliers:
        vs_courbe.add(
            Line(axes_s.c2p(t_debut, niveau), axes_s.c2p(t_fin, niveau), stroke_width=3, color=ORANGE)
        )
    for t_bascule in (t1, t2, t3, t4):
        vs_courbe.add(
            Line(axes_s.c2p(t_bascule, -vsat), axes_s.c2p(t_bascule, vsat), stroke_width=2, color=ORANGE)
        )
    label_vs = MathTex("V_s(t)", font_size=20, color=ORANGE).next_to(axes_s, UP, buff=0.1).align_to(axes_s, LEFT)

    return VGroup(axes_e, ue_courbe, uref_droite, label_ue, label_uref, axes_s, vs_courbe, label_vs)


class ChronogrammeComparateurApplications(NotionScene):
    def construct(self):
        titre = scene_title("Chronogrammes du comparateur et applications")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Quand la tension d'entrée d'un comparateur varie dans le "
                "temps, comment prévoir l'allure de la sortie sans "
                "recalculer Vs à chaque instant ?",
                width=58,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quand la tension d'entrée d'un comparateur varie dans le "
                "temps, comment prévoir l'allure de la sortie sans "
                "recalculer Vs à chaque instant ? La méthode du "
                "chronogramme répond à cette question."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : méthode -------------------------------------------
        methode = method_box(
            VGroup(
                Text("1. Tracer Ue(t) et la droite horizontale Uref sur les", font_size=19),
                Text("    mêmes axes.", font_size=19),
                Text("2. Repérer les instants où les deux courbes se", font_size=19),
                Text("    croisent : ce sont les instants de basculement.", font_size=19),
                Text("3. Entre deux basculements, conclure sur le palier", font_size=19),
                Text("    (+Vsat ou −Vsat) selon le signe de Ue − Uref.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.2,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La méthode comporte trois étapes. Un : tracer Ue de t et "
                "la droite horizontale Uref sur les mêmes axes. Deux : "
                "repérer les instants où les deux courbes se croisent, ce "
                "sont les instants de basculement. Trois : entre deux "
                "basculements, conclure sur le palier de sortie, plus "
                "Vsat ou moins Vsat, selon le signe de Ue moins Uref."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : chronogrammes complets --------------------------
        graphes = _chronogrammes()
        graphes.scale(0.82)
        graphes.next_to(titre, DOWN, buff=0.35)

        exemple_txt = example_box(
            VGroup(
                Text("Uref = 2 V, Ue(t) = 4·sin(2πft) avec f = 1 Hz,", font_size=18),
                Text("Vsat = 12 V → Vs(t) bascule à chaque croisement.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=8.6,
        )
        exemple_txt.next_to(graphes, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple traité : Uref vaut 2 volts, constante. Ue de t "
                "vaut 4 fois sinus de 2 pi f t, avec une fréquence f de 1 "
                "hertz. Vsat vaut 12 volts. Chaque fois que la sinusoïde "
                "Ue croise la droite Uref, la sortie Vs bascule "
                "instantanément entre plus 12 volts et moins 12 volts : on "
                "obtient un signal rectangulaire, comme le montre le "
                "second graphe."
            )
        ) as tracker:
            self.play(FadeIn(graphes))
            self.play(FadeIn(exemple_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphes), FadeOut(exemple_txt))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("La sortie du comparateur est un signal en créneaux :", font_size=20),
                Text("elle bascule à chaque croisement de Ue(t) et Uref.", font_size=20),
                Text("Applications : thermostat, commande d'éclairage,", font_size=20),
                Text("détection de seuil.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. La sortie d'un comparateur est "
                "toujours un signal en créneaux, qui bascule à chaque "
                "croisement entre Ue de t et Uref. Cette propriété est "
                "exploitée dans de nombreuses applications : le "
                "thermostat, la commande automatique d'éclairage, ou plus "
                "généralement la détection de seuil."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas oublier de tracer Uref sur LE MÊME graphe", font_size=19),
                Text("   que Ue(t) : sans cette comparaison visuelle, on", font_size=19),
                Text("   risque de mal placer les instants de basculement.", font_size=19),
                Text("• Le basculement est instantané dans le modèle idéal", font_size=19),
                Text("   (pas de pente lors du saut de −Vsat à +Vsat).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Ne pas oublier de tracer Uref sur "
                "le même graphe que Ue de t : sans cette comparaison "
                "visuelle directe, on risque de mal placer les instants de "
                "basculement. Et se rappeler que ce basculement est "
                "instantané dans le modèle idéal : il n'y a pas de pente "
                "progressive lors du saut de moins Vsat à plus Vsat."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
