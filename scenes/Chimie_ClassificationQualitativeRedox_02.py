"""
scenes/Chimie_ClassificationQualitativeRedox_02.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 02.

§ 1 (suite). Définitions de l'oxydant et du réducteur les plus forts,
théorème : une réaction d'oxydoréduction spontanée met en jeu l'oxydant le
plus fort et le réducteur le plus fort présents dans le milieu (schéma
Ox fort + Red fort → Red faible + Ox faible). Exemple résolu 1 : le zinc
plongé dans une solution de sulfate de cuivre.
Source : 1ereC/Chimie.pdf, chapitre 10, page 95.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ForceOxydantsReducteursDefinitions(NotionScene):
    def construct(self):
        titre = scene_title("10.1 Force des oxydants et réducteurs — définitions")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé ----------------------------------------------------------
        intro = Text(
            _wrap(
                "L'expérience précédente montre que certains oxydants ou "
                "réducteurs sont « plus forts » que d'autres. Précisons ces "
                "notions, puis énonçons le théorème qui permet de prévoir "
                "le sens d'une réaction spontanée.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'expérience précédente montre que certains oxydants ou "
                "réducteurs sont plus forts que d'autres. Précisons ces "
                "notions, puis énonçons le théorème qui permet de prévoir "
                "le sens d'une réaction spontanée entre un métal et des "
                "ions métalliques."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définitions ---------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Parmi plusieurs oxydants, le plus fort est celui qui "
                        "capte le plus facilement des électrons (celui qui "
                        "réagit effectivement).",
                        width=48,
                    ),
                    font_size=21,
                ),
                Text(
                    _wrap(
                        "Parmi plusieurs réducteurs, le plus fort est celui "
                        "qui cède le plus facilement des électrons (celui "
                        "qui s'oxyde effectivement).",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Définition : parmi plusieurs oxydants en présence, le plus "
                "fort est celui qui capte le plus facilement des électrons, "
                "c'est-à-dire celui qui réagit effectivement. Parmi "
                "plusieurs réducteurs en présence, le plus fort est celui "
                "qui cède le plus facilement des électrons, c'est-à-dire "
                "celui qui s'oxyde effectivement."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Théorème ----------------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text(
                    "Une réaction d'oxydoréduction spontanée met toujours en jeu",
                    font_size=21,
                ),
                Text(
                    "l'oxydant le plus fort et le réducteur le plus fort présents.",
                    font_size=21,
                ),
                MathTex(
                    r"Ox_{fort} + Red_{fort} \longrightarrow Red_{faible} + Ox_{faible}",
                    font_size=27,
                    color=ORANGE,
                ),
            ).arrange(DOWN, buff=0.32),
            box_width=12.4,
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Théorème : une réaction d'oxydoréduction spontanée met "
                "toujours en jeu l'oxydant le plus fort et le réducteur le "
                "plus fort présents dans le milieu. On l'écrit sous forme "
                "générale : oxydant fort, plus réducteur fort, donne "
                "réducteur faible, plus oxydant faible. L'oxydant fort "
                "capte les électrons cédés par le réducteur fort."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 1 : zinc dans sulfate de cuivre --------------------
        entete_ex = Text("Exemple résolu 1 — Zinc dans une solution de sulfate de cuivre", font_size=21, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.35)

        couples = MathTex(
            r"Cu^{2+}/Cu \quad\text{et}\quad Zn^{2+}/Zn",
            font_size=27, color=WHITE,
        )
        raisonnement = Text(
            _wrap(
                "Le zinc est plus réducteur que le cuivre : le zinc (Red fort) "
                "réagit avec Cu²⁺ (Ox fort).",
                width=50,
            ),
            font_size=21, color=WHITE,
        )
        bilan = MathTex(r"Zn + Cu^{2+} \longrightarrow Zn^{2+} + Cu", font_size=28, color=ORANGE)
        observation = Text("Observation : dépôt rouge-orangé de cuivre sur le zinc.", font_size=20, color=WHITE)

        contenu_ex = VGroup(couples, raisonnement, bilan, observation).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        contenu_ex.next_to(entete_ex, DOWN, buff=0.4)
        groupe_ex = VGroup(entete_ex, contenu_ex)
        _fit(groupe_ex, titre.get_bottom()[1] - 0.2)
        groupe_ex.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Appliquons ce théorème. On plonge une lame de zinc dans "
                "une solution de sulfate de cuivre deux : les couples en "
                "présence sont cuivre deux plus sur cuivre, et zinc deux "
                "plus sur zinc. Le zinc est plus réducteur que le cuivre, "
                "c'est donc le réducteur fort ; les ions cuivre deux sont "
                "l'oxydant fort. La réaction spontanée est donc : zinc, "
                "plus cuivre deux plus, donne zinc deux plus, plus cuivre. "
                "On observe effectivement un dépôt rouge-orangé de cuivre "
                "sur la lame de zinc."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(couples))
            self.play(FadeIn(raisonnement))
            self.play(Write(bilan))
            self.play(FadeIn(observation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_ex))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Si les espèces en présence ne sont ni l'oxydant le plus "
                    "fort ni le réducteur le plus fort du milieu (par exemple "
                    "Cu plongé dans Fe²⁺), aucune réaction spontanée ne se "
                    "produit : le théorème n'autorise pas l'inverse.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : si les espèces en présence ne sont ni "
                "l'oxydant le plus fort, ni le réducteur le plus fort du "
                "milieu — par exemple du cuivre plongé dans une solution "
                "d'ions fer deux — aucune réaction spontanée ne se produit. "
                "Le théorème ne fonctionne que dans le sens oxydant fort "
                "plus réducteur fort, jamais dans l'autre sens."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
