"""
scenes/Physique_PuissanceEnergieElectriques_02.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 02.

§ 2. Énergie et puissance électriques d'un dipôle. Établissement de
W=UIΔt à partir de W_{A→B}=qU_AB et q=IΔt. Énergie électrique W=UIt
(interprétation : le récepteur reçoit, le générateur cède). Puissance
P=W/t=UI (watt, 1 W = 1 V × 1 A). Exemple résolu : lampe U=220 V,
I=0,45 A, t=2 h → P=99 W, W=712 800 J ≈ 7,13×10⁵ J.
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 2).
"""

import textwrap

from manim import DOWN, LEFT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EnergiePuissanceElectriqueDipole(NotionScene):
    def construct(self):
        titre = scene_title("Énergie et puissance électriques d'un dipôle")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Quand un courant traverse un dipôle pendant une durée "
                "donnée, un échange d'énergie a lieu entre le dipôle et le "
                "reste du circuit. Comment quantifier cette énergie, et la "
                "puissance à laquelle elle est échangée ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quand un courant électrique traverse un dipôle pendant une "
                "certaine durée, un échange d'énergie a lieu entre ce "
                "dipôle et le reste du circuit. Comment quantifier cette "
                "énergie électrique, et la puissance à laquelle elle est "
                "échangée ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : établissement de W = UIΔt --------------------------
        etapes = VGroup(
            Text("Une charge q qui se déplace de A vers B reçoit ou cède", font_size=21),
            MathTex(r"W_{A \to B} = q \, U_{AB}", font_size=28),
            Text("Pendant une durée Δt, cette charge vaut :", font_size=21),
            MathTex(r"q = I \, \Delta t", font_size=28),
            Text("En combinant les deux relations :", font_size=21),
            MathTex(r"W = U \, I \, \Delta t", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.2)
        etapes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons le raisonnement. Une charge q qui se déplace du "
                "point A vers le point B échange une énergie W A vers B "
                "égale q fois U A B. Or, pendant une durée Δt, cette charge "
                "vaut q égale I Δt, d'après la définition de l'intensité. "
                "En combinant ces deux relations, on obtient l'énergie "
                "électrique échangée par le dipôle : W égale U I Δt."
            )
        ) as tracker:
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes))

        # --- Définition énergie électrique --------------------------------------
        definition_W = definition_box(
            VGroup(
                Text("Énergie électrique échangée par un dipôle", font_size=23, weight="BOLD"),
                MathTex(r"W = U \, I \, t", font_size=32),
                Text("U en volts (V), I en ampères (A), t en secondes (s),", font_size=20),
                Text("W en joules (J).", font_size=20),
                Text("Un récepteur REÇOIT cette énergie ; un générateur la CÈDE.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        definition_W.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Définition : l'énergie électrique échangée par un dipôle "
                "vaut W égale U I t, avec la tension en volts, l'intensité "
                "en ampères, la durée en secondes, et l'énergie en joules. "
                "Un dipôle récepteur reçoit cette énergie du circuit, "
                "tandis qu'un dipôle générateur la cède au circuit."
            )
        ) as tracker:
            self.play(FadeIn(definition_W))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_W))

        # --- Définition puissance ------------------------------------------------
        definition_P = definition_box(
            VGroup(
                Text("Puissance électrique d'un dipôle", font_size=23, weight="BOLD"),
                MathTex(r"P = \dfrac{W}{t} = U \, I", font_size=32),
                Text("P en watts (W) : 1 W = 1 V × 1 A.", font_size=20),
                Text("La puissance est l'énergie échangée PAR UNITÉ DE TEMPS.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.0,
        )
        definition_P.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La puissance électrique d'un dipôle est le quotient de "
                "l'énergie échangée par la durée : P égale W sur t, ce qui "
                "se simplifie en P égale U I. Elle s'exprime en watts, et "
                "un watt correspond exactement à un volt multiplié par un "
                "ampère. La puissance représente donc l'énergie échangée "
                "par unité de temps."
            )
        ) as tracker:
            self.play(FadeIn(definition_P))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_P))

        # --- Exemple résolu 1 ------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Une lampe fonctionne sous U = 220 V, I = 0,45 A, pendant t = 2 h.", font_size=20),
                MathTex(r"P = U \, I = 220 \times 0{,}45 = 99\ \text{W}", font_size=27),
                MathTex(r"t = 2\ \text{h} = 7200\ \text{s}", font_size=27),
                MathTex(r"W = P \, t = 99 \times 7200 = 712\,800\ \text{J} \approx 7{,}13\times10^5\ \text{J}", font_size=26),
            ).arrange(DOWN, buff=0.25),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : une lampe fonctionne sous une tension de "
                "deux cent vingt volts, parcourue par un courant de "
                "quarante-cinq centièmes d'ampère, pendant deux heures. Sa "
                "puissance vaut U I, soit deux cent vingt fois zéro virgule "
                "quarante-cinq, c'est-à-dire quatre-vingt-dix-neuf watts. "
                "En convertissant la durée en secondes, deux heures "
                "donnent sept mille deux cents secondes. L'énergie "
                "consommée vaut alors P fois t, soit sept cent douze mille "
                "huit cents joules, environ sept virgule un trois fois dix "
                "puissance cinq joules."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"W = U I t \ (\text{J}), \qquad P = \dfrac{W}{t} = U I \ (\text{W})", font_size=27),
                Text("1 W = 1 V × 1 A. Récepteur : reçoit. Générateur : cède.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'énergie électrique vaut U I t, en "
                "joules, et la puissance électrique vaut U I, en watts. Un "
                "watt égale un volt fois un ampère. Un récepteur reçoit "
                "cette énergie, un générateur la cède au reste du circuit."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Toujours convertir la durée en SECONDES pour obtenir", font_size=20),
                Text("   W en joules (1 h = 3600 s), sinon le résultat est faux.", font_size=20),
                Text("• P = UI est valable pour TOUT dipôle, quelle que soit", font_size=20),
                Text("   sa nature (résistor, moteur, générateur…).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Il faut toujours convertir la durée "
                "en secondes pour obtenir une énergie en joules : une heure "
                "vaut trois mille six cents secondes, oublier cette "
                "conversion fausse complètement le résultat. Et la formule "
                "P égale U I est valable pour absolument tout dipôle, quelle "
                "que soit sa nature : résistor, moteur ou générateur."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
