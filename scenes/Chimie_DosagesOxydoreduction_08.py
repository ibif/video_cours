"""
scenes/Chimie_DosagesOxydoreduction_08.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 08.

§ Applications : titre de l'eau oxygénée et degré chlorométrique. Eau
oxygénée ampholyte redox (H2O2/H2O oxydant E°=1,77V, O2/H2O2 réducteur
E°=0,68V), demi-équation H2O2→O2+2H++2e- face au permanganate,
équation-bilan 2MnO4-+5H2O2+6H+→2Mn2++5O2+8H2O. Définition titre en volumes
T=11,2×C. Définition degré chlorométrique de l'eau de Javel = 22,4×C(ClO⁻),
équation ClO⁻+Cl⁻+2H⁺→Cl2+H2O. Exemple résolu 3 : eau de Javel diluée,
degré chlorométrique ≈13,4°chl.
Source : 1ereC/Chimie.pdf, chapitre 12, pages 120-121.
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
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class TitreEauOxygeneeEtDegreChlorometrique(NotionScene):
    def construct(self):
        titre = scene_title("12.8 Titre de l'eau oxygénée et degré chlorométrique")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------------------
        intro = Text(
            _wrap(
                "Deux applications industrielles très courantes des "
                "dosages redox : déterminer le titre de l'eau oxygénée, "
                "et le degré chlorométrique de l'eau de Javel.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici deux applications industrielles très courantes des "
                "dosages d'oxydoréduction : déterminer le titre en "
                "volumes de l'eau oxygénée, vendue en pharmacie, et le "
                "degré chlorométrique de l'eau de Javel, vendue au "
                "supermarché."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : l'eau oxygénée, ampholyte redox --------------------------------
        entete_h2o2 = Text("L'eau oxygénée : un ampholyte redox", font_size=21, color=YELLOW, weight="BOLD")
        entete_h2o2.next_to(titre, DOWN, buff=0.35)

        couple1 = MathTex(r"H_2O_2/H_2O \quad (E^\circ = 1{,}77\ V)\ \text{— rôle OXYDANT}", font_size=22, color=WHITE)
        couple2 = MathTex(r"O_2/H_2O_2 \quad (E^\circ = 0{,}68\ V)\ \text{— rôle RÉDUCTEUR}", font_size=22, color=WHITE)
        note = Text(
            "H₂O₂ appartient à deux couples : c'est un AMPHOLYTE REDOX.",
            font_size=19, color=YELLOW, weight="BOLD",
        )
        bloc_h2o2 = VGroup(couple1, couple2, note).arrange(DOWN, buff=0.3)
        bloc_h2o2.next_to(entete_h2o2, DOWN, buff=0.3)
        groupe_h2o2 = VGroup(entete_h2o2, bloc_h2o2)
        _fit(groupe_h2o2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "L'eau oxygénée a une particularité importante : elle "
                "appartient à deux couples oxydant-réducteur différents. "
                "Dans le couple H-2-O-2 sur H-2-O, de potentiel un "
                "virgule soixante-dix-sept volt, elle joue le rôle "
                "d'oxydant. Mais dans le couple O-2 sur H-2-O-2, de "
                "potentiel zéro virgule soixante-huit volt, elle joue le "
                "rôle de réducteur. On dit que l'eau oxygénée est un "
                "ampholyte redox."
            )
        ) as tracker:
            self.play(FadeIn(entete_h2o2))
            self.play(Write(couple1))
            self.play(Write(couple2))
            self.play(FadeIn(note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_h2o2))

        # --- Face au permanganate : demi-équation + équation-bilan -------------------------
        entete_mangani_h2o2 = Text("Dosage de H₂O₂ par le permanganate", font_size=20, color=YELLOW, weight="BOLD")
        entete_mangani_h2o2.next_to(titre, DOWN, buff=0.35)

        texte_role = Text(
            "Face au permanganate, plus oxydant, H₂O₂ joue le rôle de RÉDUCTEUR :",
            font_size=18, color=WHITE,
        )
        demi = MathTex(r"H_2O_2 \longrightarrow O_2 + 2H^+ + 2e^-", font_size=24, color=WHITE)
        bilan = MathTex(
            r"2\,MnO_4^- + 5\,H_2O_2 + 6\,H^+ \longrightarrow 2\,Mn^{2+} + 5\,O_2 + 8\,H_2O",
            font_size=24, color=YELLOW,
        )
        bloc_mangani = VGroup(texte_role, demi, bilan).arrange(DOWN, buff=0.3)
        bloc_mangani.next_to(entete_mangani_h2o2, DOWN, buff=0.3)
        groupe_mangani = VGroup(entete_mangani_h2o2, bloc_mangani)
        _fit(groupe_mangani, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Pour doser l'eau oxygénée, on utilise justement le "
                "permanganate de potassium, plus oxydant qu'elle : dans "
                "ce dosage, l'eau oxygénée joue donc le rôle de "
                "réducteur, avec la demi-équation : H-2-O-2 donne O-2, "
                "plus deux H plus, plus deux électrons. En combinant "
                "avec la demi-équation du permanganate, déjà vue, on "
                "obtient l'équation-bilan : deux M-n-O-4 moins, plus cinq "
                "H-2-O-2, plus six H plus, donne deux M-n deux plus, plus "
                "cinq O-2, plus huit H-2-O."
            )
        ) as tracker:
            self.play(FadeIn(entete_mangani_h2o2))
            self.play(FadeIn(texte_role))
            self.play(Write(demi))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_mangani))

        # --- Définition : titre en volumes ---------------------------------------------------
        def_titre = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Le titre en volumes T de l'eau oxygénée est le "
                        "volume de dioxygène (en L, mesuré dans les "
                        "conditions normales) libéré par la décomposition "
                        "complète d'1 L de la solution :",
                        width=48,
                    ),
                    font_size=19,
                ),
                MathTex(r"2\,H_2O_2 \rightarrow 2\,H_2O + O_2 \quad\Longrightarrow\quad T = 11{,}2\times C", font_size=24, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.28),
            box_width=12.0,
        )
        def_titre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Introduisons maintenant le titre en volumes de l'eau "
                "oxygénée, noté T. C'est le volume de dioxygène, exprimé "
                "en litres et mesuré dans les conditions normales, "
                "libéré par la décomposition complète d'un litre de la "
                "solution, selon l'équation deux H-2-O-2 donne deux "
                "H-2-O, plus O-2. On montre que ce titre vaut T égale "
                "onze virgule deux fois C, où C est la concentration en "
                "eau oxygénée en mol par litre."
            )
        ) as tracker:
            self.play(FadeIn(def_titre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_titre))

        # --- Définition : degré chlorométrique -----------------------------------------------
        def_degre = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Le degré chlorométrique de l'eau de Javel se "
                        "définit de façon analogue, à partir de sa "
                        "réaction de décomposition :",
                        width=48,
                    ),
                    font_size=19,
                ),
                MathTex(r"ClO^- + Cl^- + 2H^+ \rightarrow Cl_2 + H_2O", font_size=23, color="#1A1A1A"),
                MathTex(r"\text{Degré chlorométrique} = 22{,}4\times C(ClO^-)", font_size=24, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.28),
            box_width=12.2,
        )
        def_degre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "De façon analogue, on définit le degré chlorométrique "
                "de l'eau de Javel, à partir de sa réaction de "
                "décomposition : C-l-O moins, plus C-l moins, plus deux H "
                "plus, donne C-l-2, plus H-2-O. Le degré chlorométrique "
                "vaut vingt-deux virgule quatre fois la concentration en "
                "ion hypochlorite, C-l-O moins."
            )
        ) as tracker:
            self.play(FadeIn(def_degre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_degre))

        # --- Exemple résolu 3 : eau de Javel diluée -------------------------------------------
        entete_ex = Text("Exemple résolu 3 — Eau de Javel diluée", font_size=20, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.35)

        enonce_ex = Text(
            _wrap(
                "1,0 mL d'eau de Javel diluée est traité par un excès "
                "d'iodure en milieu acide (iodométrie indirecte), puis le "
                "diiode formé est dosé par du thiosulfate à 0,100 mol/L, "
                "avec Veq = 12,0 mL. Calculer le degré chlorométrique.",
                width=50,
            ),
            font_size=16,
            color=WHITE,
        )

        calcul = example_box(
            VGroup(
                MathTex(r"n(S_2O_3^{2-}) = 0{,}100\times 12{,}0\times 10^{-3} = 1{,}20\times 10^{-3}\ \text{mol}", font_size=19, color="#1A1A1A"),
                MathTex(r"n(ClO^-) = n(I_2) = \dfrac{1{,}20\times 10^{-3}}{2} = 6{,}0\times 10^{-4}\ \text{mol}", font_size=19, color="#1A1A1A"),
                MathTex(r"C(ClO^-) = \dfrac{6{,}0\times 10^{-4}}{1{,}0\times 10^{-3}} = 0{,}60\ \text{mol/L}", font_size=19, color="#1A1A1A"),
                MathTex(r"\text{Degré} = 22{,}4\times 0{,}60 \approx 13{,}4\ °\text{chl}", font_size=21, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.22),
            box_width=11.8,
        )

        bloc_ex = VGroup(enonce_ex, calcul).arrange(DOWN, buff=0.3)
        bloc_ex.next_to(entete_ex, DOWN, buff=0.3)
        groupe_ex = VGroup(entete_ex, bloc_ex)
        _fit(groupe_ex, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Traitons un exemple résolu. Un millilitre d'eau de "
                "Javel diluée est traité par un excès d'iodure en milieu "
                "acide, iodométrie indirecte déjà vue, puis le diiode "
                "formé est dosé par du thiosulfate à zéro virgule cent "
                "mol par litre, l'équivalence étant obtenue pour douze "
                "millilitres. On calcule la quantité de thiosulfate : un "
                "virgule vingt fois dix puissance moins trois mole. On en "
                "déduit la quantité d'hypochlorite, égale à celle de "
                "diiode, soit six fois dix puissance moins quatre mole. "
                "En divisant par le volume prélevé, un millilitre, on "
                "obtient une concentration de zéro virgule soixante mol "
                "par litre. Le degré chlorométrique vaut alors vingt-deux "
                "virgule quatre fois zéro virgule soixante, soit environ "
                "treize virgule quatre degrés chlorométriques."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(enonce_ex))
            self.play(Write(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_ex))

        # --- Piège à éviter --------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : dans le dosage par le permanganate, H₂O₂ est "
                    "RÉDUCTEUR (pas oxydant !) — c'est parce que MnO₄⁻ "
                    "est un oxydant encore plus fort. Le rôle de H₂O₂ "
                    "dépend TOUJOURS de son partenaire de réaction.",
                    width=48,
                ),
                font_size=18,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent et important : dans le "
                "dosage par le permanganate, l'eau oxygénée joue le rôle "
                "de réducteur, et non d'oxydant, car le permanganate est "
                "un oxydant encore plus fort qu'elle. Le rôle de l'eau "
                "oxygénée, oxydant ou réducteur, dépend toujours de son "
                "partenaire de réaction : ce n'est jamais figé."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
