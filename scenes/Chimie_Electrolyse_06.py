"""
scenes/Chimie_Electrolyse_06.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 06.

§ 6. Électrolyse à électrodes inertes : solution de chlorure de sodium.
Expérience : dégagement de dichlore (odeur piquante) à l'anode,
dégagement de dihydrogène et apparition d'ions HO⁻ à la cathode (test à
la phénolphtaléine qui rosit). Demi-équations : anode 2Cl⁻ → Cl₂ + 2e⁻ ;
cathode 2H₂O + 2e⁻ → H₂ + 2OH⁻. Les ions Na⁺ ne sont pas réduits
(E°(Na⁺/Na) = -2,71 V, très négatif : c'est l'eau qui réagit à leur
place). Équation-bilan. Conclusion : cette électrolyse produit de la
soude (Na⁺ + OH⁻ en solution) — c'est le principe de l'électrolyse
chlore-soude. Exemple résolu 2 : piège d'un élève qui pense que du
sodium métallique se dépose à la cathode — correction.
Source : 1ereC/Chimie.pdf, chapitre 14, pages 139-140.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    LIGHT_GRAY,
    PINK,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, exercise_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
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


def _schema_nacl():
    """Cuve à électrolyse d'une solution de chlorure de sodium : gaz
    jaune-vert (Cl2) à l'anode, bulles (H2) + coloration rose
    (phénolphtaléine) à la cathode."""
    largeur, hauteur = 3.2, 1.8
    cuve = Rectangle(width=largeur, height=hauteur, color=LIGHT_GRAY, stroke_width=3)
    cuve.move_to([0, -0.9, 0])

    solution_incolore = Rectangle(width=(largeur - 0.1) / 2, height=hauteur - 0.2, fill_color=WHITE, fill_opacity=0.06, stroke_width=0)
    solution_incolore.move_to(cuve.get_center() + RIGHT * (largeur - 0.1) / 4)
    solution_rose = Rectangle(width=(largeur - 0.1) / 2, height=hauteur - 0.2, fill_color=PINK, fill_opacity=0.35, stroke_width=0)
    solution_rose.move_to(cuve.get_center() + LEFT * (largeur - 0.1) / 4)

    electrode_a = Line(cuve.get_center() + RIGHT * 1.0 + DOWN * 0.75, cuve.get_center() + RIGHT * 1.0 + UP * 0.9, color=RED, stroke_width=4)
    electrode_c = Line(cuve.get_center() + LEFT * 1.0 + DOWN * 0.75, cuve.get_center() + LEFT * 1.0 + UP * 0.9, color=BLUE, stroke_width=4)

    bulles_cl2 = VGroup(*[
        Circle(radius=0.06, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5, stroke_width=1)
        .move_to(electrode_a.get_center() + [0.15 + 0.05 * (i % 2), -0.3 + i * 0.28, 0])
        for i in range(4)
    ])
    label_a = Text("Cl₂ (odeur piquante)", font_size=13, color=YELLOW)
    label_a.next_to(electrode_a, UP, buff=0.15)

    bulles_h2 = VGroup(*[
        Circle(radius=0.06, color=WHITE, fill_color=WHITE, fill_opacity=0.5, stroke_width=1)
        .move_to(electrode_c.get_center() + [-0.15 - 0.05 * (i % 2), -0.3 + i * 0.28, 0])
        for i in range(4)
    ])
    label_c = Text("H₂ + HO⁻ (rose)", font_size=13, color=PINK)
    label_c.next_to(electrode_c, UP, buff=0.15)

    label_anode = Text("anode (+)", font_size=13, color=RED)
    label_anode.next_to(electrode_a, DOWN, buff=0.55)
    label_cathode = Text("cathode (−)", font_size=13, color=BLUE)
    label_cathode.next_to(electrode_c, DOWN, buff=0.55)

    return VGroup(
        cuve, solution_incolore, solution_rose,
        electrode_a, electrode_c, bulles_cl2, label_a, bulles_h2, label_c,
        label_anode, label_cathode,
    )


class ElectrolyseChlorureSodium(NotionScene):
    def construct(self):
        titre = scene_title("14.6 Électrolyse d'une solution de chlorure de sodium")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé : le montage ---------------------------------------------------
        intro = Text(
            _wrap(
                "Réalisons maintenant l'électrolyse, à électrodes inertes, "
                "d'une solution de chlorure de sodium (Na⁺ + Cl⁻), avec "
                "un indicateur coloré, la phénolphtaléine, dans la cuve.",
                width=58,
            ),
            font_size=21,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Réalisons maintenant l'électrolyse, à électrodes "
                "inertes, d'une solution de chlorure de sodium, qui "
                "contient des ions sodium et des ions chlorure. On ajoute "
                "un peu de phénolphtaléine, un indicateur coloré, dans la "
                "cuve."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : observations + schéma -----------------------------------
        entete_obs = Text("Observations expérimentales", font_size=21, color=YELLOW, weight="BOLD")
        entete_obs.next_to(titre, DOWN, buff=0.3)

        schema = _schema_nacl()
        schema.next_to(entete_obs, DOWN, buff=0.35).shift(LEFT * 2.5)

        observations = _bullets(
            [
                "à l'ANODE : dégagement d'un gaz jaune-vert à l'odeur "
                "piquante (dichlore, Cl₂) ;",
                "à la CATHODE : dégagement de dihydrogène ET la solution "
                "rosit (phénolphtaléine) : des ions HO⁻ apparaissent.",
            ],
            width=32,
        )
        observations.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Voici ce que l'on observe. À l'anode, un gaz jaune-vert "
                "à l'odeur piquante se dégage : c'est du dichlore. À la "
                "cathode, un gaz se dégage également, et surtout, la "
                "solution rosit progressivement au contact de la "
                "phénolphtaléine, preuve que des ions hydroxyde "
                "apparaissent en solution."
            )
        ) as tracker:
            self.play(FadeIn(entete_obs))
            self.play(FadeIn(schema))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_obs), FadeOut(schema), FadeOut(observations))

        # --- Exemple traité : demi-équations et bilan --------------------------------
        entete_eq = Text("Interprétation par demi-équations", font_size=21, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.3)

        anode_eq = VGroup(
            Text("Anode (oxydation des ions chlorure) :", font_size=17, color=RED, weight="BOLD"),
            MathTex(r"2\,Cl^- \longrightarrow Cl_2 + 2\,e^-", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        cathode_eq = VGroup(
            Text("Cathode (réduction de l'eau) :", font_size=17, color=BLUE, weight="BOLD"),
            MathTex(r"2\,H_2O + 2\,e^- \longrightarrow H_2 + 2\,OH^-", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        bilan = VGroup(
            Text("Équation-bilan (électrons déjà égaux) :", font_size=17, color=YELLOW, weight="BOLD"),
            MathTex(r"2\,Cl^- + 2\,H_2O \longrightarrow Cl_2 + H_2 + 2\,OH^-", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        groupe_eq = VGroup(anode_eq, cathode_eq, bilan).arrange(DOWN, buff=0.3)
        groupe_eq.next_to(entete_eq, DOWN, buff=0.3)
        _fit(groupe_eq, entete_eq.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "À l'anode, ce sont les ions chlorure, présents en "
                "solution, qui sont oxydés en priorité : deux ions "
                "chlorure donnent une molécule de dichlore et deux "
                "électrons. À la cathode, en revanche, ce n'est pas "
                "l'ion sodium qui est réduit, mais l'eau : deux molécules "
                "d'eau, plus deux électrons, donnent une molécule de "
                "dihydrogène et deux ions hydroxyde. Le nombre d'électrons "
                "est déjà égal des deux côtés, l'équation-bilan "
                "s'obtient directement par addition."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(anode_eq))
            self.play(Write(cathode_eq))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(groupe_eq))

        # --- À retenir : pourquoi pas Na+ / conclusion --------------------------------
        conclusion = _bullets(
            [
                "l'ion Na⁺ N'EST PAS réduit : son potentiel standard, "
                "E°(Na⁺/Na) = −2,71 V, est bien trop négatif — c'est "
                "l'eau qui est réduite à sa place ;",
                "cette électrolyse produit du dichlore, du dihydrogène, "
                "et une SOLUTION DE SOUDE (Na⁺ + HO⁻) : c'est le principe "
                "industriel de l'électrolyse chlore-soude.",
            ],
            font_size=18,
            width=56,
        )
        entete_concl = Text("Pourquoi pas Na⁺ ? Conclusion", font_size=20, color="#288073", weight="BOLD")
        entete_concl.next_to(titre, DOWN, buff=0.35)
        conclusion.next_to(entete_concl, DOWN, buff=0.3)
        _fit(VGroup(entete_concl, conclusion), entete_concl.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Pourquoi l'ion sodium n'est-il pas réduit à la cathode ? "
                "Parce que son potentiel standard, E rond de Na plus sur "
                "Na, vaut moins deux virgule soixante et onze volts : "
                "c'est un ion extrêmement difficile à réduire, bien plus "
                "difficile que l'eau. C'est donc l'eau qui est réduite à "
                "sa place. Au final, cette électrolyse produit du "
                "dichlore, du dihydrogène, et laisse en solution des ions "
                "sodium et hydroxyde, c'est-à-dire de la soude : c'est "
                "exactement le principe de l'électrolyse industrielle "
                "chlore-soude."
            )
        ) as tracker:
            self.play(FadeIn(entete_concl))
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_concl), FadeOut(conclusion))

        # --- Exemple résolu 2 : piège classique --------------------------------------
        exercice2 = exercise_box(
            Text(
                _wrap(
                    "Un élève affirme : « à la cathode, l'ion Na⁺ capte un "
                    "électron et du sodium métallique Na se dépose, comme "
                    "pour le cuivre dans le sulfate de cuivre ». "
                    "A-t-il raison ?",
                    width=46,
                ),
                font_size=20,
            ),
            box_width=11.0,
        )
        exercice2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici un exemple résolu, le piège classique de ce "
                "chapitre. Un élève affirme qu'à la cathode, l'ion sodium "
                "capte un électron et que du sodium métallique se dépose, "
                "par analogie avec le dépôt de cuivre observé dans une "
                "solution de sulfate de cuivre. A-t-il raison ?"
            )
        ) as tracker:
            self.play(FadeIn(exercice2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exercice2))

        corrige2 = corrige_box(
            Text(
                _wrap(
                    "Non : le sodium (E° très négatif, −2,71 V) est "
                    "beaucoup trop difficile à réduire face à l'eau, "
                    "toujours présente dans une solution aqueuse. C'est "
                    "l'eau qui est réduite à la cathode (dégagement de H₂ "
                    "+ ions HO⁻) — l'ion Na⁺ reste un simple ION "
                    "SPECTATEUR, il ne réagit pas et reste en solution.",
                    width=48,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )
        corrige2.next_to(titre, DOWN, buff=0.45)
        _fit(corrige2, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Non, il a tort. Le sodium, avec un potentiel standard "
                "très négatif de moins deux virgule soixante et onze "
                "volts, est beaucoup trop difficile à réduire face à "
                "l'eau, qui est toujours présente en solution aqueuse. "
                "C'est donc l'eau qui est réduite à la cathode, "
                "produisant du dihydrogène et des ions hydroxyde. L'ion "
                "sodium reste un simple ion spectateur : il ne réagit "
                "pas et demeure en solution, en compagnie des ions "
                "hydroxyde formés, ce qui constitue justement la soude."
            )
        ) as tracker:
            self.play(FadeIn(corrige2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige2), FadeOut(titre))
