"""
scenes/Chimie_AlcenesAlcynes_12.py — Chapitre 3 (1ereC, Chimie), scène 12.

Réactions d'addition sur les alcynes : hydrogénation totale (Ni/Pt → alcane)
ou partielle (Pd → alcène), action des dihalogènes (excès de Br2 → dérivé
tétrahalogéné), action de HCl (dichloroalcane gem-dihalogéné), hydratation
de l'acétylène (catalyseur Hg2+/H2SO4 → éthanal), et préparation au
laboratoire (carbure de calcium CaC2 + eau → acétylène + Ca(OH)2).
Source : 1ereC/Chimie.pdf, chapitre 3, page 33.
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
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class AdditionSurAlcynes(NotionScene):
    def construct(self):
        titre = scene_title("12. Réactions d'addition sur les alcynes")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : deux additions successives possibles ------------------------
        intro = Text(
            _wrap(
                "Un alcyne possède DEUX liaisons π à faire réagir : il "
                "peut donc additionner un réactif en deux étapes "
                "successives, ce qui n'existait pas pour les alcènes.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un alcyne possède une triple liaison, c'est-à-dire deux "
                "liaisons pi à faire réagir. Il peut donc additionner un "
                "réactif en deux étapes successives, ce qui n'existait "
                "pas pour les alcènes, limités à une seule addition."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : hydrogénation totale/partielle ----------
        entete1 = Text("Hydrogénation : totale ou partielle", font_size=23, color=YELLOW, weight="BOLD")
        entete1.next_to(titre, DOWN, buff=0.35)

        hydro = VGroup(
            MathTex(
                r"HC \equiv CH + 2H_2 \xrightarrow{Ni \text{ ou } Pt} CH_3-CH_3",
                font_size=25,
            ),
            Text("hydrogénation totale → alcane", font_size=18),
            MathTex(
                r"HC \equiv CH + H_2 \xrightarrow{Pd} CH_2=CH_2",
                font_size=25,
            ),
            Text("hydrogénation partielle (catalyseur Pd) → alcène", font_size=18),
        ).arrange(DOWN, buff=0.28)
        hydro.next_to(entete1, DOWN, buff=0.4)

        groupe1 = VGroup(entete1, hydro)
        _fit(groupe1, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Avec du nickel ou du platine, et un excès de "
                "dihydrogène, l'acétylène est totalement hydrogéné : il "
                "additionne deux molécules de dihydrogène et donne "
                "directement l'éthane, un alcane. Mais avec un "
                "catalyseur particulier, le palladium, on peut arrêter "
                "la réaction après une seule addition : on parle "
                "d'hydrogénation partielle, qui s'arrête au stade de "
                "l'alcène, ici l'éthylène."
            )
        ) as tracker:
            self.play(FadeIn(entete1))
            self.play(FadeIn(hydro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        # --- Exemple traité : dihalogènes en excès et HCl -------------------------
        entete2 = Text("Dihalogènes en excès et gaz chlorhydrique", font_size=21, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        eqs = VGroup(
            MathTex(
                r"HC \equiv CH + 2Br_2 \text{ (excès)} \longrightarrow CHBr_2-CHBr_2",
                font_size=23,
            ),
            Text("dérivé tétrahalogéné", font_size=17),
            MathTex(
                r"HC \equiv CH + HCl \longrightarrow CH_2=CHCl",
                font_size=23,
            ),
            MathTex(
                r"CH_2=CHCl + HCl \longrightarrow CH_3-CHCl_2",
                font_size=23,
            ),
            Text("dichloroalcane gem-dihalogéné (2 Cl sur le même C)", font_size=17),
        ).arrange(DOWN, buff=0.25)
        eqs.next_to(entete2, DOWN, buff=0.4)

        groupe2 = VGroup(entete2, eqs)
        _fit(groupe2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Avec un excès de dibrome, les deux additions "
                "successives ont lieu, et l'on obtient un dérivé "
                "tétrahalogéné, portant quatre atomes de brome. Avec le "
                "chlorure d'hydrogène, deux additions successives "
                "donnent finalement un dichloroalcane particulier, dit "
                "gem-dihalogéné, car les deux atomes de chlore se "
                "retrouvent fixés sur le même atome de carbone, et non "
                "sur deux carbones voisins."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(eqs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir : hydratation de l'acétylène → éthanal ----------------------
        retenir = definition_box(
            VGroup(
                Text("Hydratation de l'acétylène (catalyseur Hg²⁺ / H₂SO₄) :", font_size=20, weight="BOLD"),
                MathTex(
                    r"HC \equiv CH + H_2O \xrightarrow{Hg^{2+}/H_2SO_4} CH_3-CHO",
                    font_size=26,
                ),
                Text("éthanal (un aldéhyde), et non un alcool !", font_size=19, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.35)
        _fit(retenir, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Retenons un cas particulier important : l'hydratation "
                "de l'acétylène, catalysée par des ions mercure deux "
                "plus en présence d'acide sulfurique, ne donne pas "
                "directement un alcool stable, mais un composé "
                "intermédiaire instable qui se réarrange aussitôt en "
                "éthanal, c'est-à-dire un aldéhyde."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter : préparation au laboratoire (CaC2 + eau) -----------
        piege = warning_box(
            VGroup(
                Text(
                    _wrap(
                        "Préparation au laboratoire de l'acétylène : le "
                        "carbure de calcium réagit avec l'eau.",
                        width=44,
                    ),
                    font_size=20,
                ),
                MathTex(
                    r"CaC_2 + 2H_2O \longrightarrow C_2H_2 + Ca(OH)_2",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        piege.next_to(titre, DOWN, buff=0.35)
        _fit(piege, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Un dernier point à retenir, souvent source d'erreur : "
                "au laboratoire, l'acétylène ne se prépare pas par "
                "combustion, mais par une réaction bien différente entre "
                "le carbure de calcium et l'eau, qui donne de "
                "l'acétylène et de l'hydroxyde de calcium. Ne confondez "
                "pas cette réaction de préparation avec les réactions "
                "d'addition étudiées juste avant."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
