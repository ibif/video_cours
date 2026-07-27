"""
scenes/Physique_ChampElectrostatique_04.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 04.

§ Notion de champ électrostatique et vecteur champ : expérience du
pendule électrostatique dévié sans contact, définition du champ
électrostatique (région où un corps chargé subit une force), définition
du vecteur champ E⃗(M)=F⃗/q, caractéristiques (origine M, direction/sens
de F⃗ si q>0 ou opposé si q<0, norme E=F/|q| en N/C ou V/m), remarque : E
ne dépend pas de la charge test.
Source : 1ereC/Physique.pdf, pages 54-65 (chapitre 6, § 3).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    BLUE,
    Arrow,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ChampElectrostatiqueVecteurChamp(NotionScene):
    def construct(self):
        titre = scene_title("Notion de champ électrostatique, vecteur champ")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : pendule dévié sans contact -----------------------------------
        source = Dot(LEFT * 3.0, color=RED, radius=0.18)
        source_label = MathTex("Q", font_size=26).next_to(source, UP, buff=0.2)
        fil = Line(RIGHT * 1.0 + UP * 1.3, RIGHT * 1.0, color=WHITE, stroke_width=1.5)
        boule = Dot(fil.get_end(), color=YELLOW, radius=0.14)
        fleche_deviation = Arrow(boule.get_center(), boule.get_center() + LEFT * 0.7, buff=0.1, color=YELLOW, stroke_width=3)
        schema = VGroup(source, source_label, fil, boule, fleche_deviation)
        schema.move_to(DOWN * 0.3)

        mise_en_situation = Text(
            _wrap(
                "Une petite boule chargée, suspendue à un fil, est "
                "déviée dès qu'on approche une charge Q, SANS AUCUN "
                "CONTACT. Quelque chose existe donc dans l'espace "
                "autour de Q, même en l'absence de la boule.",
                width=50,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(schema, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons notre pendule électrostatique : une petite "
                "boule chargée, suspendue à un fil. Dès que l'on "
                "approche une charge Q, la boule est déviée, sans aucun "
                "contact. Il existe donc, dans l'espace autour de Q, "
                "quelque chose capable d'exercer une force à distance, "
                "même en l'absence de la boule : c'est le champ "
                "électrostatique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(mise_en_situation))

        # --- Définition : champ électrostatique -------------------------------------
        definition1 = definition_box(
            VGroup(
                Text("Champ électrostatique", font_size=23, weight="BOLD"),
                Text(
                    "Région de l'espace où un corps chargé placé subit",
                    font_size=20,
                ),
                Text("une force électrique.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=10.6,
        )
        definition1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le champ électrostatique créé par une ou plusieurs "
                "charges est la région de l'espace où tout corps chargé "
                "placé subit une force électrique."
            )
        ) as tracker:
            self.play(FadeIn(definition1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition1))

        # --- Définition : vecteur champ E(M) = F/q ----------------------------------
        m_point = Dot(ORIGIN, color=YELLOW, radius=0.1)
        m_label = MathTex("M", font_size=24).next_to(m_point, DOWN, buff=0.15)
        f_vec = Arrow(m_point.get_center(), m_point.get_center() + RIGHT * 1.6, buff=0.1, color=BLUE, stroke_width=3)
        f_label = MathTex(r"\vec{F}", font_size=26, color=BLUE).next_to(f_vec, UP, buff=0.1)
        e_vec = Arrow(m_point.get_center(), m_point.get_center() + RIGHT * 1.6, buff=0.1, color=YELLOW, stroke_width=3)
        e_vec.shift(DOWN * 0.5)
        e_label = MathTex(r"\vec{E}(M)", font_size=26, color=YELLOW).next_to(e_vec, DOWN, buff=0.1)
        schema2 = VGroup(m_point, m_label, f_vec, f_label, e_vec, e_label)
        schema2.next_to(titre, DOWN, buff=0.7)

        definition2 = definition_box(
            VGroup(
                Text("Vecteur champ électrostatique en un point M", font_size=22, weight="BOLD"),
                MathTex(r"\vec{E}(M) = \dfrac{\vec{F}}{q}", font_size=32),
                Text("q : charge test placée en M, F⃗ : force qu'elle subit.", font_size=19),
            ).arrange(DOWN, buff=0.22),
            box_width=11.0,
        )
        definition2.next_to(schema2, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On définit alors le vecteur champ électrostatique en un "
                "point M : on y place une petite charge test q, on "
                "mesure la force F qu'elle subit, et l'on pose E de M "
                "égale F sur q."
            )
        ) as tracker:
            self.play(Create(schema2))
            self.play(FadeIn(definition2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema2), FadeOut(definition2))

        # --- Caractéristiques du vecteur champ --------------------------------------
        caracteristiques = definition_box(
            VGroup(
                Text("Caractéristiques du vecteur champ E⃗(M)", font_size=22, weight="BOLD"),
                Text("• Origine : le point M.", font_size=19),
                Text("• Direction et sens : ceux de F⃗ si q > 0,", font_size=19),
                Text("   sens OPPOSÉ à F⃗ si q < 0.", font_size=19),
                MathTex(r"\bullet \ \text{Norme : } E = \dfrac{F}{|q|} \ \text{ en N/C ou V/m}", font_size=22),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.4,
        )
        caracteristiques.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le vecteur champ E de M possède trois caractéristiques. "
                "Son origine est le point M. Sa direction et son sens "
                "sont ceux de la force F si la charge test q est "
                "positive, mais de sens opposé à F si q est négative. Et "
                "sa norme vaut E égale F sur la valeur absolue de q, "
                "exprimée en newton par coulomb, ou de façon équivalente "
                "en volt par mètre."
            )
        ) as tracker:
            self.play(FadeIn(caracteristiques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(caracteristiques))

        # --- Remarque : E ne dépend pas de la charge test ---------------------------
        remarque = warning_box(
            VGroup(
                Text("• Le champ E⃗(M) est une propriété du point M, imposée", font_size=20),
                Text("   par les charges SOURCES : il ne dépend PAS de la", font_size=20),
                Text("   valeur de la charge test q utilisée pour le mesurer.", font_size=20),
                Text("• Si l'on double q, la force F double aussi : le", font_size=20),
                Text("   rapport E = F/q reste inchangé.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        remarque.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Remarque essentielle : le champ E de M est une "
                "propriété du point M, imposée par les charges qui le "
                "créent. Il ne dépend absolument pas de la valeur de la "
                "charge test q utilisée pour le mesurer : si l'on double "
                "q, la force F double également, si bien que le rapport "
                "E égale F sur q reste inchangé."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Exemple résolu -----------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Une charge q = +4 nC placée en M subit une force F = 8×10⁻⁵ N.", font_size=19),
                MathTex(r"E(M) = \dfrac{F}{q} = \dfrac{8\times 10^{-5}}{4\times 10^{-9}} = 2\times 10^{4}\ \text{N/C}", font_size=23, color=YELLOW),
                Text("q > 0 : E⃗(M) est dans le même sens que F⃗.", font_size=19),
            ).arrange(DOWN, buff=0.24),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : une charge q égale plus quatre nanocoulombs, "
                "placée en M, subit une force F égale huit fois dix "
                "puissance moins cinq newton. Le champ vaut alors E de M "
                "égale F sur q, soit deux fois dix puissance quatre "
                "newton par coulomb. Comme q est positive, le vecteur "
                "champ est dans le même sens que la force."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\vec{E}(M) = \dfrac{\vec{F}}{q}, \qquad E = \dfrac{F}{|q|}\ (\text{N/C ou V/m})", font_size=26),
                Text("Sens de F⃗ si q > 0, sens opposé si q < 0.", font_size=20),
                Text("E(M) ne dépend PAS de la charge test q.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le vecteur champ E de M vaut F "
                "sur q, de norme F sur la valeur absolue de q, exprimée "
                "en newton par coulomb ou volt par mètre. Il est dans le "
                "sens de F si q est positive, en sens opposé si q est "
                "négative. Et surtout, E de M ne dépend pas de la charge "
                "test utilisée."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
