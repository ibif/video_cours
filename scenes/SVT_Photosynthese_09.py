"""
scenes/SVT_Photosynthese_09.py — Chapitre 10 (1ereC, SVT), scène 09.

§ 10.4.2-10.4.3 (étapes 2 et 3) Réduction du PGA en PGAL (équation MathTex
avec ATP et NADPH,H+) + formation du glucose et régénération du RuBP (2
PGAL sur 12 -> glucose, 10 PGAL sur 12 -> régénération) + bilan
quantitatif du cycle de Calvin (équation MathTex complète pour 1 glucose =
6 tours) + méthode point clé « vérification par les atomes de carbone ».
Source : 1ereC/SVT.pdf, page 110.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class CycleDeCalvinReductionEtBilan(NotionScene):
    def construct(self):
        titre = scene_title("10.4.2-10.4.3 — Réduction, glucose et bilan du cycle")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : étape 2, réduction du PGA en PGAL -----------------------
        etape2_texte = Text(
            _wrap(
                "Étape 2 — Réduction du PGA : le PGA est réduit en "
                "PGAL (glycéraldéhyde-3-phosphate, sucre à 3 carbones) "
                "grâce à l'énergie de l'ATP et au pouvoir réducteur du "
                "NADPH,H+ produits par la phase claire.",
                width=56,
            ),
            font_size=21,
            color=WHITE,
        )
        etape2_texte.next_to(titre, DOWN, buff=0.5)

        equation2 = MathTex(
            r"PGA + ATP + NADPH,H^+ \longrightarrow PGAL + ADP + P_i + NADP^+",
            font_size=25,
            color=YELLOW,
        )
        equation2.next_to(etape2_texte, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième étape du cycle : la réduction du PGA. Le PGA "
                "est réduit en PGAL, le glycéraldéhyde trois phosphate, "
                "un sucre à trois carbones, grâce à l'énergie de l'ATP "
                "et au pouvoir réducteur du NADPH,H plus, tous deux "
                "produits par la phase claire. L'équation s'écrit : PGA "
                "plus ATP plus NADPH,H plus donnent PGAL, plus ADP, "
                "phosphate inorganique et NADP plus."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(etape2_texte))
            self.play(Write(equation2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape2_texte), FadeOut(equation2))

        # --- Animation du raisonnement : étape 3, glucose et régénération -----
        etape3_texte = _bullets(
            [
                "Sur les 12 molécules de PGAL formées à chaque cycle "
                "complet : 2 PGAL servent à fabriquer le glucose, "
                "précurseur de l'amidon, de la cellulose, etc.",
                "Les 10 PGAL restants servent à régénérer le RuBP (en "
                "consommant encore de l'ATP), ce qui permet au cycle de "
                "continuer.",
            ],
            font_size=21,
            width=52,
        )
        etape3_texte.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Troisième étape : la formation du glucose et la "
                "régénération du RuBP. Sur les douze molécules de PGAL "
                "formées à chaque cycle complet, deux seulement servent "
                "à fabriquer le glucose, précurseur de l'amidon, de la "
                "cellulose et de bien d'autres molécules organiques. Les "
                "dix PGAL restants servent à régénérer le RuBP, en "
                "consommant encore de l'ATP, ce qui permet au cycle de "
                "continuer indéfiniment tant que le CO2 et la lumière "
                "sont disponibles."
            )
        ) as tracker:
            self.play(FadeIn(etape3_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape3_texte))

        # --- Exemple traité : bilan quantitatif du cycle de Calvin -------------
        bilan_texte = Text(
            "Pour fabriquer 1 glucose, il faut fixer 6 CO2, soit 6 tours de cycle :",
            font_size=19,
            color=WHITE,
        )
        bilan_texte.next_to(titre, DOWN, buff=0.5)

        equation_bilan = MathTex(
            r"6\,CO_2 + 12\,NADPH,H^+ + 18\,ATP \longrightarrow "
            r"C_6H_{12}O_6 + 12\,NADP^+ + 18\,ADP + 18\,P_i + 6\,H_2O",
            font_size=22,
            color=YELLOW,
        )
        equation_bilan.next_to(bilan_texte, DOWN, buff=0.5)
        equation_bilan.set(width=min(equation_bilan.width, 12.5))

        with self.voiceover(
            text=(
                "Un seul tour de cycle ne fixe qu'un seul CO2 : il faut "
                "donc six tours complets pour rassembler les six atomes "
                "de carbone nécessaires à une molécule de glucose. Voici "
                "le bilan quantitatif complet du cycle de Calvin, pour "
                "fabriquer une molécule de glucose : six CO2, douze "
                "NADPH,H plus et dix-huit ATP donnent une molécule de "
                "glucose, douze NADP plus, dix-huit ADP, dix-huit "
                "phosphates inorganiques et six molécules d'eau."
            )
        ) as tracker:
            self.play(FadeIn(bilan_texte))
            self.play(Write(equation_bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bilan_texte), FadeOut(equation_bilan))

        # --- À retenir : bilan compact en boîte théorème -----------------------
        theoreme = theorem_box(
            MathTex(
                r"6\,CO_2 + 12\,NADPH,H^+ + 18\,ATP \longrightarrow "
                r"C_6H_{12}O_6 + 12\,NADP^+ + 18\,ADP + 18\,P_i + 6\,H_2O",
                font_size=20,
            ),
            box_width=12.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ce bilan quantitatif du cycle de Calvin est à retenir : "
                "il montre précisément combien d'ATP et de NADPH,H plus "
                "de la phase claire sont nécessaires pour fabriquer une "
                "seule molécule de glucose dans la phase sombre."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Méthode : vérification par les atomes de carbone -------------------
        methode = method_box(
            _bullets(
                [
                    "6 CO2 apportent 6 atomes de carbone.",
                    "Le glucose C6H12O6 en contient 6.",
                    "Le bilan est cohérent : tout le carbone de la "
                    "matière organique végétale provient du CO2 de "
                    "l'air.",
                ],
                font_size=19,
                width=50,
            ),
            box_width=11.5,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé de méthode : vérifions ce bilan par les "
                "atomes de carbone. Six CO2 apportent six atomes de "
                "carbone ; le glucose en contient six : le bilan est "
                "cohérent. Retenez cette idée fondamentale : tout le "
                "carbone de la matière organique végétale provient du "
                "dioxyde de carbone de l'air, capté grâce à ce cycle."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : un seul tour ne fait pas un glucose --------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : un seul tour de cycle ne produit "
                    "jamais un glucose entier (il ne fixe qu'un seul "
                    "CO2, donc un seul carbone). Il faut TOUJOURS "
                    "raisonner sur 6 tours de cycle pour obtenir les 6 "
                    "carbones d'une molécule de glucose.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter absolument : un seul tour de cycle ne "
                "produit jamais un glucose entier, puisqu'il ne fixe "
                "qu'un seul CO2, donc un seul carbone. Il faut toujours "
                "raisonner sur six tours de cycle pour obtenir les six "
                "carbones nécessaires à une molécule de glucose."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
