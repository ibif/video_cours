"""
scenes/Chimie_Alcanes_03.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 03.

§ 2.3 Chaînes carbonées (linéaire vs ramifiée, exemples butane /
2-méthylpropane) + § 3.1 Nomenclature des alcanes linéaires (tableau des
10 premiers alcanes : préfixe, nom, formule brute).
Source : 1ereC/Chimie.pdf, pages 16-17.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _chaine_lineaire(n=4):
    atomes = VGroup(*[MathTex("C", font_size=28, color=BLUE) for _ in range(n)])
    atomes.arrange(RIGHT, buff=0.55)
    liaisons = VGroup(
        *[Line(atomes[i].get_right(), atomes[i + 1].get_left(), color=WHITE, stroke_width=3) for i in range(n - 1)]
    )
    return VGroup(liaisons, atomes)


def _chaine_ramifiee():
    principale = VGroup(*[MathTex("C", font_size=28, color=BLUE) for _ in range(3)])
    principale.arrange(RIGHT, buff=0.55)
    branche = MathTex("C", font_size=28, color=BLUE)
    branche.next_to(principale[1], UP, buff=0.45)
    liaisons = VGroup(
        Line(principale[0].get_right(), principale[1].get_left(), color=WHITE, stroke_width=3),
        Line(principale[1].get_right(), principale[2].get_left(), color=WHITE, stroke_width=3),
        Line(principale[1].get_top(), branche.get_bottom(), color=WHITE, stroke_width=3),
    )
    return VGroup(liaisons, principale, branche)


class ChainesEtNomenclatureLineaire(NotionScene):
    def construct(self):
        titre = scene_title("2. Les chaînes carbonées et leur nomenclature")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition de la chaîne carbonée --------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "On appelle chaîne carbonée (ou squelette carboné) "
                    "l'enchaînement des atomes de carbone qui constituent "
                    "une molécule organique.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On appelle chaîne carbonée, ou squelette carboné, "
                "l'enchaînement des atomes de carbone qui constituent une "
                "molécule organique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : chaîne linéaire vs chaîne ramifiée ------------------
        entete_chaines = Text("Chaîne linéaire ou chaîne ramifiée ?", font_size=24, color=YELLOW, weight="BOLD")
        entete_chaines.next_to(titre, DOWN, buff=0.4)

        bloc_lin = VGroup(
            _chaine_lineaire(4),
            MathTex(r"CH_3-CH_2-CH_2-CH_3", font_size=22, color=WHITE),
            Text("linéaire (butane)", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.25)

        bloc_ram = VGroup(
            _chaine_ramifiee(),
            MathTex(r"CH_3-CH(CH_3)-CH_3", font_size=22, color=WHITE),
            Text("ramifiée (2-méthylpropane)", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.25)

        deux_chaines = VGroup(bloc_lin, bloc_ram).arrange(RIGHT, buff=1.4, aligned_edge=DOWN)
        deux_chaines.next_to(entete_chaines, DOWN, buff=0.5)
        _fit(deux_chaines, entete_chaines.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Une chaîne carbonée est dite linéaire si les atomes de "
                "carbone sont liés les uns à la suite des autres, sans "
                "former de boucle : c'est le cas du butane, C-H-3, "
                "C-H-2, C-H-2, C-H-3. Elle est dite ramifiée si au moins "
                "un atome de carbone, appelé carbone ramifié, est lié à "
                "trois ou quatre autres atomes de carbone : c'est le cas "
                "du deux-méthylpropane, dont un carbone central porte "
                "trois groupes méthyle."
            )
        ) as tracker:
            self.play(FadeIn(entete_chaines))
            self.play(FadeIn(bloc_lin))
            self.play(FadeIn(bloc_ram))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_chaines), FadeOut(deux_chaines))

        # --- Exemple traité : tableau de nomenclature des 10 premiers alcanes --
        entete_tab = Text("Nomenclature des alcanes linéaires", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["1", "méth", "méthane", "CH₄"],
            ["2", "éth", "éthane", "C₂H₆"],
            ["3", "prop", "propane", "C₃H₈"],
            ["4", "but", "butane", "C₄H₁₀"],
            ["5", "pent", "pentane", "C₅H₁₂"],
            ["6", "hex", "hexane", "C₆H₁₄"],
            ["7", "hept", "heptane", "C₇H₁₆"],
            ["8", "oct", "octane", "C₈H₁₈"],
            ["9", "non", "nonane", "C₉H₂₀"],
            ["10", "déc", "décane", "C₁₀H₂₂"],
        ]
        col_labels = ["n", "préfixe", "nom", "formule brute"]

        table = Table(
            rows,
            col_labels=[Text(c, font_size=17, weight="BOLD") for c in col_labels],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 16},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.22,
            h_buff=0.35,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)

        table.next_to(entete_tab, DOWN, buff=0.3)

        # Garde-fou d'auto-scale (voir SVT_FonctionsGonades_09 / TectoniquePlaques_07)
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = table.get_top()[1] - _bas_visible
        if table.height > _hauteur_dispo:
            table.scale(_hauteur_dispo / table.height, about_point=table.get_top())
        _largeur_dispo = config.frame_width - 0.6
        if table.width > _largeur_dispo:
            table.scale(_largeur_dispo / table.width, about_point=table.get_top())
        table.next_to(entete_tab, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Les quatre premiers alcanes ont un nom consacré par "
                "l'usage : méthane, éthane, propane, butane. Pour les "
                "suivants, le nom s'obtient par une règle simple : préfixe "
                "indiquant le nombre d'atomes de carbone, plus la "
                "terminaison ane. Voici le tableau des dix premiers "
                "alcanes linéaires, du méthane, un seul carbone, au "
                "décane, dix carbones, avec leur préfixe et leur formule "
                "brute."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table))

        # --- À retenir : la règle générale de nomenclature ----------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Nom d'un alcane linéaire = préfixe indiquant le "
                    "nombre d'atomes de carbone + terminaison « ane » "
                    "(sauf les 4 premiers : méthane, éthane, propane, "
                    "butane, consacrés par l'usage).",
                    width=48,
                ),
                font_size=24,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la règle générale : le nom d'un alcane linéaire "
                "s'obtient en ajoutant la terminaison ane au préfixe "
                "indiquant le nombre d'atomes de carbone, à l'exception "
                "des quatre premiers, méthane, éthane, propane et butane, "
                "consacrés par l'usage."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : « linéaire » ne veut pas dire « en ligne droite » -
        piege = warning_box(
            Text(
                _wrap(
                    "« Chaîne linéaire » signifie non ramifiée, pas « en "
                    "ligne droite » : le carbone restant tétraédrique, la "
                    "molécule adopte en réalité une forme en zigzag dans "
                    "l'espace, même pour un alcane dit linéaire.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : chaîne linéaire signifie "
                "seulement chaîne non ramifiée, pas chaîne en ligne "
                "droite. Le carbone restant tétraédrique, avec ses angles "
                "de cent neuf degrés, la molécule adopte en réalité une "
                "forme en zigzag dans l'espace, même pour un alcane dit "
                "linéaire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
