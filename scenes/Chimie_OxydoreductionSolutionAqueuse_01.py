"""
scenes/Chimie_OxydoreductionSolutionAqueuse_01.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 01.

§ Mise en évidence expérimentale (lame de fer plongée dans une solution de
sulfate de cuivre II : dépôt rouge de cuivre, décoloration de la solution,
précipité vert de Fe²⁺ à la soude) + interprétation par demi-équations
(Cu²⁺+2e⁻→Cu et Fe→Fe²⁺+2e⁻) + définitions fondamentales (oxydation,
réduction, réducteur, oxydant, réaction d'oxydoréduction). Piège : l'oxydant
se réduit, le réducteur s'oxyde.
Source : 1ereC/Chimie.pdf, chapitre 9, pages 85-86.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GRAY,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
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
from shapes.boxes import definition_box, scene_title, warning_box


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


def _schema_experience(stade="initial"):
    """Schéma de l'expérience fondamentale : lame de fer plongée dans une
    solution de sulfate de cuivre II, construit uniquement avec des
    primitives Manim de base (Line, Rectangle, Circle, Text, VGroup).

    stade="initial" : solution bleue limpide, lame de fer grise et propre.
    stade="final"   : dépôt rouge de cuivre sur la lame, solution décolorée.
    """
    largeur, hauteur = 2.6, 2.2
    demi = largeur / 2

    paroi_gauche = Line([-demi, hauteur / 2, 0], [-demi, -hauteur / 2, 0], color=WHITE, stroke_width=3)
    fond = Line([-demi, -hauteur / 2, 0], [demi, -hauteur / 2, 0], color=WHITE, stroke_width=3)
    paroi_droite = Line([demi, -hauteur / 2, 0], [demi, hauteur / 2, 0], color=WHITE, stroke_width=3)
    cuve = VGroup(paroi_gauche, fond, paroi_droite)

    niveau = 1.6
    opacite = 0.75 if stade == "initial" else 0.22
    liquide = Rectangle(width=largeur - 0.05, height=niveau, fill_color=BLUE, fill_opacity=opacite, stroke_width=0)
    liquide.move_to([0, -hauteur / 2 + niveau / 2, 0])

    lame_hauteur = hauteur + 0.5
    lame = Rectangle(width=0.22, height=lame_hauteur, fill_color=GRAY, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    lame.move_to([0.5, -hauteur / 2 + 0.15 + lame_hauteur / 2, 0])

    depot = VGroup()
    if stade == "final":
        for i in range(6):
            point = Circle(radius=0.045, fill_color=RED, fill_opacity=1, stroke_width=0)
            point.move_to(lame.get_center() + [0.14, -0.75 + i * 0.18, 0])
            depot.add(point)

    label_lame = Text("Fe", font_size=16, color=WHITE)
    label_lame.next_to(lame, UP, buff=0.08)

    label_liquide = Text(
        "SO₄²⁻ + Cu²⁺ (bleue)" if stade == "initial" else "solution pâlie",
        font_size=13,
        color=WHITE,
    )
    label_liquide.move_to([-0.35, -hauteur / 2 + 0.3, 0])

    return VGroup(cuve, liquide, lame, depot, label_lame, label_liquide)


class MiseEnEvidenceExperimentaleDefinitions(NotionScene):
    def construct(self):
        titre = scene_title("9.1 Mise en évidence expérimentale — définitions")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : le protocole expérimental ----------------------------------
        schema_initial = _schema_experience("initial")
        schema_initial.scale(1.1)
        schema_initial.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.8)

        protocole = Text(
            _wrap(
                "On plonge une lame de fer, décapée et propre, dans une "
                "solution de sulfate de cuivre II, de couleur bleue "
                "(ions Cu²⁺ et SO₄²⁻).",
                width=36,
            ),
            font_size=22,
            color=WHITE,
        )
        protocole.next_to(schema_initial, RIGHT, buff=0.7)

        with self.voiceover(
            text=(
                "Commençons par une expérience fondamentale. On plonge une "
                "lame de fer, décapée et propre, dans une solution de "
                "sulfate de cuivre deux, de couleur bleue, qui contient des "
                "ions cuivre deux plus et des ions sulfate. Que va-t-il se "
                "passer ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(schema_initial))
            self.play(FadeIn(protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_initial), FadeOut(protocole))

        # --- Raisonnement : les observations --------------------------------------
        schema_final = _schema_experience("final")
        schema_final.scale(1.1)
        schema_final.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.8)

        observations = _bullets(
            [
                "un dépôt ROUGE de cuivre métallique se forme sur la lame ;",
                "la solution bleue se DÉCOLORE progressivement ;",
                "un test à la soude sur la solution donne un précipité "
                "VERT : c'est l'hydroxyde de fer II, preuve de "
                "l'apparition d'ions Fe²⁺.",
            ],
            width=36,
        )
        observations.next_to(schema_final, RIGHT, buff=0.6)

        groupe_obs = VGroup(schema_final, observations)

        with self.voiceover(
            text=(
                "Après quelques minutes, on observe trois choses. Un dépôt "
                "rouge de cuivre métallique se forme sur la lame de fer. La "
                "solution bleue se décolore progressivement. Et si l'on "
                "prélève un peu de cette solution pour y verser de la "
                "soude, on obtient un précipité vert : c'est l'hydroxyde de "
                "fer deux, la preuve que des ions fer deux plus sont "
                "apparus en solution."
            )
        ) as tracker:
            self.play(FadeIn(schema_final))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_obs))

        # --- Exemple traité : interprétation par demi-équations -------------------
        entete_interp = Text("Interprétation : transfert d'électrons", font_size=24, color=YELLOW, weight="BOLD")
        entete_interp.next_to(titre, DOWN, buff=0.4)

        demi_cu = MathTex(r"Cu^{2+} + 2\,e^- \longrightarrow Cu", font_size=32, color=WHITE)
        demi_cu.next_to(entete_interp, DOWN, buff=0.5)

        demi_fe = MathTex(r"Fe \longrightarrow Fe^{2+} + 2\,e^-", font_size=32, color=WHITE)
        demi_fe.next_to(demi_cu, DOWN, buff=0.45)

        fleche_electrons = MathTex(r"2\,e^-\ \text{transférés du fer vers les ions cuivre}", font_size=22, color=YELLOW)
        fleche_electrons.next_to(demi_fe, DOWN, buff=0.45)

        groupe_interp = VGroup(entete_interp, demi_cu, demi_fe, fleche_electrons)

        with self.voiceover(
            text=(
                "Voici l'interprétation. Les ions cuivre deux plus captent "
                "chacun deux électrons pour former du cuivre métallique : "
                "Cu deux plus, plus deux électrons, donne Cu. Dans le même "
                "temps, les atomes de fer cèdent chacun deux électrons pour "
                "former des ions fer deux plus : Fe donne Fe deux plus, "
                "plus deux électrons. Ces deux électrons sont directement "
                "transférés du fer vers les ions cuivre, au contact de la "
                "lame."
            )
        ) as tracker:
            self.play(FadeIn(entete_interp))
            self.play(Write(demi_cu))
            self.play(Write(demi_fe))
            self.play(FadeIn(fleche_electrons))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_interp))

        # --- À retenir : les quatre définitions fondamentales ----------------------
        def_oxydation = definition_box(
            Text(
                _wrap("Une oxydation est une PERTE d'un ou plusieurs électrons par une espèce chimique.", width=46),
                font_size=23,
            ),
        )
        def_oxydation.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Ces observations conduisent à quatre définitions "
                "fondamentales. Une oxydation est une perte d'un ou "
                "plusieurs électrons par une espèce chimique : c'est ce que "
                "subit le fer."
            )
        ) as tracker:
            self.play(FadeIn(def_oxydation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_oxydation))

        def_reduction = definition_box(
            Text(
                _wrap("Une réduction est un GAIN d'un ou plusieurs électrons par une espèce chimique.", width=46),
                font_size=23,
            ),
        )
        def_reduction.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Une réduction est un gain d'un ou plusieurs électrons par "
                "une espèce chimique : c'est ce que subissent les ions "
                "cuivre."
            )
        ) as tracker:
            self.play(FadeIn(def_reduction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_reduction))

        def_reducteur = definition_box(
            Text(
                _wrap("Un réducteur est une espèce chimique capable de CÉDER un ou plusieurs électrons.", width=46),
                font_size=23,
            ),
        )
        def_reducteur.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un réducteur est une espèce chimique capable de céder un "
                "ou plusieurs électrons : le fer métallique est ici le "
                "réducteur."
            )
        ) as tracker:
            self.play(FadeIn(def_reducteur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_reducteur))

        def_oxydant = definition_box(
            Text(
                _wrap("Un oxydant est une espèce chimique capable de CAPTER un ou plusieurs électrons.", width=46),
                font_size=23,
            ),
        )
        def_oxydant.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un oxydant est une espèce chimique capable de capter un ou "
                "plusieurs électrons : l'ion cuivre deux plus est ici "
                "l'oxydant."
            )
        ) as tracker:
            self.play(FadeIn(def_oxydant))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_oxydant))

        def_redox = definition_box(
            Text(
                _wrap(
                    "Une réaction d'oxydoréduction (ou réaction redox) est "
                    "une réaction chimique au cours de laquelle un ou "
                    "plusieurs électrons sont transférés d'un réducteur "
                    "vers un oxydant.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        def_redox.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Et pour finir, une réaction d'oxydoréduction, ou réaction "
                "redox, est une réaction chimique au cours de laquelle un "
                "ou plusieurs électrons sont transférés d'un réducteur vers "
                "un oxydant. C'est exactement ce qui se produit entre le "
                "fer et les ions cuivre."
            )
        ) as tracker:
            self.play(FadeIn(def_redox))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_redox))

        # --- Piège à éviter : le vocabulaire contre-intuitif -----------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège classique de vocabulaire : L'OXYDANT SE RÉDUIT "
                    "(il capte des électrons) et LE RÉDUCTEUR S'OXYDE (il "
                    "cède des électrons). Le nom de l'espèce et le nom de "
                    "la transformation qu'elle subit sont inversés en "
                    "apparence — ne les confondez pas.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Attention à un piège classique de vocabulaire : l'oxydant "
                "se réduit, puisqu'il capte des électrons, et le réducteur "
                "s'oxyde, puisqu'il cède des électrons. Le nom de l'espèce "
                "et le nom de la transformation qu'elle subit semblent "
                "inversés — c'est pourtant bien cela, ne les confondez pas."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
