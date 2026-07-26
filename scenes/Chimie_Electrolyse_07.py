"""
scenes/Chimie_Electrolyse_07.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 07.

§ 7. Électrolyse à électrodes inertes : solution de sulfate de cuivre II
+ tableau récapitulatif. Expérience (dépôt de cuivre rouge à la cathode,
dégagement de dioxygène à l'anode, décoloration progressive de la
solution bleue, acidification de la solution). Demi-équations : cathode
Cu²⁺ + 2e⁻ → Cu, anode 2H₂O → O₂ + 4H⁺ + 4e⁻, équation-bilan
2Cu²⁺ + 2H₂O → 2Cu + O₂ + 4H⁺. Méthode : règle des ions spectateurs
(Na⁺, K⁺, Ca²⁺, Mg²⁺, Al³⁺ jamais réduits à la cathode ; SO₄²⁻, NO₃⁻
jamais oxydés à l'anode — c'est l'eau qui réagit à leur place). Tableau
récapitulatif des quatre électrolyses étudiées (H₂SO₄, NaCl, CuSO₄,
SnCl₂).
Source : 1ereC/Chimie.pdf, chapitre 14, pages 140-141.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    LIGHT_GRAY,
    ORANGE,
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
from shapes.boxes import method_box, scene_title


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


def _schema_cuso4():
    """Cuve à électrolyse d'une solution de sulfate de cuivre II à
    électrodes inertes : dépôt rouge de cuivre à la cathode, bulles de O2
    à l'anode, solution qui se décolore."""
    largeur, hauteur = 3.2, 1.8
    cuve = Rectangle(width=largeur, height=hauteur, color=LIGHT_GRAY, stroke_width=3)
    cuve.move_to([0, -0.9, 0])

    solution = Rectangle(width=largeur - 0.1, height=hauteur - 0.2, fill_color=BLUE, fill_opacity=0.22, stroke_width=0)
    solution.move_to(cuve.get_center())

    electrode_a = Line(cuve.get_center() + RIGHT * 1.0 + DOWN * 0.75, cuve.get_center() + RIGHT * 1.0 + UP * 0.9, color=LIGHT_GRAY, stroke_width=4)
    electrode_c = Line(cuve.get_center() + LEFT * 1.0 + DOWN * 0.75, cuve.get_center() + LEFT * 1.0 + UP * 0.9, color=LIGHT_GRAY, stroke_width=4)

    depot_cu = VGroup(*[
        Circle(radius=0.045, fill_color=ORANGE, fill_opacity=1, stroke_width=0)
        .move_to(electrode_c.get_center() + [-0.13, -0.5 + i * 0.22, 0])
        for i in range(5)
    ])
    label_c = Text("dépôt de Cu", font_size=13, color=ORANGE, weight="BOLD")
    label_c.next_to(electrode_c, UP, buff=0.15)

    bulles_o2 = VGroup(*[
        Circle(radius=0.06, color=YELLOW, stroke_width=1.5)
        .move_to(electrode_a.get_center() + [0.15, -0.3 + i * 0.3, 0])
        for i in range(4)
    ])
    label_a = Text("O₂", font_size=13, color=YELLOW, weight="BOLD")
    label_a.next_to(electrode_a, UP, buff=0.15)

    label_anode = Text("anode (+)", font_size=13, color=RED)
    label_anode.next_to(electrode_a, DOWN, buff=0.55)
    label_cathode = Text("cathode (−)", font_size=13, color=BLUE)
    label_cathode.next_to(electrode_c, DOWN, buff=0.55)

    return VGroup(
        cuve, solution,
        electrode_a, electrode_c, depot_cu, label_c, bulles_o2, label_a,
        label_anode, label_cathode,
    )


def _tableau_recapitulatif():
    """Tableau récapitulatif des 4 électrolyses étudiées."""
    lignes_txt = [
        ("Électrolyte", "Anode", "Cathode"),
        ("H₂SO₄", "O₂ (eau oxydée)", "H₂ (H⁺ réduit)"),
        ("NaCl", "Cl₂ (Cl⁻ oxydé)", "H₂ + HO⁻ (eau réduite)"),
        ("CuSO₄", "O₂ (eau oxydée)", "Cu (Cu²⁺ réduit)"),
        ("SnCl₂", "Cl₂ (Cl⁻ oxydé)", "Sn (Sn²⁺ réduit)"),
    ]
    col_x = [-3.6, -0.3, 3.1]
    tableau = VGroup()
    y = 1.3
    for i, (a, b, c) in enumerate(lignes_txt):
        couleur = YELLOW if i == 0 else WHITE
        poids = "BOLD" if i == 0 else "NORMAL"
        taille = 17 if i == 0 else 15
        ligne = VGroup(
            Text(a, font_size=taille, color=couleur, weight=poids),
            Text(b, font_size=taille, color=couleur, weight=poids),
            Text(c, font_size=taille, color=couleur, weight=poids),
        )
        ligne[0].move_to([col_x[0], y, 0])
        ligne[1].move_to([col_x[1], y, 0])
        ligne[2].move_to([col_x[2], y, 0])
        tableau.add(ligne)
        y -= 0.5

    trait_h = Line([-4.6, 1.0, 0], [4.6, 1.0, 0], color=LIGHT_GRAY, stroke_width=1.5)
    trait_v1 = Line([-1.9, 1.55, 0], [-1.9, -1.05, 0], color=LIGHT_GRAY, stroke_width=1)
    trait_v2 = Line([1.5, 1.55, 0], [1.5, -1.05, 0], color=LIGHT_GRAY, stroke_width=1)

    return VGroup(tableau, trait_h, trait_v1, trait_v2)


