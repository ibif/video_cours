"""
scenes/SVT_ProductionMatiere_02.py — Chapitre 11 (1ereD, SVT), scène 02.

§ 11.1 Les échanges gazeux entre le végétal vert et l'atmosphère :
expérience de l'élodée (dégagement de O2 à la lumière), expérience de la
plante sous cloche (absorption de CO2 à la lumière), respiration
nocturne (absorption de O2 / dégagement de CO2 à l'obscurité), propriété
récapitulative, tableau, piège « les plantes font l'inverse des
animaux », méthode d'interprétation en quatre étapes.
Source : 1ereD/SVT.pdf, pages 144-146.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORANGE,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Polygon,
    Rectangle,
    Text,
    Triangle,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.6, row_gap=0.3):
    """Tableau simple : chaque ligne partage la même hauteur (voir
    SVT_DivisionMeiotique_02.py pour l'explication de cette approche)."""
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
    d'un groupe boîte + schéma placés côte à côte) — l'ancrage haut/centre
    horizontal (le groupe est déjà centré en x avant l'appel) est
    préservé car `about_point` a x=0."""
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


def _schema_elodee():
    """Bécher + entonnoir renversé + tube à essai avec bulles de gaz."""
    becher = Polygon(
        [-1.1, -1.1, 0], [-1.1, 1.0, 0], [1.1, 1.0, 0], [1.1, -1.1, 0],
        color=WHITE, stroke_width=2, fill_opacity=0,
    )
    eau = Rectangle(width=2.15, height=1.9, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
    eau.move_to(becher.get_center() + DOWN * 0.05)

    elodee = VGroup(
        *[
            Line(ORIGIN, UP * 0.6, color=GREEN, stroke_width=4).shift(RIGHT * dx + DOWN * 0.9)
            for dx in [-0.3, -0.1, 0.1, 0.3]
        ]
    )

    entonnoir = Triangle(color=GRAY, fill_color=GRAY, fill_opacity=0.5, stroke_width=2)
    entonnoir.stretch_to_fit_width(1.3)
    entonnoir.stretch_to_fit_height(0.7)
    entonnoir.rotate(3.14159)
    entonnoir.move_to(becher.get_center() + DOWN * 0.1)

    tube = Rectangle(width=0.35, height=1.3, color=WHITE, stroke_width=2, fill_opacity=0)
    tube.next_to(entonnoir, UP, buff=0)

    gaz = Rectangle(width=0.31, height=0.4, fill_color=YELLOW, fill_opacity=0.7, stroke_width=0)
    gaz.align_to(tube, UP).shift(DOWN * 0.02)

    bulles = VGroup(
        *[Dot(radius=0.045, color=YELLOW).move_to(entonnoir.get_center() + UP * h + RIGHT * dx)
          for h, dx in [(0.1, -0.1), (0.3, 0.05), (0.5, -0.05)]]
    )

    label_o2 = Text("O2 collecté", font_size=16, color=YELLOW).next_to(tube, RIGHT, buff=0.15)
    label_elodee = Text("élodée", font_size=16, color=GREEN).next_to(becher, DOWN, buff=0.12)

    return VGroup(becher, eau, elodee, entonnoir, tube, gaz, bulles, label_o2, label_elodee)


def _schema_cloche(label, sombre=False, trouble=False):
    """Cloche simplifiée : dôme + base + petite plante + coupelle d'eau de chaux."""
    dome = Arc(radius=0.9, start_angle=0, angle=3.14159, color=WHITE, stroke_width=2)
    base = Line(LEFT * 0.9, RIGHT * 0.9, color=WHITE, stroke_width=2)
    base.move_to(dome.get_start() + (dome.get_end() - dome.get_start()) / 2)
    base.shift(DOWN * 0.02)
    cloche = VGroup(dome, base)

    if sombre:
        fond = Circle(radius=0.85, fill_color=GRAY, fill_opacity=0.35, stroke_width=0)
        fond.move_to(cloche.get_center() + UP * 0.15)
        cloche.add_to_back(fond)

    tige = Line(ORIGIN, UP * 0.55, color=GREEN, stroke_width=5)
    feuilles = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=0.8, stroke_width=0).scale(0.35)
    feuilles.next_to(tige, UP, buff=-0.05)
    plante = VGroup(tige, feuilles)
    plante.move_to(dome.get_center() + DOWN * 0.15)

    coupelle_couleur = WHITE if trouble else BLUE
    coupelle = Rectangle(width=0.5, height=0.12, fill_color=coupelle_couleur, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1.5)
    coupelle.next_to(plante, RIGHT, buff=0.15).align_to(base, DOWN).shift(UP * 0.05)

    titre = Text(label, font_size=16, color=YELLOW, weight="BOLD")
    titre.next_to(cloche, UP, buff=0.15)

    etat = Text("eau de chaux : trouble" if trouble else "eau de chaux : limpide", font_size=13, color=WHITE)
    etat.next_to(VGroup(cloche, plante, coupelle), DOWN, buff=0.15)

    return VGroup(cloche, plante, coupelle, titre, etat)


class EchangesGazeuxVegetalAtmosphere(NotionScene):
    def construct(self):
        # --- Énoncé --------------------------------------------------------
        titre = scene_title("11.1 — Les échanges gazeux avec l'atmosphère")
        titre.scale(0.55)
        titre.to_edge(UP)

        intro = Text(
            _wrap(
                "Avant de comprendre comment la matière est fabriquée, "
                "observons d'abord ce qui entre et ce qui sort d'un "
                "végétal vert, grâce à deux séries d'expériences.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant de comprendre comment la matière est fabriquée, "
                "observons d'abord ce qui entre et ce qui sort d'un "
                "végétal vert. Deux séries d'expériences classiques vont "
                "nous guider."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Exemple traité : l'expérience de l'élodée ----------------------
        exemple_elodee = example_box(
            Text(
                _wrap(
                    "Un rameau d'élodée est placé sous un entonnoir "
                    "renversé, coiffé d'un tube rempli d'eau, dans un "
                    "bécher éclairé. Des bulles de gaz montent et "
                    "s'accumulent dans le tube. Ce gaz ravive une braise "
                    "incandescente : c'est du dioxygène.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.5,
        )
        exemple_elodee.to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        schema_elodee = _schema_elodee()
        schema_elodee.scale(0.9)
        schema_elodee.next_to(exemple_elodee, RIGHT, buff=0.4)

        groupe_elodee = VGroup(exemple_elodee, schema_elodee)
        groupe_elodee.move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)
        _fit(groupe_elodee, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Premier exemple : l'expérience de l'élodée, une plante "
                "aquatique verte. On la place sous un entonnoir renversé, "
                "coiffé d'un tube à essai rempli d'eau, dans un bécher "
                "éclairé. Au bout de quelques minutes, de petites bulles "
                "de gaz apparaissent sur les feuilles et s'accumulent en "
                "haut du tube. On présente alors une allumette presque "
                "éteinte à ce gaz : la braise se ravive. Le seul gaz qui "
                "ravive une braise incandescente est le dioxygène : à la "
                "lumière, le végétal vert dégage donc du dioxygène dans le "
                "milieu."
            )
        ) as tracker:
            self.play(FadeIn(exemple_elodee))
            self.play(FadeIn(schema_elodee))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_elodee))

        # --- Exemple traité : la plante sous cloche -------------------------
        exemple_cloche = example_box(
            Text(
                _wrap(
                    "Deux plantes en pot, chacune avec une coupelle d'eau "
                    "de chaux, sous une cloche : l'une à la lumière (A), "
                    "l'autre à l'obscurité (B). Après plusieurs heures, "
                    "l'eau de chaux de A reste limpide ; celle de B se "
                    "trouble nettement.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.5,
        )
        exemple_cloche.to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        cloche_a = _schema_cloche("Cloche A — lumière", sombre=False, trouble=False)
        cloche_b = _schema_cloche("Cloche B — obscurité", sombre=True, trouble=True)
        cloches = VGroup(cloche_a, cloche_b).arrange(RIGHT, buff=0.6)
        cloches.scale(0.85)
        cloches.next_to(exemple_cloche, RIGHT, buff=0.4)

        groupe_cloche = VGroup(exemple_cloche, cloches)
        groupe_cloche.move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)
        _fit(groupe_cloche, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Deuxième exemple : deux montages identiques, chacun avec "
                "une jeune plante en pot et une coupelle d'eau de chaux, "
                "révélateur qui se trouble en présence de dioxyde de "
                "carbone. La cloche A est placée à la lumière, la cloche B "
                "à l'obscurité. Après plusieurs heures, l'eau de chaux de "
                "la cloche A reste limpide : le CO2 a été absorbé par la "
                "plante. L'eau de chaux de la cloche B se trouble "
                "nettement : la plante a rejeté du CO2. À la lumière, le "
                "végétal vert absorbe donc le dioxyde de carbone de "
                "l'atmosphère ; à l'obscurité, il en dégage au contraire."
            )
        ) as tracker:
            self.play(FadeIn(exemple_cloche))
            self.play(FadeIn(cloches))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_cloche))

        # --- Raisonnement : la respiration nocturne -------------------------
        with self.voiceover(
            text=(
                "L'expérience de la cloche B montre que, dans le noir, la "
                "plante rejette du CO2. Des expériences complémentaires, "
                "par exemple avec des graines en germination dans un "
                "flacon fermé, montrent qu'elle absorbe alors du "
                "dioxygène. Ce fonctionnement, qui consomme du O2 et "
                "rejette du CO2, est celui de la respiration : tous les "
                "êtres vivants, y compris les végétaux, respirent jour et "
                "nuit."
            )
        ) as tracker:
            self.wait(tracker.get_remaining_duration())

        # --- À retenir : propriété + tableau récapitulatif -------------------
        propriete = property_box(
            Text(
                _wrap(
                    "À la lumière, le végétal vert absorbe du CO2 et "
                    "dégage du O2 : fonctionnement lié à la production de "
                    "matière. À l'obscurité, il absorbe du O2 et dégage du "
                    "CO2 : seule la respiration est observable. En "
                    "réalité, la respiration a lieu jour et nuit, mais elle "
                    "est masquée à la lumière.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Résumons : à la lumière, le végétal vert absorbe du "
                "dioxyde de carbone et dégage du dioxygène, c'est le "
                "fonctionnement lié à la production de matière. À "
                "l'obscurité, il absorbe du dioxygène et dégage du "
                "dioxyde de carbone : seule la respiration est observable. "
                "En réalité, la respiration a lieu jour et nuit ; mais à "
                "la lumière, la production de matière consomme beaucoup de "
                "CO2 et produit beaucoup de O2, ce qui masque les échanges "
                "respiratoires."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        row1 = ["À la lumière", "CO2", "O2", "production de matière"]
        row2 = ["À l'obscurité", "O2", "CO2", "respiration seule"]
        entetes = ["Condition", "Gaz absorbé", "Gaz dégagé", "Fonctionnement dominant"]
        matrice = [
            [Text(c, font_size=19, color=YELLOW, weight="BOLD") for c in entetes],
            [Text(c, font_size=19, color=WHITE) for c in row1],
            [Text(c, font_size=19, color=WHITE) for c in row2],
        ]
        tableau = _grid_table(matrice, col_gap=0.5, row_gap=0.3)
        tableau.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Ce tableau résume la situation : à la lumière, gaz "
                "absorbé CO2, gaz dégagé O2, fonctionnement dominant, la "
                "production de matière. À l'obscurité, gaz absorbé O2, gaz "
                "dégagé CO2, fonctionnement dominant, la respiration "
                "seule."
            )
        ) as tracker:
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "« Les plantes font l'inverse des animaux, donc elles "
                    "ne respirent pas » : FAUX. La plante respire en "
                    "permanence, jour et nuit, comme l'animal. Ce qui lui "
                    "est propre, c'est un fonctionnement SUPPLÉMENTAIRE, "
                    "actif seulement à la lumière : absorption de CO2 et "
                    "dégagement de O2, plus intense que la respiration.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège classique : beaucoup d'élèves "
                "écrivent que la plante rejette du O2 et l'animal du CO2, "
                "donc que la plante ne respire pas. C'est faux. La plante "
                "respire en permanence, comme l'animal : elle consomme du "
                "O2 et rejette du CO2 jour et nuit. Ce qui est propre au "
                "végétal vert, c'est un fonctionnement supplémentaire, qui "
                "n'existe qu'à la lumière : l'absorption de CO2 et le "
                "dégagement de O2. À la lumière, ce fonctionnement est "
                "plus intense que la respiration, donc le bilan global "
                "visible est : entrée de CO2, sortie de O2."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- Méthode : interpréter une expérience en quatre étapes -----------
        methode = method_box(
            _bullets(
                [
                    "Étape 1 : décrire le dispositif (végétaux, lumière ou "
                    "obscurité, révélateur utilisé).",
                    "Étape 2 : citer l'observation exacte, sans la "
                    "traduire tout de suite.",
                    "Étape 3 : interpréter avec le révélateur (traduire "
                    "en termes de gaz).",
                    "Étape 4 : conclure sur le fonctionnement (formuler "
                    "la propriété générale).",
                ],
                font_size=20,
                width=54,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour analyser correctement toute expérience de ce type au "
                "baccalauréat, quatre étapes. Étape un : décrire le "
                "dispositif, quels végétaux, quelles conditions, quel "
                "révélateur. Étape deux : citer l'observation exacte, ce "
                "que l'on voit, sans la traduire tout de suite. Étape "
                "trois : interpréter avec le révélateur, traduire "
                "l'observation en termes de gaz. Étape quatre : conclure "
                "sur le fonctionnement, formuler la propriété générale. Ne "
                "jamais sauter de l'observation directement à la "
                "conclusion sans l'étape d'interprétation : c'est l'erreur "
                "qui coûte le plus de points."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
