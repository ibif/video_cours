"""
scenes/Physique_EnergiePotentielleElectrostatique_03.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 03.

Travail moteur / résistant de la force électrostatique : signe de
q E⃗·AB⃗ selon l'orientation du déplacement par rapport au champ, exemple
résolu (condensateur, E=2000 V/m, q=4 µC, déplacement de 10 cm dans le
sens de E⃗, W=8×10⁻⁴ J moteur).
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _mini_schema(sens_deplacement: str, couleur) -> VGroup:
    """Petit schéma : champ E⃗ horizontal fixe, déplacement AB dans une
    direction donnée ('meme', 'oppose' ou 'perp')."""
    champ = Arrow(LEFT * 1.1, RIGHT * 1.1, color=YELLOW, buff=0, stroke_width=3)
    label_champ = MathTex(r"\vec{E}", font_size=24, color=YELLOW).next_to(champ, UP, buff=0.1)
    if sens_deplacement == "meme":
        depl = Arrow(LEFT * 1.0 + DOWN * 0.7, RIGHT * 1.0 + DOWN * 0.7, color=couleur, buff=0, stroke_width=3)
    elif sens_deplacement == "oppose":
        depl = Arrow(RIGHT * 1.0 + DOWN * 0.7, LEFT * 1.0 + DOWN * 0.7, color=couleur, buff=0, stroke_width=3)
    else:
        depl = Arrow(DOWN * 1.1, UP * 0.3, color=couleur, buff=0, stroke_width=3)
    label_depl = MathTex(r"\vec{AB}", font_size=22, color=couleur).next_to(depl, DOWN, buff=0.1)
    return VGroup(champ, label_champ, depl, label_depl)


class TravailMoteurResistant(NotionScene):
    def construct(self):
        titre = scene_title("Travail moteur ou résistant : le signe compte")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------------------
        question = Text(
            _wrap(
                "Nous savons que W_A→B(F⃗)=qE⃗·AB⃗. Mais que nous apprend le "
                "signe de ce travail sur le mouvement de la charge ?",
                width=54,
            ),
            font_size=24,
        )
        question.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Nous savons désormais que le travail de la force "
                "électrostatique vaut q E fois AB. Mais que nous apprend le "
                "signe de ce travail sur le mouvement réel de la charge ? "
                "Tout dépend, en réalité, de l'orientation du déplacement "
                "par rapport au champ."
            )
        ) as tracker:
            self.play(Write(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : les trois cas -----------------------------------------------
        cas1 = VGroup(
            _mini_schema("meme", GREEN).scale(0.75),
            Text("même sens", font_size=18),
            MathTex(r"q\vec{E}\cdot\vec{AB} > 0", font_size=22, color=GREEN),
            Text("travail MOTEUR", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.15)

        cas2 = VGroup(
            _mini_schema("oppose", RED).scale(0.75),
            Text("sens opposé", font_size=18),
            MathTex(r"q\vec{E}\cdot\vec{AB} < 0", font_size=22, color=RED),
            Text("travail RÉSISTANT", font_size=20, color=RED),
        ).arrange(DOWN, buff=0.15)

        cas3 = VGroup(
            _mini_schema("perp", WHITE).scale(0.75),
            Text("perpendiculaire", font_size=18),
            MathTex(r"q\vec{E}\cdot\vec{AB} = 0", font_size=22),
            Text("travail NUL", font_size=20),
        ).arrange(DOWN, buff=0.15)

        table = VGroup(cas1, cas2, cas3).arrange(RIGHT, buff=0.9)
        table.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Trois cas se présentent, en supposant la charge q "
                "positive. Si le déplacement AB se fait dans le même sens "
                "que le champ E, le travail est positif : il est moteur, il "
                "accélère la charge. Si le déplacement se fait en sens "
                "opposé au champ, le travail est négatif : il est "
                "résistant, il freine la charge. Et si le déplacement est "
                "perpendiculaire au champ, le produit scalaire est nul : le "
                "travail est nul, la force électrostatique ne modifie ni "
                "n'accélère le mouvement dans cette direction."
            )
        ) as tracker:
            self.play(FadeIn(cas1))
            self.play(FadeIn(cas2))
            self.play(FadeIn(cas3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(table))

        # --- Complément : cas d'une charge négative ---------------------------------
        complement = property_box(
            Text(
                _wrap(
                    "Attention : si q est NÉGATIVE, tous les signes "
                    "s'inversent ! Une charge négative qui se déplace dans "
                    "le sens de E⃗ subit un travail résistant.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        complement.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Attention, un point essentiel : si la charge q est "
                "négative, tous ces signes s'inversent. Une charge "
                "négative qui se déplace dans le sens du champ E subit, au "
                "contraire, un travail résistant. Il faut donc toujours "
                "tenir compte du signe de la charge, et pas seulement de "
                "l'orientation géométrique du déplacement."
            )
        ) as tracker:
            self.play(FadeIn(complement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(complement))

        # --- Exemple résolu 2 -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Exemple : dans un condensateur, E=2000 V/m. Une charge "
                "q=4 µC se déplace de 10 cm dans le sens de E⃗. Calculer le "
                "travail de la force électrostatique.",
                width=54,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Exemple d'application. Dans un condensateur plan, le "
                "champ électrostatique vaut 2000 volts par mètre. Une "
                "charge de 4 microcoulombs se déplace de 10 centimètres, "
                "exactement dans le sens du champ. Calculons le travail de "
                "la force électrostatique sur ce trajet."
            )
        ) as tracker:
            self.play(Write(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul = example_box(
            VGroup(
                MathTex(
                    r"W = qE\,d = 4\times10^{-6} \times 2000 \times 0{,}10",
                    font_size=25,
                ),
                MathTex(r"W = 8\times10^{-4}\ \text{J} \quad (\text{moteur})", font_size=27, color=GREEN),
                Text(
                    "La charge positive est attirée vers la plaque négative.",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.4,
        )
        calcul.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le déplacement se faisant dans le sens du champ, le "
                "travail vaut simplement q fois E fois d, soit 4 fois 10 "
                "puissance moins 6, fois 2000, fois 0 virgule 10, ce qui "
                "donne 8 fois 10 puissance moins 4 joule. Ce travail est "
                "positif : il est moteur. Cela traduit le fait que la "
                "charge positive est naturellement attirée vers la plaque "
                "négative du condensateur."
            )
        ) as tracker:
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Signe de W=qE⃗·AB⃗ : moteur si déplacement et force de "
                    "même sens, résistant si sens opposés, nul si "
                    "perpendiculaires. Ne jamais oublier le signe de la "
                    "charge q dans le raisonnement.",
                    width=56,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le signe du travail de la force "
                "électrostatique dépend à la fois de l'orientation du "
                "déplacement par rapport au champ, et du signe de la "
                "charge. Travail moteur si la force et le déplacement vont "
                "dans le même sens, résistant s'ils sont opposés, nul s'ils "
                "sont perpendiculaires. Ne négligez jamais le signe de la "
                "charge dans ce raisonnement."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
