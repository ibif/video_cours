"""
scenes/Physique_TravailPuissanceRotation_07.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 07.

§ Théorème des moments (équilibre d'un solide mobile autour d'un axe
fixe) : ΣℳΔ(F⃗ext) = 0 (+ ΣF⃗ext = 0⃗), justification, remarque (moment nul
de la réaction de l'axe), méthode de résolution en 6 étapes. Exemple
résolu 6 : balançoire (Awa 30 kg à 1,5 m, Konan 40 kg).
Source : 1ereC/Physique.pdf, chapitre 2, pages 13-23.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class TheoremeDesMoments(NotionScene):
    def construct(self):
        titre = scene_title("Théorème des moments : équilibre en rotation")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : balançoire ------------------------------------------------
        enonce = Text(
            _wrap(
                "Sur une balançoire, Awa et Konan, de poids différents, "
                "peuvent-ils s'équilibrer ? À quelle condition ?",
                width=54,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sur une balançoire à bascule, deux enfants de poids "
                "différents peuvent s'équilibrer, à condition de bien "
                "choisir leur position. C'est exactement le rôle du "
                "théorème des moments."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : théorème + justification -----------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Théorème des moments (équilibre)", font_size=22, weight="BOLD"),
                MathTex(r"\sum \mathcal{M}_\Delta(\vec{F}_{ext}) = 0 \qquad \text{(et } \sum \vec{F}_{ext} = \vec{0}\text{)}", font_size=27),
                Text(
                    "Les effets de rotation des forces se compensent exactement : le solide reste immobile.",
                    font_size=20,
                ),
                Text("Remarque : la réaction de l'axe passe par l'axe ⟹ son moment est nul.", font_size=20),
            ).arrange(DOWN, buff=0.24),
            box_width=11.0,
        )
        theoreme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le théorème des moments énonce que, à l'équilibre, la "
                "somme algébrique des moments de toutes les forces "
                "extérieures, par rapport à l'axe, est nulle — et la "
                "résultante de ces forces l'est aussi. Autrement dit, les "
                "effets de rotation de chaque force se compensent "
                "exactement, si bien que le solide reste immobile. À "
                "noter : la réaction de l'axe lui-même passe toujours par "
                "l'axe, donc son moment est toujours nul — elle "
                "n'intervient jamais dans cette somme."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Méthode de résolution en 6 étapes ------------------------------------
        methode = method_box(
            VGroup(
                Text("Méthode — appliquer le théorème des moments", font_size=21, weight="BOLD"),
                Text("1. Faire le bilan des forces extérieures appliquées au solide.", font_size=18),
                Text("2. Choisir un sens positif de rotation.", font_size=18),
                Text("3. Calculer le bras de levier de chaque force.", font_size=18),
                Text("4. Affecter le signe de chaque moment selon son sens.", font_size=18),
                Text("5. Écrire ΣℳΔ(F⃗ext) = 0.", font_size=18),
                Text("6. Résoudre l'équation pour l'inconnue cherchée.", font_size=18),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=9.6,
        )
        methode.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour appliquer ce théorème, on suit toujours la même "
                "méthode en six étapes : d'abord, faire le bilan complet "
                "des forces extérieures appliquées au solide. Ensuite, "
                "choisir un sens positif de rotation. Puis calculer le "
                "bras de levier de chaque force. Affecter ensuite le "
                "signe de chaque moment selon son sens réel. Écrire alors "
                "que la somme des moments est nulle. Et enfin, résoudre "
                "l'équation obtenue pour trouver l'inconnue cherchée."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Schéma balançoire -----------------------------------------------------
        planche = Line(LEFT * 3.2 + DOWN * 0.5, RIGHT * 3.2 + DOWN * 0.5, color=WHITE, stroke_width=6)
        triangle = VGroup(
            Line(DOWN * 0.5, DOWN * 1.5 + LEFT * 0.5, color="#595959", stroke_width=5),
            Line(DOWN * 0.5, DOWN * 1.5 + RIGHT * 0.5, color="#595959", stroke_width=5),
        )
        o_pt = _dot_label(DOWN * 0.5, "O", label_dir=DOWN, dot_color="#288073")
        a_pt = LEFT * 1.5 + DOWN * 0.5
        b_pt = RIGHT * 2.25 + DOWN * 0.5
        awa = Circle(radius=0.3, color="#B42E41", fill_color="#B42E41", fill_opacity=1).move_to(a_pt + UP * 0.35)
        konan = Circle(radius=0.35, color="#1E5FA8", fill_color="#1E5FA8", fill_opacity=1).move_to(b_pt + UP * 0.4)
        pa = Vector(DOWN * 0.9, color="#B42E41").shift(a_pt)
        pb = Vector(DOWN * 1.1, color="#1E5FA8").shift(b_pt)
        a_lbl = MathTex("A", font_size=24).next_to(a_pt, DOWN, buff=0.9)
        b_lbl = MathTex("B", font_size=24).next_to(b_pt, DOWN, buff=1.1)
        schema = VGroup(triangle, planche, o_pt, awa, konan, pa, pb, a_lbl, b_lbl)
        schema.scale(0.85).move_to(DOWN * 0.8)

        with self.voiceover(
            text=(
                "Sur la balançoire, le pivot O est l'axe de rotation. Awa "
                "est assise en A, à gauche, Konan en B, à droite. Leurs "
                "poids respectifs créent chacun un moment par rapport à "
                "l'axe O — de sens opposés, puisqu'ils sont de part et "
                "d'autre du pivot."
            )
        ) as tracker:
            self.play(Create(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple résolu 6 : Awa et Konan ---------------------------------------
        exemple = example_box(
            VGroup(
                Text("Exemple 6 — balançoire : Awa (30 kg) assise à OA = 1,5 m, Konan (40 kg) en B :", font_size=18),
                MathTex(r"\text{Sens positif : rotation due au poids d'Awa} \quad \Rightarrow\ \sum \mathcal{M}_\Delta = 0", font_size=20),
                MathTex(r"m_A g \times OA - m_B g \times OB = 0", font_size=24),
                MathTex(r"OB = \dfrac{m_A \times OA}{m_B} = \dfrac{30 \times 1{,}5}{40} = 1{,}125\ \text{m}", font_size=25),
            ).arrange(DOWN, buff=0.26),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : Awa, trente kilogrammes, est assise à un "
                "mètre cinquante du pivot. Konan pèse quarante "
                "kilogrammes. On choisit comme sens positif le sens de "
                "rotation dû au poids d'Awa. Le théorème des moments "
                "donne : m indice A, g, fois O A, moins m indice B, g, "
                "fois O B, égale zéro. On en déduit O B égale m indice A "
                "fois O A, sur m indice B, soit trente fois un virgule "
                "cinq, sur quarante, c'est-à-dire un virgule cent "
                "vingt-cinq mètre. C'est à cette distance que Konan doit "
                "s'asseoir pour équilibrer la balançoire."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "À l'équilibre : ΣℳΔ(F⃗ext) = 0. La réaction de l'axe a "
                    "un moment nul, donc n'intervient jamais dans cette "
                    "somme.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : à l'équilibre, la somme des moments des "
                "forces extérieures par rapport à l'axe est nulle. La "
                "réaction de l'axe, elle, a toujours un moment nul, donc "
                "n'intervient jamais dans cette somme."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : oublier qu'à l'équilibre il faut AUSSI "
                    "ΣF⃗ext = 0⃗ (translation) — le théorème des moments "
                    "seul ne garantit pas l'absence de déplacement global "
                    "de l'axe."
                ),
                font_size=21,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : le théorème des moments assure "
                "l'équilibre en rotation, mais il faut aussi vérifier que "
                "la résultante des forces extérieures est nulle, pour "
                "garantir l'équilibre complet du solide, y compris en "
                "translation."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
