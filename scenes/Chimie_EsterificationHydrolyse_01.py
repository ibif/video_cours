"""
scenes/Chimie_EsterificationHydrolyse_01.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 01.

§ Les esters : structure (groupe -COO-, formule R-COO-R', R' jamais H),
definition_box, tableau d'exemples avec origine acide + alcool et arôme.
method_box nomenclature en 2 parties (acide → oate, alcool → yle),
occurrence naturelle (odeurs de fruits/fleurs), corps gras = triesters du
glycérol.
Source : 1ereC/Chimie.pdf, chapitre 8, pages 75-76.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class EstersStructureNomenclatureOccurrence(NotionScene):
    def construct(self):
        titre = scene_title("1. Les esters : structure, nomenclature, occurrence")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : le groupe ester -------------------------------------------
        enonce = Text(
            _wrap(
                "Vous connaissez déjà les acides carboxyliques et les "
                "alcools. En les faisant réagir ensemble, on obtient une "
                "nouvelle famille de composés très présente dans la "
                "nature comme dans l'industrie : les esters.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Vous connaissez déjà les acides carboxyliques et les "
                "alcools. En les faisant réagir ensemble, on obtient une "
                "nouvelle famille de composés organiques, très présente "
                "dans la nature comme dans l'industrie : les esters. "
                "Découvrons leur structure."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : le groupe fonctionnel -COO- --------------------------
        entete = Text("Le groupe fonctionnel ester", font_size=26, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        formule = MathTex(r"R-C(=O)-O-R'", font_size=52, color=WHITE)
        formule_simple = MathTex(r"R-COO-R'", font_size=44, color=WHITE)
        precision = Text(
            _wrap(
                "R et R' sont des groupes carbonés (chaînes hydrocarbonées) : "
                "R' ne peut JAMAIS être un simple atome d'hydrogène, sinon on "
                "retrouverait un acide carboxylique.",
                width=48,
            ),
            font_size=22,
            color=WHITE,
        )
        bloc = VGroup(formule, formule_simple, precision).arrange(DOWN, buff=0.35)
        bloc.next_to(entete, DOWN, buff=0.4)
        groupe = VGroup(entete, bloc)
        _fit(groupe, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Un ester est caractérisé par le groupe fonctionnel "
                "carbonyle-oxygène, que l'on note de façon condensée "
                "R-C-O-O-R', ou plus simplement R-C-O-O-R'. R et R' "
                "désignent des groupes carbonés : R' ne peut jamais être "
                "un simple atome d'hydrogène, sinon on retrouverait la "
                "formule d'un acide carboxylique, et non d'un ester."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(Write(formule))
            self.play(Write(formule_simple))
            self.play(FadeIn(precision))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple traité : tableau d'esters courants ---------------------------
        entete_tab = Text("Quelques esters courants", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.3)

        rows = [
            ["éthanoate d'isoamyle", "ac. éthanoïque", "alcool isoamylique", "banane"],
            ["éthanoate d'octyle", "ac. éthanoïque", "octan-1-ol", "orange"],
            ["butanoate de méthyle", "ac. butanoïque", "méthanol", "pomme"],
            ["butanoate d'éthyle", "ac. butanoïque", "éthanol", "ananas"],
        ]
        col_labels = ["ester", "acide parent", "alcool parent", "arôme"]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=16, weight="BOLD") for c in col_labels],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 15},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.2,
            h_buff=0.3,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(entete_tab, DOWN, buff=0.3)

        _largeur_dispo = config.frame_width - 0.6
        if table.width > _largeur_dispo:
            table.scale(_largeur_dispo / table.width, about_point=table.get_top())
        table.next_to(entete_tab, DOWN, buff=0.3)

        groupe_tab = VGroup(entete_tab, table)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici quatre esters courants, avec l'acide et l'alcool "
                "dont ils dérivent, et l'arôme naturel qu'ils évoquent : "
                "éthanoate d'isoamyle pour la banane, éthanoate d'octyle "
                "pour l'orange, butanoate de méthyle pour la pomme, et "
                "butanoate d'éthyle pour l'ananas. Ce sont ces molécules "
                "qui donnent leur parfum caractéristique à de nombreux "
                "fruits et fleurs."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- À retenir : definition_box « ester » ----------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Un ester est un composé organique de formule "
                        "générale R-COO-R' (R' jamais un atome d'hydrogène), "
                        "obtenu formellement par réaction d'un acide "
                        "carboxylique R-COOH avec un alcool R'-OH.",
                        width=48,
                    ),
                    font_size=23,
                ),
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons donc : un ester est un composé organique de "
                "formule générale R-C-O-O-R', où R' n'est jamais un atome "
                "d'hydrogène, obtenu formellement par réaction d'un acide "
                "carboxylique R-C-O-O-H avec un alcool R'-O-H. Nous "
                "verrons dans quelques instants comment écrire cette "
                "réaction."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Méthode : nomenclature + occurrence naturelle -------------------------
        methode = method_box(
            VGroup(
                Text(
                    "Nommer un ester en 2 parties :",
                    font_size=23,
                    weight="BOLD",
                ),
                Text(
                    _wrap(
                        "1) partie ACIDE : le suffixe -oïque de l'acide "
                        "devient -oate ; 2) partie ALCOOL : le nom de "
                        "l'alcool devient un groupe en -yle, introduit par "
                        "« de ». Exemple : acide éthanoïque + éthanol → "
                        "éthanoate d'éthyle.",
                        width=48,
                    ),
                    font_size=21,
                ),
                Text(
                    _wrap(
                        "Occurrence naturelle : les esters sont responsables "
                        "des odeurs de nombreux fruits et fleurs. Les corps "
                        "gras (huiles, graisses) sont des triesters du "
                        "glycérol avec des acides gras.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.4)
        _fit(methode, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Méthode pour nommer un ester : la nomenclature se "
                "construit en deux parties. La partie issue de l'acide "
                "voit son suffixe -oïque devenir -oate. La partie issue "
                "de l'alcool devient un groupe en -yle, introduit par "
                "« de ». Ainsi, acide éthanoïque et éthanol donnent "
                "éthanoate d'éthyle. Dans la nature, les esters sont "
                "responsables de nombreuses odeurs de fruits et de "
                "fleurs. Et les corps gras, huiles et graisses, sont en "
                "réalité des triesters du glycérol avec des acides gras : "
                "nous y reviendrons lors de l'étude de la saponification."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode), FadeOut(titre))
