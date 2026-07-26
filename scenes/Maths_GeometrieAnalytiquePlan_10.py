"""
scenes/Maths_GeometrieAnalytiquePlan_10.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 10.

§ Intersection droite-cercle (méthode géométrique : comparer d et r ;
méthode algébrique : substitution + discriminant), axe radical de deux
cercles (soustraction des équations). Théorème tangente en A :
perpendiculaire au rayon (ΩA), avec démonstration. Corollaire : équation de
la tangente par dédoublement. Exemple résolu : tangente au cercle
x²+y²-2x+4y-20=0 en A(4;2) → 3x+4y-20=0. Mention des tangentes menées d'un
point extérieur.
Source : 1ereC/Maths.pdf, chapitre 14, pages 173-174.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, Circle, Create, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class IntersectionTangenteCercle(NotionScene):
    def construct(self):
        titre = scene_title("Intersection droite-cercle et tangente")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé : position relative droite / cercle ---------------------------
        c1 = Circle(radius=1.0, color="#1E5FA8").move_to(LEFT * 4.6 + DOWN * 1.2)
        d1 = Line(c1.get_center() + LEFT * 1.6 + DOWN * 1.7, c1.get_center() + RIGHT * 1.6 + UP * 1.7, color=WHITE).move_to(c1.get_center() + RIGHT * 1.7)
        l1 = Text("extérieure (d>r)", font_size=16).next_to(VGroup(c1, d1), DOWN, buff=0.15)

        c2 = Circle(radius=1.0, color="#1E5FA8").move_to(DOWN * 1.2)
        d2 = Line(LEFT * 1.4, RIGHT * 1.4, color=WHITE).move_to(c2.get_center() + UP * 1.0)
        l2 = Text("tangente (d=r)", font_size=16).next_to(VGroup(c2, d2), DOWN, buff=0.15)

        c3 = Circle(radius=1.0, color="#1E5FA8").move_to(RIGHT * 4.6 + DOWN * 1.2)
        d3 = Line(LEFT * 1.4, RIGHT * 1.4, color=WHITE).move_to(c3.get_center())
        l3 = Text("sécante (d<r)", font_size=16).next_to(VGroup(c3, d3), DOWN, buff=0.15)

        schema = VGroup(c1, d1, l1, c2, d2, l2, c3, d3, l3)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Comment étudier la position relative d'une droite et d'un "
                "cercle de rayon r ? La méthode géométrique consiste à "
                "comparer la distance d du centre du cercle à la droite, "
                "avec le rayon r. Si d est supérieur à r, la droite est "
                "extérieure au cercle : aucune intersection. Si d est égal "
                "à r, la droite est tangente : un seul point commun. Si d "
                "est inférieur à r, la droite est sécante : deux points "
                "d'intersection."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        methode_algebrique = method_box(
            VGroup(
                Text("Méthode algébrique", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "Substituer l'équation réduite (ou paramétrique) de "
                        "la droite dans l'équation du cercle : on obtient "
                        "une équation du second degré dont le discriminant "
                        "Δ donne le nombre de solutions (0, 1 ou 2).",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        methode_algebrique.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La méthode algébrique, elle, consiste à substituer "
                "l'équation de la droite — réduite ou paramétrique — dans "
                "l'équation du cercle. On obtient une équation du second "
                "degré en x, dont le discriminant delta indique directement "
                "le nombre de points d'intersection : zéro, un ou deux "
                "points, selon le signe de delta."
            )
        ) as tracker:
            self.play(FadeIn(methode_algebrique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_algebrique))

        # --- Axe radical -----------------------------------------------------------
        axe_radical = definition_box(
            VGroup(
                Text("Axe radical de deux cercles", font_size=22, weight="BOLD"),
                MathTex(
                    r"\mathcal{C}: x^2+y^2+ux+vy+w=0"
                    r"\qquad \mathcal{C}': x^2+y^2+u'x+v'y+w'=0"
                    r"\\[4pt]"
                    r"\mathcal{C}-\mathcal{C}': (u-u')x+(v-v')y+(w-w')=0",
                    font_size=21,
                ),
                Text(
                    "Cette soustraction élimine x² et y² : c'est l'équation d'une droite.",
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.2,
        )
        axe_radical.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour étudier l'intersection de deux cercles, une astuce "
                "efficace : soustraire les deux équations développées. Les "
                "termes x carré et y carré s'annulent, et il ne reste "
                "qu'une équation de droite, appelée axe radical des deux "
                "cercles. Les points communs éventuels des deux cercles "
                "sont alors les intersections de cet axe avec l'un des deux "
                "cercles — on est ramené au cas droite-cercle."
            )
        ) as tracker:
            self.play(FadeIn(axe_radical))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(axe_radical))

        # --- Raisonnement : tangente, théorème + démonstration --------------------
        theoreme_tangente = theorem_box(
            VGroup(
                Text("Tangente à un cercle en un point A du cercle", font_size=21, weight="BOLD"),
                MathTex(
                    r"A \in \mathcal{C}(\Omega,r) \ \Rightarrow\ "
                    r"\mathcal{T}_A \perp (\Omega A) \ \text{en } A",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.0,
        )
        theoreme_tangente.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Passons à la tangente. Si A est un point du cercle de "
                "centre oméga et de rayon r, la tangente au cercle en A est "
                "la droite passant par A et perpendiculaire au rayon "
                "oméga-A."
            )
        ) as tracker:
            self.play(FadeIn(theoreme_tangente))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme_tangente))

        demo_tangente = Text(
            _wrap(
                "Démonstration : pour tout point M de la tangente distinct "
                "de A, le triangle ΩAM est rectangle en A, donc ΩM>ΩA=r : "
                "M est extérieur au cercle. La tangente ne coupe donc le "
                "cercle qu'en A, ce qui la caractérise.",
                width=54,
            ),
            font_size=22,
        )
        demo_tangente.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici pourquoi : pour tout point M de cette perpendiculaire "
                "distinct de A, le triangle oméga-A-M est rectangle en A, "
                "donc par Pythagore, oméga-M est strictement supérieur à "
                "oméga-A, qui vaut r. Le point M est donc à l'extérieur du "
                "cercle. Cette droite ne touche donc le cercle qu'au seul "
                "point A : c'est bien la tangente."
            )
        ) as tracker:
            self.play(FadeIn(demo_tangente))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_tangente))

        corollaire = method_box(
            VGroup(
                Text("Équation de la tangente (dédoublement)", font_size=21, weight="BOLD"),
                MathTex(
                    r"\mathcal{C}: x^2+y^2+ux+vy+w=0,\ A(x_A;y_A)\in\mathcal{C}"
                    r"\\[4pt]"
                    r"\mathcal{T}_A: xx_A+yy_A+u\dfrac{x+x_A}{2}+v\dfrac{y+y_A}{2}+w=0",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.5,
        )
        corollaire.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En pratique, on utilise une règle de dédoublement pour "
                "écrire directement l'équation de la tangente : on "
                "remplace x carré par x fois x-A, y carré par y fois y-A, "
                "et x par x plus x-A sur 2, y par y plus y-A sur 2, dans "
                "l'équation développée du cercle."
            )
        ) as tracker:
            self.play(FadeIn(corollaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corollaire))

        # --- Exemple traité ---------------------------------------------------
        exemple = example_box(
            MathTex(
                r"\mathcal{C}: x^2+y^2-2x+4y-20=0\ (u=-2,v=4,w=-20),\ A(4;2)"
                r"\\[5pt]"
                r"\text{Vérif.: } 16+4-8+8-20=0 \ \checkmark \ (A\in\mathcal{C})"
                r"\\[4pt]"
                r"\mathcal{T}_A:\ 4x+2y-2\cdot\dfrac{x+4}{2}+4\cdot\dfrac{y+2}{2}-20=0"
                r"\\[4pt]"
                r"\Leftrightarrow\ 4x+2y-(x+4)+2(y+2)-20=0"
                r"\\[4pt]"
                r"\Leftrightarrow\ 3x+4y-20=0",
                font_size=19,
            ),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple complet : cherchons la tangente au cercle x carré "
                "plus y carré moins 2x plus 4y moins 20 égale zéro, au "
                "point A de coordonnées 4 et 2. On vérifie d'abord que A "
                "appartient bien au cercle : 16 plus 4 moins 8 plus 8 moins "
                "20 égale zéro, c'est confirmé. En appliquant le "
                "dédoublement puis en simplifiant, on obtient l'équation de "
                "la tangente : 3x plus 4y moins 20 égale zéro."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        mention_exterieur = warning_box(
            Text(
                _wrap(
                    "Depuis un point P EXTÉRIEUR au cercle, il existe "
                    "exactement deux tangentes au cercle passant par P "
                    "(non traitées en détail ici) ; depuis un point "
                    "intérieur, aucune tangente ne passe par ce point.",
                    width=50,
                ),
                font_size=21,
            ),
        )
        mention_exterieur.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mention importante pour la suite : depuis un point P "
                "extérieur au cercle, il existe exactement deux tangentes "
                "au cercle qui passent par P — nous ne détaillerons pas "
                "leur construction ici. En revanche, depuis un point "
                "intérieur au cercle, aucune tangente ne peut passer par ce "
                "point."
            )
        ) as tracker:
            self.play(FadeIn(mention_exterieur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mention_exterieur))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                Text("d>r extérieure  |  d=r tangente  |  d<r sécante", font_size=22),
                MathTex(r"A\in\mathcal{C}(\Omega,r) \ \Rightarrow\ \mathcal{T}_A \perp (\Omega A)", font_size=25),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : comparez toujours d et r pour la position "
                "relative droite-cercle, et souvenez-vous que la tangente "
                "en un point du cercle est perpendiculaire au rayon en ce "
                "point."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Avant d'écrire l'équation de la tangente en un point A "
                    "« du cercle », vérifiez TOUJOURS que A appartient "
                    "réellement au cercle (remplacer dans l'équation) — "
                    "sinon la droite obtenue n'est pas une tangente, et un "
                    "point intérieur n'admet aucune tangente qui passe par lui.",
                    width=50,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à ne surtout pas oublier : avant d'écrire l'équation "
                "de la tangente en un point A supposé sur le cercle, "
                "vérifiez toujours que A appartient réellement au cercle en "
                "remplaçant ses coordonnées dans l'équation. Si ce n'est "
                "pas le cas, la droite obtenue par dédoublement n'est pas "
                "une tangente, et un point strictement intérieur au cercle "
                "n'admet, de toute façon, aucune tangente qui passe par "
                "lui."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
