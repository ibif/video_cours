"""
scenes/Chimie_Alcanes_11.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 11.

§ 7.2 La combustion incomplète (définition, produits CO et C en plus,
équations du méthane) + piège danger du monoxyde de carbone (toxicité,
fixation sur l'hémoglobine, contexte groupes électrogènes/délestages en
Côte d'Ivoire). Source : 1ereC/Chimie.pdf, page 22.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    GRAY,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class CombustionIncomplete(NotionScene):
    def construct(self):
        titre = scene_title("7. La combustion incomplète")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : que se passe-t-il si le dioxygène manque ? ---------------
        intro = Text(
            _wrap(
                "Que se passe-t-il si le dioxygène manque lors de la "
                "combustion d'un alcane, par exemple dans un appareil mal "
                "réglé ou une pièce mal aérée ?",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Que se passe-t-il si le dioxygène vient à manquer lors "
                "de la combustion d'un alcane, par exemple dans un "
                "appareil mal réglé ou une pièce mal aérée ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition de la combustion incomplète -------------
        definition = definition_box(
            Text(
                _wrap(
                    "Lorsque le dioxygène est en défaut, la combustion de "
                    "l'alcane est incomplète. Les produits sont alors "
                    "l'eau, le dioxyde de carbone, du carbone C (suie "
                    "noire) et du monoxyde de carbone CO.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Lorsque le dioxygène est en quantité insuffisante, la "
                "combustion de l'alcane est incomplète. Les produits de "
                "la réaction sont alors l'eau, le dioxyde de carbone, "
                "mais aussi du carbone, sous forme de suie noire, et du "
                "monoxyde de carbone, C-O."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : équations du méthane en combustion incomplète ----
        entete_eq = Text("Exemples : combustions incomplètes du méthane", font_size=21, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.4)

        eq1 = MathTex(r"2\,CH_4 + 3\,O_2 \rightarrow 2\,CO + 4\,H_2O", font_size=28, color=WHITE)
        eq2 = MathTex(r"CH_4 + O_2 \rightarrow C + 2\,H_2O", font_size=28, color=WHITE)
        equations = VGroup(eq1, eq2).arrange(DOWN, buff=0.5)
        equations.next_to(entete_eq, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici deux exemples d'équations-bilans de combustions "
                "incomplètes du méthane. D'abord, avec formation de "
                "monoxyde de carbone : deux méthane plus trois dioxygène "
                "donne deux monoxyde de carbone plus quatre eau. Ensuite, "
                "avec formation de carbone solide : méthane plus "
                "dioxygène donne carbone plus deux eau."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(eq1))
            self.play(Write(eq2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(equations))

        # --- À retenir : comparatif complète / incomplète -----------------------
        entete_comp = Text("Complète ou incomplète : des produits différents", font_size=21, color=YELLOW, weight="BOLD")
        entete_comp.next_to(titre, DOWN, buff=0.4)

        comparatif = _bullets(
            [
                "Combustion complète (excès de O₂) : uniquement CO₂ et "
                "H₂O.",
                "Combustion incomplète (défaut de O₂) : H₂O, CO₂, plus CO "
                "et/ou C (suie).",
            ],
            font_size=22,
            width=54,
        )
        comparatif.next_to(entete_comp, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la distinction essentielle : en combustion "
                "complète, avec excès de dioxygène, on n'obtient que du "
                "dioxyde de carbone et de l'eau. En combustion "
                "incomplète, avec un défaut de dioxygène, on obtient en "
                "plus du monoxyde de carbone et, ou, du carbone sous "
                "forme de suie."
            )
        ) as tracker:
            self.play(FadeIn(entete_comp))
            self.play(FadeIn(comparatif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_comp), FadeOut(comparatif))

        # --- Piège à éviter : danger du monoxyde de carbone ---------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le monoxyde de carbone CO est un gaz incolore, "
                    "inodore et très toxique : il se fixe sur "
                    "l'hémoglobine à la place du dioxygène et provoque "
                    "des asphyxies mortelles. Les groupes électrogènes "
                    "utilisés en intérieur pendant les délestages sont "
                    "une cause fréquente d'intoxication en Côte d'Ivoire : "
                    "toujours aérer une pièce où l'on brûle un "
                    "combustible.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Attention, danger : le monoxyde de carbone est un gaz "
                "incolore, inodore et très toxique. Il se fixe sur "
                "l'hémoglobine du sang à la place du dioxygène et "
                "provoque des asphyxies mortelles. Les chauffages mal "
                "aérés, et surtout les groupes électrogènes placés à "
                "l'intérieur des habitations pendant les délestages, sont "
                "des causes fréquentes d'intoxication en Côte d'Ivoire. Il "
                "faut toujours aérer les pièces où l'on brûle un "
                "combustible, et ne jamais faire fonctionner un groupe "
                "électrogène en intérieur."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
