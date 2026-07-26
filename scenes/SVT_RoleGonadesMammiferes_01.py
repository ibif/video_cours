"""
scenes/SVT_RoleGonadesMammiferes_01.py — Chapitre 1 (1ereC, SVT), scène 01.

Introduction du chapitre « Le rôle et la structure des gonades des
mammifères » : contexte de la reproduction, double rôle exocrine/endocrine
des gonades, définition de « gonade », objectifs du chapitre.
Source : 1ereC/SVT.pdf, pages 4-5 (pages imprimées).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


class IntroductionRoleGonadesMammiferes(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 1 — Le rôle et la structure des gonades")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : le contexte de la reproduction ------------------------
        contexte = Text(
            _wrap(
                "La reproduction est un phénomène biologique fondamental qui "
                "assure la pérennité des espèces. Chez les mammifères, elle "
                "fait intervenir des organes spécialisés appelés gonades.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        contexte.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La reproduction est un phénomène biologique fondamental qui "
                "assure la pérennité des espèces, c'est-à-dire leur "
                "continuité dans le temps. Chez les mammifères, elle fait "
                "intervenir des organes spécialisés, appelés gonades, que "
                "nous allons étudier tout au long de ce chapitre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(contexte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(contexte))

        # --- Animation du raisonnement : le double rôle des gonades ---------
        gonade = Circle(radius=0.7, color=YELLOW, fill_opacity=0.85)
        gonade.next_to(titre, DOWN, buff=1.0)
        gonade_label = Text("GONADE", font_size=20, color=WHITE, weight="BOLD")
        gonade_label.move_to(gonade.get_center())

        fleche_exo = Arrow(
            gonade.get_left(), gonade.get_left() + LEFT * 3.2, color=WHITE, buff=0.2
        )
        gametes = Circle(radius=0.5, color="#288073", fill_opacity=0.85)
        gametes.next_to(fleche_exo, LEFT, buff=0.1)
        gametes_label = Text("gamètes", font_size=18, color=WHITE)
        gametes_label.next_to(gametes, DOWN, buff=0.15)
        exo_label = Text("rôle EXOCRINE", font_size=18, color="#288073", weight="BOLD")
        exo_label.next_to(fleche_exo, UP, buff=0.1)

        fleche_endo = Arrow(
            gonade.get_right(), gonade.get_right() + RIGHT * 3.2, color=WHITE, buff=0.2
        )
        hormones = Circle(radius=0.5, color="#B42E41", fill_opacity=0.85)
        hormones.next_to(fleche_endo, RIGHT, buff=0.1)
        hormones_label = Text("hormones", font_size=18, color=WHITE)
        hormones_label.next_to(hormones, DOWN, buff=0.15)
        endo_label = Text("rôle ENDOCRINE", font_size=18, color="#B42E41", weight="BOLD")
        endo_label.next_to(fleche_endo, UP, buff=0.1)

        schema = VGroup(
            gonade, gonade_label,
            fleche_exo, gametes, gametes_label, exo_label,
            fleche_endo, hormones, hormones_label, endo_label,
        )

        with self.voiceover(
            text=(
                "Ces organes ont un rôle double. D'une part, un rôle "
                "exocrine : la gonade produit des gamètes, c'est-à-dire des "
                "spermatozoïdes chez le mâle et des ovules chez la femelle, "
                "libérés dans des conduits. D'autre part, un rôle endocrine : "
                "la gonade sécrète des hormones sexuelles, directement dans "
                "le sang."
            )
        ) as tracker:
            self.play(FadeIn(gonade), FadeIn(gonade_label))
            self.play(FadeIn(fleche_exo), FadeIn(gametes), FadeIn(gametes_label), FadeIn(exo_label))
            self.play(FadeIn(fleche_endo), FadeIn(hormones), FadeIn(hormones_label), FadeIn(endo_label))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : testicule et ovaire, deux gonades -------------
        exemple = _bullets(
            [
                "Chez le mâle, la gonade est le testicule : il produit les "
                "spermatozoïdes (exocrine) et la testostérone (endocrine).",
                "Chez la femelle, la gonade est l'ovaire : il produit les "
                "ovules (exocrine) et les œstrogènes/progestérone (endocrine).",
            ],
            font_size=23,
            width=52,
        )
        exemple.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Deux exemples concrets. Chez le mâle, la gonade est le "
                "testicule : il produit les spermatozoïdes, c'est le rôle "
                "exocrine, et il sécrète la testostérone, c'est le rôle "
                "endocrine. Chez la femelle, la gonade est l'ovaire : il "
                "produit les ovules, rôle exocrine, et il sécrète les "
                "œstrogènes et la progestérone, rôle endocrine."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : définition de la gonade + objectifs -----------------
        definition = definition_box(
            Text(
                _wrap(
                    "La gonade est l'organe reproducteur primaire qui produit "
                    "les gamètes et les hormones sexuelles. Chez le mâle, il "
                    "s'agit des testicules ; chez la femelle, des ovaires.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Retenons la définition : la gonade est l'organe reproducteur "
                "primaire qui produit à la fois les gamètes et les hormones "
                "sexuelles. Chez le mâle, il s'agit des testicules ; chez la "
                "femelle, des ovaires. Ce chapitre a pour objectifs de "
                "déterminer ce double rôle à partir de résultats "
                "expérimentaux, d'annoter les schémas des appareils "
                "reproducteurs et des coupes de gonades, de décrire la "
                "structure du testicule et de l'ovaire, et de distinguer les "
                "caractères sexuels primaires des caractères secondaires."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas « gonade » (l'organe : testicule ou "
                    "ovaire) et « gamète » (la cellule produite par cet "
                    "organe : spermatozoïde ou ovule). La gonade produit le "
                    "gamète, elle n'EST pas le gamète.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre gonade et gamète : la gonade "
                "est l'organe, le testicule ou l'ovaire ; le gamète est la "
                "cellule que cet organe produit, le spermatozoïde ou "
                "l'ovule. La gonade produit le gamète, elle n'est pas "
                "elle-même le gamète."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
