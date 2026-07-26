"""
scenes/Chimie_CorrosionProtectionMetaux_07.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 07.

§ 7. Moyens de protection : revêtements non métalliques et métallisation.
Deux grandes idées (faire barrière / faire s'oxyder un autre métal à la
place du fer). Revêtements non métalliques (peinture, vernis, plastique,
émail — efficaces seulement si intacts). definition_box métallisation,
classification électrochimique Mg > Zn > Fe > Sn > Cu, property_box (métal
plus réducteur protège même rayé / métal moins réducteur = barrière
seule). Galvanisation (zinc), étamage (étain), chromage. Tableau
comparatif des 3 procédés. Exemple résolu 2 (clou galvanisé vs étamé,
rayés).
Source : 1ereC/Chimie.pdf, chapitre 15, pages 149-150.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    RED,
    ORANGE,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


def _tableau(entetes, lignes, col_widths, row_height=0.5, font_size=18):
    n_cols = len(entetes)
    n_rows = 1 + len(lignes)
    x_positions = [0.0]
    for w in col_widths:
        x_positions.append(x_positions[-1] + w)
    largeur_totale = x_positions[-1]
    x_centres = [(x_positions[j] + x_positions[j + 1]) / 2 - largeur_totale / 2 for j in range(n_cols)]

    cells = VGroup()
    for j, entete in enumerate(entetes):
        c = Text(entete, font_size=font_size, color=YELLOW, weight="BOLD")
        c.move_to([x_centres[j], (n_rows - 1) / 2 * row_height, 0])
        cells.add(c)

    for i, ligne in enumerate(lignes):
        for j, val in enumerate(ligne):
            c = Text(val, font_size=font_size, color=WHITE)
            c.move_to([x_centres[j], ((n_rows - 1) / 2 - (i + 1)) * row_height, 0])
            cells.add(c)

    hauteur_totale = n_rows * row_height
    contour = Rectangle(width=largeur_totale, height=hauteur_totale, color=WHITE, stroke_width=2)

    lignes_h = VGroup(
        *[
            Line(
                [-largeur_totale / 2, (n_rows / 2 - k) * row_height, 0],
                [largeur_totale / 2, (n_rows / 2 - k) * row_height, 0],
                color=WHITE,
                stroke_width=1,
            )
            for k in range(n_rows + 1)
        ]
    )
    lignes_v = VGroup(
        *[
            Line(
                [x_positions[k] - largeur_totale / 2, hauteur_totale / 2, 0],
                [x_positions[k] - largeur_totale / 2, -hauteur_totale / 2, 0],
                color=WHITE,
                stroke_width=1,
            )
            for k in range(n_cols + 1)
        ]
    )

    return VGroup(contour, lignes_h, lignes_v, cells)


class MoyensProtectionRevetementsMetallisation(NotionScene):
    def construct(self):
        titre = scene_title("15.7 Protection : revêtements et métallisation")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : deux grandes idées -----------------------------------------
        idees = _bullets(
            [
                "faire barrière : isoler complètement le fer de l'eau et de l'air",
                "faire s'oxyder un autre métal à la place du fer",
            ],
            font_size=22,
        )
        idees.next_to(titre, DOWN, buff=0.5)
        entete_idees = Text("Protéger un métal : deux grandes idées", font_size=22, color=YELLOW, weight="BOLD")
        entete_idees.next_to(titre, DOWN, buff=0.35)
        idees.next_to(entete_idees, DOWN, buff=0.35)
        groupe_idees = VGroup(entete_idees, idees)

        with self.voiceover(
            text=(
                "Puisque la corrosion exige à la fois de l'eau et du "
                "dioxygène, protéger un métal repose sur deux grandes "
                "idées. Première idée : faire barrière, en isolant "
                "complètement le fer de l'eau et de l'air. Seconde idée, "
                "plus subtile : faire s'oxyder volontairement un autre "
                "métal à la place du fer."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(groupe_idees))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_idees))

        # --- Raisonnement : revêtements non métalliques --------------------------
        entete_revet = Text("Idée 1 : les revêtements non métalliques", font_size=21, color=YELLOW, weight="BOLD")
        entete_revet.next_to(titre, DOWN, buff=0.35)

        revetements = _bullets(
            ["peinture", "vernis", "plastique (gainage)", "émail"],
            font_size=21,
        )
        avantage = Text(
            "Efficace seulement si le revêtement reste intact : la moindre",
            font_size=18, color=RED,
        )
        avantage2 = Text(
            "rayure expose le fer nu, et la corrosion reprend localement.",
            font_size=18, color=RED,
        )
        limite = VGroup(avantage, avantage2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        groupe_revet = VGroup(entete_revet, revetements, limite).arrange(DOWN, buff=0.35)
        _fit(groupe_revet, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Les revêtements non métalliques les plus courants sont "
                "la peinture, le vernis, le plastique ou encore l'émail. "
                "Ils forment une barrière physique simple et peu "
                "coûteuse. Mais leur limite est sérieuse : ils ne "
                "protègent que tant qu'ils restent parfaitement intacts. "
                "La moindre rayure expose le fer nu, et la corrosion "
                "reprend localement, souvent même plus vite qu'ailleurs, "
                "car l'eau s'infiltre sous le revêtement resté en place."
            )
        ) as tracker:
            self.play(FadeIn(entete_revet))
            self.play(FadeIn(revetements))
            self.play(FadeIn(limite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_revet))

        # --- Exemple traité : métallisation + classification électrochimique ----
        definition_metal = definition_box(
            Text(
                _wrap(
                    "La métallisation consiste à recouvrir le fer d'une "
                    "fine couche d'un autre métal, choisi selon sa "
                    "position dans la classification électrochimique.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        definition_metal.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La seconde idée, la métallisation, consiste à recouvrir "
                "le fer d'une fine couche d'un autre métal. Le choix de "
                "ce métal n'est pas arbitraire : il dépend directement "
                "de sa position dans la classification électrochimique "
                "des couples oxydant-réducteur, déjà étudiée."
            )
        ) as tracker:
            self.play(FadeIn(definition_metal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_metal))

        classification = MathTex(
            r"Mg \;>\; Zn \;>\; Fe \;>\; Sn \;>\; Cu",
            font_size=30, color=YELLOW,
        )
        note_classif = Text(
            "(pouvoir réducteur décroissant, de gauche à droite)",
            font_size=18, color=WHITE,
        )
        groupe_classif = VGroup(classification, note_classif).arrange(DOWN, buff=0.35)
        groupe_classif.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la classification électrochimique utile ici, du "
                "réducteur le plus fort au plus faible : magnésium, "
                "zinc, fer, étain, cuivre. Le magnésium et le zinc sont "
                "plus réducteurs que le fer ; l'étain et le cuivre sont "
                "moins réducteurs que le fer."
            )
        ) as tracker:
            self.play(Write(classification))
            self.play(FadeIn(note_classif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_classif))

        propriete = property_box(
            VGroup(
                Text("Métal de revêtement PLUS réducteur que le fer (Zn, Mg) :", font_size=20, weight="BOLD"),
                Text("protège même rayé (protection cathodique locale).", font_size=19),
                Text("Métal de revêtement MOINS réducteur que le fer (Sn, Cu) :", font_size=20, weight="BOLD"),
                Text("protège seulement intact (barrière) — corrosion accélérée si rayé.", font_size=19),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.6,
        )
        propriete.next_to(titre, DOWN, buff=0.4)
        _fit(propriete, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Retenons la propriété clé de la métallisation : si le "
                "métal de revêtement est plus réducteur que le fer, "
                "comme le zinc ou le magnésium, il continue de protéger "
                "le fer même si le revêtement est rayé. Si, au contraire, "
                "le métal de revêtement est moins réducteur que le fer, "
                "comme l'étain ou le cuivre, il ne protège que tant qu'il "
                "reste intact, et accélère même la corrosion du fer une "
                "fois rayé."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Les trois procédés : tableau comparatif -----------------------------
        entete_tab = Text("Trois procédés de métallisation", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.3)

        tableau = _tableau(
            ["Procédé", "Métal", "Application", "Si rayé"],
            [
                ["Galvanisation", "zinc", "tôles, barbelés,\npylônes", "protège\nquand même"],
                ["Étamage", "étain", "boîtes de\nconserve", "corrosion\naccélérée"],
                ["Chromage", "chrome", "décoration,\nbarrière", "protection\nperdue"],
            ],
            col_widths=[2.6, 1.6, 2.8, 2.2],
            row_height=0.75,
            font_size=15,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.3)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Trois procédés de métallisation sont à connaître. La "
                "galvanisation dépose du zinc, utilisée pour les tôles, "
                "les fils barbelés ou les pylônes : elle protège le fer "
                "même rayé, par protection cathodique locale. L'étamage "
                "dépose de l'étain, utilisé pour les boîtes de conserve : "
                "s'il est rayé, la corrosion du fer est au contraire "
                "accélérée. Le chromage dépose du chrome, surtout pour la "
                "décoration : c'est une simple barrière, qui perd toute "
                "efficacité une fois rayée."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- À retenir : exemple résolu 2 -----------------------------------------
        exemple = example_box(
            VGroup(
                Text(
                    "Deux clous en fer, l'un galvanisé (Zn), l'autre étamé (Sn),",
                    font_size=19, weight="BOLD",
                ),
                Text("sont rayés puis exposés à l'air humide. Que prévoir ?", font_size=19, weight="BOLD"),
                Text("Clou galvanisé : le zinc, plus réducteur, s'oxyde à", font_size=18, color=GREEN),
                Text("la place du fer → le fer reste protégé, même rayé.", font_size=18, color=GREEN),
                Text("Clou étamé : l'étain, moins réducteur, forme une", font_size=18, color=RED),
                Text("micropile qui accélère l'oxydation du fer mis à nu.", font_size=18, color=RED),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.35)
        _fit(exemple, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Exemple résolu : on raye deux clous en fer, l'un "
                "galvanisé au zinc, l'autre étamé à l'étain, avant de les "
                "exposer à l'air humide. Que prévoir ? Pour le clou "
                "galvanisé, le zinc, plus réducteur que le fer, continue "
                "de s'oxyder à sa place : le fer reste protégé, même "
                "rayé. Pour le clou étamé, l'étain, moins réducteur que "
                "le fer, forme au contraire une micropile qui accélère "
                "l'oxydation du fer mis à nu à l'endroit de la rayure."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
