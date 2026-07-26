"""
scenes/SVT_FecondationMammiferes_07.py — Chapitre 4 (1ereC, SVT), scène 07.

§ 5.1 La segmentation (définition, tableau des stades zygote -> œuf
segmenté -> morula -> blastocyste avec âges, schéma) + remarque "le volume
de l'œuf ne grandit pas". Source : 1ereC/SVT.pdf, pages 40-41.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, Circle, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.5, row_gap=0.26):
    n_rows = len(cell_matrix)
    n_cols = len(cell_matrix[0])
    col_widths = [max(cell_matrix[r][c].width for r in range(n_rows)) for c in range(n_cols)]

    col_x = []
    x = 0.0
    for c in range(n_cols):
        col_x.append(x)
        x += col_widths[c] + col_gap

    table = VGroup()
    y = 0.0
    for r in range(n_rows):
        row_height = max(cell_matrix[r][c].height for c in range(n_cols))
        for c in range(n_cols):
            cell = cell_matrix[r][c]
            cell.move_to([col_x[c] + cell.width / 2, y - row_height / 2, 0])
            table.add(cell)
        y -= row_height + row_gap
    return table


def _blastomeres(n, enveloppe_radius=1.0, color="#288073"):
    """n petits blastomères disposés en cercle à l'intérieur de
    l'enveloppe (zone pellucide) de rayon fixe, taille décroissante avec n,
    pour illustrer que le volume total de l'œuf reste constant."""
    import math

    rayon_cellule = min(0.45, (enveloppe_radius * 0.75) / max(1, math.sqrt(n)))
    groupe = VGroup()
    if n == 1:
        positions = [(0, 0)]
    else:
        positions = [
            (0.45 * enveloppe_radius * math.cos(2 * math.pi * i / n), 0.45 * enveloppe_radius * math.sin(2 * math.pi * i / n))
            for i in range(n)
        ]
    for x, y in positions:
        cellule = Circle(radius=rayon_cellule, color=color, fill_color=color, fill_opacity=0.55, stroke_width=1.5)
        cellule.move_to([x, y, 0])
        groupe.add(cellule)
    return groupe


