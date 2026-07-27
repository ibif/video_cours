"""
scenes/Physique_EnergieMecanique_05.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 05.

Loi de conservation de l'énergie mécanique : théorème (système soumis
uniquement à des forces conservatives et/ou à travail nul → Em=constante),
notions de système conservatif, isolé ou pseudo-isolé, conséquence
(transformation Ec↔Ep). Exemple résolu 2 : solide de 2 kg lâché du sommet
d'un plan incliné poli, zA=1 m → vB=√(2gzA)≈4,47 m/s (la masse se
simplifie).
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
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
    Polygon,
    Square,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, exercise_box, scene_title, theorem_box, warning_box

POIDS_COLOR = "#1E5FA8"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _plan_incline_poli():
    return Polygon(
        LEFT * 2.0 + DOWN * 1.2,
        RIGHT * 2.0 + DOWN * 1.2,
        RIGHT * 2.0 + UP * 1.0,
        color=WHITE,
        fill_color="#3A3A3A",
        fill_opacity=0.6,
    )


class LoiConservationEnergieMecanique(NotionScene):
    def construct(self):
        titre = scene_title("Loi de conservation de l'énergie mécanique")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé : formulation du théorème -----------------------------------------
        intro = Text(
            _wrap(
                "La démonstration précédente se généralise : formulons "
                "maintenant la loi de conservation de l'énergie "
                "mécanique.",
                width=54,
            ),
            font_size=24,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La démonstration que nous venons de mener se généralise à "
                "toute situation analogue. Formulons à présent, sous forme "
                "de théorème, la loi de conservation de l'énergie "
                "mécanique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Théorème ------------------------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Loi de conservation de l'énergie mécanique", font_size=21, weight="BOLD"),
                Text(
                    "Si un système n'est soumis qu'à des forces conservatives",
                    font_size=19,
                ),
                Text(
                    "et/ou des forces à travail nul, alors :",
                    font_size=19,
                ),
                MathTex(r"E_m = E_c + E_p = \text{constante}", font_size=28, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
            box_width=10.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Théorème : si un système n'est soumis qu'à des forces "
                "conservatives, et éventuellement des forces à travail nul "
                "comme une réaction normale, alors son énergie mécanique "
                "reste constante au cours du mouvement. On parle alors de "
                "système conservatif, système isolé ou pseudo-isolé du "
                "point de vue de l'énergie mécanique."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : conséquence, transformation Ec <-> Ep --------------------
        consequence = Text(
            _wrap(
                "Conséquence : quand Em est constante, Ec et Ep se "
                "transforment l'une en l'autre. Si le système descend, Ep "
                "diminue et Ec augmente. S'il monte, c'est l'inverse.",
                width=54,
            ),
            font_size=23,
        )
        consequence.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Conséquence directe : puisque leur somme reste constante, "
                "l'énergie cinétique et l'énergie potentielle se "
                "transforment continuellement l'une en l'autre. Quand le "
                "système descend, son énergie potentielle diminue tandis "
                "que son énergie cinétique augmente : il accélère. Quand il "
                "monte, c'est l'inverse : l'énergie cinétique diminue au "
                "profit de l'énergie potentielle, et il ralentit."
            )
        ) as tracker:
            self.play(Write(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- Exemple traité : plan incliné poli ---------------------------------------
        plan = _plan_incline_poli().scale(0.75)
        point_a = plan.get_vertices()[2] + LEFT * 0.3 + DOWN * 0.1
        point_b = plan.get_vertices()[0] + RIGHT * 0.3 + UP * 0.1
        solide_a = Square(side_length=0.28, color=YELLOW, fill_color=YELLOW, fill_opacity=0.9).move_to(point_a)
        solide_b = Square(side_length=0.28, color=YELLOW, fill_color=YELLOW, fill_opacity=0.4).move_to(point_b)
        label_a = MathTex("A", font_size=22).next_to(solide_a, LEFT, buff=0.12)
        label_b = MathTex("B", font_size=22).next_to(solide_b, UP, buff=0.12)
        z_label = MathTex("z_A", font_size=20).next_to(solide_a, DOWN, buff=0.4)
        schema = VGroup(plan, solide_a, solide_b, label_a, label_b, z_label)
        schema.scale(0.8).move_to(LEFT * 3.2 + DOWN * 0.3)

        enonce = exercise_box(
            Text(
                _wrap(
                    "Un solide de masse 2 kg est lâché sans vitesse "
                    "initiale du sommet A d'un plan incliné poli (sans "
                    "frottement), à zA=1 m au-dessus du bas du plan B. "
                    "Calculer sa vitesse vB en bas (g=10 N/kg).",
                    width=40,
                ),
                font_size=19,
            ),
            box_width=6.6,
        )
        enonce.next_to(schema, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu. Un solide de masse deux kilogrammes est "
                "lâché sans vitesse initiale du sommet A d'un plan incliné "
                "poli, c'est-à-dire sans frottement, situé à un mètre "
                "au-dessus du point B, en bas du plan. On prend g égale dix "
                "newtons par kilogramme. Calculons sa vitesse en B."
            )
        ) as tracker:
            self.play(FadeIn(schema), FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(enonce))

        calc1 = MathTex(
            r"E_m(A) = E_m(B) \ \Longrightarrow\ \tfrac{1}{2}mv_A^2 + mgz_A = \tfrac{1}{2}mv_B^2 + mgz_B",
            font_size=25,
        )
        calc2 = MathTex(
            r"v_A = 0, \quad z_B = 0 \ \Longrightarrow\ mgz_A = \tfrac{1}{2}mv_B^2",
            font_size=27,
        )
        calc3 = MathTex(
            r"v_B = \sqrt{2gz_A} = \sqrt{2\times 10\times 1} \approx 4{,}47\ \text{m/s}",
            font_size=27,
            color=YELLOW,
        )
        calc = VGroup(calc1, calc2, calc3).arrange(DOWN, buff=0.32)
        calc.next_to(titre, DOWN, buff=0.5)

        note_masse = Text(
            "Remarque : la masse m se simplifie dans le calcul !",
            font_size=20,
        )
        note_masse.next_to(calc, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le solide n'étant soumis qu'au poids et à une réaction "
                "sans frottement, l'énergie mécanique se conserve entre A "
                "et B. La vitesse initiale est nulle, et l'on prend l'altitude "
                "de B comme référence. On obtient m g z de A égale un demi "
                "m v de B au carré. En simplifiant par la masse m, qui "
                "disparaît du calcul, on trouve v de B égale racine de deux "
                "g z de A, soit environ quatre virgule quarante-sept mètres "
                "par seconde."
            )
        ) as tracker:
            self.play(Write(calc1))
            self.play(Write(calc2))
            self.play(Write(calc3))
            self.play(FadeIn(note_masse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc), FadeOut(note_masse))

        # --- À retenir -------------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                MathTex(r"E_m = \text{constante} \ \Rightarrow \ v_B = \sqrt{2g z_A}", font_size=27),
                Text("(sans frottement, vitesse initiale nulle)", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=9.6,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : quand l'énergie mécanique se "
                "conserve, avec une vitesse initiale nulle, la vitesse "
                "atteinte après une chute de hauteur z de A vaut racine de "
                "deux g z de A — et la masse du solide n'intervient jamais "
                "dans ce résultat."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : la loi de conservation ne s'applique QUE si "
                    "aucun frottement ne travaille. Vérifiez toujours "
                    "l'énoncé (« sans frottement », « poli », « lisse ») "
                    "avant de l'utiliser.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=10.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège important : la loi de conservation de l'énergie "
                "mécanique ne s'applique que si aucun frottement ne "
                "travaille. Il faut toujours vérifier dans l'énoncé la "
                "présence de mots comme sans frottement, poli, ou lisse, "
                "avant de l'utiliser sans réfléchir."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
