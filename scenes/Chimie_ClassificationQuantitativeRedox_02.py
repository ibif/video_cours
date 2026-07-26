"""
scenes/Chimie_ClassificationQuantitativeRedox_02.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 02.

§ 2. La pile Daniell : description et observations. Description du
montage (lame de zinc plongeant dans une solution de sulfate de zinc,
lame de cuivre plongeant dans une solution de sulfate de cuivre, pont
salin au chlorure de potassium reliant les deux compartiments, voltmètre
branché entre les deux lames) — schéma complet construit avec des
primitives Manim de base. Observations expérimentales : f.é.m. mesurée
≈ 1,10 V, le cuivre est le pôle positif, le zinc le pôle négatif, les
électrons circulent du zinc vers le cuivre dans le circuit extérieur, la
lame de zinc s'amincit, la lame de cuivre s'épaissit, la solution de
sulfate de cuivre bleue se décolore progressivement.
Source : 1ereC/Chimie.pdf, chapitre 11, pages 103-104.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    LIGHT_GRAY,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
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


def _schema_pile_daniell():
    """Schéma complet de la pile Daniell : deux béchers (Zn/ZnSO4 et
    Cu/CuSO4), pont salin, lames métalliques, fils et voltmètre — construit
    uniquement avec des primitives Manim de base (Line, Rectangle, Arrow,
    Circle, VGroup, Text)."""

    # Béchers
    becher_zn = Rectangle(width=2.6, height=1.9, color=LIGHT_GRAY, stroke_width=3)
    becher_zn.move_to([-3.2, -0.9, 0])
    becher_cu = Rectangle(width=2.6, height=1.9, color=LIGHT_GRAY, stroke_width=3)
    becher_cu.move_to([3.2, -0.9, 0])

    # Solutions (remplissage coloré, incolore pour ZnSO4, bleu pour CuSO4)
    solution_zn = Rectangle(
        width=2.5, height=1.6, fill_color=WHITE, fill_opacity=0.08, stroke_width=0,
    )
    solution_zn.move_to(becher_zn.get_bottom() + UP * 0.8)
    solution_cu = Rectangle(
        width=2.5, height=1.6, fill_color=BLUE, fill_opacity=0.45, stroke_width=0,
    )
    solution_cu.move_to(becher_cu.get_bottom() + UP * 0.8)

    label_zn_sol = Text("ZnSO₄ (aq)", font_size=15, color=WHITE)
    label_zn_sol.move_to(becher_zn.get_bottom() + UP * 0.35)
    label_cu_sol = Text("CuSO₄ (aq)", font_size=15, color=WHITE)
    label_cu_sol.move_to(becher_cu.get_bottom() + UP * 0.35)

    # Lames métalliques
    lame_zn = Rectangle(width=0.35, height=2.3, fill_color=LIGHT_GRAY, fill_opacity=0.9, stroke_width=1)
    lame_zn.move_to(becher_zn.get_center() + UP * 0.5)
    label_lame_zn = Text("Zn", font_size=20, color=WHITE, weight="BOLD")
    label_lame_zn.next_to(lame_zn, UP, buff=0.15)

    lame_cu = Rectangle(width=0.35, height=2.3, fill_color=ORANGE, fill_opacity=0.9, stroke_width=1)
    lame_cu.move_to(becher_cu.get_center() + UP * 0.5)
    label_lame_cu = Text("Cu", font_size=20, color=ORANGE, weight="BOLD")
    label_lame_cu.next_to(lame_cu, UP, buff=0.15)

    # Pont salin (tube en U simplifié par un arc de rectangle arrondi via
    # deux lignes verticales + une ligne horizontale en haut)
    pont_gauche = Line(
        [-3.2, 1.0, 0], [-3.2, 2.0, 0], color="#B08D57", stroke_width=10,
    )
    pont_haut = Line([-3.2, 2.0, 0], [3.2, 2.0, 0], color="#B08D57", stroke_width=10)
    pont_droit = Line([3.2, 2.0, 0], [3.2, 1.0, 0], color="#B08D57", stroke_width=10)
    pont_salin = VGroup(pont_gauche, pont_haut, pont_droit)
    label_pont = Text("pont salin (KCl)", font_size=16, color="#B08D57")
    label_pont.next_to(pont_haut, UP, buff=0.12)

    # Fil électrique + voltmètre
    fil_gauche = Line(lame_zn.get_top(), [-3.2, 3.0, 0], color=YELLOW, stroke_width=2)
    fil_droit = Line(lame_cu.get_top(), [3.2, 3.0, 0], color=YELLOW, stroke_width=2)
    fil_haut_g = Line([-3.2, 3.0, 0], [-0.55, 3.0, 0], color=YELLOW, stroke_width=2)
    fil_haut_d = Line([0.55, 3.0, 0], [3.2, 3.0, 0], color=YELLOW, stroke_width=2)

    voltmetre = Circle(radius=0.55, color=YELLOW, stroke_width=3)
    voltmetre.move_to([0, 3.0, 0])
    label_v = Text("V", font_size=26, color=YELLOW, weight="BOLD")
    label_v.move_to(voltmetre.get_center())

    fleche_electrons = Arrow(
        [-2.2, 3.35, 0], [2.2, 3.35, 0], color=WHITE, stroke_width=3, buff=0,
        max_tip_length_to_length_ratio=0.08,
    )
    label_electrons = Text("sens de circulation des électrons", font_size=14, color=WHITE)
    label_electrons.next_to(fleche_electrons, UP, buff=0.1)

    return VGroup(
        becher_zn, becher_cu,
        solution_zn, solution_cu, label_zn_sol, label_cu_sol,
        lame_zn, lame_cu, label_lame_zn, label_lame_cu,
        pont_salin, label_pont,
        fil_gauche, fil_droit, fil_haut_g, fil_haut_d,
        voltmetre, label_v,
        fleche_electrons, label_electrons,
    )


class PileDaniellDescriptionObservations(NotionScene):
    def construct(self):
        titre = scene_title("11.2 La pile Daniell : description et observations")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : présentation du montage ------------------------------------
        intro = Text(
            _wrap(
                "Comment obtenir, à partir de deux couples oxydant sur "
                "réducteur, un courant électrique exploitable ? La "
                "première pile étudiée en cours est la pile Daniell, "
                "construite à partir des couples Zn²⁺/Zn et Cu²⁺/Cu.",
                width=58,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment transformer une réaction d'oxydoréduction en "
                "courant électrique exploitable ? La pile historique qui "
                "répond à cette question est la pile Daniell, construite "
                "à partir des deux couples que nous connaissons déjà : "
                "zinc deux plus sur zinc, et cuivre deux plus sur cuivre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : description + schéma ---------------------------------
        entete_schema = Text("Description du montage", font_size=22, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.3)

        schema = _schema_pile_daniell()
        schema.scale(0.92)
        schema.next_to(entete_schema, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le montage comprend deux demi-piles. À gauche, une lame "
                "de zinc plonge dans une solution de sulfate de zinc. À "
                "droite, une lame de cuivre plonge dans une solution de "
                "sulfate de cuivre, reconnaissable à sa couleur bleue. Les "
                "deux compartiments sont reliés par un pont salin, ici "
                "rempli de chlorure de potassium, qui assure la fermeture "
                "du circuit électrique sans mélanger les solutions. Un "
                "voltmètre est branché entre les deux lames métalliques "
                "pour mesurer la tension aux bornes de la pile."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(Write(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(schema))

        # --- Exemple traité : observations quantitatives -------------------------
        entete_obs = Text("Observations expérimentales", font_size=22, color=YELLOW, weight="BOLD")
        entete_obs.next_to(titre, DOWN, buff=0.35)

        observations = _bullets(
            [
                "Le voltmètre indique une f.é.m. quasi constante, "
                "E ≈ 1,10 V.",
                "La lame de cuivre est le pôle positif (⊕), la lame de "
                "zinc le pôle négatif (⊖) de la pile.",
                "Dans le circuit extérieur, les électrons circulent de "
                "la lame de zinc vers la lame de cuivre.",
                "Au cours du temps : la lame de zinc s'amincit (elle est "
                "consommée), la lame de cuivre s'épaissit (du cuivre "
                "s'y dépose), et la couleur bleue de la solution de "
                "sulfate de cuivre se décolore progressivement.",
            ],
            font_size=19,
            width=56,
        )
        observations.next_to(entete_obs, DOWN, buff=0.3)
        _fit(VGroup(entete_obs, observations), entete_obs.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici les observations expérimentales. Le voltmètre "
                "indique une force électromotrice quasi constante, "
                "environ un virgule dix volt. La lame de cuivre constitue "
                "le pôle positif de la pile, la lame de zinc le pôle "
                "négatif. Dans le circuit extérieur, les électrons "
                "circulent de la lame de zinc vers la lame de cuivre. Au "
                "cours du temps, la lame de zinc s'amincit car elle est "
                "consommée, la lame de cuivre s'épaissit car du cuivre "
                "métallique s'y dépose, et la couleur bleue de la "
                "solution de sulfate de cuivre se décolore "
                "progressivement, signe que les ions cuivre deux plus "
                "sont consommés."
            )
        ) as tracker:
            self.play(FadeIn(entete_obs))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_obs), FadeOut(observations))

        # --- À retenir -------------------------------------------------------------
        recap = _bullets(
            [
                "Pile Daniell = lame Zn dans ZnSO₄ + lame Cu dans CuSO₄ + "
                "pont salin + voltmètre.",
                "f.é.m. ≈ 1,10 V ; pôle ⊕ = Cu, pôle ⊖ = Zn ; électrons : "
                "Zn → Cu dans le circuit extérieur.",
            ],
            font_size=21,
            width=56,
        )
        entete_recap = Text("À retenir", font_size=22, color="#288073", weight="BOLD")
        entete_recap.next_to(titre, DOWN, buff=0.4)
        recap.next_to(entete_recap, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de cette observation : la pile "
                "Daniell associe une lame de zinc dans une solution de "
                "sulfate de zinc, une lame de cuivre dans une solution de "
                "sulfate de cuivre, un pont salin et un voltmètre. Elle "
                "délivre une force électromotrice d'environ un virgule "
                "dix volt, avec le cuivre au pôle positif, le zinc au "
                "pôle négatif, et des électrons qui circulent du zinc "
                "vers le cuivre dans le circuit extérieur. Nous allons "
                "maintenant interpréter ces observations."
            )
        ) as tracker:
            self.play(FadeIn(entete_recap))
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_recap), FadeOut(recap), FadeOut(titre))
