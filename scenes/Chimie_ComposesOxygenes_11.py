"""
scenes/Chimie_ComposesOxygenes_11.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 11.

§ Méthodes de calcul : déterminer la formule brute par la masse molaire
(tableau M=f(n) par famille), résolution par entier n, densité de vapeur
M=29d et composition centésimale %O=16k/M.
Source : 1ereC/Chimie.pdf, chapitre 6, page 64 (exploitation de données
expérimentales).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, exercise_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class DeterminerLaFormuleBrute(NotionScene):
    def construct(self):
        titre = scene_title("Déterminer une formule brute à partir de données")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : la méthode par masse molaire -------------------------------------
        methode1 = method_box(
            VGroup(
                Text(
                    "Connaissant la masse molaire M et la famille chimique,",
                    font_size=21,
                ),
                Text("on résout M = 14n + k pour l'entier n :", font_size=21),
                VGroup(
                    Text("alcool : k = 18", font_size=20),
                    Text("aldéhyde / cétone : k = 16", font_size=20),
                    Text("acide / ester : k = 32", font_size=20),
                ).arrange(RIGHT, buff=0.7),
            ).arrange(DOWN, buff=0.3),
            box_width=12.0,
        )
        methode1.next_to(titre, DOWN, buff=0.4)
        _fit(methode1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par les méthodes de calcul qui "
                "permettent d'exploiter des données expérimentales. "
                "Première méthode : connaissant la masse molaire M et la "
                "famille chimique du composé, on résout l'équation M égale "
                "quatorze n plus k pour trouver l'entier n. La constante k "
                "vaut dix-huit pour un alcool, seize pour un aldéhyde ou "
                "une cétone, et trente-deux pour un acide carboxylique ou "
                "un ester."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Raisonnement : exemple résolu (alcool) -------------------------------------
        enonce1 = exercise_box(
            Text(
                "Un alcool a pour masse molaire M = 74 g/mol. Formule brute ?",
                font_size=22,
                color="#1A1A1A",
            ),
            box_width=11.0,
        )
        enonce1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : un alcool a pour masse molaire soixante-quatorze "
                "grammes par mole. Quelle est sa formule brute ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce1))

        resolution1 = corrige_box(
            VGroup(
                MathTex(r"74 = 14n + 18 \;\Rightarrow\; n = \dfrac{56}{14} = 4", font_size=27, color="#1A1A1A"),
                Text("Formule brute : C₄H₁₀O", font_size=26, weight="BOLD"),
            ).arrange(DOWN, buff=0.35),
            box_width=9.5,
        )
        resolution1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On pose soixante-quatorze égale quatorze n plus dix-huit, "
                "d'où n égale cinquante-six sur quatorze, soit quatre. La "
                "formule brute est donc C-4, H-10, O."
            )
        ) as tracker:
            self.play(FadeIn(resolution1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution1))

        # --- Exemple traité : densité de vapeur et composition centésimale -------------
        methode2_titre = Text("Autre voie : densité de vapeur", font_size=23, color=YELLOW, weight="BOLD")
        methode2_titre.next_to(titre, DOWN, buff=0.35)

        formule_densite = MathTex(r"M = 29\,d", font_size=30, color=WHITE)
        formule_densite.next_to(methode2_titre, DOWN, buff=0.4)

        commentaire_densite = Text(
            _wrap(
                "où d est la densité de la vapeur du composé par rapport à "
                "l'air (masse molaire de l'air ≈ 29 g/mol).",
                width=48,
            ),
            font_size=20,
        )
        commentaire_densite.next_to(formule_densite, DOWN, buff=0.35)

        groupe_densite = VGroup(methode2_titre, formule_densite, commentaire_densite)

        with self.voiceover(
            text=(
                "Autre voie possible pour obtenir M : à partir de la "
                "densité de vapeur du composé. On a M égale vingt-neuf d, "
                "où d est la densité de la vapeur du composé par rapport à "
                "l'air, dont la masse molaire moyenne vaut environ "
                "vingt-neuf grammes par mole."
            )
        ) as tracker:
            self.play(FadeIn(methode2_titre))
            self.play(Write(formule_densite))
            self.play(FadeIn(commentaire_densite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_densite))

        methode3_titre = Text("Composition centésimale massique en oxygène", font_size=22, color=YELLOW, weight="BOLD")
        methode3_titre.next_to(titre, DOWN, buff=0.35)

        formule_pct = MathTex(r"\%O = \dfrac{16k}{M}\times 100", font_size=30, color=WHITE)
        formule_pct.next_to(methode3_titre, DOWN, buff=0.4)

        commentaire_pct = Text(
            _wrap(
                "où k est le nombre d'atomes d'oxygène par molécule (k=1 "
                "pour un alcool/aldéhyde/cétone, k=2 pour un acide/ester).",
                width=48,
            ),
            font_size=20,
        )
        commentaire_pct.next_to(formule_pct, DOWN, buff=0.35)

        groupe_pct = VGroup(methode3_titre, formule_pct, commentaire_pct)
        _fit(groupe_pct, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "On peut aussi exploiter la composition centésimale "
                "massique en oxygène : le pourcentage d'oxygène est égal à "
                "seize k sur M, multiplié par cent, où k est le nombre "
                "d'atomes d'oxygène par molécule — un pour un alcool, un "
                "aldéhyde ou une cétone ; deux pour un acide carboxylique "
                "ou un ester."
            )
        ) as tracker:
            self.play(FadeIn(methode3_titre))
            self.play(Write(formule_pct))
            self.play(FadeIn(commentaire_pct))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_pct))

        # --- À retenir : synthèse de la méthode -----------------------------------------
        synthese = method_box(
            Text(
                _wrap(
                    "Quelle que soit la donnée de départ (masse molaire, "
                    "densité de vapeur, composition centésimale), l'objectif "
                    "est TOUJOURS de retrouver M, puis de résoudre "
                    "M = 14n + k pour un entier n, k dépendant de la "
                    "famille chimique identifiée.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        synthese.next_to(titre, DOWN, buff=0.4)
        _fit(synthese, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons la méthode générale. Quelle que soit la donnée "
                "expérimentale de départ — masse molaire directe, densité "
                "de vapeur, ou composition centésimale — l'objectif est "
                "toujours de retrouver la masse molaire M, puis de "
                "résoudre l'équation M égale quatorze n plus k pour un "
                "entier n, la constante k dépendant de la famille chimique "
                "déjà identifiée grâce aux tests de reconnaissance."
            )
        ) as tracker:
            self.play(FadeIn(synthese))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(synthese), FadeOut(titre))
