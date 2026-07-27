"""
scenes/Physique_IntroductionOptiqueGeometrique_01.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 01.

§ 1. Sources de lumière : primaires (produisent elles-mêmes leur lumière —
naturelles : Soleil, étoiles, luciole ; artificielles : lampe, néon, laser)
et secondaires (diffusent la lumière reçue d'une source primaire — Lune,
écran, mur). Sources ponctuelles / étendues.
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 1).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    GRAY,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _schema_soleil_lune():
    """Soleil (source primaire, il produit sa propre lumière, rayons vers
    l'extérieur) à gauche, Lune (source secondaire, elle ne fait que
    réfléchir la lumière reçue) à droite."""
    soleil = Circle(radius=0.55, color=YELLOW, fill_color=YELLOW, fill_opacity=1.0)
    soleil.move_to(LEFT * 3.4)
    rayons_soleil = VGroup(
        *[
            Arrow(
                soleil.get_center(),
                soleil.get_center() + 1.1 * ORIGIN.copy() + 1.1 * direction,
                buff=0.55,
                stroke_width=2,
                color=YELLOW,
                max_tip_length_to_length_ratio=0.3,
            )
            for direction in [UP, DOWN, LEFT, RIGHT, UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT]
        ]
    )
    label_soleil = Text("Source primaire", font_size=18, color=YELLOW)
    label_soleil.next_to(soleil, DOWN, buff=1.1)

    lune = Circle(radius=0.4, color=GRAY, fill_color=GRAY, fill_opacity=1.0)
    lune.move_to(RIGHT * 3.4)
    rayon_incident = Arrow(
        soleil.get_center() + UP * 0.3 + RIGHT * 0.5,
        lune.get_left(),
        buff=0.1,
        stroke_width=2,
        color=YELLOW,
        max_tip_length_to_length_ratio=0.12,
    )
    rayons_diffuses = VGroup(
        *[
            Arrow(
                lune.get_center(),
                lune.get_center() + 0.9 * direction,
                buff=0.42,
                stroke_width=2,
                color=WHITE,
                max_tip_length_to_length_ratio=0.3,
            )
            for direction in [UP + RIGHT, RIGHT, DOWN + RIGHT, DOWN]
        ]
    )
    label_lune = Text("Source secondaire", font_size=18, color=WHITE)
    label_lune.next_to(lune, DOWN, buff=1.1)

    return VGroup(
        soleil, rayons_soleil, label_soleil,
        rayon_incident, lune, rayons_diffuses, label_lune,
    )


class SourcesPrimairesSecondaires(NotionScene):
    def construct(self):
        titre = scene_title("Sources de lumière : primaires et secondaires")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Le Soleil brille, une lampe brille, mais la Lune aussi "
                "semble briller la nuit. Toutes ces sources de lumière "
                "sont-elles vraiment identiques ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le Soleil brille, une lampe brille, mais la Lune aussi "
                "semble briller la nuit. Toutes ces sources de lumière "
                "sont-elles vraiment identiques ? C'est ce que nous allons "
                "voir dans ce premier chapitre d'optique géométrique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : source primaire --------------------------------
        definition_primaire = definition_box(
            VGroup(
                Text("Une source PRIMAIRE produit elle-même sa propre", font_size=20),
                Text("lumière.", font_size=20),
                Text("Naturelles : Soleil, étoiles, luciole.", font_size=19),
                Text("Artificielles : lampe, tube néon, laser.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.0,
        )
        definition_primaire.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une source primaire produit elle-même sa propre lumière. "
                "Il existe des sources primaires naturelles, comme le "
                "Soleil, les étoiles ou une luciole, et des sources "
                "primaires artificielles, comme une lampe, un tube néon ou "
                "un laser."
            )
        ) as tracker:
            self.play(FadeIn(definition_primaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_primaire))

        # --- Raisonnement : source secondaire -------------------------------
        definition_secondaire = definition_box(
            VGroup(
                Text("Une source SECONDAIRE ne produit pas sa propre", font_size=20),
                Text("lumière : elle diffuse la lumière reçue d'une", font_size=20),
                Text("source primaire.", font_size=20),
                Text("Exemples : la Lune, un écran de cinéma, un mur.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.0,
        )
        definition_secondaire.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À l'inverse, une source secondaire ne produit pas sa "
                "propre lumière : elle se contente de diffuser la lumière "
                "qu'elle reçoit d'une source primaire. C'est le cas de la "
                "Lune, d'un écran de cinéma ou simplement d'un mur éclairé."
            )
        ) as tracker:
            self.play(FadeIn(definition_secondaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_secondaire))

        # --- Exemple traité : Soleil vs Lune --------------------------------
        schema = _schema_soleil_lune()
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Regardons le Soleil et la Lune. Le Soleil émet sa propre "
                "lumière dans toutes les directions : c'est une source "
                "primaire. La Lune, elle, ne fait que recevoir la lumière "
                "du Soleil et la renvoyer vers la Terre : c'est une source "
                "secondaire."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Ponctuelle / étendue -------------------------------------------
        ponctuelle_etendue = definition_box(
            VGroup(
                Text("Source PONCTUELLE : ses dimensions sont négligeables", font_size=20),
                Text("devant la distance d'observation (petite lampe, étoile", font_size=20),
                Text("lointaine).", font_size=20),
                Text("Source ÉTENDUE : ses dimensions ne sont PAS", font_size=20),
                Text("négligeables (Soleil, tube néon proche).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.4,
        )
        ponctuelle_etendue.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On distingue enfin deux tailles de sources. Une source "
                "ponctuelle a des dimensions négligeables devant la "
                "distance d'observation, comme une petite lampe ou une "
                "étoile lointaine. Une source étendue, elle, a des "
                "dimensions qui ne sont pas négligeables, comme le Soleil "
                "ou un tube néon proche."
            )
        ) as tracker:
            self.play(FadeIn(ponctuelle_etendue))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ponctuelle_etendue))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Source primaire = produit sa propre lumière.", font_size=20),
                Text("Source secondaire = diffuse la lumière reçue.", font_size=20),
                Text("Ponctuelle = dimensions négligeables ; étendue = non.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.22),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Une source primaire produit sa "
                "propre lumière, une source secondaire ne fait que "
                "diffuser celle qu'elle reçoit. Et selon sa taille "
                "relative, une source est dite ponctuelle ou étendue."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• La Lune n'est PAS une source primaire : elle ne", font_size=20),
                Text("   brille pas par elle-même, elle réfléchit la lumière", font_size=20),
                Text("   du Soleil.", font_size=20),
                Text("• Un objet éclairé qui brille (mur, écran) reste une", font_size=20),
                Text("   source SECONDAIRE, jamais une source primaire.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un piège classique : la Lune n'est pas une source "
                "primaire. Elle ne brille pas par elle-même, elle réfléchit "
                "simplement la lumière du Soleil. Plus généralement, un "
                "objet éclairé qui semble briller, comme un mur ou un "
                "écran, reste une source secondaire, jamais une source "
                "primaire."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
