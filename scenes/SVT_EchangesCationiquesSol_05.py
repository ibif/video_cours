"""
scenes/SVT_EchangesCationiquesSol_05.py — Chapitre 9 (1ereC, SVT), scène 05.

Conséquence des échanges cationiques : la nutrition minérale des plantes.
La racine libère des H+ qui chassent les cations nutritifs vers la
solution du sol ; schéma complet CAH / solution / racine ; Exemple résolu 1
(échange K+ / H+ complet en 4 étapes). Source : 1ereC/SVT.pdf, pages 99-100.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, exercise_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class NutritionMineraleDesPlantes(NotionScene):
    def construct(self):
        titre = scene_title("9.4 — Conséquence : la nutrition minérale")
        titre.scale(0.66)
        titre.to_edge(UP)

        # --- Énoncé : comment la plante « débloque »-t-elle ses réserves ? -
        intro = Text(
            _wrap(
                "Le complexe argilo-humique retient les cations "
                "nutritifs. Mais comment la racine, qui n'a pas de "
                "« pinces », parvient-elle à les récupérer ?",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le complexe argilo-humique retient les cations "
                "nutritifs à sa surface. Mais comment la racine, qui n'a "
                "pas de pince pour aller les chercher, parvient-elle "
                "malgré tout à les récupérer ? La réponse tient en un "
                "seul ion : l'ion hydrogène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : la racine libère des H+ -------------------------
        texte_meca = Text(
            _wrap(
                "Les racines des plantes absorbent les cations de la "
                "solution du sol. En contrepartie, elles libèrent des "
                "ions H+ qui se fixent sur le complexe et chassent les "
                "cations nutritifs (Ca2+, Mg2+, K+) vers la solution : la "
                "plante « débloque » ainsi les réserves du complexe.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        texte_meca.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici le mécanisme. Les racines des plantes absorbent "
                "les cations de la solution du sol. Mais en contrepartie, "
                "elles libèrent des ions hydrogène, qui viennent se fixer "
                "sur le complexe argilo-humique et chassent les cations "
                "nutritifs, calcium, magnésium, potassium, vers la "
                "solution. La plante débloque ainsi elle-même les "
                "réserves du complexe."
            )
        ) as tracker:
            self.play(FadeIn(texte_meca))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(texte_meca))

        # Schéma : CAH -- solution -- racine, avec échanges H+ / cations
        cah = Circle(radius=0.85, color=ORANGE, fill_color=ORANGE, fill_opacity=0.3, stroke_width=3)
        cah_label = Text("CAH", font_size=18, color=WHITE, weight="BOLD").move_to(cah.get_center())
        bloc_cah = VGroup(cah, cah_label)

        solution = Rectangle(width=2.6, height=1.5, color=WHITE, stroke_width=2)
        solution_label = Text("Solution\ndu sol", font_size=18, color=WHITE).move_to(solution.get_center())
        bloc_solution = VGroup(solution, solution_label)

        racine = Rectangle(width=1.8, height=1.5, color=GREEN, stroke_width=2, fill_color=GREEN, fill_opacity=0.15)
        racine_label = Text("Racine", font_size=18, color=GREEN).move_to(racine.get_center())
        bloc_racine = VGroup(racine, racine_label)

        schema_ligne = VGroup(bloc_cah, bloc_solution, bloc_racine).arrange(RIGHT, buff=1.2)
        schema_ligne.next_to(titre, DOWN, buff=0.85)

        fleche_cations = Arrow(
            bloc_cah.get_right(), bloc_solution.get_left(), buff=0.1, color=YELLOW, stroke_width=3
        ).shift(UP * 0.35)
        label_cations1 = Text("Ca2+, Mg2+, K+", font_size=14, color=YELLOW).next_to(fleche_cations, UP, buff=0.05)

        fleche_cations2 = Arrow(
            bloc_solution.get_right(), bloc_racine.get_left(), buff=0.1, color=YELLOW, stroke_width=3
        ).shift(UP * 0.35)

        fleche_h1 = Arrow(
            bloc_racine.get_left(), bloc_solution.get_right(), buff=0.1, color=RED, stroke_width=3
        ).shift(DOWN * 0.35)
        label_h = Text("H+", font_size=14, color=RED).next_to(fleche_h1, DOWN, buff=0.05)

        fleche_h2 = Arrow(
            bloc_solution.get_left(), bloc_cah.get_right(), buff=0.1, color=RED, stroke_width=3
        ).shift(DOWN * 0.35)

        schema = VGroup(
            schema_ligne, fleche_cations, label_cations1, fleche_cations2, fleche_h1, label_h, fleche_h2
        )

        with self.voiceover(
            text=(
                "Ce schéma résume les trois compartiments en jeu : le "
                "complexe argilo-humique, la solution du sol, et la "
                "racine. En jaune, les cations nutritifs, désorbés du "
                "complexe, traversent la solution du sol jusqu'à la "
                "racine, qui les absorbe. En rouge, en sens inverse, les "
                "ions hydrogène libérés par la racine traversent la "
                "solution et s'adsorbent sur le complexe, prenant la "
                "place des cations partis. Le complexe reconstitue ainsi "
                "en permanence la solution du sol, au fur et à mesure des "
                "prélèvements de la racine."
            )
        ) as tracker:
            self.play(FadeIn(schema_ligne))
            self.play(FadeIn(fleche_cations), FadeIn(label_cations1), FadeIn(fleche_cations2))
            self.play(FadeIn(fleche_h1), FadeIn(label_h), FadeIn(fleche_h2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité 1 : échange K+ / H+ en 4 étapes -----------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Exemple résolu 1 : on met en présence un sol riche "
                    "en ions H+ adsorbés avec une solution contenant des "
                    "ions K+. Décrire les échanges qui se produisent.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mettons en pratique avec un exemple résolu. On met en "
                "présence un sol riche en ions H+ adsorbés avec une "
                "solution contenant des ions potassium. Décrivons les "
                "échanges qui se produisent."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        resolution = corrige_box(
            _bullets(
                [
                    "Le complexe argilo-humique porte des charges "
                    "négatives occupées par des ions H+ adsorbés.",
                    "Les ions K+ de la solution sont attirés par les "
                    "charges négatives du complexe : il y a adsorption "
                    "des K+.",
                    "À charge égale (1 K+ pour 1 H+), les ions H+ sont "
                    "chassés du complexe vers la solution : il y a "
                    "désorption des H+.",
                    "Conclusion : il s'est produit un échange cationique "
                    "K+/H+ : le sol s'est enrichi en potassium retenu, et "
                    "la solution s'est chargée en H+ (elle devient plus "
                    "acide).",
                ],
                font_size=19,
                width=52,
            ),
            box_width=12.0,
        )
        resolution.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résolution en quatre étapes. Un : le complexe "
                "argilo-humique porte des charges négatives, occupées "
                "par des ions H+ adsorbés. Deux : les ions potassium de "
                "la solution sont attirés par ces charges négatives, il y "
                "a donc adsorption des ions K+. Trois : à charge égale, "
                "un potassium pour un hydrogène, les ions H+ sont chassés "
                "du complexe vers la solution, il y a désorption des H+. "
                "Quatre, conclusion : il s'est produit un échange "
                "cationique potassium contre hydrogène. Le sol s'est "
                "enrichi en potassium retenu, et la solution s'est "
                "chargée en ions H+, elle devient donc plus acide."
            )
        ) as tracker:
            self.play(FadeIn(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(resolution))
