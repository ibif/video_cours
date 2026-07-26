"""
scenes/Chimie_AlcenesAlcynes_13.py — Chapitre 3 (1ereC, Chimie), scène 13.

Polymérisation d'addition (monomère, polymère, motif, degré de
polymérisation n=M/M0), exemples polyéthylène (PE), PVC, polystyrène (PS)
avec équations et usages, importance industrielle (vapocraquage, SIR).
Puis synthèse du chapitre : method_box ×2 (nommer un alcène/alcyne,
appliquer Markovnikov) et warning_box ×4 (pièges à éviter), et essentiel_box
récapitulatif final. Source : 1ereC/Chimie.pdf, chapitre 3, page 34.
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
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class PolymerisationEtSynthese(NotionScene):
    def construct(self):
        titre = scene_title("13. Polymérisation d'addition et synthèse")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : de la molécule au matériau ------------------------------------
        intro = Text(
            _wrap(
                "La double liaison C=C d'un alcène peut aussi s'ouvrir "
                "pour enchaîner des milliers de molécules identiques bout "
                "à bout : c'est la polymérisation d'addition, à l'origine "
                "des plastiques.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La double liaison carbone-carbone d'un alcène peut "
                "aussi s'ouvrir pour enchaîner des milliers de molécules "
                "identiques bout à bout : c'est la polymérisation "
                "d'addition, à l'origine de la plupart des matières "
                "plastiques qui nous entourent."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : vocabulaire de la polymérisation --------
        definition = definition_box(
            VGroup(
                Text("monomère : petite molécule de départ (alcène)", font_size=19),
                Text("polymère : longue chaîne formée par répétition", font_size=19),
                Text("motif : unité qui se répète dans le polymère", font_size=19),
                MathTex(r"\text{degré de polymérisation : } n = \dfrac{M}{M_0}", font_size=26),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=11.0,
        )
        definition.next_to(titre, DOWN, buff=0.35)
        _fit(definition, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Quatre mots de vocabulaire à maîtriser. Le monomère est "
                "la petite molécule de départ, ici un alcène. Le "
                "polymère est la longue chaîne formée par la répétition "
                "de ce monomère. Le motif est l'unité qui se répète dans "
                "le polymère. Et le degré de polymérisation, noté n, "
                "s'obtient en divisant la masse molaire M du polymère par "
                "la masse molaire M zéro du motif."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : PE, PVC, PS -------------------------------------------
        entete = Text("Trois polymères industriels", font_size=22, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.3)

        polymeres = VGroup(
            VGroup(
                MathTex(r"n\,CH_2=CH_2 \longrightarrow -(CH_2-CH_2)_n-", font_size=22),
                Text("polyéthylène (PE) — sacs, bidons, tuyaux", font_size=16),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                MathTex(r"n\,CH_2=CHCl \longrightarrow -(CH_2-CHCl)_n-", font_size=22),
                Text("PVC — tuyaux, câbles, revêtements de sol", font_size=16),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                MathTex(r"n\,CH_2=CH-C_6H_5 \longrightarrow -(CH_2-CH(C_6H_5))_n-", font_size=20),
                Text("polystyrène (PS) — emballages, isolation", font_size=16),
            ).arrange(DOWN, buff=0.12),
        ).arrange(DOWN, buff=0.28)
        polymeres.next_to(entete, DOWN, buff=0.35)

        groupe = VGroup(entete, polymeres)
        _fit(groupe, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Trois exemples industriels majeurs. L'éthylène "
                "polymérise pour donner le polyéthylène, utilisé pour "
                "les sacs plastiques, les bidons et les tuyaux. Le "
                "chlorure de vinyle polymérise pour donner le PVC, "
                "utilisé pour les tuyaux, les câbles électriques et les "
                "revêtements de sol. Le styrène polymérise pour donner "
                "le polystyrène, utilisé pour les emballages et "
                "l'isolation thermique."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(polymeres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Importance industrielle : vapocraquage, SIR ----------------------------
        industrie = Text(
            _wrap(
                "Les monomères (éthylène, propène...) sont eux-mêmes "
                "produits par vapocraquage du pétrole ou du gaz naturel, "
                "comme à la SIR (Société Ivoirienne de Raffinage) : la "
                "pétrochimie relie directement le raffinage à l'industrie "
                "du plastique.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        industrie.next_to(titre, DOWN, buff=0.4)
        _fit(industrie, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Ces monomères, comme l'éthylène ou le propène, sont "
                "eux-mêmes produits à grande échelle par vapocraquage du "
                "pétrole ou du gaz naturel, notamment à la Société "
                "Ivoirienne de Raffinage. La pétrochimie relie ainsi "
                "directement le raffinage du pétrole brut à l'industrie "
                "des matières plastiques."
            )
        ) as tracker:
            self.play(FadeIn(industrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(industrie))

        # --- À retenir : les deux méthodes clés du chapitre --------------------------
        entete_m = Text("Les deux méthodes clés du chapitre", font_size=22, color=YELLOW, weight="BOLD")
        entete_m.next_to(titre, DOWN, buff=0.3)

        methode1 = method_box(
            VGroup(
                Text("Nommer un alcène/alcyne :", font_size=17, weight="BOLD"),
                Text("1. Chaîne principale avec la double/triple liaison", font_size=15),
                Text("2. Suffixe -ène/-yne, indice le plus petit", font_size=15),
                Text("3. Numéroter en priorité sur l'insaturation", font_size=15),
                Text("4. Ramifications par ordre alphabétique", font_size=15),
            ).arrange(DOWN, buff=0.13, aligned_edge=LEFT),
            box_width=5.4,
        )
        methode2 = method_box(
            VGroup(
                Text("Appliquer Markovnikov :", font_size=17, weight="BOLD"),
                Text("1. Repérer les 2 C de la double liaison", font_size=15),
                Text("2. Compter les H sur chaque carbone", font_size=15),
                Text("3. H (de HX/H2O) va sur le C le plus", font_size=15),
                Text("   hydrogéné ; X/OH sur l'autre", font_size=15),
            ).arrange(DOWN, buff=0.13, aligned_edge=LEFT),
            box_width=5.4,
        )
        methodes = VGroup(methode1, methode2).arrange(RIGHT, buff=0.5)
        methodes.next_to(entete_m, DOWN, buff=0.35)
        _fit(methodes, entete_m.get_bottom()[1] - 0.35)

        groupe_m = VGroup(entete_m, methodes)

        with self.voiceover(
            text=(
                "Avant de conclure, rappelons les deux méthodes clés du "
                "chapitre. Pour nommer un alcène ou un alcyne : repérer "
                "la chaîne principale contenant l'insaturation, choisir "
                "le suffixe avec l'indice le plus petit, numéroter en "
                "priorité sur la double ou triple liaison, puis placer "
                "les ramifications par ordre alphabétique. Pour "
                "appliquer la règle de Markovnikov : repérer les deux "
                "carbones de la double liaison, compter leurs "
                "hydrogènes, et faire aller l'hydrogène du réactif vers "
                "le carbone le plus hydrogéné."
            )
        ) as tracker:
            self.play(FadeIn(entete_m))
            self.play(FadeIn(methode1))
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_m))

        # --- Pièges à éviter : les 4 pièges du chapitre ------------------------------
        entete_p = Text("Les 4 pièges à éviter absolument", font_size=22, color=YELLOW, weight="BOLD")
        entete_p.next_to(titre, DOWN, buff=0.3)

        pieges = warning_box(
            VGroup(
                Text("1. Confondre substitution (alcanes) et addition", font_size=17),
                Text("   (alcènes/alcynes) — mécanismes différents.", font_size=17),
                Text("2. Le test à l'eau de brome NE distingue PAS", font_size=17),
                Text("   un alcène d'un alcyne (les deux décolorent).", font_size=17),
                Text("3. Attribuer Z/E sans vérifier que chaque C de", font_size=17),
                Text("   la double liaison porte 2 groupes différents.", font_size=17),
                Text("4. Mal numéroter : la priorité va TOUJOURS à", font_size=17),
                Text("   l'insaturation, pas aux ramifications.", font_size=17),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=11.0,
        )
        pieges.next_to(entete_p, DOWN, buff=0.35)
        _fit(VGroup(entete_p, pieges), titre.get_bottom()[1] - 0.3)

        groupe_p = VGroup(entete_p, pieges)

        with self.voiceover(
            text=(
                "Récapitulons les quatre pièges à éviter absolument. "
                "Un : ne pas confondre la substitution, propre aux "
                "alcanes, avec l'addition, propre aux alcènes et "
                "alcynes — ce sont deux mécanismes différents. Deux : le "
                "test à l'eau de brome ne distingue jamais un alcène "
                "d'un alcyne, puisque les deux le décolorent de la même "
                "façon. Trois : ne jamais attribuer une étiquette Z ou E "
                "sans vérifier que chaque carbone de la double liaison "
                "porte bien deux groupes différents. Quatre : lors de la "
                "numérotation, la priorité revient toujours à "
                "l'insaturation, jamais aux ramifications."
            )
        ) as tracker:
            self.play(FadeIn(entete_p))
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_p))

        # --- L'essentiel à retenir : récapitulatif final du chapitre ---------------
        essentiel = essentiel_box(
            VGroup(
                Text("Alcènes CₙH₂ₙ (C=C) et alcynes CₙH₂ₙ₋₂ (C≡C) :", font_size=19, weight="BOLD"),
                Text("hydrocarbures insaturés, nommés par -ène / -yne.", font_size=18),
                Text("Réactions d'addition (H₂, X₂, HX, H₂O) suivant", font_size=18),
                Text("la règle de Markovnikov ; eau de brome = test", font_size=18),
                Text("d'insaturation. La polymérisation d'addition des", font_size=18),
                Text("alcènes fabrique les plastiques (PE, PVC, PS).", font_size=18),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
            box_width=11.5,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)
        _fit(essentiel, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, retenons l'essentiel. Les "
                "alcènes, de formule C indice n H indice deux n avec une "
                "double liaison, et les alcynes, de formule C indice n H "
                "indice deux n moins deux avec une triple liaison, sont "
                "des hydrocarbures insaturés, nommés respectivement par "
                "les suffixes ène et yne. Ils subissent des réactions "
                "d'addition avec le dihydrogène, les dihalogènes, les "
                "halogénures d'hydrogène et l'eau, en suivant la règle "
                "de Markovnikov ; l'eau de brome sert de test de "
                "l'insaturation. Enfin, la polymérisation d'addition des "
                "alcènes est à la base de la fabrication industrielle des "
                "plastiques, comme le polyéthylène, le PVC et le "
                "polystyrène."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
