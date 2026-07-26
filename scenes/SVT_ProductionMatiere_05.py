"""
scenes/SVT_ProductionMatiere_05.py — Chapitre 11 (1ereD, SVT), scène 05.

§ 11.2.4 Le dioxyde de carbone est indispensable (cloche avec potasse +
témoin, entièrement résolue) + piège « oublier le témoin » + § 11.2.5
l'eau et les sels minéraux (absorption racinaire, sève brute, culture
hydroponique) + piège « la plante mange la terre » (Van Helmont) +
tableau récapitulatif des quatre conditions.
Source : 1ereD/SVT.pdf, pages 148-149.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    Triangle,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _grid_table(cell_matrix, col_gap=0.5, row_gap=0.28):
    n_rows = len(cell_matrix)
    n_cols = len(cell_matrix[0])
    col_widths = [max(cell_matrix[r][c].width for r in range(n_rows)) for c in range(n_cols)]
    row_height = max(cell.height for row in cell_matrix for cell in row)

    col_x = []
    x = 0.0
    for c in range(n_cols):
        col_x.append(x)
        x += col_widths[c] + col_gap

    table = VGroup()
    y = 0.0
    for r in range(n_rows):
        for c in range(n_cols):
            cell = cell_matrix[r][c]
            cell.move_to([col_x[c] + cell.width / 2, y, 0])
            table.add(cell)
        y -= row_height + row_gap
    return table


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


def _cloche_co2(label, potasse=False, sans_amidon=False):
    dome = Arc(radius=0.85, start_angle=0, angle=3.14159, color=WHITE, stroke_width=2)
    base = Line(LEFT * 0.85, RIGHT * 0.85, color=WHITE, stroke_width=2)
    base.move_to(dome.get_start() + (dome.get_end() - dome.get_start()) / 2).shift(DOWN * 0.02)
    cloche = VGroup(dome, base)

    tige = Line(ORIGIN, [0, 0.5, 0], color=GREEN, stroke_width=5)
    feuilles = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=0.8, stroke_width=0).scale(0.32)
    feuilles.next_to(tige, UP, buff=-0.05)
    plante = VGroup(tige, feuilles)
    plante.move_to(dome.get_center() + DOWN * 0.2 + LEFT * 0.25)

    coupelle_couleur = GRAY if potasse else BLUE
    coupelle = Rectangle(width=0.45, height=0.12, fill_color=coupelle_couleur, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1.5)
    coupelle.next_to(plante, RIGHT, buff=0.15).align_to(base, DOWN).shift(UP * 0.05)
    coupelle_label = Text("potasse" if potasse else "eau distillée", font_size=12, color=WHITE)
    coupelle_label.next_to(coupelle, DOWN, buff=0.08)

    titre = Text(label, font_size=15, color=YELLOW, weight="BOLD")
    titre.next_to(cloche, UP, buff=0.15)

    resultat = Text(
        "test : jaune-brun (pas d'amidon)" if sans_amidon else "test : bleu-noir (amidon)",
        font_size=12,
        color=WHITE,
    )
    resultat.next_to(VGroup(cloche, plante, coupelle, coupelle_label), DOWN, buff=0.15)

    return VGroup(cloche, plante, coupelle, coupelle_label, titre, resultat)


class CO2EauSelsMineraux(NotionScene):
    def construct(self):
        # --- Énoncé -------------------------------------------------------
        titre = scene_title("11.2.4-11.2.5 — CO2, eau et sels minéraux")
        titre.scale(0.5)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Après la lumière et la chlorophylle, deux autres facteurs "
                "restent à tester : le dioxyde de carbone, puis les "
                "matériaux venus du sol, l'eau et les sels minéraux."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Exemple traité : la plante privée de CO2 -------------------------
        exemple_co2 = example_box(
            Text(
                _wrap(
                    "Deux plantes, 48 h à l'obscurité, sous cloche à la "
                    "lumière. Cloche A : coupelle de potasse (absorbe le "
                    "CO2). Cloche B, témoin : coupelle d'eau distillée. "
                    "Test à l'eau iodée : feuille A jaune-brun, feuille B "
                    "bleu-noir.",
                    width=52,
                ),
                font_size=20,
            ),
            box_width=11.2,
        )
        exemple_co2.to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        cloche_a = _cloche_co2("Cloche A", potasse=True, sans_amidon=True)
        cloche_b = _cloche_co2("Cloche B — témoin", potasse=False, sans_amidon=False)
        cloches = VGroup(cloche_a, cloche_b).arrange(RIGHT, buff=0.5)
        cloches.scale(0.85)
        cloches.next_to(exemple_co2, RIGHT, buff=0.4)

        groupe_co2 = VGroup(exemple_co2, cloches)
        groupe_co2.move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)
        _fit(groupe_co2, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Deux plantes identiques, ayant séjourné quarante-huit "
                "heures à l'obscurité, sont placées chacune sous une "
                "cloche transparente, à la lumière. Sous la cloche A, une "
                "coupelle de potasse absorbe le CO2 de l'air : il n'en "
                "reste pratiquement plus. Sous la cloche B, une coupelle "
                "d'eau distillée n'absorbe pas le CO2 : c'est le témoin."
            )
        ) as tracker:
            self.play(FadeIn(exemple_co2))
            self.play(FadeIn(cloches))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Après quelques heures, on teste des feuilles des deux "
                "plantes à l'eau iodée : la feuille de la plante A reste "
                "jaune-brun, celle de la plante B devient bleu-noir. Les "
                "deux plantes ont reçu la même lumière et possèdent de la "
                "chlorophylle ; seule la présence de CO2 différait. "
                "Conclusion : le dioxyde de carbone est indispensable, "
                "c'est lui qui fournit le carbone de la matière organique. "
                "Le témoin B prouve que la cloche, la lumière ou la "
                "manipulation ne sont pas en cause."
            )
        ) as tracker:
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_co2))

        # --- Piège : oublier le témoin ----------------------------------------
        piege_temoin = warning_box(
            Text(
                _wrap(
                    "Une expérience où l'on supprime un facteur n'a de "
                    "valeur que comparée à un témoin qui possède ce "
                    "facteur, toutes les autres conditions étant "
                    "identiques. Sans le témoin B, impossible d'affirmer "
                    "que c'est bien l'absence de CO2, et non la cloche ou "
                    "la manipulation, qui empêche l'amidon.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        piege_temoin.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique à éviter : une expérience où l'on "
                "supprime un facteur n'a de valeur que si l'on compare à "
                "un témoin qui possède ce facteur, toutes les autres "
                "conditions étant identiques. Sans le témoin B de "
                "l'expérience précédente, on ne pourrait pas affirmer que "
                "c'est bien l'absence de CO2, et non la cloche, la "
                "chaleur ou la manipulation, qui empêche la formation "
                "d'amidon. Dans une copie, cite toujours le rôle du "
                "témoin."
            )
        ) as tracker:
            self.play(FadeIn(piege_temoin))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_temoin))

        # --- Propriété : l'absorption racinaire --------------------------------
        propriete_racine = property_box(
            Text(
                _wrap(
                    "Les racines absorbent l'eau et les sels minéraux du "
                    "sol grâce aux poils absorbants : c'est la sève brute, "
                    "qui monte par la tige jusqu'aux feuilles. La culture "
                    "hydroponique (sans terre, en solution minérale) "
                    "montre que seuls l'eau et les sels minéraux dissous "
                    "comptent.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        propriete_racine.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "D'où viennent l'hydrogène et l'oxygène de la matière "
                "organique ? Le carbone vient du CO2 de l'air, mais les "
                "autres éléments sont apportés par l'eau et les sels "
                "minéraux, ions nitrate, phosphate, potassium, puisés dans "
                "le sol. Les racines absorbent l'eau et les sels minéraux "
                "grâce aux poils absorbants ; ce mélange, la sève brute, "
                "monte ensuite par la tige jusqu'aux feuilles. La culture "
                "hydroponique, une plante cultivée dans une solution "
                "minérale sans terre, comme dans certaines fermes modernes "
                "d'Abidjan, montre qu'une plante peut se développer "
                "normalement sans terre, à condition que la solution "
                "contienne tous les éléments minéraux indispensables : la "
                "terre n'est qu'un support, ce sont l'eau et les sels "
                "minéraux dissous qui comptent."
            )
        ) as tracker:
            self.play(FadeIn(propriete_racine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_racine))

        # --- Piège : « la plante mange la terre » (Van Helmont) ---------------
        piege_vanhelmont = warning_box(
            Text(
                _wrap(
                    "Expérience de Van Helmont (17e siècle) : un saule "
                    "gagnant plus de 74 kg en cinq ans ne faisait perdre "
                    "au sol qu'environ 60 g. La masse du végétal ne vient "
                    "donc pas de la terre, mais essentiellement du CO2 de "
                    "l'air et de l'eau. Ne jamais dire qu'une plante « se "
                    "nourrit de terre ».",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        piege_vanhelmont.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Autre piège classique : « la plante mange la terre ». "
                "L'expérience historique de Van Helmont, au dix-septième "
                "siècle, a montré qu'un saule gagnant plus de "
                "soixante-quatorze kilogrammes en cinq ans ne faisait "
                "perdre au sol qu'environ soixante grammes. La masse du "
                "végétal ne vient donc pas de la terre : elle vient "
                "essentiellement du CO2 de l'air et de l'eau. Ne dis "
                "jamais qu'une plante se nourrit de terre."
            )
        ) as tracker:
            self.play(FadeIn(piege_vanhelmont))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_vanhelmont))

        # --- À retenir : tableau récapitulatif des quatre conditions ----------
        entetes = ["Condition", "Rôle", "Expérience qui le prouve"]
        rows = [
            ["Lumière", "fournit l'énergie", "feuille partiellement masquée"],
            ["Chlorophylle", "capte l'énergie lumineuse", "feuille panachée"],
            ["CO2", "fournit le carbone", "cloche avec potasse + témoin"],
            ["Eau / sels minéraux", "H, O, éléments constitutifs (N,P,K)", "absorption racinaire, hydroponie"],
        ]
        matrice = [[Text(c, font_size=17, color=YELLOW, weight="BOLD") for c in entetes]]
        for row in rows:
            matrice.append([Text(c, font_size=16, color=WHITE) for c in row])
        tableau = _grid_table(matrice, col_gap=0.45, row_gap=0.22)
        tableau.next_to(titre, DOWN, buff=0.6)
        _fit(tableau, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Récapitulons les quatre conditions indispensables à la "
                "production de matière. La lumière fournit l'énergie, "
                "prouvée par l'expérience de la feuille partiellement "
                "masquée. La chlorophylle capte l'énergie lumineuse, "
                "prouvée par l'expérience de la feuille panachée. Le "
                "dioxyde de carbone fournit le carbone, prouvé par "
                "l'expérience de la cloche avec potasse et son témoin. "
                "Enfin, l'eau et les sels minéraux fournissent l'hydrogène, "
                "l'oxygène et les éléments constitutifs comme l'azote, le "
                "phosphore et le potassium, prouvés par l'absorption "
                "racinaire et la culture hydroponique."
            )
        ) as tracker:
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(tableau))
