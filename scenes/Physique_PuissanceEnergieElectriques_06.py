"""
scenes/Physique_PuissanceEnergieElectriques_06.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 06.

§ Synthèse graphique. Mise en scène des deux caractéristiques U=f(I) :
générateur (droite décroissante, ordonnée E, pente -r) et récepteur
(droite croissante, ordonnée E', pente r'), tracées avec Axes. Tableau
récapitulatif des trois dipôles (conducteur ohmique, générateur,
récepteur) avec loi d'Ohm / puissance échangée / puissance utile /
puissance Joule / rendement.
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, synthèse § 4-5).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    Create,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class CaracteristiquesSynthese(NotionScene):
    def construct(self):
        titre = scene_title("Caractéristiques U=f(I) — synthèse")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Récapitulons visuellement les deux lois d'Ohm rencontrées : "
                "celle du générateur et celle du récepteur, en traçant "
                "leurs caractéristiques U en fonction de I sur un même type "
                "de graphique.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Récapitulons visuellement les deux lois d'Ohm rencontrées : "
                "celle du générateur et celle du récepteur, en traçant "
                "leurs caractéristiques, c'est-à-dire la tension U en "
                "fonction de l'intensité I."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : les deux droites -----------------------------------
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 14, 2],
            x_length=6.0,
            y_length=4.2,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.4)

        E, r = 12, 1.2
        Eprime, rprime = 2, 1.6
        droite_gen = axes.plot(lambda i: max(E - r * i, 0), x_range=[0, 5], color=YELLOW)
        droite_rec = axes.plot(lambda i: Eprime + rprime * i, x_range=[0, 5], color=RED)

        x_lab = MathTex("I \\ (\\text{A})", font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.15)
        y_lab = MathTex("U \\ (\\text{V})", font_size=22).next_to(axes.y_axis.get_end(), UP, buff=0.1)

        legende = VGroup(
            VGroup(MathTex(r"U = E - rI", font_size=26, color=YELLOW), Text("générateur (décroissante)", font_size=18)).arrange(DOWN, buff=0.1),
            VGroup(MathTex(r"U = E' + r'I", font_size=26, color=RED), Text("récepteur (croissante)", font_size=18)).arrange(DOWN, buff=0.1),
        ).arrange(DOWN, buff=0.35)
        legende.next_to(axes, RIGHT, buff=0.5)

        graphe = VGroup(axes, x_lab, y_lab)

        with self.voiceover(
            text=(
                "Sur ce graphique, la caractéristique du générateur, U "
                "égale E moins r I, est une droite décroissante : elle part "
                "de l'ordonnée E, quand I est nul, et descend avec une "
                "pente négative égale à moins r. À l'inverse, la "
                "caractéristique du récepteur, U égale E prime plus r "
                "prime I, est une droite croissante : elle part de "
                "l'ordonnée E prime et monte avec une pente positive égale "
                "à r prime."
            )
        ) as tracker:
            self.play(Create(axes), Write(x_lab), Write(y_lab))
            self.play(Create(droite_gen), FadeIn(legende[0]))
            self.play(Create(droite_rec), FadeIn(legende[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe), FadeOut(legende), FadeOut(droite_gen), FadeOut(droite_rec))

        # --- Exemple : lecture du graphe (point de fonctionnement) ---------------
        exemple_txt = property_box(
            VGroup(
                Text("Le point d'intersection des deux droites donne le point de", font_size=20),
                Text("fonctionnement du circuit : l'intensité I et la tension U", font_size=20),
                Text("communes au générateur et au récepteur qui se débitent", font_size=20),
                Text("mutuellement leur courant (utilisé en loi de Pouillet).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        exemple_txt.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une lecture utile de ce graphique : le point d'intersection "
                "des deux droites donne le point de fonctionnement réel du "
                "circuit, c'est-à-dire l'intensité et la tension communes "
                "au générateur et au récepteur reliés ensemble. C'est "
                "exactement cette idée que nous retrouverons avec la loi de "
                "Pouillet."
            )
        ) as tracker:
            self.play(FadeIn(exemple_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_txt))

        # --- Tableau récapitulatif des trois dipôles ------------------------------
        col1 = VGroup(
            Text("Dipôle", font_size=19, weight="BOLD"),
            Text("Conducteur ohmique", font_size=18),
            Text("Générateur", font_size=18),
            Text("Récepteur", font_size=18),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        col2 = VGroup(
            Text("Loi d'Ohm", font_size=19, weight="BOLD"),
            MathTex("U=RI", font_size=20),
            MathTex("U=E-rI", font_size=20),
            MathTex("U=E'+r'I", font_size=20),
        ).arrange(DOWN, buff=0.28)

        col3 = VGroup(
            Text("P. échangée", font_size=19, weight="BOLD"),
            MathTex("P=UI", font_size=20),
            MathTex("P_e=EI", font_size=20),
            MathTex("P_r=UI", font_size=20),
        ).arrange(DOWN, buff=0.28)

        col4 = VGroup(
            Text("P. utile", font_size=19, weight="BOLD"),
            Text("—", font_size=18),
            MathTex("P_f=UI", font_size=20),
            MathTex("P_u=E'I", font_size=20),
        ).arrange(DOWN, buff=0.28)

        col5 = VGroup(
            Text("Rendement", font_size=19, weight="BOLD"),
            Text("—", font_size=18),
            MathTex("\\eta_g=U/E", font_size=20),
            MathTex("\\eta_r=E'/U", font_size=20),
        ).arrange(DOWN, buff=0.28)

        tableau = VGroup(col1, col2, col3, col4, col5).arrange(RIGHT, buff=0.55, aligned_edge=UP)
        tableau_box = property_box(tableau, box_width=12.8)
        tableau_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le tableau récapitulatif des trois dipôles étudiés. "
                "Le conducteur ohmique suit U égale R I, échange une "
                "puissance U I, entièrement dissipée par effet Joule : il "
                "n'a ni puissance utile ni rendement à proprement parler. "
                "Le générateur suit U égale E moins r I, engendre E I, en "
                "fournit U I, avec un rendement U sur E. Le récepteur suit "
                "U égale E prime plus r prime I, reçoit U I, en utilise E "
                "prime I, avec un rendement E prime sur U."
            )
        ) as tracker:
            self.play(FadeIn(tableau_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_box))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Générateur : droite décroissante U=E-rI (ordonnée E, pente -r).", font_size=20),
                Text("Récepteur : droite croissante U=E'+r'I (ordonnée E', pente r').", font_size=20),
                Text("Rendements : η_g = U/E (générateur), η_r = E'/U (récepteur).", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la caractéristique du générateur "
                "est une droite décroissante, celle du récepteur une droite "
                "croissante. Le rendement du générateur vaut U sur E, celui "
                "du récepteur vaut E prime sur U — deux formules à ne "
                "jamais confondre."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas confondre les deux droites : celle qui MONTE", font_size=20),
                Text("   est le récepteur, celle qui DESCEND est le générateur.", font_size=20),
                Text("• L'ordonnée à l'origine donne E ou E' ; la valeur absolue", font_size=20),
                Text("   de la pente donne r ou r' — ne pas inverser les deux.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges de lecture graphique à éviter. Il ne faut pas "
                "confondre les deux droites : celle qui monte est le "
                "récepteur, celle qui descend est le générateur. Et sur "
                "chaque droite, l'ordonnée à l'origine donne la f é m ou la "
                "f c é m, tandis que la valeur absolue de la pente donne la "
                "résistance interne : il ne faut jamais inverser les deux."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
