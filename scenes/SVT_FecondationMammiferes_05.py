"""
scenes/SVT_FecondationMammiferes_05.py — Chapitre 4 (1ereC, SVT), scène 05.

§ 3.4 Le blocage de la polyspermie (définition, blocage rapide électrique,
blocage lent = réaction corticale) + § 3.5 l'amphimixie (pronucleus mâle/
femelle, fusion des noyaux n+n=2n, schéma en 4 étapes).
Source : 1ereC/SVT.pdf, pages 38-39.
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
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class BlocagePolyspermieAmphimixie(NotionScene):
    def construct(self):
        titre = scene_title("4.3 — Blocage de la polyspermie et amphimixie")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : la définition de la polyspermie -----------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La polyspermie est la pénétration de plusieurs "
                    "spermatozoïdes dans le même ovule. Elle produirait un "
                    "œuf polyploïde, non viable. Dès que le premier "
                    "spermatozoïde franchit la membrane vitelline, "
                    "l'ovule déclenche des mécanismes de défense.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un seul spermatozoïde doit féconder l'ovule. La "
                "polyspermie est la pénétration de plusieurs "
                "spermatozoïdes dans le même ovule : elle produirait un "
                "œuf polyploïde, non viable. C'est pourquoi, dès que le "
                "premier spermatozoïde franchit la membrane vitelline, "
                "l'ovule déclenche immédiatement des mécanismes de "
                "défense."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : les 2 blocages ----------------------------
        ovule = Circle(radius=1.4, color="#B42E41", stroke_width=3)
        ovule.next_to(titre, DOWN, buff=0.7)
        premier_sperm = Dot(radius=0.09, color=WHITE)
        premier_sperm.move_to(ovule.get_left())
        deuxieme_sperm = Dot(radius=0.09, color="#888888")
        deuxieme_sperm.move_to(ovule.get_top() + UP * 0.4)

        label1 = Text("1. Blocage rapide : membrane vitelline\ndevient électriquement infranchissable", font_size=15, color=YELLOW)
        label1.next_to(ovule, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premier mécanisme, le blocage rapide : dès que le premier "
                "spermatozoïde entre en contact, les propriétés "
                "électriques de la membrane vitelline se modifient "
                "instantanément, et elle devient infranchissable pour tout "
                "autre spermatozoïde."
            )
        ) as tracker:
            self.play(FadeIn(ovule), FadeIn(premier_sperm))
            self.play(ovule.animate.set_color("#DE7C1F"))
            self.play(FadeIn(label1))
            self.wait(tracker.get_remaining_duration())

        grains = VGroup(*[Dot(radius=0.04, color=YELLOW).move_to(ovule.point_at_angle(a)) for a in [i * 0.9 for i in range(7)]])
        label2 = Text("2. Blocage lent : réaction corticale\ndurcit la zone pellucide (imperméable)", font_size=15, color=YELLOW)
        label2.next_to(ovule, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Second mécanisme, plus lent : la réaction corticale. Des "
                "grains corticaux, situés sous la membrane de l'ovule, "
                "libèrent leur contenu. Cela durcit la zone pellucide et "
                "détruit ses récepteurs : elle devient imperméable aux "
                "autres spermatozoïdes, qui ne peuvent plus s'y fixer."
            )
        ) as tracker:
            self.play(FadeIn(grains), FadeOut(label1), FadeIn(label2))
            self.play(deuxieme_sperm.animate.shift(UP * 0.4), FadeIn(deuxieme_sperm))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ovule), FadeOut(premier_sperm), FadeOut(deuxieme_sperm), FadeOut(grains), FadeOut(label2))

        # --- Exemple traité : l'amphimixie en 4 étapes -----------------------------
        entete_amphi = Text("L'amphimixie, en 4 étapes", font_size=25, color=YELLOW, weight="BOLD")
        entete_amphi.next_to(titre, DOWN, buff=0.45)

        cellule = Circle(radius=1.5, color="#F0E7FA", fill_color="#F0E7FA", fill_opacity=0.9, stroke_color="#74458C", stroke_width=2)
        cellule.next_to(entete_amphi, DOWN, buff=0.4)

        tete_sperm = Dot(radius=0.1, color="#1E5FA8")
        tete_sperm.move_to(cellule.get_left())
        label_etape1 = Text("1. Fusion des membranes :\ntête + flagelle pénètrent", font_size=14, color=WHITE)
        label_etape1.next_to(cellule, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Suivons maintenant les quatre étapes de l'amphimixie, "
                "après la pénétration du spermatozoïde vainqueur. Étape "
                "un : la fusion des membranes ; la tête et le flagelle du "
                "spermatozoïde pénètrent dans le cytoplasme de l'ovule."
            )
        ) as tracker:
            self.play(FadeIn(entete_amphi))
            self.play(FadeIn(cellule), FadeIn(tete_sperm))
            self.play(FadeIn(label_etape1))
            self.wait(tracker.get_remaining_duration())

        noyau_male = Dot(radius=0.14, color="#1E5FA8")
        noyau_male.move_to(cellule.get_left() + RIGHT * 0.5)
        globule_polaire = Dot(radius=0.05, color="#888888")
        globule_polaire.move_to(cellule.get_top())
        label_etape2 = Text("2. Noyau mâle formé (n) ;\n2e globule polaire expulsé", font_size=14, color=WHITE)
        label_etape2.next_to(cellule, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Étape deux : la tête du spermatozoïde gonfle et se "
                "transforme en noyau mâle, ou pronucleus mâle, haploïde. "
                "Simultanément, l'entrée du spermatozoïde déclenche chez "
                "l'ovocyte deux l'achèvement de la méiose : il expulse son "
                "deuxième globule polaire, et son noyau devient le noyau "
                "femelle, lui aussi haploïde."
            )
        ) as tracker:
            self.play(
                FadeOut(tete_sperm), FadeIn(noyau_male),
                FadeOut(label_etape1), FadeIn(label_etape2),
                globule_polaire.animate.shift(UP * 0.6), FadeIn(globule_polaire),
            )
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(globule_polaire))

        noyau_femelle = Dot(radius=0.14, color="#DE7C1F")
        noyau_femelle.move_to(cellule.get_right() + LEFT * 0.5)
        label_etape3 = Text("3. Rapprochement des 2 pronuclei\n(n + n), migration l'un vers l'autre", font_size=14, color=WHITE)
        label_etape3.next_to(cellule, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Étape trois : les deux pronuclei, mâle en bleu et femelle "
                "en orange, migrent l'un vers l'autre au sein du "
                "cytoplasme de l'ovule."
            )
        ) as tracker:
            self.play(FadeIn(noyau_femelle), FadeOut(label_etape2), FadeIn(label_etape3))
            self.play(noyau_male.animate.move_to(cellule.get_center() + LEFT * 0.15), noyau_femelle.animate.move_to(cellule.get_center() + RIGHT * 0.15))
            self.wait(tracker.get_remaining_duration())

        zygote_label = MathTex("n", "+", "n", "=", "2n", font_size=34, color="#1A1A1A")
        zygote_label.move_to(cellule.get_center())
        label_etape4 = Text("4. Amphimixie : zygote diploïde (2n)", font_size=15, color=YELLOW, weight="BOLD")
        label_etape4.next_to(cellule, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Étape quatre, l'amphimixie proprement dite : leurs "
                "membranes disparaissent et leurs chromosomes se "
                "mélangent. Le zygote ainsi formé possède un stock "
                "chromosomique diploïde : n plus n égale deux n. Chez "
                "l'Homme, vingt-trois plus vingt-trois égale "
                "quarante-six chromosomes. La fécondation restaure la "
                "diploïdie que la méiose avait réduite à l'haploïdie."
            )
        ) as tracker:
            self.play(FadeOut(noyau_male), FadeOut(noyau_femelle), FadeIn(zygote_label), FadeOut(label_etape3), FadeIn(label_etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_amphi), FadeOut(cellule), FadeOut(zygote_label), FadeOut(label_etape4))

        # --- À retenir : définition de l'amphimixie + brassage génétique ----------
        definition2 = definition_box(
            Text(
                _wrap(
                    "L'amphimixie est la fusion du noyau mâle (n) et du "
                    "noyau femelle (n) au sein du cytoplasme de l'ovule. "
                    "Elle constitue l'acte essentiel de la fécondation.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        definition2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la définition : l'amphimixie est la fusion du "
                "noyau mâle et du noyau femelle, tous deux haploïdes, au "
                "sein du cytoplasme de l'ovule. Elle constitue l'acte "
                "essentiel de la fécondation."
            )
        ) as tracker:
            self.play(FadeIn(definition2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition2))

        methode = method_box(
            Text(
                _wrap(
                    "La fécondation réalise un double brassage génétique : "
                    "chaque parent transmet la moitié de ses chromosomes, "
                    "et le nouvel individu possède un patrimoine génétique "
                    "unique, différent de celui de ses parents et de ses "
                    "frères et sœurs. C'est une source de diversité des "
                    "individus.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé à retenir : la fécondation réalise un double "
                "brassage génétique. Chaque parent transmet la moitié de "
                "ses chromosomes, et le nouvel individu possède un "
                "patrimoine génétique unique, différent de celui de ses "
                "parents et de ses frères et sœurs. C'est une source "
                "majeure de diversité des individus."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : le blocage garantit la diploïdie --------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne dites jamais que l'ovule « choisit » son "
                    "spermatozoïde : c'est le premier arrivé qui déclenche "
                    "le blocage. Sans ce blocage de la polyspermie, le "
                    "zygote ne serait pas diploïde (2n) mais polyploïde, "
                    "et non viable.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ce piège : ne dites jamais que l'ovule "
                "choisirait son spermatozoïde. C'est simplement le "
                "premier arrivé qui déclenche le blocage. Sans ce blocage "
                "de la polyspermie, le zygote ne serait pas diploïde mais "
                "polyploïde, et donc non viable."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
