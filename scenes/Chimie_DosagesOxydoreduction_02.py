"""
scenes/Chimie_DosagesOxydoreduction_02.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 02.

§ L'équivalence et son repérage : définition de l'équivalence, lecture
électronique de l'équivalence (électrons cédés = électrons captés), les 3
modes de repérage (auto-indication, indicateur coloré, couleur propre des
couples), tableau des couleurs à connaître (MnO4-, Mn2+, Fe3+, Fe2+,
Cr2O7^2-, Cr3+, I2, I-), schéma du dispositif expérimental (burette +
erlenmeyer + agitateur magnétique).
Source : 1ereC/Chimie.pdf, chapitre 12, pages 114-115.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GRAY,
    Arrow,
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    ManimColor,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _ligne_couleur(formule_tex, hex_color, nom_couleur):
    """Une ligne du tableau des couleurs : formule + pastille + nom."""
    formule = MathTex(formule_tex, font_size=26, color=WHITE)
    pastille = Rectangle(
        width=0.5, height=0.32, fill_color=ManimColor(hex_color), fill_opacity=1.0,
        stroke_color=WHITE, stroke_width=1,
    )
    nom = Text(nom_couleur, font_size=20, color=WHITE)
    ligne = VGroup(formule, pastille, nom).arrange(RIGHT, buff=0.3)
    return ligne


def _tableau_couleurs():
    lignes = VGroup(
        _ligne_couleur(r"MnO_4^-", "#7A1FA2", "violet"),
        _ligne_couleur(r"Mn^{2+}", "#EDEDED", "quasi incolore (rose très pâle)"),
        _ligne_couleur(r"Fe^{3+}", "#D99A1B", "jaune-orangé"),
        _ligne_couleur(r"Fe^{2+}", "#BFE0B0", "vert très pâle"),
        _ligne_couleur(r"Cr_2O_7^{2-}", "#E06A1A", "orange"),
        _ligne_couleur(r"Cr^{3+}", "#3C8F5C", "vert"),
        _ligne_couleur(r"I_2", "#5A3A1A", "brun (jaune pâle si dilué)"),
        _ligne_couleur(r"I^-", "#F2F2F2", "incolore"),
    ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
    return lignes


def _schema_dispositif_dosage():
    """Schéma simplifié burette + erlenmeyer + agitateur magnétique,
    construit uniquement avec des primitives Manim de base (Line,
    Rectangle, Polygon, Ellipse, Arrow, MathTex/Text, VGroup)."""

    # Potence (support vertical + pied)
    tige = Line([0, 2.0, 0], [0, -1.6, 0], color=GRAY, stroke_width=4)
    pied = Line([-0.6, -1.6, 0], [0.6, -1.6, 0], color=GRAY, stroke_width=4)
    pince = Rectangle(width=0.5, height=0.15, color=GRAY, fill_color=GRAY, fill_opacity=1, stroke_width=0)
    pince.move_to([0.35, 1.5, 0])

    # Burette graduée : long tube fin, fixé sur la potence
    burette_corps = Rectangle(width=0.35, height=2.6, color=WHITE, stroke_width=2)
    burette_corps.move_to([0.7, 1.0, 0])
    graduations = VGroup(
        *[
            Line(
                [burette_corps.get_left()[0], y, 0],
                [burette_corps.get_left()[0] + 0.12, y, 0],
                color=WHITE, stroke_width=1.5,
            )
            for y in [1.9, 1.5, 1.1, 0.7, 0.3]
        ]
    )
    liquide_burette = Rectangle(
        width=0.31, height=1.6, fill_color=ManimColor("#7A1FA2"), fill_opacity=0.85, stroke_width=0,
    )
    liquide_burette.move_to(burette_corps.get_bottom() + [0, 0.8, 0])
    robinet = Rectangle(width=0.22, height=0.18, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=1)
    robinet.next_to(burette_corps, DOWN, buff=0)
    goutte = Ellipse(width=0.1, height=0.16, fill_color=ManimColor("#7A1FA2"), fill_opacity=1, stroke_width=0)
    goutte.next_to(robinet, DOWN, buff=0.15)

    label_burette = Text("burette graduée\n(solution titrante)", font_size=15, color=WHITE, line_spacing=0.8)
    label_burette.next_to(burette_corps, RIGHT, buff=0.35)

    # Erlenmeyer : forme conique obtenue avec un Polygon
    sommet_col_g = [burette_corps.get_bottom()[0] - 0.35, -0.55, 0]
    sommet_col_d = [burette_corps.get_bottom()[0] + 0.35, -0.55, 0]
    base_g = [burette_corps.get_bottom()[0] - 1.3, -1.75, 0]
    base_d = [burette_corps.get_bottom()[0] + 1.3, -1.75, 0]
    erlenmeyer = Polygon(
        sommet_col_g, sommet_col_d, base_d, base_g,
        color=WHITE, stroke_width=3,
    )
    solution = Polygon(
        [sommet_col_g[0], -1.1, 0], [sommet_col_d[0], -1.1, 0], base_d, base_g,
        fill_color=ManimColor("#BFE0B0"), fill_opacity=0.75, stroke_width=0,
    )
    label_erlen = Text("erlenmeyer\n(solution titrée)", font_size=15, color=WHITE, line_spacing=0.8)
    label_erlen.next_to(erlenmeyer, LEFT, buff=0.4)

    # Agitateur magnétique : plaque + barreau aimanté au fond de l'erlenmeyer
    plaque = Rectangle(width=2.9, height=0.22, color=GRAY, fill_color=GRAY, fill_opacity=1, stroke_width=0)
    plaque.next_to(erlenmeyer, DOWN, buff=0)
    barreau = Ellipse(width=0.4, height=0.12, fill_color="#333333", fill_opacity=1, stroke_width=1, color=WHITE)
    barreau.move_to([base_g[0] + 1.3, -1.68, 0])
    label_agit = Text("agitateur magnétique", font_size=14, color=GRAY)
    label_agit.next_to(plaque, DOWN, buff=0.12)

    fleche_goutte = Arrow(
        goutte.get_bottom(), goutte.get_bottom() + [0, -0.35, 0],
        color=ManimColor("#7A1FA2"), stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.5,
    )

    schema = VGroup(
        tige, pied, pince,
        burette_corps, graduations, liquide_burette, robinet, goutte, fleche_goutte, label_burette,
        erlenmeyer, solution, label_erlen,
        plaque, barreau, label_agit,
    )
    return schema


class EquivalenceEtReperage(NotionScene):
    def construct(self):
        titre = scene_title("12.2 L'équivalence et son repérage")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : le problème du repérage ------------------------------------
        intro = Text(
            _wrap(
                "Pendant le dosage, comment savoir précisément à quel "
                "moment arrêter de verser la solution titrante ? Ce "
                "moment précis s'appelle l'équivalence.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pendant un dosage, comment savoir précisément à quel "
                "moment arrêter de verser la solution titrante ? Ce moment "
                "précis, où la réaction vient tout juste de se terminer, "
                "s'appelle l'équivalence. Voyons comment la définir, puis "
                "comment la repérer expérimentalement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition + lecture électronique --------------------
        def_eq = definition_box(
            Text(
                _wrap(
                    "L'équivalence d'un dosage est l'instant où les "
                    "réactifs (titrant et titré) ont été mélangés dans les "
                    "proportions exactes de l'équation de la réaction : "
                    "ils sont alors entièrement consommés l'un et "
                    "l'autre, sans excès.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        def_eq.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'équivalence d'un dosage est l'instant où les réactifs, "
                "titrant et titré, ont été mélangés exactement dans les "
                "proportions de l'équation de la réaction : à cet "
                "instant précis, ils sont entièrement consommés l'un et "
                "l'autre, sans qu'aucun ne soit en excès."
            )
        ) as tracker:
            self.play(FadeIn(def_eq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_eq))

        theo_electrons = theorem_box(
            Text(
                _wrap(
                    "Lecture électronique de l'équivalence : à "
                    "l'équivalence, le nombre d'électrons CÉDÉS par le "
                    "réducteur est exactement égal au nombre d'électrons "
                    "CAPTÉS par l'oxydant.",
                    width=46,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        theo_electrons.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On peut aussi lire l'équivalence de façon électronique : "
                "à l'équivalence, le nombre d'électrons cédés par le "
                "réducteur est exactement égal au nombre d'électrons "
                "captés par l'oxydant. C'est cette égalité qui nous "
                "servira de base pour établir toutes les relations de "
                "calcul de ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(theo_electrons))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_electrons))

        # --- Raisonnement : les 3 modes de repérage -------------------------------
        entete_modes = Text("Les 3 modes de repérage de l'équivalence", font_size=22, color=YELLOW, weight="BOLD")
        entete_modes.next_to(titre, DOWN, buff=0.35)

        modes = _bullets(
            [
                "AUTO-INDICATION : un des réactifs change lui-même de "
                "couleur (ex : permanganate de potassium, violet, devient "
                "incolore une fois réduit).",
                "INDICATEUR COLORÉ : on ajoute une substance qui change "
                "nettement de couleur à l'équivalence (ex : empois "
                "d'amidon avec le diiode).",
                "COULEUR PROPRE DES COUPLES : on suit le changement de "
                "couleur d'un couple présent (ex : dichromate, orange, "
                "vire au vert du chrome III).",
            ],
            font_size=19,
            width=54,
        )
        modes.next_to(entete_modes, DOWN, buff=0.3)
        groupe_modes = VGroup(entete_modes, modes)
        _fit(groupe_modes, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Expérimentalement, on repère l'équivalence de trois "
                "façons. Premièrement, par auto-indication : un des "
                "réactifs change lui-même de couleur, par exemple le "
                "permanganate de potassium, violet, devient incolore une "
                "fois réduit. Deuxièmement, à l'aide d'un indicateur "
                "coloré, une substance ajoutée qui change nettement de "
                "couleur à l'équivalence, par exemple l'empois d'amidon "
                "avec le diiode. Troisièmement, en suivant la couleur "
                "propre d'un couple présent dans le mélange, par exemple "
                "le dichromate, orange, qui vire au vert de l'ion chrome "
                "trois."
            )
        ) as tracker:
            self.play(FadeIn(entete_modes))
            self.play(FadeIn(modes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_modes))

        # --- Exemple traité : tableau des couleurs --------------------------------
        entete_tab = Text("Tableau des couleurs à connaître", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_couleurs()
        tableau.scale(0.85)
        tableau.next_to(entete_tab, DOWN, buff=0.3)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici les couleurs à connaître par cœur pour ce "
                "chapitre. L'ion permanganate M-n-O-4 moins est violet, "
                "l'ion manganèse deux plus est quasiment incolore, rose "
                "très pâle. L'ion fer trois plus est jaune orangé, l'ion "
                "fer deux plus est vert très pâle. L'ion dichromate est "
                "orange, l'ion chrome trois plus est vert. Le diiode est "
                "brun en solution concentrée, jaune pâle dilué, tandis "
                "que l'ion iodure est incolore."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- À retenir : le dispositif expérimental -------------------------------
        entete_disp = Text("Le dispositif expérimental de dosage", font_size=22, color=YELLOW, weight="BOLD")
        entete_disp.next_to(titre, DOWN, buff=0.35)

        schema = _schema_dispositif_dosage()
        schema.scale(0.85)
        schema.next_to(entete_disp, DOWN, buff=0.3)
        groupe_disp = VGroup(entete_disp, schema)
        _fit(groupe_disp, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Retenons le dispositif type d'un dosage direct. La "
                "solution titrante, ici colorée en violet, est versée "
                "goutte à goutte depuis la burette graduée fixée sur une "
                "potence. Elle tombe dans l'erlenmeyer contenant la "
                "solution titrée, maintenue en agitation constante grâce "
                "à un barreau aimanté posé sur un agitateur magnétique : "
                "cette agitation homogénéise le mélange et rend le "
                "changement de couleur bien net au moment de "
                "l'équivalence."
            )
        ) as tracker:
            self.play(FadeIn(entete_disp))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_disp))

        # --- Piège à éviter ----------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Près de l'équivalence, il faut ralentir le versement "
                    "puis passer goutte à goutte : s'arrêter dès la 1ère "
                    "goutte qui provoque un changement de couleur "
                    "PERSISTANT (au moins 30 secondes). Verser trop vite "
                    "fait dépasser l'équivalence et fausse Veq par excès.",
                    width=48,
                ),
                font_size=19,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège expérimental fréquent : à "
                "l'approche de l'équivalence, il faut impérativement "
                "ralentir le versement, puis passer goutte à goutte, et "
                "s'arrêter dès la première goutte qui provoque un "
                "changement de couleur persistant, pendant au moins une "
                "trentaine de secondes. Verser trop vite fait dépasser "
                "l'équivalence et fausse le volume Veq par excès."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
