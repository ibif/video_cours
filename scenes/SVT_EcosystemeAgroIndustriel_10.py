"""
scenes/SVT_EcosystemeAgroIndustriel_10.py — Chapitre 11 (1ereC, SVT), scène 10.

§ 4.4 Les pyramides écologiques : définition, tableau des 3 types
(nombres / biomasses / énergies) avec grandeur représentée et forme
habituelle, précision sur les pyramides parfois renversées vs la pyramide
des énergies toujours régulière, puis schéma de la pyramide des énergies
de la savane (valeurs de l'exemple résolu 1).
Source : 1ereC/SVT.pdf, page 126 (Figure 2).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Rectangle, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
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


def _etage(largeur, couleur, texte_gauche, texte_droite):
    rect = Rectangle(width=largeur, height=0.65, fill_color=couleur, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1.5)
    label = Text(texte_gauche, font_size=17, color="#1A1A1A", weight="BOLD")
    label.move_to(rect.get_center())
    valeur = Text(texte_droite, font_size=15, color=WHITE)
    valeur.next_to(rect, RIGHT, buff=0.3)
    return VGroup(rect, label, valeur)


class PyramidesEcologiques(NotionScene):
    def construct(self):
        titre = scene_title("4.4 — Les pyramides écologiques")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : définition ------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une pyramide écologique est la représentation "
                    "graphique, par rectangles superposés dont la largeur "
                    "est proportionnelle à la grandeur mesurée, des "
                    "quantités présentes à chaque niveau trophique.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.5,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Une pyramide écologique est la représentation graphique, "
                "par rectangles superposés dont la largeur est "
                "proportionnelle à la grandeur mesurée, des quantités "
                "présentes à chaque niveau trophique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les 3 types de pyramides --------------------------
        tab_titre = Text("Les trois types de pyramides écologiques", font_size=22, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.4)
        tableau = _bullets(
            [
                "Pyramide des nombres : nombre d'individus par niveau → généralement régulière, mais exceptions (un seul arbre nourrit des milliers d'insectes).",
                "Pyramide des biomasses : masse de matière vivante (kg/ha) → régulière sur terre ; parfois renversée en milieu aquatique (le phytoplancton se reproduit très vite).",
                "Pyramide des énergies : flux d'énergie (kJ/ha/an) → TOUJOURS régulière (base large, sommet étroit), car l'énergie diminue obligatoirement à chaque transfert.",
            ],
            font_size=18,
            width=60,
        )
        tableau.next_to(tab_titre, DOWN, buff=0.35)
        groupe_tab = VGroup(tab_titre, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Il existe trois types de pyramides. La pyramide des "
                "nombres représente le nombre d'individus par niveau : "
                "elle est généralement régulière, mais des exceptions "
                "existent, par exemple un seul arbre peut nourrir des "
                "milliers d'insectes. La pyramide des biomasses "
                "représente la masse de matière vivante par niveau, en "
                "kilogrammes par hectare : elle est régulière sur terre, "
                "mais parfois renversée en milieu aquatique, car le "
                "phytoplancton se reproduit si vite qu'une petite "
                "biomasse instantanée peut nourrir un zooplancton de "
                "biomasse supérieure. Enfin, la pyramide des énergies "
                "représente le flux d'énergie par niveau, en kilojoules "
                "par hectare et par an : elle est toujours régulière, car "
                "l'énergie diminue obligatoirement à chaque transfert, "
                "conformément à la loi de Lindeman."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- Exemple traité : pyramide des énergies de la savane --------------
        pyr_titre = Text("Pyramide des énergies de la savane", font_size=22, color=YELLOW, weight="BOLD")
        pyr_titre.next_to(titre, DOWN, buff=0.4)

        etage_p = _etage(8.5, "#2E7D32", "Producteurs (P)", "6×10⁷ kJ/ha/an")
        etage_c1 = _etage(6.2, "#66BB6A", "C1", "6×10⁶ kJ/ha/an")
        etage_c2 = _etage(3.9, "#FFEE58", "C2", "4,8×10⁵ kJ/ha/an")
        etage_c3 = _etage(2.0, "#EF5350", "C3", "3,4×10⁴ kJ/ha/an")

        pyramide = VGroup(etage_c3, etage_c2, etage_c1, etage_p).arrange(DOWN, buff=0.06, center=True)
        pyramide.next_to(pyr_titre, DOWN, buff=0.45)

        note_echelle = Text("(schéma symbolique — échelle non linéaire)", font_size=14, color="#888888")
        note_echelle.next_to(pyramide, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Reprenons les valeurs de notre exemple résolu sur la "
                "savane, et construisons la pyramide des énergies. À la "
                "base : les producteurs, six fois dix puissance sept "
                "kilojoules par hectare et par an. Au-dessus : les "
                "consommateurs primaires, six fois dix puissance six. "
                "Puis les consommateurs secondaires, quatre virgule huit "
                "fois dix puissance cinq. Et au sommet, les consommateurs "
                "tertiaires, environ trois virgule quatre fois dix "
                "puissance quatre. La forme est nettement pyramidale : "
                "base large, sommet étroit, exactement comme le prévoit la "
                "loi de Lindeman."
            )
        ) as tracker:
            self.play(FadeIn(pyr_titre))
            self.play(FadeIn(etage_p))
            self.play(FadeIn(etage_c1))
            self.play(FadeIn(etage_c2))
            self.play(FadeIn(etage_c3))
            self.play(FadeIn(note_echelle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pyr_titre), FadeOut(pyramide), FadeOut(note_echelle))

        # --- À retenir -------------------------------------------------------
        retenir = _bullets(
            [
                "Seule la pyramide des énergies est TOUJOURS régulière : elle ne peut jamais être renversée.",
                "Les pyramides des nombres ou des biomasses peuvent parfois être renversées.",
                "Une pyramide des énergies étroite au sommet illustre concrètement la perte d'énergie à chaque niveau.",
            ],
            font_size=21,
            width=54,
        )
        retenir_titre = Text("À retenir", font_size=25, color=YELLOW, weight="BOLD")
        retenir_titre.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(retenir_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : seule la pyramide des énergies est toujours "
                "régulière, elle ne peut jamais être renversée. Les "
                "pyramides des nombres ou des biomasses, elles, peuvent "
                "parfois l'être. Une pyramide des énergies étroite au "
                "sommet illustre très concrètement la perte d'énergie "
                "à chaque niveau trophique."
            )
        ) as tracker:
            self.play(FadeIn(retenir_titre))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir_titre), FadeOut(retenir))
