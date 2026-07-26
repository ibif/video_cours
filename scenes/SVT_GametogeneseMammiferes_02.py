"""
scenes/SVT_GametogeneseMammiferes_02.py — Chapitre 3 (1ereC, SVT), scène 02.

La spermatogenèse : localisation (tubules séminifères, organisation en
couches concentriques, cellules de Sertoli, schéma en coupe transversale)
et les quatre étapes détaillées (multiplication par mitoses, croissance,
maturation/méiose, spermiogenèse avec transformations de la spermatide).
Source : 1ereC/SVT.pdf, pages 23-25.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    PINK,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    Triangle,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class SpermatogeneseLocalisationEtEtapes(NotionScene):
    def construct(self):
        titre = scene_title("3.1 — La spermatogenèse : localisation et étapes")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : définition -----------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La spermatogenèse est l'ensemble des transformations "
                    "qui conduisent, à partir des spermatogonies "
                    "diploïdes, à la formation des spermatozoïdes "
                    "haploïdes. Elle comporte quatre phases : "
                    "multiplication, croissance, maturation (méiose) et "
                    "spermiogenèse.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La spermatogenèse est l'ensemble des transformations qui "
                "conduisent, à partir des spermatogonies diploïdes, à la "
                "formation des spermatozoïdes haploïdes. Elle comporte "
                "quatre phases : la multiplication, la croissance, la "
                "maturation, c'est-à-dire la méiose, et la spermiogenèse."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : localisation et schéma du tubule ------
        entete_loc = Text("Localisation : le tubule séminifère", font_size=24, color=YELLOW, weight="BOLD")
        entete_loc.next_to(titre, DOWN, buff=0.4)

        loc_texte = _bullets(
            [
                "Testicules, dans le scrotum, à ~35°C (2°C sous la "
                "température corporelle).",
                "250 à 300 lobules par testicule, chacun avec 1 à 4 "
                "tubules séminifères très enroulés.",
            ],
            font_size=19,
            width=48,
        )
        loc_texte.next_to(entete_loc, DOWN, buff=0.3).to_edge(LEFT, buff=1.0)

        # Schéma : coupe transversale du tubule séminifère (couches
        # concentriques). Le cercle le plus grand est dessiné en premier,
        # les cercles plus petits sont superposés dessus.
        c_spermatogonies = Circle(radius=1.55, color=BLUE, fill_color=BLUE, fill_opacity=0.55, stroke_width=2)
        c_spermatocytes = Circle(radius=1.1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.6, stroke_width=2)
        c_spermatides = Circle(radius=0.65, color=PINK, fill_color=PINK, fill_opacity=0.65, stroke_width=2)
        c_lumiere = Circle(radius=0.28, color=WHITE, fill_color=WHITE, fill_opacity=0.15, stroke_width=2)
        coupe = VGroup(c_spermatogonies, c_spermatocytes, c_spermatides, c_lumiere)
        coupe.move_to(RIGHT * 3.0 + DOWN * 0.3)

        # Cellules de Sertoli : petits triangles verts, disposés en couronne
        # entre la périphérie et la zone médiane.
        sertoli = VGroup()
        import numpy as np

        for k in range(8):
            angle = k * (2 * np.pi / 8)
            tri = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=0.9, stroke_width=1)
            tri.scale(0.13)
            tri.move_to(coupe.get_center() + 1.3 * np.array([np.cos(angle), np.sin(angle), 0]))
            sertoli.add(tri)

        label_spermatogonies = Text("Spermatogonies (2n)\npériphérie", font_size=15, color=BLUE)
        label_spermatogonies.next_to(coupe, LEFT, buff=1.6).shift(UP * 1.3)
        arrow_sg = Arrow(label_spermatogonies.get_right(), c_spermatogonies.get_top() + LEFT * 0.3, buff=0.08, color=WHITE)

        label_sertoli = Text("Cellules de Sertoli\n(nourricières)", font_size=15, color=GREEN)
        label_sertoli.next_to(coupe, LEFT, buff=1.6).shift(DOWN * 0.6)
        arrow_st = Arrow(label_sertoli.get_right(), sertoli[3].get_center(), buff=0.08, color=WHITE)

        label_spermatides = Text("Spermatides\nprès de la lumière", font_size=15, color=PINK)
        label_spermatides.next_to(coupe, RIGHT, buff=0.6).shift(UP * 1.0)
        arrow_sp = Arrow(label_spermatides.get_left(), c_spermatides.get_right(), buff=0.08, color=WHITE)

        label_lumiere = Text("Lumière", font_size=14, color=WHITE)
        label_lumiere.next_to(coupe, RIGHT, buff=0.6).shift(DOWN * 1.0)
        arrow_lum = Arrow(label_lumiere.get_left(), c_lumiere.get_right(), buff=0.08, color=WHITE)

        schema = VGroup(
            coupe, sertoli, label_spermatogonies, arrow_sg,
            label_sertoli, arrow_st, label_spermatides, arrow_sp,
            label_lumiere, arrow_lum,
        )

        with self.voiceover(
            text=(
                "La spermatogenèse se déroule dans les tubules séminifères "
                "des testicules, organes situés dans le scrotum, à une "
                "température d'environ trente-cinq degrés, soit deux "
                "degrés en dessous de la température corporelle. Chaque "
                "testicule contient deux cent cinquante à trois cents "
                "lobules, renfermant chacun un à quatre tubules "
                "séminifères très enroulés. Sur une coupe transversale, on "
                "observe une organisation en couches concentriques : les "
                "spermatogonies, cellules les plus jeunes, sont à la "
                "périphérie, contre la membrane basale ; les spermatocytes "
                "occupent la zone médiane ; les spermatides, cellules les "
                "plus évoluées, sont proches de la lumière, au centre du "
                "tubule. Les cellules de Sertoli, cellules nourricières, "
                "encadrent les cellules germinales et les accompagnent "
                "durant tout le processus."
            )
        ) as tracker:
            self.play(FadeIn(entete_loc))
            self.play(FadeIn(loc_texte))
            self.play(FadeIn(coupe))
            self.play(FadeIn(sertoli))
            self.play(
                FadeIn(label_spermatogonies), FadeIn(arrow_sg),
                FadeIn(label_sertoli), FadeIn(arrow_st),
                FadeIn(label_spermatides), FadeIn(arrow_sp),
                FadeIn(label_lumiere), FadeIn(arrow_lum),
            )
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_loc), FadeOut(loc_texte), FadeOut(schema))

        # --- Raisonnement : phases 1 et 2 (multiplication, croissance) ---------
        entete_p12 = Text("Phases 1 et 2 : multiplication et croissance", font_size=23, color=YELLOW, weight="BOLD")
        entete_p12.next_to(titre, DOWN, buff=0.45)

        p12 = _bullets(
            [
                "Phase 1 — Multiplication : les spermatogonies (2n), "
                "contre la membrane basale, se multiplient par mitoses. "
                "Renouvelle le stock et produit les cellules destinées à "
                "la croissance.",
                "Phase 2 — Croissance : certaines spermatogonies cessent "
                "de se diviser, grossissent et deviennent des "
                "spermatocytes I (2n, chromosomes à 2 chromatides, ADN "
                "répliqué).",
            ],
            font_size=21,
            width=52,
        )
        p12.next_to(entete_p12, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Détaillons les quatre phases. Phase un : la "
                "multiplication. Les spermatogonies, diploïdes, situées "
                "contre la membrane basale, se multiplient activement par "
                "mitoses. Ces divisions assurent deux choses : le "
                "renouvellement du stock de spermatogonies, qui ne "
                "s'épuise donc jamais, et la production de nouvelles "
                "cellules destinées à entrer en croissance. Phase deux : la "
                "croissance. Certaines spermatogonies cessent de se "
                "diviser, augmentent de volume et deviennent des "
                "spermatocytes de premier ordre. Ces cellules restent "
                "diploïdes, mais leur ADN a été répliqué : chaque "
                "chromosome est désormais formé de deux chromatides "
                "identiques."
            )
        ) as tracker:
            self.play(FadeIn(entete_p12))
            self.play(FadeIn(p12))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_p12), FadeOut(p12))

        # --- Exemple traité : phases 3 et 4 (méiose, spermiogenèse) ------------
        entete_p34 = Text("Phases 3 et 4 : méiose et spermiogenèse", font_size=23, color=YELLOW, weight="BOLD")
        entete_p34.next_to(titre, DOWN, buff=0.45)

        p3 = _bullets(
            [
                "Phase 3 — Maturation (méiose) : 1 spermatocyte I (2n) "
                "→méiose I→ 2 spermatocytes II (n) →méiose II→ 4 "
                "spermatides (n). Divisions cytoplasmiques équitables : "
                "4 cellules de même taille, toutes viables.",
            ],
            font_size=20,
            width=52,
        )
        p3.next_to(entete_p34, DOWN, buff=0.3)

        p4 = _bullets(
            [
                "Phase 4 — Spermiogenèse (sans division) : le noyau se "
                "condense et migre vers un pôle ; le Golgi forme "
                "l'acrosome ; les mitochondries s'enroulent en pièce "
                "intermédiaire ; les centrioles édifient le flagelle ; "
                "le cytoplasme en excès est phagocyté par les cellules "
                "de Sertoli.",
            ],
            font_size=20,
            width=52,
        )
        p4.next_to(p3, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Phase trois : la maturation, c'est-à-dire la méiose. "
                "Chaque spermatocyte de premier ordre, diploïde, subit la "
                "méiose un : il donne deux spermatocytes de second ordre, "
                "haploïdes, à chromosomes encore formés de deux "
                "chromatides. Puis la méiose deux sépare les chromatides "
                "sœurs : les deux spermatocytes deux donnent quatre "
                "spermatides haploïdes. Les divisions cytoplasmiques sont "
                "équitables : les quatre spermatides ont toutes la même "
                "taille et sont toutes viables. Phase quatre : la "
                "spermiogenèse, une différenciation morphologique sans "
                "aucune division. Chaque spermatide, cellule ronde et "
                "immobile, se transforme en spermatozoïde, cellule "
                "allongée et mobile : le noyau se condense et migre vers "
                "un pôle de la cellule ; l'appareil de Golgi forme "
                "l'acrosome, une vésicule riche en enzymes, qui coiffe le "
                "noyau ; les mitochondries se rassemblent en spirale "
                "autour du début du flagelle pour former la pièce "
                "intermédiaire ; les centrioles édifient le flagelle, "
                "long filament locomoteur ; enfin, l'essentiel du "
                "cytoplasme est éliminé, ses résidus étant phagocytés par "
                "les cellules de Sertoli."
            )
        ) as tracker:
            self.play(FadeIn(entete_p34))
            self.play(FadeIn(p3))
            self.play(FadeIn(p4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_p34), FadeOut(p3), FadeOut(p4))

        # --- À retenir : les quatre phases, en un coup d'œil --------------------
        retenir = property_box(
            _bullets(
                [
                    "1) Multiplication (mitoses) : spermatogonies (2n).",
                    "2) Croissance : spermatocyte I (2n, 2 chromatides).",
                    "3) Maturation (méiose I puis II) : spermatocyte II "
                    "(n) puis spermatides (n).",
                    "4) Spermiogenèse (différenciation, sans division) : "
                    "spermatide → spermatozoïde (n).",
                ],
                font_size=19,
                width=48,
            ),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'enchaînement des quatre phases : d'abord la "
                "multiplication, par mitoses, qui maintient le stock de "
                "spermatogonies diploïdes ; puis la croissance, qui donne "
                "le spermatocyte de premier ordre, toujours diploïde ; "
                "puis la maturation, la méiose proprement dite, qui "
                "produit d'abord des spermatocytes de second ordre puis "
                "des spermatides, haploïdes ; et enfin la spermiogenèse, "
                "une différenciation sans division, qui transforme la "
                "spermatide ronde en spermatozoïde allongé et mobile."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne place jamais la spermiogenèse avant la méiose : "
                    "c'est TOUJOURS après les deux divisions méiotiques, "
                    "sur la spermatide déjà haploïde, que se déroule la "
                    "différenciation morphologique en spermatozoïde. Une "
                    "réponse qui mélange l'ordre des étapes est lourdement "
                    "pénalisée.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : ne place jamais la spermiogenèse avant "
                "la méiose. C'est toujours après les deux divisions "
                "méiotiques, sur la spermatide déjà haploïde, que se "
                "déroule la différenciation morphologique en "
                "spermatozoïde. Une réponse qui mélange l'ordre des étapes "
                "est lourdement pénalisée."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
