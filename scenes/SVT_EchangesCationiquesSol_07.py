"""
scenes/SVT_EchangesCationiquesSol_07.py — Chapitre 9 (1ereC, SVT), scène 07.

La somme des bases échangeables S et le taux de saturation V : définitions
et formules, tableau d'interprétation, méthode point clé (fatigue des
sols = désaturation progressive), et Exemple résolu 2 (calcul complet
CEC/S/V pour un sol de plantation de cacao à Divo). Source : 1ereC/SVT.pdf,
pages 101-102.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, definition_box, exercise_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class SommeBasesEtTauxSaturation(NotionScene):
    def construct(self):
        titre = scene_title("9.6 — Somme des bases et taux de saturation")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : la CEC seule ne dit pas tout ---------------------------
        intro = Text(
            _wrap(
                "Deux sols peuvent avoir la même CEC, mais l'un rempli de "
                "bases nutritives et l'autre rempli d'ions H+ acidifiants. "
                "Comment distinguer ces deux situations ?",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux sols peuvent avoir exactement la même CEC, mais "
                "l'un rempli de bases nutritives et l'autre rempli d'ions "
                "hydrogène acidifiants. Comment distinguer ces deux "
                "situations, pourtant très différentes pour la plante ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définitions de S et V ----------------------------
        def_s = definition_box(
            Text(
                _wrap(
                    "La somme des bases échangeables, notée S, est la "
                    "somme des quantités de cations métalliques fixés sur "
                    "le complexe : S = Ca2+ + Mg2+ + K+ + Na+ (en "
                    "cmol+/kg).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_s.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "On appelle somme des bases échangeables, notée S, la "
                "somme des quantités de cations métalliques fixés sur le "
                "complexe : calcium, plus magnésium, plus potassium, plus "
                "sodium, en cmol plus par kilogramme. Attention : les ions "
                "H+ ne font jamais partie de S, puisque ce ne sont pas des "
                "bases."
            )
        ) as tracker:
            self.play(FadeIn(def_s))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_s))

        def_v = definition_box(
            Text(
                _wrap(
                    "Le taux de saturation, noté V, est le pourcentage de "
                    "la CEC occupée par les bases échangeables : "
                    "V = (S/CEC) × 100, exprimé en pourcentage.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        def_v.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On appelle taux de saturation, noté V, le pourcentage de "
                "la CEC occupée par les bases échangeables : V égale S "
                "divisé par CEC, multiplié par cent, exprimé en "
                "pourcentage. Plus V est proche de cent pour cent, plus le "
                "complexe est saturé en bases nutritives."
            )
        ) as tracker:
            self.play(FadeIn(def_v))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_v))

        # --- Tableau d'interprétation du taux de saturation -----------------
        interp_titre = Text("Interprétation du taux de saturation V", font_size=23, color=YELLOW, weight="BOLD")
        interp_titre.next_to(titre, DOWN, buff=0.5)

        col1 = VGroup(
            Text("V proche de 100%", font_size=20, color=GREEN),
            Text("V faible (< 50%)", font_size=20, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        col2 = VGroup(
            Text("Complexe saturé en bases", font_size=20, color=WHITE),
            Text("Complexe désaturé", font_size=20, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        col3 = VGroup(
            Text("Sol riche, pH voisin de la\nneutralité", font_size=18, color=WHITE),
            Text("Beaucoup de H+/Al3+ adsorbés :\nsol acide, pauvre", font_size=18, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        tableau = VGroup(col1, col2, col3).arrange(RIGHT, buff=0.5, aligned_edge=UP)
        tableau.next_to(interp_titre, DOWN, buff=0.4)
        tableau.scale(0.95)

        with self.voiceover(
            text=(
                "Voici comment interpréter le taux de saturation. Quand V "
                "est proche de cent pour cent, le complexe est saturé en "
                "bases : le sol est riche en éléments nutritifs, avec un "
                "pH neutre ou voisin de la neutralité. Quand V est "
                "faible, en dessous de cinquante pour cent, le complexe "
                "est désaturé : beaucoup d'ions H+ et d'aluminium sont "
                "adsorbés, le sol est acide et pauvre en bases nutritives."
            )
        ) as tracker:
            self.play(FadeIn(interp_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interp_titre), FadeOut(tableau))

        # --- À retenir : la fatigue des sols = désaturation progressive -----
        methode = method_box(
            Text(
                _wrap(
                    "Point clé : plus le taux de saturation est élevé, "
                    "plus le sol est fertile. La fatigue des sols "
                    "correspond à une désaturation progressive du "
                    "complexe : les bases nutritives sont remplacées par "
                    "des ions H+.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé : plus le taux de saturation est "
                "élevé, plus le sol est fertile. La fatigue des sols, "
                "dont nous reparlerons, correspond justement à une "
                "désaturation progressive du complexe : les bases "
                "nutritives y sont peu à peu remplacées par des ions H+."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité 2 : sol de cacao à Divo --------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Exemple résolu 2 : l'analyse d'un sol de plantation "
                    "de cacao à Divo donne, en cmol+/kg : Ca2+ = 6 ; "
                    "Mg2+ = 2,5 ; K+ = 0,4 ; Na+ = 0,1 ; H+ = 3. Calculer "
                    "la CEC, la somme des bases S, le taux de saturation "
                    "V. Conclure sur la fertilité du sol.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Appliquons cela à un cas concret. L'analyse d'un sol de "
                "plantation de cacao à Divo donne les teneurs suivantes, "
                "en cmol plus par kilogramme : calcium six, magnésium "
                "deux virgule cinq, potassium zéro virgule quatre, sodium "
                "zéro virgule un, hydrogène trois. Calculons la CEC, la "
                "somme des bases S, le taux de saturation V, et concluons "
                "sur la fertilité de ce sol."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc_cec = MathTex(
            r"CEC = 6+2{,}5+0{,}4+0{,}1+3 = 12\ cmol^+/kg",
            font_size=26,
            color=WHITE,
        )
        calc_s = MathTex(
            r"S = 6+2{,}5+0{,}4+0{,}1 = 9\ cmol^+/kg",
            font_size=26,
            color=WHITE,
        )
        calc_v = MathTex(
            r"V = \dfrac{9}{12}\times 100 = 75\%",
            font_size=26,
            color=WHITE,
        )
        calculs = VGroup(calc_cec, calc_s, calc_v).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        calculs.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "D'abord la CEC : six plus deux virgule cinq plus zéro "
                "virgule quatre plus zéro virgule un plus trois, égale "
                "douze cmol plus par kilogramme. Ensuite la somme des "
                "bases S : six plus deux virgule cinq plus zéro virgule "
                "quatre plus zéro virgule un, égale neuf cmol plus par "
                "kilogramme, sans le H+. Enfin le taux de saturation V : "
                "neuf divisé par douze, multiplié par cent, égale "
                "soixante-quinze pour cent."
            )
        ) as tracker:
            self.play(Write(calc_cec))
            self.play(Write(calc_s))
            self.play(Write(calc_v))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calculs))

        conclusion = corrige_box(
            Text(
                _wrap(
                    "Conclusion : la CEC est moyenne (12 cmol+/kg) et le "
                    "complexe est saturé aux trois quarts (V = 75%) : le "
                    "sol est encore assez fertile, mais la présence de "
                    "3 cmol+/kg de H+ signale une acidification en cours "
                    "(fatigue du sol).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Conclusion : la CEC est moyenne, douze cmol plus par "
                "kilogramme, et le complexe est saturé aux trois quarts, "
                "avec un V de soixante-quinze pour cent. Ce sol est donc "
                "encore assez fertile. Mais la présence de trois cmol "
                "plus par kilogramme d'ions H+ signale une acidification "
                "déjà en cours : c'est le tout début d'une fatigue du "
                "sol, à surveiller."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(conclusion))
