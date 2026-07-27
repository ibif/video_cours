"""
scenes/Physique_ChampElectrostatique_05.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 05.

§ Champ créé par une charge ponctuelle et principe de superposition :
démonstration de E⃗(M)=k(Q/r²)u⃗ à partir de la loi de Coulomb, direction
et sens (Q>0 champ divergent/centrifuge, Q<0 champ convergent/centripète),
remarque sur la décroissance en 1/r², principe de superposition
E⃗(M)=ΣE⃗_i(M) (démonstration courte via les forces). Exemple résolu 3 :
qA=+2nC, qB=-6nC, d=30cm, champ résultant en M (AM=10cm) → E=3150 N/C.
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
    GREEN,
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


class ChampChargePonctuelleSuperposition(NotionScene):
    def construct(self):
        titre = scene_title("Champ d'une charge ponctuelle, superposition")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : quel champ crée une charge ponctuelle Q ? --------------------
        mise_en_situation = Text(
            _wrap(
                "Quelle est l'expression du champ électrostatique créé, "
                "en un point M, par une charge ponctuelle Q seule dans "
                "le vide ?",
                width=52,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quelle est l'expression du champ électrostatique créé, "
                "en un point M, par une charge ponctuelle Q seule dans "
                "le vide ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : démonstration à partir de la loi de Coulomb -----------
        demonstration = VGroup(
            MathTex(r"F = k\,\dfrac{|Q\, q|}{r^2} \quad \text{(loi de Coulomb, charge test } q \text{ en M)}", font_size=25),
            MathTex(r"E(M) = \dfrac{F}{q} = k\,\dfrac{|Q|}{r^2}", font_size=28),
            MathTex(r"\Longrightarrow\ \vec{E}(M) = k\,\dfrac{Q}{r^2}\ \vec{u}", font_size=32, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        demonstration.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Plaçons une charge test q au point M, à une distance r "
                "de Q. D'après la loi de Coulomb, la force qu'elle subit "
                "vaut k fois la valeur absolue de Q q, divisée par r au "
                "carré. Comme le champ vaut E égale F sur q, on obtient E "
                "de M égale k fois Q, divisé par r au carré. Sous forme "
                "vectorielle, en notant u le vecteur unitaire dirigé de Q "
                "vers M, on écrit E de M égale k fois Q sur r carré, fois "
                "u."
            )
        ) as tracker:
            self.play(Write(demonstration[0]))
            self.play(Write(demonstration[1]))
            self.play(Write(demonstration[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demonstration))

        # --- Théorème : direction, sens, décroissance -------------------------------
        q_pos = Dot(LEFT * 3.2, color=RED, radius=0.16)
        fleches_pos = VGroup(*[
            Arrow(q_pos.get_center(), q_pos.get_center() + 1.0 * v, buff=0.2, color=YELLOW, stroke_width=2.5)
            for v in [RIGHT, UP, DOWN, RIGHT + UP * 0.6, RIGHT + DOWN * 0.6]
        ])
        label_pos = Text("Q > 0 : champ divergent", font_size=17).next_to(q_pos, DOWN, buff=1.3)
        groupe_pos = VGroup(q_pos, fleches_pos, label_pos)

        q_neg = Dot(RIGHT * 3.2, color=BLUE, radius=0.16)
        fleches_neg = VGroup(*[
            Arrow(q_neg.get_center() + 1.0 * v, q_neg.get_center(), buff=0.2, color=YELLOW, stroke_width=2.5)
            for v in [LEFT, UP, DOWN, LEFT + UP * 0.6, LEFT + DOWN * 0.6]
        ])
        label_neg = Text("Q < 0 : champ convergent", font_size=17).next_to(q_neg, DOWN, buff=1.3)
        groupe_neg = VGroup(q_neg, fleches_neg, label_neg)

        schemas = VGroup(groupe_pos, groupe_neg)
        schemas.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Direction et sens du champ : si Q est positive, le "
                "champ pointe radialement vers l'extérieur, on dit qu'il "
                "est divergent, ou centrifuge. Si Q est négative, le "
                "champ pointe au contraire vers la charge, il est "
                "convergent, ou centripète. Remarquons aussi que la norme "
                "du champ décroît très vite avec la distance, en un sur r "
                "au carré : elle est divisée par quatre quand la distance "
                "double."
            )
        ) as tracker:
            self.play(Create(groupe_pos))
            self.play(Create(groupe_neg))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schemas))

        # --- Théorème : principe de superposition -----------------------------------
        superposition = theorem_box(
            VGroup(
                Text("Principe de superposition", font_size=23, weight="BOLD"),
                MathTex(r"\vec{E}(M) = \sum_i \vec{E}_i(M) = \vec{E}_1(M) + \vec{E}_2(M) + \dots", font_size=27),
                Text("(car les forces électriques s'additionnent vectoriellement,", font_size=18),
                Text("et E = F/q, à q constante, pour chaque charge source).", font_size=18),
            ).arrange(DOWN, buff=0.22),
            box_width=11.8,
        )
        superposition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quand plusieurs charges créent chacune un champ au même "
                "point M, le champ résultant est la somme VECTORIELLE des "
                "champs créés par chacune : E de M égale la somme des E "
                "indice i de M. Cela se démontre simplement : la force "
                "totale subie par une charge test est la somme des forces "
                "dues à chaque charge source, et comme le champ vaut "
                "force divisée par q, cette somme se retrouve directement "
                "sur les champs."
            )
        ) as tracker:
            self.play(FadeIn(superposition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(superposition))

        # --- Exemple résolu 3 : champ résultant de deux charges --------------------
        a_pt = Dot(LEFT * 3.0, color=RED, radius=0.14)
        a_label = MathTex("q_A", font_size=22).next_to(a_pt, UP, buff=0.15)
        m_pt = Dot(LEFT * 1.0, color=YELLOW, radius=0.1)
        m_label = MathTex("M", font_size=22).next_to(m_pt, UP, buff=0.15)
        b_pt = Dot(RIGHT * 3.0, color=BLUE, radius=0.14)
        b_label = MathTex("q_B", font_size=22).next_to(b_pt, UP, buff=0.15)
        e_a = Arrow(m_pt.get_center(), m_pt.get_center() + RIGHT * 1.0, buff=0.1, color=GREEN, stroke_width=3)
        e_a_label = MathTex(r"\vec{E}_A", font_size=20, color=GREEN).next_to(e_a, DOWN, buff=0.1)
        e_b = Arrow(m_pt.get_center(), m_pt.get_center() + RIGHT * 0.8, buff=0.1, color="#DE7C1F", stroke_width=3)
        e_b.shift(DOWN * 0.35)
        e_b_label = MathTex(r"\vec{E}_B", font_size=20, color="#DE7C1F").next_to(e_b, DOWN, buff=0.1)
        am_label = MathTex("AM = 10\\ \\text{cm}", font_size=16).next_to(Line(a_pt.get_center(), m_pt.get_center()), DOWN, buff=0.55)
        mb_label = MathTex("MB = 20\\ \\text{cm}", font_size=16).next_to(Line(m_pt.get_center(), b_pt.get_center()), DOWN, buff=0.55)
        schema_ex = VGroup(a_pt, a_label, m_pt, m_label, b_pt, b_label, e_a, e_a_label, e_b, e_b_label, am_label, mb_label)
        schema_ex.next_to(titre, DOWN, buff=0.55)

        calculs = VGroup(
            Text("qA = +2 nC, qB = -6 nC, AB = d = 30 cm, AM = 10 cm, MB = 20 cm", font_size=17),
            MathTex(r"E_A = k\dfrac{|q_A|}{AM^2} = 1800\ \text{N/C}\ (\text{loin de A})", font_size=19),
            MathTex(r"E_B = k\dfrac{|q_B|}{MB^2} = 1350\ \text{N/C}\ (\text{vers B})", font_size=19),
            MathTex(r"\vec{E}_A \text{ et } \vec{E}_B \text{ de même sens} \Rightarrow E = E_A + E_B = 3150\ \text{N/C}", font_size=20, color=YELLOW),
        ).arrange(DOWN, buff=0.18)
        calculs.next_to(schema_ex, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu : sur une droite, qA vaut plus deux "
                "nanocoulombs, qB vaut moins six nanocoulombs, séparées "
                "de trente centimètres. Le point M est situé entre les "
                "deux, à dix centimètres de A, donc vingt centimètres de "
                "B. Le champ créé par qA en M vaut mille huit cents "
                "newtons par coulomb, dirigé en s'éloignant de A, donc "
                "vers B. Le champ créé par qB, négative, en M vaut mille "
                "trois cent cinquante newtons par coulomb, dirigé vers B "
                "puisque le champ d'une charge négative converge vers "
                "elle. Les deux vecteurs pointent donc dans le même sens : "
                "on additionne directement leurs normes, et le champ "
                "résultant vaut trois mille cent cinquante newtons par "
                "coulomb."
            )
        ) as tracker:
            self.play(Create(schema_ex))
            self.play(Write(calculs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_ex), FadeOut(calculs))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\vec{E}(M) = k\,\dfrac{Q}{r^2}\ \vec{u} \qquad \vec{E}(M) = \sum_i \vec{E}_i(M)", font_size=26),
                Text("Q > 0 : champ divergent. Q < 0 : champ convergent.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le champ créé par une charge "
                "ponctuelle Q vaut k fois Q sur r au carré, fois u, et le "
                "champ résultant de plusieurs charges est la somme "
                "vectorielle de chacun d'eux. Une charge positive crée un "
                "champ divergent, une charge négative crée un champ "
                "convergent."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• La superposition porte sur les VECTEURS, pas sur", font_size=20),
                Text("   les normes : n'additionner directement E1 et E2 que", font_size=20),
                Text("   s'ils ont la MÊME direction et le MÊME sens.", font_size=20),
                Text("• Sinon, il faut décomposer en coordonnées ou utiliser", font_size=20),
                Text("   une construction géométrique (parallélogramme).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à éviter : le principe de superposition porte sur "
                "des vecteurs, pas sur des normes. On ne peut additionner "
                "directement les intensités des champs que s'ils ont la "
                "même direction et le même sens ; sinon, il faut passer "
                "par une décomposition en coordonnées ou une construction "
                "géométrique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
