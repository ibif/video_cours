"""
scenes/Physique_PuissanceEnergieElectriques_05.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 05.

§ 5. Bilan énergétique d'un récepteur (transforme l'énergie électrique en
une autre forme : mécanique pour un moteur, chimique pour un
électrolyseur). F.c.é.m. E' et résistance interne r'. Loi d'Ohm du
récepteur U=E'+r'I (caractéristique croissante). Bilan des puissances :
P_r=UI (reçue), P_u=E'I (utile), P_J=r'I² (perdue), P_r=P_u+P_J.
Rendement η_r=E'/U. Cas particulier du moteur calé (E'=0, tout en
chaleur, risque de destruction — fusibles/disjoncteurs). Exemple résolu :
E'=6 V, r'=1 Ω, U=9 V → I=3 A, P_r=27 W, P_u=18 W, P_J=9 W, η≈66,7 %.
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 5).
"""

import textwrap

from manim import DOWN, LEFT, RED, RIGHT, UP, WHITE, YELLOW, Circle, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _recepteur_schema():
    """Moteur (cercle 'M') traversé par un courant, avec les flèches I et
    U de SENS OPPOSÉS (convention récepteur)."""
    moteur = Circle(radius=0.5, color=WHITE, stroke_width=3)
    label_m = Text("M", font_size=26, color=WHITE, weight="BOLD").move_to(moteur.get_center())

    fil_g = Line(moteur.get_left() + LEFT * 1.6, moteur.get_left(), stroke_width=3, color=WHITE)
    fil_d = Line(moteur.get_right(), moteur.get_right() + RIGHT * 1.6, stroke_width=3, color=WHITE)

    fleche_I = Line(moteur.get_left() + LEFT * 1.3, moteur.get_left() + LEFT * 0.3, stroke_width=3, color=YELLOW)
    fleche_I_tip = Text("→", font_size=22, color=YELLOW).move_to(moteur.get_left() + LEFT * 0.2)
    label_I = Text("I", font_size=22, color=YELLOW).next_to(fleche_I, UP, buff=0.08)

    fleche_U = Line(moteur.get_right() + RIGHT * 0.3, moteur.get_right() + RIGHT * 1.3, stroke_width=3, color=RED)
    fleche_U_tip = Text("←", font_size=22, color=RED).move_to(moteur.get_right() + RIGHT * 0.35)
    label_U = Text("U", font_size=22, color=RED).next_to(fleche_U, DOWN, buff=0.5)

    return VGroup(fil_g, moteur, label_m, fil_d, fleche_I, fleche_I_tip, label_I, fleche_U_tip, label_U)


