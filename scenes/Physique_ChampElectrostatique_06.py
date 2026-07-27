"""
scenes/Physique_ChampElectrostatique_06.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 06.

§ Lignes de champ : définition (tangente à E⃗, orientée dans le même
sens), propriétés (ne se croisent jamais, partent des charges positives,
arrivent aux charges négatives, densité=intensité du champ), spectre
d'une charge ponctuelle seule (radial, divergent si +, convergent si -),
spectre d'un dipôle électrostatique (définition, lignes de la charge +
vers la charge -).
Source : 1ereC/Physique.pdf, pages 54-65 (chapitre 6, § 4).
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    BLUE,
    ArcBetweenPoints,
    Arrow,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _radial_line(center, angle, r_min, r_max, color, pointe_vers_exterieur=True):
    direction = np.array([np.cos(angle), np.sin(angle), 0])
    start = center + r_min * direction
    end = center + r_max * direction
    if pointe_vers_exterieur:
        return Arrow(start, end, buff=0, color=color, stroke_width=2.5, max_tip_length_to_length_ratio=0.18)
    return Arrow(end, start, buff=0, color=color, stroke_width=2.5, max_tip_length_to_length_ratio=0.18)


class LignesDeChamp(NotionScene):
    def construct(self):
        titre = scene_title("Les lignes de champ")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : comment visualiser un champ électrostatique ? ---------------
        mise_en_situation = Text(
            _wrap(
                "Le champ électrostatique existe en tout point de "
                "l'espace : comment le visualiser simplement, en un seul "
                "schéma ?",
                width=52,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le champ électrostatique existe en tout point de "
                "l'espace : comment le visualiser simplement, en un seul "
                "schéma ? La réponse est la notion de ligne de champ."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Définition et propriétés des lignes de champ ---------------------------
        definition = definition_box(
            VGroup(
                Text("Ligne de champ", font_size=22, weight="BOLD"),
                Text("Courbe tangente au vecteur champ E⃗ en chacun de ses", font_size=19),
                Text("points, orientée dans le même sens que E⃗.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.2,
        )
        proprietes = property_box(
            VGroup(
                Text("Propriétés", font_size=22, weight="BOLD"),
                Text("• Deux lignes de champ ne se croisent jamais.", font_size=19),
                Text("• Elles partent des charges positives et arrivent", font_size=19),
                Text("   aux charges négatives.", font_size=19),
                Text("• Leur densité (resserrement) traduit l'intensité", font_size=19),
                Text("   du champ : lignes serrées = champ fort.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=11.6,
        )
        groupe_def = VGroup(definition, proprietes).arrange(DOWN, buff=0.35)
        groupe_def.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une ligne de champ est une courbe tangente, en chacun "
                "de ses points, au vecteur champ E, et orientée dans le "
                "même sens que lui. Elle possède trois propriétés "
                "importantes : deux lignes de champ ne se croisent "
                "jamais ; elles partent toujours des charges positives "
                "et arrivent aux charges négatives ; et leur densité, "
                "c'est-à-dire leur resserrement, traduit l'intensité du "
                "champ, des lignes serrées signalant un champ fort."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_def))

        # --- Spectre d'une charge ponctuelle seule (+ et -) -------------------------
        centre_pos = LEFT * 3.2
        q_pos = Dot(centre_pos, color=RED, radius=0.14)
        angles = [i * PI / 4 for i in range(8)]
        lignes_pos = VGroup(*[
            _radial_line(centre_pos, a, 0.3, 1.5, YELLOW, pointe_vers_exterieur=True) for a in angles
        ])
        label_pos = Text("Q > 0 : spectre divergent", font_size=17).next_to(q_pos, DOWN, buff=1.7)
        groupe_pos = VGroup(q_pos, lignes_pos, label_pos)

        centre_neg = RIGHT * 3.2
        q_neg = Dot(centre_neg, color=BLUE, radius=0.14)
        lignes_neg = VGroup(*[
            _radial_line(centre_neg, a, 0.3, 1.5, YELLOW, pointe_vers_exterieur=False) for a in angles
        ])
        label_neg = Text("Q < 0 : spectre convergent", font_size=17).next_to(q_neg, DOWN, buff=1.7)
        groupe_neg = VGroup(q_neg, lignes_neg, label_neg)

        spectres = VGroup(groupe_pos, groupe_neg)
        spectres.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le spectre d'une charge ponctuelle isolée est constitué "
                "de droites radiales. Si la charge est positive, les "
                "lignes de champ divergent à partir d'elle, dans toutes "
                "les directions de l'espace. Si la charge est négative, "
                "elles convergent au contraire vers elle."
            )
        ) as tracker:
            self.play(Create(groupe_pos))
            self.play(Create(groupe_neg))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(spectres))

        # --- Définition et spectre d'un dipôle électrostatique ----------------------
        definition_dipole = definition_box(
            VGroup(
                Text("Dipôle électrostatique", font_size=22, weight="BOLD"),
                Text("Ensemble de deux charges ponctuelles opposées, +q et -q,", font_size=19),
                Text("séparées d'une distance petite devant les distances", font_size=19),
                Text("d'observation.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        definition_dipole.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On appelle dipôle électrostatique l'ensemble formé par "
                "deux charges ponctuelles opposées, plus q et moins q, "
                "séparées d'une petite distance."
            )
        ) as tracker:
            self.play(FadeIn(definition_dipole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_dipole))

        p_pos = LEFT * 1.6
        p_neg = RIGHT * 1.6
        dp_pos = Dot(p_pos, color=RED, radius=0.14)
        dp_pos_label = MathTex("+q", font_size=22).next_to(dp_pos, UP, buff=0.15)
        dp_neg = Dot(p_neg, color=BLUE, radius=0.14)
        dp_neg_label = MathTex("-q", font_size=22).next_to(dp_neg, UP, buff=0.15)

        courbes = VGroup()
        offsets = [1.6, 0.9, 0.0, -0.9, -1.6]
        for off in offsets:
            # Ligne courbe reliant la charge + à la charge -, bombée
            # verticalement d'autant plus que |off| est grand.
            vertical_shift = 0.15 * np.sign(off) if off != 0 else 0
            depart = p_pos + np.array([0.15, vertical_shift, 0])
            arrivee = p_neg + np.array([-0.15, vertical_shift, 0])
            courbe = ArcBetweenPoints(depart, arrivee, angle=-off * 0.6 if off != 0 else 0.001, color=YELLOW, stroke_width=2.5)
            courbes.add(courbe)

        dipole_schema = VGroup(dp_pos, dp_pos_label, dp_neg, dp_neg_label, courbes)
        dipole_schema.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Le spectre d'un dipôle électrostatique montre des "
                "lignes de champ qui partent toutes de la charge "
                "positive et rejoignent toutes la charge négative, en "
                "s'incurvant entre les deux : c'est la représentation "
                "typique du champ créé par deux charges opposées "
                "proches l'une de l'autre."
            )
        ) as tracker:
            self.play(Create(dp_pos), Write(dp_pos_label), Create(dp_neg), Write(dp_neg_label))
            self.play(Create(courbes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(dipole_schema))

        # --- Exemple résolu : lire un spectre ----------------------------------------
        exemple = example_box(
            VGroup(
                Text("Sur un spectre, les lignes convergent toutes vers une charge X,", font_size=19),
                Text("de plus en plus serrées à mesure qu'on s'en approche.", font_size=19),
                MathTex(r"\Rightarrow \ X \text{ est une charge NÉGATIVE, et le champ y est fort.}", font_size=21, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : sur un spectre donné, on observe des lignes de "
                "champ qui convergent toutes vers une charge X, en "
                "devenant de plus en plus serrées à mesure qu'on s'en "
                "approche. On peut en conclure que X est une charge "
                "négative, et que le champ y est particulièrement fort, "
                "puisque les lignes y sont les plus resserrées."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Ligne de champ : tangente à E⃗, part du + , arrive au -.", font_size=20),
                Text("Ne se croisent jamais ; densité = intensité du champ.", font_size=20),
                Text("Charge seule : spectre radial. Dipôle : lignes courbes + → -.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : une ligne de champ est tangente "
                "au vecteur champ, part d'une charge positive et arrive "
                "sur une charge négative. Deux lignes ne se croisent "
                "jamais, et leur densité traduit l'intensité du champ. "
                "Une charge ponctuelle isolée donne un spectre radial ; "
                "un dipôle donne des lignes courbes qui vont de la "
                "charge positive vers la charge négative."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
