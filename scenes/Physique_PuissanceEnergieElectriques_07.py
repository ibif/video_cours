"""
scenes/Physique_PuissanceEnergieElectriques_07.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 07.

§ 6. Bilan énergétique d'un circuit série (loi de Pouillet). Circuit série
générateur (E, r) + résistor R + récepteur (E', r'). Bilan énergétique
global P_e=P_u+P_th, simplification par I, établissement de la loi de
Pouillet I=(E-E')/(R+r+r'). Condition de fonctionnement E>E'. Exemple
résolu (circuit générateur + résistor + moteur en série).
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 6).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Circle, FadeIn, FadeOut, Line, MathTex, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _circuit_pouillet():
    """Boucle série : générateur (E,r) — résistor R — moteur (E',r'),
    reliés par des fils, avec la flèche du courant I."""
    tl = UP * 1.1 + LEFT * 3.4
    tr = UP * 1.1 + RIGHT * 3.4
    bl = DOWN * 1.1 + LEFT * 3.4
    br = DOWN * 1.1 + RIGHT * 3.4

    # Générateur sur le côté gauche (vertical)
    gen_mid = (tl + bl) / 2
    gen = VGroup(
        Line(gen_mid + UP * 0.3 + LEFT * 0.22, gen_mid + UP * 0.3 + RIGHT * 0.22, stroke_width=5, color=WHITE),
        Line(gen_mid + DOWN * 0.3 + LEFT * 0.1, gen_mid + DOWN * 0.3 + RIGHT * 0.1, stroke_width=2, color=WHITE),
    )
    label_gen = Text("E, r", font_size=18, color=WHITE).next_to(gen, LEFT, buff=0.15)
    fil_g_haut = Line(tl, gen_mid + UP * 0.3, stroke_width=3, color=WHITE)
    fil_g_bas = Line(gen_mid + DOWN * 0.3, bl, stroke_width=3, color=WHITE)

    # Résistor sur le côté haut (horizontal)
    R = Rectangle(width=1.1, height=0.5, color=WHITE, stroke_width=3)
    R.move_to((tl + tr) / 2)
    label_R = Text("R", font_size=20, color=WHITE).move_to(R.get_center())
    fil_h_g = Line(tl, R.get_left(), stroke_width=3, color=WHITE)
    fil_h_d = Line(R.get_right(), tr, stroke_width=3, color=WHITE)

    # Moteur sur le côté droit (vertical)
    moteur = Circle(radius=0.42, color=WHITE, stroke_width=3)
    moteur.move_to((tr + br) / 2)
    label_m = Text("M", font_size=22, color=WHITE, weight="BOLD").move_to(moteur.get_center())
    label_moteur = Text("E', r'", font_size=18, color=WHITE).next_to(moteur, RIGHT, buff=0.15)
    fil_d_haut = Line(tr, moteur.get_top(), stroke_width=3, color=WHITE)
    fil_d_bas = Line(moteur.get_bottom(), br, stroke_width=3, color=WHITE)

    # Fil du bas
    fil_bas = Line(bl, br, stroke_width=3, color=WHITE)

    fleche_I = Line(bl + RIGHT * 1.0, bl + RIGHT * 2.2, stroke_width=3, color=YELLOW)
    fleche_I_tip = Text("→", font_size=22, color=YELLOW).move_to(bl + RIGHT * 2.35)
    label_I = Text("I", font_size=20, color=YELLOW).next_to(fleche_I, DOWN, buff=0.08)

    return VGroup(
        gen, label_gen, fil_g_haut, fil_g_bas,
        R, label_R, fil_h_g, fil_h_d,
        moteur, label_m, label_moteur, fil_d_haut, fil_d_bas,
        fil_bas, fleche_I, fleche_I_tip, label_I,
    )


class LoiPouillet(NotionScene):
    def construct(self):
        titre = scene_title("La loi de Pouillet")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Considérons un circuit série complet : un générateur (E, r), "
                "un résistor R, et un récepteur (E', r'). Comment calculer "
                "directement l'intensité qui circule, sans jamais mesurer "
                "de tension ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Considérons un circuit série complet, comprenant un "
                "générateur de f é m E et de résistance interne r, un "
                "résistor R, et un récepteur de f c é m E prime et de "
                "résistance interne r prime. Comment calculer directement "
                "l'intensité qui circule dans ce circuit, sans avoir à "
                "mesurer la moindre tension ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : bilan énergétique global + établissement -------------
        circuit = _circuit_pouillet()
        circuit.scale(0.9)
        circuit.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Dans ce circuit série, un seul et même courant I traverse "
                "tous les dipôles. Le générateur engendre une puissance E "
                "I. Cette puissance se répartit entre la puissance utile "
                "fournie par le récepteur, E prime I, et toutes les "
                "puissances dissipées par effet Joule dans les trois "
                "résistances internes r, R et r prime."
            )
        ) as tracker:
            self.play(FadeIn(circuit))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(circuit))

        etablissement = VGroup(
            Text("Bilan énergétique global du circuit (puissance engendrée", font_size=20),
            Text("= puissance utile + toutes les pertes Joule) :", font_size=20),
            MathTex(r"E I = E' I + r I^2 + R I^2 + r' I^2", font_size=25),
            Text("En divisant chaque terme par I (I ≠ 0) :", font_size=20),
            MathTex(r"E = E' + (r + R + r') I", font_size=27),
        ).arrange(DOWN, buff=0.18)
        etablissement.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Écrivons ce bilan énergétique global : la puissance "
                "engendrée E I est égale à la puissance utile E prime I, "
                "plus toutes les puissances Joule, r I carré, R I carré, et "
                "r prime I carré. En divisant chaque terme par I, qui n'est "
                "jamais nul dans un circuit fermé, on obtient : E égale E "
                "prime plus, entre parenthèses, r plus R plus r prime, le "
                "tout fois I."
            )
        ) as tracker:
            self.play(FadeIn(etablissement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etablissement))

        loi_pouillet = theorem_box(
            VGroup(
                Text("Loi de Pouillet", font_size=24, weight="BOLD"),
                MathTex(r"I = \dfrac{E - E'}{R + r + r'}", font_size=34),
                Text("Condition de fonctionnement : E > E'", font_size=21),
                Text("(sinon aucun courant ne peut circuler dans ce sens).", font_size=19),
            ).arrange(DOWN, buff=0.22),
            box_width=10.6,
        )
        loi_pouillet.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En isolant I, on obtient la loi de Pouillet : l'intensité "
                "dans un circuit série vaut la différence des forces "
                "électromotrices et contre-électromotrices, E moins E "
                "prime, divisée par la somme de TOUTES les résistances du "
                "circuit, R plus r plus r prime. Ce courant ne peut circuler "
                "dans ce sens que si E est strictement supérieure à E "
                "prime."
            )
        ) as tracker:
            self.play(FadeIn(loi_pouillet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi_pouillet))

        # --- Exemple résolu ---------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Générateur E = 12 V, r = 0,2 Ω ; résistor R = 3 Ω ;", font_size=20),
                Text("moteur E' = 4 V, r' = 0,8 Ω, montés en série.", font_size=20),
                MathTex(r"I = \dfrac{E - E'}{R + r + r'} = \dfrac{12 - 4}{3 + 0{,}2 + 0{,}8} = \dfrac{8}{4} = 2\ \text{A}", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : un générateur de f é m douze volts et de "
                "résistance interne zéro virgule deux ohm, un résistor de "
                "trois ohms, et un moteur de f c é m quatre volts et de "
                "résistance interne zéro virgule huit ohm, sont montés en "
                "série. L'intensité vaut E moins E prime, sur R plus r plus "
                "r prime, soit douze moins quatre, sur trois plus zéro "
                "virgule deux plus zéro virgule huit, c'est-à-dire huit sur "
                "quatre, soit deux ampères."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"I = \dfrac{E - E'}{R + r + r'} \qquad (\text{circuit série, condition } E > E')", font_size=26),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : dans un circuit série, la loi de "
                "Pouillet donne directement l'intensité, différence des f é "
                "m sur somme de toutes les résistances, sous la condition "
                "que E soit supérieure à E prime."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas oublier r et r' au dénominateur : ce sont des", font_size=20),
                Text("   résistances comme R, elles s'additionnent avec elle.", font_size=20),
                Text("• S'il n'y a pas de récepteur (juste des résistors), E' = 0", font_size=20),
                Text("   dans la formule : I = E/(R+r).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Il ne faut jamais oublier les "
                "résistances internes r et r prime au dénominateur : ce "
                "sont des résistances comme les autres, elles s'ajoutent à "
                "R. Et s'il n'y a pas de récepteur dans le circuit, mais "
                "seulement des résistors, on prend simplement E prime égale "
                "zéro, et la formule se réduit à I égale E sur R plus r."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
