"""
scenes/Chimie_Alcanes_05.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 05.

§ Exemple résolu 1 : nommer CH₃–CH(CH₃)–CH₂–CH(C₂H₅)–CH₃ en 3 étapes
(→ 4-éthyl-2-méthylhexane, choix du sens de numérotation 2+4<3+5).
§ Exemple résolu 2 : nommer CH₃–C(CH₃)₂–CH(CH₃)–CH₃ (→
2,2,3-triméthylbutane, indice répété). Source : 1ereC/Chimie.pdf, page 18.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, exercise_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ExemplesNommageAlcanesRamifies(NotionScene):
    def construct(self):
        titre = scene_title("3. Nommer un alcane ramifié : deux exemples résolus")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : appliquons les 5 règles ------------------------------------
        intro = Text(
            _wrap(
                "Appliquons maintenant les cinq règles de nomenclature de "
                "l'UICPA à deux alcanes ramifiés concrets.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Appliquons maintenant les cinq règles de nomenclature de "
                "l'UICPA à deux alcanes ramifiés concrets."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement + Exemple traité : exemple résolu 1 -------------------
        enonce1 = exercise_box(
            MathTex(r"CH_3-CH(CH_3)-CH_2-CH(C_2H_5)-CH_3", font_size=28, color="#1A1A1A"),
            box_width=10.5,
        )
        enonce1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier exemple : nommons l'alcane de formule "
                "semi-développée C-H-3, C-H parenthèse C-H-3 fermée "
                "parenthèse, C-H-2, C-H parenthèse C-2 H-5 fermée "
                "parenthèse, C-H-3."
            )
        ) as tracker:
            self.play(FadeIn(enonce1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce1))

        etape1 = Text(
            _wrap(
                "Étape 1 — chaîne principale : la chaîne la plus longue "
                "contient 6 atomes de carbone en passant par le groupe "
                "éthyle : c'est un dérivé de l'hexane.",
                width=50,
            ),
            font_size=22,
            color=WHITE,
        )
        etape1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Étape un : on recherche la chaîne principale. La chaîne "
                "la plus longue ne suit pas forcément l'horizontale du "
                "dessin : ici, en passant par le groupe éthyle, elle "
                "contient six atomes de carbone. C'est donc un dérivé de "
                "l'hexane."
            )
        ) as tracker:
            self.play(FadeIn(etape1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape1))

        etape2_titre = Text("Étape 2 — numérotation : quel sens choisir ?", font_size=22, color=YELLOW, weight="BOLD")
        etape2_titre.next_to(titre, DOWN, buff=0.4)

        comparaison = MathTex(
            r"\text{gauche} : 2+4=6 \qquad\qquad \text{droite} : 3+5=8",
            font_size=28,
            color=WHITE,
        )
        comparaison.next_to(etape2_titre, DOWN, buff=0.45)

        conclusion2 = MathTex(r"6 < 8 \;\Rightarrow\; \text{on numérote à partir de la gauche}", font_size=26, color=GREEN)
        conclusion2.next_to(comparaison, DOWN, buff=0.4)

        groupe_etape2 = VGroup(etape2_titre, comparaison, conclusion2)

        with self.voiceover(
            text=(
                "Étape deux : la numérotation. En numérotant à partir de "
                "la gauche, les substituants portent les numéros deux, "
                "pour le méthyle, et quatre, pour l'éthyle, soit une "
                "somme de six. En numérotant à partir de la droite, ce "
                "serait trois et cinq, soit une somme de huit. Comme six "
                "est inférieur à huit, on numérote à partir de la "
                "gauche."
            )
        ) as tracker:
            self.play(FadeIn(etape2_titre))
            self.play(Write(comparaison))
            self.play(Write(conclusion2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_etape2))

        etape3_titre = Text("Étape 3 — nom final (ordre alphabétique)", font_size=22, color=YELLOW, weight="BOLD")
        etape3_titre.next_to(titre, DOWN, buff=0.4)

        nom_final1 = corrige_box(
            Text("4-éthyl-2-méthylhexane", font_size=30, weight="BOLD"),
            box_width=8.0,
        )
        nom_final1.next_to(etape3_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étape trois : on cite les substituants par ordre "
                "alphabétique, éthyle avant méthyle. Le nom complet est "
                "donc : quatre-éthyl-deux-méthylhexane."
            )
        ) as tracker:
            self.play(FadeIn(etape3_titre))
            self.play(FadeIn(nom_final1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape3_titre), FadeOut(nom_final1))

        # --- Exemple traité : exemple résolu 2 (indice répété) ------------------
        enonce2 = exercise_box(
            MathTex(r"CH_3-C(CH_3)_2-CH(CH_3)-CH_3", font_size=28, color="#1A1A1A"),
            box_width=9.0,
        )
        enonce2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Second exemple, où un même indice se répète : nommons "
                "l'alcane C-H-3, C parenthèse C-H-3 fermée parenthèse "
                "indice deux, C-H parenthèse C-H-3 fermée parenthèse, "
                "C-H-3."
            )
        ) as tracker:
            self.play(FadeIn(enonce2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce2))

        resolution2 = corrige_box(
            VGroup(
                Text(
                    "Chaîne principale : 4 carbones (butane).\n"
                    "3 méthyles portent les numéros 2, 2 et 3.",
                    font_size=22,
                ),
                Text("2,2,3-triméthylbutane", font_size=28, weight="BOLD"),
            ).arrange(DOWN, buff=0.35),
            box_width=9.0,
        )
        resolution2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La chaîne principale compte quatre carbones : c'est un "
                "dérivé du butane. Trois groupes méthyle portent les "
                "numéros deux, deux et trois. Le nom est donc "
                "deux-virgule-deux-virgule-trois-triméthylbutane. "
                "Remarquez que l'indice deux est répété deux fois, "
                "séparé par une virgule, avant l'indice trois."
            )
        ) as tracker:
            self.play(FadeIn(resolution2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution2))

        # --- À retenir : méthode condensée ---------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "1) Trouver la chaîne la plus longue (elle peut passer "
                    "par une branche). 2) Numéroter dans le sens qui "
                    "minimise la somme des indices. 3) Nommer par ordre "
                    "alphabétique, en regroupant les substituants "
                    "identiques (di, tri…) avec indices répétés.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.5,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la méthode : un, trouver la chaîne la plus "
                "longue, qui peut très bien passer par une branche ; "
                "deux, numéroter dans le sens qui minimise la somme des "
                "indices de position ; trois, nommer par ordre "
                "alphabétique, en regroupant les substituants identiques "
                "avec di, tri, tétra, et en répétant l'indice de position "
                "autant de fois que nécessaire."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : bien choisir le sens de numérotation --------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne numérotez jamais « au hasard » : comparez toujours "
                    "la SOMME (ou, en cas d'égalité, la suite chiffre par "
                    "chiffre) des indices obtenus dans les deux sens, et "
                    "gardez le sens qui donne les indices les plus petits.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : ne numérotez jamais au hasard. Comparez "
                "toujours la somme des indices obtenus dans les deux sens "
                "possibles — ou, en cas d'égalité, la suite des indices "
                "chiffre par chiffre — et conservez le sens qui donne les "
                "indices les plus petits."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
