"""
scenes/Chimie_OxydoreductionVoieSeche_01.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 01.

§ 1 (début). Rappel de l'oxydoréduction en solution aqueuse (oxydation =
perte d'électrons, réduction = gain d'électrons). Expérience 1 : combustion
du magnésium dans le dioxygène (lumière blanche éblouissante, fumées,
cendre blanche de MgO), demi-équations Mg → Mg²⁺ + 2e⁻ et
O₂ + 4e⁻ → 2 O²⁻, bilan 2Mg + O₂ → 2MgO. Expérience 2 : combustion du
magnésium dans le dichlore (MgCl₂), demi-équations et bilan. Conclusion
capitale : l'oxydation ne suppose pas la présence de dioxygène.
Source : 1ereC/Chimie.pdf, chapitre 13, pages 124-125.
"""

import textwrap

from manim import (
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import theorem_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _schema_combustion(flamme_color, stade="avant"):
    """Schéma d'une combustion de ruban de magnésium tenu par une pince,
    construit uniquement avec des primitives Manim de base (Line, Polygon,
    Rectangle, Circle, VGroup) — aucune bibliothèque externe.

    stade="avant" : ruban de magnésium intact, pas de flamme.
    stade="apres" : ruban en cours de combustion (flamme + fumées) ou
    disparu, remplacé par un dépôt de cendre solide.
    """
    pince_gauche = Line([-0.35, 1.6, 0], [-0.1, 1.3, 0], color=WHITE, stroke_width=4)
    pince_droite = Line([0.35, 1.6, 0], [0.1, 1.3, 0], color=WHITE, stroke_width=4)
    manche = Line([0, 2.3, 0], [0, 1.6, 0], color=WHITE, stroke_width=4)
    pince = VGroup(manche, pince_gauche, pince_droite)

    groupe = VGroup(pince)

    if stade == "avant":
        ruban = Rectangle(width=0.16, height=1.6, fill_color=GRAY, fill_opacity=1, stroke_width=0)
        ruban.move_to([0, 0.5, 0])
        groupe.add(ruban)
    else:
        ruban_restant = Rectangle(width=0.16, height=0.5, fill_color=GRAY, fill_opacity=1, stroke_width=0)
        ruban_restant.move_to([0, 1.05, 0])
        groupe.add(ruban_restant)

        flamme = Polygon(
            [0, 0.85, 0], [0.28, 0.4, 0], [0.1, 0.15, 0], [0, -0.05, 0],
            [-0.1, 0.15, 0], [-0.28, 0.4, 0],
            fill_color=flamme_color, fill_opacity=0.9, stroke_width=0,
        )
        groupe.add(flamme)

        fumees = VGroup(*[
            Circle(radius=0.06 + 0.015 * i, fill_color=WHITE, fill_opacity=0.5 - 0.06 * i, stroke_width=0)
            .move_to([0.15 * (-1) ** i, 1.0 + 0.22 * i, 0])
            for i in range(4)
        ])
        groupe.add(fumees)

        cendre = Circle(radius=0.22, fill_color=WHITE, fill_opacity=0.9, stroke_width=1, stroke_color=GRAY)
        cendre.stretch(0.35, dim=1)
        cendre.move_to([0, -0.35, 0])
        groupe.add(cendre)

    return groupe


class RappelsEtExperiencesDecouverte(NotionScene):
    def construct(self):
        titre = scene_title("13.1 Rappels et expériences de découverte")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : rappel de l'oxydoréduction en solution --------------
        rappel = _bullets(
            [
                "Oxydation : PERTE d'un ou plusieurs électrons par une "
                "espèce chimique (c'est le réducteur qui s'oxyde).",
                "Réduction : GAIN d'un ou plusieurs électrons par une "
                "espèce chimique (c'est l'oxydant qui se réduit).",
                "Jusqu'ici, ces échanges d'électrons ont toujours eu lieu "
                "EN SOLUTION AQUEUSE. Est-ce toujours le cas ?",
            ],
            width=52,
        )
        rappel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappelons les définitions vues en solution aqueuse. Une "
                "oxydation est une perte d'un ou plusieurs électrons par "
                "une espèce chimique : c'est le réducteur qui s'oxyde. Une "
                "réduction est un gain d'un ou plusieurs électrons : c'est "
                "l'oxydant qui se réduit. Mais jusqu'ici, ces échanges "
                "d'électrons ont toujours eu lieu en solution aqueuse. "
                "Est-ce toujours le cas ? Deux expériences vont nous "
                "montrer que non."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel))

        # --- Raisonnement : expérience 1, Mg dans O2 -----------------------
        entete1 = Text("Expérience 1 : combustion du magnésium dans O₂", font_size=22, color=YELLOW, weight="BOLD")
        entete1.next_to(titre, DOWN, buff=0.35)

        schema_avant = _schema_combustion(WHITE, "avant")
        schema_apres = _schema_combustion(WHITE, "apres")
        schema_avant.next_to(entete1, DOWN, buff=0.4).shift(LEFT * 3.2)
        schema_apres.move_to(schema_avant)

        obs1 = _bullets(
            [
                "Lumière blanche éblouissante, dégagement de fumées ;",
                "il reste une cendre blanche : l'oxyde de magnésium MgO.",
            ],
            width=34,
        )
        obs1.next_to(schema_avant, RIGHT, buff=0.9)

        with self.voiceover(
            text=(
                "Première expérience : on approche un ruban de magnésium "
                "enflammé d'un flacon rempli de dioxygène pur. La "
                "combustion est spectaculaire : une lumière blanche "
                "éblouissante, accompagnée de fumées. Il ne reste, au fond "
                "du flacon, qu'une cendre blanche : l'oxyde de magnésium, "
                "MgO."
            )
        ) as tracker:
            self.play(FadeIn(entete1))
            self.play(FadeIn(schema_avant))
            self.wait(0.3)
            self.play(FadeIn(obs1))
            self.play(FadeIn(schema_apres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete1), FadeOut(schema_avant), FadeOut(schema_apres), FadeOut(obs1))

        demi_mg = MathTex(r"Mg \longrightarrow Mg^{2+} + 2\,e^-", font_size=30, color=WHITE)
        demi_o2 = MathTex(r"O_2 + 4\,e^- \longrightarrow 2\,O^{2-}", font_size=30, color=WHITE)
        bilan1 = MathTex(r"2\,Mg + O_2 \longrightarrow 2\,MgO", font_size=32, color=ORANGE)
        eqs1 = VGroup(demi_mg, demi_o2, bilan1).arrange(DOWN, buff=0.4)
        eqs1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Interprétons : le magnésium cède deux électrons pour "
                "former l'ion magnésium deux plus, Mg donne Mg deux plus "
                "plus deux électrons. Le dioxygène capte ces électrons "
                "pour former des ions oxyde, O deux, plus quatre "
                "électrons, donne deux O deux moins. En combinant ces deux "
                "demi-équations, on obtient le bilan : deux Mg plus O deux "
                "donne deux MgO."
            )
        ) as tracker:
            self.play(Write(demi_mg))
            self.play(Write(demi_o2))
            self.play(Write(bilan1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(eqs1))

        # --- Exemple traité : expérience 2, Mg dans Cl2 ---------------------
        entete2 = Text("Expérience 2 : combustion du magnésium dans Cl₂", font_size=22, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        schema2_apres = _schema_combustion(GREEN, "apres")
        schema2_apres.next_to(entete2, DOWN, buff=0.4).shift(LEFT * 3.2)

        obs2 = _bullets(
            [
                "Combustion vive, sans besoin d'oxygène cette fois ;",
                "il se forme un solide blanc : le chlorure de "
                "magnésium MgCl₂.",
            ],
            width=34,
        )
        obs2.next_to(schema2_apres, RIGHT, buff=0.9)

        with self.voiceover(
            text=(
                "Deuxième expérience : on recommence, mais cette fois dans "
                "un flacon rempli de dichlore, un gaz verdâtre, et sans "
                "aucune trace de dioxygène. Le ruban de magnésium brûle "
                "pourtant tout aussi vivement, et il se forme un solide "
                "blanc : le chlorure de magnésium, MgCl deux."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(schema2_apres))
            self.play(FadeIn(obs2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete2), FadeOut(schema2_apres), FadeOut(obs2))

        demi_mg2 = MathTex(r"Mg \longrightarrow Mg^{2+} + 2\,e^-", font_size=30, color=WHITE)
        demi_cl2 = MathTex(r"Cl_2 + 2\,e^- \longrightarrow 2\,Cl^-", font_size=30, color=WHITE)
        bilan2 = MathTex(r"Mg + Cl_2 \longrightarrow MgCl_2", font_size=32, color=ORANGE)
        eqs2 = VGroup(demi_mg2, demi_cl2, bilan2).arrange(DOWN, buff=0.4)
        eqs2.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le magnésium cède encore deux électrons, Mg donne Mg deux "
                "plus, plus deux électrons. Le dichlore, lui, capte ces "
                "deux électrons pour former deux ions chlorure : Cl deux, "
                "plus deux électrons, donne deux Cl moins. Le bilan "
                "s'écrit : Mg plus Cl deux donne MgCl deux."
            )
        ) as tracker:
            self.play(Write(demi_mg2))
            self.play(Write(demi_cl2))
            self.play(Write(bilan2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(eqs2))

        # --- À retenir : conclusion capitale ---------------------------------
        conclusion = theorem_box(
            VGroup(
                Text(
                    "Dans les deux expériences, le magnésium CÈDE des",
                    font_size=23, weight="BOLD",
                ),
                Text("électrons : il y a bien OXYDATION du magnésium,", font_size=23, weight="BOLD"),
                Text(
                    "que le comburant soit O₂ ou Cl₂ — sans aucun rapport",
                    font_size=22,
                ),
                Text("nécessaire avec l'oxygène.", font_size=22),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.4,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Conclusion capitale : dans les deux expériences, le "
                "magnésium cède des électrons, il y a bien oxydation du "
                "magnésium — que le comburant soit le dioxygène ou le "
                "dichlore. Le mot « oxydation » vient historiquement de "
                "l'oxygène, mais le phénomène chimique, lui, ne suppose "
                "absolument pas la présence d'oxygène."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège fréquent : ne pas croire que « oxydation » "
                    "signifie forcément « réaction avec du dioxygène ». Le "
                    "vrai critère est le TRANSFERT D'ÉLECTRONS, quelle que "
                    "soit la nature du réactif qui les capte.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : « oxydation » ne signifie "
                "pas forcément « réaction avec du dioxygène ». Le vrai "
                "critère est le transfert d'électrons, quelle que soit la "
                "nature du réactif qui les capte. C'est cette idée qui va "
                "nous permettre, dans la suite du chapitre, de généraliser "
                "l'oxydoréduction aux réactions par voie sèche."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