class ElectrolyseSulfateCuivreTableauRecap(NotionScene):
    def construct(self):
        titre = scene_title("14.7 Électrolyse du sulfate de cuivre II — récapitulatif")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé : le montage ---------------------------------------------------
        intro = Text(
            _wrap(
                "Dernière électrolyse à électrodes inertes : une solution "
                "de sulfate de cuivre II (Cu²⁺ + SO₄²⁻).",
                width=58,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étudions une dernière électrolyse à électrodes inertes : "
                "celle d'une solution de sulfate de cuivre deux, qui "
                "contient des ions cuivre deux plus et des ions sulfate."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : observations + schéma -----------------------------------
        entete_obs = Text("Observations expérimentales", font_size=21, color=YELLOW, weight="BOLD")
        entete_obs.next_to(titre, DOWN, buff=0.3)

        schema = _schema_cuso4()
        schema.next_to(entete_obs, DOWN, buff=0.35).shift(LEFT * 2.5)

        observations = _bullets(
            [
                "un dépôt ROUGE de cuivre métallique se forme à la "
                "CATHODE ;",
                "un gaz (dioxygène) se dégage à l'ANODE ;",
                "la solution bleue se DÉCOLORE et devient ACIDE.",
            ],
            width=32,
        )
        observations.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "On observe un dépôt rouge de cuivre métallique qui se "
                "forme à la cathode, un dégagement de dioxygène à "
                "l'anode, et la solution bleue se décolore progressivement "
                "tout en devenant acide."
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

        cathode_eq = VGroup(
            Text("Cathode (réduction de Cu²⁺) :", font_size=17, color=BLUE, weight="BOLD"),
            MathTex(r"Cu^{2+} + 2\,e^- \longrightarrow Cu", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        anode_eq = VGroup(
            Text("Anode (oxydation de l'eau) :", font_size=17, color=RED, weight="BOLD"),
            MathTex(r"2\,H_2O \longrightarrow O_2 + 4\,H^+ + 4\,e^-", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        bilan = VGroup(
            Text("Équation-bilan (cathode × 2 pour équilibrer) :", font_size=17, color=YELLOW, weight="BOLD"),
            MathTex(r"2\,Cu^{2+} + 2\,H_2O \longrightarrow 2\,Cu + O_2 + 4\,H^+", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        groupe_eq = VGroup(cathode_eq, anode_eq, bilan).arrange(DOWN, buff=0.3)
        groupe_eq.next_to(entete_eq, DOWN, buff=0.3)
        _fit(groupe_eq, entete_eq.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "À la cathode, l'ion cuivre deux plus est réduit : Cu deux "
                "plus, plus deux électrons, donne du cuivre métal, ce qui "
                "explique le dépôt rouge. À l'anode, il n'y a pas d'ion "
                "chlorure, bromure ou iodure : c'est donc l'eau qui est "
                "oxydée, produisant du dioxygène et des ions H plus, ce "
                "qui explique l'acidification. En multipliant la demi-"
                "équation de la cathode par deux puis en additionnant, on "
                "obtient l'équation-bilan : deux ions cuivre deux plus, "
                "plus deux molécules d'eau, donnent deux cuivres métal, "
                "une molécule de dioxygène, et quatre ions H plus."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(cathode_eq))
            self.play(Write(anode_eq))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(groupe_eq))

        # --- À retenir : règle des ions spectateurs (method_box) ---------------------
        methode = method_box(
            VGroup(
                Text("Règle des ions spectateurs", font_size=20, weight="BOLD"),
                Text(
                    "Certains ions ne réagissent JAMAIS en solution "
                    "aqueuse, quelle que soit l'électrolyse :",
                    font_size=16,
                ),
                Text("• à la CATHODE : Na⁺, K⁺, Ca²⁺, Mg²⁺, Al³⁺ (trop difficiles à réduire)", font_size=15),
                Text("• à l'ANODE : SO₄²⁻, NO₃⁻ (trop difficiles à oxyder)", font_size=15),
                Text("→ dans ces deux cas, c'est L'EAU qui réagit à leur place.", font_size=16, weight="BOLD"),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons une règle méthodologique très utile : certains "
                "ions ne réagissent jamais en solution aqueuse, quelle "
                "que soit l'électrolyse considérée. À la cathode, les "
                "ions sodium, potassium, calcium, magnésium et aluminium "
                "sont toujours trop difficiles à réduire. À l'anode, les "
                "ions sulfate et nitrate sont toujours trop difficiles à "
                "oxyder. Dans ces deux cas, c'est systématiquement l'eau "
                "qui réagit à leur place : ce sont des ions spectateurs."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Tableau récapitulatif ----------------------------------------------------
        entete_tab = Text("Tableau récapitulatif des 4 électrolyses étudiées", font_size=20, color="#288073", weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_recapitulatif()
        tableau.scale(0.85)
        tableau.next_to(entete_tab, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Faisons le bilan des quatre électrolyses étudiées "
                "jusqu'ici. Pour l'acide sulfurique, c'est l'eau qui "
                "réagit aux deux électrodes. Pour le chlorure de sodium, "
                "le chlorure est oxydé à l'anode, l'eau réduite à la "
                "cathode. Pour le sulfate de cuivre, l'eau est oxydée à "
                "l'anode, le cuivre déposé à la cathode. Et pour le "
                "chlorure d'étain de notre expérience de découverte, le "
                "chlorure est oxydé à l'anode, l'étain déposé à la "
                "cathode. Ce tableau résume l'essentiel : dans chaque "
                "cas, c'est l'espèce la plus facile à oxyder, ou à "
                "réduire, qui l'emporte."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau), FadeOut(titre))