class LaSegmentation(NotionScene):
    def construct(self):
        titre = scene_title("4.5.1 — La segmentation")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : définition de la segmentation --------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La segmentation est l'ensemble des divisions "
                    "mitotiques successives du zygote, qui augmentent le "
                    "nombre de cellules (blastomères) SANS augmentation "
                    "du volume total de l'œuf.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dès sa formation, le zygote entame sa descente de la "
                "trompe vers l'utérus, tout en se divisant : c'est la "
                "segmentation. Retenons la définition : la segmentation "
                "est l'ensemble des divisions mitotiques successives du "
                "zygote, qui augmentent le nombre de cellules, appelées "
                "blastomères, sans augmentation du volume total de "
                "l'œuf."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : 1 -> 2 -> 4 -> 8 blastomères --------------
        enveloppe = Circle(radius=1.1, color=WHITE, stroke_width=2)
        enveloppe.next_to(titre, DOWN, buff=0.7)
        label_zp = Text("Zone pellucide : taille CONSTANTE", font_size=15, color=YELLOW)
        label_zp.next_to(enveloppe, DOWN, buff=0.35)

        contenu = _blastomeres(1, enveloppe_radius=1.1)
        contenu.move_to(enveloppe.get_center())

        with self.voiceover(
            text=(
                "Voici le zygote, une cellule unique, à l'intérieur de la "
                "zone pellucide dont la taille reste constante tout au "
                "long de la segmentation."
            )
        ) as tracker:
            self.play(FadeIn(enveloppe), FadeIn(label_zp))
            self.play(FadeIn(contenu))
            self.wait(tracker.get_remaining_duration())

        for n, commentaire in [
            (2, "Première division : 2 blastomères"),
            (4, "Deuxième division : 4 blastomères"),
            (8, "Troisième division : 8 blastomères"),
            (16, "Quatrième division : 16 blastomères"),
        ]:
            nouveau_contenu = _blastomeres(n, enveloppe_radius=1.1)
            nouveau_contenu.move_to(enveloppe.get_center())
            label_n = Text(commentaire, font_size=16, color=WHITE)
            label_n.next_to(enveloppe, UP, buff=0.3)
            with self.voiceover(
                text=(
                    f"Nouvelle division mitotique : {commentaire.split(': ')[1]}, "
                    "toujours à l'intérieur de la même enveloppe. Chaque "
                    "blastomère est plus petit que le précédent, mais "
                    "toutes les cellules restent diploïdes, à deux n égale "
                    "quarante-six chromosomes, car la mitose conserve le "
                    "nombre de chromosomes."
                )
            ) as tracker:
                self.play(FadeOut(contenu), FadeIn(nouveau_contenu), FadeIn(label_n))
                self.wait(tracker.get_remaining_duration())
            self.play(FadeOut(label_n))
            contenu = nouveau_contenu

        self.play(FadeOut(enveloppe), FadeOut(contenu), FadeOut(label_zp))

        # --- Exemple traité : le tableau des stades --------------------------------
        entete_tab = Text("Les 4 stades de la segmentation", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        rows = [
            ("Stade", "Aspect", "Âge approx."),
            ("Zygote", "Cellule-œuf unique, 2n", "Jour 0"),
            ("Œuf segmenté", "2, 4, 8, 16 blastomères", "Jours 1 à 3"),
            ("Morula", "Boule compacte, 16-32\nblastomères (« mûre »)", "Jours 3 à 4"),
            ("Blastocyste", "Sphère creuse : blastocèle,\nbouton embryonnaire, trophoblaste", "Jours 5 à 6"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=16, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.45, row_gap=0.22)
        tableau.next_to(entete_tab, DOWN, buff=0.35)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = tableau.get_top()[1] - _bas_visible
        if tableau.height > _hauteur_dispo:
            tableau.scale(_hauteur_dispo / tableau.height, about_point=tableau.get_top())

        with self.voiceover(
            text=(
                "Résumons les stades successifs dans un tableau. Le "
                "zygote, cellule-œuf unique, diploïde, au jour zéro. "
                "L'œuf segmenté, de deux à seize blastomères, des jours un "
                "à trois. La morula, une boule compacte de seize à "
                "trente-deux blastomères, ressemblant à une mûre, des "
                "jours trois à quatre. Enfin le blastocyste, une sphère "
                "creuse avec une cavité, le blastocèle, un massif "
                "cellulaire interne, le bouton embryonnaire, et une "
                "enveloppe, le trophoblaste, des jours cinq à six."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : toutes les cellules restent diploïdes ---------------------
        retenir = _bullets(
            [
                "Le zygote descend la trompe vers l'utérus en 3 à 4 jours "
                "tout en se divisant par mitoses.",
                "1 cellule → 2 → 4 → 8 → 16 blastomères...",
                "Toutes les cellules restent diploïdes (2n=46), car la "
                "mitose conserve le nombre de chromosomes.",
            ],
            font_size=22,
            width=52,
        )
        retenir.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le zygote descend la trompe vers "
                "l'utérus en trois à quatre jours, tout en se divisant par "
                "mitoses successives, une cellule, deux, quatre, huit, "
                "seize blastomères. Toutes ces cellules restent "
                "diploïdes, à deux n égale quarante-six chromosomes, car "
                "la mitose conserve toujours le nombre de chromosomes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter : le volume de l'œuf ne grandit pas --------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le volume de l'œuf ne grandit PAS pendant la "
                    "segmentation : les blastomères sont de plus en plus "
                    "petits, car les divisions s'effectuent à l'intérieur "
                    "de la zone pellucide, sans apport nutritif "
                    "extérieur.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : le volume de l'œuf ne "
                "grandit pas pendant la segmentation. Ce sont les "
                "blastomères qui deviennent de plus en plus petits, car "
                "les divisions s'effectuent à l'intérieur de la zone "
                "pellucide, sans aucun apport nutritif extérieur."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
