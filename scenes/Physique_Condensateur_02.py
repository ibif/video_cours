"""
scenes/Physique_Condensateur_02.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 02.

§ 2. Intensité et charge en régime transitoire. Courant i=dq/dt (ou
I=Δq/Δt en régime uniforme). Signe du courant selon que le condensateur
se charge (i>0, q croît) ou se décharge (i change de sens, q décroît).
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 2).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class IntensiteChargeRegimeTransitoire(NotionScene):
    def construct(self):
        titre = scene_title("Intensité et charge en régime transitoire")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "La charge q d'un condensateur n'est jamais constante "
                "pendant qu'un courant circule : elle varie dans le temps. "
                "Quel lien relie l'intensité du courant à cette variation "
                "de charge ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La charge q d'un condensateur n'est jamais constante tant "
                "qu'un courant circule dans le circuit : elle varie dans le "
                "temps. Quel lien relie l'intensité de ce courant à cette "
                "variation de charge ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : i = dq/dt --------------------------------------
        etapes = VGroup(
            Text("L'intensité du courant qui charge le condensateur est", font_size=21),
            Text("le taux de variation de sa charge au cours du temps :", font_size=21),
            MathTex(r"i = \dfrac{dq}{dt}", font_size=32, color=YELLOW),
            Text("En régime uniforme (variation régulière), on utilise :", font_size=21),
            MathTex(r"I = \dfrac{\Delta q}{\Delta t}", font_size=30),
        ).arrange(DOWN, buff=0.22)
        etapes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'intensité du courant qui alimente un condensateur est le "
                "taux de variation de sa charge au cours du temps : i égale "
                "d q sur d t. Lorsque cette variation est uniforme, on "
                "utilise la version simplifiée : I égale Δ q sur Δ t, "
                "exactement comme pour la définition générale de "
                "l'intensité."
            )
        ) as tracker:
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes))

        # --- Raisonnement : signe selon charge / décharge --------------------
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=6.2,
            y_length=3.6,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.55).shift(LEFT * 2.2)

        courbe_charge = axes.plot(lambda t: min(t, 5) if t <= 5 else 10 - t, x_range=[0, 8], color=YELLOW)
        x_lab = MathTex("t", font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        y_lab = MathTex("q", font_size=22).next_to(axes.y_axis.get_end(), UP, buff=0.1)

        legende = VGroup(
            Text("q croît → charge → i > 0", font_size=19, color=YELLOW),
            Text("q décroît → décharge → i change de sens", font_size=19, color="#4FA8FF"),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        legende.next_to(axes, RIGHT, buff=0.5)

        graphe = VGroup(axes, x_lab, y_lab)

        with self.voiceover(
            text=(
                "Regardons l'allure d'une charge q au cours du temps. "
                "Quand le condensateur SE CHARGE, sa charge q augmente : la "
                "pente de la courbe est positive, donc l'intensité i est "
                "positive. Quand le condensateur SE DÉCHARGE au contraire, "
                "sa charge q diminue : la pente devient négative, "
                "l'intensité change de sens par rapport à la charge."
            )
        ) as tracker:
            self.play(Create(axes), Write(x_lab), Write(y_lab))
            self.play(Create(courbe_charge))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe), FadeOut(courbe_charge), FadeOut(legende))

        # --- Exemple : lecture de pente sur un graphe -------------------------
        exemple = example_box(
            VGroup(
                Text("Entre t = 0 s et t = 5 s, la charge passe de 0 à 250 µC,", font_size=20),
                Text("de façon uniforme (portion de droite).", font_size=20),
                MathTex(r"I = \dfrac{\Delta q}{\Delta t} = \dfrac{250\ \mu\text{C}}{5\ \text{s}} = 50\ \mu\text{A}", font_size=26),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.22),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : entre l'instant zéro et cinq secondes, la charge "
                "passe de zéro à deux cent cinquante microcoulombs, de "
                "façon uniforme. L'intensité moyenne pendant cette phase "
                "vaut alors Δ q sur Δ t, soit deux cent cinquante "
                "microcoulombs sur cinq secondes, c'est-à-dire cinquante "
                "microampères."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"i = \dfrac{dq}{dt} \quad \text{(ou } I = \dfrac{\Delta q}{\Delta t} \text{ en régime uniforme)}", font_size=25),
                Text("Charge : q croît, i > 0. Décharge : q décroît, i change de sens.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'intensité vaut d q sur d t, ou Δ q "
                "sur Δ t en régime uniforme. Pendant la charge, q croît et "
                "l'intensité est positive ; pendant la décharge, q décroît "
                "et l'intensité change de sens."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter -----------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Le signe de i dépend du sens choisi pour orienter le", font_size=20),
                Text("   circuit : toujours préciser ce sens avant de conclure.", font_size=20),
                Text("• I = Δq/Δt n'est valable que si la variation de q est", font_size=20),
                Text("   uniforme ; sinon il faut utiliser i = dq/dt (pente locale).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Le signe de l'intensité dépend "
                "toujours du sens choisi pour orienter le circuit : il faut "
                "le préciser avant de conclure quoi que ce soit sur le "
                "signe de i. Et la relation I égale Δ q sur Δ t n'est "
                "valable que si la variation de charge est uniforme ; sinon "
                "il faut revenir à la définition générale, i égale d q sur "
                "d t, c'est-à-dire la pente locale de la courbe."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
