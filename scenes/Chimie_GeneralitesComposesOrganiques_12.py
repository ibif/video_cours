"""
scenes/Chimie_GeneralitesComposesOrganiques_12.py — Chapitre 1 (1ereC, Chimie), scène 12.

Méthodes et astuces (3 méthodes) + 3 pièges à éviter + L'ESSENTIEL DU
CHAPITRE (clôture). Source : 1ereC/Chimie.pdf, pages 12-13.
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
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
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


class MethodesPiegesEtEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("Méthodes, astuces et l'essentiel du chapitre")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : trois méthodes à automatiser -------------------------------
        intro = Text(
            _wrap(
                "Terminons ce chapitre par trois méthodes à automatiser, "
                "trois pièges classiques à éviter, puis l'essentiel à "
                "retenir.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce premier chapitre de chimie organique par "
                "trois méthodes à automatiser, trois pièges classiques à "
                "éviter, puis l'essentiel à retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : méthode 1 (formule brute) -------------
        methode1 = method_box(
            Text(
                _wrap(
                    "Déterminer la formule brute : 1) calculer m(C) et "
                    "m(H) à partir de m(CO₂) et m(H₂O), puis %C et %H ; "
                    "2) obtenir %O par différence (la somme doit faire "
                    "100 : c'est une vérification) ; 3) appliquer "
                    "12x/%C = y/%H = 16z/%O = M/100 et arrondir à "
                    "l'entier le plus proche ; 4) si M manque mais la "
                    "famille est connue, exploiter y/x = (%H/1)/(%C/12).",
                    width=48,
                ),
                font_size=21,
            ),
        )
        methode1.next_to(titre, DOWN, buff=0.4)
        _fit(methode1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Première méthode : déterminer la formule brute d'un "
                "composé organique. On calcule d'abord les masses de "
                "carbone et d'hydrogène à partir des masses de CO2 et "
                "d'eau, puis les pourcentages. On obtient le pourcentage "
                "d'oxygène par différence — la somme des trois doit faire "
                "cent, c'est un excellent moyen de vérification. On "
                "applique ensuite la relation fondamentale, en arrondissant "
                "à l'entier le plus proche. Et si la masse molaire manque "
                "mais que la famille est connue, on exploite le rapport y "
                "sur x."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : dénombrer les isomères + Méthode 3 : équilibrer -------
        methode2 = method_box(
            Text(
                _wrap(
                    "Dénombrer les isomères sans en oublier : procéder "
                    "méthodiquement — écrire la chaîne linéaire la plus "
                    "longue, puis la raccourcir d'un carbone en plaçant le "
                    "méthyle à toutes les positions non équivalentes, puis "
                    "raccourcir encore, puis faire varier la position du "
                    "groupe caractéristique, puis la fonction. Toujours "
                    "vérifier que deux formules ne sont pas le même corps.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        methode2.next_to(titre, DOWN, buff=0.4)
        _fit(methode2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : dénombrer les isomères sans en "
                "oublier. On procède méthodiquement : on écrit la chaîne "
                "linéaire la plus longue, puis on la raccourcit d'un "
                "carbone en plaçant le méthyle à toutes les positions non "
                "équivalentes, puis on raccourcit encore en plaçant deux "
                "méthyles ou un éthyle, puis on fait varier la position du "
                "groupe caractéristique, puis la fonction. On vérifie "
                "toujours que deux formules écrites ne sont pas, en fait, "
                "le même corps lu dans l'autre sens."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            VGroup(
                Text(
                    _wrap(
                        "Équilibrer une équation de combustion complète : "
                        "pour CₓHᵧOᵤ, on équilibre dans l'ordre C, puis H, "
                        "puis O.",
                        width=44,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"C_xH_yO_z + \left(x+\dfrac{y}{4}-\dfrac{z}{2}\right)O_2 \rightarrow xCO_2 + \dfrac{y}{2}H_2O",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=11.5,
        )
        methode3.next_to(titre, DOWN, buff=0.4)
        _fit(methode3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième méthode : équilibrer une équation de combustion "
                "complète. Pour un composé C indice x H indice y O indice "
                "z, l'équation s'écrit directement avec, devant le "
                "dioxygène, le coefficient x plus y sur quatre moins z sur "
                "deux. On équilibre toujours dans le même ordre : le "
                "carbone, puis l'hydrogène, puis l'oxygène."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Exemple traité / pièges à éviter -----------------------------------
        pieges = warning_box(
            _bullets(
                [
                    "Deux écritures différentes ne font pas nécessairement "
                    "deux isomères : CH₃-CH₂-CH(CH₃)-CH₂-CH₃ et "
                    "CH₃-CH₂-CH(CH₂CH₃)-CH₃ sont le même corps, le "
                    "3-méthylpentane.",
                    "En nomenclature, ne pas se fier à la chaîne écrite "
                    "horizontalement : chercher systématiquement la "
                    "chaîne la plus longue, y compris en « montant » dans "
                    "les branches.",
                    "Dans les calculs de pourcentages massiques, ne pas "
                    "oublier le facteur 2 pour l'hydrogène : m(H) = "
                    "(2/18)×m(H₂O), pas (1/18).",
                ],
                font_size=20,
                width=48,
            ),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)
        _fit(pieges, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Trois pièges classiques à éviter. Premièrement, deux "
                "écritures différentes ne font pas nécessairement deux "
                "isomères : seule la formule développée, c'est-à-dire "
                "l'enchaînement réel des atomes, permet de trancher — deux "
                "écritures peuvent désigner le même corps, comme ici deux "
                "façons d'écrire le trois-méthylpentane. Deuxièmement, en "
                "nomenclature, ne jamais se fier à la chaîne écrite "
                "horizontalement : il faut chercher systématiquement la "
                "chaîne la plus longue, y compris en montant dans les "
                "branches. Troisièmement, dans les calculs de "
                "pourcentages massiques, ne pas oublier le facteur deux "
                "pour l'hydrogène."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) ----------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "La chimie organique est la chimie des composés du "
                    "carbone (élément toujours présent, avec H, souvent "
                    "O, parfois N).",
                    "Analyse qualitative : CO₂ et H₂O révèlent C et H ; "
                    "NH₃ révèle N ; l'oxygène se déduit par différence.",
                    "Analyse quantitative : %C, %H par pesée de CO₂/H₂O, "
                    "%O par différence, puis formule brute via "
                    "12x/%C = y/%H = 16z/%O = M/100.",
                    "Une molécule s'écrit en formule brute, développée, "
                    "semi-développée ou topologique.",
                    "Chaînes linéaires, ramifiées ou cycliques ; "
                    "isomérie de chaîne, de position ou de fonction.",
                    "Six familles clés : alcool, aldéhyde, cétone, acide "
                    "carboxylique, ester, amine ; nomenclature en 3 règles.",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)
        _fit(essentiel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici l'essentiel à retenir de ce chapitre. La chimie "
                "organique est la chimie des composés du carbone. "
                "L'analyse qualitative révèle le carbone et l'hydrogène "
                "par la formation de CO2 et d'eau, l'azote par le "
                "dégagement d'ammoniac, et l'oxygène se déduit par "
                "différence. L'analyse quantitative permet de calculer les "
                "pourcentages massiques, puis d'en déduire la formule "
                "brute grâce à la relation fondamentale. Une molécule peut "
                "s'écrire de quatre façons : brute, développée, "
                "semi-développée ou topologique. Les chaînes carbonées "
                "sont linéaires, ramifiées ou cycliques, et l'isomérie se "
                "décline en trois types : chaîne, position, fonction. "
                "Enfin, six familles de fonctions organiques sont à "
                "connaître, avec les bases de la nomenclature."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
