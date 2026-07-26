"""
scenes/Chimie_OxydoreductionSolutionAqueuse_09.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 09.

§ Retour sur les couples oxygénés + schéma expérimental détaillé de
l'expérience fondamentale (lame de fer + Cu²⁺, transfert d'électrons,
construit avec des primitives Manim de base) ; permanganate/dichromate/
diiode utilisés comme tests colorés de présence d'un réducteur.
Source : 1ereC/Chimie.pdf, chapitre 9, page 92.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GRAY,
    LEFT,
    ORANGE,
    PURPLE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
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
from shapes.boxes import example_box, property_box, scene_title, warning_box


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


def _schema_transfert_electrons():
    """Schéma détaillé de l'expérience fondamentale (lame de fer dans une
    solution de sulfate de cuivre II), avec la flèche de transfert
    d'électrons Fe → Cu²⁺, construit uniquement avec des primitives Manim
    de base (Line, Rectangle, Circle, Arrow, MathTex, Text, VGroup)."""
    largeur, hauteur = 3.4, 2.4
    demi = largeur / 2

    paroi_gauche = Line([-demi, hauteur / 2, 0], [-demi, -hauteur / 2, 0], color=WHITE, stroke_width=3)
    fond = Line([-demi, -hauteur / 2, 0], [demi, -hauteur / 2, 0], color=WHITE, stroke_width=3)
    paroi_droite = Line([demi, -hauteur / 2, 0], [demi, hauteur / 2, 0], color=WHITE, stroke_width=3)
    cuve = VGroup(paroi_gauche, fond, paroi_droite)

    niveau = 1.7
    liquide = Rectangle(width=largeur - 0.05, height=niveau, fill_color=BLUE, fill_opacity=0.5, stroke_width=0)
    liquide.move_to([0, -hauteur / 2 + niveau / 2, 0])

    lame_hauteur = hauteur + 0.5
    lame = Rectangle(width=0.22, height=lame_hauteur, fill_color=GRAY, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    lame.move_to([-0.6, -hauteur / 2 + 0.15 + lame_hauteur / 2, 0])
    label_lame = Text("Fe", font_size=16, color=WHITE)
    label_lame.next_to(lame, UP, buff=0.08)

    # Ion Cu²⁺ en solution, proche de la lame, relié par une flèche
    # d'électrons partant de la surface du fer.
    ion_cu = Circle(radius=0.16, color=BLUE, fill_color=BLUE, fill_opacity=0.9, stroke_width=1)
    ion_cu.move_to(lame.get_center() + [0.8, 0.2, 0])
    label_cu = MathTex(r"Cu^{2+}", font_size=18, color=WHITE)
    label_cu.move_to(ion_cu.get_center())

    fleche_electrons = Arrow(
        lame.get_right() + UP * 0.2,
        ion_cu.get_left(),
        color=YELLOW, stroke_width=3, buff=0.08, max_tip_length_to_length_ratio=0.35,
    )
    label_electrons = MathTex(r"2\,e^-", font_size=18, color=YELLOW)
    label_electrons.next_to(fleche_electrons, UP, buff=0.05)

    # Atome de fer qui quitte la lame sous forme d'ion Fe²⁺ dans la solution
    ion_fe = Circle(radius=0.16, color="#7A9A6B", fill_color="#7A9A6B", fill_opacity=0.9, stroke_width=1)
    ion_fe.move_to(lame.get_center() + [0.8, -0.5, 0])
    label_fe = MathTex(r"Fe^{2+}", font_size=17, color=WHITE)
    label_fe.move_to(ion_fe.get_center())

    schema = VGroup(
        cuve, liquide, lame, label_lame,
        ion_cu, label_cu,
        fleche_electrons, label_electrons,
        ion_fe, label_fe,
    )
    return schema


class RetourCouplesOxygenesEtSchema(NotionScene):
    def construct(self):
        titre = scene_title("9.9 Retour sur les couples oxygénés — schéma du transfert d'électrons")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : reprendre l'expérience fondamentale avec tout ce qu'on sait --
        schema = _schema_transfert_electrons()
        schema.scale(1.15)
        schema.next_to(titre, DOWN, buff=0.55).shift(LEFT * 2.6)

        texte = Text(
            _wrap(
                "Revenons à l'expérience fondamentale du début de "
                "chapitre, avec tout le vocabulaire acquis depuis : au "
                "contact de la lame de fer, chaque ion Cu²⁺ capte "
                "directement deux électrons cédés par un atome de fer.",
                width=34,
            ),
            font_size=20,
            color=WHITE,
        )
        texte.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Revenons à l'expérience fondamentale du début de "
                "chapitre, en mobilisant tout le vocabulaire acquis "
                "depuis. Au contact de la lame de fer, chaque ion cuivre "
                "deux plus de la solution capte directement deux "
                "électrons, cédés par un atome de fer situé à la surface "
                "de la lame."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(schema))
            self.play(FadeIn(texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(texte))

        # --- Raisonnement : ce schéma résume tout le chapitre ------------------------
        entete_resume = Text("Ce schéma résume toute la notion", font_size=22, color=YELLOW, weight="BOLD")
        entete_resume.next_to(titre, DOWN, buff=0.4)

        resume = _bullets(
            [
                "Fe (réducteur du couple Fe²⁺/Fe) cède 2 électrons : "
                "il s'oxyde ;",
                "Cu²⁺ (oxydant du couple Cu²⁺/Cu) capte ces 2 électrons : "
                "il se réduit ;",
                "les électrons ne circulent jamais librement en solution : "
                "le transfert se fait au contact direct des deux espèces.",
            ],
            width=52,
        )
        resume.next_to(entete_resume, DOWN, buff=0.35)
        groupe_resume = VGroup(entete_resume, resume)

        with self.voiceover(
            text=(
                "Ce schéma résume toute la notion. Le fer, réducteur du "
                "couple fer deux plus sur fer, cède deux électrons : il "
                "s'oxyde. L'ion cuivre deux plus, oxydant du couple cuivre "
                "deux plus sur cuivre, capte ces deux électrons : il se "
                "réduit. Et surtout : les électrons ne circulent jamais "
                "librement dans la solution, contrairement à ce qu'on "
                "pourrait croire — le transfert se fait au contact direct "
                "entre les deux espèces chimiques."
            )
        ) as tracker:
            self.play(FadeIn(entete_resume))
            self.play(FadeIn(resume))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_resume))

        # --- Exemple traité : les oxydants colorés comme tests de réducteurs --------
        entete_tests = Text("Les oxydants colorés, des tests de présence d'un réducteur", font_size=19, color=YELLOW, weight="BOLD")
        entete_tests.next_to(titre, DOWN, buff=0.35)

        tests = _bullets(
            [
                "quelques gouttes de permanganate (violet) qui se "
                "décolorent au contact d'un liquide révèlent la présence "
                "d'un réducteur ;",
                "le dichromate (orange) qui vire au vert révèle, lui "
                "aussi, la présence d'un réducteur (ex : alcootest) ;",
                "l'eau iodée (brune) qui se décolore révèle un réducteur "
                "comme la vitamine C (acide ascorbique).",
            ],
            width=52,
        )
        tests.next_to(entete_tests, DOWN, buff=0.35)
        groupe_tests = VGroup(entete_tests, tests)
        _fit(groupe_tests, titre.get_bottom()[1] - 0.35)
        groupe_tests.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Les couples oxygénés étudiés dans ce chapitre sont "
                "d'ailleurs utilisés comme de véritables tests colorés de "
                "présence d'un réducteur. Quelques gouttes de permanganate, "
                "violet, qui se décolorent au contact d'un liquide, "
                "révèlent la présence d'un réducteur. Le dichromate, "
                "orange, qui vire au vert, révèle lui aussi la présence "
                "d'un réducteur — c'est le principe des anciens "
                "alcootests. Et l'eau iodée, brune, qui se décolore, "
                "révèle un réducteur comme la vitamine C, l'acide "
                "ascorbique."
            )
        ) as tracker:
            self.play(FadeIn(entete_tests))
            self.play(FadeIn(tests))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tests))

        # --- À retenir : le principe du test qualitatif -------------------------------
        recap = property_box(
            Text(
                _wrap(
                    "Retenir : décolorer un oxydant coloré (permanganate, "
                    "dichromate, diiode) est un test qualitatif simple et "
                    "rapide de la présence d'un réducteur dans une "
                    "solution.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        recap.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ceci : décolorer un oxydant coloré, comme le "
                "permanganate, le dichromate ou le diiode, est un test "
                "qualitatif simple et rapide de la présence d'un réducteur "
                "dans une solution."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : un test coloré n'identifie pas le réducteur -----------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : un test coloré prouve la PRÉSENCE d'un "
                    "réducteur, mais ne l'IDENTIFIE pas. Pour savoir "
                    "lequel, il faut d'autres informations (contexte, "
                    "autres tests) — la décoloration seule ne suffit "
                    "jamais à conclure sur la nature exacte de l'espèce.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)
        _fit(piege, titre.get_bottom()[1] - 0.5)

        with self.voiceover(
            text=(
                "Attention à un dernier piège : un test coloré prouve la "
                "présence d'un réducteur, mais ne l'identifie pas "
                "précisément. Pour savoir de quel réducteur il s'agit, il "
                "faut d'autres informations, comme le contexte ou d'autres "
                "tests complémentaires — la simple décoloration ne suffit "
                "jamais, à elle seule, à conclure sur la nature exacte de "
                "l'espèce présente."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
