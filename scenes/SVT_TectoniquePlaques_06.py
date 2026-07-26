"""
scenes/SVT_TectoniquePlaques_06.py — Chapitre 8 (1ereC, SVT), scène 06.

III.C L'âge des fonds océaniques (jamais plus de 180-200 Ma, âge croissant
symétriquement, épaisseur des sédiments croissante, topographie : rift
axial surélevé) + point clé méthode "trois preuves convergent" ; III.D
confirmation par les points chauds (alignement des volcans, exemple
Hawaï). Source : 1ereC/SVT.pdf, page 89.
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
    Circle,
    Create,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class AgeDesFondsEtPointsChauds(NotionScene):
    def construct(self):
        titre = scene_title("III. L'âge des fonds océaniques")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : les fonds océaniques sont jeunes -----------------------
        intro = Text(
            _wrap(
                "Les datations (potassium-argon) et les forages profonds "
                "montrent qu'aucune croûte océanique n'est plus ancienne "
                "que 180 à 200 Ma, alors que certaines roches continentales "
                "ont près de 4 Ga. Les fonds océaniques sont donc jeunes et "
                "se renouvellent.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les datations, par la méthode potassium-argon, et les "
                "forages profonds réalisés dans les océans montrent "
                "qu'aucune croûte océanique n'est plus ancienne que cent "
                "quatre-vingts à deux cents millions d'années, alors que "
                "certaines roches continentales approchent quatre "
                "milliards d'années. Les fonds océaniques sont donc "
                "étonnamment jeunes, et se renouvellent en permanence."
            )
        ) as tracker:
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : schéma âge / sédiments / relief -----
        ocean = Rectangle(width=10.0, height=1.6, fill_color=BLUE_E, fill_opacity=0.5, stroke_width=0)

        # relief : rift surélevé au centre, profondeur croissante vers les bords
        relief_pts = [
            [-5.0, -0.3, 0], [-2.5, -0.5, 0], [-1.0, 0.1, 0], [0, 0.5, 0],
            [1.0, 0.1, 0], [2.5, -0.5, 0], [5.0, -0.3, 0],
        ]
        relief = VGroup(*[Line(relief_pts[i], relief_pts[i + 1], color=ORANGE, stroke_width=5) for i in range(len(relief_pts) - 1)])

        # sédiments : couche fine près de l'axe, épaisse loin de l'axe
        sed_g = Rectangle(width=4.0, height=0.35, fill_color=WHITE, fill_opacity=0.4, stroke_width=0)
        sed_g.move_to([-3.2, -0.55, 0])
        sed_d = Rectangle(width=4.0, height=0.35, fill_color=WHITE, fill_opacity=0.4, stroke_width=0)
        sed_d.move_to([3.2, -0.55, 0])

        axe_label = Text("axe (jeune)", font_size=15, color=YELLOW).move_to([0, 0.85, 0])
        bord_g_label = Text("bord (ancien,\nsédiments épais)", font_size=13, color=WHITE).move_to([-5.0, 0.85, 0])
        bord_d_label = Text("bord (ancien,\nsédiments épais)", font_size=13, color=WHITE).move_to([5.0, 0.85, 0])

        schema = VGroup(ocean, sed_g, sed_d, relief, axe_label, bord_g_label, bord_d_label)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Trois observations complémentaires confirment "
                "l'expansion. D'abord, l'âge de la croûte océanique "
                "augmente régulièrement avec la distance à l'axe de la "
                "dorsale, de façon symétrique : les fonds les plus jeunes "
                "sont sur la dorsale, les plus vieux près des fosses ou des "
                "continents."
            )
        ) as tracker:
            self.play(FadeIn(ocean))
            self.play(Create(relief), FadeIn(axe_label))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Ensuite, l'épaisseur des sédiments déposés sur le fond "
                "augmente elle aussi avec la distance à la dorsale : la "
                "croûte jeune a eu moins de temps pour se recouvrir de "
                "sédiments."
            )
        ) as tracker:
            self.play(FadeIn(sed_g), FadeIn(sed_d), FadeIn(bord_g_label), FadeIn(bord_d_label))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Enfin, la topographie change : la dorsale est surélevée, "
                "car sa lithosphère est chaude et peu dense, et creusée "
                "d'une vallée axiale, le rift ; la profondeur de l'océan "
                "augmente avec l'âge de la croûte, qui se refroidit, se "
                "contracte et devient plus dense en s'éloignant de l'axe."
            )
        ) as tracker:
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir : point clé méthode ------------------------------------
        point_cle = method_box(
            Text(
                _wrap(
                    "Point clé : trois preuves indépendantes convergent — "
                    "anomalies magnétiques symétriques, âge croissant des "
                    "fonds océaniques, épaisseur croissante des sédiments. "
                    "L'expansion océanique est un fait mesuré : les océans "
                    "s'élargissent de 1 à 10 cm/an selon les dorsales.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        point_cle.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons ce point clé : trois preuves indépendantes "
                "convergent — les anomalies magnétiques symétriques, l'âge "
                "croissant des fonds océaniques, et l'épaisseur croissante "
                "des sédiments. L'expansion océanique n'est donc pas une "
                "simple hypothèse : c'est un fait mesuré. Les océans "
                "s'élargissent de un à dix centimètres par an, selon les "
                "dorsales."
            )
        ) as tracker:
            self.play(FadeIn(point_cle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(point_cle))

        # --- Exemple traité : confirmation par les points chauds --------------
        entete_pc = Text("Confirmation par les points chauds", font_size=25, color=YELLOW, weight="BOLD")
        entete_pc.next_to(titre, DOWN, buff=0.5)

        pc_texte = Text(
            _wrap(
                "Certains volcans intraplaques (ex. Hawaï, sur la plaque "
                "pacifique) sont alignés, et d'autant plus âgés qu'ils sont "
                "éloignés du volcan actuellement actif. On les explique par "
                "le passage de la plaque au-dessus d'un point chaud fixe "
                "dans le manteau.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        pc_texte.next_to(entete_pc, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une dernière confirmation, indépendante, vient des points "
                "chauds. Certains volcans situés à l'intérieur des plaques, "
                "comme l'archipel d'Hawaï sur la plaque pacifique, sont "
                "alignés, et d'autant plus âgés qu'ils sont éloignés du "
                "volcan actuellement actif. On les explique par le passage "
                "de la plaque au-dessus d'un point chaud fixe, ancré dans "
                "le manteau profond."
            )
        ) as tracker:
            self.play(FadeIn(entete_pc))
            self.play(FadeIn(pc_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pc), FadeOut(pc_texte))

        # --- Schéma : alignement de volcans Hawaï -----------------------------
        point_chaud = Circle(radius=0.15, fill_color=RED, fill_opacity=1, stroke_width=0)
        point_chaud.move_to([3.5, 0, 0])
        label_pc = Text("point chaud (fixe)", font_size=14, color=RED).next_to(point_chaud, DOWN, buff=0.15)

        volcans = VGroup()
        distances = [3.5, 2.0, 0.5, -1.2, -3.0]
        ages_v = ["actif", "1 Ma", "3 Ma", "5 Ma", "8 Ma"]
        for dist, age in zip(distances, ages_v):
            v = Circle(radius=0.18, fill_color=ORANGE, fill_opacity=0.85, stroke_color=WHITE, stroke_width=1)
            v.move_to([dist, 0.6, 0])
            lbl = Text(age, font_size=13, color=WHITE).next_to(v, UP, buff=0.1)
            volcans.add(VGroup(v, lbl))

        fleche_deplacement = Line([-3.0, -0.6, 0], [3.5, -0.6, 0], color=WHITE, stroke_width=3)
        label_deplacement = Text("sens de déplacement de la plaque", font_size=15, color=WHITE)
        label_deplacement.next_to(fleche_deplacement, DOWN, buff=0.15)

        schema_hawaii = VGroup(point_chaud, label_pc, volcans, fleche_deplacement, label_deplacement)
        schema_hawaii.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'alignement des volcans enregistre ainsi le sens et la "
                "vitesse du déplacement de la plaque : c'est une "
                "confirmation indépendante, et visuelle, de la mobilité des "
                "plaques."
            )
        ) as tracker:
            self.play(FadeIn(point_chaud), FadeIn(label_pc))
            self.play(FadeIn(volcans))
            self.play(Create(fleche_deplacement), FadeIn(label_deplacement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_hawaii), FadeOut(titre))
