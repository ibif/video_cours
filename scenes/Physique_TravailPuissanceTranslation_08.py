"""
scenes/Physique_TravailPuissanceTranslation_08.py — Chapitre 1 « Travail et
puissance dans le cas d'un mouvement de translation » (1ereC, Physique),
scène 08 (synthèse).

§ Tableau récapitulatif des formules du chapitre (travail d'une force
constante, travail du poids, travail des frottements, puissance moyenne,
puissance instantanée, conversion kWh, rendement) ; méthodes (calculer le
travail d'une force, exploiter le travail du poids, calculer une
puissance, calculer un rendement) ; pièges à éviter, notamment l'angle α
sur un plan incliné (le poids fait un angle 90°±β avec le déplacement, pas
β).
Source : 1ereC/Physique.pdf, chapitre 1, pages 4-12.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    YELLOW,
    Arc,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Square,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


POIDS_COLOR = "#1E5FA8"


class SyntheseTravailPuissance(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse — Travail et puissance en translation")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : récapitulons -----------------------------------------------------
        intro = Text(
            _wrap(
                "Ce chapitre a couvert le travail d'une force constante, "
                "les cas particuliers du poids et du frottement, la "
                "puissance, et le rendement. Faisons le point.",
                width=56,
            ),
            font_size=23,
        )
        intro.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Ce chapitre a couvert le travail d'une force constante, "
                "les cas particuliers du travail du poids et du travail "
                "des frottements, la puissance d'une force, et enfin le "
                "rendement d'une machine. Faisons le point sur l'ensemble "
                "des formules et des méthodes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : tableau récapitulatif -----------------------------------
        formules = VGroup(
            MathTex(r"W_{AB}(\vec{F}) = F\times AB\times\cos(\alpha)", font_size=22),
            MathTex(r"W_{AB}(\vec{P}) = \pm\,mgh", font_size=22),
            MathTex(r"W(\vec{f}) = -f\times\ell", font_size=22),
            MathTex(r"P_m = \dfrac{W}{\Delta t} \qquad P = \vec{F}\cdot\vec{v} = F\,v\,\cos(\alpha)", font_size=22),
            MathTex(r"1\ kWh = 3{,}6\times10^{6}\ J", font_size=22),
            MathTex(r"r = \dfrac{P_u}{P_t} = \dfrac{W_u}{W_t}", font_size=22),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        recap = essentiel_box(formules, box_width=10.5)
        recap.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici les six formules à connaître par cœur. Le travail "
                "d'une force constante, F fois A-B fois cosinus de alpha. "
                "Le travail du poids, plus ou moins m g h. Le travail des "
                "frottements, moins f fois ℓ. La puissance moyenne, W sur "
                "delta t, et la puissance instantanée, F vecteur scalaire v "
                "vecteur. La conversion du kilowattheure, trois virgule six "
                "millions de joules. Et enfin le rendement, P-u sur P-t."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Méthodes ---------------------------------------------------------------------
        methodes = VGroup(
            Text("1. Travail d'une force : bilan des forces, mesurer l'angle α", font_size=21),
            Text("   RÉEL entre F⃗ et AB⃗, appliquer la formule, conclure sur", font_size=21),
            Text("   la nature (moteur/résistant/nul).", font_size=21),
            Text("2. Travail du poids : identifier la dénivellation h, fixer le", font_size=21),
            Text("   signe selon montée (−) ou descente (+).", font_size=21),
            Text("3. Puissance : convertir vitesse (m/s) et durée (s), puis", font_size=21),
            Text("   appliquer P=W/Δt ou P=F⃗·v⃗ selon les données.", font_size=21),
            Text("4. Rendement : identifier Pu et Pt (ou Wu et Wt), calculer", font_size=21),
            Text("   r=Pu/Pt, vérifier 0<r≤1.", font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        methode_recap = method_box(methodes, box_width=12.3)
        methode_recap.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Quatre méthodes à mobiliser selon la situation. Pour le "
                "travail d'une force, faire le bilan des forces, mesurer "
                "l'angle réel entre la force et le déplacement, appliquer "
                "la formule, puis conclure sur la nature du travail. Pour "
                "le travail du poids, identifier la dénivellation et fixer "
                "le signe selon que l'objet monte ou descend. Pour la "
                "puissance, toujours convertir vitesse et durée dans les "
                "bonnes unités avant de calculer. Pour le rendement, bien "
                "identifier ce qui est utile et ce qui est total, puis "
                "vérifier que le résultat reste entre zéro et un."
            )
        ) as tracker:
            self.play(FadeIn(methode_recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_recap))

        # --- Exemple traité : piège de l'angle sur un plan incliné -----------------------
        base = Line(LEFT * 2.5, RIGHT * 2.0, color="#FFFFFF")
        plan = Line(base.get_start(), base.get_start() + [3.5, 1.8, 0], color="#FFFFFF")
        arc_beta = Arc(radius=0.9, start_angle=0, angle=0.47, color=YELLOW, stroke_width=2)
        arc_beta.shift(base.get_start())
        label_beta = MathTex(r"\beta", font_size=24, color=YELLOW).move_to(base.get_start() + [1.15, 0.28, 0])

        milieu_plan = (plan.get_start() + plan.get_end()) / 2
        objet = Square(side_length=0.35, color="#FFFFFF", fill_color="#3A3A3A", fill_opacity=1)
        objet.move_to(milieu_plan)
        deplacement = Vector([1.0, 0.51, 0], color="#288073")
        deplacement.move_to(objet.get_center() + [0.55, 0.28, 0])
        poids = Vector(DOWN * 1.0, color=POIDS_COLOR)
        poids.move_to(objet.get_center() + DOWN * 0.6)
        label_poids = MathTex(r"\vec{P}", font_size=22, color=POIDS_COLOR).next_to(poids, RIGHT, buff=0.1)
        label_angle_reel = MathTex(r"90°{+}\beta", font_size=18, color="#B42E41")
        label_angle_reel.next_to(objet, DOWN + RIGHT, buff=0.35)

        schema_plan = VGroup(
            base, plan, arc_beta, label_beta, objet, deplacement, poids,
            label_poids, label_angle_reel,
        )
        schema_plan.scale(0.85).move_to(ORIGIN).shift(DOWN * 0.2 + LEFT * 0.5)

        note_plan = Text(
            _wrap(
                "Sur un plan incliné d'angle β, l'angle entre le poids P⃗ "
                "et le déplacement AB⃗ (le long de la pente) vaut 90°+β en "
                "descente — jamais β lui-même.",
                width=42,
            ),
            font_size=20,
        )
        note_plan.to_edge(RIGHT, buff=0.3)

        with self.voiceover(
            text=(
                "Prenons un exemple qui illustre le piège le plus fréquent "
                "du chapitre : un objet sur un plan incliné d'angle bêta "
                "par rapport à l'horizontale. Le déplacement se fait le "
                "long de la pente, mais le poids, lui, reste toujours "
                "vertical. L'angle réel entre le poids et le déplacement "
                "n'est donc pas bêta, mais quatre-vingt-dix degrés plus "
                "bêta : c'est cet angle-là qu'il faut utiliser dans la "
                "formule du travail, jamais l'angle de la pente lui-même."
            )
        ) as tracker:
            self.play(FadeIn(schema_plan), FadeIn(note_plan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_plan), FadeOut(note_plan))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Un chapitre, quatre grandeurs : travail (J), puissance "
                    "(W), énergie (kWh), rendement (sans unité, 0 à 1). "
                    "Toujours identifier la NATURE du travail avant son "
                    "signe.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir pour tout le chapitre : quatre grandeurs "
                "principales, le travail en joules, la puissance en watts, "
                "l'énergie en kilowattheures, et le rendement, sans unité, "
                "toujours compris entre zéro et un. Dans chaque exercice, "
                "identifiez d'abord la nature du travail, moteur, "
                "résistant ou nul, avant même de vous soucier de son signe "
                "précis."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter (récapitulatif complet) --------------------------------------
        piege = warning_box(
            VGroup(
                Text("• α se mesure entre F⃗ et AB⃗, pas forcément l'horizontale.", font_size=19),
                Text("• Sur un plan incliné, le poids fait un angle 90°±β avec", font_size=19),
                Text("  le déplacement, jamais β lui-même.", font_size=19),
                Text("• Convertir vitesses en m/s et durées en s avant tout calcul.", font_size=19),
                Text("• Ne pas confondre kWh (énergie) et kW (puissance).", font_size=19),
                Text("• Le signe du travail est une question de NATURE, pas de", font_size=19),
                Text("  grandeur ; le travail total est la somme algébrique de tous", font_size=19),
                Text("  les travaux (ne pas oublier les forces à travail nul).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.5,
        )
        piege.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Récapitulons tous les pièges du chapitre. L'angle alpha se "
                "mesure toujours entre la force et le déplacement, pas "
                "forcément par rapport à l'horizontale. Sur un plan "
                "incliné, le poids fait un angle de quatre-vingt-dix "
                "degrés plus ou moins bêta avec le déplacement, jamais "
                "bêta lui-même. Convertissez systématiquement les vitesses "
                "en mètres par seconde et les durées en secondes. Ne "
                "confondez jamais le kilowattheure, une énergie, avec le "
                "kilowatt, une puissance. Et rappelez-vous que le signe du "
                "travail traduit sa nature, moteur ou résistant, que le "
                "travail total est la somme algébrique de tous les "
                "travaux, et qu'il ne faut jamais oublier les forces dont "
                "le travail est nul, comme la réaction normale "
                "perpendiculaire au déplacement."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
