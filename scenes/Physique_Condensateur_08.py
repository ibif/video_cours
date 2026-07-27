"""
scenes/Physique_Condensateur_08.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 08.

§ 5. Énergie emmagasinée dans un condensateur. Mise en évidence (une
lampe branchée sur un condensateur chargé brille brièvement pendant la
décharge). Établissement de E=½qu à partir de l'aire sous la droite
u=f(q). Théorème : formes équivalentes E=½Cu²=q²/(2C)=½qu.
Exemple résolu 6 : C=220 µF, u=24 V → E≈63 mJ, vérifié par les deux
formules.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 5).
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
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EnergieEmmagasinee(NotionScene):
    def construct(self):
        titre = scene_title("Énergie emmagasinée dans un condensateur")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Un condensateur chargé, débranché du générateur, peut "
                "encore allumer brièvement une lampe en se déchargeant à "
                "travers elle. Il stocke donc bien de l'énergie. Comment "
                "la calculer ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un condensateur chargé, débranché du générateur, peut "
                "encore allumer brièvement une lampe lorsqu'on le fait se "
                "décharger à travers elle. Il stocke donc bien de "
                "l'énergie. Comment la calculer ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : aire sous u = f(q) ----------------------------------
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=4.6,
            y_length=4.0,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.55).shift(LEFT * 2.6)
        droite = axes.plot(lambda q: q, x_range=[0, 5], color=YELLOW)

        triangle = Polygon(
            axes.c2p(0, 0), axes.c2p(5, 0), axes.c2p(5, 5),
            fill_color=YELLOW, fill_opacity=0.35, stroke_width=0,
        )

        x_lab = MathTex("q", font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        y_lab = MathTex("u", font_size=22).next_to(axes.y_axis.get_end(), UP, buff=0.1)

        note = VGroup(
            Text("L'aire du triangle sous la droite", font_size=19),
            Text("u = f(q) représente l'énergie E", font_size=19),
            Text("reçue par le condensateur.", font_size=19),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        note.next_to(axes, RIGHT, buff=0.5)

        graphe = VGroup(axes, x_lab, y_lab)

        with self.voiceover(
            text=(
                "Reprenons la droite u égale q sur C, obtenue lors de la "
                "charge. L'énergie reçue par le condensateur correspond à "
                "l'aire du triangle situé sous cette droite, entre zéro et "
                "la charge finale q. Or l'aire d'un triangle vaut la moitié "
                "de la base fois la hauteur."
            )
        ) as tracker:
            self.play(Create(axes), Write(x_lab), Write(y_lab))
            self.play(Create(droite))
            self.play(FadeIn(triangle), FadeIn(note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe), FadeOut(droite), FadeOut(triangle), FadeOut(note))

        etablissement = VGroup(
            Text("Aire du triangle = ½ × base × hauteur = ½ × q × u :", font_size=21),
            MathTex(r"E = \dfrac{1}{2}\, q\, u", font_size=32, color=YELLOW),
        ).arrange(DOWN, buff=0.25)
        etablissement.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'aire de ce triangle vaut donc un demi fois q fois u : "
                "l'énergie emmagasinée par le condensateur, une fois "
                "chargé, vaut E égale un demi q u."
            )
        ) as tracker:
            self.play(FadeIn(etablissement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etablissement))

        # --- Théorème : formes équivalentes -------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Énergie emmagasinée dans un condensateur", font_size=22, weight="BOLD"),
                MathTex(r"E = \dfrac{1}{2}\, q\, u = \dfrac{1}{2}\, C u^2 = \dfrac{q^2}{2 C}", font_size=30),
                Text("E en joules (J), en utilisant q = C u pour passer d'une", font_size=19),
                Text("forme à l'autre.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En remplaçant q par C u, ou u par q sur C, on obtient trois "
                "formes équivalentes de la même énergie : E égale un demi q "
                "u, égale un demi C u carré, égale q carré sur deux C. Le "
                "choix de la formule dépend simplement des données dont on "
                "dispose dans l'énoncé."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 6 ------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un condensateur C = 220 µF est chargé sous u = 24 V.", font_size=20),
                MathTex(r"E = \dfrac{1}{2} C u^2 = \dfrac{1}{2} \times 220\times10^{-6} \times 24^2 \approx 63\ \text{mJ}", font_size=24),
                Text("Vérification avec q = C u = 5,28 mC :", font_size=19),
                MathTex(r"E = \dfrac{q^2}{2C} = \dfrac{(5{,}28\times10^{-3})^2}{2 \times 220\times10^{-6}} \approx 63\ \text{mJ}\ \checkmark", font_size=23),
            ).arrange(DOWN, buff=0.2),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : un condensateur de deux cent vingt "
                "microfarads est chargé sous vingt-quatre volts. Son "
                "énergie vaut un demi C u carré, soit environ soixante-trois "
                "millijoules. Vérifions avec l'autre formule : la charge q "
                "vaut C u, soit cinq virgule vingt-huit millicoulombs, et q "
                "carré sur deux C redonne bien environ soixante-trois "
                "millijoules."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"E = \dfrac{1}{2} q u = \dfrac{1}{2} C u^2 = \dfrac{q^2}{2C} \ \ (\text{joules})", font_size=27),
            ).arrange(DOWN, buff=0.22),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'énergie emmagasinée par un "
                "condensateur vaut un demi q u, ou un demi C u carré, ou q "
                "carré sur deux C, toujours exprimée en joules."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas oublier le FACTEUR ½ dans les trois formules :", font_size=20),
                Text("   E = C u² (sans le ½) est une erreur fréquente.", font_size=20),
                Text("• Toujours convertir C en FARADS (pas en µF) avant de", font_size=20),
                Text("   calculer E en joules, sous peine d'un résultat faux d'un", font_size=20),
                Text("   facteur 10⁶.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges fréquents. Il ne faut jamais oublier le "
                "facteur un demi dans les trois formules : écrire E égale C "
                "u carré, sans ce facteur, est une erreur très courante. Et "
                "il faut toujours convertir la capacité en farads, et non "
                "en microfarads, avant de calculer l'énergie en joules, "
                "sous peine d'un résultat faux d'un facteur un million."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
