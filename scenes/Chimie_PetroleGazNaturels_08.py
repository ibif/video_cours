"""
scenes/Chimie_PetroleGazNaturels_08.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 08.

§ 8. Les enjeux environnementaux : pollutions liées à l'exploitation
(marées noires, pollution des sols/nappes, torchage du gaz associé) et à
la combustion (équation de combustion de l'octane, effet de serre du
CO₂, toxicité du CO de la combustion incomplète, SOₓ et pluies acides,
NOₓ et smog). Ressource non renouvelable, alternatives (énergies
renouvelables, bioéthanol, recyclage).
Source : 1ereC/Chimie.pdf, chapitre 5, page 52-53.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
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
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LesEnjeuxEnvironnementaux(NotionScene):
    def construct(self):
        titre = scene_title("8. Les enjeux environnementaux")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : deux sources de pollution ----------------------------------
        intro = Text(
            _wrap(
                "L'exploitation du pétrole et du gaz naturel a un coût "
                "environnemental important, à deux moments : lors de "
                "leur extraction, et lors de leur combustion.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'exploitation du pétrole et du gaz naturel a un coût "
                "environnemental important, à deux moments distincts : "
                "d'abord lors de leur extraction, ensuite lors de leur "
                "combustion."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : pollutions liées à l'exploitation --------------------
        entete_exploit = Text("Pollutions liées à l'exploitation", font_size=23, color=YELLOW, weight="BOLD")
        entete_exploit.next_to(titre, DOWN, buff=0.35)

        exploit = _bullets(
            [
                "Marées noires : déversements accidentels en mer, lors de "
                "l'extraction ou du transport",
                "Pollution des sols et des nappes phréatiques autour des "
                "sites d'exploitation et de raffinage",
                "Torchage du gaz associé : brûlage à l'air libre du gaz "
                "naturel extrait avec le pétrole, faute de valorisation",
            ],
            font_size=19,
            width=50,
        )
        exploit.next_to(entete_exploit, DOWN, buff=0.35)
        _fit(exploit, entete_exploit.get_bottom()[1] - 0.25)

        groupe_exploit = VGroup(entete_exploit, exploit)

        with self.voiceover(
            text=(
                "L'exploitation elle-même génère trois types de "
                "pollutions. Les marées noires, d'abord : des "
                "déversements accidentels en mer, lors de l'extraction ou "
                "du transport par pétrolier. La pollution des sols et des "
                "nappes phréatiques, ensuite, autour des sites "
                "d'exploitation et de raffinage. Et enfin le torchage du "
                "gaz associé : ce gaz naturel extrait en même temps que "
                "le pétrole est parfois brûlé à l'air libre, faute de "
                "pouvoir être valorisé, ce qui gaspille une ressource et "
                "pollue l'atmosphère."
            )
        ) as tracker:
            self.play(FadeIn(entete_exploit))
            self.play(FadeIn(exploit))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_exploit))

        # --- Exemple traité : équation de la combustion de l'octane -------------
        entete_combustion = Text("La combustion : l'exemple de l'octane", font_size=23, color=YELLOW, weight="BOLD")
        entete_combustion.next_to(titre, DOWN, buff=0.35)

        equation_combustion = MathTex(
            r"2\,C_8H_{18} + 25\,O_2 \;\rightarrow\; 16\,CO_2 + 18\,H_2O",
            font_size=30,
            color=WHITE,
        )
        equation_combustion.next_to(entete_combustion, DOWN, buff=0.45)

        groupe_combustion = VGroup(entete_combustion, equation_combustion)

        with self.voiceover(
            text=(
                "Prenons l'exemple de la combustion complète de "
                "l'octane, un constituant de l'essence : deux C-huit "
                "H-dix-huit, plus vingt-cinq O-deux, donnent seize C-O-"
                "deux, plus dix-huit H-deux-O. Cette combustion, bien que "
                "libérant de l'énergie utile, a plusieurs conséquences "
                "néfastes sur l'environnement."
            )
        ) as tracker:
            self.play(FadeIn(entete_combustion))
            self.play(Write(equation_combustion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_combustion))

        # --- Exemple traité : conséquences de la combustion ----------------------
        consequences = _bullets(
            [
                "CO₂ : gaz à effet de serre, responsable du réchauffement "
                "climatique",
                "CO (monoxyde de carbone) : gaz toxique, produit lors "
                "d'une combustion incomplète",
                "SOₓ (oxydes de soufre) : à l'origine des pluies acides",
                "NOₓ (oxydes d'azote) : contribuent au smog urbain",
            ],
            font_size=19,
            width=50,
        )
        consequences.next_to(titre, DOWN, buff=0.5)
        _fit(consequences, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Le dioxyde de carbone, C-O-deux, est un gaz à effet de "
                "serre, responsable du réchauffement climatique. Le "
                "monoxyde de carbone, C-O, gaz toxique, apparaît lors "
                "d'une combustion incomplète, en l'absence d'oxygène "
                "suffisant. Les oxydes de soufre, notés S-O-x, sont à "
                "l'origine des pluies acides. Et les oxydes d'azote, "
                "notés N-O-x, contribuent au smog urbain, ce brouillard "
                "de pollution qui affecte de nombreuses grandes villes."
            )
        ) as tracker:
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequences))

        # --- À retenir : ressource non renouvelable et alternatives -------------
        alternatives = property_box(
            _bullets(
                [
                    "Le pétrole et le gaz sont des ressources épuisables",
                    "Alternatives : énergies renouvelables (solaire, "
                    "éolien, hydraulique)",
                    "Le bioéthanol, carburant issu de la biomasse",
                    "Le recyclage des matières plastiques issues de la "
                    "pétrochimie",
                ],
                font_size=19,
                width=48,
            ),
            box_width=11.0,
        )
        alternatives.next_to(titre, DOWN, buff=0.5)
        _fit(alternatives, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons enfin que le pétrole et le gaz naturel restent "
                "des ressources non renouvelables et épuisables. Plusieurs "
                "alternatives se développent : les énergies renouvelables, "
                "solaire, éolienne, hydraulique ; le bioéthanol, un "
                "carburant issu de la biomasse végétale ; et le recyclage "
                "des matières plastiques issues de la pétrochimie."
            )
        ) as tracker:
            self.play(FadeIn(alternatives))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(alternatives))

        # --- Piège à éviter : gaz à effet de serre pas forcément toxique -------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas les deux effets du CO₂ et du CO : le "
                    "CO₂ n'est pas toxique par inhalation à faible dose "
                    "mais réchauffe le climat, tandis que le CO est un "
                    "poison direct, même à faible concentration, car il "
                    "se fixe sur l'hémoglobine du sang.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre les deux effets du C-O-deux "
                "et du C-O. Le dioxyde de carbone n'est pas toxique par "
                "inhalation à faible dose, mais il réchauffe le climat à "
                "l'échelle planétaire. Le monoxyde de carbone, lui, est "
                "un poison direct, même à faible concentration, car il se "
                "fixe sur l'hémoglobine du sang et empêche le transport "
                "de l'oxygène."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
