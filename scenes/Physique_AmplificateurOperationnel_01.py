"""
scenes/Physique_AmplificateurOperationnel_01.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 01.

§ 1. Présentation de l'amplificateur opérationnel (AO) : composant intégré
qui amplifie la différence de potentiel entre ses deux entrées. Boîtier
DIP8 : bornes 2 = E- (entrée inverseuse), 3 = E+ (entrée non inverseuse),
4 = -Vcc, 7 = +Vcc, 6 = S (sortie), 1 et 5 = offset (non étudié),
8 = NC (non connecté). Alimentation symétrique (ex : ±15 V). Symbole
normalisé (triangle), tension différentielle ε = V+ - V-.
Source : 1ereC/Physique.pdf, pages 99-107 (§ 1).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _boitier_dip8():
    """Boîtier DIP8 schématique : rectangle avec 8 broches numérotées,
    4 à gauche (1 à 4, de haut en bas) et 4 à droite (5 à 8, de bas en
    haut) — numérotation standard en U autour du boîtier."""
    corps = Rectangle(width=2.4, height=1.8, color=WHITE, stroke_width=3)
    encoche = Text("●", font_size=14, color=WHITE).move_to(corps.get_top() + LEFT * 0.9 + DOWN * 0.15)

    pins = VGroup()
    gauche_y = [0.6, 0.2, -0.2, -0.6]
    gauche_num = ["1", "2", "3", "4"]
    for y, n in zip(gauche_y, gauche_num):
        depart = corps.get_left() + UP * y
        fin = depart + LEFT * 0.55
        ligne = Line(depart, fin, stroke_width=3, color=WHITE)
        label = Text(n, font_size=16, color=WHITE).next_to(fin, LEFT, buff=0.08)
        pins.add(ligne, label)

    droite_y = [-0.6, -0.2, 0.2, 0.6]
    droite_num = ["5", "6", "7", "8"]
    for y, n in zip(droite_y, droite_num):
        depart = corps.get_right() + UP * y
        fin = depart + RIGHT * 0.55
        ligne = Line(depart, fin, stroke_width=3, color=WHITE)
        label = Text(n, font_size=16, color=WHITE).next_to(fin, RIGHT, buff=0.08)
        pins.add(ligne, label)

    return VGroup(corps, encoche, pins)


def _ao_symbole(width=2.4, height=1.6):
    """Symbole normalisé de l'AO : triangle pointant vers la droite (la
    sortie), base à gauche avec l'entrée E+ en haut et E- en bas."""
    haut = UP * height / 2 + LEFT * width / 2
    bas = DOWN * height / 2 + LEFT * width / 2
    pointe = RIGHT * width / 2
    triangle = Polygon(haut, bas, pointe, color=WHITE, stroke_width=3)

    plus = Text("+", font_size=24, color=WHITE).move_to(haut + RIGHT * 0.35 + DOWN * 0.05)
    moins = Text("−", font_size=24, color=WHITE).move_to(bas + RIGHT * 0.35 + UP * 0.05)

    fil_e_plus = Line(haut + LEFT * 0.5, haut, stroke_width=3, color=WHITE)
    fil_e_moins = Line(bas + LEFT * 0.5, bas, stroke_width=3, color=WHITE)
    fil_s = Line(pointe, pointe + RIGHT * 0.5, stroke_width=3, color=WHITE)

    label_e_plus = Text("E+", font_size=18, color=YELLOW).next_to(fil_e_plus, LEFT, buff=0.08)
    label_e_moins = Text("E−", font_size=18, color=YELLOW).next_to(fil_e_moins, LEFT, buff=0.08)
    label_s = Text("S", font_size=18, color=ORANGE).next_to(fil_s, RIGHT, buff=0.08)

    return VGroup(
        triangle, plus, moins, fil_e_plus, fil_e_moins, fil_s,
        label_e_plus, label_e_moins, label_s,
    )


