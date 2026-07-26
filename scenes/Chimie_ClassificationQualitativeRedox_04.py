"""
scenes/Chimie_ClassificationQualitativeRedox_04.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 04.

§ 2 (suite). Action des acides sur les métaux : expériences (Zn et Fe
plongés dans HCl dilué → dégagement de H₂ reconnu par détonation à la
flamme, réaction exothermique ; Cu dans HCl → rien), demi-équation
2H₃O⁺ + 2e⁻ → H₂ + 2H₂O, équations bilans pour Zn et Fe. Remarque : l'acide
nitrique fait exception et attaque le cuivre (via les ions NO₃⁻, pas via
H₃O⁺).
Source : 1ereC/Chimie.pdf, chapitre 10, pages 96-97.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
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
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ActionAcidesSurMetaux(NotionScene):
    def construct(self):
        titre = scene_title("10.2 Action des acides sur les métaux")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : expériences -------------------------------------------
        intro = Text(
            _wrap(
                "Les ions oxonium H₃O⁺, présents dans tout acide, forment "
                "eux aussi un couple oxydant/réducteur. Voyons comment ce "
                "couple se situe par rapport aux métaux usuels.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les ions oxonium H-trois-O-plus, présents dans tout acide, "
                "forment eux aussi un couple oxydant réducteur. Voyons "
                "comment ce couple se situe par rapport aux métaux usuels, "
                "en étudiant l'action des acides sur le zinc, le fer et le "
                "cuivre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : observations expérimentales -----------------------
        entete_obs = Text("Expériences avec l'acide chlorhydrique dilué", font_size=21, color=YELLOW, weight="BOLD")
        entete_obs.next_to(titre, DOWN, buff=0.35)

        obs = _bullets(
            [
                "Zn + HCl dilué : dégagement gazeux abondant, détonation "
                "caractéristique à l'approche d'une flamme (test de H₂), "
                "réaction exothermique.",
                "Fe + HCl dilué : même observation, dégagement de H₂, "
                "réaction exothermique.",
                "Cu + HCl dilué : aucun changement, aucun gaz.",
            ],
            font_size=21, width=54,
        )
        obs.next_to(entete_obs, DOWN, buff=0.35)
        groupe_obs = VGroup(entete_obs, obs)
        _fit(groupe_obs, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "On plonge séparément du zinc, du fer et du cuivre dans de "
                "l'acide chlorhydrique dilué. Avec le zinc : un dégagement "
                "gazeux abondant se produit, et ce gaz détone "
                "caractéristiquement à l'approche d'une flamme, ce qui "
                "identifie le dihydrogène ; la réaction est exothermique. "
                "Avec le fer : on observe exactement le même phénomène. "
                "Avec le cuivre, en revanche : aucun changement, aucun "
                "dégagement gazeux."
            )
        ) as tracker:
            self.play(FadeIn(entete_obs))
            self.play(FadeIn(obs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_obs))

        # --- Exemple traité : interprétation par demi-équations ---------------
        entete_eq = Text("Interprétation : le couple H₃O⁺/H₂", font_size=21, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.35)

        demi_h = MathTex(r"2H_3O^{+} + 2e^{-} \longrightarrow H_2 + 2H_2O", font_size=27, color=WHITE)
        bilan_zn = MathTex(r"Zn + 2H_3O^{+} \longrightarrow Zn^{2+} + H_2 + 2H_2O", font_size=26, color=ORANGE)
        bilan_fe = MathTex(r"Fe + 2H_3O^{+} \longrightarrow Fe^{2+} + H_2 + 2H_2O", font_size=26, color=ORANGE)

        equations = VGroup(demi_h, bilan_zn, bilan_fe).arrange(DOWN, buff=0.35)
        equations.next_to(entete_eq, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les ions oxonium sont réduits en dihydrogène selon la "
                "demi-équation : deux H-trois-O-plus, plus deux électrons, "
                "donne H-deux, plus deux H-deux-O. Le zinc et le fer, plus "
                "réducteurs que le dihydrogène, cèdent leurs électrons aux "
                "ions oxonium. On obtient les équations bilans : zinc, plus "
                "deux H-trois-O-plus, donne zinc deux plus, plus "
                "H-deux, plus deux H-deux-O ; et de même pour le fer. Le "
                "cuivre, lui, ne réagit pas : il est moins réducteur que le "
                "dihydrogène."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(demi_h))
            self.play(Write(bilan_zn))
            self.play(Write(bilan_fe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(equations))

        # --- À retenir --------------------------------------------------------
        retenir = property_box(
            VGroup(
                Text(
                    "Un métal plus réducteur que H₂ réagit avec un acide (HCl,",
                    font_size=21,
                ),
                Text(
                    "H₂SO₄ dilué...) en dégageant du dihydrogène.",
                    font_size=21,
                ),
                Text(
                    "Cu, Ag, Au, moins réducteurs que H₂, ne réagissent pas.",
                    font_size=21, weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=12.4,
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : un métal plus réducteur que le "
                "dihydrogène réagit avec un acide comme l'acide "
                "chlorhydrique ou l'acide sulfurique dilué, en dégageant du "
                "dihydrogène. Le cuivre, l'argent et l'or, moins réducteurs "
                "que le dihydrogène, ne réagissent pas avec ces acides."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter : l'acide nitrique fait exception ------------------
        piege = warning_box(
            VGroup(
                Text(
                    "L'acide nitrique HNO₃ fait exception : il attaque le cuivre",
                    font_size=20,
                ),
                Text(
                    "(et l'argent), mais pas grâce à H₃O⁺ — c'est l'ion NO₃⁻",
                    font_size=20,
                ),
                Text(
                    "qui joue ici le rôle d'oxydant. Ne pas généraliser à tous",
                    font_size=20,
                ),
                Text("les acides !", font_size=20, weight="BOLD"),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.6,
        )
        piege.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Attention à un piège classique : l'acide nitrique, H-N-O-3, "
                "fait exception. Il attaque le cuivre, et même l'argent, "
                "mais ce n'est pas grâce aux ions oxonium : ce sont les ions "
                "nitrate, N-O-3 moins, qui jouent ici le rôle d'oxydant, "
                "selon un mécanisme différent. Il ne faut donc jamais "
                "généraliser le comportement d'un acide à tous les autres "
                "acides."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
