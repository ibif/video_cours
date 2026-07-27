"""
scenes/Physique_PuissanceEnergieElectriques_04.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 04.

§ 4. Bilan énergétique d'un générateur. F.é.m. E et résistance interne r.
Loi d'Ohm du générateur U_PN=E-rI (caractéristique décroissante). Bilan
des puissances (multiplier par I) : P_e=EI (engendrée), P_J=rI² (perdue
Joule), P_f=UI=EI-rI² (fournie), avec P_e=P_f+P_J. Rendement du
générateur η_g=P_f/P_e=U/E=1-rI/E. Exemple résolu : E=12 V, r=0,5 Ω,
I=2 A → U=11 V, P_e=24 W, P_J=2 W, P_f=22 W, η≈91,7 %.
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 4).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _generateur_schema():
    """Générateur (pile idéalisée E, r) débitant dans un fil, avec les
    flèches I et U de MÊME SENS (convention générateur)."""
    p = UP * 0.3 + LEFT * 0.3
    n = DOWN * 0.3 + LEFT * 0.3
    borne_p = Line(p + LEFT * 0.25, p + RIGHT * 0.25, stroke_width=5, color=WHITE)
    borne_n = Line(n + LEFT * 0.12, n + RIGHT * 0.12, stroke_width=2, color=WHITE)
    label_gen = Text("E, r", font_size=22, color=WHITE).next_to(VGroup(borne_p, borne_n), LEFT, buff=0.35)

    fil_haut = Line(p, p + RIGHT * 2.2, stroke_width=3, color=WHITE)
    fil_bas = Line(n, n + RIGHT * 2.2, stroke_width=3, color=WHITE)

    fleche_I = Line(p + RIGHT * 0.5, p + RIGHT * 1.6, stroke_width=3, color=YELLOW)
    fleche_I_tip = Text("→", font_size=24, color=YELLOW).move_to(p + RIGHT * 1.7)
    label_I = Text("I", font_size=22, color=YELLOW).next_to(fleche_I, UP, buff=0.08)

    label_P = Text("P", font_size=18, color=WHITE).move_to(p + RIGHT * 0.0 + UP * 0.35)
    label_N = Text("N", font_size=18, color=WHITE).move_to(n + RIGHT * 0.0 + DOWN * 0.3)

    return VGroup(borne_p, borne_n, label_gen, fil_haut, fil_bas, fleche_I, fleche_I_tip, label_I, label_P, label_N)


class BilanGenerateur(NotionScene):
    def construct(self):
        titre = scene_title("Bilan énergétique d'un générateur")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Une pile ne convertit jamais 100 % de son énergie chimique "
                "en énergie électrique utile : une partie chauffe la pile "
                "elle-même. Comment quantifier ce que le générateur "
                "engendre, perd et fournit réellement au circuit ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une pile ne convertit jamais toute son énergie chimique en "
                "énergie électrique utile : une partie chauffe la pile "
                "elle-même, par effet Joule interne. Comment quantifier ce "
                "qu'un générateur engendre, ce qu'il perd, et ce qu'il "
                "fournit réellement au circuit ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- f.é.m., résistance interne, loi d'Ohm générateur -------------------
        schema = _generateur_schema()
        schema.next_to(titre, DOWN, buff=0.55)

        definition_E = definition_box(
            VGroup(
                Text("Tout générateur réel est caractérisé par :", font_size=21),
                Text("• sa force électromotrice (f.é.m.) E, en volts (V) ;", font_size=20),
                Text("• sa résistance interne r, en ohms (Ω).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=10.6,
        )
        definition_E.next_to(schema, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Tout générateur réel est caractérisé par deux grandeurs : "
                "sa force électromotrice, notée E, exprimée en volts, et sa "
                "résistance interne, notée r, exprimée en ohms. En "
                "convention générateur, les flèches I et U sont de même "
                "sens, comme sur ce schéma."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(definition_E))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(definition_E))

        loi_ohm_gen = theorem_box(
            VGroup(
                Text("Loi d'Ohm du générateur", font_size=23, weight="BOLD"),
                MathTex(r"U_{PN} = E - r I", font_size=32),
                Text("Caractéristique U=f(I) : droite DÉCROISSANTE,", font_size=20),
                Text("d'ordonnée à l'origine E et de pente -r.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=10.8,
        )
        loi_ohm_gen.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La loi d'Ohm du générateur s'écrit U P N égale E moins r "
                "I : la tension aux bornes chute quand l'intensité "
                "débitée augmente. Sur un graphique U en fonction de I, "
                "cette relation est une droite décroissante, dont "
                "l'ordonnée à l'origine vaut E et la pente vaut moins r."
            )
        ) as tracker:
            self.play(FadeIn(loi_ohm_gen))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi_ohm_gen))

        # --- Bilan des puissances --------------------------------------------------
        bilan = VGroup(
            Text("En multipliant U_PN = E - rI par I :", font_size=21),
            MathTex(r"U I = E I - r I^2", font_size=28),
            MathTex(r"P_e = E I \quad (\text{puissance engendrée})", font_size=25),
            MathTex(r"P_J = r I^2 \quad (\text{puissance perdue par effet Joule})", font_size=25),
            MathTex(r"P_f = U I = E I - r I^2 \quad (\text{puissance fournie au circuit})", font_size=25),
            MathTex(r"P_e = P_f + P_J", font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.16)
        bilan.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Multiplions la loi d'Ohm par l'intensité I : U I égale E I "
                "moins r I carré. On identifie trois puissances. E I est la "
                "puissance engendrée par le générateur, notée P e. r I "
                "carré est la puissance perdue par effet Joule à "
                "l'intérieur du générateur, notée P J. Et U I, ce qui reste, "
                "est la puissance fournie au reste du circuit, notée P f. "
                "Le bilan s'écrit : P e égale P f plus P J."
            )
        ) as tracker:
            self.play(FadeIn(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bilan))

        # --- Rendement -----------------------------------------------------------
        rendement = definition_box(
            VGroup(
                Text("Rendement du générateur", font_size=23, weight="BOLD"),
                MathTex(r"\eta_g = \dfrac{P_f}{P_e} = \dfrac{U}{E} = 1 - \dfrac{r I}{E}", font_size=28),
                Text("η_g est toujours compris entre 0 et 1 (souvent en %).", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=10.8,
        )
        rendement.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le rendement du générateur, noté êta indice g, est le "
                "rapport de la puissance fournie sur la puissance "
                "engendrée : êta g égale P f sur P e, ce qui se simplifie "
                "en U sur E, ou encore un moins r I sur E. Ce rendement est "
                "toujours compris entre zéro et un, et s'exprime souvent en "
                "pourcentage."
            )
        ) as tracker:
            self.play(FadeIn(rendement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rendement))

        # --- Exemple résolu 3 -------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Générateur E = 12 V, r = 0,5 Ω, débitant I = 2 A.", font_size=20),
                MathTex(r"U = E - rI = 12 - 0{,}5\times 2 = 11\ \text{V}", font_size=25),
                MathTex(r"P_e = EI = 24\ \text{W}, \quad P_J = rI^2 = 2\ \text{W}, \quad P_f = UI = 22\ \text{W}", font_size=23),
                MathTex(r"\eta_g = \dfrac{22}{24} \approx 91{,}7\ \%", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : un générateur de f é m douze volts et de "
                "résistance interne zéro virgule cinq ohm débite un courant "
                "de deux ampères. La tension à ses bornes vaut E moins r I, "
                "soit onze volts. La puissance engendrée vaut vingt-quatre "
                "watts, la puissance perdue par effet Joule vaut deux "
                "watts, et la puissance fournie au circuit vaut vingt-deux "
                "watts. Le rendement vaut vingt-deux sur vingt-quatre, "
                "environ quatre-vingt-onze virgule sept pour cent."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"U = E - rI, \qquad P_e = EI = P_f + P_J, \qquad \eta_g = \dfrac{U}{E}", font_size=25),
            ).arrange(DOWN, buff=0.22),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la loi d'Ohm du générateur s'écrit "
                "U égale E moins r I. La puissance engendrée E I se "
                "répartit entre la puissance fournie au circuit et la "
                "puissance perdue par effet Joule interne, et le rendement "
                "vaut U sur E."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas confondre E (f.é.m., en volts) et P_e = EI", font_size=20),
                Text("   (puissance, en watts) : E n'est PAS une puissance.", font_size=20),
                Text("• Le rendement d'un générateur diminue quand I augmente", font_size=20),
                Text("   (η_g = 1 - rI/E) : plus on tire de courant, plus les", font_size=20),
                Text("   pertes Joule internes pèsent relativement lourd.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Il ne faut pas confondre la f é m E, "
                "exprimée en volts, avec la puissance engendrée P e égale E "
                "I, exprimée en watts : E n'est pas une puissance. Et il "
                "faut retenir que le rendement d'un générateur diminue "
                "quand l'intensité débitée augmente : plus on tire de "
                "courant, plus les pertes Joule internes pèsent lourd dans "
                "le bilan."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
