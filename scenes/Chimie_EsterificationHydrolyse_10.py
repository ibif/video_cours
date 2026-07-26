"""
scenes/Chimie_EsterificationHydrolyse_10.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 10.

§ L'hydrolyse des esters + la saponification. definition_box hydrolyse
(réaction inverse, R-COO-R'+H2O⇌R-COOH+R'-OH), mêmes caractéristiques
(lente, athermique, limitée), moyens d'amélioration (excès d'eau,
chauffage, H+). definition_box saponification (hydrolyse basique totale,
R-COO-R'+HO-→R-COO-+R'-OH), warning_box différence capitale : réaction
totale donc flèche simple. Application : fabrication des savons (triester
du glycérol + soude → glycérol + carboxylate de sodium), propriété
détersive (ion amphiphile, tête hydrophile/queue hydrophobe).
Source : 1ereC/Chimie.pdf, chapitre 8, pages 82-83.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    RED,
    Circle,
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
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class HydrolyseEstersEtSaponification(NotionScene):
    def construct(self):
        titre = scene_title("10. L'hydrolyse des esters et la saponification")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Nous avons déjà croisé l'hydrolyse comme réaction "
                "inverse, responsable du caractère limité de "
                "l'estérification. Il est temps de l'étudier pour "
                "elle-même, et de découvrir une variante décisive : la "
                "saponification.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons déjà croisé l'hydrolyse comme réaction "
                "inverse de l'estérification, responsable de son "
                "caractère limité. Il est temps de l'étudier pour "
                "elle-même, et de découvrir une variante décisive pour "
                "la fabrication des savons : la saponification."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : definition_box hydrolyse ---------------------------------
        definition1 = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "L'hydrolyse d'un ester est la réaction, réversible, "
                        "d'un ester avec l'eau, qui redonne l'acide "
                        "carboxylique et l'alcool dont il est issu.",
                        width=48,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"R-COO-R' + H_2O \;\rightleftharpoons\; R-COOH + R'-OH",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        definition1.next_to(titre, DOWN, buff=0.4)
        _fit(definition1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons cette définition : l'hydrolyse d'un ester est "
                "la réaction, réversible, d'un ester avec l'eau, qui "
                "redonne l'acide carboxylique et l'alcool dont il est "
                "issu : R-C-O-O-R' plus eau, en équilibre avec "
                "R-C-O-O-H plus R'-O-H. Sans surprise, c'est exactement "
                "l'équation inverse de l'estérification."
            )
        ) as tracker:
            self.play(FadeIn(definition1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition1))

        # --- même caractéristiques + moyens d'amélioration ---------------------------
        entete = Text("Mêmes caractéristiques, mêmes leviers", font_size=22, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        carac = Text(
            _wrap(
                "L'hydrolyse partage les 3 caractéristiques de "
                "l'estérification : réaction lente, athermique et "
                "limitée (même équilibre, vu dans l'autre sens).",
                width=48,
            ),
            font_size=21,
            color=WHITE,
        )
        leviers = Text(
            _wrap(
                "On augmente son rendement par les mêmes leviers : excès "
                "d'eau, chauffage (facteur cinétique) et catalyse par "
                "les ions H+ (facteur cinétique).",
                width=48,
            ),
            font_size=21,
            color=WHITE,
        )
        bloc = VGroup(carac, leviers).arrange(DOWN, buff=0.3)
        bloc.next_to(entete, DOWN, buff=0.35)
        groupe = VGroup(entete, bloc)
        _fit(groupe, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "L'hydrolyse partage exactement les trois "
                "caractéristiques de l'estérification, puisqu'il s'agit "
                "du même équilibre observé dans l'autre sens : c'est une "
                "réaction lente, athermique, et limitée. On augmente son "
                "rendement par les mêmes leviers : un excès d'eau "
                "déplace l'équilibre, tandis que le chauffage et la "
                "catalyse par les ions H plus restent de simples "
                "facteurs cinétiques, qui accélèrent sans déplacer "
                "l'équilibre."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(carac))
            self.play(FadeIn(leviers))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple traité : definition_box saponification + warning différence ---
        definition2 = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "La saponification est l'hydrolyse BASIQUE d'un "
                        "ester, par les ions hydroxyde HO⁻ : elle est "
                        "TOTALE (pas d'équilibre).",
                        width=48,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"R-COO-R' + HO^- \;\longrightarrow\; R-COO^- + R'-OH",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        definition2.next_to(titre, DOWN, buff=0.4)
        _fit(definition2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Introduisons maintenant la saponification. Retenons sa "
                "définition : c'est l'hydrolyse basique d'un ester, "
                "réalisée par les ions hydroxyde, HO moins, en général "
                "apportés par la soude. Son équation s'écrit R-C-O-O-R' "
                "plus HO moins, donnant R-C-O-O moins plus R'-O-H. Et "
                "surtout : cette réaction est totale, elle ne s'arrête "
                "pas à un équilibre."
            )
        ) as tracker:
            self.play(FadeIn(definition2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition2))

        piege = warning_box(
            Text(
                _wrap(
                    "Différence capitale : l'ion carboxylate R-COO⁻ formé "
                    "(base conjuguée, chargée négativement) ne peut PAS "
                    "régénérer l'ester — l'estérification exige l'acide "
                    "neutre R-COOH, pas sa base conjuguée. D'où une "
                    "flèche SIMPLE (→), et non double (⇌), pour la "
                    "saponification.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici la différence capitale à bien retenir : l'ion "
                "carboxylate formé, R-C-O-O moins, est la base conjuguée "
                "de l'acide, chargée négativement. Il ne peut absolument "
                "pas régénérer l'ester, car l'estérification exige "
                "l'acide carboxylique neutre, et non sa base conjuguée. "
                "C'est pourquoi la saponification s'écrit avec une "
                "flèche simple, et non une double flèche : c'est une "
                "réaction totale, irréversible dans les conditions "
                "usuelles."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- Application : fabrication des savons -------------------------------------
        entete2 = Text("Application : la fabrication des savons", font_size=22, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        eq_savon = Text(
            "triester du glycérol (corps gras) + soude → glycérol + carboxylate de sodium",
            font_size=17,
            color=WHITE,
        )
        eq_savon.next_to(entete2, DOWN, buff=0.3)

        # Schéma simplifié d'un ion amphiphile : tête hydrophile + queue hydrophobe
        tete = Circle(radius=0.22, color=BLUE, fill_color=BLUE, fill_opacity=1)
        queue = Line(start=tete.get_center() + [0.22, 0, 0], end=tete.get_center() + [2.3, 0, 0], color=RED, stroke_width=6)
        tete.move_to(queue.get_start())
        schema = VGroup(queue, tete)
        label_tete = Text("tête hydrophile (COO⁻)", font_size=16, color=BLUE).next_to(tete, LEFT, buff=0.2)
        label_queue = Text("queue hydrophobe (chaîne carbonée)", font_size=16, color=RED).next_to(queue, RIGHT, buff=0.2)
        schema_complet = VGroup(schema, label_tete, label_queue)
        schema_complet.next_to(eq_savon, DOWN, buff=0.5)

        groupe2 = VGroup(entete2, eq_savon, schema_complet)
        _fit(groupe2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "L'application la plus célèbre de la saponification est "
                "la fabrication des savons : un triester du glycérol, "
                "c'est-à-dire un corps gras comme une huile ou une "
                "graisse, réagit avec la soude pour donner du glycérol "
                "et un carboxylate de sodium, c'est-à-dire le savon "
                "lui-même. L'ion carboxylate obtenu est une molécule "
                "amphiphile : une tête hydrophile, chargée, qui aime "
                "l'eau, et une longue queue hydrophobe, une chaîne "
                "carbonée, qui la fuit. C'est cette double affinité qui "
                "donne au savon sa propriété détersive, en permettant "
                "d'emprisonner les graisses dans des micelles."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(eq_savon))
            self.play(FadeIn(schema_complet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2), FadeOut(titre))
