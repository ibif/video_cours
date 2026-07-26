"""
scenes/Chimie_OxydoreductionVoieSeche_05.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 05.

§ 3. Variation du n.o. au cours d'une réaction : élément dont le n.o.
augmente = oxydé = réducteur ; élément dont le n.o. diminue = réduit =
oxydant. Conservation des électrons. Échelle des n.o. pour 2Mg + O₂ →
2MgO. Exemple résolu 3 : analyse de CuO + H₂ → Cu + H₂O par les n.o.,
avec vérification de la conservation des électrons.
Source : 1ereC/Chimie.pdf, chapitre 13, pages 128-129.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _echelle_no(label, no_avant, no_apres, couleur):
    """Petite échelle verticale schématisant la variation du n.o. d'un
    élément, construite avec des primitives Manim de base (Line, Arrow,
    Text, VGroup) — aucune bibliothèque externe."""
    axe = Line(UP * 0.9, DOWN * 0.9, color=WHITE, stroke_width=2)
    tick_avant = Line(LEFT * 0.12, RIGHT * 0.12, color=WHITE, stroke_width=2)
    tick_avant.move_to(axe.point_from_proportion(1 - (no_avant + 4) / 8))
    tick_apres = Line(LEFT * 0.12, RIGHT * 0.12, color=couleur, stroke_width=2)
    tick_apres.move_to(axe.point_from_proportion(1 - (no_apres + 4) / 8))

    label_avant = Text(f"{label} : {no_avant:+d}".replace("+0", "0"), font_size=17, color=WHITE)
    label_avant.next_to(tick_avant, LEFT, buff=0.15)
    label_apres = Text(f"{label} : {no_apres:+d}".replace("+0", "0"), font_size=17, color=couleur)
    label_apres.next_to(tick_apres, LEFT, buff=0.15)

    fleche = Arrow(tick_avant.get_center(), tick_apres.get_center(), color=couleur, buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.35)
    fleche.shift(RIGHT * 0.5)

    return VGroup(axe, tick_avant, tick_apres, label_avant, label_apres, fleche)


class VariationNoAuCoursReaction(NotionScene):
    def construct(self):
        titre = scene_title("13.3 Variation du n.o. au cours d'une réaction")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : théorème de la variation du n.o. ----------------------
        theoreme = theorem_box(
            VGroup(
                Text("Au cours d'une réaction d'oxydoréduction :", font_size=22, weight="BOLD"),
                Text("• le n.o. d'un élément qui AUGMENTE : il est OXYDÉ,", font_size=21),
                Text("  c'est un RÉDUCTEUR (il cède des électrons) ;", font_size=21),
                Text("• le n.o. d'un élément qui DIMINUE : il est RÉDUIT,", font_size=21),
                Text("  c'est un OXYDANT (il capte des électrons).", font_size=21),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le nombre d'oxydation permet de repérer directement "
                "l'oxydant et le réducteur, sans même écrire de "
                "demi-équation. Au cours d'une réaction d'oxydoréduction : "
                "l'élément dont le n.o. augmente est oxydé, c'est un "
                "réducteur, puisqu'il a cédé des électrons. L'élément dont "
                "le n.o. diminue est réduit, c'est un oxydant, puisqu'il a "
                "capté des électrons."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : conservation des électrons + échelle Mg/O2 -----
        propriete = property_box(
            Text(
                _wrap(
                    "CONSERVATION DES ÉLECTRONS : le nombre total "
                    "d'électrons cédés par le(s) réducteur(s) est "
                    "toujours égal au nombre total d'électrons captés par "
                    "le(s) oxydant(s), en tenant compte des coefficients "
                    "stœchiométriques.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une propriété fondamentale accompagne toujours cette "
                "règle : la conservation des électrons. Le nombre total "
                "d'électrons cédés par le ou les réducteurs est toujours "
                "égal au nombre total d'électrons captés par le ou les "
                "oxydants, en tenant compte des coefficients "
                "stœchiométriques de l'équation."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        entete_ech = Text("Illustration : 2 Mg + O₂ → 2 MgO", font_size=22, color=YELLOW, weight="BOLD")
        entete_ech.next_to(titre, DOWN, buff=0.35)

        echelle_mg = _echelle_no("Mg", 0, 2, ORANGE)
        echelle_o = _echelle_no("O", 0, -2, "#288073")
        echelles = VGroup(echelle_mg, echelle_o).arrange(RIGHT, buff=1.8)
        echelles.next_to(entete_ech, DOWN, buff=0.45)
        groupe_ech = VGroup(entete_ech, echelles)
        _fit(groupe_ech, titre.get_bottom()[1] - 0.15)
        groupe_ech.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Reprenons la combustion du magnésium : deux Mg, plus O "
                "deux, donne deux MgO. Le n.o. du magnésium passe de zéro, "
                "dans le métal, à plus deux, dans MgO : il augmente, le "
                "magnésium est donc oxydé, c'est le réducteur. Le n.o. de "
                "l'oxygène passe de zéro, dans O deux, à moins deux, dans "
                "MgO : il diminue, l'oxygène est donc réduit, c'est "
                "l'oxydant."
            )
        ) as tracker:
            self.play(FadeIn(entete_ech))
            self.play(FadeIn(echelles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_ech))

        # --- Exemple traité : CuO + H2 -> Cu + H2O -------------------------
        bilan = MathTex(r"CuO + H_2 \longrightarrow Cu + H_2O", font_size=30)
        analyse1 = Text("Cu : +II (dans CuO) → 0 (dans Cu)  n.o. DIMINUE → RÉDUIT → oxydant", font_size=18)
        analyse2 = Text("H : 0 (dans H₂) → +I (dans H₂O)  n.o. AUGMENTE → OXYDÉ → réducteur", font_size=18)
        analyse3 = Text("O : −II → −II  (inchangé, simple spectateur ici)", font_size=18)
        verif1 = Text("Cu gagne 2 e⁻ (de +2 à 0) : 2 e⁻ captés", font_size=18)
        verif2 = Text("2 atomes H perdent chacun 1 e⁻ (de 0 à +1) : 2 e⁻ cédés", font_size=18)
        verif3 = MathTex(r"2\,e^-\ \text{cédés} = 2\,e^-\ \text{captés} \checkmark", font_size=22, color=ORANGE)

        contenu = VGroup(bilan, analyse1, analyse2, analyse3, verif1, verif2, verif3).arrange(DOWN, buff=0.22)
        boite = example_box(contenu, box_width=13.0)
        boite.next_to(titre, DOWN, buff=0.3)
        _fit(boite, titre.get_bottom()[1] - 0.1)

        with self.voiceover(
            text=(
                "Exemple résolu : analysons la réduction de l'oxyde de "
                "cuivre par le dihydrogène, CuO plus H deux, donne Cu plus "
                "H deux O, à l'aide des nombres d'oxydation. Le cuivre "
                "passe de plus deux, dans CuO, à zéro, dans Cu : son n.o. "
                "diminue, il est donc réduit, c'est l'oxydant. "
                "L'hydrogène passe de zéro, dans H deux, à plus un, dans "
                "l'eau : son n.o. augmente, il est donc oxydé, c'est le "
                "réducteur. L'oxygène, lui, reste à moins deux : il ne "
                "participe pas à l'échange d'électrons. Vérifions la "
                "conservation : le cuivre gagne deux électrons, et les "
                "deux atomes d'hydrogène en perdent chacun un, soit deux "
                "électrons cédés en tout. Deux électrons cédés égale deux "
                "électrons captés : c'est cohérent."
            )
        ) as tracker:
            self.play(FadeIn(boite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(boite))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas inverser le vocabulaire : n.o. qui AUGMENTE "
                    "= élément OXYDÉ = RÉDUCTEUR (et non l'inverse). "
                    "n.o. qui DIMINUE = élément RÉDUIT = OXYDANT.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : il ne faut pas inverser "
                "le vocabulaire. Un n.o. qui augmente correspond à un "
                "élément oxydé, qui joue le rôle de réducteur, et non "
                "l'inverse. Un n.o. qui diminue correspond à un élément "
                "réduit, qui joue le rôle d'oxydant."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