class BilanRecepteur(NotionScene):
    def construct(self):
        titre = scene_title("Bilan énergétique d'un récepteur")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Un moteur électrique transforme de l'énergie électrique en "
                "énergie mécanique, mais pas intégralement : lui aussi "
                "chauffe. Comment décrire ce dipôle récepteur, et quantifier "
                "la part réellement utile de l'énergie reçue ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un moteur électrique transforme de l'énergie électrique en "
                "énergie mécanique, mais pas intégralement : lui aussi "
                "chauffe pendant son fonctionnement. Comment décrire ce "
                "dipôle récepteur, et quantifier la part réellement utile "
                "de l'énergie qu'il reçoit ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- f.c.é.m., résistance interne, loi d'Ohm récepteur -------------------
        schema = _recepteur_schema()
        schema.next_to(titre, DOWN, buff=0.55)

        definition_Eprime = definition_box(
            VGroup(
                Text("Un récepteur transforme l'énergie électrique en une", font_size=20),
                Text("autre forme : mécanique (moteur), chimique (électrolyseur).", font_size=20),
                Text("Il est caractérisé par sa force contre-électromotrice", font_size=20),
                Text("(f.c.é.m.) E' et sa résistance interne r'.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.4,
        )
        definition_Eprime.next_to(schema, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Un récepteur, comme un moteur ou un électrolyseur, "
                "transforme l'énergie électrique reçue en une autre forme "
                "d'énergie : mécanique pour un moteur, chimique pour un "
                "électrolyseur. Il est caractérisé par sa force "
                "contre-électromotrice, notée E prime, et sa résistance "
                "interne, notée r prime. En convention récepteur, les "
                "flèches I et U sont de sens opposés, comme sur ce schéma."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(definition_Eprime))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(definition_Eprime))

        loi_ohm_rec = theorem_box(
            VGroup(
                Text("Loi d'Ohm du récepteur", font_size=23, weight="BOLD"),
                MathTex(r"U = E' + r' I", font_size=32),
                Text("Caractéristique U=f(I) : droite CROISSANTE,", font_size=20),
                Text("d'ordonnée à l'origine E' et de pente r'.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=10.8,
        )
        loi_ohm_rec.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La loi d'Ohm du récepteur s'écrit U égale E prime plus r "
                "prime I : la tension à ses bornes augmente avec "
                "l'intensité. Sur un graphique U en fonction de I, on "
                "obtient une droite croissante, d'ordonnée à l'origine E "
                "prime et de pente r prime."
            )
        ) as tracker:
            self.play(FadeIn(loi_ohm_rec))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi_ohm_rec))

        # --- Bilan des puissances --------------------------------------------------
        bilan = VGroup(
            Text("En multipliant U = E' + r'I par I :", font_size=21),
            MathTex(r"U I = E' I + r' I^2", font_size=28),
            MathTex(r"P_r = U I \quad (\text{puissance reçue})", font_size=25),
            MathTex(r"P_u = E' I \quad (\text{puissance utile})", font_size=25),
            MathTex(r"P_J = r' I^2 \quad (\text{puissance perdue par effet Joule})", font_size=25),
            MathTex(r"P_r = P_u + P_J", font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.16)
        bilan.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Multiplions la loi d'Ohm du récepteur par l'intensité I : "
                "U I égale E prime I plus r prime I carré. U I est la "
                "puissance reçue par le récepteur, notée P r. E prime I est "
                "la puissance réellement utile, transformée en énergie "
                "mécanique ou chimique, notée P u. Et r prime I carré est "
                "la puissance perdue par effet Joule, notée P J. Le bilan "
                "s'écrit : P r égale P u plus P J."
            )
        ) as tracker:
            self.play(FadeIn(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bilan))

        # --- Rendement + moteur calé -----------------------------------------------
        rendement = definition_box(
            VGroup(
                Text("Rendement du récepteur", font_size=23, weight="BOLD"),
                MathTex(r"\eta_r = \dfrac{P_u}{P_r} = \dfrac{E'}{U}", font_size=28),
            ).arrange(DOWN, buff=0.2),
            box_width=9.0,
        )
        rendement.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le rendement du récepteur, noté êta indice r, est le "
                "rapport de la puissance utile sur la puissance reçue : "
                "êta r égale P u sur P r, ce qui se simplifie en E prime "
                "sur U."
            )
        ) as tracker:
            self.play(FadeIn(rendement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rendement))

        moteur_cale = warning_box(
            VGroup(
                Text("Cas particulier : moteur CALÉ (bloqué, immobile).", font_size=21),
                Text("Alors E' = 0 : toute l'énergie reçue part en chaleur", font_size=21),
                Text("(P_J = P_r), d'où un risque de destruction du moteur.", font_size=21),
                Text("→ D'où l'utilité des fusibles et disjoncteurs de protection.", font_size=21),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        moteur_cale.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cas particulier important : un moteur calé, c'est-à-dire "
                "bloqué et immobile, a une f c é m E prime nulle, puisqu'il "
                "ne fournit plus aucun travail mécanique. Toute l'énergie "
                "reçue part alors intégralement en chaleur, ce qui peut "
                "détruire le moteur par échauffement excessif. C'est pour "
                "cette raison que les circuits sont protégés par des "
                "fusibles et des disjoncteurs."
            )
        ) as tracker:
            self.play(FadeIn(moteur_cale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(moteur_cale))

        # --- Exemple résolu 4 -------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Moteur E' = 6 V, r' = 1 Ω, alimenté sous U = 9 V.", font_size=20),
                MathTex(r"U = E' + r'I \Rightarrow I = \dfrac{U - E'}{r'} = \dfrac{9-6}{1} = 3\ \text{A}", font_size=25),
                MathTex(r"P_r = UI = 27\ \text{W}, \quad P_u = E'I = 18\ \text{W}, \quad P_J = r'I^2 = 9\ \text{W}", font_size=22),
                MathTex(r"\eta_r = \dfrac{18}{27} \approx 66{,}7\ \%", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=12.4,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : un moteur de f c é m six volts et de "
                "résistance interne un ohm est alimenté sous une tension de "
                "neuf volts. La loi d'Ohm du récepteur donne l'intensité : "
                "I égale U moins E prime, sur r prime, soit trois ampères. "
                "La puissance reçue vaut U I, vingt-sept watts ; la "
                "puissance utile vaut E prime I, dix-huit watts ; la "
                "puissance perdue par effet Joule vaut r prime I carré, "
                "neuf watts. Le rendement vaut dix-huit sur vingt-sept, "
                "environ soixante-six virgule sept pour cent."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"U = E' + r'I, \qquad P_r = UI = P_u + P_J, \qquad \eta_r = \dfrac{E'}{U}", font_size=24),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la loi d'Ohm du récepteur s'écrit U "
                "égale E prime plus r prime I. La puissance reçue U I se "
                "répartit entre la puissance utile et la puissance perdue "
                "par effet Joule, et le rendement vaut E prime sur U."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas confondre le rendement du récepteur (η_r = E'/U)", font_size=20),
                Text("   avec celui du générateur (η_g = U/E) : la formule", font_size=20),
                Text("   s'inverse selon le type de dipôle !", font_size=20),
                Text("• Pour un récepteur, U est TOUJOURS supérieure à E'", font_size=20),
                Text("   (sinon le courant ne pourrait pas circuler).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Il ne faut pas confondre le "
                "rendement du récepteur, E prime sur U, avec celui du "
                "générateur, U sur E : la formule s'inverse selon le type "
                "de dipôle, il faut toujours vérifier lequel des deux on "
                "étudie. Et pour un récepteur, la tension U est toujours "
                "supérieure à la f c é m E prime, sinon aucun courant ne "
                "pourrait circuler."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
