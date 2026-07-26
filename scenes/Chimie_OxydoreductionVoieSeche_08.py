"""
scenes/Chimie_OxydoreductionVoieSeche_08.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 08.

§ 5. Applications métallurgiques : la sidérurgie et le haut fourneau.
Chargement (minerai, coke, fondant), air chaud aux tuyères, réactions
successives (combustion du coke, formation de CO, réduction
Fe₂O₃ + 3CO → 2Fe + 3CO₂, élimination de la gangue avec le laitier).
Produits (fonte, laitier, gaz). Tableau d'obtention des métaux selon leur
réactivité. Exemple résolu 4 : masse de fer produite à partir d'1 tonne
d'hématite.
Source : 1ereC/Chimie.pdf, chapitre 13, pages 131-133.
"""

import textwrap

from manim import (
    DOWN,
    GRAY,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
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


def _bullets(items, font_size=20, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


def _schema_haut_fourneau():
    """Coupe très simplifiée d'un haut fourneau, construite uniquement
    avec des primitives Manim de base (Polygon, Line, Arrow, Text,
    VGroup) — aucune bibliothèque externe."""
    contour = Polygon(
        [-0.55, 2.2, 0], [0.55, 2.2, 0], [0.75, 0.6, 0], [0.25, -1.6, 0],
        [-0.25, -1.6, 0], [-0.75, 0.6, 0],
        stroke_color=WHITE, stroke_width=2.5, fill_color=GRAY, fill_opacity=0.12,
    )

    charge = VGroup(*[
        Line([-0.5 + 0.1 * i, 2.15, 0], [-0.4 + 0.1 * i, 2.15, 0], color=ORANGE, stroke_width=4)
        for i in range(9)
    ])
    label_charge = Text("minerai + coke + fondant", font_size=13, color=ORANGE)
    label_charge.next_to(contour, UP, buff=0.15)

    tuyere_g = Arrow([-1.4, -1.0, 0], [-0.78, -1.0, 0], color="#DE7C1F", stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.3)
    tuyere_d = Arrow([1.4, -1.0, 0], [0.78, -1.0, 0], color="#DE7C1F", stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.3)
    label_tuyeres = Text("air chaud", font_size=13, color="#DE7C1F")
    label_tuyeres.next_to(tuyere_d, RIGHT, buff=0.1)

    zone1 = Text("combustion du coke", font_size=11, color=RED)
    zone1.move_to([0, -0.9, 0])
    zone2 = Text("formation de CO", font_size=11, color=YELLOW)
    zone2.move_to([0, -0.3, 0])
    zone3 = Text("réduction Fe₂O₃ + 3CO", font_size=11, color=WHITE)
    zone3.move_to([0, 0.5, 0])
    zone4 = Text("→ 2Fe + 3CO₂", font_size=11, color=WHITE)
    zone4.next_to(zone3, DOWN, buff=0.08)

    fonte = Line([-0.2, -1.55, 0], [0.05, -1.75, 0], color=ORANGE, stroke_width=6)
    label_fonte = Text("fonte", font_size=12, color=ORANGE)
    label_fonte.next_to(fonte, DOWN, buff=0.1)

    return VGroup(
        contour, charge, label_charge, tuyere_g, tuyere_d, label_tuyeres,
        zone1, zone2, zone3, zone4, fonte, label_fonte,
    )


def _tableau_reactivite():
    """Tableau d'obtention des métaux selon leur réactivité, construit
    avec des primitives Manim de base (Line, Text, VGroup)."""
    lignes = [
        ("Peu réactifs (Au, Ag, Pt)", "trouvés à l'état natif (métal pur)"),
        ("Moyennement réactifs (Cu, Hg)", "grillage du sulfure puis réduction"),
        ("Réactifs (Fe, Zn, Pb, Sn)", "réduction de l'oxyde par C ou CO"),
        ("Très réactifs (Al, Na, Mg, Ca)", "électrolyse (réducteurs chimiques insuffisants)"),
    ]
    col1 = VGroup(*[Text(t[0], font_size=17, color=YELLOW) for t in lignes])
    col1.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
    col2 = VGroup(*[Text(t[1], font_size=16, color=WHITE) for t in lignes])
    for a, b in zip(col1, col2):
        b.next_to(a, DOWN, buff=0.06, aligned_edge=LEFT)
    lignes_groupees = VGroup(*[VGroup(a, b) for a, b in zip(col1, col2)]).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
    return lignes_groupees


class MetallurgieSiderurgieHautFourneau(NotionScene):
    def construct(self):
        titre = scene_title("13.5 Applications métallurgiques : la sidérurgie")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : définitions métallurgie / sidérurgie -------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La MÉTALLURGIE est l'ensemble des techniques "
                    "d'extraction et d'élaboration des métaux à partir de "
                    "leurs minerais. La SIDÉRURGIE est la métallurgie du "
                    "FER, réalisée dans un HAUT FOURNEAU.",
                    width=44,
                ),
                font_size=22,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Nous savons désormais réduire un oxyde métallique en "
                "laboratoire. Voyons maintenant comment ce principe est "
                "utilisé à l'échelle industrielle. La métallurgie est "
                "l'ensemble des techniques d'extraction et d'élaboration "
                "des métaux à partir de leurs minerais. La sidérurgie est "
                "la métallurgie du fer, réalisée dans un immense four "
                "appelé haut fourneau."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : schéma du haut fourneau --------------------------
        schema = _schema_haut_fourneau()
        schema.scale(1.15)
        schema.next_to(titre, DOWN, buff=0.55).shift(LEFT * 3.3)

        legende = _bullets(
            [
                "Au sommet : chargement du minerai de fer (hématite "
                "Fe₂O₃), de coke (carbone) et de fondant (calcaire).",
                "Aux tuyères, en bas : soufflage d'air chaud.",
                "En descendant, la température augmente : plusieurs "
                "réactions se succèdent (voir schéma).",
            ],
            width=38,
        )
        legende.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Voici le principe du haut fourneau. Au sommet, on charge "
                "en continu le minerai de fer, généralement de "
                "l'hématite, Fe deux O trois, du coke, qui est du "
                "carbone, et du fondant, du calcaire. En bas, aux "
                "tuyères, on souffle de l'air chaud. En descendant à "
                "l'intérieur du four, la charge rencontre des "
                "températures de plus en plus élevées, et plusieurs "
                "réactions se succèdent."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(legende))

        # --- Raisonnement (suite) : les réactions successives -----------------
        entete_reac = Text("Les réactions successives, du bas vers le haut", font_size=20, color=YELLOW, weight="BOLD")
        entete_reac.next_to(titre, DOWN, buff=0.35)

        r1 = MathTex(r"1)\ \ C + O_2 \longrightarrow CO_2", font_size=24)
        r1_txt = Text("combustion du coke près des tuyères (zone la plus chaude)", font_size=15)
        r2 = MathTex(r"2)\ \ CO_2 + C \longrightarrow 2\,CO", font_size=24)
        r2_txt = Text("formation du monoxyde de carbone, plus haut", font_size=15)
        r3 = MathTex(r"3)\ \ Fe_2O_3 + 3\,CO \longrightarrow 2\,Fe + 3\,CO_2", font_size=24, color=ORANGE)
        r3_txt = Text("réduction du minerai par CO : c'est LE cœur de la sidérurgie", font_size=15)
        r4 = MathTex(r"4)\ \ CaCO_3 \longrightarrow CaO + CO_2\ ;\ \ CaO + gangue \longrightarrow laitier", font_size=20)
        r4_txt = Text("élimination de la gangue (silice) par le fondant", font_size=15)

        reactions = VGroup(
            VGroup(r1, r1_txt).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(r2, r2_txt).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(r3, r3_txt).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(r4, r4_txt).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        reactions.next_to(entete_reac, DOWN, buff=0.35)
        groupe_reac = VGroup(entete_reac, reactions)
        _fit(groupe_reac, titre.get_bottom()[1] - 0.1)
        groupe_reac.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Premièrement, près des tuyères, le coke brûle dans l'air "
                "chaud : C plus O deux donne CO deux, c'est la zone la "
                "plus chaude. Deuxièmement, un peu plus haut, ce CO deux "
                "réagit avec l'excès de coke pour former du monoxyde de "
                "carbone : CO deux plus C donne deux CO. Troisièmement, "
                "c'est ce monoxyde de carbone qui réduit le minerai de "
                "fer : Fe deux O trois plus trois CO, donne deux Fe plus "
                "trois CO deux — c'est le cœur même de la sidérurgie. "
                "Enfin, le fondant se décompose et capte la gangue, la "
                "silice indésirable du minerai, pour former un laitier "
                "liquide qui flotte au-dessus du fer fondu."
            )
        ) as tracker:
            self.play(FadeIn(entete_reac))
            self.play(Write(r1), FadeIn(r1_txt))
            self.play(Write(r2), FadeIn(r2_txt))
            self.play(Write(r3), FadeIn(r3_txt))
            self.play(Write(r4), FadeIn(r4_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_reac))

        # --- Exemple traité : masse de fer produite ---------------------------
        enonce_ex = Text("Exemple résolu : masse de fer produite à partir d'1 tonne d'hématite", font_size=18, color=WHITE)
        m1 = Text("M(Fe₂O₃) = 2×56 + 3×16 = 160 g/mol", font_size=18)
        m2 = Text("n(Fe₂O₃) = 1 000 000 g ÷ 160 g/mol = 6250 mol", font_size=18)
        m3 = MathTex(r"Fe_2O_3 + 3\,CO \longrightarrow 2\,Fe + 3\,CO_2", font_size=22)
        m4 = Text("n(Fe) = 2 × n(Fe₂O₃) = 2 × 6250 = 12 500 mol", font_size=18)
        m5 = Text("m(Fe) = 12 500 × 56 = 700 000 g", font_size=18)
        resultat = MathTex(r"m(Fe) = 700\ \text{kg}", font_size=26, color=ORANGE)

        contenu_ex = VGroup(enonce_ex, m1, m2, m3, m4, m5, resultat).arrange(DOWN, buff=0.22)
        boite_ex = example_box(contenu_ex, box_width=12.8)
        boite_ex.next_to(titre, DOWN, buff=0.3)
        _fit(boite_ex, titre.get_bottom()[1] - 0.1)

        with self.voiceover(
            text=(
                "Exemple résolu : quelle masse de fer peut-on produire à "
                "partir d'une tonne d'hématite pure ? La masse molaire de "
                "Fe deux O trois vaut cent soixante grammes par mole. Une "
                "tonne, soit un million de grammes, représente donc six "
                "mille deux cent cinquante moles d'hématite. D'après "
                "l'équation, une mole d'hématite donne deux moles de fer, "
                "donc douze mille cinq cents moles de fer sont produites. "
                "Comme la masse molaire du fer vaut cinquante-six grammes "
                "par mole, cela représente sept cent mille grammes, soit "
                "sept cents kilogrammes de fer."
            )
        ) as tracker:
            self.play(FadeIn(boite_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(boite_ex))

        # --- À retenir : produits et tableau de réactivité --------------------
        entete_tab = Text("Obtention des métaux selon leur réactivité", font_size=20, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_reactivite()
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.1)
        groupe_tab.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Le haut fourneau produit en réalité trois choses : la "
                "fonte, un fer liquide riche en carbone recueilli au "
                "fond, le laitier, récupéré séparément et valorisé dans "
                "le bâtiment, et des gaz de gueulard réutilisés comme "
                "combustible. Plus généralement, la méthode d'obtention "
                "d'un métal dépend de sa réactivité : les métaux peu "
                "réactifs, comme l'or ou l'argent, se trouvent à l'état "
                "natif ; les métaux moyennement réactifs, comme le "
                "cuivre, nécessitent un grillage puis une réduction ; les "
                "métaux réactifs, comme le fer, sont obtenus par "
                "réduction de leur oxyde par le carbone ou le monoxyde de "
                "carbone ; et les métaux très réactifs, comme "
                "l'aluminium, exigent une électrolyse, car aucun "
                "réducteur chimique n'est assez puissant."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre la FONTE (riche en carbone, "
                    "obtenue directement au haut fourneau) et l'ACIER "
                    "(fer raffiné, beaucoup moins riche en carbone, "
                    "obtenu par un traitement ultérieur de la fonte).",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre deux mots proches : la "
                "fonte, riche en carbone, est le produit direct du haut "
                "fourneau, tandis que l'acier, beaucoup moins riche en "
                "carbone, résulte d'un traitement ultérieur de cette "
                "fonte."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
