"""
scenes/Chimie_OxydoreductionVoieSeche_03.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 03.

§ 2 (début). Le nombre d'oxydation (n.o.) : définition (charge fictive,
chiffres romains signés) et les 5 règles de calcul (corps pur simple,
ion monoatomique, molécule neutre, ion polyatomique, valeurs de référence
H et O avec exceptions). Exemple résolu 1 : n.o. du soufre dans H₂SO₄.
Source : 1ereC/Chimie.pdf, chapitre 13, pages 126-127.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
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
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=21, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class NombreOxydationDefinitionRegles(NotionScene):
    def construct(self):
        titre = scene_title("13.2 Le nombre d'oxydation : définition et règles")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : définition du n.o. --------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le NOMBRE D'OXYDATION (n.o.) d'un élément est la "
                    "charge fictive qu'il porterait si toutes ses liaisons "
                    "étaient rompues de façon purement ionique, l'électron "
                    "de liaison allant à l'atome le plus électronégatif. "
                    "Il se note en CHIFFRES ROMAINS SIGNÉS : par exemple "
                    "+II ou −I.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Introduisons un nouvel outil, indispensable pour "
                "analyser une oxydoréduction par voie sèche : le nombre "
                "d'oxydation, noté n point o point. Le nombre d'oxydation "
                "d'un élément est la charge fictive qu'il porterait si "
                "toutes ses liaisons étaient rompues de façon purement "
                "ionique, l'électron de chaque liaison étant attribué à "
                "l'atome le plus électronégatif. Il se note en chiffres "
                "romains signés, par exemple plus deux romain, ou moins un "
                "romain."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les 5 règles de calcul ----------------------------
        entete_regles = Text("Cinq règles de calcul", font_size=23, color=YELLOW, weight="BOLD")
        entete_regles.next_to(titre, DOWN, buff=0.35)

        regles = _bullets(
            [
                "1. Corps pur simple (atome seul ou molécule "
                "homoatomique) : n.o. = 0. Ex : Cu, Fe, O₂, Cl₂.",
                "2. Ion monoatomique : n.o. = charge de l'ion. "
                "Ex : Mg²⁺ → n.o. = +II ; Cl⁻ → n.o. = −I.",
                "3. Molécule neutre : la SOMME des n.o. de tous les "
                "atomes est égale à 0.",
                "4. Ion polyatomique : la SOMME des n.o. de tous les "
                "atomes est égale à la CHARGE de l'ion.",
                "5. Valeurs de référence : H → +I (sauf hydrures "
                "métalliques : −I) ; O → −II (sauf peroxydes : −I).",
            ],
            width=54,
        )
        regles.next_to(entete_regles, DOWN, buff=0.35)
        groupe_regles = VGroup(entete_regles, regles)
        _fit(groupe_regles, titre.get_bottom()[1] - 0.15)
        groupe_regles.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Le nombre d'oxydation se calcule grâce à cinq règles. "
                "Première règle : dans un corps pur simple, un atome seul "
                "ou une molécule formée d'un seul type d'atome, le n.o. "
                "vaut zéro, comme pour le cuivre, le fer, le dioxygène ou "
                "le dichlore. Deuxième règle : pour un ion monoatomique, "
                "le n.o. est égal à la charge de l'ion, plus deux romain "
                "pour Mg deux plus, moins un romain pour Cl moins. "
                "Troisième règle : dans une molécule neutre, la somme des "
                "n.o. de tous les atomes vaut zéro. Quatrième règle : dans "
                "un ion polyatomique, cette somme vaut la charge de l'ion. "
                "Cinquième règle : deux valeurs de référence à connaître "
                "par cœur, l'hydrogène vaut plus un romain, sauf dans les "
                "hydrures métalliques où il vaut moins un romain, et "
                "l'oxygène vaut moins deux romain, sauf dans les peroxydes "
                "où il vaut moins un romain."
            )
        ) as tracker:
            self.play(FadeIn(entete_regles))
            self.play(FadeIn(regles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_regles))

        # --- Exemple traité : n.o. du soufre dans H2SO4 ------------------------
        formule = MathTex(r"H_2SO_4", font_size=32, color=WHITE)
        etape1 = Text("2 atomes H (+I chacun) + 1 atome S (n.o.(S)) + 4 atomes O (−II chacun) = 0", font_size=19, color=WHITE)
        etape2 = Text("2 × (+1) + n.o.(S) + 4 × (−2) = 0", font_size=21, color=WHITE)
        etape3 = Text("2 + n.o.(S) − 8 = 0  →  n.o.(S) = +6", font_size=21, color=WHITE)
        resultat = MathTex(r"n.o.(S) = +VI", font_size=28, color=ORANGE)

        contenu_exemple = VGroup(formule, etape1, etape2, etape3, resultat).arrange(DOWN, buff=0.3)
        exemple_groupe = example_box(contenu_exemple, box_width=12.6)
        exemple_groupe.next_to(titre, DOWN, buff=0.35)
        _fit(exemple_groupe, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Mettons ces règles en pratique. Exemple résolu : "
                "déterminons le nombre d'oxydation du soufre dans l'acide "
                "sulfurique, H deux S O quatre. La molécule est neutre, "
                "donc la somme des n.o. de ses six atomes vaut zéro : deux "
                "atomes d'hydrogène, à plus un chacun, plus le n.o. du "
                "soufre, plus quatre atomes d'oxygène, à moins deux "
                "chacun. Cela donne : deux, plus n point o de S, moins "
                "huit, égale zéro. On isole le n.o. du soufre : il vaut "
                "plus six, soit n.o. de S égale plus six romain."
            )
        ) as tracker:
            self.play(FadeIn(exemple_groupe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_groupe))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre le NOMBRE D'OXYDATION (chiffre "
                    "romain signé, ex : +VI) avec la CHARGE RÉELLE d'un "
                    "ion (chiffre arabe, ex : 2+). Le soufre de H₂SO₄ "
                    "n'est pas un ion S⁶⁺ isolé !",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : il ne faut pas confondre "
                "le nombre d'oxydation, noté en chiffres romains signés, "
                "avec la charge réelle d'un ion, notée en chiffres "
                "arabes. Le soufre de l'acide sulfurique n'est pas un ion "
                "S six plus isolé : c'est une charge purement fictive, "
                "utile pour analyser les échanges d'électrons."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
