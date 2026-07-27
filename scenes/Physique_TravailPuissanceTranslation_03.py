"""
scenes/Physique_TravailPuissanceTranslation_03.py — Chapitre 1 « Travail et
puissance dans le cas d'un mouvement de translation » (1ereC, Physique),
scène 03.

§ Travail du poids : repère (O ; i⃗,j⃗,k⃗) d'axe vertical ascendant,
P⃗ = mg⃗ = -mg k⃗, démonstration W_AB(P⃗) = mg(z_A - z_B) = ±mgh avec
h = |z_A - z_B|, convention de signe (descend → moteur positif, monte →
résistant négatif), indépendance du chemin suivi, travail nul sur un
trajet fermé. Exemple résolu 2 : maçon montant un seau de 15 kg sur 2,5 m,
puis redescendant un seau vide de 2 kg (g = 10 N/kg).
Source : 1ereC/Physique.pdf, chapitre 1, pages 4-12.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Square,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import (
    corrige_box,
    definition_box,
    essentiel_box,
    exercise_box,
    scene_title,
    theorem_box,
    warning_box,
)


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


POIDS_COLOR = "#1E5FA8"
DEPLACEMENT_COLOR = "#288073"


class TravailDuPoids(NotionScene):
    def construct(self):
        titre = scene_title("Travail du poids")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ----------------------------------------------
        axe = Line(DOWN * 1.8, UP * 1.8, color="#FFFFFF")
        fleche_axe = Vector(UP * 0.5, color="#FFFFFF").next_to(axe, UP, buff=0)
        label_k = MathTex(r"\vec{k}", font_size=24, color="#FFFFFF").next_to(fleche_axe, RIGHT, buff=0.1)
        point_a = DOWN * 1.3
        point_b = UP * 1.0
        seau_a = Square(side_length=0.35, color=YELLOW, fill_color=YELLOW, fill_opacity=0.8)
        seau_a.move_to(point_a + RIGHT * 0.6)
        seau_b = Square(side_length=0.35, color=YELLOW, fill_color=YELLOW, fill_opacity=0.4)
        seau_b.move_to(point_b + RIGHT * 0.6)
        poids_vec = Vector(DOWN * 0.7, color=POIDS_COLOR).move_to(seau_a.get_center() + DOWN * 0.5)
        label_poids = MathTex(r"\vec{P}", font_size=24, color=POIDS_COLOR).next_to(poids_vec, RIGHT, buff=0.1)
        label_a = MathTex("A", font_size=24).next_to(seau_a, LEFT, buff=0.2)
        label_b = MathTex("B", font_size=24).next_to(seau_b, LEFT, buff=0.2)
        deplacement = Vector(point_b - point_a, color=DEPLACEMENT_COLOR).shift(point_a + RIGHT * 1.4)

        figure = VGroup(
            axe, fleche_axe, label_k, seau_a, seau_b, poids_vec, label_poids,
            label_a, label_b, deplacement,
        )
        figure.scale(0.9).move_to(ORIGIN).shift(DOWN * 0.2)

        mise_en_situation = Text(
            _wrap(
                "Un maçon monte un seau de mortier le long d'un "
                "échafaudage. Le poids du seau s'oppose-t-il, ou "
                "favorise-t-il, ce mouvement ?",
                width=54,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Un maçon monte un seau de mortier le long d'un "
                "échafaudage. Le poids du seau s'oppose-t-il à ce "
                "mouvement, ou favorise-t-il au contraire ? Étudions "
                "précisément le travail du poids."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(figure))

        # --- Raisonnement : démonstration ---------------------------------------------
        setup = definition_box(
            VGroup(
                Text("Repère (O ; i⃗, j⃗, k⃗), axe k⃗ vertical ascendant", font_size=23, weight="BOLD"),
                MathTex(r"\vec{P} = m\vec{g} = -mg\,\vec{k}", font_size=27),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        setup.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On se place dans un repère d'origine O, muni des vecteurs "
                "i, j, k, où k vecteur est l'axe vertical dirigé vers le "
                "haut. Le poids s'écrit alors P vecteur égale m fois g "
                "vecteur, égale moins m g fois k vecteur : il pointe "
                "toujours vers le bas, quel que soit le mouvement de "
                "l'objet."
            )
        ) as tracker:
            self.play(FadeIn(setup))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(setup))

        demo1 = MathTex(
            r"W_{AB}(\vec{P}) = \vec{P}\cdot\overrightarrow{AB} = -mg\,\vec{k}\cdot\overrightarrow{AB}",
            font_size=26,
        )
        demo2 = MathTex(
            r"\vec{k}\cdot\overrightarrow{AB} = z_B - z_A \ \Longrightarrow\ "
            r"W_{AB}(\vec{P}) = -mg(z_B-z_A)",
            font_size=25,
        )
        demo3 = MathTex(
            r"W_{AB}(\vec{P}) = mg(z_A - z_B) = \pm\,mgh, \quad h = |z_A - z_B|",
            font_size=27,
            color=YELLOW,
        )
        demo = VGroup(demo1, demo2, demo3).arrange(DOWN, buff=0.35)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le travail du poids entre A et B est le produit scalaire "
                "de P vecteur par le vecteur A-B, soit moins m g, fois k "
                "vecteur, scalaire A-B. Or ce produit scalaire ne retient "
                "que la composante verticale du déplacement, z de B moins z "
                "de A. On obtient donc W égale m g, fois z de A moins z de "
                "B, que l'on note aussi plus ou moins m g h, où h est la "
                "dénivellation, toujours positive, entre A et B."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        convention = definition_box(
            VGroup(
                Text("Convention de signe", font_size=23, weight="BOLD"),
                Text("L'objet descend  →  travail du poids MOTEUR, positif", font_size=21),
                Text("L'objet monte    →  travail du poids RÉSISTANT, négatif", font_size=21),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
            box_width=10.5,
        )
        convention.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La convention de signe est simple : quand l'objet "
                "descend, le poids travaille dans le sens du mouvement, son "
                "travail est moteur, positif. Quand l'objet monte, le poids "
                "s'oppose au mouvement, son travail est résistant, négatif."
            )
        ) as tracker:
            self.play(FadeIn(convention))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(convention))

        theoreme = theorem_box(
            Text(
                _wrap(
                    "Le poids étant une force constante, son travail ne "
                    "dépend pas du chemin suivi, seulement de la "
                    "dénivellation entre A et B. Sur un trajet fermé "
                    "(retour au point de départ), son travail total est "
                    "nul.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comme le poids est une force constante, on retrouve le "
                "théorème vu précédemment : son travail ne dépend pas du "
                "chemin suivi, seulement de la dénivellation entre le point "
                "de départ et le point d'arrivée. Conséquence directe : sur "
                "un trajet fermé, où l'on revient au point de départ, le "
                "travail du poids est toujours nul."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple traité : maçon (2 seaux) -------------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Un maçon monte un seau de mortier de masse 15 kg sur "
                    "une hauteur de 2,5 m, puis redescend un seau vide de "
                    "masse 2 kg sur la même hauteur. Calculer le travail du "
                    "poids dans chaque cas (g = 10 N/kg).",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. Un maçon monte un seau de mortier de "
                "quinze kilogrammes sur une hauteur de deux mètres "
                "cinquante, puis redescend un seau vide de deux "
                "kilogrammes sur la même hauteur. On prend g égale dix "
                "newtons par kilogramme. Calculons le travail du poids dans "
                "chacun des deux cas."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc = corrige_box(
            VGroup(
                Text("Montée (15 kg) : travail résistant", font_size=21),
                MathTex(r"W(\vec{P}) = -mgh = -15\times10\times2{,}5 = -375\ J", font_size=25),
                Text("Descente (2 kg) : travail moteur", font_size=21),
                MathTex(r"W(\vec{P}) = +mgh = 2\times10\times2{,}5 = +50\ J", font_size=25),
            ).arrange(DOWN, buff=0.28),
            box_width=11.0,
        )
        calc.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour la montée du seau plein, le poids s'oppose au "
                "mouvement : son travail vaut moins m g h, soit moins "
                "quinze fois dix fois deux virgule cinq, c'est-à-dire moins "
                "trois cent soixante-quinze joules. Pour la descente du "
                "seau vide, le poids favorise le mouvement : son travail "
                "vaut plus deux fois dix fois deux virgule cinq, soit plus "
                "cinquante joules."
            )
        ) as tracker:
            self.play(FadeIn(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                MathTex(r"W_{AB}(\vec{P}) = \pm\,mgh", font_size=28),
                Text(
                    _wrap(
                        "+ si l'objet descend (moteur), − s'il monte "
                        "(résistant). Indépendant du chemin suivi, nul sur "
                        "un trajet fermé.",
                        width=52,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : le travail du poids vaut plus ou moins m g h. "
                "Positif quand l'objet descend, négatif quand il monte. Il "
                "ne dépend que de la dénivellation entre le départ et "
                "l'arrivée, jamais du chemin suivi, et il est nul sur un "
                "trajet fermé."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "h = |z_A − z_B| est TOUJOURS positive : c'est le sens "
                    "du mouvement (monter ou descendre), pas la valeur de "
                    "h, qui détermine le signe du travail du poids.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège fréquent : la dénivellation h est toujours une "
                "distance positive. Ce n'est jamais la valeur de h qui "
                "détermine le signe du travail du poids, mais uniquement le "
                "sens du mouvement : monter ou descendre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
