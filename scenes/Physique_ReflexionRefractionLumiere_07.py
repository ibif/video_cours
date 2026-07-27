"""
scenes/Physique_ReflexionRefractionLumiere_07.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 07.

§ Applications de la réflexion totale : la fibre optique. Constitution
(cœur d'indice n1, gaine d'indice n2 < n1 légèrement inférieur), principe
(réflexions totales successives, lumière guidée même si la fibre est
courbée), applications (télécommunications à Abidjan, endoscopie médicale,
éclairage décoratif).
Source : 1ereC/Physique.pdf, pages 117-129.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREY,
    ORANGE,
    Create,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ApplicationsFibreOptique(NotionScene):
    def construct(self):
        titre = scene_title("Applications de la réflexion totale : la fibre optique")
        titre.scale(0.38)
        titre.to_edge(UP)

        # --- Énoncé : comment guider la lumière sur de longues distances ? -----------
        mise_en_situation = Text(
            _wrap(
                "Peut-on transporter de la lumière — et donc de "
                "l'information — sur des kilomètres, en la faisant suivre "
                "un fil fin, même courbé, sans qu'elle ne s'échappe sur "
                "les côtés ?",
                width=48,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Peut-on transporter de la lumière, et donc de "
                "l'information, sur des kilomètres, en la faisant suivre "
                "un fil fin, même courbé, sans qu'elle ne s'échappe sur "
                "les côtés ? La réponse est oui, grâce à la réflexion "
                "totale : c'est le principe de la fibre optique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : constitution de la fibre ----------------------------------
        gaine = RoundedRectangle(width=7.0, height=1.4, corner_radius=0.3, fill_color=BLUE, fill_opacity=0.12, stroke_color=BLUE, stroke_width=2)
        coeur = Rectangle(width=6.6, height=0.6, fill_color=YELLOW, fill_opacity=0.15, stroke_color=YELLOW, stroke_width=2)
        fibre = VGroup(gaine, coeur)
        fibre.move_to(DOWN * 0.6)

        label_gaine = Text("gaine (n2, légèrement < n1)", font_size=16, color=BLUE).next_to(gaine, UP, buff=0.15)
        label_coeur = Text("cœur (n1, le plus réfringent)", font_size=16, color=YELLOW).move_to(coeur.get_center() + DOWN * 0.0)

        with self.voiceover(
            text=(
                "Une fibre optique est constituée de deux parties "
                "cylindriques concentriques en verre très pur. Le cœur, "
                "au centre, a un indice de réfraction n1 élevé. Il est "
                "entouré d'une gaine optique, d'indice n2 légèrement "
                "inférieur à n1. C'est cette petite différence d'indice, "
                "avec n1 supérieur à n2, qui va permettre la réflexion "
                "totale à l'intérieur du cœur."
            )
        ) as tracker:
            self.play(Create(gaine))
            self.play(Create(coeur), Write(label_gaine))
            self.play(Write(label_coeur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(fibre), FadeOut(label_gaine), FadeOut(label_coeur))

        # --- Trajet du rayon par réflexions totales successives -----------------------
        gaine2 = RoundedRectangle(width=8.4, height=1.4, corner_radius=0.3, fill_color=BLUE, fill_opacity=0.12, stroke_color=BLUE, stroke_width=2)
        coeur2 = Rectangle(width=8.0, height=0.6, fill_color=YELLOW, fill_opacity=0.12, stroke_color=YELLOW, stroke_width=1)
        fibre2 = VGroup(gaine2, coeur2)
        fibre2.move_to(DOWN * 0.5)

        # Zigzag du rayon lumineux entre les deux parois du cœur (réflexions totales successives)
        y_top = 0.3 - 0.5
        y_bot = -0.3 - 0.5
        xs = np.linspace(-3.9, 3.9, 7)
        points = []
        for k, x in enumerate(xs):
            y = y_top if k % 2 == 0 else y_bot
            points.append(np.array([x, y, 0]))
        segments = VGroup(*[Line(points[k], points[k + 1], color=ORANGE, stroke_width=3) for k in range(len(points) - 1)])

        with self.voiceover(
            text=(
                "À l'intérieur du cœur, un rayon lumineux qui frappe la "
                "paroi cœur-gaine avec un angle d'incidence supérieur à "
                "l'angle limite subit une réflexion totale : il repart "
                "intégralement vers l'autre paroi, où il subit une "
                "nouvelle réflexion totale, et ainsi de suite. La lumière "
                "progresse ainsi en zigzag le long de la fibre, guidée "
                "par une succession de réflexions totales, sans jamais "
                "s'échapper à travers la gaine — même lorsque la fibre "
                "est légèrement courbée."
            )
        ) as tracker:
            self.play(Create(fibre2))
            self.play(Create(segments), run_time=2.5)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(fibre2), FadeOut(segments))

        # --- Propriété : condition de guidage -----------------------------------------
        condition = property_box(
            VGroup(
                Text("Condition de guidage dans une fibre optique", font_size=21, weight="BOLD"),
                MathTex(r"n_{\text{coeur}} > n_{\text{gaine}} \quad \text{et} \quad i_1 > \lambda \ \text{à chaque réflexion}", font_size=24),
                Text("La lumière reste confinée au cœur sur toute la longueur", font_size=19),
                Text("de la fibre, même sur plusieurs kilomètres.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        condition.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On retrouve exactement les deux conditions de la "
                "réflexion totale vues précédemment : l'indice du cœur "
                "doit être supérieur à celui de la gaine, et l'angle "
                "d'incidence doit rester supérieur à l'angle limite à "
                "chaque réflexion. Tant que ces deux conditions sont "
                "respectées, la lumière reste confinée au cœur sur toute "
                "la longueur de la fibre, même sur plusieurs kilomètres."
            )
        ) as tracker:
            self.play(FadeIn(condition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(condition))

        # --- Applications --------------------------------------------------------------
        applications = definition_box(
            VGroup(
                Text("Applications de la fibre optique", font_size=22, weight="BOLD"),
                Text("• Télécommunications : internet et téléphonie très haut", font_size=20),
                Text("   débit (ex : réseau de fibre optique à Abidjan).", font_size=20),
                Text("• Endoscopie médicale : observer l'intérieur du corps", font_size=20),
                Text("   sans chirurgie lourde.", font_size=20),
                Text("• Éclairage décoratif (guirlandes, signalétique).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        applications.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Les applications sont nombreuses. En télécommunications, "
                "les fibres optiques transportent internet et la "
                "téléphonie à très haut débit, comme le réseau de fibre "
                "optique déployé à Abidjan. En médecine, l'endoscopie "
                "utilise des fibres optiques souples pour observer "
                "l'intérieur du corps sans chirurgie lourde. Et en "
                "décoration, on retrouve des fibres optiques dans des "
                "guirlandes lumineuses ou de la signalétique."
            )
        ) as tracker:
            self.play(FadeIn(applications))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(applications))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Fibre optique = cœur (n1) + gaine (n2 < n1).", font_size=20),
                Text("Lumière guidée par réflexions totales successives.", font_size=20),
                Text("Applications : télécoms, endoscopie, éclairage.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : une fibre optique est constituée "
                "d'un cœur d'indice n1 entouré d'une gaine d'indice n2 "
                "inférieur. La lumière y est guidée par une succession de "
                "réflexions totales. Ses applications couvrent les "
                "télécommunications, l'endoscopie médicale et "
                "l'éclairage décoratif."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Le cœur doit être PLUS réfringent que la gaine, jamais", font_size=20),
                Text("   l'inverse : sans cette condition, aucun guidage possible.", font_size=20),
                Text("• Une fibre trop courbée peut faire chuter l'angle", font_size=20),
                Text("   d'incidence sous l'angle limite : la lumière fuit alors", font_size=20),
                Text("   hors du cœur (perte de signal).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Piège à éviter : le cœur doit toujours être plus "
                "réfringent que la gaine, jamais l'inverse, sinon aucun "
                "guidage n'est possible. Attention aussi : une fibre "
                "trop courbée peut faire chuter l'angle d'incidence "
                "sous l'angle limite à certains endroits, ce qui fait "
                "fuir la lumière hors du cœur et provoque une perte de "
                "signal."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
