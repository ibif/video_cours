"""
scenes/Physique_IntroductionOptiqueGeometrique_02.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 02.

§ 1 (suite). Récepteurs de lumière (œil, photopile, pellicule/capteur) —
pourquoi voit-on les objets ? Exemple résolu 1 : classement source
primaire / source secondaire / récepteur.
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 1).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    GRAY,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    Dot,
    Ellipse,
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


def _schema_oeil():
    """Schéma très simplifié d'un œil recevant un rayon lumineux issu d'un
    objet éclairé, pour illustrer le rôle de récepteur."""
    objet = Circle(radius=0.18, color=YELLOW, fill_color=YELLOW, fill_opacity=1.0)
    objet.move_to(LEFT * 3.2)
    label_objet = Text("objet éclairé", font_size=16, color=WHITE)
    label_objet.next_to(objet, DOWN, buff=0.2)

    oeil = Ellipse(width=1.0, height=0.6, color=WHITE)
    oeil.move_to(RIGHT * 2.6)
    pupille = Dot(oeil.get_center(), color=WHITE, radius=0.09)
    label_oeil = Text("œil (récepteur)", font_size=16, color=WHITE)
    label_oeil.next_to(oeil, DOWN, buff=0.2)

    rayon = Arrow(
        objet.get_right(),
        oeil.get_left(),
        buff=0.1,
        stroke_width=2,
        color=YELLOW,
        max_tip_length_to_length_ratio=0.08,
    )

    return VGroup(objet, label_objet, rayon, oeil, pupille, label_oeil)


class RecepteursDeLumiere(NotionScene):
    def construct(self):
        titre = scene_title("Récepteurs de lumière")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Nous avons vu les sources de lumière. Mais comment cette "
                "lumière est-elle finalement reçue et utilisée : par notre "
                "œil, par un appareil photo ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Nous avons vu les sources de lumière. Mais comment cette "
                "lumière est-elle finalement reçue et utilisée, par notre "
                "œil ou par un appareil photo ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition récepteur -----------------------------
        definition_recepteur = definition_box(
            VGroup(
                Text("Un RÉCEPTEUR est un objet ou un système qui reçoit la", font_size=20),
                Text("lumière et la transforme en une autre grandeur.", font_size=20),
                Text("• L'œil la transforme en influx nerveux.", font_size=19),
                Text("• La photopile la transforme en énergie électrique.", font_size=19),
                Text("• La pellicule / le capteur la transforme en image.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.6,
        )
        definition_recepteur.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un récepteur est un objet ou un système qui reçoit la "
                "lumière et la transforme en une autre grandeur. L'œil la "
                "transforme en influx nerveux, la photopile la transforme "
                "en énergie électrique, et la pellicule ou le capteur d'un "
                "appareil photo la transforme en image."
            )
        ) as tracker:
            self.play(FadeIn(definition_recepteur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_recepteur))

        # --- Raisonnement : pourquoi voit-on les objets ? ---------------------
        schema = _schema_oeil()
        schema.scale(0.9)
        schema.next_to(titre, DOWN, buff=0.6)

        remarque_vision = definition_box(
            VGroup(
                Text("On voit un objet lorsque de la lumière — issue d'une", font_size=19),
                Text("source ou diffusée par l'objet — pénètre dans notre œil.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.2,
        )
        remarque_vision.next_to(schema, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pourquoi voit-on les objets qui nous entourent ? Parce que "
                "de la lumière, qu'elle vienne directement d'une source ou "
                "qu'elle soit diffusée par l'objet, pénètre dans notre œil, "
                "qui joue ici le rôle de récepteur."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(remarque_vision))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(remarque_vision))

        # --- Exemple résolu 1 : classement -------------------------------------
        tableau = VGroup(
            Text("Lune → source secondaire", font_size=19),
            Text("Ampoule allumée → source primaire", font_size=19),
            Text("Œil → récepteur", font_size=19),
            Text("Cahier éclairé → source secondaire", font_size=19),
            Text("Étoile → source primaire", font_size=19),
            Text("Photopile → récepteur", font_size=19),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        exemple = example_box(tableau, box_width=9.4)
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : classons ces objets. La Lune est une source "
                "secondaire, elle réfléchit la lumière solaire. Une "
                "ampoule allumée est une source primaire, elle produit sa "
                "propre lumière. L'œil est un récepteur. Un cahier éclairé "
                "diffuse la lumière qu'il reçoit : c'est aussi une source "
                "secondaire. Une étoile est une source primaire. Et une "
                "photopile, qui transforme la lumière en électricité, est "
                "un récepteur."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Récepteur = reçoit la lumière et la transforme", font_size=20),
                Text("(œil, photopile, pellicule/capteur).", font_size=20),
                Text("On voit un objet quand sa lumière atteint notre œil.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Un récepteur reçoit la lumière et "
                "la transforme, comme l'œil, une photopile ou une "
                "pellicule. Et l'on ne voit un objet que si la lumière "
                "qu'il émet ou diffuse atteint effectivement notre œil."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas confondre récepteur et source secondaire :", font_size=20),
                Text("   un objet éclairé qui diffuse la lumière (cahier,", font_size=20),
                Text("   mur) est une SOURCE secondaire, pas un récepteur.", font_size=20),
                Text("• Question utile : l'objet PRODUIT-il de la lumière,", font_size=20),
                Text("   la DIFFUSE-t-il, ou la REÇOIT-il pour la", font_size=20),
                Text("   transformer ?", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : il ne faut pas confondre "
                "récepteur et source secondaire. Un objet éclairé qui "
                "diffuse la lumière, comme un cahier ou un mur, est une "
                "source secondaire, pas un récepteur. La question à se "
                "poser est simple : l'objet produit-il de la lumière, la "
                "diffuse-t-il, ou la reçoit-il pour la transformer en "
                "autre chose ?"
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
