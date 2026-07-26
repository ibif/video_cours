"""
scenes/SVT_ProductionMatiere_06.py — Chapitre 11 (1ereD, SVT), scène 06.

§ 11.3 Les organes et structures cellulaires de la production de matière :
la feuille (limbe, épiderme, parenchyme palissadique/lacuneux, nervures)
avec schéma en coupe, les stomates (cellules de garde, double rôle), les
chloroplastes (pigments chlorophylliens).
Source : 1ereD/SVT.pdf, pages 150-151.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    Rectangle,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_anchor):
    """Réduit l'échelle de `mobject` si sa hauteur dépasse le cadre
    visible OU si sa largeur dépasse la largeur du cadre (cas fréquent
    d'un groupe boîte + schéma placés côte à côte)."""
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_anchor - bas_visible
    largeur_dispo = config.frame_width - 0.5
    echelle = 1.0
    if mobject.height > hauteur_dispo:
        echelle = min(echelle, hauteur_dispo / mobject.height)
    if mobject.width > largeur_dispo:
        echelle = min(echelle, largeur_dispo / mobject.width)
    if echelle < 1.0:
        mobject.scale(echelle, about_point=mobject.get_top())
    return mobject


def _coupe_feuille():
    """Coupe transversale schématique du limbe (empilement de couches)."""
    largeur = 5.0

    epiderme_sup = Rectangle(width=largeur, height=0.25, fill_color="#8FBF8F", fill_opacity=0.9, stroke_color=WHITE, stroke_width=1)
    palissadique = Rectangle(width=largeur, height=0.9, fill_color="#1F7A3D", fill_opacity=0.85, stroke_color=WHITE, stroke_width=1)
    lacuneux = Rectangle(width=largeur, height=0.9, fill_color="#4FAF6D", fill_opacity=0.55, stroke_color=WHITE, stroke_width=1)
    epiderme_inf = Rectangle(width=largeur, height=0.25, fill_color="#8FBF8F", fill_opacity=0.9, stroke_color=WHITE, stroke_width=1)

    couches = VGroup(epiderme_sup, palissadique, lacuneux, epiderme_inf)
    couches.arrange(DOWN, buff=0)

    # Nervure : petit faisceau de vaisseaux au centre du parenchyme lacuneux
    nervure = VGroup(
        Dot(radius=0.09, color=YELLOW),
        Dot(radius=0.09, color="#5AA9E6"),
    ).arrange(RIGHT, buff=0.03)
    nervure.move_to(lacuneux.get_center())

    # Petites cellules verticales dans le parenchyme palissadique (allongées)
    cellules_pal = VGroup(
        *[
            Rectangle(width=0.35, height=0.75, stroke_color=WHITE, stroke_width=1, fill_opacity=0)
            for _ in range(8)
        ]
    ).arrange(RIGHT, buff=0.05)
    cellules_pal.move_to(palissadique.get_center())

    # Petits ronds espacés dans le parenchyme lacuneux (cellules + espaces d'air)
    cellules_lac = VGroup(
        *[Dot(radius=0.08, color="#2E8B57") for _ in range(10)]
    ).arrange_in_grid(rows=2, cols=5, buff=0.28)
    cellules_lac.move_to(lacuneux.get_center()).shift(LEFT * 0.9)

    # Ouverture stomatique dans l'épiderme inférieur
    stomate_trou = Rectangle(width=0.18, height=0.22, fill_color="black", fill_opacity=1, stroke_width=0)
    stomate_trou.move_to(epiderme_inf.get_center() + RIGHT * 1.6)

    labels = VGroup(
        Text("épiderme supérieur", font_size=13, color=WHITE).next_to(epiderme_sup, LEFT, buff=0.15),
        Text("parenchyme palissadique", font_size=13, color=WHITE).next_to(palissadique, LEFT, buff=0.15),
        Text("parenchyme lacuneux", font_size=13, color=WHITE).next_to(lacuneux, LEFT, buff=0.15),
        Text("épiderme inférieur", font_size=13, color=WHITE).next_to(epiderme_inf, LEFT, buff=0.15),
    )
    label_nervure = Text("nervure", font_size=12, color=YELLOW).next_to(nervure, UP, buff=0.08)
    label_stomate = Text("stomate", font_size=12, color=WHITE).next_to(stomate_trou, DOWN, buff=0.1)

    return VGroup(
        couches, cellules_pal, cellules_lac, nervure, stomate_trou,
        labels, label_nervure, label_stomate,
    )


def _schema_stomate():
    """Zoom sur un stomate : deux cellules de garde en haricot autour d'un pore."""
    garde_gauche = Ellipse(width=0.9, height=0.4, fill_color="#3FA34D", fill_opacity=0.85, stroke_color=WHITE, stroke_width=1.5)
    garde_droite = garde_gauche.copy()
    garde_gauche.rotate(0.35)
    garde_droite.rotate(-0.35)
    garde_gauche.shift(LEFT * 0.32 + DOWN * 0.08)
    garde_droite.shift(RIGHT * 0.32 + DOWN * 0.08)
    ostiole = Rectangle(width=0.14, height=0.22, fill_color="black", fill_opacity=1, stroke_width=0)

    fleche_co2 = Arrow(UP * 0.9, ORIGIN, color="#5AA9E6", buff=0).scale(0.7)
    fleche_co2.next_to(ostiole, UP, buff=0.05)
    label_co2 = Text("CO2 entre", font_size=14, color="#5AA9E6").next_to(fleche_co2, UP, buff=0.05)

    fleche_o2 = Arrow(ORIGIN, DOWN * 0.9, color=YELLOW, buff=0).scale(0.7)
    fleche_o2.next_to(ostiole, DOWN, buff=0.05)
    label_o2 = Text("O2 sort", font_size=14, color=YELLOW).next_to(fleche_o2, DOWN, buff=0.05)

    label_cg = Text("cellules de garde", font_size=13, color=WHITE)
    stomate = VGroup(garde_gauche, garde_droite, ostiole)
    label_cg.next_to(stomate, RIGHT, buff=0.3)

    return VGroup(stomate, fleche_co2, label_co2, fleche_o2, label_o2, label_cg)


def _schema_chloroplaste():
    """Cellule végétale simplifiée avec chloroplastes (ovales verts) à l'intérieur."""
    cellule = RoundedRectangle(width=2.6, height=1.8, corner_radius=0.15, stroke_color=WHITE, stroke_width=2, fill_opacity=0)
    noyau = Ellipse(width=0.5, height=0.4, fill_color="#B08BD8", fill_opacity=0.7, stroke_width=0)
    noyau.move_to(cellule.get_center() + LEFT * 0.7 + UP * 0.3)

    chloroplastes = VGroup(
        *[
            Ellipse(width=0.42, height=0.24, fill_color=GREEN, fill_opacity=0.85, stroke_color="#0F5A22", stroke_width=1)
            for _ in range(6)
        ]
    )
    positions = [(0.6, 0.4), (0.9, -0.2), (0.2, -0.5), (-0.3, 0.6), (0.0, 0.0), (-0.6, -0.4)]
    for chloro, (dx, dy) in zip(chloroplastes, positions):
        chloro.move_to(cellule.get_center() + [dx, dy, 0])

    label_chloro = Text("chloroplaste\n(pigments chlorophylliens)", font_size=13, color=GREEN)
    label_chloro.next_to(cellule, RIGHT, buff=0.35)
    label_noyau = Text("noyau", font_size=12, color="#B08BD8").next_to(noyau, UP, buff=0.08)
    label_cellule = Text("cellule du parenchyme palissadique", font_size=13, color=WHITE)
    groupe = VGroup(cellule, noyau, chloroplastes)
    label_cellule.next_to(groupe, DOWN, buff=0.25)

    return VGroup(groupe, label_chloro, label_noyau, label_cellule)


class OrganeEtStructuresFeuille(NotionScene):
    def construct(self):
        # --- Énoncé : la feuille, organe spécialisé -----------------------
        titre = scene_title("11.3 — Organes et structures cellulaires")
        titre.scale(0.55)
        titre.to_edge(UP)

        def_feuille = definition_box(
            Text(
                _wrap(
                    "La feuille est l'organe spécialisé dans la "
                    "production de matière organique. Sa forme aplatie et "
                    "étalée, le limbe, offre une grande surface "
                    "d'exposition à la lumière et aux gaz, tout en "
                    "restant mince. Elle est rattachée à la tige par le "
                    "pétiole.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.5,
        )
        def_feuille.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La feuille est l'organe spécialisé dans la production de "
                "matière organique. Sa forme aplatie et étalée, le limbe, "
                "offre une grande surface d'exposition à la lumière et aux "
                "gaz, tout en restant mince, pour que la lumière atteigne "
                "toutes les cellules. Elle est rattachée à la tige par le "
                "pétiole."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_feuille))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_feuille))

        # --- Animation du raisonnement : coupe transversale du limbe -----------
        coupe = _coupe_feuille()
        coupe.scale(0.95)
        coupe.next_to(titre, DOWN, buff=0.6)
        _fit(coupe, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Observons une coupe transversale du limbe au microscope. "
                "On distingue un épiderme supérieur et un épiderme "
                "inférieur, couches protectrices couvertes d'une cuticule "
                "imperméable qui limite les pertes d'eau. Juste sous "
                "l'épiderme supérieur, là où la lumière arrive, se trouve "
                "le parenchyme palissadique, fait de cellules allongées "
                "très riches en chloroplastes. En dessous, le parenchyme "
                "lacuneux a des cellules plus lâches, entourées d'espaces "
                "d'air qui facilitent la circulation des gaz. Enfin, les "
                "nervures contiennent les vaisseaux conducteurs : les uns "
                "amènent la sève brute, eau et sels minéraux, les autres "
                "répartissent la sève élaborée, la matière organique, vers "
                "toute la plante. C'est par les stomates de l'épiderme "
                "inférieur que les gaz entrent et sortent."
            )
        ) as tracker:
            self.play(FadeIn(coupe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coupe))

        # --- Exemple traité : le stomate, définition + schéma -------------------
        def_stomate = definition_box(
            Text(
                _wrap(
                    "Les stomates sont de petits orifices situés surtout "
                    "dans l'épiderme inférieur. Chaque stomate est "
                    "encadré par deux cellules de garde qui ouvrent ou "
                    "ferment l'orifice. C'est par les stomates que le CO2 "
                    "entre et que le O2 produit sort.",
                    width=52,
                ),
                font_size=20,
            ),
            box_width=11.2,
        )
        def_stomate.to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        schema_stomate = _schema_stomate()
        schema_stomate.scale(1.1)
        schema_stomate.next_to(def_stomate, RIGHT, buff=0.5)

        groupe_stomate = VGroup(def_stomate, schema_stomate)
        groupe_stomate.move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)
        _fit(groupe_stomate, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Les stomates sont de petits orifices situés surtout dans "
                "l'épiderme inférieur des feuilles. Chaque stomate est "
                "encadré par deux cellules de garde, qui peuvent gonfler "
                "ou se dégonfler, ce qui ouvre ou ferme l'orifice. C'est "
                "par les stomates que le CO2 de l'air entre dans la "
                "feuille, et que le O2 produit en sort. Les stomates ont "
                "un double rôle : ils permettent les échanges gazeux, "
                "mais laissent aussi s'évaporer l'eau, la transpiration. "
                "La plante règle donc leur ouverture : ouverts le jour "
                "pour laisser entrer le CO2, souvent resserrés quand la "
                "sécheresse menace, comme chez les plantes de savane en "
                "saison sèche."
            )
        ) as tracker:
            self.play(FadeIn(def_stomate))
            self.play(FadeIn(schema_stomate))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_stomate))

        # --- À retenir : le chloroplaste, définition + schéma ---------------------
        def_chloroplaste = definition_box(
            Text(
                _wrap(
                    "Le chloroplaste est un organite du cytoplasme des "
                    "cellules végétales vertes. Il contient les pigments "
                    "chlorophylliens qui captent l'énergie lumineuse. "
                    "C'est dans les chloroplastes que se déroulent les "
                    "réactions de production de matière organique.",
                    width=52,
                ),
                font_size=20,
            ),
            box_width=11.2,
        )
        def_chloroplaste.to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        schema_chloro = _schema_chloroplaste()
        schema_chloro.scale(0.95)
        schema_chloro.next_to(def_chloroplaste, RIGHT, buff=0.4)

        groupe_chloroplaste = VGroup(def_chloroplaste, schema_chloro)
        groupe_chloroplaste.move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)
        _fit(groupe_chloroplaste, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Le chloroplaste est un organite, une petite structure du "
                "cytoplasme des cellules végétales vertes. Il contient les "
                "pigments chlorophylliens, les chlorophylles, de couleur "
                "verte, qui captent l'énergie lumineuse. C'est dans les "
                "chloroplastes que se déroulent toutes les réactions de la "
                "production de matière organique. Les cellules de "
                "l'épiderme, sauf les cellules de garde, celles de la "
                "tige ligneuse ou des racines n'en contiennent pas : elles "
                "ne produisent pas de matière."
            )
        ) as tracker:
            self.play(FadeIn(def_chloroplaste))
            self.play(FadeIn(schema_chloro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_chloroplaste))

        # --- Piège / remarque : lien avec la feuille panachée ----------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "La présence des chloroplastes explique l'expérience "
                    "de la feuille panachée : les zones blanches sont des "
                    "zones dont les cellules n'ont pas de chloroplastes "
                    "fonctionnels ; sans chlorophylle, pas de captation "
                    "d'énergie, donc pas de production d'amidon, même en "
                    "pleine lumière.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une remarque importante relie ces structures à "
                "l'expérience vue précédemment : la présence des "
                "chloroplastes explique l'expérience de la feuille "
                "panachée. Les zones blanches de la feuille sont des zones "
                "dont les cellules n'ont pas de chloroplastes "
                "fonctionnels ; sans chlorophylle, pas de captation "
                "d'énergie, donc pas de production d'amidon, même en "
                "pleine lumière."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(remarque))
