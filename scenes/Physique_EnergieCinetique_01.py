"""
scenes/Physique_EnergieCinetique_01.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 01.

§ Mise en évidence expérimentale (chute libre d'une bille, v²=f(h) droite
passant par l'origine de pente 2g) et définition de l'énergie cinétique de
translation Ec=½mv². Remarques : signe, dépendance au référentiel, unités,
proportionnalité au carré de la vitesse. Exemple résolu : moto-taxi.
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, § 1).
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EnergieCinetiqueTranslationDefinition(NotionScene):
    def construct(self):
        titre = scene_title("Énergie cinétique de translation")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : expérience de la chute libre --------------------------
        mise_en_situation = Text(
            _wrap(
                "Lâchons une bille en chute libre, sans vitesse initiale, "
                "depuis différentes hauteurs h, et mesurons sa vitesse v "
                "juste avant l'impact au sol. Que peut-on observer entre "
                "v² et h ?",
                width=54,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        haut = UP * 1.7 + LEFT * 4.2
        bas = DOWN * 1.7 + LEFT * 4.2
        chute_ligne = DashedLine(haut, bas, color=WHITE, stroke_width=2)
        bille = Dot(haut, color=YELLOW, radius=0.14)
        h_fleche = DoubleArrow(haut + RIGHT * 0.6, bas + RIGHT * 0.6, buff=0, stroke_width=2, color=WHITE)
        h_label = MathTex("h", font_size=28).next_to(h_fleche, RIGHT, buff=0.15)
        sol = DashedLine(bas + LEFT * 0.5, bas + RIGHT * 1.5, color=WHITE, stroke_width=2)
        schema = VGroup(chute_ligne, bille, h_fleche, h_label, sol)
        schema.next_to(mise_en_situation, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Faisons une expérience simple : lâchons une bille en "
                "chute libre, sans vitesse initiale, depuis différentes "
                "hauteurs h, et mesurons à chaque fois sa vitesse v juste "
                "avant l'impact au sol. La question est : quelle relation "
                "existe-t-il entre le carré de cette vitesse et la hauteur "
                "de chute ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(Create(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(schema))

        # --- Raisonnement : graphe v²=f(h), droite de pente 2g -----------------
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 100, 20],
            x_length=5.6,
            y_length=3.8,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.45).shift(LEFT * 2.6)
        g_val = 9.8
        droite = axes.plot(lambda h: 2 * g_val * h, x_range=[0, 5], color=YELLOW)
        x_lab = MathTex("h \\ (\\text{m})", font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.15)
        y_lab = MathTex("v^2 \\ (\\text{m}^2/\\text{s}^2)", font_size=22).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        legende = VGroup(
            MathTex(r"v^2 = 2g \, h", font_size=30, color=YELLOW),
            Text("droite passant par l'origine", font_size=20),
            Text("pente = 2g", font_size=20),
        ).arrange(DOWN, buff=0.15)
        legende.next_to(axes, RIGHT, buff=0.4)
        graphe = VGroup(axes, droite, x_lab, y_lab)

        with self.voiceover(
            text=(
                "En reportant, pour chaque essai, le carré de la vitesse en "
                "fonction de la hauteur de chute, on obtient une droite qui "
                "passe par l'origine, de pente égale à deux fois "
                "l'intensité de la pesanteur g. On en déduit la relation "
                "v carré égale deux g h, résultat déjà connu de la chute "
                "libre. En multipliant les deux membres par la masse m et "
                "par un demi, on obtient un demi m v carré égale m g h, "
                "c'est-à-dire le travail du poids. Cette quantité, un demi "
                "m v carré, mérite un nom : c'est l'énergie cinétique."
            )
        ) as tracker:
            self.play(Create(axes), Write(x_lab), Write(y_lab))
            self.play(Create(droite), FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe), FadeOut(legende))

        # --- Définition ----------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Énergie cinétique de translation", font_size=24, weight="BOLD"),
                MathTex(r"E_c = \dfrac{1}{2} m v^2", font_size=34),
                Text("m en kg, v en m/s, Ec en joules (J)", font_size=21),
            ).arrange(DOWN, buff=0.25),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Définition : l'énergie cinétique de translation d'un "
                "corps de masse m animé d'une vitesse v est E c égale un "
                "demi m v carré. La masse m s'exprime en kilogrammes, la "
                "vitesse v en mètres par seconde, et l'énergie cinétique E "
                "c en joules."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Remarques (pièges à connaître dès la définition) --------------------
        remarques = warning_box(
            VGroup(
                Text("• Ec est toujours positive ou nulle (jamais négative).", font_size=21),
                Text("• Ec dépend du référentiel choisi : un passager assis", font_size=21),
                Text("   dans un car a Ec = 0 par rapport au car, mais Ec ≠ 0", font_size=21),
                Text("   par rapport au sol.", font_size=21),
                Text("• Toujours convertir v en m/s : diviser une vitesse", font_size=21),
                Text("   en km/h par 3,6.", font_size=21),
                Text("• Ec est proportionnelle au CARRÉ de v : doubler v", font_size=21),
                Text("   multiplie Ec par 4, pas par 2.", font_size=21),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.2,
        )
        remarques.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quatre remarques importantes. Premièrement, l'énergie "
                "cinétique est toujours positive ou nulle, jamais "
                "négative. Deuxièmement, elle dépend du référentiel "
                "choisi : un passager assis dans un car a une énergie "
                "cinétique nulle par rapport au car, mais non nulle par "
                "rapport au sol. Troisièmement, la vitesse doit toujours "
                "être exprimée en mètres par seconde : pour convertir des "
                "kilomètres par heure, on divise par trois virgule six. "
                "Enfin, l'énergie cinétique est proportionnelle au carré "
                "de la vitesse : doubler la vitesse multiplie l'énergie "
                "cinétique par quatre, pas par deux."
            )
        ) as tracker:
            self.play(FadeIn(remarques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarques))

        # --- Exemple résolu : moto-taxi ------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un moto-taxi et son pilote, m = 250 kg, roulent à 54 km/h.", font_size=21),
                MathTex(r"v = \dfrac{54}{3{,}6} = 15\ \text{m/s}", font_size=27),
                MathTex(r"E_c = \dfrac{1}{2}\times 250\times 15^2 = 28\,125\ \text{J}", font_size=27),
            ).arrange(DOWN, buff=0.28),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : un moto-taxi et son pilote, de masse "
                "totale deux cent cinquante kilogrammes, roulent à "
                "cinquante-quatre kilomètres par heure. On convertit "
                "d'abord la vitesse : cinquante-quatre divisé par trois "
                "virgule six, soit quinze mètres par seconde. L'énergie "
                "cinétique vaut alors un demi fois deux cent cinquante "
                "fois quinze au carré, soit vingt-huit mille cent "
                "vingt-cinq joules."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"E_c = \dfrac{1}{2} m v^2 \quad (m \ \text{en kg}, v \ \text{en m/s}, E_c \ \text{en J})", font_size=25),
                Text("Toujours ≥ 0, dépend du référentiel, ∝ v².", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'énergie cinétique de translation "
                "vaut un demi m v carré, avec la masse en kilogrammes, la "
                "vitesse en mètres par seconde et l'énergie en joules. "
                "Elle est toujours positive ou nulle, dépend du "
                "référentiel choisi, et est proportionnelle au carré de "
                "la vitesse."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
