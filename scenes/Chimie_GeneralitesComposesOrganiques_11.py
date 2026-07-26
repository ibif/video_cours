"""
scenes/Chimie_GeneralitesComposesOrganiques_11.py — Chapitre 1 (1ereC, Chimie), scène 11.

§ 7, 8 Les principales fonctions organiques (tableau des 6 familles) +
bases de la nomenclature (radicaux alkyles, 3 règles) + Exemple résolu 4
(3-méthylhexane). Source : 1ereC/Chimie.pdf, pages 10-12.
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
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class FonctionsEtNomenclature(NotionScene):
    def construct(self):
        titre = scene_title("7-8. Fonctions organiques et nomenclature")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition de la fonction organique -----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une fonction organique est un groupement d'atomes "
                    "(groupe caractéristique) qui confère à la molécule "
                    "des propriétés chimiques semblables. L'ensemble des "
                    "composés possédant la même fonction constitue une "
                    "famille.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une fonction organique est un groupement d'atomes, appelé "
                "groupe caractéristique, qui confère à la molécule des "
                "propriétés chimiques semblables. L'ensemble des composés "
                "possédant la même fonction constitue une famille."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : tableau des 6 familles -----------------
        entete = Text("Les six principales familles", font_size=23, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        familles = VGroup(
            Text("Alcool : –OH, R–OH (éthanol CH₃-CH₂-OH)", font_size=18),
            Text("Aldéhyde : –CHO, R–CHO (éthanal CH₃-CHO)", font_size=18),
            Text("Cétone : –CO–, R–CO–R' (propanone CH₃-CO-CH₃)", font_size=18),
            Text("Acide carboxylique : –COOH, R–COOH (acide éthanoïque CH₃-COOH)", font_size=18),
            Text("Ester : –COO–, R–COO–R' (éthanoate de méthyle CH₃-COO-CH₃)", font_size=18),
            Text("Amine : –NH₂, R–NH₂ (méthanamine CH₃-NH₂)", font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        familles.next_to(entete, DOWN, buff=0.35)
        _fit(familles, entete.get_bottom()[1] - 0.4)

        groupe_familles = VGroup(entete, familles)

        with self.voiceover(
            text=(
                "Voici les six principales familles à connaître. L'alcool, "
                "avec le groupe hydroxyle, comme l'éthanol. L'aldéhyde, "
                "avec le carbonyle en bout de chaîne, comme l'éthanal. La "
                "cétone, avec le carbonyle à l'intérieur de la chaîne, "
                "comme la propanone. L'acide carboxylique, avec le groupe "
                "carboxyle, comme l'acide éthanoïque. L'ester, comme "
                "l'éthanoate de méthyle. Et l'amine, avec le groupe amino, "
                "comme la méthanamine. On note R, et R prime, un groupe "
                "alkyle ou un atome d'hydrogène."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(familles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_familles))

        # --- Exemple traité : radicaux alkyles + règles de nomenclature --------
        entete2 = Text("Radicaux alkyles et règles de nomenclature", font_size=21, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        radicaux = VGroup(
            Text("méthyle CH₃–  •  éthyle C₂H₅–  •  propyle C₃H₇–  •  butyle C₄H₉–", font_size=18, color=WHITE),
        )
        radicaux.next_to(entete2, DOWN, buff=0.3)

        regles = VGroup(
            Text("1. Chaîne principale : la chaîne linéaire la plus longue (attention, pas forcément horizontale !)", font_size=17),
            Text("2. Numérotation : indices les plus petits possibles pour les ramifications", font_size=17),
            Text("3. Nom = indice(s) + nom du/des radical(aux) + nom de la chaîne principale (di-, tri- ; ordre alphabétique)", font_size=17),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        regles.next_to(radicaux, DOWN, buff=0.35)

        groupe_regles = VGroup(entete2, radicaux, regles)
        _fit(groupe_regles, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Un radical alkyle s'obtient en retirant un atome "
                "d'hydrogène à un alcane : méthyle, éthyle, propyle, "
                "butyle. Trois règles gouvernent la nomenclature des "
                "hydrocarbures ramifiés. Un, on cherche la chaîne "
                "carbonée linéaire la plus longue : c'est la chaîne "
                "principale — attention, elle n'est pas toujours celle "
                "écrite horizontalement ! Deux, on numérote les carbones "
                "dans le sens qui donne aux ramifications les indices les "
                "plus petits possibles. Trois, le nom s'écrit : indice de "
                "position, tiret, nom du radical, puis nom de la chaîne "
                "principale, avec les préfixes di, tri, tétra si un même "
                "radical se répète, et l'ordre alphabétique si les "
                "radicaux sont différents."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(radicaux))
            self.play(FadeIn(regles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_regles))

        # --- À retenir : exemple résolu 4 (3-méthylhexane) ----------------------
        exemple = example_box(
            VGroup(
                MathTex(r"CH_3-CH(C_2H_5)-CH_2-CH_2-CH_3", font_size=26),
                Text(
                    _wrap(
                        "La chaîne horizontale compte 5 carbones, mais en "
                        "« montant » dans le groupe éthyle, on trouve une "
                        "chaîne de 6 carbones : c'est un hexane. En "
                        "numérotant depuis l'extrémité la plus proche de "
                        "la ramification, le méthyle porte le numéro 3.",
                        width=46,
                    ),
                    font_size=21,
                ),
                MathTex(r"\text{Nom : } 3\text{-méthylhexane}", font_size=28, color=YELLOW),
            ).arrange(DOWN, buff=0.32),
            box_width=11.5,
        )
        exemple.next_to(titre, DOWN, buff=0.4)
        _fit(exemple, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : nommons le composé CH3, CH parenthèse C2 "
                "H5 fermer la parenthèse, CH2, CH2, CH3. La chaîne écrite "
                "horizontalement compte cinq atomes de carbone, mais en "
                "montant dans le groupe éthyle, on trouve une chaîne de "
                "six atomes : c'est donc un hexane. En numérotant depuis "
                "l'extrémité la plus proche de la ramification, le groupe "
                "méthyle porte le numéro trois, et non quatre. Le nom est "
                "donc trois-méthylhexane."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
