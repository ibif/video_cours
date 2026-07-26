"""
scenes/Chimie_PetroleGazNaturels_01.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 01.

§ 1. Origine du pétrole et des gaz naturels : définitions, mécanisme de
formation en 4 étapes (dépôt de débris organiques → enfouissement →
décomposition anaérobie sous pression/température → migration et
piégeage), schéma de coupe géologique d'un gisement (roche-mère,
roche-réservoir, roche de couverture, puits de forage), conditions
favorables, et rappel : énergies fossiles non renouvelables.
Source : 1ereC/Chimie.pdf, chapitre 5, pages 45-46.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    BLUE,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _etape_box(numero, texte, color=BLUE, width=20):
    label = Text(f"{numero}. {_wrap(texte, width=width)}", font_size=16, color=WHITE)
    cadre = Rectangle(
        width=label.width + 0.4,
        height=label.height + 0.35,
        color=color,
        fill_color=color,
        fill_opacity=0.18,
        stroke_width=2,
    )
    label.move_to(cadre.get_center())
    return VGroup(cadre, label)


def _schema_mecanisme():
    etape1 = _etape_box(1, "Dépôt de débris organiques (plancton, végétaux) au fond de l'eau", color=YELLOW)
    etape2 = _etape_box(2, "Enfouissement sous des couches de sédiments", color=YELLOW)
    etape3 = _etape_box(3, "Décomposition anaérobie sous pression et température", color=YELLOW)
    etape4 = _etape_box(4, "Migration puis piégeage dans un gisement", color=YELLOW)

    etape1.move_to(UP * 1.0 + LEFT * 3.0)
    etape2.move_to(UP * 1.0 + RIGHT * 3.0)
    etape3.move_to(DOWN * 1.0 + RIGHT * 3.0)
    etape4.move_to(DOWN * 1.0 + LEFT * 3.0)

    fleche1 = Arrow(etape1.get_right(), etape2.get_left(), buff=0.1, color=WHITE, stroke_width=3)
    fleche2 = Arrow(etape2.get_bottom(), etape3.get_top(), buff=0.1, color=WHITE, stroke_width=3)
    fleche3 = Arrow(etape3.get_left(), etape4.get_right(), buff=0.1, color=WHITE, stroke_width=3)

    return VGroup(etape1, etape2, etape3, etape4, fleche1, fleche2, fleche3)


def _coupe_geologique():
    largeur = 6.0
    couverture = Rectangle(width=largeur, height=0.85, fill_color="#8B7355", fill_opacity=0.95, stroke_color=WHITE, stroke_width=1.5)
    reservoir = Rectangle(width=largeur, height=1.0, fill_color="#D9A441", fill_opacity=0.95, stroke_color=WHITE, stroke_width=1.5)
    roche_mere = Rectangle(width=largeur, height=0.85, fill_color="#3B2F2F", fill_opacity=0.95, stroke_color=WHITE, stroke_width=1.5)
    couches = VGroup(couverture, reservoir, roche_mere).arrange(DOWN, buff=0)

    puits = Line(couches.get_top() + RIGHT * 2.0, couches.get_bottom() + RIGHT * 2.0, color=RED, stroke_width=5)
    derrick = Polygon(
        puits.get_start() + LEFT * 0.3,
        puits.get_start() + RIGHT * 0.3,
        puits.get_start() + UP * 0.7,
        color=RED,
        stroke_width=2,
    )

    label_couverture = Text("Roche de couverture\n(imperméable)", font_size=14, color=WHITE)
    label_couverture.next_to(couverture, LEFT, buff=0.5)
    fleche_couverture = Arrow(label_couverture.get_right(), couverture.get_left(), buff=0.08, color=WHITE, stroke_width=2)

    label_reservoir = Text("Roche-réservoir\n(poreuse : piège)", font_size=14, color=WHITE)
    label_reservoir.next_to(reservoir, LEFT, buff=0.5)
    fleche_reservoir = Arrow(label_reservoir.get_right(), reservoir.get_left(), buff=0.08, color=WHITE, stroke_width=2)

    label_mere = Text("Roche-mère\n(matière organique)", font_size=14, color=WHITE)
    label_mere.next_to(roche_mere, LEFT, buff=0.5)
    fleche_mere = Arrow(label_mere.get_right(), roche_mere.get_left(), buff=0.08, color=WHITE, stroke_width=2)

    label_puits = Text("Puits de forage", font_size=14, color=RED)
    label_puits.next_to(derrick, UP, buff=0.15)

    return VGroup(
        couches, puits, derrick,
        label_couverture, fleche_couverture,
        label_reservoir, fleche_reservoir,
        label_mere, fleche_mere,
        label_puits,
    )


class OrigineDuPetroleEtDesGazNaturels(NotionScene):
    def construct(self):
        titre = scene_title("1. Origine du pétrole et des gaz naturels")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définitions du pétrole et du gaz naturel -----------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Pétrole : mélange naturel d'hydrocarbures liquides, "
                        "de couleur brune à noire, présent dans certaines "
                        "roches poreuses du sous-sol.",
                        width=50,
                    ),
                    font_size=23,
                ),
                Text(
                    _wrap(
                        "Gaz naturel : mélange gazeux d'hydrocarbures, "
                        "souvent associé au pétrole ou piégé seul dans un "
                        "gisement.",
                        width=50,
                    ),
                    font_size=23,
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35),
            box_width=11.5,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le pétrole est un mélange naturel d'hydrocarbures "
                "liquides, de couleur brune à noire, présent dans "
                "certaines roches poreuses du sous-sol. Le gaz naturel, "
                "lui, est un mélange gazeux d'hydrocarbures, souvent "
                "associé au pétrole ou piégé seul dans un gisement. Mais "
                "d'où viennent ces ressources ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : mécanisme de formation en 4 étapes -----------------
        entete_mecanisme = Text("Le mécanisme de formation, en 4 étapes", font_size=24, color=YELLOW, weight="BOLD")
        entete_mecanisme.next_to(titre, DOWN, buff=0.4)

        schema_mecanisme = _schema_mecanisme()
        schema_mecanisme.next_to(entete_mecanisme, DOWN, buff=0.4)
        _fit(schema_mecanisme, entete_mecanisme.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "La formation du pétrole et du gaz naturel suit quatre "
                "grandes étapes, étalées sur des millions d'années. "
                "Premièrement, le dépôt de débris organiques, plancton et "
                "végétaux, au fond des mers ou des lacs. Deuxièmement, "
                "leur enfouissement progressif sous des couches "
                "successives de sédiments. Troisièmement, la "
                "décomposition anaérobie de cette matière organique, sous "
                "l'effet combiné de la pression et de la température. "
                "Et quatrièmement, la migration des hydrocarbures formés, "
                "puis leur piégeage dans un gisement."
            )
        ) as tracker:
            self.play(FadeIn(entete_mecanisme))
            self.play(FadeIn(schema_mecanisme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_mecanisme), FadeOut(schema_mecanisme))

        # --- Exemple traité : schéma de coupe géologique d'un gisement --------
        entete_coupe = Text("Coupe géologique d'un gisement", font_size=24, color=YELLOW, weight="BOLD")
        entete_coupe.next_to(titre, DOWN, buff=0.35)

        coupe = _coupe_geologique()
        coupe.next_to(entete_coupe, DOWN, buff=0.4)
        _fit(coupe, entete_coupe.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici la coupe géologique typique d'un gisement. Tout en "
                "bas, la roche-mère : c'est là que la matière organique "
                "s'est transformée en hydrocarbures. Ceux-ci migrent "
                "ensuite vers le haut et s'accumulent dans la "
                "roche-réservoir, une roche poreuse qui joue le rôle de "
                "piège. Au-dessus, la roche de couverture, imperméable, "
                "empêche les hydrocarbures de continuer leur migration : "
                "c'est elle qui scelle le gisement. Le puits de forage "
                "traverse ces trois couches pour atteindre le réservoir."
            )
        ) as tracker:
            self.play(FadeIn(entete_coupe))
            self.play(FadeIn(coupe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_coupe), FadeOut(coupe))

        # --- À retenir : conditions favorables ----------------------------------
        conditions = property_box(
            _bullets(
                [
                    "Absence de dioxygène (milieu anaérobie)",
                    "Température comprise entre 60°C et 150°C",
                    "Pression et temps géologique suffisants (millions d'années)",
                ],
                font_size=22,
                width=44,
            ),
            box_width=11.0,
        )
        conditions.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons les trois conditions favorables à cette "
                "formation : l'absence de dioxygène, c'est-à-dire un "
                "milieu anaérobie ; une température comprise entre "
                "soixante et cent cinquante degrés Celsius ; et enfin, "
                "une pression et un temps géologique suffisants, comptés "
                "en millions d'années."
            )
        ) as tracker:
            self.play(FadeIn(conditions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conditions))

        # --- Piège à éviter : ressources non renouvelables ----------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le pétrole et le gaz naturel sont des énergies "
                    "fossiles : leur formation demande des millions "
                    "d'années. À l'échelle humaine, ce sont donc des "
                    "ressources NON renouvelables, qui s'épuisent plus "
                    "vite qu'elles ne se reconstituent.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "N'oublions jamais ceci : le pétrole et le gaz naturel "
                "sont des énergies fossiles, dont la formation demande "
                "des millions d'années. À l'échelle humaine, ce sont donc "
                "des ressources non renouvelables, qui s'épuisent bien "
                "plus vite qu'elles ne se reconstituent."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
