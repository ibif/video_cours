"""
scenes/SVT_FecondationMammiferes_01.py — Chapitre 4 (1ereC, SVT), scène 01.

Introduction : définition de la fécondation (union spermatozoïde/ovule ->
zygote), lieu de la fécondation (tiers externe de la trompe de Fallope,
schéma simplifié de l'appareil génital féminin), objectifs du chapitre,
piège "jamais dans l'utérus". Source : 1ereC/SVT.pdf, pages 34-35.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UL,
    UP,
    UR,
    WHITE,
    YELLOW,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    Polygon,
    Rectangle,
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
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _schema_appareil_genital():
    """Schéma simplifié de l'appareil génital féminin (Figure 1) : utérus,
    une trompe de Fallope avec son tiers externe mis en évidence (lieu de
    la fécondation), un ovaire, le vagin, la montée des spermatozoïdes.

    Retourne (base, highlight, sperm) : trois VGroup distincts, affichés en
    trois temps par la scène, plus utiles pour les FadeOut ciblés."""
    uterus = Polygon(
        UL * 0.9, UR * 0.9, RIGHT * 1.3 + DOWN * 1.4, LEFT * 1.3 + DOWN * 1.4,
        color=WHITE, stroke_width=2,
    )
    vagin = Rectangle(width=0.7, height=1.1, color=WHITE, stroke_width=2)
    vagin.next_to(uterus, DOWN, buff=0)

    trompe = Line(uterus.get_corner(UR), uterus.get_corner(UR) + RIGHT * 2.0 + UP * 0.3, color=WHITE, stroke_width=3)
    tiers_externe = Line(
        trompe.get_end(),
        trompe.get_end() + RIGHT * 0.9 + UP * 0.05,
        color=YELLOW,
        stroke_width=5,
    )
    ovaire = Ellipse(width=0.9, height=0.6, color=WHITE, stroke_width=2, fill_color=WHITE, fill_opacity=0.15)
    ovaire.next_to(tiers_externe, RIGHT, buff=0.15)

    ovule = Dot(radius=0.07, color=YELLOW)
    ovule.move_to(tiers_externe.get_center())

    label_uterus = Text("Utérus", font_size=16, color=WHITE)
    label_uterus.move_to(uterus.get_center())
    label_vagin = Text("Vagin", font_size=14, color=WHITE)
    label_vagin.move_to(vagin.get_center())
    label_trompe = Text("Trompe de Fallope", font_size=13, color=WHITE)
    label_trompe.next_to(trompe, UP, buff=0.35)
    label_tiers = Text("Tiers externe :\nlieu de la fécondation", font_size=13, color=YELLOW)
    label_tiers.next_to(tiers_externe, UP, buff=0.15)
    label_ovaire = Text("Ovaire", font_size=13, color=WHITE)
    label_ovaire.next_to(ovaire, RIGHT, buff=0.15)

    spermatozoides = VGroup(*[Dot(radius=0.035, color="#FF6666") for _ in range(5)])
    spermatozoides.arrange(UP, buff=0.12)
    spermatozoides.move_to(vagin.get_center() + UP * 0.1)
    fleche_montee = Line(vagin.get_top(), uterus.get_center() + DOWN * 0.3, color="#FF6666", stroke_width=2)

    base = VGroup(uterus, vagin, trompe, ovaire, label_uterus, label_vagin, label_trompe, label_ovaire)
    highlight = VGroup(tiers_externe, ovule, label_tiers)
    sperm = VGroup(spermatozoides, fleche_montee)
    return base, highlight, sperm


class IntroductionFecondation(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 4 — La fécondation chez les mammifères")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition de la fécondation ------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La fécondation est l'union d'un gamète mâle (le "
                    "spermatozoïde) et d'un gamète femelle (l'ovule ou "
                    "ovocyte II) pour former une cellule unique : l'œuf ou "
                    "zygote, cellule diploïde (2n), première cellule du "
                    "nouvel individu. Chez les mammifères, elle est "
                    "interne : elle se déroule dans l'appareil génital "
                    "féminin.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Bienvenue dans ce chapitre quatre consacré à la "
                "fécondation chez les mammifères. Retenons d'abord la "
                "définition : la fécondation est l'union d'un gamète mâle, "
                "le spermatozoïde, et d'un gamète femelle, l'ovule ou "
                "ovocyte deux, pour former une cellule unique appelée œuf "
                "ou zygote. C'est une cellule diploïde, à deux n "
                "chromosomes, la toute première cellule du nouvel "
                "individu. Chez les mammifères, la fécondation est "
                "interne : elle se déroule à l'intérieur de l'appareil "
                "génital féminin."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : le schéma de l'appareil génital --------
        base, highlight, sperm = _schema_appareil_genital()
        schema = VGroup(base, highlight, sperm)
        schema.scale(1.5)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Voici un schéma simplifié de l'appareil génital féminin : "
                "l'utérus, le vagin en dessous, et une trompe de Fallope "
                "reliant l'utérus à l'ovaire. Les spermatozoïdes déposés "
                "dans le vagin remontent vers l'utérus, puis vers la "
                "trompe."
            )
        ) as tracker:
            self.play(FadeIn(base))
            self.play(FadeIn(sperm))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Chez l'espèce humaine, la fécondation a lieu précisément "
                "dans le tiers externe de la trompe de Fallope : la "
                "portion de la trompe la plus proche de l'ovaire, au "
                "voisinage du pavillon, mise en évidence ici en jaune. "
                "C'est là, et seulement là, que les spermatozoïdes "
                "rencontrent l'ovule."
            )
        ) as tracker:
            self.play(FadeIn(highlight))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : localiser le lieu exact ----------------------------
        exemple = definition_box(
            Text(
                _wrap(
                    "Après la fécondation, l'œuf migre pendant plusieurs "
                    "jours de la trompe vers l'utérus, en se divisant "
                    "(segmentation, chapitre suivant). Le trajet complet "
                    "est donc : ovule libéré près de l'ovaire → "
                    "fécondation dans le tiers externe de la trompe → "
                    "migration → nidation dans l'utérus.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un exemple pour bien situer les événements dans le temps "
                "et l'espace : l'ovule est libéré près de l'ovaire, la "
                "fécondation a lieu dans le tiers externe de la trompe, "
                "puis l'œuf migre pendant plusieurs jours vers l'utérus en "
                "se divisant, avant de s'y nicher. Fécondation et nidation "
                "sont donc deux événements séparés, dans deux lieux "
                "différents."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : objectifs du chapitre -----------------------------------
        objectifs_titre = Text("Objectifs de ce chapitre", font_size=27, color=YELLOW, weight="BOLD")
        objectifs_titre.next_to(titre, DOWN, buff=0.5)
        objectifs = _bullets(
            [
                "Définir la fécondation et décrire le trajet des gamètes.",
                "Expliquer les étapes de la fécondation : capacitation, "
                "réaction acrosomique, franchissement des enveloppes, "
                "blocage de la polyspermie, amphimixie.",
                "Montrer que la fécondation restaure la diploïdie et "
                "détermine le sexe de l'embryon.",
                "Décrire la segmentation, la morula, le blastocyste et la "
                "nidation.",
                "Distinguer vrais et faux jumeaux.",
                "Connaître les principes de la contraception, de l'IVG et "
                "de la FIVETE pour un comportement responsable.",
            ],
            font_size=20,
            width=50,
        )
        objectifs.next_to(objectifs_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, vous devrez être capables de : "
                "définir la fécondation et décrire le trajet des gamètes "
                "mâles et femelles ; expliquer les étapes de la "
                "fécondation, de la capacitation à l'amphimixie ; montrer "
                "que la fécondation restaure la diploïdie et détermine le "
                "sexe de l'embryon ; décrire la segmentation, la morula, "
                "le blastocyste et la nidation ; distinguer vrais et faux "
                "jumeaux ; et enfin connaître les principes scientifiques "
                "de la contraception, de l'IVG et de la FIVETE, pour "
                "adopter un comportement responsable."
            )
        ) as tracker:
            self.play(FadeIn(objectifs_titre))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(objectifs_titre), FadeOut(objectifs))

        # --- Piège à éviter : jamais dans l'utérus -------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne jamais écrire que la fécondation a lieu dans "
                    "l'utérus. L'utérus est le lieu de la NIDATION et du "
                    "développement de l'embryon, pas de la fécondation. "
                    "Elle n'a lieu ni dans l'utérus, ni dans le vagin, ni "
                    "dans l'ovaire, mais dans le tiers externe de la "
                    "trompe de Fallope.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège très fréquent dans les devoirs de "
                "niveau : ne jamais écrire que la fécondation a lieu dans "
                "l'utérus. L'utérus est le lieu de la nidation et du "
                "développement de l'embryon, pas de la fécondation. Elle "
                "n'a lieu ni dans l'utérus, ni dans le vagin, ni dans "
                "l'ovaire, mais bien dans le tiers externe de la trompe de "
                "Fallope."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
