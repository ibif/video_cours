"""
scenes/Physique_PuissanceEnergieElectriques_08.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 08.

§ 7 (partie 1). Le kilowattheure. Définition 1 kWh = 10³ W × 3600 s =
3,6×10⁶ J. Règle pratique W(kWh) = P(kW) × t(h). Le compteur électrique
(index, disjoncteur de branchement, puissance maximale = U × I_calibre).
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 7).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _compteur_schema():
    """Compteur électrique simplifié : boîtier avec un afficheur d'index
    et un disjoncteur de branchement."""
    boitier = Rectangle(width=2.6, height=1.8, color=WHITE, stroke_width=3)
    ecran = Rectangle(width=1.9, height=0.55, color=YELLOW, stroke_width=2, fill_color=YELLOW, fill_opacity=0.12)
    ecran.move_to(boitier.get_center() + UP * 0.4)
    index_txt = Text("012458", font_size=22, color=YELLOW).move_to(ecran.get_center())
    label_kwh = Text("kWh", font_size=14, color=WHITE).next_to(ecran, RIGHT, buff=0.08)

    disjoncteur = Rectangle(width=0.7, height=0.9, color=WHITE, stroke_width=2)
    disjoncteur.move_to(boitier.get_center() + DOWN * 0.55)
    levier = Rectangle(width=0.14, height=0.4, color=YELLOW, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
    levier.move_to(disjoncteur.get_center())
    label_disj = Text("disjoncteur", font_size=13, color=WHITE).next_to(disjoncteur, DOWN, buff=0.08)

    label_compteur = Text("compteur", font_size=15, color=WHITE).next_to(boitier, UP, buff=0.1)

    return VGroup(boitier, ecran, index_txt, label_kwh, disjoncteur, levier, label_disj, label_compteur)


class Kilowattheure(NotionScene):
    def construct(self):
        titre = scene_title("Le kilowattheure")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Le joule est une unité d'énergie minuscule à l'échelle "
                "domestique : une facture d'électricité en joules donnerait "
                "des nombres à dix chiffres. D'où l'usage d'une unité plus "
                "pratique, le kilowattheure.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le joule est une unité d'énergie minuscule à l'échelle "
                "domestique : une facture d'électricité exprimée en joules "
                "donnerait des nombres à dix chiffres. C'est pourquoi on "
                "utilise une unité plus pratique au quotidien, le "
                "kilowattheure."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition du kWh -----------------------------------
        definition = definition_box(
            VGroup(
                Text("Le kilowattheure (kWh) est l'énergie consommée par un", font_size=21),
                Text("appareil de puissance 1 kW pendant 1 heure.", font_size=21),
                MathTex(r"1\ \text{kWh} = 10^3\ \text{W} \times 3600\ \text{s} = 3{,}6\times10^6\ \text{J}", font_size=28),
            ).arrange(DOWN, buff=0.22),
            box_width=11.4,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le kilowattheure, noté kWh, est l'énergie consommée par un "
                "appareil de puissance mille watts, c'est-à-dire un "
                "kilowatt, fonctionnant pendant une heure. Un kilowattheure "
                "vaut donc dix puissance trois watts, fois trois mille six "
                "cents secondes, soit trois virgule six millions de joules."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        regle = method_box(
            VGroup(
                Text("Règle pratique : pour calculer une énergie directement", font_size=21),
                Text("en kWh, exprimer P en kW et t en heures :", font_size=21),
                MathTex(r"W(\text{kWh}) = P(\text{kW}) \times t(\text{h})", font_size=30, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=11.2,
        )
        regle.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En pratique, pour calculer directement une énergie en "
                "kilowattheures, il suffit d'exprimer la puissance en "
                "kilowatts et la durée en heures, puis de les multiplier : "
                "W en kilowattheures égale P en kilowatts, fois t en heures. "
                "Plus besoin de passer par les secondes ni par les joules."
            )
        ) as tracker:
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle))

        # --- Le compteur électrique --------------------------------------------
        compteur = _compteur_schema()
        compteur.scale(1.1)
        compteur.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le compteur électrique de l'habitation totalise, en "
                "kilowattheures, toute l'énergie consommée depuis son "
                "installation : c'est ce qu'on appelle l'index. Il intègre "
                "aussi un disjoncteur de branchement, qui coupe "
                "automatiquement le courant si l'intensité appelée dépasse "
                "le calibre souscrit, protégeant ainsi l'installation."
            )
        ) as tracker:
            self.play(FadeIn(compteur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(compteur))

        # --- Exemple résolu -----------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un fer à repasser de 1200 W fonctionne pendant 30 minutes.", font_size=20),
                MathTex(r"P = 1{,}2\ \text{kW}, \quad t = 0{,}5\ \text{h}", font_size=25),
                MathTex(r"W = P \times t = 1{,}2 \times 0{,}5 = 0{,}6\ \text{kWh}", font_size=27),
                Text("Puissance maximale du compteur : P_max = U × I_calibre", font_size=20),
                MathTex(r"P_{max} = 220 \times 30 = 6600\ \text{W} = 6{,}6\ \text{kW}", font_size=25),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : un fer à repasser de mille deux cents "
                "watts fonctionne pendant trente minutes. En kilowatts, sa "
                "puissance vaut un virgule deux, et la durée vaut zéro "
                "virgule cinq heure. L'énergie consommée vaut donc zéro "
                "virgule six kilowattheure. Pour le compteur lui-même, la "
                "puissance maximale disponible vaut U fois l'intensité de "
                "calibre du disjoncteur : sous deux cent vingt volts et un "
                "calibre de trente ampères, cela donne six mille six cents "
                "watts, soit six virgule six kilowatts."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"1\ \text{kWh} = 3{,}6\times10^6\ \text{J}, \qquad W(\text{kWh}) = P(\text{kW}) \times t(\text{h})", font_size=25),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : un kilowattheure vaut trois virgule "
                "six millions de joules, et pour le calculer directement, "
                "on multiplie la puissance en kilowatts par la durée en "
                "heures."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne jamais mélanger les unités : soit tout en (W, s, J),", font_size=20),
                Text("   soit tout en (kW, h, kWh) — jamais un mélange des deux.", font_size=20),
                Text("• 1 kWh ≠ 1000 J : ne pas confondre kilowattheure (énergie)", font_size=20),
                Text("   et kilojoule (autre unité d'énergie, bien plus petite).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter absolument. Il ne faut jamais mélanger "
                "les systèmes d'unités : soit tout en watts, secondes et "
                "joules, soit tout en kilowatts, heures et kilowattheures, "
                "jamais un mélange des deux. Et un kilowattheure n'est "
                "surtout pas égal à mille joules : ce serait confondre le "
                "kilowattheure avec le kilojoule, une unité d'énergie bien "
                "plus petite."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
