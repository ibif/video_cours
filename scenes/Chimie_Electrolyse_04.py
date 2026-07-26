"""
scenes/Chimie_Electrolyse_04.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 04.

§ 4. Tension de seuil et prévision des réactions aux électrodes. Courbe
I = f(Uac) d'une électrolyse : courant quasi nul tant que U reste en
dessous de la tension de seuil, puis croissance rapide au-delà (tracée
avec Axes). Règle pratique pour prévoir les réactions : à la cathode
(électrode inerte), l'oxydant le plus facile à réduire réagit en
priorité (ion métallique réductible, sinon H⁺, sinon l'eau) ; à l'anode
inerte, le réducteur le plus facile à oxyder réagit en priorité (Cl⁻,
Br⁻, I⁻, sinon l'eau) ; si l'anode est soluble (en métal), c'est le
métal de l'électrode qui s'oxyde en priorité.
Source : 1ereC/Chimie.pdf, chapitre 14, pages 137-138.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _courbe_seuil():
    """Courbe I = f(Uac) avec tension de seuil, construite avec Axes."""
    axes = Axes(
        x_range=[0, 3, 1],
        y_range=[0, 2.2, 1],
        x_length=5.5,
        y_length=3.2,
        axis_config={"color": WHITE, "stroke_width": 2, "include_tip": True},
    )
    label_x = Text("U_AC (V)", font_size=16, color=WHITE)
    label_x.next_to(axes.x_axis, RIGHT, buff=0.15)
    label_y = Text("I (A)", font_size=16, color=WHITE)
    label_y.next_to(axes.y_axis, UP, buff=0.15)

    u_seuil = 1.4
    courbe = axes.plot(
        lambda x: 0 if x < u_seuil else 1.6 * (x - u_seuil) ** 1.3,
        x_range=[0, 2.9],
        color=YELLOW,
        stroke_width=4,
    )

    point_seuil = axes.coords_to_point(u_seuil, 0)
    ligne_seuil = DashedLine(
        axes.coords_to_point(u_seuil, 0), axes.coords_to_point(u_seuil, 2.2),
        color=RED, stroke_width=2,
    )
    dot_seuil = Dot(point_seuil, color=RED)
    label_seuil = Text("U_seuil ≈ 1,4 V", font_size=16, color=RED)
    label_seuil.next_to(ligne_seuil, UP, buff=0.1).shift(RIGHT * 0.3)

    return VGroup(axes, label_x, label_y, courbe, ligne_seuil, dot_seuil, label_seuil)


class TensionSeuilPrevoirReactionsElectrodes(NotionScene):
    def construct(self):
        titre = scene_title("14.4 Tension de seuil et prévision des réactions aux électrodes")
        titre.scale(0.36)
        titre.to_edge(UP)

        # --- Énoncé : la courbe I = f(U) -------------------------------------------
        intro = Text(
            _wrap(
                "L'expérience de découverte montrait un seuil net à 1,4 V. "
                "La courbe intensité-tension d'une électrolyse confirme "
                "ce comportement à toutes les tensions.",
                width=58,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avions observé, avec le chlorure d'étain, un seuil "
                "très net à un virgule quatre volt. La courbe intensité "
                "en fonction de la tension d'une électrolyse confirme ce "
                "comportement de façon générale."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : tracé de la courbe --------------------------------------
        entete_courbe = Text("Courbe I = f(U_AC) d'une électrolyse", font_size=21, color=YELLOW, weight="BOLD")
        entete_courbe.next_to(titre, DOWN, buff=0.3)

        courbe = _courbe_seuil()
        courbe.next_to(entete_courbe, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Tant que la tension U entre anode et cathode reste "
                "inférieure à la tension de seuil, le courant I mesuré "
                "reste quasiment nul : aucune transformation ne se "
                "produit. Dès que la tension de seuil est dépassée, le "
                "courant croît rapidement, signe que la réaction "
                "d'électrolyse démarre et s'intensifie."
            )
        ) as tracker:
            self.play(FadeIn(entete_courbe))
            self.play(Write(courbe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_courbe), FadeOut(courbe))

        # --- Exemple traité : règle pratique cathode --------------------------------
        entete_regle = Text("Comment prévoir la réaction à chaque électrode ?", font_size=20, color=YELLOW, weight="BOLD")
        entete_regle.next_to(titre, DOWN, buff=0.3)

        regle_cathode = VGroup(
            Text("À LA CATHODE (réduction) :", font_size=19, color="#288073", weight="BOLD"),
            Text("l'oxydant le PLUS FACILE À RÉDUIRE réagit en priorité :", font_size=17, color=WHITE),
            Text("1) un ion métallique réductible, s'il y en a un ;", font_size=16, color=WHITE),
            Text("2) sinon, l'ion H⁺ ;", font_size=16, color=WHITE),
            Text("3) sinon, c'est l'eau elle-même qui est réduite.", font_size=16, color=WHITE),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)

        regle_anode = VGroup(
            Text("À L'ANODE inerte (oxydation) :", font_size=19, color=RED, weight="BOLD"),
            Text("le réducteur le PLUS FACILE À OXYDER réagit en priorité :", font_size=17, color=WHITE),
            Text("1) un ion Cl⁻, Br⁻ ou I⁻, s'il y en a un ;", font_size=16, color=WHITE),
            Text("2) sinon, c'est l'eau elle-même qui est oxydée.", font_size=16, color=WHITE),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)

        regles = VGroup(regle_cathode, regle_anode).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        regles.next_to(entete_regle, DOWN, buff=0.3)
        _fit(VGroup(entete_regle, regles), entete_regle.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Pour prévoir la réaction qui se produit réellement à "
                "chaque électrode inerte, on applique une règle de "
                "priorité. À la cathode, siège de la réduction, c'est "
                "l'oxydant le plus facile à réduire qui réagit en "
                "priorité : d'abord un ion métallique réductible s'il y "
                "en a un dans la solution, sinon l'ion hydrogène H plus, "
                "sinon, en dernier recours, c'est l'eau elle-même qui est "
                "réduite. À l'anode inerte, siège de l'oxydation, c'est le "
                "réducteur le plus facile à oxyder qui réagit en "
                "priorité : un ion chlorure, bromure ou iodure s'il y en a "
                "un, sinon c'est l'eau elle-même qui est oxydée."
            )
        ) as tracker:
            self.play(FadeIn(entete_regle))
            self.play(Write(regle_cathode))
            self.play(Write(regle_anode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_regle), FadeOut(regles))

        # --- À retenir : cas particulier de l'anode soluble ---------------------
        methode = method_box(
            VGroup(
                Text("Cas particulier : ANODE SOLUBLE (en métal)", font_size=20, weight="BOLD"),
                Text(
                    "Si l'électrode reliée au pôle + est un métal (Cu, Ag, "
                    "Zn...), c'est ce MÉTAL lui-même qui s'oxyde en "
                    "priorité — les règles ci-dessus, valables pour une "
                    "électrode inerte, ne s'appliquent plus à cette "
                    "électrode.",
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=11.5,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons enfin un cas particulier important. Si "
                "l'électrode reliée au pôle plus, c'est-à-dire l'anode, "
                "est constituée d'un métal comme le cuivre, l'argent ou le "
                "zinc, ce sont les règles de l'anode inerte qui ne "
                "s'appliquent plus : c'est le métal de l'électrode "
                "lui-même qui s'oxyde en priorité, avant tout autre "
                "réducteur présent en solution. On parle alors d'anode "
                "soluble."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode), FadeOut(titre))
