"""
scenes/Chimie_DosagesOxydoreduction_07.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 07.

§ Relation générale à l'équivalence. Formulation stœchiométrique (a Ox1 +
b Red2 → produits, n(Ox1)/a = n(Red2)/b) avec démonstration courte.
Formulation électronique (νox×Cox×Voxeq = νred×Cred×Vred), vérification sur
la manganimétrie du fer. Tableau récapitulatif des dosages usuels
(manganimétrie Fe²⁺, manganimétrie H₂O₂, iodométrie directe, dichromate/fer
II).
Source : 1ereC/Chimie.pdf, chapitre 12, pages 119-120.
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
from shapes.boxes import scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _ligne_tableau(nom, equation_tex, nu_ox, nu_red):
    label = Text(nom, font_size=16, color=YELLOW, weight="BOLD")
    eq = MathTex(equation_tex, font_size=18, color=WHITE)
    nus = MathTex(rf"\nu_{{ox}}={nu_ox}\ ;\ \nu_{{red}}={nu_red}", font_size=18, color=WHITE)
    ligne = VGroup(label, eq, nus).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    return ligne


def _tableau_recap():
    lignes = VGroup(
        _ligne_tableau(
            "Manganimétrie du fer",
            r"MnO_4^- + 5Fe^{2+} + 8H^+ \rightarrow Mn^{2+} + 5Fe^{3+} + 4H_2O",
            5, 1,
        ),
        _ligne_tableau(
            "Manganimétrie de H₂O₂",
            r"2MnO_4^- + 5H_2O_2 + 6H^+ \rightarrow 2Mn^{2+} + 5O_2 + 8H_2O",
            5, 2,
        ),
        _ligne_tableau(
            "Iodométrie directe",
            r"I_2 + 2S_2O_3^{2-} \rightarrow 2I^- + S_4O_6^{2-}",
            2, 1,
        ),
        _ligne_tableau(
            "Dichromate / fer II",
            r"Cr_2O_7^{2-} + 6Fe^{2+} + 14H^+ \rightarrow 2Cr^{3+} + 6Fe^{3+} + 7H_2O",
            6, 1,
        ),
    ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    return lignes


class RelationGeneraleEquivalence(NotionScene):
    def construct(self):
        titre = scene_title("12.7 La relation générale à l'équivalence")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------------------
        intro = Text(
            _wrap(
                "Nous avons établi une relation différente pour chaque "
                "dosage étudié. Existe-t-il une formule GÉNÉRALE, valable "
                "pour n'importe quel dosage redox ?",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Jusqu'ici, nous avons établi une relation différente "
                "pour chaque dosage étudié : manganimétrie, iodométrie "
                "directe ou indirecte. Existe-t-il une formule générale, "
                "valable pour n'importe quel dosage d'oxydoréduction ? "
                "Oui, et nous allons l'établir maintenant."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : formulation stœchiométrique -----------------------------------
        theo_stoechio = theorem_box(
            VGroup(
                MathTex(r"a\,Ox_1 + b\,Red_2 \longrightarrow \text{produits}", font_size=26, color="#1A1A1A"),
                Text("À l'équivalence, mélange stœchiométrique :", font_size=19, color="#1A1A1A"),
                MathTex(r"\dfrac{n(Ox_1)}{a} = \dfrac{n(Red_2)}{b}", font_size=28, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.28),
            box_width=11.5,
        )
        theo_stoechio.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Formulation stœchiométrique : pour une réaction générale "
                "a Ox-1, plus b Red-2, donnant des produits, l'équivalence "
                "correspond exactement au mélange stœchiométrique : les "
                "réactifs sont introduits, et donc consommés, dans les "
                "proportions de l'équation. On peut alors écrire : n de "
                "Ox-1, divisé par a, égale n de Red-2, divisé par b. "
                "C'est la démonstration la plus directe : diviser chaque "
                "quantité de matière par son coefficient stœchiométrique "
                "donne toujours la même valeur à l'équivalence, "
                "l'avancement de la réaction."
            )
        ) as tracker:
            self.play(FadeIn(theo_stoechio))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_stoechio))

        # --- Raisonnement : formulation électronique --------------------------------------
        theo_electrons = theorem_box(
            VGroup(
                Text(
                    "Formulation électronique (électrons cédés = électrons captés) :",
                    font_size=19, color="#1A1A1A",
                ),
                MathTex(
                    r"\nu_{ox}\times C_{ox}\times V_{ox\,eq} = \nu_{red}\times C_{red}\times V_{red}",
                    font_size=28, color="#1A1A1A",
                ),
                Text(
                    "(νox, νred = nombre d'électrons échangés par chaque demi-équation)",
                    font_size=16, color="#1A1A1A",
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=12.0,
        )
        theo_electrons.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Formulation électronique, équivalente : puisqu'à "
                "l'équivalence les électrons cédés par le réducteur sont "
                "captés par l'oxydant, on peut aussi écrire : nu-ox fois "
                "Cox fois Voxeq égale nu-red fois Cred fois Vred, où "
                "nu-ox et nu-red représentent le nombre d'électrons "
                "échangés dans chaque demi-équation de l'oxydant et du "
                "réducteur."
            )
        ) as tracker:
            self.play(FadeIn(theo_electrons))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_electrons))

        # --- Exemple traité : vérification sur la manganimétrie du fer -------------------
        entete_verif = Text("Vérification sur la manganimétrie du fer", font_size=21, color=YELLOW, weight="BOLD")
        entete_verif.next_to(titre, DOWN, buff=0.4)

        verif = VGroup(
            Text("MnO₄⁻ capte 5 électrons (νox=5) ; Fe²⁺ en cède 1 (νred=1).", font_size=19, color=WHITE),
            MathTex(r"5\times C_{ox}\times V_{ox\,eq} = 1\times C_{red}\times V_{red}", font_size=24, color=WHITE),
            MathTex(r"\Longrightarrow\ C_{red} = \dfrac{5\,C_{ox}\,V_{ox\,eq}}{V_{red}}\quad\text{(formule déjà établie)}", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.3)
        verif.next_to(entete_verif, DOWN, buff=0.3)
        groupe_verif = VGroup(entete_verif, verif)
        _fit(groupe_verif, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Vérifions cette formule générale sur la manganimétrie du "
                "fer, déjà traitée. L'ion permanganate capte cinq "
                "électrons, donc nu-ox égale cinq ; l'ion fer deux plus "
                "en cède un seul, donc nu-red égale un. La formule "
                "générale donne alors : cinq fois Cox fois Voxeq égale un "
                "fois Cred fois Vred, soit Cred égale cinq Cox Voxeq sur "
                "Vred. On retrouve exactement la relation établie "
                "précédemment : les deux formulations, stœchiométrique et "
                "électronique, sont parfaitement cohérentes."
            )
        ) as tracker:
            self.play(FadeIn(entete_verif))
            self.play(FadeIn(verif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_verif))

        # --- À retenir : tableau récapitulatif des dosages usuels -------------------------
        entete_tab = Text("Tableau récapitulatif des dosages usuels", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_recap()
        tableau.scale(0.85)
        tableau.next_to(entete_tab, DOWN, buff=0.3)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Récapitulons les dosages usuels avec leurs coefficients "
                "électroniques. Pour la manganimétrie du fer : nu-ox égale "
                "cinq, nu-red égale un. Pour la manganimétrie de l'eau "
                "oxygénée : nu-ox égale cinq, nu-red égale deux. Pour "
                "l'iodométrie directe : nu-ox égale deux, nu-red égale "
                "un. Et pour le dosage par le dichromate du fer deux "
                "plus : nu-ox égale six, nu-red égale un. Ce tableau sera "
                "notre référence pour tous les exercices de ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Piège à éviter -----------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "νox et νred ne sont PAS les coefficients a et b de "
                    "l'équation-bilan : ce sont les nombres d'électrons "
                    "échangés dans CHAQUE demi-équation. Pour la "
                    "manganimétrie de H₂O₂ par exemple, a=5 et b=... mais "
                    "νox=5 et νred=2 (H₂O₂ cède 2 électrons).",
                    width=48,
                ),
                font_size=18,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège de vocabulaire : nu-ox et nu-red ne "
                "sont pas les coefficients de l'équation-bilan globale, "
                "ce sont les nombres d'électrons échangés dans chacune "
                "des deux demi-équations séparées. Par exemple, pour "
                "l'eau oxygénée face au permanganate, que nous détaillons "
                "dans la scène suivante, l'eau oxygénée cède deux "
                "électrons dans sa demi-équation : nu-red vaut donc deux, "
                "et non le coefficient de l'équation-bilan globale."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
