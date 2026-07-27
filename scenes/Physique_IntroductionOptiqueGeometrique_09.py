"""
scenes/Physique_IntroductionOptiqueGeometrique_09.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 09.

§ 6. Principe de réversibilité de la lumière : le trajet suivi par la
lumière est indépendant du sens de parcours. Exemple résolu 5 : Awa voit
l'œil de Konan à travers une fente F — Konan peut-il voir l'œil d'Awa ?
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 6).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    GREEN,
    WHITE,
    YELLOW,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _schema_awa_konan(sens: str) -> VGroup:
    """Un mur percé d'une fente F entre Awa (gauche) et Konan (droite) ;
    `sens` = "awa_vers_konan" ou "konan_vers_awa" pour le sens du rayon
    tracé (le trajet géométrique — donc la fente traversée — est
    identique dans les deux cas, seul le sens de la flèche change)."""
    mur = Rectangle(width=0.25, height=2.4, color=WHITE, fill_color=WHITE, fill_opacity=0.85)
    mur.move_to(0 * RIGHT)

    fente = Rectangle(width=0.25, height=0.18, color=YELLOW, fill_color=YELLOW, fill_opacity=1.0)
    fente.move_to(mur.get_center())
    label_F = Text("F", font_size=16, color=YELLOW).next_to(fente, UP, buff=0.12)

    oeil_awa = Ellipse(width=0.5, height=0.3, color=WHITE).move_to(LEFT * 3.4)
    pupille_awa = Dot(oeil_awa.get_center(), color=WHITE, radius=0.05)
    label_awa = Text("Awa", font_size=16, color=WHITE).next_to(oeil_awa, DOWN, buff=0.15)

    oeil_konan = Ellipse(width=0.5, height=0.3, color=WHITE).move_to(RIGHT * 3.4)
    pupille_konan = Dot(oeil_konan.get_center(), color=WHITE, radius=0.05)
    label_konan = Text("Konan", font_size=16, color=WHITE).next_to(oeil_konan, DOWN, buff=0.15)

    if sens == "awa_vers_konan":
        rayon1 = Line(oeil_konan.get_center(), fente.get_center(), color=GREEN, stroke_width=2.5)
        rayon2 = Line(fente.get_center(), oeil_awa.get_center(), color=GREEN, stroke_width=2.5)
    else:
        rayon1 = Line(oeil_awa.get_center(), fente.get_center(), color=GREEN, stroke_width=2.5)
        rayon2 = Line(fente.get_center(), oeil_konan.get_center(), color=GREEN, stroke_width=2.5)

    return VGroup(
        oeil_awa, pupille_awa, label_awa,
        mur, fente, label_F,
        oeil_konan, pupille_konan, label_konan,
        rayon1, rayon2,
    )


class PrincipeDeReversibilite(NotionScene):
    def construct(self):
        titre = scene_title("Principe de réversibilité de la lumière")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Awa regarde l'œil de Konan à travers une petite fente "
                "dans un mur. Si Konan regarde à son tour par cette même "
                "fente, verra-t-il l'œil d'Awa ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Awa regarde l'œil de Konan à travers une petite fente "
                "percée dans un mur. Si Konan regarde à son tour par cette "
                "même fente, verra-t-il l'œil d'Awa ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : théorème --------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("PRINCIPE DE RÉVERSIBILITÉ : le trajet suivi par la", font_size=20),
                Text("lumière entre deux points est indépendant du sens de", font_size=20),
                Text("parcours.", font_size=20),
                Text("Si un rayon va de A à B en suivant un trajet donné, un", font_size=19),
                Text("rayon allant de B à A suit exactement le même trajet.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le principe de réversibilité énonce que le trajet suivi "
                "par la lumière entre deux points est indépendant du sens "
                "de parcours. Si un rayon va d'un point A à un point B en "
                "suivant un certain trajet, un rayon allant de B vers A "
                "suit exactement ce même trajet, parcouru en sens "
                "inverse."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        consequence = theorem_box(
            Text(
                "Conséquence pratique : ce principe permet de construire\n"
                "facilement le trajet d'un rayon lumineux dans un sens en\n"
                "le déduisant du trajet, connu, dans l'autre sens.",
                font_size=19,
            ),
            box_width=11.2,
        )
        consequence.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce principe a une conséquence très pratique : il permet "
                "de construire facilement le trajet d'un rayon lumineux "
                "dans un sens en le déduisant simplement du trajet connu "
                "dans l'autre sens, ce qui simplifie de nombreuses "
                "constructions géométriques."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- Exemple résolu 5 -----------------------------------------------------
        schema1 = _schema_awa_konan("konan_vers_awa")
        schema1.scale(0.8)
        schema1.next_to(titre, DOWN, buff=0.5)

        legende1 = Text(
            "Awa voit l'œil de Konan à travers la fente F.",
            font_size=18, color=WHITE,
        )
        legende1.next_to(schema1, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Reprenons notre exemple. Awa voit l'œil de Konan à "
                "travers la fente F : le rayon lumineux part de l'œil de "
                "Konan, traverse la fente, et atteint l'œil d'Awa."
            )
        ) as tracker:
            self.play(FadeIn(schema1))
            self.play(FadeIn(legende1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema1), FadeOut(legende1))

        schema2 = _schema_awa_konan("awa_vers_konan")
        schema2.scale(0.8)
        schema2.next_to(titre, DOWN, buff=0.5)

        reponse = example_box(
            VGroup(
                Text("Par le principe de réversibilité, le rayon inverse", font_size=19),
                Text("(de l'œil d'Awa vers l'œil de Konan) suit EXACTEMENT", font_size=19),
                Text("le même trajet à travers la fente F.", font_size=19),
                Text("→ OUI, Konan peut voir l'œil d'Awa.", font_size=19, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.2,
        )
        reponse.next_to(schema2, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Par le principe de réversibilité, le rayon qui va cette "
                "fois de l'œil d'Awa vers l'œil de Konan suit exactement "
                "le même trajet à travers la fente F. La réponse est donc "
                "oui : Konan peut voir l'œil d'Awa à travers cette même "
                "fente."
            )
        ) as tracker:
            self.play(FadeIn(schema2))
            self.play(FadeIn(reponse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema2), FadeOut(reponse))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Le trajet de la lumière ne dépend pas du sens de", font_size=20),
                Text("parcours : ce qui est vu dans un sens l'est aussi", font_size=20),
                Text("dans l'autre, par le même trajet.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le trajet de la lumière ne dépend "
                "pas du sens de parcours. Ce qui est vu dans un sens l'est "
                "donc aussi dans l'autre, en empruntant exactement le même "
                "trajet."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Le principe porte sur le TRAJET géométrique, pas sur", font_size=19),
                Text("   la garantie que deux observateurs voient la même", font_size=19),
                Text("   chose au même instant (la scène peut avoir changé).", font_size=19),
                Text("• Il ne s'applique que si le trajet reste inchangé", font_size=19),
                Text("   (même fente, mêmes obstacles) entre les deux sens.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Attention : ce principe porte sur le trajet géométrique "
                "de la lumière, pas sur une garantie que deux observateurs "
                "voient exactement la même chose au même instant, la scène "
                "pouvant avoir changé entre-temps. Il ne s'applique "
                "d'ailleurs que si le trajet reste inchangé, avec la même "
                "fente et les mêmes obstacles, dans les deux sens."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
