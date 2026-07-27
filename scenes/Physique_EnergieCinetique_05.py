"""
scenes/Physique_EnergieCinetique_05.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 05.

§ Interprétation des conséquences du théorème de l'énergie cinétique (somme
des travaux positive/négative/nulle → mouvement accéléré/retardé/uniforme ;
ΔEc indépendant du référentiel et du chemin suivi) et exemple résolu complet
(automobile en descente, moteur coupé, frottements).
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, § 5, partie 1).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, essentiel_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class InterpretationExempleAutomobile(NotionScene):
    def construct(self):
        titre = scene_title("Interprétation et exemple : automobile en descente")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé : trois cas possibles pour la somme des travaux --------------
        interpretation = property_box(
            VGroup(
                Text("Interprétation du signe de ΣW", font_size=22, weight="BOLD"),
                Text("• ΣW(F_ext) > 0  →  mouvement ACCÉLÉRÉ (Ec augmente)", font_size=20),
                Text("• ΣW(F_ext) < 0  →  mouvement RETARDÉ (Ec diminue)", font_size=20),
                Text("• ΣW(F_ext) = 0  →  mouvement UNIFORME (Ec constante)", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.4,
        )
        interpretation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le théorème de l'énergie cinétique se lit aussi comme un "
                "critère sur le mouvement. Si la somme des travaux des "
                "forces extérieures est positive, l'énergie cinétique "
                "augmente : le mouvement est accéléré. Si elle est "
                "négative, l'énergie cinétique diminue : le mouvement est "
                "retardé. Si elle est nulle, l'énergie cinétique reste "
                "constante : le mouvement est uniforme."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interpretation))

        # --- Raisonnement : ΔEc ne dépend ni du référentiel ni du chemin ---------
        propriete = property_box(
            VGroup(
                Text("Propriété importante", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "ΔEc entre deux états A et B ne dépend QUE de ces deux "
                        "états et des travaux des forces : ni du référentiel "
                        "d'étude, ni du chemin réellement suivi entre A et B.",
                        width=52,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        propriete.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Une propriété importante : la variation d'énergie "
                "cinétique entre deux états A et B ne dépend que de ces "
                "deux états et des travaux des forces appliquées, jamais "
                "du référentiel d'étude ni du chemin réellement suivi "
                "entre A et B."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple résolu : automobile en descente, moteur coupé ---------------
        enonce_ex = Text(
            _wrap(
                "Une automobile de masse m = 800 kg descend une pente de "
                "2 %, moteur coupé, sur AB = 200 m. Les frottements "
                "s'opposent au mouvement avec f = 150 N. En A, "
                "v_A = 36 km/h = 10 m/s. Quelle est la vitesse en B ?",
                width=56,
            ),
            font_size=21,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.4)

        # schéma pente
        a_pt = UP * 0.7 + LEFT * 3.3
        b_pt = DOWN * 0.9 + RIGHT * 2.7
        pente = Line(a_pt, b_pt, color=WHITE, stroke_width=3)
        sol_h = Line(a_pt + DOWN * 0.02, a_pt + RIGHT * 6.0 + DOWN * 0.02, color="#595959", stroke_width=1)
        voiture = Polygon(
            b_pt + LEFT * 0.35 + UP * 0.05,
            b_pt + RIGHT * 0.35 + UP * 0.05,
            b_pt + RIGHT * 0.25 + UP * 0.35,
            b_pt + LEFT * 0.25 + UP * 0.35,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.6, stroke_width=2,
        )
        label_a = MathTex("A", font_size=24).next_to(a_pt, UP, buff=0.1)
        label_b = MathTex("B", font_size=24).next_to(b_pt, DOWN, buff=0.35)
        f_arrow = Arrow(b_pt + UP * 0.2, b_pt + UP * 0.2 + LEFT * 0.9, color="#B42E41", buff=0)
        f_label = MathTex("f", font_size=22, color="#B42E41").next_to(f_arrow, UP, buff=0.05)
        schema = VGroup(sol_h, pente, voiture, label_a, label_b, f_arrow, f_label)
        schema.scale(0.75)
        schema.next_to(enonce_ex, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu complet : une automobile de masse huit "
                "cents kilogrammes descend une pente de deux pour cent, "
                "moteur coupé, sur une distance A-B de deux cents mètres. "
                "Les frottements s'opposent au mouvement avec une force f "
                "de cent cinquante newtons. En A, la vitesse vaut "
                "trente-six kilomètres par heure, soit dix mètres par "
                "seconde. Quelle est la vitesse en B ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.play(Create(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex), FadeOut(schema))

        # --- Résolution --------------------------------------------------------------
        resolution = example_box(
            VGroup(
                MathTex(r"h = AB \times 0{,}02 = 200\times 0{,}02 = 4\ \text{m}", font_size=22),
                MathTex(r"W(\vec{P}) = mgh = 800\times 9{,}8\times 4 = 31\,360\ \text{J}", font_size=22),
                MathTex(r"W(\vec{f}) = -f\times AB = -150\times 200 = -30\,000\ \text{J}", font_size=22),
                MathTex(r"\Sigma W = 31\,360 - 30\,000 = 2\,000\ \text{J}", font_size=22),
                MathTex(r"v_B = \sqrt{v_A^2 + \dfrac{2\Sigma W}{m}} = \sqrt{10^2 + \dfrac{2\times 2000}{800}} \approx 10{,}25\ \text{m/s}", font_size=22, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
            box_width=12.6,
        )
        resolution.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résolvons. La hauteur de descente h vaut la distance A-B "
                "fois la pente, soit deux cents fois zéro virgule zéro "
                "deux, quatre mètres. Le travail du poids vaut m g h, soit "
                "trente et un mille trois cent soixante joules, positif "
                "car le véhicule descend. Le travail des frottements vaut "
                "moins f fois A-B, soit moins trente mille joules. La "
                "somme des travaux vaut donc deux mille joules, positive : "
                "le mouvement est accéléré. Le théorème de l'énergie "
                "cinétique donne alors v B égale racine carrée de v A "
                "carré plus deux fois la somme des travaux sur m, ce qui "
                "donne environ dix virgule vingt-cinq mètres par seconde."
            )
        ) as tracker:
            self.play(FadeIn(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "ΣW > 0 → accéléré, ΣW < 0 → retardé, ΣW = 0 → "
                        "uniforme. ΔEc ne dépend que des états A et B et des "
                        "travaux, jamais du référentiel ni du chemin suivi.",
                        width=56,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le signe de la somme des travaux "
                "indique directement la nature du mouvement, accéléré, "
                "retardé ou uniforme, et la variation d'énergie cinétique "
                "ne dépend que des états de départ et d'arrivée et des "
                "travaux des forces, jamais du référentiel ni du chemin "
                "suivi."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
