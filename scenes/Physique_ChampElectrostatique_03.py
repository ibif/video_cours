"""
scenes/Physique_ChampElectrostatique_03.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 03.

§ La loi de Coulomb : définition d'une charge ponctuelle, énoncé de la loi
de Coulomb (F=k|qA·qB|/d², k=9,0×10⁹ N·m²·C⁻², attractive ou répulsive
selon les signes), expression vectorielle F⃗=k(qA·qB/d²)u⃗. Exemple résolu
1 : q1=+2µC, q2=+3µC, d=50cm → F=0,216N, puis d divisée par 2 → F×4.
Exemple résolu 2 : comparaison force électrique / force gravitationnelle
dans l'atome d'hydrogène (rapport ≈2,3×10³⁹).
Source : 1ereC/Physique.pdf, pages 54-65 (chapitre 6, § 2).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LoiDeCoulomb(NotionScene):
    def construct(self):
        titre = scene_title("La loi de Coulomb")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : deux charges ponctuelles séparées par une distance d --------
        qa = Dot(LEFT * 2.5, color=RED, radius=0.16)
        qa_label = MathTex("q_A", font_size=26).next_to(qa, UP, buff=0.2)
        qb = Dot(RIGHT * 2.5, color=RED, radius=0.16)
        qb_label = MathTex("q_B", font_size=26).next_to(qb, UP, buff=0.2)
        d_ligne = Line(qa.get_center() + DOWN * 0.8, qb.get_center() + DOWN * 0.8, color=WHITE, stroke_width=1.5)
        d_label = MathTex("d", font_size=26).next_to(d_ligne, DOWN, buff=0.15)
        schema = VGroup(qa, qa_label, qb, qb_label, d_ligne, d_label)
        schema.next_to(titre, DOWN, buff=0.6)

        mise_en_situation = Text(
            _wrap(
                "Deux charges ponctuelles qA et qB, séparées d'une "
                "distance d dans le vide, exercent l'une sur l'autre "
                "une force électrique. De quoi dépend son intensité ?",
                width=54,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(schema, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Considérons deux charges ponctuelles q A et q B, "
                "séparées d'une distance d dans le vide. Une charge "
                "ponctuelle est une charge dont les dimensions sont "
                "négligeables devant la distance qui la sépare des "
                "autres charges. Ces deux charges exercent l'une sur "
                "l'autre une force électrique. De quoi dépend son "
                "intensité ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(mise_en_situation))

        # --- Théorème : énoncé de la loi de Coulomb --------------------------------
        loi = theorem_box(
            VGroup(
                Text("Loi de Coulomb", font_size=24, weight="BOLD"),
                MathTex(r"F = k\,\dfrac{|q_A \cdot q_B|}{d^2}", font_size=32),
                MathTex(r"k = 9{,}0 \times 10^{9}\ \text{N}\cdot\text{m}^2\cdot\text{C}^{-2}", font_size=24),
                Text("Répulsive si qA et qB de même signe,", font_size=20),
                Text("attractive si qA et qB de signes contraires.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        loi.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La loi de Coulomb énonce que l'intensité de la force "
                "électrique entre deux charges ponctuelles q A et q B, "
                "séparées d'une distance d, vaut F égale k fois la "
                "valeur absolue du produit de q A par q B, le tout "
                "divisé par d au carré. La constante k vaut neuf fois "
                "dix puissance neuf newton mètre carré par coulomb "
                "carré. Cette force est répulsive si les deux charges "
                "sont de même signe, et attractive si elles sont de "
                "signes contraires."
            )
        ) as tracker:
            self.play(FadeIn(loi))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi))

        # --- Expression vectorielle -------------------------------------------------
        qa2 = Dot(LEFT * 2.5, color=RED, radius=0.16)
        qb2 = Dot(RIGHT * 2.5, color=RED, radius=0.16)
        u_vec = Arrow(qa2.get_center(), qb2.get_center(), buff=0.2, color=YELLOW, stroke_width=3)
        u_label = MathTex(r"\vec{u}", font_size=26, color=YELLOW).next_to(u_vec, UP, buff=0.15)
        f_vec = Arrow(qb2.get_center(), qb2.get_center() + RIGHT * 1.2, buff=0.2, color=BLUE, stroke_width=3)
        f_label = MathTex(r"\vec{F}_{A/B}", font_size=24, color=BLUE).next_to(f_vec, RIGHT, buff=0.15)
        schema_vect = VGroup(qa2, qb2, u_vec, u_label, f_vec, f_label)
        schema_vect.next_to(titre, DOWN, buff=0.7)

        formule_vect = MathTex(
            r"\vec{F}_{A/B} = k\,\dfrac{q_A\, q_B}{d^2}\ \vec{u}",
            font_size=30,
        )
        formule_vect.next_to(schema_vect, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sous forme vectorielle, en notant u le vecteur unitaire "
                "porté par la droite qui joint les deux charges, orienté "
                "de A vers B, la force exercée par q A sur q B s'écrit F "
                "A sur B égale k fois q A fois q B, divisé par d au "
                "carré, fois u. Le signe du produit q A q B donne "
                "directement le sens du vecteur : positif, la force "
                "pousse dans le sens de u, donc repousse ; négatif, elle "
                "pointe en sens inverse, donc attire."
            )
        ) as tracker:
            self.play(Create(schema_vect))
            self.play(Write(formule_vect))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_vect), FadeOut(formule_vect))

        # --- Exemple résolu 1 : F puis d/2 -----------------------------------------
        exemple1 = example_box(
            VGroup(
                Text("q1 = +2 µC, q2 = +3 µC, d = 50 cm = 0,50 m", font_size=20),
                MathTex(r"F = 9\times 10^9 \times \dfrac{2\times 10^{-6}\times 3\times 10^{-6}}{0{,}50^2} = 0{,}216\ \text{N}", font_size=22),
                Text("Si l'on divise d par 2 (d' = 0,25 m) :", font_size=20),
                MathTex(r"F' = k\dfrac{q_1 q_2}{(d/2)^2} = 4\,F = 0{,}864\ \text{N}", font_size=24, color=YELLOW),
            ).arrange(DOWN, buff=0.24),
            box_width=12.0,
        )
        exemple1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : deux charges q un égale plus deux "
                "microcoulombs et q deux égale plus trois microcoulombs, "
                "séparées de cinquante centimètres, soit zéro virgule "
                "cinquante mètre. La force vaut neuf fois dix puissance "
                "neuf, fois deux fois dix puissance moins six, fois trois "
                "fois dix puissance moins six, divisé par zéro virgule "
                "cinquante au carré, soit zéro virgule deux cent seize "
                "newton. Si l'on divise maintenant la distance par deux, "
                "la force est multipliée par quatre, car elle varie en "
                "un sur d au carré : elle atteint zéro virgule huit cent "
                "soixante-quatre newton."
            )
        ) as tracker:
            self.play(FadeIn(exemple1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple1))

        # --- Exemple résolu 2 : force électrique vs gravitationnelle --------------
        exemple2 = example_box(
            VGroup(
                Text("Dans l'atome d'hydrogène (proton-électron) :", font_size=20),
                MathTex(r"\dfrac{F_{\text{élec}}}{F_{\text{grav}}} \approx 2{,}3\times 10^{39}", font_size=27, color=YELLOW),
                Text("La force gravitationnelle est totalement négligeable", font_size=19),
                Text("devant la force électrique à l'échelle atomique.", font_size=19),
            ).arrange(DOWN, buff=0.24),
            box_width=11.4,
        )
        exemple2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième exemple résolu : comparons, dans l'atome "
                "d'hydrogène, la force électrique entre le proton et "
                "l'électron à leur force gravitationnelle. Le rapport de "
                "ces deux forces vaut environ deux virgule trois fois dix "
                "puissance trente-neuf. Autrement dit, la force "
                "gravitationnelle est totalement négligeable devant la "
                "force électrique à l'échelle atomique."
            )
        ) as tracker:
            self.play(FadeIn(exemple2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple2))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"F = k\,\dfrac{|q_A q_B|}{d^2}, \quad k = 9{,}0\times 10^{9}\ \text{N}\cdot\text{m}^2\cdot\text{C}^{-2}", font_size=24),
                Text("Même signe → répulsion. Signes contraires → attraction.", font_size=20),
                Text("F varie en 1/d² : diviser d par 2 multiplie F par 4.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la loi de Coulomb donne F égale "
                "k fois la valeur absolue de q A q B, divisé par d au "
                "carré, avec k égale neuf fois dix puissance neuf. Même "
                "signe donne répulsion, signes contraires donnent "
                "attraction. Et comme la force varie en un sur d au "
                "carré, diviser la distance par deux multiplie la force "
                "par quatre."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Toujours convertir d en MÈTRES avant de calculer F", font_size=20),
                Text("   (une distance oubliée en cm fausse F d'un facteur 10⁴).", font_size=20),
                Text("• La valeur absolue dans F = k|qA·qB|/d² donne", font_size=20),
                Text("   l'INTENSITÉ ; le signe de qA·qB donne seulement le", font_size=20),
                Text("   caractère attractif ou répulsif, jamais une force", font_size=20),
                Text("   négative.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. D'abord, toujours convertir la "
                "distance d en mètres avant de calculer F : une distance "
                "oubliée en centimètres fausse le résultat d'un facteur "
                "dix mille. Ensuite, la valeur absolue dans la formule "
                "donne l'intensité de la force, qui n'est jamais "
                "négative ; c'est uniquement le signe du produit q A q B "
                "qui indique si la force est attractive ou répulsive."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
