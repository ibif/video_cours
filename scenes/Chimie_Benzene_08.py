"""
scenes/Chimie_Benzene_08.py — Chapitre 4 (1ereC, Chimie), scène 08.

§ Nitration du benzène : mélange sulfonitrique HNO3 + H2SO4 concentrés,
50-60 °C, C6H6 + HNO3 → C6H5NO2 + H2O, rôle double de H2SO4 (catalyseur +
agent déshydratant qui déplace l'équilibre), nitrobenzène → aniline
(colorants, médicaments). Tableau récapitulatif des 3 substitutions
(bromation / chloration / nitration) + exemple résolu 2 : masse de
bromobenzène obtenue à partir de 7,8 g de benzène.
Source : 1ereC/Chimie.pdf, chapitre 4, pages 41-42.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    ORANGE,
    FadeIn,
    FadeOut,
    Arrow,
    Line,
    MathTex,
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


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
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


class NitrationBenzene(NotionScene):
    def construct(self):
        titre = scene_title("8. La nitration du benzène")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le mélange sulfonitrique -----------------------------------
        enonce = Text(
            _wrap(
                "Une troisième substitution électrophile importante est "
                "la nitration : le benzène réagit avec l'acide nitrique "
                "concentré, en présence d'acide sulfurique concentré — le "
                "mélange dit \"sulfonitrique\" — vers 50-60 °C.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)
        _fit(enonce, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Une troisième réaction de substitution électrophile est "
                "essentielle : la nitration. Le benzène réagit avec "
                "l'acide nitrique concentré, en présence d'acide "
                "sulfurique concentré — ce mélange est appelé mélange "
                "sulfonitrique — porté à une température de cinquante à "
                "soixante degrés Celsius."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : équation + rôle double de H2SO4 --------
        entete = Text("L'équation de nitration et le rôle de H2SO4", font_size=22, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        equation = MathTex(
            r"C_6H_6 + HNO_3 \xrightarrow[50-60^{\circ}C]{H_2SO_4} C_6H_5NO_2 + H_2O",
            font_size=30,
            color=WHITE,
        )
        equation.next_to(entete, DOWN, buff=0.5)

        roles = _bullets(
            [
                "H2SO4 joue un double rôle : catalyseur de la réaction",
                "et agent déshydratant, qui élimine l'eau formée et "
                "déplace la réaction dans le sens de la formation du "
                "nitrobenzène",
            ],
            font_size=20,
            width=54,
        )
        roles.next_to(equation, DOWN, buff=0.45)

        groupe = VGroup(entete, equation, roles)
        _fit(groupe, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "L'équation s'écrit ainsi : le benzène réagit avec "
                "l'acide nitrique, en présence d'acide sulfurique et vers "
                "cinquante à soixante degrés, pour donner du "
                "nitrobenzène et de l'eau. L'acide sulfurique joue ici un "
                "double rôle : il sert de catalyseur, mais aussi d'agent "
                "déshydratant, qui élimine l'eau formée et déplace ainsi "
                "la réaction dans le sens de la formation du "
                "nitrobenzène."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(Write(equation))
            self.play(FadeIn(roles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple traité : du nitrobenzène à l'aniline + tableau récap --------
        entete2 = Text("Du nitrobenzène à l'aniline", font_size=24, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        chaine = MathTex(
            r"C_6H_5NO_2 \xrightarrow{\text{réduction}} C_6H_5NH_2 \ (\text{aniline})",
            font_size=28,
            color=ORANGE,
        )
        chaine.next_to(entete2, DOWN, buff=0.4)

        usages = Text(
            "L'aniline sert à fabriquer colorants et médicaments",
            font_size=20,
            color=WHITE,
        )
        usages.next_to(chaine, DOWN, buff=0.35)

        groupe2 = VGroup(entete2, chaine, usages)
        _fit(groupe2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Le nitrobenzène obtenu n'est pas une fin en soi : par "
                "réduction, il se transforme en aniline, C six H cinq "
                "N H deux, un composé industriellement majeur qui sert de "
                "matière première à la fabrication de nombreux colorants "
                "et médicaments."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(Write(chaine))
            self.play(FadeIn(usages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        entete3 = Text("Récapitulatif des 3 substitutions", font_size=22, color=YELLOW, weight="BOLD")
        entete3.next_to(titre, DOWN, buff=0.3)

        tableau = _tableau(
            ["Réaction", "Réactif", "Catalyseur", "Produit"],
            [
                ["Bromation", "Br2", "FeBr3", "C6H5Br"],
                ["Chloration", "Cl2", "FeCl3", "C6H5Cl"],
                ["Nitration", "HNO3", "H2SO4", "C6H5NO2"],
            ],
            col_widths=[2.6, 2.2, 2.4, 2.4],
            row_height=0.45,
            font_size=17,
        )
        tableau.next_to(entete3, DOWN, buff=0.3)
        groupe3 = VGroup(entete3, tableau)
        _fit(groupe3, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Récapitulons les trois substitutions étudiées : la "
                "bromation, avec le dibrome et le tribromure de fer, "
                "donne le bromobenzène ; la chloration, avec le "
                "dichlore et le trichlorure de fer, donne le "
                "chlorobenzène ; la nitration, avec l'acide nitrique et "
                "l'acide sulfurique, donne le nitrobenzène. Dans les "
                "trois cas, un hydrogène du cycle est remplacé, et le "
                "noyau aromatique est conservé."
            )
        ) as tracker:
            self.play(FadeIn(entete3))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe3))

        # --- À retenir : exemple résolu 2 (stœchiométrie 1:1) --------------------
        enonce_ex = Text(
            _wrap(
                "Exemple résolu : quelle masse de bromobenzène (M = 157 "
                "g/mol) peut-on obtenir à partir de 7,8 g de benzène "
                "(M = 78 g/mol) ?",
                width=50,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Terminons par un exemple résolu de stœchiométrie. Quelle "
                "masse de bromobenzène, de masse molaire cent "
                "cinquante-sept grammes par mole, peut-on obtenir à "
                "partir de sept virgule huit grammes de benzène, de masse "
                "molaire soixante-dix-huit grammes par mole ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        etape1 = MathTex(r"n(C_6H_6) = \dfrac{7{,}8}{78} = 0{,}10\ mol", font_size=28, color=WHITE)
        etape2 = MathTex(r"n(C_6H_5Br) = n(C_6H_6) = 0{,}10\ mol \quad (1{:}1)", font_size=28, color=WHITE)
        etape3 = MathTex(r"m(C_6H_5Br) = 0{,}10 \times 157 = 15{,}7\ g", font_size=28, color=YELLOW)
        etapes = VGroup(etape1, etape2, etape3).arrange(DOWN, buff=0.4)
        etapes.next_to(titre, DOWN, buff=0.6)
        _fit(etapes, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "On calcule d'abord la quantité de matière de benzène : "
                "sept virgule huit divisé par soixante-dix-huit, soit "
                "zéro virgule dix mole. Comme la réaction de bromation "
                "est stœchiométrique un pour un, on obtient la même "
                "quantité de matière de bromobenzène : zéro virgule dix "
                "mole. La masse correspondante vaut zéro virgule dix fois "
                "cent cinquante-sept, soit quinze virgule sept grammes de "
                "bromobenzène."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes), FadeOut(titre))
