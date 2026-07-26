"""
scenes/Chimie_Electrolyse_11.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 11.

§ 11. Méthodes, pièges à éviter et essentiel. Deux méthodes pratiques :
(a) écrire l'équation-bilan d'une électrolyse en 5 étapes (identifier les
espèces en présence, appliquer la règle de priorité à chaque électrode,
écrire les deux demi-équations, égaliser le nombre d'électrons échangés,
additionner) ; (b) chaîne de calcul quantitatif I, t → Q → n(e⁻) →
n(produit) → m ou V. Méthode complémentaire pour identifier une anode
soluble. Trois pièges à éviter : anode/cathode inversés par rapport à la
pile ; ions « fantômes » (Na⁺, K⁺, Ca²⁺, Mg²⁺, Al³⁺, SO₄²⁻, NO₃⁻) qui ne
réagissent jamais en solution aqueuse ; unités et coefficients (convertir
en secondes, ne pas oublier le nombre d'électrons n). Essentiel à
retenir, en conclusion du chapitre.
Source : 1ereC/Chimie.pdf, chapitre 14, synthèse pages 134-143.
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
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


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


class MethodesPiegesEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("14.11 Méthodes, pièges à éviter et essentiel")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : synthèse du chapitre --------------------------------------------
        intro = Text(
            _wrap(
                "Terminons ce chapitre sur l'électrolyse par une synthèse "
                "méthodologique : comment procéder efficacement, et quels "
                "pièges éviter à tout prix.",
                width=58,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce chapitre sur l'électrolyse par une synthèse "
                "méthodologique : comment procéder efficacement face à un "
                "exercice, et quels pièges éviter à tout prix."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : méthode 1, écrire l'équation-bilan en 5 étapes -----------
        methode1 = method_box(
            VGroup(
                Text("Écrire l'équation-bilan d'une électrolyse en 5 étapes", font_size=19, weight="BOLD"),
                Text("1. Identifier toutes les espèces en présence (ions, eau, nature des électrodes).", font_size=15),
                Text("2. Appliquer la règle de priorité à CHAQUE électrode (ou repérer une anode soluble).", font_size=15),
                Text("3. Écrire les deux demi-équations (oxydation à l'anode, réduction à la cathode).", font_size=15),
                Text("4. Multiplier si besoin pour ÉGALISER le nombre d'électrons échangés.", font_size=15),
                Text("5. ADDITIONNER les deux demi-équations : les électrons disparaissent.", font_size=15),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=12.4,
        )
        methode1.next_to(titre, DOWN, buff=0.4)
        _fit(methode1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Première méthode : comment écrire l'équation-bilan d'une "
                "électrolyse, en cinq étapes. Un, identifier toutes les "
                "espèces en présence : les ions dissous, l'eau, et la "
                "nature des électrodes. Deux, appliquer la règle de "
                "priorité à chaque électrode, ou repérer si l'anode est "
                "soluble. Trois, écrire les deux demi-équations, "
                "oxydation à l'anode, réduction à la cathode. Quatre, "
                "multiplier si besoin pour égaliser le nombre d'électrons "
                "échangés. Cinq, additionner les deux demi-équations : "
                "les électrons doivent alors disparaître complètement."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Exemple traité : méthode 2, chaîne de calcul quantitatif ----------------
        methode2 = method_box(
            VGroup(
                Text("Chaîne de calcul quantitatif", font_size=20, weight="BOLD"),
                Text("I, t  →  Q = I×t  →  n(e⁻) = Q/F  →  n(produit) via la demi-équation  →  m ou V", font_size=17),
                Text(
                    "Repère complémentaire : une ANODE SOLUBLE se reconnaît "
                    "à une électrode faite du MÊME MÉTAL que celui présent "
                    "en ions dans la solution — dans ce cas, c'est ce "
                    "métal, et non l'eau ni un ion Cl⁻, qui s'oxyde.",
                    font_size=16,
                ),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.4,
        )
        methode2.next_to(titre, DOWN, buff=0.4)
        _fit(methode2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : la chaîne de calcul quantitatif, "
                "toujours dans le même ordre. À partir de l'intensité I "
                "et de la durée t, on calcule Q égale I fois t. On en "
                "déduit n de e moins, égal à Q sur F. Grâce au "
                "coefficient de la demi-équation, on obtient la quantité "
                "de matière du produit formé. Et enfin, on calcule sa "
                "masse ou son volume. Un repère complémentaire pour "
                "identifier une anode soluble : elle est faite du même "
                "métal que celui présent en ions dans la solution — dans "
                "ce cas précis, c'est ce métal qui s'oxyde, pas l'eau, "
                "ni un ion chlorure éventuellement présent."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Pièges à éviter --------------------------------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "PIÈGE 1 : ne pas inverser la polarité anode/cathode "
                    "par rapport à une pile. En ÉLECTROLYSE, l'anode est "
                    "le pôle POSITIF du générateur (l'inverse de la pile).",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Premier piège à éviter absolument : ne jamais inverser "
                "la polarité anode-cathode par rapport à une pile. En "
                "électrolyse, l'anode est le pôle positif du générateur, "
                "exactement l'inverse de la pile."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            Text(
                _wrap(
                    "PIÈGE 2 : les ions « fantômes » — Na⁺, K⁺, Ca²⁺, Mg²⁺, "
                    "Al³⁺ à la cathode, et SO₄²⁻, NO₃⁻ à l'anode — ne "
                    "réagissent JAMAIS en solution aqueuse : c'est "
                    "toujours l'eau qui réagit à leur place.",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Deuxième piège : les ions fantômes. Les ions sodium, "
                "potassium, calcium, magnésium et aluminium à la "
                "cathode, les ions sulfate et nitrate à l'anode, ne "
                "réagissent jamais en solution aqueuse : c'est toujours "
                "l'eau qui réagit à leur place."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            Text(
                _wrap(
                    "PIÈGE 3 : unités et coefficients — convertir "
                    "SYSTÉMATIQUEMENT la durée en secondes avant de "
                    "calculer Q, et ne jamais oublier le nombre "
                    "d'électrons n de la demi-équation dans le calcul "
                    "de n(produit) = n(e⁻) / n.",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege3.next_to(titre, DOWN, buff=0.45)
        _fit(piege3, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Troisième piège : les unités et les coefficients. "
                "Convertissez systématiquement la durée en secondes avant "
                "de calculer Q, et n'oubliez jamais de diviser par le "
                "nombre d'électrons n de la demi-équation pour passer de "
                "n de e moins à la quantité de matière du produit."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- À retenir : l'essentiel du chapitre --------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'ESSENTIEL DU CHAPITRE 14 — ÉLECTROLYSE", font_size=18, weight="BOLD"),
                Text("• Électrolyse = transformation FORCÉE par un générateur (inverse de la pile).", font_size=14),
                Text("• Anode = pôle + = oxydation ; Cathode = pôle − = réduction.", font_size=14),
                Text("• Électrons dans les fils ; double migration des ions (cations→C, anions→A) dans l'électrolyte.", font_size=14),
                Text("• Électrode inerte : priorité à l'espèce la plus facile à oxyder/réduire ; anode soluble : le métal s'oxyde.", font_size=14),
                Text("• Q = I×t = n(e⁻)×F, avec F ≈ 96500 C/mol, pour relier le courant à la matière produite.", font_size=14),
                Text("• Applications : affinage, galvanoplastie, électrozingage, chlore-soude, sels fondus.", font_size=14),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=12.6,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)
        _fit(essentiel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pour conclure, voici l'essentiel à retenir de ce "
                "chapitre sur l'électrolyse. Une électrolyse est une "
                "transformation forcée par un générateur, l'inverse d'une "
                "pile. L'anode est le pôle positif, siège de l'oxydation ; "
                "la cathode est le pôle négatif, siège de la réduction. "
                "Les électrons circulent dans les fils, tandis qu'une "
                "double migration d'ions se produit dans l'électrolyte, "
                "les cations vers la cathode, les anions vers l'anode. "
                "Avec une électrode inerte, c'est l'espèce la plus facile "
                "à oxyder ou à réduire qui réagit en priorité ; avec une "
                "anode soluble, c'est le métal de l'électrode lui-même "
                "qui s'oxyde. Enfin, la relation Q égale I fois t, égale "
                "n de e moins fois F, permet de relier le courant "
                "électrique à la quantité de matière réellement produite. "
                "Ce chapitre trouve de nombreuses applications "
                "industrielles : affinage des métaux, galvanoplastie, "
                "électrozingage, industrie chlore-soude, et électrolyse "
                "de sels fondus pour les métaux les plus réducteurs."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
