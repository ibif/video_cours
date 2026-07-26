"""
scenes/Chimie_CorrosionProtectionMetaux_04.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 04.

§ 4. Nature de la rouille. definition_box de la rouille (Fe2O3, x H2O,
brun roux), propriétés physiques (poreuse, friable, non adhérente, ne
protège pas le métal sous-jacent) contrastées avec l'alumine (Al) et les
oxydes de zinc / chrome, compacts et adhérents.
Source : 1ereC/Chimie.pdf, chapitre 15, page 147.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    RED,
    FadeIn,
    FadeOut,
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


def _bullets(items, font_size=22, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


class NatureDeLaRouille(NotionScene):
    def construct(self):
        titre = scene_title("15.4 Nature de la rouille")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : formule et définition -------------------------------------
        definition = definition_box(
            VGroup(
                Text("La rouille est un composé de formule :", font_size=23),
                MathTex(r"Fe_2O_3, x\,H_2O", font_size=32),
                Text("(oxyde de fer III hydraté), de couleur brun roux.", font_size=21),
            ).arrange(DOWN, buff=0.3),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La rouille formée sur le fer est un composé bien "
                "défini : de l'oxyde de fer trois hydraté, de formule "
                "F-e-deux-O-trois, x fois H-deux-O, où x représente un "
                "nombre variable de molécules d'eau. Sa couleur "
                "caractéristique est le brun roux."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : propriétés physiques de la rouille -------------------
        entete_prop = Text("Les propriétés physiques de la rouille", font_size=22, color=YELLOW, weight="BOLD")
        entete_prop.next_to(titre, DOWN, buff=0.35)

        proprietes = _bullets(
            [
                "poreuse : laisse passer l'eau et l'air",
                "friable : s'effrite et se détache facilement",
                "non adhérente : ne reste pas solidement fixée au métal",
            ],
            font_size=21,
            color=RED,
        )
        proprietes.next_to(entete_prop, DOWN, buff=0.35)
        groupe_prop = VGroup(entete_prop, proprietes)

        with self.voiceover(
            text=(
                "Ce qui rend la rouille si dangereuse pour le fer, ce "
                "sont ses propriétés physiques. Elle est poreuse : l'eau "
                "et l'air continuent de la traverser. Elle est friable : "
                "elle s'effrite et se détache facilement. Elle est non "
                "adhérente : elle ne reste pas solidement fixée à la "
                "surface du métal."
            )
        ) as tracker:
            self.play(FadeIn(entete_prop))
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_prop))

        # --- Exemple traité : comparaison avec l'alumine et les autres oxydes ---
        entete_comp = Text("Comparaison : l'alumine, elle, protège l'aluminium", font_size=20, color=YELLOW, weight="BOLD")
        entete_comp.next_to(titre, DOWN, buff=0.35)

        comparaison = _bullets(
            [
                "alumine (Al2O3) sur l'aluminium : compacte, adhérente → couche protectrice",
                "oxydes de zinc / de chrome : compacts et adhérents → protecteurs",
                "rouille (Fe2O3, xH2O) sur le fer : poreuse, non adhérente → NE protège PAS",
            ],
            font_size=19,
            color=GREEN,
        )
        comparaison[2].set_color(RED)
        comparaison.next_to(entete_comp, DOWN, buff=0.35)
        groupe_comp = VGroup(entete_comp, comparaison)
        _fit(groupe_comp, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Comparons avec d'autres métaux. Sur l'aluminium, "
                "l'alumine qui se forme est compacte et adhérente : elle "
                "constitue une couche protectrice qui empêche l'oxydation "
                "de se poursuivre en profondeur. De même, les oxydes de "
                "zinc ou de chrome sont compacts et adhérents, donc "
                "protecteurs. La rouille du fer, elle, ne protège "
                "absolument pas le métal, puisqu'elle est poreuse et non "
                "adhérente : l'eau et l'air continuent d'attaquer le fer "
                "sous la couche de rouille, qui s'épaissit sans jamais "
                "s'arrêter."
            )
        ) as tracker:
            self.play(FadeIn(entete_comp))
            self.play(FadeIn(comparaison))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_comp))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Une couche d'oxyde n'est pas automatiquement "
                    "protectrice : tout dépend de sa structure (poreuse "
                    "ou compacte, adhérente ou non). C'est précisément "
                    "l'absence de protection de la rouille qui rend le "
                    "fer si vulnérable, contrairement à l'aluminium.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Retenons bien ce piège classique : une couche d'oxyde "
                "n'est pas automatiquement protectrice. Tout dépend de "
                "sa structure, poreuse ou compacte, adhérente ou non. "
                "C'est précisément cette absence de protection de la "
                "rouille qui rend le fer si vulnérable à la corrosion, "
                "contrairement à l'aluminium qui, lui, s'auto-protège."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
