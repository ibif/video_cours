"""
scenes/Maths_Denombrement_04.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 04.

§ Principe multiplicatif : théorème et justification (tableau à double
entrée, arbre de choix), figure de l'arbre. Exemple résolu 2
(immatriculation de véhicules, 9999×26×10). Méthode pour reconnaître un
produit cartésien (choix successifs indépendants).
Source : 1ereC/Maths.pdf, chapitre 6, pages 69-70.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    ORIGIN,
    WHITE,
    YELLOW,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _arbre_choix() -> VGroup:
    """Arbre à 2 niveaux : 3 choix puis 2 choix (illustre 3×2=6)."""
    racine = Dot(ORIGIN, radius=0.05)
    niveau1 = [racine.get_center() + DOWN * 0.8 + RIGHT * dx for dx in (-2.0, 0, 2.0)]
    branches1 = VGroup(*[Line(racine.get_center(), p, color=WHITE) for p in niveau1])
    noeuds1 = VGroup(*[Dot(p, radius=0.05) for p in niveau1])
    labels1 = VGroup(
        *[
            MathTex(lab, font_size=20).next_to(p, UP, buff=0.08)
            for p, lab in zip(niveau1, ["c_1", "c_2", "c_3"])
        ]
    )

    niveau2 = []
    branches2 = VGroup()
    labels2 = VGroup()
    for p in niveau1:
        feuilles = [p + DOWN * 0.8 + RIGHT * dx for dx in (-0.35, 0.35)]
        for f, lab in zip(feuilles, ["d_1", "d_2"]):
            branches2.add(Line(p, f, color=WHITE))
            niveau2.append(f)
            labels2.add(MathTex(lab, font_size=18).next_to(f, DOWN, buff=0.08))
    noeuds2 = VGroup(*[Dot(p, radius=0.04) for p in niveau2])

    return VGroup(branches1, noeuds1, labels1, branches2, noeuds2, labels2)


class PrincipeMultiplicatif(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Principe multiplicatif")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : théorème du principe multiplicatif ----------------------
        theo = theorem_box(
            VGroup(
                Text("Principe multiplicatif", font_size=24, weight="BOLD"),
                MathTex(
                    r"\mathrm{Card}(A \times B) = \mathrm{Card}(A) \times \mathrm{Card}(B)",
                    font_size=27,
                ),
                MathTex(
                    r"\mathrm{Card}(A_1\times\cdots\times A_p) = \mathrm{Card}(A_1)\times\cdots\times\mathrm{Card}(A_p)",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici l'un des outils les plus utilisés du chapitre : le "
                "principe multiplicatif. Le cardinal du produit cartésien "
                "A fois B est égal au produit des cardinaux de A et de B. "
                "Ce résultat se généralise à un nombre quelconque "
                "d'ensembles : le cardinal d'un produit cartésien de p "
                "ensembles est le produit de leurs p cardinaux."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        # --- Raisonnement : tableau à double entrée + arbre --------------------
        justif = Text(
            _wrap(
                "Justification : pour chacun des Card(A) choix possibles "
                "dans A, il y a Card(B) choix possibles dans B — on peut "
                "les organiser dans un tableau à double entrée, ou les "
                "lister avec un arbre de choix.",
                width=54,
            ),
            font_size=23,
        )
        justif.next_to(titre, DOWN, buff=0.4)

        arbre = _arbre_choix()
        arbre.next_to(justif, DOWN, buff=0.5)
        calcul_arbre = MathTex(r"3 \times 2 = 6 \text{ chemins possibles}", font_size=25, color=YELLOW)
        calcul_arbre.next_to(arbre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pourquoi ce résultat ? Pour chacun des Card de A choix "
                "possibles dans A, il existe Card de B choix possibles "
                "dans B. On peut organiser toutes les combinaisons dans un "
                "tableau à double entrée, ou bien les représenter par un "
                "arbre de choix : un premier niveau de branches pour A, "
                "puis un second niveau pour B à chaque extrémité. Ici, "
                "avec 3 choix puis 2 choix, l'arbre compte exactement 6 "
                "chemins de la racine à une feuille, soit 3 fois 2."
            )
        ) as tracker:
            self.play(FadeIn(justif))
            self.play(Create(arbre))
            self.play(FadeIn(calcul_arbre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(justif), FadeOut(arbre), FadeOut(calcul_arbre))

        # --- Exemple traité : immatriculation ------------------------------------
        enonce_immat = Text(
            _wrap(
                "Exemple résolu 2 : une plaque d'immatriculation "
                "comporte 4 chiffres (de 0001 à 9999), suivis d'une "
                "lettre parmi 26, suivis d'un chiffre de série parmi 10. "
                "Combien de plaques distinctes peut-on former ?",
                width=54,
            ),
            font_size=23,
        )
        enonce_immat.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Mettons ce principe en pratique. Une plaque "
                "d'immatriculation est composée de 4 chiffres, allant de "
                "0001 à 9999, suivis d'une lettre parmi les 26 lettres de "
                "l'alphabet, suivis d'un chiffre de série parmi 10. "
                "Combien de plaques distinctes peut-on ainsi former ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_immat))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_immat))

        calcul_immat = MathTex(
            r"9999 \times 26 \times 10 = 2\,599\,740 \text{ plaques possibles}",
            font_size=27,
            color=YELLOW,
        )
        calcul_immat.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Il s'agit de trois choix successifs et indépendants : "
                "9999 possibilités pour le bloc de chiffres, 26 pour la "
                "lettre, 10 pour le chiffre de série. Le principe "
                "multiplicatif donne directement le résultat : 9999 fois "
                "26 fois 10, soit deux millions cinq cent quatre-vingt-dix "
                "neuf mille sept cent quarante plaques possibles."
            )
        ) as tracker:
            self.play(Write(calcul_immat))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_immat))

        # --- À retenir : méthode pour reconnaître un produit cartésien ---------
        meth = method_box(
            VGroup(
                Text("Reconnaître un produit cartésien", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "On peut appliquer le principe multiplicatif dès que la "
                        "situation se décompose en choix SUCCESSIFS et "
                        "INDÉPENDANTS les uns des autres (le nombre de "
                        "possibilités à une étape ne dépend pas des choix "
                        "précédents).",
                        width=52,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        meth.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la méthode : on peut appliquer le principe "
                "multiplicatif dès que la situation se décompose en choix "
                "successifs et indépendants les uns des autres, c'est-à-"
                "dire que le nombre de possibilités à une étape ne dépend "
                "jamais des choix faits aux étapes précédentes. C'est "
                "exactement le cas pour la plaque d'immatriculation : le "
                "nombre de lettres disponibles ne dépend pas du bloc de "
                "chiffres déjà choisi."
            )
        ) as tracker:
            self.play(FadeIn(meth))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth), FadeOut(titre))
