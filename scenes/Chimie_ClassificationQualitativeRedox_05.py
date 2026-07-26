"""
scenes/Chimie_ClassificationQualitativeRedox_05.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 05.

§ 2 (fin). Place du couple H₃O⁺/H₂ dans la classification : logique (les
métaux qui réduisent H₃O⁺ sont plus réducteurs que H₂, ceux qui ne le font
pas sont moins réducteurs que H₂), placement entre Pb²⁺/Pb et Cu²⁺/Cu,
tableau complet de la classification qualitative générale (de Au³⁺/Au en
haut à Mg²⁺/Mg en bas). Schéma de l'échelle verticale construit uniquement
avec des primitives Manim de base (Line, Arrow, MathTex, VGroup).
Source : 1ereC/Chimie.pdf, chapitre 10, page 97.
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
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


COUPLES_TEX = [
    r"Au^{3+}/Au",
    r"Ag^{+}/Ag",
    r"Cu^{2+}/Cu",
    r"H_3O^{+}/H_2",
    r"Pb^{2+}/Pb",
    r"Sn^{2+}/Sn",
    r"Ni^{2+}/Ni",
    r"Fe^{2+}/Fe",
    r"Zn^{2+}/Zn",
    r"Mg^{2+}/Mg",
]


def _schema_echelle():
    """Échelle verticale de la classification qualitative, construite
    uniquement avec des primitives Manim de base (Line, Arrow, MathTex,
    VGroup) — aucune bibliothèque externe."""

    labels = VGroup(*[MathTex(t, font_size=20, color=WHITE) for t in COUPLES_TEX])
    labels.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
    labels[3].set_color(YELLOW)  # met en évidence H3O+/H2

    ticks = VGroup()
    for lbl in labels:
        tick = Line(
            lbl.get_left() + LEFT * 0.55,
            lbl.get_left() + LEFT * 0.15,
            color=WHITE,
            stroke_width=2,
        )
        ticks.add(tick)
    ticks[3].set_color(YELLOW)

    axe = Line(ticks[0].get_start(), ticks[-1].get_start(), color=WHITE, stroke_width=2)

    milieu = axe.get_center()
    fleche_haut = Arrow(
        milieu + LEFT * 0.15, axe.get_start() + LEFT * 0.15,
        color="#DE7C1F", stroke_width=3, buff=0.1, max_tip_length_to_length_ratio=0.15,
    )
    texte_haut = Text("pouvoir oxydant\ncroissant", font_size=15, color="#DE7C1F", line_spacing=0.8)
    texte_haut.next_to(fleche_haut, LEFT, buff=0.15)

    fleche_bas = Arrow(
        milieu + LEFT * 0.15, axe.get_end() + LEFT * 0.15,
        color="#288073", stroke_width=3, buff=0.1, max_tip_length_to_length_ratio=0.15,
    )
    texte_bas = Text("pouvoir réducteur\ncroissant", font_size=15, color="#288073", line_spacing=0.8)
    texte_bas.next_to(fleche_bas, LEFT, buff=0.15)

    schema = VGroup(axe, ticks, labels, fleche_haut, texte_haut, fleche_bas, texte_bas)
    return schema


class PlaceCoupleH3OPlusH2(NotionScene):
    def construct(self):
        titre = scene_title("10.2 Place du couple H₃O⁺/H₂ dans la classification")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        intro = Text(
            _wrap(
                "Où placer exactement le couple H₃O⁺/H₂ parmi les métaux "
                "usuels ? La scène précédente donne déjà la réponse : il "
                "suffit d'en tirer la logique.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Où placer exactement le couple H-trois-O-plus sur H-deux "
                "parmi les métaux usuels ? La scène précédente donne déjà "
                "la réponse : il suffit d'en tirer la logique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : logique du placement -------------------------------
        logique = property_box(
            VGroup(
                Text(
                    "Zn et Fe réduisent H₃O⁺ (dégagent H₂) : ils sont plus",
                    font_size=21,
                ),
                Text("réducteurs que H₂ → placés SOUS le couple H₃O⁺/H₂.", font_size=21),
                Text(
                    "Cu ne réduit pas H₃O⁺ : il est moins réducteur que H₂",
                    font_size=21,
                ),
                Text("→ placé AU-DESSUS du couple H₃O⁺/H₂.", font_size=21),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.6,
        )
        logique.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le zinc et le fer réduisent les ions oxonium, puisqu'ils "
                "dégagent du dihydrogène en présence d'un acide : ils sont "
                "donc plus réducteurs que le dihydrogène, et se placent "
                "sous le couple H-trois-O-plus sur H-deux dans la "
                "classification. Le cuivre, au contraire, ne réduit pas les "
                "ions oxonium : il est moins réducteur que le dihydrogène, "
                "et se place au-dessus du couple H-trois-O-plus sur "
                "H-deux."
            )
        ) as tracker:
            self.play(FadeIn(logique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(logique))

        # --- Exemple traité : placement précis entre Cu et Pb ------------------
        placement = MathTex(
            r"Cu^{2+}/Cu \;>\; H_3O^{+}/H_2 \;>\; Pb^{2+}/Pb",
            font_size=28, color=YELLOW,
        )
        placement.next_to(titre, DOWN, buff=0.6)
        note_placement = Text(
            "(le plomb réduit H₃O⁺, mais moins bien que Zn ou Fe)",
            font_size=19, color=WHITE,
        )
        note_placement.next_to(placement, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Plus précisément, le couple H-trois-O-plus sur H-deux "
                "vient s'intercaler entre le couple cuivre deux plus sur "
                "cuivre, au-dessus, et le couple plomb deux plus sur plomb, "
                "en dessous : le plomb réduit bien les ions oxonium, mais "
                "moins facilement que le zinc ou le fer."
            )
        ) as tracker:
            self.play(Write(placement))
            self.play(FadeIn(note_placement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(placement), FadeOut(note_placement))

        # --- À retenir : l'échelle complète -------------------------------------
        entete_schema = Text("Classification qualitative générale", font_size=21, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.3)

        schema = _schema_echelle()
        schema.next_to(entete_schema, DOWN, buff=0.3)
        groupe = VGroup(entete_schema, schema)
        _fit(groupe, titre.get_bottom()[1] - 0.15)
        groupe.move_to(ORIGIN)
        groupe.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Voici la classification qualitative complète des couples "
                "usuels, du haut vers le bas : or, argent, cuivre, puis le "
                "couple H-trois-O-plus sur H-deux, puis plomb, étain, "
                "nickel, fer, zinc, et enfin magnésium tout en bas. Plus on "
                "descend, plus le réducteur est fort ; plus on monte, plus "
                "l'oxydant est fort. Cette échelle résume à elle seule tout "
                "ce que nous avons observé expérimentalement."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(Write(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas inverser le sens des deux flèches : le pouvoir "
                    "OXYDANT croît vers le HAUT de l'échelle (vers Au³⁺), le "
                    "pouvoir RÉDUCTEUR croît vers le BAS (vers Mg).",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : il ne faut pas inverser le "
                "sens des deux flèches de l'échelle. Le pouvoir oxydant "
                "croît vers le haut, en direction de l'or, tandis que le "
                "pouvoir réducteur croît vers le bas, en direction du "
                "magnésium."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
