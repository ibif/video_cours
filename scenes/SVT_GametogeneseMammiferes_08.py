"""
scenes/SVT_GametogeneseMammiferes_08.py — Chapitre 3 (1ereC, SVT), scène 08.

La structure de l'ovule : membrane plasmique, cytoplasme/vitellus,
noyau, zone pellucide, couronne radiée, premier globule polaire —
tableau structure/fonction, schéma annoté, et méthode « structure →
fonction » (spermatozoïde = cellule du voyage, ovule = cellule des
réserves).
Source : 1ereC/SVT.pdf, pages 30-31.
"""

import textwrap

import numpy as np
from manim import (
    DOWN,
    GREEN,
    GREY,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
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
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class StructureDeLOvule(NotionScene):
    def construct(self):
        titre = scene_title("3.8 — La structure de l'ovule")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : une cellule géante et riche en réserves -------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'ovule humain (ovocyte II expulsé à l'ovulation) "
                    "est une cellule sphérique géante à l'échelle "
                    "cellulaire : diamètre de 100 à 150 µm (visible à "
                    "l'œil nu). Il est immobile et riche en réserves : "
                    "c'est la plus grande cellule du corps humain.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'ovule humain, c'est-à-dire l'ovocyte de second ordre "
                "expulsé à l'ovulation, est une cellule sphérique géante à "
                "l'échelle cellulaire : son diamètre atteint cent à cent "
                "cinquante micromètres, visible à l'œil nu en pointe de "
                "tête d'épingle. Il est immobile et riche en réserves : "
                "c'est la plus grande cellule du corps humain."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma annoté --------------------------
        entete_schema = Text("Schéma annoté", font_size=25, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.4)

        centre = LEFT * 3.0
        vitellus = Circle(radius=0.65, color=ORANGE, fill_color=ORANGE, fill_opacity=0.85, stroke_width=0).move_to(centre)
        membrane = Circle(radius=0.65, color=WHITE, stroke_width=3, fill_opacity=0).move_to(centre)
        noyau = Circle(radius=0.12, color=RED, fill_color=RED, fill_opacity=0.9).move_to(centre + LEFT * 0.15 + UP * 0.15)
        zone_pellucide = Circle(radius=0.85, color=YELLOW, stroke_width=4, fill_opacity=0).move_to(centre)
        couronne = VGroup()
        for k in range(12):
            angle = k * (2 * np.pi / 12)
            cell = Circle(radius=0.1, color=GREEN, fill_color=GREEN, fill_opacity=0.7)
            cell.move_to(centre + 1.12 * np.array([np.cos(angle), np.sin(angle), 0]))
            couronne.add(cell)
        globule_polaire = Circle(radius=0.13, color=GREY, fill_color=GREY, fill_opacity=0.8)
        globule_polaire.move_to(centre + RIGHT * 0.75)

        ovule_schema = VGroup(couronne, zone_pellucide, vitellus, membrane, noyau, globule_polaire)

        label_membrane = Text("Membrane plasmique\n(oolemme)", font_size=14, color=WHITE)
        label_membrane.move_to(RIGHT * 2.8 + UP * 2.0)
        arrow_membrane = Arrow(label_membrane.get_bottom(), membrane.get_top() + LEFT * 0.1, buff=0.1, color=WHITE)

        label_vitellus = Text("Cytoplasme / vitellus\n(réserves nutritives)", font_size=14, color=ORANGE)
        label_vitellus.move_to(RIGHT * 2.8 + UP * 0.8)
        arrow_vitellus = Arrow(label_vitellus.get_left(), vitellus.get_center() + RIGHT * 0.2, buff=0.1, color=WHITE)

        label_noyau = Text("Noyau (n)\nbloqué en métaphase II", font_size=14, color=RED)
        label_noyau.move_to(RIGHT * 2.8 + DOWN * 0.4)
        arrow_noyau = Arrow(label_noyau.get_left(), noyau.get_center(), buff=0.1, color=WHITE)

        label_zp = Text("Zone pellucide", font_size=14, color=YELLOW)
        label_zp.move_to(RIGHT * 2.8 + DOWN * 1.6)
        arrow_zp = Arrow(label_zp.get_left(), zone_pellucide.get_bottom() + LEFT * 0.3, buff=0.1, color=WHITE)

        label_couronne = Text("Couronne radiée", font_size=14, color=GREEN)
        label_couronne.move_to(centre + DOWN * 2.0)
        arrow_couronne = Arrow(label_couronne.get_top(), couronne[8].get_center(), buff=0.1, color=WHITE)

        label_gp = Text("1er globule polaire", font_size=14, color=GREY)
        label_gp.move_to(centre + UP * 1.9)
        arrow_gp = Arrow(label_gp.get_bottom(), globule_polaire.get_center(), buff=0.1, color=WHITE)

        schema_full = VGroup(
            ovule_schema,
            label_membrane, arrow_membrane,
            label_vitellus, arrow_vitellus,
            label_noyau, arrow_noyau,
            label_zp, arrow_zp,
            label_couronne, arrow_couronne,
            label_gp, arrow_gp,
        )

        with self.voiceover(
            text=(
                "Observons le schéma de l'ovule. Au centre, le noyau, "
                "haploïde, encore bloqué en métaphase de méiose deux. "
                "Autour, un cytoplasme abondant, le vitellus, chargé de "
                "granules de réserves. Ce cytoplasme est délimité par la "
                "membrane plasmique, ou oolemme. Plus loin, la zone "
                "pellucide, épaisse enveloppe glycoprotéique translucide. "
                "Encore plus loin, la couronne radiée, des cellules "
                "folliculaires restées accolées. Enfin, tout près de la "
                "membrane, dans l'espace sous la zone pellucide, le "
                "premier globule polaire, petite cellule qui va dégénérer."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(ovule_schema))
            self.play(
                FadeIn(label_membrane), FadeIn(arrow_membrane),
                FadeIn(label_vitellus), FadeIn(arrow_vitellus),
                FadeIn(label_noyau), FadeIn(arrow_noyau),
                FadeIn(label_zp), FadeIn(arrow_zp),
                FadeIn(label_couronne), FadeIn(arrow_couronne),
                FadeIn(label_gp), FadeIn(arrow_gp),
            )
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(schema_full))

        # --- Exemple traité : tableau structure / fonction ----------------------
        entete_tab = Text("Structure et fonction", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        tableau = _bullets(
            [
                "Membrane plasmique : reconnaissance et fusion avec le "
                "spermatozoïde.",
                "Cytoplasme (ooplasme) : matériel des premières "
                "divisions de l'embryon.",
                "Vitellus : nutrition de l'embryon les premiers jours.",
                "Noyau : patrimoine génétique maternel (n).",
                "Zone pellucide : protection, reconnaissance des "
                "spermatozoïdes, blocage de la polyspermie.",
                "Couronne radiée : protection et nutrition, franchie par "
                "les enzymes acrosomiales.",
                "1er globule polaire : déchet de la méiose I, dégénère.",
            ],
            font_size=18,
            width=52,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Reprenons structure et fonction. La membrane plasmique "
                "assure la reconnaissance et la fusion avec le "
                "spermatozoïde. Le cytoplasme, riche en organites et en "
                "ARN, fournit le matériel des toutes premières divisions "
                "de l'embryon, tandis que le vitellus, ses granules de "
                "réserves, nourrit l'embryon durant les premiers jours. Le "
                "noyau porte le patrimoine génétique maternel. La zone "
                "pellucide protège l'ovule, porte les récepteurs de "
                "reconnaissance spécifique des spermatozoïdes, et bloque "
                "la polyspermie après la fécondation. La couronne radiée "
                "protège et nourrit l'ovule ; elle est franchie par les "
                "enzymes de l'acrosome. Enfin, le premier globule polaire "
                "n'est qu'un déchet de la méiose un, destiné à dégénérer."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : méthode « structure → fonction » ------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Raisonner « structure → fonction » : le spermatozoïde "
                    "est la cellule du voyage — petit, léger, mobile "
                    "(flagelle + mitochondries), capable de percer les "
                    "enveloppes (acrosome). L'ovule est la cellule des "
                    "réserves — gros, chargé de vitellus pour nourrir le "
                    "futur embryon, immobile, protégé par la zone "
                    "pellucide et la couronne radiée.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.4,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons une méthode pour tout devoir de niveau : "
                "raisonner structure vers fonction. Le spermatozoïde est "
                "la cellule du voyage : petit, léger, car peu de "
                "cytoplasme, mobile grâce au flagelle et aux "
                "mitochondries, capable de percer les enveloppes grâce à "
                "l'acrosome. L'ovule, à l'inverse, est la cellule des "
                "réserves : gros, chargé de vitellus pour nourrir le futur "
                "embryon, immobile car transporté par la trompe, protégé "
                "par la zone pellucide et la couronne radiée."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "N'inverse jamais acrosome et vitellus : l'acrosome "
                    "appartient au spermatozoïde (enzymes de "
                    "pénétration), le vitellus appartient à l'ovule "
                    "(réserves nutritives). La zone pellucide entoure "
                    "toujours l'ovule, jamais le spermatozoïde.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : n'inverse jamais acrosome et vitellus. "
                "L'acrosome appartient au spermatozoïde, ce sont des "
                "enzymes de pénétration ; le vitellus appartient à "
                "l'ovule, ce sont des réserves nutritives. La zone "
                "pellucide, elle, entoure toujours l'ovule, jamais le "
                "spermatozoïde."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
