"""
scenes/Chimie_DosagesOxydoreduction_03.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 03.

§ La manganimétrie : réactifs et réaction de dosage. Présentation du
permanganate de potassium (solide violet, solution violette), couples
MnO4-/Mn2+ (E°=1,51V) et Fe3+/Fe2+ (E°=0,77V), demi-équations et
équation-bilan MnO4- + 5Fe2+ + 8H+ → Mn2+ + 5Fe3+ + 4H2O. Définition de la
manganimétrie.
Source : 1ereC/Chimie.pdf, chapitre 12, pages 115-116.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
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
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ManganimetrieReactifsEtReaction(NotionScene):
    def construct(self):
        titre = scene_title("12.3 La manganimétrie : réactifs et réaction de dosage")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : présentation du permanganate de potassium -------------------
        intro = Text(
            _wrap(
                "Le permanganate de potassium, KMnO₄, est un solide "
                "violet très soluble, donnant des solutions violettes "
                "intenses. Grâce à son ion actif, MnO₄⁻, un oxydant "
                "puissant, il est très utilisé pour doser les réducteurs : "
                "c'est la manganimétrie.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le permanganate de potassium, de formule K-M-n-O-4, est "
                "un solide violet très soluble dans l'eau, donnant des "
                "solutions violettes intenses. Son ion actif, l'ion "
                "permanganate M-n-O-4 moins, est un oxydant puissant, ce "
                "qui en fait un réactif de choix pour doser de nombreux "
                "réducteurs. Cette famille de dosages porte un nom : la "
                "manganimétrie."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        def_mangani = definition_box(
            Text(
                _wrap(
                    "La manganimétrie est un dosage d'oxydoréduction dans "
                    "lequel l'ion permanganate MnO₄⁻ (en milieu acide) "
                    "joue le rôle d'OXYDANT TITRANT, versé depuis la "
                    "burette pour doser un réducteur.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        def_mangani.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La manganimétrie est un dosage d'oxydoréduction dans "
                "lequel l'ion permanganate, en milieu acide, joue le rôle "
                "d'oxydant titrant, versé depuis la burette pour doser un "
                "réducteur présent dans la solution titrée."
            )
        ) as tracker:
            self.play(FadeIn(def_mangani))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_mangani))

        # --- Raisonnement : les deux couples rédox --------------------------------
        entete_couples = Text("Les deux couples oxydant/réducteur en jeu", font_size=22, color=YELLOW, weight="BOLD")
        entete_couples.next_to(titre, DOWN, buff=0.35)

        couple1 = MathTex(r"MnO_4^-/Mn^{2+} \quad (E^\circ = 1{,}51\ V)", font_size=28, color=WHITE)
        couple2 = MathTex(r"Fe^{3+}/Fe^{2+} \quad (E^\circ = 0{,}77\ V)", font_size=28, color=WHITE)
        note = Text(
            _wrap(
                "Le potentiel standard de MnO₄⁻/Mn²⁺ étant nettement plus "
                "élevé, MnO₄⁻ oxyde spontanément et totalement Fe²⁺ en "
                "Fe³⁺.",
                width=50,
            ),
            font_size=20,
            color=WHITE,
        )
        couples = VGroup(couple1, couple2, note).arrange(DOWN, buff=0.35)
        couples.next_to(entete_couples, DOWN, buff=0.35)
        groupe_couples = VGroup(entete_couples, couples)
        _fit(groupe_couples, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Deux couples oxydant-réducteur sont en jeu dans le "
                "dosage du fer deux par le permanganate. D'une part, le "
                "couple M-n-O-4 moins sur M-n deux plus, de potentiel "
                "standard un virgule cinquante-et-un volt. D'autre part, "
                "le couple fer trois plus sur fer deux plus, de potentiel "
                "standard zéro virgule soixante-dix-sept volt. Le "
                "potentiel du couple du permanganate étant nettement plus "
                "élevé, l'ion permanganate oxyde spontanément et "
                "totalement l'ion fer deux plus en ion fer trois plus."
            )
        ) as tracker:
            self.play(FadeIn(entete_couples))
            self.play(Write(couple1))
            self.play(Write(couple2))
            self.play(FadeIn(note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_couples))

        # --- Exemple traité : demi-équations et équation-bilan --------------------
        entete_demi = Text("Demi-équations et équation-bilan", font_size=22, color=YELLOW, weight="BOLD")
        entete_demi.next_to(titre, DOWN, buff=0.35)

        demi1 = MathTex(
            r"MnO_4^- + 8H^+ + 5e^- \longrightarrow Mn^{2+} + 4H_2O",
            font_size=26, color=WHITE,
        )
        demi2 = MathTex(
            r"Fe^{2+} \longrightarrow Fe^{3+} + e^-",
            font_size=26, color=WHITE,
        )
        bilan = MathTex(
            r"MnO_4^- + 5Fe^{2+} + 8H^+ \longrightarrow Mn^{2+} + 5Fe^{3+} + 4H_2O",
            font_size=26, color=YELLOW,
        )
        demis = VGroup(demi1, demi2, bilan).arrange(DOWN, buff=0.4)
        demis.next_to(entete_demi, DOWN, buff=0.35)
        groupe_demi = VGroup(entete_demi, demis)
        _fit(groupe_demi, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Écrivons les deux demi-équations électroniques. Pour "
                "l'oxydant : M-n-O-4 moins, plus huit H plus, plus cinq "
                "électrons, donne M-n deux plus, plus quatre H-2-O. Pour "
                "le réducteur : fer deux plus donne fer trois plus, plus "
                "un électron. Pour additionner ces deux demi-équations "
                "sans faire apparaître les électrons, il faut multiplier "
                "la seconde par cinq, afin d'égaliser le nombre "
                "d'électrons échangés. On obtient l'équation-bilan de la "
                "manganimétrie du fer : M-n-O-4 moins, plus cinq fer deux "
                "plus, plus huit H plus, donne M-n deux plus, plus cinq "
                "fer trois plus, plus quatre H-2-O."
            )
        ) as tracker:
            self.play(FadeIn(entete_demi))
            self.play(Write(demi1))
            self.play(Write(demi2))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_demi))

        # --- À retenir ---------------------------------------------------------------
        retenir = definition_box(
            VGroup(
                Text("Manganimétrie : MnO₄⁻ = oxydant titrant (violet → incolore).", font_size=21, weight="BOLD"),
                MathTex(r"MnO_4^- + 5Fe^{2+} + 8H^+ \rightarrow Mn^{2+} + 5Fe^{3+} + 4H_2O", font_size=23, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de cette scène : la manganimétrie "
                "utilise l'ion permanganate comme oxydant titrant, violet "
                "et devenant incolore une fois réduit, avec pour "
                "équation-bilan, dans le cas du fer deux plus : M-n-O-4 "
                "moins, plus cinq fer deux plus, plus huit H plus, donne "
                "M-n deux plus, plus cinq fer trois plus, plus quatre "
                "H-2-O."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas oublier le milieu ACIDE (ions H⁺) : sans excès "
                    "d'acide, la demi-équation de MnO₄⁻ ne s'équilibre "
                    "pas et la réaction de dosage n'est plus la même "
                    "(risque de formation de MnO₂ solide au lieu de "
                    "Mn²⁺).",
                    width=48,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas oublier le milieu acide, apporté par "
                "les ions H plus : sans excès d'acide, la demi-équation "
                "de l'ion permanganate ne s'équilibre plus de la même "
                "façon, avec un risque de formation de dioxyde de "
                "manganèse solide, au lieu de l'ion manganèse deux plus "
                "attendu. Le milieu acide est donc une condition "
                "indispensable de la manganimétrie."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
