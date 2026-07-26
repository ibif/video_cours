"""
scenes/Chimie_ComposesOxygenes_10.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 10.

§ Les tests de reconnaissance des composés oxygénés : 2,4-DNPH (aldéhydes
+ cétones), liqueur de Fehling à chaud (aldéhydes seuls, Cu₂O rouge
brique), réactif de Tollens (aldéhydes seuls, miroir d'argent), réactif de
Schiff (aldéhydes, rose) + stratégie d'identification en cascade.
Source : 1ereC/Chimie.pdf, chapitre 6, pages 63-64.
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
from shapes.boxes import method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class TestsDeReconnaissance(NotionScene):
    def construct(self):
        titre = scene_title("Les tests de reconnaissance des composés oxygénés")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi des tests ----------------------------------------------
        intro = Text(
            _wrap(
                "Comment distinguer un aldéhyde d'une cétone au "
                "laboratoire, sans connaître d'avance la formule du "
                "composé ? Quatre tests de reconnaissance permettent de "
                "trancher.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment distinguer, au laboratoire, un aldéhyde d'une "
                "cétone, sans connaître d'avance la formule du composé "
                "étudié ? Quatre tests de reconnaissance permettent de "
                "trancher."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : test 1 et 2 ------------------------------------------------
        test1_titre = Text("Test 1 — la 2,4-DNPH", font_size=23, color=YELLOW, weight="BOLD")
        test1_titre.next_to(titre, DOWN, buff=0.35)

        test1 = Text(
            _wrap(
                "La 2,4-dinitrophénylhydrazine (2,4-DNPH) réagit avec le "
                "groupe carbonyle >C=O, donc avec les ALDÉHYDES ET les "
                "CÉTONES, en donnant un précipité JAUNE ORANGÉ. Ce test "
                "révèle un carbonyle mais ne distingue pas les deux "
                "familles.",
                width=48,
            ),
            font_size=21,
        )
        test1.next_to(test1_titre, DOWN, buff=0.4)

        groupe1 = VGroup(test1_titre, test1)
        _fit(groupe1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Premier test : la 2,4-dinitrophénylhydrazine, souvent "
                "abrégée 2,4-DNPH. Elle réagit avec le groupe carbonyle, "
                "donc à la fois avec les aldéhydes et avec les cétones, en "
                "formant un précipité jaune orangé. Ce test révèle donc la "
                "présence d'un groupe carbonyle, mais ne permet pas, à lui "
                "seul, de distinguer un aldéhyde d'une cétone."
            )
        ) as tracker:
            self.play(FadeIn(test1_titre))
            self.play(FadeIn(test1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        test2_titre = Text("Test 2 — la liqueur de Fehling (à chaud)", font_size=22, color=YELLOW, weight="BOLD")
        test2_titre.next_to(titre, DOWN, buff=0.35)

        test2 = Text(
            _wrap(
                "Chauffée avec un ALDÉHYDE, la liqueur de Fehling (bleue) "
                "forme un précipité ROUGE BRIQUE d'oxyde de cuivre(I), "
                "Cu₂O. Les CÉTONES ne réagissent PAS : ce test est "
                "spécifique des aldéhydes.",
                width=48,
            ),
            font_size=21,
        )
        test2.next_to(test2_titre, DOWN, buff=0.4)

        groupe2 = VGroup(test2_titre, test2)
        _fit(groupe2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deuxième test : la liqueur de Fehling, à chaud. Chauffée "
                "en présence d'un aldéhyde, cette solution bleue forme un "
                "précipité rouge brique d'oxyde de cuivre un, Cu-2-O. Les "
                "cétones, elles, ne réagissent pas : ce test est donc "
                "spécifique des aldéhydes."
            )
        ) as tracker:
            self.play(FadeIn(test2_titre))
            self.play(FadeIn(test2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- Exemple traité : test 3 et 4 -----------------------------------------------
        test3_titre = Text("Test 3 — le réactif de Tollens (au bain-marie)", font_size=21, color=YELLOW, weight="BOLD")
        test3_titre.next_to(titre, DOWN, buff=0.35)

        test3 = Text(
            _wrap(
                "Chauffé au bain-marie avec un ALDÉHYDE, le réactif de "
                "Tollens dépose un MIROIR D'ARGENT sur la paroi du tube. "
                "Là encore, spécifique des aldéhydes.",
                width=48,
            ),
            font_size=21,
        )
        test3.next_to(test3_titre, DOWN, buff=0.4)

        groupe3 = VGroup(test3_titre, test3)
        _fit(groupe3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième test : le réactif de Tollens. Chauffé "
                "doucement, au bain-marie, en présence d'un aldéhyde, il "
                "dépose un miroir d'argent brillant sur la paroi du tube à "
                "essai. Ce test, lui aussi, est spécifique des aldéhydes."
            )
        ) as tracker:
            self.play(FadeIn(test3_titre))
            self.play(FadeIn(test3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe3))

        test4_titre = Text("Test 4 — le réactif de Schiff", font_size=23, color=YELLOW, weight="BOLD")
        test4_titre.next_to(titre, DOWN, buff=0.35)

        test4 = Text(
            _wrap(
                "Le réactif de Schiff, incolore, prend une coloration "
                "ROSE / VIOLETTE au contact d'un ALDÉHYDE, à froid.",
                width=48,
            ),
            font_size=21,
        )
        test4.next_to(test4_titre, DOWN, buff=0.4)

        groupe4 = VGroup(test4_titre, test4)
        _fit(groupe4, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Quatrième test : le réactif de Schiff, incolore au "
                "départ, prend une coloration rose à violette au contact "
                "d'un aldéhyde, à froid, sans même besoin de chauffer."
            )
        ) as tracker:
            self.play(FadeIn(test4_titre))
            self.play(FadeIn(test4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe4))

        # --- À retenir : stratégie d'identification en cascade --------------------------
        strategie = method_box(
            Text(
                _wrap(
                    "Stratégie d'identification en cascade : 1) tester la "
                    "2,4-DNPH — précipité jaune orangé = carbonyle présent "
                    "(aldéhyde OU cétone) ; 2) tester Fehling ou Tollens — "
                    "positif = ALDÉHYDE, négatif = CÉTONE ; 3) tester le "
                    "papier pH si l'on soupçonne une oxydation poussée = "
                    "ACIDE CARBOXYLIQUE.",
                    width=48,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        strategie.next_to(titre, DOWN, buff=0.4)
        _fit(strategie, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons la stratégie d'identification en cascade, à "
                "appliquer dans cet ordre. Un, on teste la 2,4-DNPH : un "
                "précipité jaune orangé indique la présence d'un carbonyle, "
                "donc d'un aldéhyde ou d'une cétone. Deux, on teste "
                "ensuite la liqueur de Fehling ou le réactif de Tollens : "
                "un résultat positif confirme un aldéhyde, un résultat "
                "négatif oriente vers une cétone. Trois, si l'on soupçonne "
                "une oxydation poussée jusqu'à l'acide, on teste le papier "
                "pH, qui rougit en présence d'un acide carboxylique."
            )
        ) as tracker:
            self.play(FadeIn(strategie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(strategie), FadeOut(titre))
