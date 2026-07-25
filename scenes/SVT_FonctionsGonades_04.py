"""
scenes/SVT_FonctionsGonades_04.py — Chapitre 1 (1ereD, SVT), scène 04.

§ 1.3.1-1.3.2 Structure du testicule et spermatogenèse : cellules
germinales du tube séminifère, définition, 4 phases, chiffres clés
(100 millions/jour, 70 jours, 35°C). Source : 1ereD/SVT.pdf, pages 9-10.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Annulus,
    Arrow,
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
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class StructureTesticuleEtSpermatogenese(NotionScene):
    def construct(self):
        titre = scene_title("1.3 — Structure du testicule et spermatogenèse")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : schéma du tube séminifère ----------------------------
        outer = Annulus(inner_radius=1.55, outer_radius=1.95, color=BLUE, fill_opacity=0.85)
        ring2 = Annulus(inner_radius=1.05, outer_radius=1.55, color=GREEN, fill_opacity=0.85)
        ring3 = Annulus(inner_radius=0.55, outer_radius=1.05, color=ORANGE, fill_opacity=0.85)
        center = Circle(radius=0.55, color=RED, fill_opacity=0.85)
        tube = VGroup(outer, ring2, ring3, center)
        tube.shift(LEFT * 3.3 + DOWN * 0.3)

        label_outer = Text("Spermatogonies", font_size=20, color=WHITE)
        label_outer.next_to(tube, UP, buff=0.9).shift(LEFT * 0.3)
        arrow_outer = Arrow(label_outer.get_bottom(), outer.get_top(), buff=0.1, color=WHITE)

        label_sertoli = Text("Cellules de Sertoli\n(nourricières)", font_size=18, color=WHITE)
        label_sertoli.next_to(tube, RIGHT, buff=1.4).shift(UP * 1.0)
        arrow_sertoli = Arrow(label_sertoli.get_left(), ring2.get_right(), buff=0.1, color=WHITE)

        label_center = Text("Spermatozoïdes\n(lumière du tube)", font_size=18, color=WHITE)
        label_center.next_to(tube, RIGHT, buff=1.4).shift(DOWN * 1.0)
        arrow_center = Arrow(label_center.get_left(), center.get_right(), buff=0.1, color=WHITE)

        leydig_dots = VGroup(*[Dot(color=YELLOW) for _ in range(5)]).arrange(RIGHT, buff=0.15)
        leydig_dots.next_to(tube, DOWN, buff=0.7)
        label_leydig = Text("Cellules interstitielles de Leydig", font_size=18, color=YELLOW)
        label_leydig.next_to(leydig_dots, DOWN, buff=0.15)

        schema = VGroup(
            tube, label_outer, arrow_outer, label_sertoli, arrow_sertoli,
            label_center, arrow_center, leydig_dots, label_leydig,
        )
        schema.next_to(titre, DOWN, buff=0.4).shift(LEFT * 0.3)

        with self.voiceover(
            text=(
                "Chaque testicule renferme de longs tubes enroulés, les tubes "
                "séminifères. Sur une coupe, la paroi contient des cellules "
                "germinales à tous les stades : à la périphérie, contre la "
                "membrane basale, les spermatogonies ; en se rapprochant du "
                "centre, les spermatocytes puis les spermatides, et enfin les "
                "spermatozoïdes, libérés dans la lumière centrale. Entre les "
                "cellules germinales, de grandes cellules de Sertoli "
                "nourrissent la fabrication des gamètes. Entre les tubes se "
                "trouve un tissu interstitiel avec les cellules de Leydig, "
                "responsables de la fonction endocrine du testicule."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(tube))
            self.play(FadeIn(label_outer), FadeIn(arrow_outer))
            self.play(FadeIn(label_sertoli), FadeIn(arrow_sertoli))
            self.play(FadeIn(label_center), FadeIn(arrow_center))
            self.play(FadeIn(leydig_dots), FadeIn(label_leydig))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Animation du raisonnement : définition + 4 phases -------------
        definition = definition_box(
            Text(
                _wrap(
                    "La spermatogenèse est l'ensemble des phénomènes qui, "
                    "dans les tubes séminifères, transforment une "
                    "spermatogonie en spermatozoïdes. Elle débute à la "
                    "puberté et se poursuit en continu toute la vie.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La spermatogenèse est l'ensemble des phénomènes qui, dans "
                "les tubes séminifères, transforment une spermatogonie en "
                "spermatozoïdes. Elle débute à la puberté et se poursuit, de "
                "façon continue, pendant toute la vie de l'homme."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # Chaîne des 4 phases avec chromosomes
        etapes_labels = [
            ("Spermatogonie", "2n=46"),
            ("Spermatocyte I", "2n=46"),
            ("Spermatocytes II", "n=23"),
            ("Spermatides", "n=23"),
            ("Spermatozoïdes", "n=23"),
        ]
        cellules = VGroup()
        for nom, formule in etapes_labels:
            nom_txt = Text(nom, font_size=19, color=WHITE)
            formule_txt = MathTex(formule.replace("n=", "n = "), font_size=26, color=YELLOW)
            bloc = VGroup(nom_txt, formule_txt).arrange(DOWN, buff=0.15)
            cellules.add(bloc)
        cellules.arrange(RIGHT, buff=1.1)
        cellules.next_to(titre, DOWN, buff=1.3)
        cellules.scale(0.8)

        fleches = VGroup(
            *[
                Arrow(cellules[i].get_right(), cellules[i + 1].get_left(), buff=0.08, color=WHITE)
                for i in range(len(cellules) - 1)
            ]
        )

        phases_labels = VGroup(
            Text("Multiplication", font_size=15, color=BLUE),
            Text("Croissance", font_size=15, color=GREEN),
            Text("Méiose I", font_size=15, color=ORANGE),
            Text("Méiose II\n+ Spermiogenèse", font_size=15, color=RED),
        )
        for i, lbl in enumerate(phases_labels):
            lbl.next_to(fleches[i], UP, buff=0.15)

        with self.voiceover(
            text=(
                "La spermatogenèse enchaîne quatre phases. Phase de "
                "multiplication : les spermatogonies, à deux n égale "
                "quarante-six chromosomes, se divisent par mitoses. Phase de "
                "croissance : chaque cellule grossit et devient un "
                "spermatocyte premier, toujours à deux n égale quarante-six. "
                "Phase de maturation : la méiose transforme le spermatocyte "
                "premier en deux spermatocytes seconds, à n égale vingt-trois, "
                "puis en quatre spermatides. Enfin, la spermiogenèse : chaque "
                "spermatide perd son cytoplasme, condense son noyau et "
                "développe un flagelle pour devenir un spermatozoïde, à n "
                "égale vingt-trois chromosomes."
            )
        ) as tracker:
            self.play(FadeIn(cellules))
            self.play(FadeIn(fleches), FadeIn(phases_labels))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cellules), FadeOut(fleches), FadeOut(phases_labels))

        # --- Exemple traité : suivre une spermatogonie ----------------------
        entete_ex = Text("Exemple traité", font_size=27, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        bilan = MathTex(
            r"1 \text{ spermatocyte I} \;\longrightarrow\; 4 \text{ spermatozoïdes}",
            font_size=32,
            color=WHITE,
        )
        bilan.next_to(entete_ex, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Suivons le bilan d'une seule cellule : un spermatocyte "
                "premier, après les deux divisions de la méiose, donne "
                "quatre spermatides, qui deviennent quatre spermatozoïdes "
                "tous fonctionnels. Rien ne se perd dans la lignée mâle."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(bilan))

        # --- À retenir : chiffres clés --------------------------------------
        chiffres = _bullets(
            [
                "Durée de fabrication d'un spermatozoïde : environ 70 jours.",
                "Production : environ 100 millions de spermatozoïdes par "
                "jour, soit plus de 1000 par seconde.",
                "Température nécessaire : environ 35°C, d'où la position "
                "des testicules dans les bourses.",
            ],
            width=48,
        )
        entete_chiffres = Text("À retenir — chiffres clés", font_size=27, color=YELLOW, weight="BOLD")
        entete_chiffres.next_to(titre, DOWN, buff=0.5)
        chiffres.next_to(entete_chiffres, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Trois chiffres à retenir : la fabrication complète d'un "
                "spermatozoïde dure environ soixante-dix jours ; la "
                "production est massive, de l'ordre de cent millions de "
                "spermatozoïdes par jour, soit plus de mille par seconde ; et "
                "elle exige une température voisine de trente-cinq degrés, ce "
                "qui explique la position des testicules dans les bourses."
            )
        ) as tracker:
            self.play(FadeIn(entete_chiffres))
            self.play(FadeIn(chiffres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_chiffres), FadeOut(chiffres))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Une spermatogonie à 2n=46 donne des spermatozoïdes à "
                    "n=23, jamais à 46 : la méiose ne fabrique pas de "
                    "chromosomes, elle les répartit. Et un spermatozoïde "
                    "n'est pas fabriqué en un instant : sa production dure "
                    "environ 70 jours.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention : une spermatogonie à deux n égale quarante-six "
                "donne des spermatozoïdes à n égale vingt-trois, jamais à "
                "quarante-six ; la méiose ne fabrique pas de chromosomes, "
                "elle les répartit. Et un spermatozoïde n'est pas créé en un "
                "instant : sa fabrication a duré environ soixante-dix jours."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
