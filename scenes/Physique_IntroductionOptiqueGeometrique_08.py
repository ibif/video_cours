"""
scenes/Physique_IntroductionOptiqueGeometrique_08.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 08.

§ 5. Célérité de la lumière c = 3,0×10⁸ m/s dans le vide (≈ air). Tableau
des célérités (vide, air, eau, verre). Relation d = c·Δt. Conséquence :
on voit le Soleil tel qu'il était il y a 8 min 20 s, année-lumière.
Exemple résolu 3 : Abidjan-Paris (≈4800 km, Δt≈16 ms). Exemple résolu 4 :
aller-retour laser Terre-Lune (Δt=2,56 s → d≈384000 km, diviser par 2).
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 5).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    BLUE,
    GRAY,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _schema_aller_retour_lune() -> VGroup:
    """Terre à gauche, Lune à droite, impulsion laser aller (trait plein)
    puis retour (trait pointillé mimé par des tirets)."""
    terre = Circle(radius=0.4, color=BLUE, fill_color=BLUE, fill_opacity=1.0).move_to(LEFT * 4.0)
    label_terre = Text("Terre", font_size=16, color=BLUE).next_to(terre, DOWN, buff=0.15)

    lune = Circle(radius=0.22, color=GRAY, fill_color=GRAY, fill_opacity=1.0).move_to(RIGHT * 4.0)
    label_lune = Text("Lune", font_size=16, color=WHITE).next_to(lune, DOWN, buff=0.15)

    aller = Line(terre.get_right(), lune.get_left(), color=YELLOW, stroke_width=2)
    aller.shift(UP * 0.15)
    label_aller = Text("aller", font_size=14, color=YELLOW).next_to(aller, UP, buff=0.08)

    retour = Line(lune.get_left(), terre.get_right(), color=YELLOW, stroke_width=2)
    retour.shift(DOWN * 0.15)
    label_retour = Text("retour", font_size=14, color=YELLOW).next_to(retour, DOWN, buff=0.08)

    return VGroup(terre, label_terre, lune, label_lune, aller, label_aller, retour, label_retour)


class CeleriteDeLaLumiere(NotionScene):
    def construct(self):
        titre = scene_title("Célérité de la lumière")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "La lumière semble instantanée, mais elle voyage à une "
                "vitesse bien précise. Quelle est cette vitesse, et à quoi "
                "sert-elle pour mesurer des distances ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La lumière semble se propager instantanément, mais elle "
                "voyage en réalité à une vitesse bien précise. Quelle est "
                "cette vitesse, et à quoi sert-elle pour mesurer des "
                "distances ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition + tableau ---------------------------------
        definition_celerite = definition_box(
            VGroup(
                Text("La CÉLÉRITÉ de la lumière dans le vide vaut :", font_size=20),
                MathTex(r"c = 3{,}0 \times 10^{8}\ \text{m/s}", font_size=28),
                Text("Dans l'air, la célérité est quasiment la même.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=10.6,
        )
        definition_celerite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La célérité de la lumière dans le vide vaut trois virgule "
                "zéro fois dix puissance huit mètres par seconde. Dans "
                "l'air, la célérité est quasiment identique à celle du "
                "vide."
            )
        ) as tracker:
            self.play(FadeIn(definition_celerite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_celerite))

        tableau = VGroup(
            Text("Vide  →  3,0 × 10⁸ m/s", font_size=20),
            Text("Air   →  ≈ 3,0 × 10⁸ m/s", font_size=20),
            Text("Eau   →  2,25 × 10⁸ m/s", font_size=20),
            Text("Verre →  ≈ 2,0 × 10⁸ m/s", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        tableau_box = definition_box(tableau, box_width=8.4)
        tableau_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La célérité dépend du milieu traversé. Dans le vide, elle "
                "vaut trois virgule zéro fois dix puissance huit mètres "
                "par seconde. Dans l'air, elle est quasiment la même. Dans "
                "l'eau, elle tombe à deux virgule vingt-cinq fois dix "
                "puissance huit mètres par seconde. Et dans le verre, elle "
                "descend encore, vers deux fois dix puissance huit mètres "
                "par seconde."
            )
        ) as tracker:
            self.play(FadeIn(tableau_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_box))

        relation = definition_box(
            VGroup(
                MathTex(r"d = c \times \Delta t", font_size=30),
                Text("d : distance parcourue (m) · Δt : durée (s)", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=8.2,
        )
        relation.next_to(titre, DOWN, buff=0.4)

        consequence = Text(
            _wrap(
                "Conséquence : on voit le Soleil tel qu'il était il y a "
                "8 min 20 s (durée du trajet de sa lumière). Une "
                "année-lumière est la distance parcourue par la lumière "
                "en une année.",
                width=54,
            ),
            font_size=19,
        )
        consequence.next_to(relation, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On en tire la relation fondamentale : la distance d "
                "parcourue par la lumière est égale à sa célérité c "
                "multipliée par la durée Δt du trajet. Conséquence "
                "frappante : la lumière du Soleil mettant huit minutes et "
                "vingt secondes à nous parvenir, nous voyons le Soleil "
                "tel qu'il était huit minutes vingt plus tôt. Une "
                "année-lumière, elle, est la distance parcourue par la "
                "lumière en une année entière."
            )
        ) as tracker:
            self.play(FadeIn(relation))
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(relation), FadeOut(consequence))

        # --- Exemple résolu 3 : Abidjan-Paris ------------------------------------
        exemple3 = example_box(
            VGroup(
                Text("Distance Abidjan-Paris ≈ 4800 km = 4,8 × 10⁶ m.", font_size=19),
                Text("Durée de propagation de la lumière :", font_size=19),
                MathTex(
                    r"\Delta t = \dfrac{d}{c} = \dfrac{4{,}8 \times 10^{6}}{3{,}0 \times 10^{8}}"
                    r" \approx 16 \times 10^{-3}\ \text{s} = 16\ \text{ms}",
                    font_size=23,
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.0,
        )
        exemple3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : la distance entre Abidjan et Paris est "
                "d'environ quatre mille huit cents kilomètres, soit quatre "
                "virgule huit fois dix puissance six mètres. La durée de "
                "propagation de la lumière vaut Δt égale d sur c, soit "
                "quatre virgule huit fois dix puissance six, divisé par "
                "trois fois dix puissance huit, ce qui donne environ "
                "seize millisecondes."
            )
        ) as tracker:
            self.play(FadeIn(exemple3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple3))

        # --- Exemple résolu 4 : aller-retour Terre-Lune ---------------------------
        schema_lune = _schema_aller_retour_lune()
        schema_lune.scale(0.85)
        schema_lune.next_to(titre, DOWN, buff=0.5)

        enonce4 = example_box(
            Text(
                "Une impulsion laser Terre-Lune met Δt = 2,56 s pour l'ALLER-RETOUR.\n"
                "Quelle est la distance Terre-Lune ?",
                font_size=19,
            ),
            box_width=10.8,
        )
        enonce4.next_to(schema_lune, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Autre exemple : une impulsion laser envoyée de la Terre "
                "vers la Lune, puis réfléchie, met deux virgule "
                "cinquante-six secondes pour effectuer l'aller-retour. "
                "Quelle est la distance entre la Terre et la Lune ?"
            )
        ) as tracker:
            self.play(FadeIn(schema_lune))
            self.play(FadeIn(enonce4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_lune), FadeOut(enonce4))

        resolution4 = example_box(
            VGroup(
                Text("Attention : Δt = 2,56 s correspond à l'ALLER-RETOUR,", font_size=19),
                Text("il faut diviser par 2 avant de multiplier par c.", font_size=19),
                MathTex(
                    r"d = c \times \dfrac{\Delta t}{2} = 3{,}0 \times 10^{8} \times \dfrac{2{,}56}{2}"
                    r" \approx 3{,}84 \times 10^{8}\ \text{m} \approx 384\,000\ \text{km}",
                    font_size=21,
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.6,
        )
        resolution4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention, ces deux virgule cinquante-six secondes "
                "correspondent à l'aller-retour complet : il faut donc "
                "diviser cette durée par deux avant de multiplier par c. "
                "On obtient d égale c fois Δt sur deux, soit trois fois "
                "dix puissance huit, multiplié par un virgule vingt-huit, "
                "ce qui donne environ trois cent quatre-vingt-quatre mille "
                "kilomètres, la distance réelle entre la Terre et la "
                "Lune."
            )
        ) as tracker:
            self.play(FadeIn(resolution4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution4))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"c \approx 3{,}0 \times 10^{8}\ \text{m/s (vide, air)} \quad d = c\,\Delta t", font_size=24),
                Text("La célérité diminue dans l'eau, puis dans le verre.", font_size=19),
                Text("Aller-retour : diviser Δt par 2 avant de calculer d.", font_size=19),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. La célérité de la lumière vaut "
                "environ trois fois dix puissance huit mètres par seconde "
                "dans le vide comme dans l'air, et la distance parcourue "
                "vaut c multiplié par Δt. Cette célérité diminue dans "
                "l'eau, puis encore davantage dans le verre. Et pour un "
                "aller-retour, il faut toujours diviser la durée mesurée "
                "par deux avant de calculer la distance."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Oublier de diviser par 2 dans un calcul d'aller-retour", font_size=19),
                Text("   (écho, radar, laser) : c'est l'erreur la plus fréquente.", font_size=19),
                Text("• Toujours convertir les distances en MÈTRES et les", font_size=19),
                Text("   durées en SECONDES avant tout calcul (pas en km, ms).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le piège le plus fréquent : oublier de diviser par deux "
                "dans un calcul d'aller-retour, que ce soit avec un écho, "
                "un radar ou un laser. Et n'oubliez jamais de convertir "
                "toutes les distances en mètres et toutes les durées en "
                "secondes avant de faire le moindre calcul."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
