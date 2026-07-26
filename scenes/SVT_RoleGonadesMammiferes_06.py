"""
scenes/SVT_RoleGonadesMammiferes_06.py — Chapitre 1 (1ereC, SVT), scène 06.

Structure et ultrastructure de l'ovaire : épithélium ovarien, zone
corticale, follicules ovariens à différents stades (primordial, primaire,
secondaire, tertiaire/De Graaf), corps jaune, ovocytes.
Source : 1ereC/SVT.pdf, page 10.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Ellipse,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class StructureUltrastructureOvaire(NotionScene):
    def construct(self):
        titre = scene_title("1.6 — Structure de l'ovaire")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : structure générale ---------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'ovaire est entouré d'un épithélium ovarien et "
                    "contient, dans sa zone corticale, de nombreux "
                    "follicules ovariens à différents stades de "
                    "développement ; chaque follicule contient un ovocyte.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'ovaire est entouré d'un épithélium ovarien et contient, "
                "dans sa zone corticale, c'est-à-dire sa région externe, de "
                "nombreux follicules ovariens à différents stades de "
                "développement. Chaque follicule contient un ovocyte."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : les stades des follicules -------------
        ovaire = Ellipse(width=8.0, height=3.3, color=WHITE, stroke_width=3)
        ovaire.next_to(titre, DOWN, buff=0.6)
        epithelium_lbl = Text("épithélium ovarien", font_size=14, color=WHITE).next_to(
            ovaire, UP, buff=0.15
        )

        f_primordial = Circle(radius=0.16, color="#DE7C1F", fill_opacity=0.9).move_to(
            ovaire.get_center() + LEFT * 2.9 + UP * 0.5
        )
        f_primaire = Circle(radius=0.28, color="#DE7C1F", fill_opacity=0.9).move_to(
            ovaire.get_center() + LEFT * 1.6 + UP * 0.8
        )
        f_secondaire = Circle(radius=0.42, color="#DE7C1F", fill_opacity=0.9).move_to(
            ovaire.get_center() + LEFT * 0.1 + UP * 0.6
        )
        f_mur = Circle(radius=0.6, color=YELLOW, fill_opacity=0.9).move_to(
            ovaire.get_center() + RIGHT * 1.7 + UP * 0.3
        )
        corps_jaune = Circle(radius=0.55, color="#288073", fill_opacity=0.9).move_to(
            ovaire.get_center() + RIGHT * 2.9 + DOWN * 0.8
        )

        follicules = VGroup(f_primordial, f_primaire, f_secondaire, f_mur)

        labels = VGroup(
            Text("primordial", font_size=13, color=WHITE).next_to(f_primordial, DOWN, buff=0.15),
            Text("primaire", font_size=13, color=WHITE).next_to(f_primaire, UP, buff=0.15),
            Text("secondaire", font_size=13, color=WHITE).next_to(f_secondaire, UP, buff=0.15),
            Text("mûr (De Graaf)", font_size=13, color=WHITE).next_to(f_mur, UP, buff=0.15),
            Text("corps jaune", font_size=13, color=WHITE).next_to(corps_jaune, DOWN, buff=0.15),
        )

        schema = VGroup(ovaire, epithelium_lbl, follicules, corps_jaune, labels)

        with self.voiceover(
            text=(
                "Suivons la maturation d'un follicule dans la zone "
                "corticale de l'ovaire. Il naît follicule primordial, de "
                "très petite taille, puis grossit en follicule primaire, "
                "puis en follicule secondaire, avant de devenir un "
                "follicule mûr, dit follicule de De Graaf, prêt pour "
                "l'ovulation. Après l'ovulation, ce qui reste du follicule "
                "rompu se transforme en corps jaune."
            )
        ) as tracker:
            self.play(FadeIn(ovaire), FadeIn(epithelium_lbl))
            self.play(FadeIn(f_primordial), FadeIn(labels[0]))
            self.play(FadeIn(f_primaire), FadeIn(labels[1]))
            self.play(FadeIn(f_secondaire), FadeIn(labels[2]))
            self.play(FadeIn(f_mur), FadeIn(labels[3]))
            self.play(FadeIn(corps_jaune), FadeIn(labels[4]))
            self.wait(tracker.get_remaining_duration())

        # --- Exemple traité : de l'ovulation au corps jaune ---------------------
        exemple_lbl = Text("Après l'ovulation...", font_size=20, color=YELLOW, weight="BOLD")
        exemple_lbl.next_to(schema, DOWN, buff=0.35)

        exemple = Text(
            _wrap(
                "Le follicule de De Graaf libère l'ovocyte : c'est "
                "l'ovulation. Le follicule rompu se transforme alors en "
                "corps jaune, une structure endocrine TEMPORAIRE qui "
                "sécrète la progestérone.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        exemple.next_to(exemple_lbl, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Prenons l'exemple de ce qui se passe après l'ovulation : le "
                "follicule de De Graaf libère son ovocyte, c'est "
                "l'ovulation. Le follicule rompu se transforme alors en "
                "corps jaune, une structure endocrine temporaire qui "
                "sécrète la progestérone, une hormone essentielle en cas de "
                "grossesse."
            )
        ) as tracker:
            self.play(FadeIn(exemple_lbl), FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(exemple_lbl), FadeOut(exemple))

        # --- À retenir : le corps jaune, structure endocrine temporaire --------
        retenir = property_box(
            Text(
                _wrap(
                    "Le corps jaune est une structure endocrine TEMPORAIRE : "
                    "il sécrète la progestérone après l'ovulation, mais "
                    "régresse (en corps blanc) en l'absence de "
                    "fécondation, avant qu'un nouveau cycle ne commence.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons que le corps jaune est une structure endocrine "
                "temporaire : il sécrète la progestérone après "
                "l'ovulation, mais il régresse en l'absence de "
                "fécondation, avant qu'un nouveau cycle ne recommence."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas le FOLLICULE (la structure qui entoure "
                    "et nourrit) avec l'OVOCYTE (la cellule reproductrice "
                    "qu'il contient) : un follicule n'est pas un gamète, "
                    "c'est son enveloppe protectrice et nourricière.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre le follicule, la structure qui "
                "entoure et nourrit, avec l'ovocyte, la cellule "
                "reproductrice qu'il contient : un follicule n'est pas un "
                "gamète, c'est son enveloppe protectrice et nourricière."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
