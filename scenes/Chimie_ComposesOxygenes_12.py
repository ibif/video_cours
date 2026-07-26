"""
scenes/Chimie_ComposesOxygenes_12.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 12 (clôture).

§ Méthodes condensées (classe d'un alcool, prévoir l'oxydation ménagée —
mnémotechnique « P-A-A, S-C, T-rien », rédiger une identification en 3
temps) + 5 pièges à éviter + L'ESSENTIEL DU CHAPITRE.
Source : 1ereC/Chimie.pdf, chapitre 6, pages 54-65 (synthèse).
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


def _bullets(items, font_size=20, color=WHITE, width=52):
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
        titre = scene_title("Méthodes, pièges à éviter et l'essentiel du chapitre")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : trois méthodes à automatiser --------------------------------------
        intro = Text(
            _wrap(
                "Terminons ce chapitre par trois méthodes à automatiser, "
                "cinq pièges classiques à éviter, puis l'essentiel à "
                "retenir.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce chapitre sur les composés oxygénés par trois "
                "méthodes à automatiser, cinq pièges classiques à éviter, "
                "puis l'essentiel à retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : méthode 1 (classe d'un alcool) -------------------------------
        methode1 = method_box(
            Text(
                _wrap(
                    "Déterminer la classe d'un alcool : repérer le carbone "
                    "fonctionnel (celui qui porte -OH), puis compter le "
                    "nombre d'autres atomes de carbone qui lui sont "
                    "directement reliés — 1 = primaire, 2 = secondaire, "
                    "3 = tertiaire.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        methode1.next_to(titre, DOWN, buff=0.4)
        _fit(methode1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Première méthode : déterminer la classe d'un alcool. On "
                "repère le carbone fonctionnel, celui qui porte le groupe "
                "hydroxyle, puis on compte le nombre d'autres atomes de "
                "carbone qui lui sont directement reliés. Un seul : "
                "l'alcool est primaire. Deux : il est secondaire. Trois : "
                "il est tertiaire."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : mnémotechnique de l'oxydation ménagée ---------------------------
        methode2 = method_box(
            VGroup(
                Text(
                    "Prévoir les produits d'une oxydation ménagée —",
                    font_size=22,
                ),
                Text(
                    "mnémotechnique « P-A-A, S-C, T-rien » :",
                    font_size=22,
                    weight="BOLD",
                ),
                Text("Primaire → Aldéhyde → Acide  |  Secondaire → Cétone  |  Tertiaire → rien", font_size=19),
            ).arrange(DOWN, buff=0.3),
            box_width=12.0,
        )
        methode2.next_to(titre, DOWN, buff=0.4)
        _fit(methode2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : prévoir les produits d'une oxydation "
                "ménagée grâce au moyen mnémotechnique « P-A-A, S-C, "
                "T-rien ». P-A-A : un alcool Primaire donne un Aldéhyde, "
                "puis un Acide en cas d'excès d'oxydant. S-C : un alcool "
                "Secondaire donne une Cétone, et s'arrête là. T-rien : un "
                "alcool Tertiaire ne donne rien du tout."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Méthode 3 : rédiger une identification par tests -----------------------------
        methode3 = method_box(
            Text(
                _wrap(
                    "Rédiger une identification par tests en 3 temps : "
                    "1) décrire le test effectué et l'observation obtenue ; "
                    "2) énoncer la conclusion que cette observation "
                    "autorise (pas plus !) ; 3) conclure sur la fonction du "
                    "composé seulement après avoir croisé plusieurs tests.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        methode3.next_to(titre, DOWN, buff=0.4)
        _fit(methode3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième méthode : rédiger une identification par tests "
                "en trois temps. Un, on décrit le test effectué et "
                "l'observation obtenue. Deux, on énonce précisément la "
                "conclusion que cette seule observation autorise, pas plus. "
                "Trois, on ne conclut sur la fonction exacte du composé "
                "qu'après avoir croisé les résultats de plusieurs tests."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Exemple traité / pièges à éviter ----------------------------------------------
        pieges = warning_box(
            _bullets(
                [
                    "N'écrivez jamais un aldéhyde R-COH : le groupe est "
                    "R-CHO (le H est sur le carbone du carbonyle, pas sur "
                    "un oxygène).",
                    "Un précipité avec la 2,4-DNPH ne prouve PAS un "
                    "aldéhyde : il faut confirmer par Fehling ou Tollens "
                    "(une cétone donne aussi ce précipité).",
                    "Jamais d'indice de position pour un aldéhyde : on dit "
                    "« butanal », jamais « butan-1-ol » ni « 1-butanal ».",
                    "Ne confondez pas carboxyle (-COOH, acides), hydroxyle "
                    "(-OH, alcools/phénols) et carbonyle (>C=O, "
                    "aldéhydes/cétones) : trois groupes distincts.",
                    "Un alcool tertiaire ne s'oxyde JAMAIS par oxydation "
                    "ménagée, quel que soit l'oxydant utilisé.",
                ],
                font_size=18,
                width=50,
            ),
            box_width=12.3,
        )
        pieges.next_to(titre, DOWN, buff=0.4)
        _fit(pieges, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Cinq pièges classiques à éviter. Premièrement, n'écrivez "
                "jamais un aldéhyde R-C-O-H : le groupe s'écrit R-C-H-O, "
                "l'hydrogène est porté par le carbone du carbonyle, pas "
                "par un oxygène. Deuxièmement, un précipité avec la "
                "2,4-DNPH ne prouve pas un aldéhyde : il faut toujours "
                "confirmer par le test de Fehling ou de Tollens, car une "
                "cétone donne aussi ce précipité. Troisièmement, jamais "
                "d'indice de position pour un aldéhyde : on dit butanal, "
                "jamais butan-un-al. Quatrièmement, ne confondez pas "
                "carboxyle, hydroxyle et carbonyle : trois groupes bien "
                "distincts. Cinquièmement, un alcool tertiaire ne s'oxyde "
                "jamais par oxydation ménagée, quel que soit l'oxydant "
                "utilisé."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) ---------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Alcool R-OH (CₙH₂ₙ₊₂O) : primaire, secondaire ou "
                    "tertiaire selon le carbone fonctionnel.",
                    "Phénol : -OH sur noyau benzénique — pas un alcool, "
                    "acide faible.",
                    "Aldéhyde R-CHO (bout de chaîne) et cétone R₁-CO-R₂ "
                    "(milieu de chaîne) : isomères de fonction (CₙH₂ₙO).",
                    "Acide carboxylique R-COOH (CₙH₂ₙO₂) : acide faible, "
                    "dissociation partielle avec l'eau.",
                    "Ester R-COO-R' (CₙH₂ₙO₂) : isomère de fonction des "
                    "acides, odeurs fruitées.",
                    "Oxydation ménagée : Primaire→Aldéhyde→Acide ; "
                    "Secondaire→Cétone ; Tertiaire→rien.",
                    "Tests : DNPH (carbonyle) ; Fehling/Tollens/Schiff "
                    "(aldéhyde seul).",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.3,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)
        _fit(essentiel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici l'essentiel à retenir de ce chapitre. Un alcool "
                "R-O-H, de formule C indice n, H indice deux n plus deux, "
                "O, est primaire, secondaire ou tertiaire selon la "
                "structure de son carbone fonctionnel. Un phénol porte "
                "l'hydroxyle sur un noyau benzénique : ce n'est pas un "
                "alcool, et il est acide faible. Un aldéhyde, en bout de "
                "chaîne, et une cétone, en milieu de chaîne, sont des "
                "isomères de fonction de formule C indice n, H indice deux "
                "n, O. Un acide carboxylique, R-C-O-O-H, est un acide "
                "faible qui ne se dissocie que partiellement dans l'eau. "
                "Un ester, R-C-O-O-R prime, est un isomère de fonction des "
                "acides, aux odeurs fruitées. L'oxydation ménagée : un "
                "alcool primaire donne un aldéhyde puis un acide ; un "
                "alcool secondaire donne une cétone ; un alcool tertiaire "
                "ne donne rien. Enfin, la 2,4-DNPH révèle un carbonyle, "
                "tandis que Fehling, Tollens et Schiff sont spécifiques "
                "des aldéhydes."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
