"""
scenes/SVT_TectoniquePlaques_08.py — Chapitre 8 (1ereC, SVT), scène 08.

IV.A Les frontières divergentes — les dorsales : mécanisme (écartement,
décompression, fusion partielle, magma basaltique, volcanisme effusif,
accrétion océanique), structures associées, exemples (dorsale
médio-atlantique, Islande) + le rift continental (stade embryonnaire d'un
océan, rift est-africain, stades d'ouverture). Source : 1ereC/SVT.pdf,
pages 89-90.
"""

import textwrap

from manim import (
    BLUE_E,
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class FrontieresDivergentesDorsales(NotionScene):
    def construct(self):
        titre = scene_title("IV.A Les frontières divergentes : les dorsales")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : le mécanisme --------------------------------------------
        mecanisme = _bullets(
            [
                "Les deux plaques s'écartent : l'asthénosphère remonte "
                "entre elles et subit une décompression qui provoque sa "
                "fusion partielle.",
                "Le magma produit est basaltique (pauvre en silice, "
                "fluide) : il alimente un volcanisme effusif et fabrique "
                "la nouvelle croûte océanique — l'accrétion océanique.",
            ],
            font_size=22,
            width=52,
        )
        mecanisme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Au niveau d'une dorsale, les deux plaques s'écartent : "
                "l'asthénosphère remonte entre elles et subit une "
                "décompression, ce qui provoque sa fusion partielle. Le "
                "magma produit est basaltique, pauvre en silice, donc "
                "fluide : il alimente un volcanisme effusif, et fabrique la "
                "nouvelle croûte océanique. C'est l'accrétion océanique."
            )
        ) as tracker:
            self.play(FadeIn(mecanisme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mecanisme))

        # --- Animation du raisonnement : schéma d'une dorsale détaillé -------
        ocean = Rectangle(width=9.0, height=1.3, fill_color=BLUE_E, fill_opacity=0.5, stroke_width=0)
        flanc_g = Polygon(
            [-4.5, -0.65, 0], [-0.6, -0.65, 0], [-0.15, 0.5, 0], [-4.5, 0.15, 0],
            fill_color=ORANGE, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1,
        )
        flanc_d = Polygon(
            [4.5, -0.65, 0], [0.6, -0.65, 0], [0.15, 0.5, 0], [4.5, 0.15, 0],
            fill_color=ORANGE, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1,
        )
        rift = Polygon(
            [-0.6, -0.65, 0], [0.6, -0.65, 0], [0.15, 0.5, 0], [-0.15, 0.5, 0],
            fill_color=RED, fill_opacity=0.85, stroke_color=WHITE, stroke_width=1,
        )
        magma = Arrow(start=[0, -1.5, 0], end=[0, -0.3, 0], color=RED, buff=0, stroke_width=4)
        fleche_g = Arrow(start=[-0.5, 0.0, 0], end=[-2.2, 0.0, 0], color=WHITE, buff=0, stroke_width=3)
        fleche_d = Arrow(start=[0.5, 0.0, 0], end=[2.2, 0.0, 0], color=WHITE, buff=0, stroke_width=3)

        fumeur_g = Dot(point=[-0.35, 0.55, 0], radius=0.06, color=YELLOW)
        fumeur_d = Dot(point=[0.35, 0.55, 0], radius=0.06, color=YELLOW)
        label_fumeurs = Text("fumeurs noirs", font_size=14, color=YELLOW).next_to(fumeur_d, RIGHT, buff=0.15)

        label_rift = Text("rift (vallée axiale)", font_size=15, color=WHITE).next_to(rift, UP, buff=0.55)
        label_faille = Text("failles normales", font_size=14, color=WHITE).move_to([-2.5, 0.35, 0])

        schema = VGroup(
            ocean, flanc_g, flanc_d, rift, magma, fleche_g, fleche_d,
            fumeur_g, fumeur_d, label_fumeurs, label_rift, label_faille,
        )
        schema.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Les structures associées à une dorsale : une ride "
                "surélevée, une vallée axiale appelée rift, bordée de "
                "failles normales ; des séismes superficiels, de moins de "
                "trente kilomètres de profondeur, de faible magnitude ; et "
                "des sources hydrothermales, les fameux fumeurs noirs, où "
                "l'eau de mer, réchauffée par le magma, ressort chargée de "
                "minéraux."
            )
        ) as tracker:
            self.play(FadeIn(ocean))
            self.play(Create(flanc_g), Create(flanc_d), Create(rift), FadeIn(label_rift), FadeIn(label_faille))
            self.play(Create(magma), Create(fleche_g), Create(fleche_d))
            self.play(FadeIn(fumeur_g), FadeIn(fumeur_d), FadeIn(label_fumeurs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : dorsale médio-atlantique et Islande -----------
        exemples = _bullets(
            [
                "Dorsale médio-atlantique (entre les plaques africaine et "
                "américaines) et dorsale Est-Pacifique.",
                "Islande : portion émergée de la dorsale médio-atlantique, "
                "où le volcanisme basaltique et le rift sont directement "
                "visibles à la surface.",
            ],
            font_size=22,
            width=52,
        )
        exemples.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deux exemples à connaître : la dorsale médio-atlantique, "
                "entre les plaques africaine et américaines, et la dorsale "
                "Est-Pacifique. L'Islande, elle, est une portion émergée de "
                "la dorsale médio-atlantique : on peut y observer "
                "directement, à l'air libre, le volcanisme basaltique et le "
                "rift."
            )
        ) as tracker:
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples))

        # --- À retenir : le rift continental, stade embryonnaire d'un océan --
        entete_rift = Text("Le rift continental : un océan en formation", font_size=23, color=YELLOW, weight="BOLD")
        entete_rift.next_to(titre, DOWN, buff=0.5)

        rift_texte = _bullets(
            [
                "Lorsque la divergence débute à l'intérieur d'un continent, "
                "celui-ci s'amincit et s'effondre en fossés (grabens) "
                "bordés de failles normales.",
                "Le rift est-africain (Afars, lacs Tanganyika et Malawi, "
                "volcans Kilimandjaro et Nyiragongo) est un océan en "
                "formation : à terme, l'Afrique de l'Est se séparera du "
                "reste du continent.",
                "Stades d'ouverture : rift continental → mer étroite (mer "
                "Rouge) → océan mature (Atlantique).",
            ],
            font_size=20,
            width=52,
        )
        rift_texte.next_to(entete_rift, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Un dernier point essentiel : le rift continental, stade "
                "embryonnaire d'un océan. Lorsque la divergence débute à "
                "l'intérieur d'un continent, celui-ci s'amincit et "
                "s'effondre en fossés, appelés grabens, bordés de failles "
                "normales. Le rift est-africain, avec la région des Afars, "
                "les lacs Tanganyika et Malawi, et les volcans Kilimandjaro "
                "et Nyiragongo, est un océan en formation : à terme, "
                "l'Afrique de l'Est se séparera du reste du continent. Les "
                "stades d'ouverture d'un océan sont donc : rift "
                "continental, puis mer étroite, comme la mer Rouge "
                "aujourd'hui, puis océan mature, comme l'Atlantique."
            )
        ) as tracker:
            self.play(FadeIn(entete_rift))
            self.play(FadeIn(rift_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_rift), FadeOut(rift_texte))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre : un rift continental (fossé "
                    "d'effondrement, encore sur un continent, comme l'Afrique "
                    "de l'Est) et une dorsale océanique (déjà séparatrice de "
                    "deux plaques océaniques, comme l'Atlantique). Le premier "
                    "deviendra la seconde, dans des dizaines de millions "
                    "d'années.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre un rift continental, encore "
                "situé sur un continent, comme en Afrique de l'Est "
                "aujourd'hui, et une dorsale océanique, qui sépare déjà "
                "deux plaques océaniques, comme dans l'Atlantique. Le "
                "premier deviendra la seconde, mais seulement dans des "
                "dizaines de millions d'années."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
