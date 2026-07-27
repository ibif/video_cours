"""
scenes/Physique_Condensateur_05.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 05.

§ 3c. Capacité d'un condensateur plan (qualitatif). Dépendance de la
surface S en regard (proportionnelle), de l'épaisseur e du diélectrique
(inversement proportionnelle), et de la nature du diélectrique
(permittivité). Théorème C=εS/e=ε₀ε_r S/e, avec ε₀≈8,85×10⁻¹² F/m.
Exemple résolu 3 : S=100 cm²=10⁻² m², e=0,1 mm=10⁻⁴ m → C≈885 pF (air),
puis avec ε_r=5 → C'≈4,4 nF.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 3c).
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
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _condensateur_plan(largeur: float = 1.6, ecart: float = 0.9, epaisseur_trait: float = 6):
    """Deux plaques planes en regard, avec repères S (surface) et e
    (écart), construit avec Line et Rectangle uniquement."""
    plaque_haut = Line(LEFT * largeur / 2, RIGHT * largeur / 2, stroke_width=epaisseur_trait, color=WHITE)
    plaque_haut.shift(UP * ecart / 2)
    plaque_bas = Line(LEFT * largeur / 2, RIGHT * largeur / 2, stroke_width=epaisseur_trait, color=WHITE)
    plaque_bas.shift(DOWN * ecart / 2)

    dielectrique = Rectangle(
        width=largeur, height=ecart * 0.92,
        fill_color="#3A3A3A", fill_opacity=0.55, stroke_width=0,
    )

    repere_S = Text("S", font_size=20, color=YELLOW).next_to(plaque_haut, UP, buff=0.15)
    repere_e = VGroup(
        Line(RIGHT * (largeur / 2 + 0.3) + UP * ecart / 2, RIGHT * (largeur / 2 + 0.3) + DOWN * ecart / 2, stroke_width=2, color=YELLOW),
    )
    repere_e_label = Text("e", font_size=20, color=YELLOW).next_to(repere_e, RIGHT, buff=0.1)

    return VGroup(dielectrique, plaque_haut, plaque_bas, repere_S, repere_e, repere_e_label)


class CapaciteCondensateurPlan(NotionScene):
    def construct(self):
        titre = scene_title("Capacité d'un condensateur plan")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "La capacité C dépend de la fabrication du condensateur. "
                "Pour un condensateur PLAN (deux plaques parallèles), de "
                "quels paramètres géométriques et physiques dépend-elle "
                "concrètement ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La capacité C dépend de la fabrication du condensateur. "
                "Pour un condensateur plan, formé de deux plaques "
                "parallèles, de quels paramètres géométriques et physiques "
                "dépend-elle concrètement ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : dépendances qualitatives ---------------------------
        schema = _condensateur_plan()
        schema.scale(1.3)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Considérons deux plaques planes en regard, de surface S, "
                "séparées par un diélectrique d'épaisseur e."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        dependances = VGroup(
            Text("• Plus la surface S en regard est grande, plus C est GRANDE", font_size=20),
            Text("   (C est proportionnelle à S).", font_size=20),
            Text("• Plus l'épaisseur e du diélectrique est petite, plus C est", font_size=20),
            Text("   GRANDE (C est inversement proportionnelle à e).", font_size=20),
            Text("• La nature du diélectrique (sa permittivité) influence aussi C.", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        dependances.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois paramètres influencent la capacité. Plus la surface "
                "S en regard des deux plaques est grande, plus la capacité "
                "est grande : C est proportionnelle à S. Plus l'épaisseur e "
                "du diélectrique est petite, c'est-à-dire plus les plaques "
                "sont rapprochées, plus la capacité est grande : C est "
                "inversement proportionnelle à e. Enfin, la nature du "
                "diélectrique, à travers sa permittivité, influence "
                "également la capacité."
            )
        ) as tracker:
            self.play(FadeIn(dependances))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(dependances))

        # --- Théorème : formule du condensateur plan ---------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Capacité d'un condensateur plan", font_size=22, weight="BOLD"),
                MathTex(r"C = \dfrac{\varepsilon S}{e} = \dfrac{\varepsilon_0 \varepsilon_r S}{e}", font_size=32),
                Text("S en m², e en m, C en farads (F).", font_size=19),
                MathTex(r"\varepsilon_0 \approx 8{,}85 \times 10^{-12}\ \text{F/m (permittivité du vide)}", font_size=21),
                Text("ε_r : permittivité relative du diélectrique (ε_r = 1 pour l'air).", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On démontre que la capacité d'un condensateur plan vaut C "
                "égale epsilon S sur e, ce qui s'écrit aussi epsilon zéro "
                "epsilon r S sur e, avec S en mètres carrés, e en mètres, "
                "et C en farads. Epsilon zéro, la permittivité du vide, "
                "vaut environ huit virgule quatre-vingt-cinq fois dix "
                "puissance moins douze farad par mètre. Epsilon r est la "
                "permittivité relative du diélectrique, égale à un pour "
                "l'air."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 3 ------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("S = 100 cm² = 10⁻² m², e = 0,1 mm = 10⁻⁴ m, diélectrique = AIR.", font_size=19),
                MathTex(r"C = \dfrac{\varepsilon_0 S}{e} = \dfrac{8{,}85\times10^{-12} \times 10^{-2}}{10^{-4}} \approx 885\ \text{pF}", font_size=23),
                Text("Avec un diélectrique de permittivité relative ε_r = 5 :", font_size=19),
                MathTex(r"C' = \varepsilon_r \, C \approx 5 \times 885\ \text{pF} \approx 4{,}4\ \text{nF}", font_size=25),
            ).arrange(DOWN, buff=0.22),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : une surface de cent centimètres carrés, "
                "soit dix puissance moins deux mètres carrés, séparée par "
                "zéro virgule un millimètre d'air, soit dix puissance moins "
                "quatre mètres. La capacité vaut epsilon zéro S sur e, "
                "environ huit cent quatre-vingt-cinq picofarads. Si l'on "
                "remplace l'air par un diélectrique de permittivité "
                "relative cinq, la capacité est multipliée par cinq et "
                "vaut environ quatre virgule quatre nanofarads."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"C = \dfrac{\varepsilon_0 \varepsilon_r S}{e}, \qquad \varepsilon_0 \approx 8{,}85\times10^{-12}\ \text{F/m}", font_size=26),
                Text("C croît avec S et avec ε_r ; C décroît quand e augmente.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : C égale epsilon zéro epsilon r S "
                "sur e, avec epsilon zéro environ huit virgule "
                "quatre-vingt-cinq fois dix puissance moins douze farad par "
                "mètre. La capacité croît avec la surface et avec la "
                "permittivité relative du diélectrique, et décroît quand "
                "l'épaisseur du diélectrique augmente."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Conversion cm² → m² : diviser par 10⁴, PAS par 10² —", font_size=20),
                Text("   100 cm² = 10⁻² m², pas 1 m².", font_size=20),
                Text("• Conversion mm → m : diviser par 10³ (0,1 mm = 10⁻⁴ m).", font_size=20),
                Text("• ε_r est un nombre SANS UNITÉ (≥ 1), à ne pas oublier.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Trois pièges fréquents. La conversion des centimètres "
                "carrés en mètres carrés se fait en divisant par dix "
                "puissance quatre, pas par cent : cent centimètres carrés "
                "égalent dix puissance moins deux mètres carrés, pas un "
                "mètre carré. La conversion des millimètres en mètres se "
                "fait en divisant par mille. Et epsilon r est un nombre "
                "sans unité, toujours supérieur ou égal à un, à ne jamais "
                "oublier dans la formule."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
