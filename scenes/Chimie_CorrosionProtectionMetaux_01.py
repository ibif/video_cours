"""
scenes/Chimie_CorrosionProtectionMetaux_01.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 01.

§ 1. La corrosion : constat et définition. Constat visuel (clou rouillé,
portail, tôle, carrosserie), definition_box de la corrosion (oxydation par
l'air humide, lente, voie humide, température ordinaire), remarques
(Fe → Fe²⁺ → Fe³⁺ avec cession d'électrons, distinction voie humide / voie
sèche, tous les métaux ne se corrodent pas de la même façon). Tableau des
produits de corrosion des métaux usuels (Fe, Zn, Al, Cu, Cr).
Source : 1ereC/Chimie.pdf, chapitre 15, pages 144-145.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
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


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


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


class CorrosionConstatDefinition(NotionScene):
    def construct(self):
        titre = scene_title("15.1 La corrosion : constat et définition")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : constat -----------------------------------------------
        constat = Text(
            _wrap(
                "Un clou oublié dehors, un portail en fer, une tôle de "
                "toiture, la carrosserie d'un véhicule : tous finissent "
                "par se couvrir d'une couche brun-rouge. Ce phénomène "
                "quotidien a un nom : la corrosion.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        constat.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un clou oublié dehors, un portail en fer, une tôle de "
                "toiture, la carrosserie d'un véhicule : tous finissent "
                "tôt ou tard par se couvrir d'une couche brun-rouge "
                "friable. Ce phénomène très quotidien porte un nom précis "
                "en chimie : la corrosion."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(constat))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(constat))

        # --- Raisonnement : définition ---------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La corrosion est l'oxydation lente d'un métal par "
                    "l'air humide (voie humide), à température ordinaire, "
                    "qui le transforme progressivement en un composé "
                    "métallique (oxyde, hydroxyde…).",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On définit la corrosion comme l'oxydation lente d'un "
                "métal par l'air humide : on parle de corrosion par voie "
                "humide. Elle se produit à température ordinaire, sans "
                "flamme ni combustion, et transforme progressivement le "
                "métal en un composé métallique, un oxyde ou un "
                "hydroxyde par exemple."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : le mécanisme électronique du fer ----------------
        entete_meca = Text("Le fer cède ses électrons", font_size=23, color=YELLOW, weight="BOLD")
        entete_meca.next_to(titre, DOWN, buff=0.4)

        equation = MathTex(
            r"Fe \;\longrightarrow\; Fe^{2+} \;\longrightarrow\; Fe^{3+}",
            font_size=30,
            color=WHITE,
        )
        equation.next_to(entete_meca, DOWN, buff=0.4)

        note = Text(
            "à chaque étape, le fer perd des électrons : c'est une oxydation",
            font_size=19,
            color=WHITE,
        )
        note.next_to(equation, DOWN, buff=0.35)

        groupe_meca = VGroup(entete_meca, equation, note)

        with self.voiceover(
            text=(
                "Chimiquement, le métal cède des électrons : le fer "
                "métallique se transforme d'abord en ion fer deux plus, "
                "puis en ion fer trois plus. À chaque étape, le fer perd "
                "des électrons : c'est bien une oxydation, au sens de "
                "l'oxydoréduction, et non une simple réaction avec une "
                "flamme."
            )
        ) as tracker:
            self.play(FadeIn(entete_meca))
            self.play(Write(equation))
            self.play(FadeIn(note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_meca))

        # --- Remarque : voie humide / voie sèche -------------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre voie humide (corrosion, lente, à "
                    "froid, nécessite eau + air) et voie sèche "
                    "(combustion, rapide, avec flamme, ex : fer qui brûle "
                    "dans O2 pur). Ce chapitre traite uniquement la voie "
                    "humide.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        remarque.next_to(titre, DOWN, buff=0.45)
        _fit(remarque, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Attention à une distinction importante : il ne faut pas "
                "confondre la voie humide, celle de la corrosion, lente "
                "et à froid, avec la voie sèche, celle de la combustion, "
                "rapide et avec flamme, comme le fer qui brûle dans le "
                "dioxygène pur. Ce chapitre traite uniquement de la "
                "corrosion par voie humide."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- À retenir : tableau des produits de corrosion ---------------------
        entete_tab = Text("Tous les métaux ne se corrodent pas pareil", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau(
            ["Métal", "Produit de corrosion"],
            [
                ["Fer (Fe)", "rouille, non protectrice"],
                ["Zinc (Zn)", "rouille blanche, protectrice"],
                ["Aluminium (Al)", "alumine, protectrice"],
                ["Cuivre (Cu)", "vert-de-gris"],
                ["Chrome (Cr)", "invisible, protecteur"],
            ],
            col_widths=[3.6, 5.2],
            row_height=0.5,
            font_size=18,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.3)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Retenons enfin que tous les métaux ne se corrodent pas "
                "de la même façon. Le fer donne une rouille non "
                "protectrice ; le zinc donne une rouille blanche qui, "
                "elle, protège le métal ; l'aluminium se recouvre "
                "d'alumine protectrice ; le cuivre se couvre de "
                "vert-de-gris ; et le chrome forme une couche d'oxyde "
                "invisible mais protectrice. Cette différence sera "
                "essentielle pour comprendre les moyens de protection."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab), FadeOut(titre))