class PresentationAmplificateurOperationnel(NotionScene):
    def construct(self):
        titre = scene_title("L'amplificateur opérationnel : présentation")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Un petit boîtier à 8 broches capable d'amplifier des "
                "milliers de fois une infime différence de tension : "
                "c'est l'amplificateur opérationnel, présent dans presque "
                "tous les circuits électroniques modernes.",
                width=58,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un petit boîtier à huit broches, capable d'amplifier des "
                "milliers de fois une infime différence de tension : c'est "
                "l'amplificateur opérationnel, noté AO, présent dans "
                "presque tous les circuits électroniques modernes. Voyons "
                "de quoi il s'agit."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition -------------------------------------
        definition = definition_box(
            VGroup(
                Text("L'amplificateur opérationnel (AO) est un composant", font_size=20),
                Text("électronique intégré qui amplifie la différence de", font_size=20),
                Text("potentiel entre ses deux entrées.", font_size=20),
                MathTex(r"\varepsilon = V_+ - V_-", font_size=30),
            ).arrange(DOWN, buff=0.2),
            box_width=10.6,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'amplificateur opérationnel, ou AO, est un composant "
                "électronique intégré : il amplifie la différence de "
                "potentiel entre ses deux entrées, notée epsilon, et égale "
                "à V plus moins V moins."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : boîtier DIP8 -----------------------------------
        boitier = _boitier_dip8()
        boitier.scale(1.1)
        boitier.next_to(titre, DOWN, buff=0.6).shift(LEFT * 3.0)

        legende_pins = VGroup(
            Text("2 = E− (entrée inverseuse)", font_size=18, color=YELLOW),
            Text("3 = E+ (entrée non inverseuse)", font_size=18, color=YELLOW),
            Text("4 = −Vcc  •  7 = +Vcc (alimentation)", font_size=18, color=ORANGE),
            Text("6 = S (sortie)", font_size=18, color=ORANGE),
            Text("1 et 5 = offset (réglage, non étudié)", font_size=17),
            Text("8 = NC (non connecté)", font_size=17),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        legende_pins.next_to(boitier, RIGHT, buff=0.7)

        with self.voiceover(
            text=(
                "Vu de dessus, le boîtier possède huit broches. La broche "
                "2 est l'entrée inverseuse E moins, la broche 3 est "
                "l'entrée non inverseuse E plus. Les broches 4 et 7 "
                "reçoivent l'alimentation, moins V C C et plus V C C. La "
                "broche 6 délivre la tension de sortie S. Les broches 1 et "
                "5 servent à un réglage d'offset que nous n'étudierons "
                "pas, et la broche 8 n'est pas connectée."
            )
        ) as tracker:
            self.play(FadeIn(boitier))
            self.play(FadeIn(legende_pins))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(boitier), FadeOut(legende_pins))

        # --- Exemple : symbole + alimentation symétrique --------------------
        symbole = _ao_symbole()
        symbole.next_to(titre, DOWN, buff=0.7).shift(LEFT * 1.5)

        alim = VGroup(
            Text("+Vcc = +15 V", font_size=20, color=ORANGE),
            Text("−Vcc = −15 V", font_size=20, color=ORANGE),
        ).arrange(DOWN, buff=0.2)
        alim.next_to(symbole, RIGHT, buff=1.0)

        exemple = example_box(
            VGroup(
                Text("Symbole normalisé : triangle, entrée E+ (en haut),", font_size=19),
                Text("entrée E− (en bas), sortie S (pointe).", font_size=19),
                Text("Exemple d'alimentation symétrique : +Vcc = +15 V", font_size=19),
                Text("et −Vcc = −15 V, appliquées aux broches 7 et 4.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=10.8,
        )
        exemple.next_to(VGroup(symbole, alim), DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Sur les schémas, l'AO est représenté par ce symbole "
                "normalisé : un triangle, avec l'entrée E plus en haut, "
                "l'entrée E moins en bas, et la sortie S à la pointe. Par "
                "exemple, on l'alimente souvent de façon symétrique : plus "
                "quinze volts et moins quinze volts, appliqués aux broches "
                "sept et quatre. Cette alimentation, bien que rarement "
                "dessinée sur les schémas simplifiés, est indispensable "
                "au fonctionnement du composant."
            )
        ) as tracker:
            self.play(FadeIn(symbole))
            self.play(FadeIn(alim))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(symbole), FadeOut(alim), FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("AO = composant intégré amplifiant ε = V+ − V−.", font_size=20),
                Text("Bornes clés : 2 = E−, 3 = E+, 6 = S, 4 = −Vcc, 7 = +Vcc.", font_size=20),
                Text("Alimentation symétrique indispensable (ex : ±15 V).", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. L'AO est un composant intégré qui "
                "amplifie epsilon, la différence entre V plus et V moins. "
                "Les bornes clés sont : deux pour E moins, trois pour E "
                "plus, six pour la sortie S, quatre et sept pour "
                "l'alimentation. Cette alimentation symétrique, par "
                "exemple plus ou moins quinze volts, est indispensable au "
                "fonctionnement du composant."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas confondre l'entrée E+ (broche 3) et l'entrée", font_size=19),
                Text("   E− (broche 2) : leur rôle est totalement différent", font_size=19),
                Text("   dans le comportement du montage.", font_size=19),
                Text("• Ne jamais oublier l'alimentation symétrique sur un", font_size=19),
                Text("   schéma : sans elle, l'AO ne peut pas fonctionner,", font_size=19),
                Text("   même si elle n'est pas toujours dessinée.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. D'abord, ne pas confondre l'entrée "
                "E plus, broche trois, avec l'entrée E moins, broche deux "
                ": leur rôle dans le comportement du montage est "
                "totalement différent. Ensuite, ne jamais oublier "
                "l'alimentation symétrique sur un schéma : sans elle, "
                "l'AO ne peut tout simplement pas fonctionner, même si "
                "elle n'est pas toujours représentée par souci de "
                "simplicité."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
