"""
scenes/Physique_ChampElectrostatique_10.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 10.

§ Synthèse : pièges à éviter. Récapitulatif transversal du chapitre :
piège des conversions d'unités (µC, nC en C ; cm en m), piège du sens de
F⃗=qE⃗ pour une charge négative, piège d'additionner les normes au lieu
des vecteurs (principe de superposition), astuce de comparer
systématiquement force électrique et poids dans les exercices sur les
particules. Clôt le chapitre par un résumé des formules essentielles.
Source : 1ereC/Physique.pdf, pages 54-65 (synthèse de chapitre).
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
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SynthesePiegesChampElectrostatique(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse du chapitre — pièges à éviter")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : introduction de la synthèse -----------------------------------
        mise_en_situation = Text(
            _wrap(
                "Nous avons parcouru tout le chapitre sur le champ "
                "électrostatique. Revenons sur les quatre erreurs les "
                "plus fréquentes commises dans les exercices, et sur une "
                "astuce à retenir.",
                width=54,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons parcouru tout le chapitre sur le champ "
                "électrostatique. Revenons maintenant sur les quatre "
                "erreurs les plus fréquentes commises dans les exercices, "
                "et sur une astuce essentielle à retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Piège 1 : conversions d'unités -----------------------------------------
        piege1 = warning_box(
            VGroup(
                Text("Piège 1 — Conversions d'unités", font_size=21, weight="BOLD"),
                Text("Convertir TOUJOURS µC, nC, pC en C, et cm en m,", font_size=19),
                Text("AVANT tout calcul.", font_size=19),
                MathTex(r"\text{Une distance oubliée en cm fausse } F \text{ ou } E \text{ d'un facteur } 10^4 !", font_size=20, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=12.0,
        )
        piege1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier piège : les conversions d'unités. Il faut "
                "toujours convertir les microcoulombs, nanocoulombs et "
                "picocoulombs en coulombs, et les centimètres en mètres, "
                "avant tout calcul. Une distance oubliée en centimètres "
                "fausse la force ou le champ d'un facteur dix mille, "
                "puisque ces grandeurs varient en un sur d au carré."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        # --- Piège 2 : sens de F = qE pour une charge négative -----------------------
        e_vec = Arrow(LEFT * 2.5, RIGHT * 0.3, buff=0.1, color=YELLOW, stroke_width=3)
        e_label = MathTex(r"\vec{E}", font_size=24, color=YELLOW).next_to(e_vec, UP, buff=0.1)
        q_neg = Dot(LEFT * 1.0, color=BLUE, radius=0.12)
        q_label = MathTex("q<0", font_size=20).next_to(q_neg, DOWN, buff=0.2)
        f_vec = Arrow(q_neg.get_center(), q_neg.get_center() + LEFT * 1.4, buff=0.15, color=RED, stroke_width=3)
        f_label = MathTex(r"\vec{F}", font_size=24, color=RED).next_to(f_vec, UP, buff=0.1)
        schema2 = VGroup(e_vec, e_label, q_neg, q_label, f_vec, f_label)
        schema2.move_to(DOWN * 0.2)

        piege2_texte = VGroup(
            Text("Piège 2 — Sens de F⃗ = qE⃗ pour q < 0", font_size=21, weight="BOLD"),
            Text("Pour une charge NÉGATIVE, F⃗ est en sens OPPOSÉ à E⃗,", font_size=19),
            Text("jamais dans le même sens.", font_size=19),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        piege2_texte.next_to(titre, DOWN, buff=0.4)
        schema2.next_to(piege2_texte, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième piège : le sens de la force F égale q E pour "
                "une charge négative. Beaucoup d'élèves dessinent, par "
                "réflexe, la force dans le même sens que le champ, quel "
                "que soit le signe de la charge. C'est faux : pour une "
                "charge négative, la force est en sens opposé au champ."
            )
        ) as tracker:
            self.play(Write(piege2_texte))
            self.play(Create(schema2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2_texte), FadeOut(schema2))

        # --- Piège 3 : additionner les normes au lieu des vecteurs -------------------
        piege3 = warning_box(
            VGroup(
                Text("Piège 3 — Additionner les normes au lieu des vecteurs", font_size=20, weight="BOLD"),
                Text("Le principe de superposition porte sur des VECTEURS :", font_size=19),
                MathTex(r"E = E_1 + E_2 \ \text{ SEULEMENT si } \vec{E}_1 \text{ et } \vec{E}_2 \text{ ont même direction ET même sens.}", font_size=18),
                Text("Sinon : décomposition en coordonnées, ou construction géométrique.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.6,
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège : additionner les normes au lieu des "
                "vecteurs. Le principe de superposition porte sur des "
                "vecteurs : on ne peut écrire que le champ résultant est "
                "la somme des normes E un plus E deux que si ces deux "
                "vecteurs ont exactement la même direction et le même "
                "sens. Dans tous les autres cas, il faut décomposer en "
                "coordonnées, ou utiliser une construction géométrique."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- Astuce : comparer force électrique et poids ------------------------------
        astuce = example_box(
            VGroup(
                Text("Astuce — comparer force électrique et poids", font_size=21, weight="BOLD"),
                Text("Dans un exercice sur une particule élémentaire", font_size=19),
                Text("(électron, proton…), calculer systématiquement", font_size=19),
                MathTex(r"\dfrac{F_{\text{élec}}}{P} = \dfrac{|q|E}{mg}", font_size=24),
                Text("Ce rapport est presque toujours énorme (>10¹⁰) :", font_size=19),
                Text("le poids peut être négligé sans hésiter.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        astuce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une astuce, enfin, à toujours avoir en tête dans les "
                "exercices portant sur une particule élémentaire, comme "
                "un électron ou un proton : calculer systématiquement le "
                "rapport de la force électrique sur le poids, F élec sur "
                "P égale valeur absolue de q, fois E, divisé par m g. Ce "
                "rapport est presque toujours énorme, largement supérieur "
                "à dix puissance dix, ce qui permet de négliger le poids "
                "sans hésiter."
            )
        ) as tracker:
            self.play(FadeIn(astuce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(astuce))

        # --- À retenir : résumé de tout le chapitre -----------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir — tout le chapitre en un coup d'œil", font_size=23, weight="BOLD"),
                MathTex(r"F = k\dfrac{|q_A q_B|}{d^2} \qquad \vec{E}(M) = \dfrac{\vec{F}}{q} \qquad \vec{E}(M) = k\dfrac{Q}{r^2}\vec{u}", font_size=21),
                MathTex(r"\vec{E}(M) = \textstyle\sum_i \vec{E}_i(M) \qquad E = \dfrac{U}{d} \qquad \vec{F} = q\,\vec{E}", font_size=21),
                Text("Même signe repousse, signes contraires attirent.", font_size=19),
            ).arrange(DOWN, buff=0.24),
            box_width=13.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, retenons l'ensemble de ses "
                "formules essentielles : la loi de Coulomb, F égale k "
                "fois la valeur absolue de qA qB sur d carré ; la "
                "définition du champ, E de M égale F sur q ; le champ "
                "d'une charge ponctuelle, k Q sur r carré fois u ; le "
                "principe de superposition ; le champ uniforme, E égale U "
                "sur d ; et la force subie par une charge, F égale q E. "
                "Et toujours cette règle fondamentale : même signe "
                "repousse, signes contraires attirent."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
