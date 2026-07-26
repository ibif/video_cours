"""
scenes/SVT_AbsorptionNutriments_07.py — Chapitre 13 (1ereD, SVT), scène 07.

§ 13.3.2-13.3.3 Le transport actif : mise en situation, définition,
exemples, preuves expérimentales (sac intestinal + cyanure + froid,
figure 13.2), récapitulatif des modes d'absorption par nutriment, et les
deux pièges du transport.
Source : 1ereD/SVT.pdf, pages 173-175.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREEN,
    ORANGE,
    RED,
    Arrow,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class TransportActif(NotionScene):
    def construct(self):
        titre = scene_title("13.3.2 — Le transport actif")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation, le glucose contre le gradient -------
        intro = Text(
            _wrap(
                "Après un repas, il arrive que la concentration en "
                "glucose du sang des villosités dépasse celle de la "
                "lumière intestinale. Pourtant, le glucose continue "
                "d'être absorbé : contre le gradient. Un tel déplacement "
                "est impossible par simple diffusion.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Après un repas, il arrive que la concentration en "
                "glucose dans le sang des villosités devienne supérieure "
                "à celle de la lumière intestinale. Pourtant, le glucose "
                "continue d'être absorbé : il passe alors du milieu le "
                "moins concentré vers le milieu le plus concentré, c'est-"
                "à-dire contre le gradient. Un tel déplacement est "
                "impossible par simple diffusion."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        definition = definition_box(
            Text(
                _wrap(
                    "Le transport actif est le passage d'une substance à "
                    "travers une membrane, du milieu le moins concentré "
                    "vers le milieu le plus concentré (contre le "
                    "gradient), grâce à des protéines transporteuses "
                    "membranaires et grâce à l'énergie fournie par la "
                    "respiration cellulaire sous forme d'ATP.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le transport actif est le passage d'une substance à "
                "travers une membrane, du milieu le moins concentré vers "
                "le milieu le plus concentré, contre le gradient, grâce à "
                "des protéines transporteuses membranaires et grâce à "
                "l'énergie fournie par la respiration cellulaire sous "
                "forme d'ATP. Le glucose et les acides aminés sont "
                "absorbés par transport actif : un transporteur "
                "membranaire les fait entrer dans l'entérocyte en même "
                "temps que des ions sodium, grâce à l'énergie de l'ATP. De "
                "nombreux sels minéraux, sodium, calcium, fer, sont "
                "également absorbés par transport actif."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : preuve expérimentale (figure 13.2) --
        entete_preuve = Text("Preuve expérimentale : cyanure et froid", font_size=24, color=YELLOW, weight="BOLD")
        entete_preuve.next_to(titre, DOWN, buff=0.5)

        temoin = Rectangle(width=2.6, height=1.6, color=GREEN, fill_color=GREEN, fill_opacity=0.25, stroke_width=3)
        temoin_label = Text("Témoin, 37°C", font_size=17, color=GREEN)
        temoin_label.next_to(temoin, UP, buff=0.15)
        temoin_valeur = Text("glucose ↑ normalement", font_size=15, color=GREEN)
        temoin_valeur.move_to(temoin.get_center())

        cyanure = Rectangle(width=2.6, height=1.6, color=RED, fill_color=RED, fill_opacity=0.25, stroke_width=3)
        cyanure_label = Text("+ cyanure (ou 4°C)", font_size=17, color=RED)
        cyanure_label.next_to(cyanure, UP, buff=0.15)
        cyanure_valeur = Text("glucose bloqué", font_size=15, color=RED)
        cyanure_valeur.move_to(cyanure.get_center())

        temoin_grp = VGroup(temoin, temoin_label, temoin_valeur)
        cyanure_grp = VGroup(cyanure, cyanure_label, cyanure_valeur)
        paire = VGroup(temoin_grp, cyanure_grp).arrange(RIGHT, buff=1.2)
        paire.next_to(entete_preuve, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Reprenons l'expérience du sac intestinal. Si l'on ajoute "
                "dans le bain du cyanure, un poison qui bloque la "
                "respiration cellulaire, donc la production d'ATP, "
                "l'entrée du glucose dans le sac s'arrête presque "
                "totalement. On obtient un blocage semblable en "
                "refroidissant le milieu à quatre degrés, température à "
                "laquelle les réactions cellulaires sont ralenties. En "
                "revanche, l'absorption du fructose, passive, n'est pas "
                "affectée par le cyanure : conclusion, l'absorption du "
                "glucose est un phénomène actif, qui exige de l'énergie."
            )
        ) as tracker:
            self.play(FadeIn(entete_preuve))
            self.play(FadeIn(paire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_preuve), FadeOut(paire))

        # --- Exemple traité : lecture de la figure 13.2 ------------------------
        exemple = example_box(
            _bullets(
                [
                    "Témoin à 37°C : le glucose dans le sac passe de 0 à 2,9 g/L en 45 min.",
                    "Intestin au cyanure : le glucose ne dépasse pas 0,15 g/L en 45 min.",
                    "Seule différence entre les deux lots : le blocage de la production d'ATP.",
                    "Conclusion : sans énergie, l'absorption du glucose ne se fait plus — c'est un transport actif.",
                ],
                font_size=18,
                width=56,
            ),
            box_width=12.3,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exploitons la figure treize point deux. Chez l'intestin "
                "témoin maintenu à trente-sept degrés, la concentration en "
                "glucose à l'intérieur du sac passe de zéro à deux virgule "
                "neuf grammes par litre en quarante-cinq minutes : le "
                "glucose traverse activement la paroi intestinale. Chez "
                "l'intestin traité au cyanure, la concentration ne dépasse "
                "pas zéro virgule quinze gramme par litre au bout de "
                "quarante-cinq minutes : l'entrée du glucose est "
                "quasiment stoppée. La seule différence entre les deux "
                "lots est le blocage de la respiration cellulaire, "
                "c'est-à-dire l'absence de production d'ATP. Conclusion : "
                "sans énergie fournie par la respiration cellulaire, "
                "l'absorption du glucose ne se fait plus — il s'agit donc "
                "bien d'un transport actif."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : tableau récapitulatif des modes d'absorption ----------
        tab_titre = Text("Récapitulatif : mode d'absorption par nutriment", font_size=20, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.45)

        nutriments = [
            "Glucose, galactose", "Fructose", "Acides aminés",
            "Acides gras, glycérol", "Eau", "Sels minéraux",
            "Vitamines hydrosolubles", "Vitamines liposolubles",
        ]
        modes = [
            "transport actif", "diffusion facilitée", "transport actif",
            "diffusion simple", "osmose", "actif ou diffusion",
            "diffusion", "avec les lipides",
        ]
        voies = ["sang", "sang", "sang", "lymphe", "sang", "sang", "sang", "lymphe"]
        couleurs = [ORANGE, BLUE, ORANGE, GREEN, BLUE, ORANGE, BLUE, GREEN]

        col1 = VGroup(*[Text(n, font_size=15, color=WHITE) for n in nutriments]).arrange(DOWN, aligned_edge=LEFT, buff=0.185)
        col2 = VGroup(*[Text(m, font_size=15, color=couleurs[i]) for i, m in enumerate(modes)]).arrange(DOWN, aligned_edge=LEFT, buff=0.185)
        col3 = VGroup(*[Text(v, font_size=15, color=WHITE) for v in voies]).arrange(DOWN, aligned_edge=LEFT, buff=0.185)

        tableau = VGroup(col1, col2, col3).arrange(RIGHT, buff=0.55, aligned_edge=UP)
        tableau.next_to(tab_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici un récapitulatif complet. Le glucose et le "
                "galactose sont absorbés par transport actif, vers le "
                "sang. Le fructose, par diffusion facilitée, vers le "
                "sang. Les acides aminés, par transport actif, vers le "
                "sang. Les acides gras et le glycérol, par diffusion "
                "simple, vers la lymphe, après transformation. L'eau, par "
                "osmose, vers le sang. Les sels minéraux, par transport "
                "actif ou par diffusion, vers le sang. Les vitamines "
                "hydrosolubles, B et C, par diffusion, vers le sang. Les "
                "vitamines liposolubles, A, D, E, K, suivent les lipides, "
                "vers la lymphe."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- Pièges à éviter : les deux pièges du transport -----------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Premier piège : croire que la diffusion fait passer "
                    "les substances du milieu pauvre vers le milieu "
                    "riche — c'est l'inverse, elle descend toujours le "
                    "gradient. Deuxième piège : oublier l'énergie. Dès "
                    "qu'un passage se fait contre le gradient, il faut "
                    "invoquer un transport actif et une dépense d'ATP : "
                    "« le glucose diffuse contre son gradient » est une "
                    "contradiction.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux pièges à éviter absolument. Premier piège : croire "
                "que la diffusion fait passer les substances du milieu "
                "pauvre vers le milieu riche. C'est l'inverse : la "
                "diffusion descend toujours le gradient, du plus concentré "
                "vers le moins concentré. Deuxième piège : oublier "
                "l'énergie. Dès qu'un passage se fait contre le gradient, "
                "il faut nécessairement invoquer un transport actif et une "
                "dépense d'ATP. Une phrase comme « le glucose diffuse "
                "contre son gradient » est une contradiction : un passage "
                "contre le gradient n'est jamais une diffusion."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
