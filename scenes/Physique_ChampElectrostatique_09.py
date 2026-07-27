"""
scenes/Physique_ChampElectrostatique_09.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 09.

§ Méthodes et astuces (première partie) : (1) déterminer le champ
résultant créé par plusieurs charges (schéma, tracer chaque vecteur,
calculer chaque norme, additionner vectoriellement) ; (2) trouver un
point de champ nul (repérer les zones de sens opposés, égalité des
normes, résoudre) ; (3) étudier l'équilibre d'une bille chargée suspendue
(bilan des forces, projection, tan α = F/P).
Source : 1ereC/Physique.pdf, pages 54-65 (chapitre 6, méthodes).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    BLUE,
    Arrow,
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
from shapes.boxes import essentiel_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MethodesChampElectrostatique(NotionScene):
    def construct(self):
        titre = scene_title("Méthodes et astuces — champ électrostatique")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : trois méthodes à maîtriser ------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Trois types d'exercices reviennent très souvent sur le "
                "champ électrostatique : trouver un champ résultant, "
                "trouver un point de champ nul, et étudier l'équilibre "
                "d'une bille chargée. Voici la méthode pour chacun.",
                width=54,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois types d'exercices reviennent très souvent sur le "
                "champ électrostatique : déterminer un champ résultant, "
                "trouver un point de champ nul, et étudier l'équilibre "
                "d'une bille chargée suspendue. Voyons la méthode pour "
                "chacun."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Méthode 1 : champ résultant de plusieurs charges -----------------------
        methode1 = method_box(
            VGroup(
                Text("Déterminer le champ résultant de plusieurs charges", font_size=21, weight="BOLD"),
                Text("1. Faire un schéma : position des charges et du point M.", font_size=19),
                Text("2. Tracer chaque vecteur E⃗_i en M (sens selon le signe", font_size=19),
                Text("    de la charge source, direction = droite charge-M).", font_size=19),
                Text("3. Calculer chaque norme E_i = k|Q_i|/r_i².", font_size=19),
                Text("4. Additionner VECTORIELLEMENT (géométrie ou coordonnées)", font_size=19),
                Text("    pour obtenir E⃗ résultant.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.2,
        )
        methode1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Première méthode : déterminer le champ résultant créé "
                "par plusieurs charges en un point M. On commence par "
                "faire un schéma avec la position de chaque charge et du "
                "point M. On trace ensuite chaque vecteur champ E indice "
                "i en M, avec le sens qui dépend du signe de la charge "
                "source. On calcule la norme de chacun avec la formule k "
                "Q sur r carré. Enfin, on additionne vectoriellement tous "
                "ces vecteurs, par une construction géométrique ou par "
                "leurs coordonnées, pour obtenir le champ résultant."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : trouver un point de champ nul -------------------------------
        methode2 = method_box(
            VGroup(
                Text("Trouver un point de champ nul", font_size=21, weight="BOLD"),
                Text("1. Repérer la zone où les champs créés par chaque", font_size=19),
                Text("    charge peuvent être de sens OPPOSÉS.", font_size=19),
                Text("2. Écrire l'égalité des normes : E₁(x) = E₂(x).", font_size=19),
                Text("3. Résoudre cette équation pour trouver la position x", font_size=19),
                Text("    du point cherché.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=11.6,
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : trouver un point où le champ "
                "résultant est nul. On repère d'abord la zone de "
                "l'espace où les champs créés par chaque charge peuvent "
                "être de sens opposés, seule zone où une annulation est "
                "possible. On écrit ensuite l'égalité de leurs normes, E "
                "un de x égale E deux de x, puis on résout cette "
                "équation pour trouver la position x du point cherché."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Méthode 3 : équilibre d'une bille chargée suspendue --------------------
        fil = Line(UP * 1.2, UP * 1.2 + RIGHT * 0.8 + DOWN * 1.2, color=WHITE, stroke_width=1.5)
        bille = Dot(fil.get_end(), color=YELLOW, radius=0.14)
        poids = Arrow(bille.get_center(), bille.get_center() + DOWN * 0.9, buff=0.1, color=RED, stroke_width=2.5)
        poids_label = MathTex("P", font_size=20, color=RED).next_to(poids, RIGHT, buff=0.1)
        tension = Arrow(bille.get_center(), fil.get_start(), buff=0.1, color=BLUE, stroke_width=2.5)
        tension_label = MathTex("T", font_size=20, color=BLUE).next_to(tension, LEFT, buff=0.1)
        force_e = Arrow(bille.get_center(), bille.get_center() + RIGHT * 0.9, buff=0.1, color="#288073", stroke_width=2.5)
        force_e_label = MathTex("F", font_size=20, color="#288073").next_to(force_e, DOWN, buff=0.1)
        alpha_label = MathTex(r"\alpha", font_size=20).next_to(fil.get_start(), DOWN + RIGHT, buff=0.15)
        schema3 = VGroup(fil, bille, poids, poids_label, tension, tension_label, force_e, force_e_label, alpha_label)
        schema3.move_to(LEFT * 3.3 + UP * 0.2)

        methode3_texte = VGroup(
            Text("Équilibre d'une bille chargée suspendue", font_size=20, weight="BOLD"),
            Text("1. Bilan des forces : poids P⃗, tension T⃗ du fil,", font_size=18),
            Text("    force électrique F⃗ = qE⃗.", font_size=18),
            Text("2. Projeter sur les axes horizontal/vertical.", font_size=18),
            MathTex(r"3.\ \tan\alpha = \dfrac{F}{P}", font_size=22),
            Text("   (α : angle du fil avec la verticale à l'équilibre).", font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        methode3_texte.next_to(schema3, RIGHT, buff=0.7)

        methode3 = method_box(VGroup(schema3, methode3_texte).arrange(RIGHT, buff=0.5), box_width=12.6)
        methode3.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Troisième méthode : étudier l'équilibre d'une bille "
                "chargée suspendue dans un champ uniforme horizontal. On "
                "fait le bilan des trois forces : le poids P, la tension "
                "T du fil, et la force électrique F égale q E. On projette "
                "ensuite ces forces sur les axes horizontal et vertical. À "
                "l'équilibre, on obtient une relation simple entre "
                "l'angle alpha que fait le fil avec la verticale, la "
                "force électrique et le poids : tangente de alpha égale F "
                "sur P."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- À retenir : les trois méthodes en un coup d'œil ---------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Champ résultant : schéma → vecteurs → normes → somme vectorielle.", font_size=19),
                Text("Point de champ nul : sens opposés → égalité des normes → résoudre.", font_size=19),
                MathTex(r"\text{Bille suspendue à l'équilibre : } \tan\alpha = F/P", font_size=21),
            ).arrange(DOWN, buff=0.22),
            box_width=12.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de ces trois méthodes. Pour un "
                "champ résultant : schéma, vecteurs, normes, puis somme "
                "vectorielle. Pour un point de champ nul : repérer les "
                "sens opposés, égaler les normes, puis résoudre. Pour une "
                "bille suspendue à l'équilibre dans un champ uniforme : "
                "tangente de alpha égale F sur P."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
