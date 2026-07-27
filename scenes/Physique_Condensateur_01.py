"""
scenes/Physique_Condensateur_01.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 01.

§ 1. Constitution et symbole d'un condensateur. Deux armatures
conductrices séparées par un isolant (diélectrique). Charges opposées sur
les deux armatures q_A=-q_B, charge notée q=|q_A|=|q_B|. Tension
u=V_A-V_B. Symbole normalisé (deux traits parallèles). Types de
condensateurs (film, céramique, variable, électrolytique polarisé —
attention à la polarité).
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 1).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _condensateur_arme(gap: float = 0.35, hauteur: float = 1.2, fil: float = 1.1):
    """Deux armatures (plaques conductrices) en regard, séparées par un
    diélectrique, avec fils de connexion — construit uniquement avec Line
    et Rectangle (aucune bibliothèque externe)."""
    armature_a = Line(UP * hauteur / 2, DOWN * hauteur / 2, stroke_width=7, color=WHITE)
    armature_a.shift(LEFT * gap / 2)
    armature_b = Line(UP * hauteur / 2, DOWN * hauteur / 2, stroke_width=7, color=WHITE)
    armature_b.shift(RIGHT * gap / 2)

    dielectrique = Rectangle(
        width=gap * 0.85, height=hauteur * 0.92,
        fill_color="#3A3A3A", fill_opacity=0.6, stroke_width=0,
    )

    fil_gauche = Line(armature_a.get_center() + LEFT * gap / 2, armature_a.get_center() + LEFT * (gap / 2 + fil), stroke_width=3, color=WHITE)
    fil_droit = Line(armature_b.get_center() + RIGHT * gap / 2, armature_b.get_center() + RIGHT * (gap / 2 + fil), stroke_width=3, color=WHITE)

    label_a = Text("A", font_size=22, color=YELLOW).next_to(armature_a, UP, buff=0.15)
    label_b = Text("B", font_size=22, color=YELLOW).next_to(armature_b, UP, buff=0.15)

    return VGroup(dielectrique, armature_a, armature_b, fil_gauche, fil_droit, label_a, label_b)


def _condensateur_charges(gap: float = 0.35, hauteur: float = 1.2):
    """Même schéma, avec les signes des charges portées par chaque
    armature (qA positive, qB négative) affichés en vis-à-vis."""
    base = _condensateur_arme(gap=gap, hauteur=hauteur)
    signes_a = VGroup(*[Text("+", font_size=20, color=RED) for _ in range(3)]).arrange(DOWN, buff=0.18)
    signes_a.next_to(base[1], LEFT, buff=0.08)
    signes_b = VGroup(*[Text("−", font_size=20, color="#4FA8FF") for _ in range(3)]).arrange(DOWN, buff=0.18)
    signes_b.next_to(base[2], RIGHT, buff=0.08)
    return VGroup(base, signes_a, signes_b)


class ConstitutionSymboleCondensateur(NotionScene):
    def construct(self):
        titre = scene_title("Le condensateur : constitution et symbole")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Certains circuits doivent stocker de l'énergie électrique "
                "pendant un court instant, puis la restituer rapidement : "
                "flash d'un appareil photo, mémoire d'un ordinateur. Le "
                "composant responsable de ce stockage est le condensateur.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Certains circuits doivent stocker de l'énergie électrique "
                "pendant un court instant, puis la restituer très "
                "rapidement : c'est le cas du flash d'un appareil photo, "
                "ou de la mémoire d'un ordinateur. Le composant responsable "
                "de ce stockage s'appelle le condensateur. Découvrons sa "
                "constitution."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : constitution et symbole ------------------------
        schema = _condensateur_arme()
        schema.scale(1.3)
        schema.next_to(titre, DOWN, buff=0.6)

        definition_condens = definition_box(
            VGroup(
                Text("Un condensateur est formé de deux armatures conductrices", font_size=20),
                Text("en regard, séparées par un isolant appelé diélectrique.", font_size=20),
                Text("Symbole normalisé : deux traits parallèles reliés par des fils.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.4,
        )
        definition_condens.next_to(schema, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un condensateur est constitué de deux armatures "
                "conductrices placées en regard l'une de l'autre, séparées "
                "par un isolant appelé diélectrique : de l'air, du "
                "plastique, ou de la céramique par exemple. Son symbole "
                "normalisé reprend cette idée : deux traits parallèles, "
                "reliés chacun à un fil de connexion."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(definition_condens))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(definition_condens))

        # --- Raisonnement : charge q et tension u ---------------------------
        schema_charges = _condensateur_charges()
        schema_charges.scale(1.2)
        schema_charges.next_to(titre, DOWN, buff=0.55)

        definition_qu = definition_box(
            VGroup(
                Text("Sous tension, les armatures portent des charges opposées :", font_size=20),
                MathTex(r"q_A = -\,q_B", font_size=28),
                Text("On appelle charge du condensateur la valeur commune :", font_size=20),
                MathTex(r"q = |q_A| = |q_B|", font_size=28),
                Text("La tension aux bornes est u = V_A − V_B (armature A vers B).", font_size=20),
            ).arrange(DOWN, buff=0.18),
            box_width=11.4,
        )
        definition_qu.next_to(schema_charges, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Lorsqu'on branche un condensateur sous tension, ses deux "
                "armatures se chargent avec des charges opposées : la "
                "charge de l'armature A vaut moins la charge de l'armature "
                "B. On appelle charge du condensateur la valeur commune, "
                "notée q, égale à la valeur absolue de la charge de chaque "
                "armature. La tension à ses bornes est u égale V A moins V "
                "B, où A désigne l'armature reliée au potentiel le plus "
                "élevé quand u est positive."
            )
        ) as tracker:
            self.play(FadeIn(schema_charges))
            self.play(FadeIn(definition_qu))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_charges), FadeOut(definition_qu))

        # --- Exemple : identifier signes et types -----------------------------
        exemple = example_box(
            VGroup(
                Text("Un condensateur porte q_A = +8 µC sur son armature A.", font_size=20),
                MathTex(r"q_B = -q_A = -8\ \mu\text{C}, \qquad q = |q_A| = 8\ \mu\text{C}", font_size=26),
                Text("Types courants : condensateur film, céramique, variable,", font_size=20),
                Text("et électrolytique (celui-ci est POLARISÉ, il possède un + et un −).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : un condensateur porte une charge q A égale plus "
                "huit microcoulombs sur son armature A. Son armature B "
                "porte donc moins huit microcoulombs, et la charge du "
                "condensateur vaut huit microcoulombs. On rencontre "
                "plusieurs types de condensateurs : à film plastique, "
                "céramique, variable, ou électrolytique. Ce dernier est "
                "polarisé : il possède une borne plus et une borne moins "
                "qu'il ne faut jamais inverser."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Deux armatures conductrices + un diélectrique isolant.", font_size=20),
                MathTex(r"q_A = -q_B, \quad q = |q_A| = |q_B|, \quad u = V_A - V_B", font_size=25),
            ).arrange(DOWN, buff=0.22),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : un condensateur est formé de deux "
                "armatures conductrices séparées par un diélectrique "
                "isolant. Les charges portées par les deux armatures sont "
                "opposées, q A égale moins q B, la charge du condensateur "
                "est leur valeur absolue commune, et la tension à ses "
                "bornes vaut V A moins V B."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter -----------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Un condensateur ÉLECTROLYTIQUE est POLARISÉ : brancher", font_size=20),
                Text("   sa borne − sur le + du circuit peut le détruire (voire", font_size=20),
                Text("   provoquer une explosion). Respecter TOUJOURS la polarité.", font_size=20),
                Text("• q désigne la charge du condensateur, pas la charge totale", font_size=20),
                Text("   des deux armatures (dont la somme est nulle).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter absolument. Un condensateur "
                "électrolytique est polarisé : brancher sa borne moins sur "
                "le plus du circuit peut le détruire, voire provoquer une "
                "explosion — il faut toujours respecter sa polarité. Et il "
                "ne faut pas confondre la charge q du condensateur, qui est "
                "une valeur absolue, avec la charge totale des deux "
                "armatures, qui est toujours nulle puisqu'elles sont "
                "opposées."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
