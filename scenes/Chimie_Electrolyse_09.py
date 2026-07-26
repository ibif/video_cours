"""
scenes/Chimie_Electrolyse_09.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 09.

§ 9. Aspect quantitatif : quantité d'électricité et lien avec la quantité
de matière. Définition de la quantité d'électricité Q = I × t (I en
ampères, t en secondes, Q en coulombs). Constante de Faraday
F ≈ 96500 C/mol (charge d'une mole d'électrons). Propriété
Q = n(e⁻) × F et conséquences pratiques (calcul de la masse de métal
déposé, du volume de gaz dégagé). Exemple résolu 3 : électrolyse d'une
solution de CuSO₄ avec anode de cuivre, I = 2,0 A, t = 1 h, calcul de la
masse de cuivre déposée à la cathode (≈ 2,37 g).
Source : 1ereC/Chimie.pdf, chapitre 14, pages 142-143.
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
from shapes.boxes import definition_box, example_box, property_box, scene_title


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


class QuantiteElectriciteFaraday(NotionScene):
    def construct(self):
        titre = scene_title("14.9 Quantité d'électricité et quantité de matière")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : la question quantitative ---------------------------------------
        intro = Text(
            _wrap(
                "Jusqu'ici, nous savions PRÉVOIR la nature des produits "
                "d'une électrolyse. Pouvons-nous aussi CALCULER la masse "
                "de métal déposé, ou le volume de gaz dégagé ?",
                width=58,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Jusqu'ici, nous savions prévoir la nature des produits "
                "d'une électrolyse. Mais peut-on aussi calculer la masse "
                "exacte de métal déposé, ou le volume exact de gaz "
                "dégagé, en fonction de la durée et de l'intensité du "
                "courant ? C'est l'objet de cette partie quantitative."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : quantité d'électricité Q = I x t --------------------------
        def_q = definition_box(
            VGroup(
                Text("La quantité d'électricité Q est la charge électrique", font_size=20),
                Text("totale ayant traversé le circuit pendant la durée t :", font_size=20),
                MathTex(r"Q = I \times t", font_size=32, color="#1A1A1A"),
                Text("(I en ampères A, t en secondes s, Q en coulombs C)", font_size=17),
            ).arrange(DOWN, buff=0.22),
        )
        def_q.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Commençons par définir la quantité d'électricité, notée "
                "Q. C'est la charge électrique totale ayant traversé le "
                "circuit pendant la durée de l'électrolyse. Elle se "
                "calcule par la relation Q égale I fois t, où I est "
                "l'intensité du courant en ampères, t la durée en "
                "secondes, et Q s'exprime alors en coulombs. Attention : "
                "la durée doit impérativement être convertie en secondes."
            )
        ) as tracker:
            self.play(FadeIn(def_q))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_q))

        # --- Constante de Faraday + propriété Q = n(e-) x F ----------------------------
        entete_faraday = Text("La constante de Faraday", font_size=21, color=YELLOW, weight="BOLD")
        entete_faraday.next_to(titre, DOWN, buff=0.35)

        faraday_txt = VGroup(
            Text(
                "Une mole d'électrons transporte une charge fixe, "
                "appelée constante de Faraday :",
                font_size=19,
            ),
            MathTex(r"F \approx 96500\ C/mol", font_size=30, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        faraday_txt.next_to(entete_faraday, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cette charge, à l'échelle microscopique, provient du "
                "déplacement d'électrons. Or, une mole d'électrons "
                "transporte toujours une charge fixe, appelée constante "
                "de Faraday, notée F, et qui vaut environ quatre-vingt-"
                "seize mille cinq cents coulombs par mole."
            )
        ) as tracker:
            self.play(FadeIn(entete_faraday))
            self.play(Write(faraday_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_faraday), FadeOut(faraday_txt))

        propriete = property_box(
            VGroup(
                Text("La quantité d'électricité et la quantité de matière", font_size=19),
                Text("d'électrons échangés n(e⁻) sont reliées par :", font_size=19),
                MathTex(r"Q = n(e^-) \times F", font_size=32, color="#1A1A1A"),
                Text(
                    "→ permet de calculer n(e⁻), puis, via les demi-équations, "
                    "n(produit), puis sa masse m ou son volume V.",
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.5,
        )
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On obtient ainsi la propriété centrale de cette partie "
                "quantitative : Q égale n de e moins, fois F, où n de e "
                "moins est la quantité de matière d'électrons échangés "
                "pendant l'électrolyse. Cette relation permet de calculer "
                "n de e moins à partir de Q, puis, grâce aux coefficients "
                "des demi-équations, la quantité de matière du produit "
                "formé, puis enfin sa masse ou son volume."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple résolu 3 ----------------------------------------------------------
        exemple3 = example_box(
            VGroup(
                Text("Exemple résolu — électrolyse de CuSO₄, anode de cuivre", font_size=18, weight="BOLD"),
                Text("Données : I = 2,0 A ; t = 1 h. Masse de cuivre déposée à la cathode ?", font_size=16),
                MathTex(r"t = 1\ h = 3600\ s \quad\Rightarrow\quad Q = I \times t = 2{,}0 \times 3600 = 7200\ C", font_size=20, color="#1A1A1A"),
                MathTex(r"n(e^-) = \dfrac{Q}{F} = \dfrac{7200}{96500} \approx 7{,}46 \times 10^{-2}\ mol", font_size=20, color="#1A1A1A"),
                MathTex(r"Cu^{2+} + 2\,e^- \longrightarrow Cu \quad\Rightarrow\quad n(Cu) = \dfrac{n(e^-)}{2} \approx 3{,}73 \times 10^{-2}\ mol", font_size=19, color="#1A1A1A"),
                MathTex(r"m(Cu) = n(Cu) \times M(Cu) = 3{,}73 \times 10^{-2} \times 63{,}5 \approx 2{,}37\ g", font_size=21, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.6,
        )
        exemple3.next_to(titre, DOWN, buff=0.4)
        _fit(exemple3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Traitons un exemple complet. On électrolyse une solution "
                "de sulfate de cuivre avec une anode de cuivre, sous une "
                "intensité de deux virgule zéro ampères pendant une "
                "heure. Quelle masse de cuivre se dépose à la cathode ? "
                "D'abord, on convertit la durée en secondes : une heure "
                "égale trois mille six cents secondes. On calcule ensuite "
                "Q, égal à I fois t, soit deux virgule zéro fois trois "
                "mille six cents, soit sept mille deux cents coulombs. On "
                "en déduit n de e moins, égal à Q sur F, soit environ "
                "sept virgule quarante-six fois dix puissance moins deux "
                "mole. La demi-équation à la cathode, Cu deux plus plus "
                "deux électrons donne Cu, montre qu'il faut deux "
                "électrons pour déposer une mole de cuivre : n de Cu vaut "
                "donc n de e moins divisé par deux, soit environ trois "
                "virgule soixante-treize fois dix puissance moins deux "
                "mole. Enfin, la masse de cuivre déposée vaut n de Cu "
                "fois la masse molaire du cuivre, soixante-trois virgule "
                "cinq grammes par mole, soit environ deux virgule "
                "trente-sept grammes."
            )
        ) as tracker:
            self.play(FadeIn(exemple3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple3))

        # --- À retenir : conséquences pratiques -----------------------------------------
        consequences = _bullets(
            [
                "cette même chaîne de calcul s'applique à TOUT produit "
                "d'électrolyse : métal déposé, mais aussi dihydrogène ou "
                "dioxygène dégagé (via le volume molaire) ;",
                "à courant I fixé, la masse (ou le volume) de produit "
                "obtenu est directement PROPORTIONNELLE au temps "
                "d'électrolyse t.",
            ],
            font_size=19,
            width=56,
        )
        entete_conseq = Text("À retenir", font_size=21, color="#288073", weight="BOLD")
        entete_conseq.next_to(titre, DOWN, buff=0.4)
        consequences.next_to(entete_conseq, DOWN, buff=0.3)
        _fit(VGroup(entete_conseq, consequences), entete_conseq.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Retenons que cette même chaîne de calcul, de l'intensité "
                "et du temps jusqu'à la masse ou au volume de produit, "
                "s'applique à toute électrolyse : dépôt métallique, mais "
                "aussi dégagement de dihydrogène ou de dioxygène, en "
                "passant alors par le volume molaire. Et à intensité "
                "fixée, la masse ou le volume de produit obtenu est "
                "directement proportionnel à la durée de l'électrolyse."
            )
        ) as tracker:
            self.play(FadeIn(entete_conseq))
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_conseq), FadeOut(consequences), FadeOut(titre))
