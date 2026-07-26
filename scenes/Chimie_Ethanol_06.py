"""
scenes/Chimie_Ethanol_06.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 06.

§ 4.2 Oxydation ménagée de l'éthanol — la lampe sans flamme. Définition de
l'oxydation ménagée. Protocole expérimental (fil de cuivre chauffé au
rouge + vapeurs d'éthanol, papier réactif de Schiff + papier pH),
observations (incandescence entretenue = exothermique, odeur de pomme,
Schiff rosit → éthanal, papier pH rouge → acide éthanoïque), équations en
2 étapes (2CH₃-CH₂-OH+O₂→2CH₃-CHO+2H₂O puis 2CH₃-CHO+O₂→2CH₃-COOH), rôle
catalyseur du cuivre.
Source : 1ereC/Chimie.pdf, chapitre 7, pages 71-72.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    PINK,
    Arrow,
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
from shapes.boxes import definition_box, property_box, scene_title, warning_box


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


def _schema_lampe_sans_flamme():
    """Schéma simplifié de l'expérience de la lampe sans flamme (flacon
    d'éthanol + spirale de cuivre incandescente + papiers-tests), construit
    uniquement avec des primitives Manim de base."""

    flacon = Rectangle(width=1.4, height=1.8, color=WHITE, stroke_width=3)
    flacon.move_to([-2.3, -0.7, 0])
    label_flacon = Text("éthanol\n(vapeurs)", font_size=13, color=WHITE, line_spacing=0.8)
    label_flacon.move_to(flacon.get_center() + DOWN * 0.4)

    # Spirale de cuivre représentée par une ligne en zig-zag
    spirale_pts = [
        [-2.3 + dx * 0.18, -0.1 + (0.12 if i % 2 == 0 else -0.12), 0]
        for i, dx in enumerate(range(-3, 4))
    ]
    spirale = VGroup(*[
        Line(spirale_pts[i], spirale_pts[i + 1], color=ORANGE, stroke_width=4)
        for i in range(len(spirale_pts) - 1)
    ])
    label_cuivre = Text("fil de cuivre\nincandescent (catalyseur)", font_size=12, color=ORANGE, line_spacing=0.8)
    label_cuivre.next_to(spirale, UP, buff=0.15)

    # Papier de Schiff et papier pH, à l'entrée du flacon
    papier_schiff = Rectangle(width=0.35, height=0.9, color=PINK, fill_color=PINK, fill_opacity=0.6, stroke_width=1)
    papier_schiff.next_to(flacon, RIGHT, buff=0.5).shift(UP * 0.35)
    label_schiff = Text("papier de Schiff\n(rosit → éthanal)", font_size=12, color=PINK, line_spacing=0.8)
    label_schiff.next_to(papier_schiff, RIGHT, buff=0.15)

    papier_ph = Rectangle(width=0.35, height=0.9, color=RED, fill_color=RED, fill_opacity=0.6, stroke_width=1)
    papier_ph.next_to(papier_schiff, DOWN, buff=0.55)
    label_ph = Text("papier pH\n(rouge → acide)", font_size=12, color=RED, line_spacing=0.8)
    label_ph.next_to(papier_ph, RIGHT, buff=0.15)

    fleche = Arrow(flacon.get_right(), papier_schiff.get_left(), color=YELLOW, stroke_width=2, buff=0.1, max_tip_length_to_length_ratio=0.2)

    return VGroup(
        flacon, label_flacon,
        spirale, label_cuivre,
        fleche,
        papier_schiff, label_schiff,
        papier_ph, label_ph,
    )


class OxydationMenageeLampeSansFlamme(NotionScene):
    def construct(self):
        titre = scene_title("7.4 Oxydation ménagée — la lampe sans flamme")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définition de l'oxydation ménagée --------------------------
        def_ox = definition_box(
            Text(
                _wrap(
                    "Une oxydation ménagée consiste à oxyder un composé "
                    "organique tout en conservant sa chaîne carbonée : "
                    "seul le groupe fonctionnel est modifié.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        def_ox.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Après la combustion, qui détruit totalement la "
                "molécule, découvrons une oxydation plus douce : "
                "l'oxydation ménagée. Une oxydation ménagée consiste à "
                "oxyder un composé organique tout en conservant sa chaîne "
                "carbonée : seul le groupe fonctionnel est modifié. "
                "L'expérience historique qui l'illustre s'appelle la "
                "lampe sans flamme."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_ox))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ox))

        # --- Raisonnement : protocole expérimental --------------------------------
        entete_protocole = Text("Protocole : la lampe sans flamme", font_size=22, color=YELLOW, weight="BOLD")
        entete_protocole.next_to(titre, DOWN, buff=0.35)

        schema = _schema_lampe_sans_flamme()
        schema.scale(0.95)
        schema.next_to(entete_protocole, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Protocole : on introduit de l'éthanol dans un flacon. On "
                "approche de la surface du liquide une spirale de fil de "
                "cuivre, préalablement chauffée au rouge. À l'entrée du "
                "flacon, on dispose un papier imbibé de réactif de "
                "Schiff et un papier pH."
            )
        ) as tracker:
            self.play(FadeIn(entete_protocole))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_protocole), FadeOut(schema))

        # --- Exemple traité : observations + équations ----------------------------
        entete_obs = Text("Observations", font_size=22, color=YELLOW, weight="BOLD")
        entete_obs.next_to(titre, DOWN, buff=0.35)

        observations = _bullets(
            [
                "Le fil de cuivre reste incandescent : la réaction "
                "dégage de la chaleur (exothermique) — d'où le nom de "
                "« lampe sans flamme ».",
                "Une odeur de pomme se dégage.",
                "Le papier de Schiff rosit : il s'est formé un aldéhyde, "
                "l'éthanal CH₃-CHO.",
                "Le papier pH vire au rouge : il s'est aussi formé un "
                "acide, l'acide éthanoïque CH₃-COOH.",
            ],
            font_size=19,
            width=56,
        )
        observations.next_to(entete_obs, DOWN, buff=0.3)
        _fit(VGroup(entete_obs, observations), entete_obs.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici les observations. Le fil de cuivre reste "
                "incandescent : la réaction dégage donc de la chaleur, "
                "elle est exothermique, et c'est elle qui entretient "
                "l'incandescence, d'où le nom de lampe sans flamme. Une "
                "odeur de pomme se dégage. Le papier imbibé de réactif de "
                "Schiff rosit : il s'est formé un aldéhyde, l'éthanal, "
                "C-H-3 tiret C-H-O. Le papier pH vire au rouge : il s'est "
                "aussi formé un acide, l'acide éthanoïque, C-H-3 tiret "
                "C-O-O-H."
            )
        ) as tracker:
            self.play(FadeIn(entete_obs))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_obs), FadeOut(observations))

        entete_eq = Text("Équations-bilans (catalyseur : cuivre)", font_size=21, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.4)

        eq1 = MathTex(r"2\,CH_3{-}CH_2{-}OH + O_2 \longrightarrow 2\,CH_3{-}CHO + 2\,H_2O", font_size=25, color=WHITE)
        eq1.next_to(entete_eq, DOWN, buff=0.4)

        eq2_texte = Text("puis, si le dioxygène est en excès :", font_size=18, color=WHITE)
        eq2_texte.next_to(eq1, DOWN, buff=0.35)

        eq2 = MathTex(r"2\,CH_3{-}CHO + O_2 \longrightarrow 2\,CH_3{-}COOH", font_size=25, color=WHITE)
        eq2.next_to(eq2_texte, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Les équations-bilans s'écrivent, avec le cuivre comme "
                "catalyseur : deux C-H-3 tiret C-H-2 tiret O-H, plus "
                "O-2, donne deux C-H-3 tiret C-H-O, plus deux H-2-O. "
                "Puis, si le dioxygène est en excès, une seconde étape a "
                "lieu : deux C-H-3 tiret C-H-O, plus O-2, donne deux "
                "C-H-3 tiret C-O-O-H. Le cuivre est un catalyseur : il "
                "accélère la réaction sans être consommé."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(eq1))
            self.play(FadeIn(eq2_texte))
            self.play(Write(eq2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(eq1), FadeOut(eq2_texte), FadeOut(eq2))

        # --- À retenir : fiche récapitulative ---------------------------------------
        propriete = property_box(
            VGroup(
                Text("Éthanol —(Cu, O₂)→ éthanal —(O₂ excès)→ acide éthanoïque", font_size=20, weight="BOLD"),
                Text("Le cuivre est un catalyseur : il n'est jamais consommé", font_size=19),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=12.0,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'oxydation ménagée de l'éthanol "
                "par le dioxygène de l'air, catalysée par le cuivre, "
                "donne d'abord l'éthanal, puis, si le dioxygène est en "
                "excès, l'acide éthanoïque. Le cuivre, comme tout "
                "catalyseur, accélère la réaction sans jamais être "
                "consommé."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : catalyseur ≠ réactif ---------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas écrire le cuivre comme réactif dans l'équation "
                    ": c'est un catalyseur, il n'apparaît qu'au-dessus de "
                    "la flèche (ou en légende), jamais avec un "
                    "coefficient stœchiométrique dans les réactifs ou les "
                    "produits.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas écrire le cuivre comme un réactif "
                "dans l'équation-bilan : c'est un catalyseur, il "
                "n'apparaît qu'au-dessus de la flèche, ou en légende, "
                "mais jamais avec un coefficient stœchiométrique parmi "
                "les réactifs ou les produits."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
