"""
scenes/Physique_IntroductionOptiqueGeometrique_10.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 10.

§ 7. Synthèse : méthodes (résoudre un problème d'ombre, calculs avec la
célérité, distinguer ombre/pénombre, utiliser la réversibilité) et
récapitulatif des pièges à éviter du chapitre.
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, synthèse).
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
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesEtPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse : méthodes et pièges à éviter")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Nous avons vu les sources, les milieux, la propagation "
                "rectiligne, les ombres, les éclipses, la célérité et la "
                "réversibilité. Comment aborder efficacement un exercice "
                "qui combine plusieurs de ces notions ?",
                width=56,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Nous avons vu les sources de lumière, les milieux, la "
                "propagation rectiligne, les ombres, les éclipses, la "
                "célérité et la réversibilité. Comment aborder "
                "efficacement un exercice qui combine plusieurs de ces "
                "notions ? Récapitulons les méthodes essentielles."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : les quatre méthodes -----------------------------------
        methode_ombre = method_box(
            VGroup(
                Text("MÉTHODE — Résoudre un problème d'ombre :", font_size=19, weight="BOLD"),
                Text("1. Faire un schéma clair (source, objet, écran).", font_size=18),
                Text("2. Tracer les rayons tangents à l'objet opaque.", font_size=18),
                Text("3. Utiliser le théorème de Thalès / l'homothétie.", font_size=18),
                Text("4. Vérifier l'ordre de grandeur du résultat.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.4,
        )
        methode_ombre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première méthode, pour résoudre un problème d'ombre : "
                "faire un schéma clair avec la source, l'objet et "
                "l'écran ; tracer les rayons tangents à l'objet opaque ; "
                "utiliser le théorème de Thalès ou l'homothétie ; et "
                "toujours vérifier l'ordre de grandeur du résultat obtenu."
            )
        ) as tracker:
            self.play(FadeIn(methode_ombre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_ombre))

        methode_celerite = method_box(
            VGroup(
                Text("MÉTHODE — Calculs avec la célérité :", font_size=19, weight="BOLD"),
                Text("1. Convertir toutes les longueurs en mètres et toutes", font_size=18),
                Text("   les durées en secondes.", font_size=18),
                Text("2. En cas d'aller-retour, diviser la durée par 2.", font_size=18),
                MathTex(r"3.\ \ d = c \times \Delta t", font_size=22),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.4,
        )
        methode_celerite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode, pour les calculs avec la célérité : "
                "convertir toutes les longueurs en mètres et toutes les "
                "durées en secondes ; en cas d'aller-retour, diviser la "
                "durée par deux ; puis appliquer d égale c fois Δt."
            )
        ) as tracker:
            self.play(FadeIn(methode_celerite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_celerite))

        methode_ombre_penombre = method_box(
            VGroup(
                Text("MÉTHODE — Ombre ou pénombre ?", font_size=19, weight="BOLD"),
                Text("Se placer au point étudié et dénombrer les points de", font_size=18),
                Text("la source visibles depuis ce point :", font_size=18),
                Text("• Aucun point visible → ombre.", font_size=18),
                Text("• Une partie visible → pénombre.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.4,
        )
        methode_ombre_penombre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième méthode, pour distinguer ombre et pénombre : se "
                "placer par la pensée au point étudié et dénombrer les "
                "points de la source qui y sont visibles. Si aucun point "
                "de la source n'est visible, c'est l'ombre. Si une partie "
                "seulement est visible, c'est la pénombre."
            )
        ) as tracker:
            self.play(FadeIn(methode_ombre_penombre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_ombre_penombre))

        methode_reversibilite = method_box(
            VGroup(
                Text("MÉTHODE — Utiliser la réversibilité :", font_size=19, weight="BOLD"),
                Text("Pour une construction difficile dans un sens, tracer", font_size=18),
                Text("d'abord le trajet dans le sens le plus simple, puis", font_size=18),
                Text("l'utiliser tel quel dans l'autre sens.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.2,
        )
        methode_reversibilite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatrième méthode : pour une construction difficile dans "
                "un sens, on trace d'abord le trajet dans le sens le plus "
                "simple, puis on l'utilise tel quel dans l'autre sens, "
                "grâce au principe de réversibilité."
            )
        ) as tracker:
            self.play(FadeIn(methode_reversibilite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_reversibilite))

        # --- Exemple traité : application rapide de la méthode ombre --------------
        exemple = method_box(
            VGroup(
                Text("Application rapide : ombre d'un poteau au soleil.", font_size=19, weight="BOLD"),
                Text("1. Schéma : Soleil (source lointaine) → poteau → sol.", font_size=18),
                Text("2. Rayons du Soleil considérés parallèles (pas de S", font_size=18),
                Text("   unique à tracer, un seul angle d'incidence).", font_size=18),
                Text("3. Thalès : hauteur/ombre = constant pour tout objet", font_size=18),
                Text("   vertical au même instant.", font_size=18),
                Text("4. Ordre de grandeur : quelques mètres, cohérent.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Appliquons rapidement la méthode à l'ombre d'un poteau au "
                "soleil : on fait le schéma avec le Soleil, le poteau et "
                "le sol ; on considère les rayons du Soleil parallèles, "
                "avec un seul angle d'incidence ; on utilise Thalès, "
                "puisque le rapport hauteur sur ombre est constant pour "
                "tout objet vertical au même instant ; et l'on vérifie que "
                "le résultat, de l'ordre de quelques mètres, reste "
                "cohérent."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : synthèse du chapitre --------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir — synthèse du chapitre", font_size=22, weight="BOLD"),
                Text("Sources primaires/secondaires · milieux transparent/", font_size=17),
                Text("translucide/opaque · propagation rectiligne en milieu", font_size=17),
                Text("transparent et homogène · ombre (source ponctuelle) vs", font_size=17),
                Text("ombre/pénombre (source étendue) · éclipses (alignement", font_size=17),
                MathTex(r"\text{de 3 astres)} \quad c \approx 3{,}0 \times 10^{8}\ \text{m/s} \quad d = c\,\Delta t", font_size=19),
                Text("Principe de réversibilité du trajet lumineux.", font_size=17),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.4,
        )
        retenir.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Pour clore ce chapitre, résumons l'essentiel : les "
                "sources primaires et secondaires, les milieux "
                "transparent, translucide et opaque, la propagation "
                "rectiligne dans un milieu transparent et homogène, "
                "l'ombre avec une source ponctuelle contre l'ombre et la "
                "pénombre avec une source étendue, les éclipses comme "
                "alignement de trois astres, la célérité de la lumière "
                "avec la relation d égale c fois Δt, et enfin le principe "
                "de réversibilité du trajet lumineux."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter : récapitulatif ----------------------------------------
        pieges = warning_box(
            VGroup(
                Text("Pièges classiques à ne plus jamais commettre :", font_size=19, weight="BOLD"),
                Text("• Oublier de diviser par 2 dans un calcul d'aller-retour.", font_size=18),
                Text("• Confondre source primaire et source secondaire", font_size=18),
                Text("   (se demander : l'objet PRODUIT-il sa lumière ?).", font_size=18),
                Text("• Dire que la lumière se propage \"toujours\" en ligne", font_size=18),
                Text("   droite, sans préciser milieu transparent ET homogène.", font_size=18),
                Text("• Confondre ombre totale et pénombre.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.4,
        )
        pieges.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Pour finir, les pièges classiques à ne plus jamais "
                "commettre : oublier de diviser par deux dans un calcul "
                "d'aller-retour ; confondre source primaire et source "
                "secondaire, en se demandant toujours si l'objet produit "
                "sa propre lumière ; affirmer que la lumière se propage "
                "toujours en ligne droite, sans préciser que le milieu "
                "doit être transparent et homogène ; et enfin confondre "
                "ombre totale et pénombre."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
