"""
scenes/Physique_EnergieCinetique_07.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 07.

§ Application : chute libre et vitesse d'arrivée au sol. Établissement de
v = √(2gh) par le théorème de l'énergie cinétique (retrouve le résultat
expérimental de la scène 01). Remarque : la vitesse ne dépend pas de la
masse.
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, § 5, partie 3).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Create,
    DashedLine,
    Dot,
    DoubleArrow,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ApplicationChuteLibre(NotionScene):
    def construct(self):
        titre = scene_title("Application : chute libre, vitesse d'arrivée au sol")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : corps lâché sans vitesse initiale depuis une hauteur h -----
        haut = UP * 1.7 + LEFT * 3.5
        bas = DOWN * 1.5 + LEFT * 3.5
        ligne = DashedLine(haut, bas, color=WHITE, stroke_width=2)
        corps = Dot(haut, color=YELLOW, radius=0.14)
        h_fleche = DoubleArrow(haut + RIGHT * 0.6, bas + RIGHT * 0.6, buff=0, stroke_width=2, color=WHITE)
        h_label = MathTex("h", font_size=26).next_to(h_fleche, RIGHT, buff=0.15)
        sol = DashedLine(bas + LEFT * 0.6, bas + RIGHT * 1.8, color=WHITE, stroke_width=2)
        label_a = MathTex("A", font_size=24).next_to(haut, LEFT, buff=0.2)
        label_b = MathTex("B", font_size=24).next_to(bas, LEFT, buff=0.2)
        schema = VGroup(ligne, corps, h_fleche, h_label, sol, label_a, label_b)
        schema.move_to(LEFT * 3.0)

        enonce = Text(
            _wrap(
                "Un corps de masse m est lâché sans vitesse initiale (en A) "
                "d'une hauteur h. Quelle est sa vitesse v_B à l'arrivée au "
                "sol (en B), en négligeant les frottements de l'air ?",
                width=42,
            ),
            font_size=21,
        )
        enonce.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Retrouvons maintenant, par le théorème de l'énergie "
                "cinétique, le résultat observé expérimentalement au "
                "début du chapitre. Un corps de masse m est lâché sans "
                "vitesse initiale en A, d'une hauteur h. Quelle est sa "
                "vitesse v B à l'arrivée au sol, en B, en négligeant les "
                "frottements de l'air ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(enonce))

        # --- Raisonnement : application du théorème --------------------------------
        raisonnement = VGroup(
            Text("Seul le poids travaille (frottements négligés) :", font_size=21),
            MathTex(r"\Delta E_c = E_{cB} - E_{cA} = \dfrac{1}{2}mv_B^2 - 0 = W_{A\to B}(\vec{P}) = mgh", font_size=24),
            MathTex(r"\Longrightarrow\ \dfrac{1}{2}v_B^2 = gh \ \Longrightarrow\ v_B = \sqrt{2gh}", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.3)
        raisonnement.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Seul le poids travaille, les frottements de l'air étant "
                "négligés. Le théorème de l'énergie cinétique donne : "
                "l'énergie cinétique en B, un demi m v B carré, moins "
                "l'énergie cinétique en A, qui est nulle, est égale au "
                "travail du poids, m g h. En simplifiant par la masse m, "
                "qui disparaît des deux côtés, on obtient v B égale "
                "racine carrée de deux g h."
            )
        ) as tracker:
            self.play(Write(raisonnement[0]))
            self.play(Write(raisonnement[1]))
            self.play(Write(raisonnement[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(raisonnement))

        # --- Formule encadrée --------------------------------------------------------
        formule = theorem_box(
            VGroup(
                Text("Vitesse d'arrivée au sol en chute libre", font_size=22, weight="BOLD"),
                MathTex(r"v_B = \sqrt{2gh}", font_size=34),
            ).arrange(DOWN, buff=0.25),
        )
        formule.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "On retrouve exactement le résultat observé "
                "expérimentalement en tout début de chapitre : la vitesse "
                "d'arrivée au sol vaut v B égale racine carrée de deux g "
                "h."
            )
        ) as tracker:
            self.play(FadeIn(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule))

        # --- Remarque : indépendance vis-à-vis de la masse --------------------------
        remarque = warning_box(
            VGroup(
                Text("La vitesse d'arrivée au sol NE DÉPEND PAS de la masse m :", font_size=21),
                Text("la masse a disparu du calcul. Une bille légère et une bille", font_size=21),
                Text("lourde lâchées de la même hauteur (sans frottement de l'air)", font_size=21),
                Text("arrivent au sol avec la même vitesse.", font_size=21),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        remarque.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Remarque essentielle : la vitesse d'arrivée au sol ne "
                "dépend pas de la masse du corps, puisque celle-ci "
                "s'élimine dans le calcul. Une bille légère et une bille "
                "lourde, lâchées de la même hauteur, sans frottement de "
                "l'air, arrivent au sol avec exactement la même vitesse."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Exemple : application numérique ----------------------------------------
        exemple = example_box(
            VGroup(
                Text("Chute libre depuis h = 20 m (g ≈ 9,8 m/s²) :", font_size=21),
                MathTex(r"v_B = \sqrt{2\times 9{,}8\times 20} \approx 19{,}8\ \text{m/s} \approx 71\ \text{km/h}", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Application numérique : pour une chute libre depuis vingt "
                "mètres, avec g environ égal à neuf virgule huit mètres "
                "par seconde carré, on trouve une vitesse d'arrivée "
                "d'environ dix-neuf virgule huit mètres par seconde, soit "
                "environ soixante-onze kilomètres par heure."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"v_B = \sqrt{2gh}", font_size=30),
                Text("Résultat indépendant de la masse m.", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=10.6,
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la vitesse d'arrivée au sol en "
                "chute libre vaut racine carrée de deux g h, et ce "
                "résultat est totalement indépendant de la masse du "
                "corps qui tombe."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
