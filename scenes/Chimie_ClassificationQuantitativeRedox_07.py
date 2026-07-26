"""
scenes/Chimie_ClassificationQuantitativeRedox_07.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 07.

§ 7. Signification des valeurs de E° : force des oxydants et des
réducteurs. `theorem_box` : plus E° est élevé, plus l'oxydant du couple
est fort (et son réducteur conjugué est faible) ; plus E° est faible,
plus le réducteur du couple est fort (et son oxydant conjugué est
faible). Conséquences pratiques : les métaux alcalins (Na, K...) sont des
réducteurs très forts (E° très négatif), les métaux nobles (Au, Ag) sont
de mauvais réducteurs (E° élevé), et l'ion H₃O⁺ ne peut oxyder que les
métaux de potentiel standard négatif.
Source : 1ereC/Chimie.pdf, chapitre 11, pages 108-109.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    GREEN,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, theorem_box, warning_box


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


def _axe_force():
    """Petit axe vertical schématique montrant, aux deux extrémités, les
    zones "oxydant fort" (E° élevé) et "réducteur fort" (E° faible)."""
    axe = Line([0, -1.6, 0], [0, 1.6, 0], color=WHITE, stroke_width=3)
    fleche = Arrow([0, 1.6, 0], [0, 2.0, 0], color=WHITE, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.5)

    haut = VGroup(
        Text("E° élevé", font_size=18, color=YELLOW, weight="BOLD"),
        Text("→ Ox fort, Red conjugué faible", font_size=15, color=YELLOW),
    ).arrange(DOWN, buff=0.1)
    haut.next_to(axe.get_top(), RIGHT, buff=0.3)

    bas = VGroup(
        Text("E° faible", font_size=18, color=GREEN, weight="BOLD"),
        Text("→ Red fort, Ox conjugué faible", font_size=15, color=GREEN),
    ).arrange(DOWN, buff=0.1)
    bas.next_to(axe.get_bottom(), RIGHT, buff=0.3)

    return VGroup(axe, fleche, haut, bas)


class SignificationValeursE0(NotionScene):
    def construct(self):
        titre = scene_title("11.7 Signification des valeurs de E° : force des couples")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------------------
        intro = Text(
            _wrap(
                "L'échelle des E° construite précédemment n'est pas "
                "qu'un classement : chaque valeur numérique renseigne "
                "directement sur la FORCE de l'oxydant et du réducteur "
                "du couple.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'échelle des potentiels standard que nous venons de "
                "construire n'est pas un simple classement décoratif : "
                "chaque valeur numérique renseigne directement sur la "
                "force de l'oxydant et du réducteur du couple considéré. "
                "C'est ce lien que nous allons établir maintenant."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : théorème + schéma ------------------------------------------
        theo = theorem_box(
            VGroup(
                Text("Plus E°(Ox/Red) est ÉLEVÉ,", font_size=21, weight="BOLD"),
                Text("plus l'oxydant Ox est FORT (son réducteur conjugué est faible).", font_size=19),
                Text("Plus E°(Ox/Red) est FAIBLE,", font_size=21, weight="BOLD"),
                Text("plus le réducteur Red est FORT (son oxydant conjugué est faible).", font_size=19),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.4,
        )
        theo.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le théorème central de cette échelle. Plus le "
                "potentiel standard d'un couple est élevé, plus son "
                "oxydant est fort — et donc plus son réducteur conjugué "
                "est faible. À l'inverse, plus le potentiel standard "
                "d'un couple est faible, c'est-à-dire plus il est "
                "négatif, plus son réducteur est fort — et donc plus son "
                "oxydant conjugué est faible."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        axe = _axe_force()
        axe.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Visualisons cela sur notre échelle : en haut, là où le "
                "potentiel standard est élevé, comme le fluor, on trouve "
                "les oxydants les plus forts, et leurs réducteurs "
                "conjugués, comme l'ion fluorure, sont extrêmement "
                "faibles. En bas, là où le potentiel standard est très "
                "négatif, comme le potassium, on trouve les réducteurs "
                "les plus forts, et leurs oxydants conjugués, comme l'ion "
                "potassium, sont extrêmement faibles."
            )
        ) as tracker:
            self.play(FadeIn(axe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(axe))

        # --- Exemple traité : conséquences pratiques ------------------------------------
        entete_consequences = Text("Conséquences pratiques", font_size=22, color=YELLOW, weight="BOLD")
        entete_consequences.next_to(titre, DOWN, buff=0.35)

        consequences = _bullets(
            [
                "Les métaux alcalins (Na, K...), en bas de l'échelle "
                "(E° très négatif), sont des réducteurs très forts : "
                "ils réagissent violemment, même avec l'eau.",
                "Les métaux « nobles » (Au, Ag), en haut de l'échelle "
                "(E° élevé), sont de très mauvais réducteurs : ils "
                "restent inaltérés dans la plupart des milieux (d'où "
                "leur usage en bijouterie).",
                "L'ion H₃O⁺ (E° = 0,00 V) ne peut oxyder que les "
                "métaux dont le potentiel standard est négatif "
                "(situés en dessous de lui sur l'échelle).",
            ],
            font_size=19,
            width=56,
        )
        consequences.next_to(entete_consequences, DOWN, buff=0.3)
        _fit(VGroup(entete_consequences, consequences), entete_consequences.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voyons trois conséquences pratiques. Les métaux "
                "alcalins, comme le sodium ou le potassium, situés tout "
                "en bas de l'échelle avec un potentiel standard très "
                "négatif, sont des réducteurs très forts : ils réagissent "
                "violemment, y compris avec l'eau. À l'opposé, les "
                "métaux dits nobles, comme l'or ou l'argent, situés en "
                "haut de l'échelle avec un potentiel standard élevé, sont "
                "de très mauvais réducteurs : ils restent inaltérés dans "
                "la plupart des milieux, ce qui explique leur usage en "
                "bijouterie. Enfin, l'ion oxonium, dont le potentiel "
                "standard vaut zéro, ne peut oxyder que les métaux dont "
                "le potentiel standard est négatif, c'est-à-dire situés "
                "en dessous de lui sur l'échelle."
            )
        ) as tracker:
            self.play(FadeIn(entete_consequences))
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_consequences), FadeOut(consequences))

        # --- Piège à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre « oxydant fort » et « réducteur "
                    "fort » d'un même couple : un couple avec un oxydant "
                    "fort a nécessairement un réducteur conjugué faible, "
                    "jamais les deux forts à la fois.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : au sein d'un même "
                "couple, on ne peut jamais avoir à la fois un oxydant "
                "fort et un réducteur fort. Un oxydant fort a "
                "nécessairement un réducteur conjugué faible, et "
                "réciproquement : c'est ce qu'on appelle la force "
                "relative d'un couple."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
