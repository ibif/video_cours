"""
scenes/Chimie_ClassificationQualitativeRedox_07.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 07.

§ 3 (fin) et § 4. Justification microscopique de la règle du gamma
(transfert d'électrons du réducteur le plus fort vers l'oxydant le plus
fort). Applications : (1) action des acides sur les métaux — pourquoi
l'or et l'argent y résistent ; (2) métallurgie — réduction des oxydes
métalliques par un réducteur plus fort (ZnO + C → Zn + CO), obtention par
électrolyse des métaux très réducteurs (Na, Mg, Al, Ca).
Source : 1ereC/Chimie.pdf, chapitre 10, pages 98-99.
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


class JustificationEtApplications(NotionScene):
    def construct(self):
        titre = scene_title("10.3-4 Justification microscopique et applications")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        intro = Text(
            _wrap(
                "Pourquoi la règle du gamma fonctionne-t-elle ? Et à quoi "
                "sert concrètement cette classification, au-delà des "
                "expériences de laboratoire ?",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi la règle du gamma fonctionne-t-elle vraiment ? Et "
                "à quoi sert concrètement cette classification, au-delà des "
                "expériences de laboratoire ? Répondons à ces deux "
                "questions."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : justification microscopique -------------------------
        entete_justif = Text("Justification : un transfert d'électrons", font_size=21, color=YELLOW, weight="BOLD")
        entete_justif.next_to(titre, DOWN, buff=0.35)

        transfert = MathTex(
            r"Red_{fort} \xrightarrow{\;e^{-}\;} Ox_{fort}",
            font_size=30, color=ORANGE,
        )
        texte_justif = Text(
            _wrap(
                "À l'échelle microscopique, le réducteur le plus fort cède "
                "spontanément ses électrons ; l'oxydant le plus fort est "
                "précisément celui qui les capte le plus facilement. Le γ "
                "matérialise ce transfert.",
                width=52,
            ),
            font_size=20, color=WHITE,
        )
        contenu_justif = VGroup(transfert, texte_justif).arrange(DOWN, buff=0.35)
        contenu_justif.next_to(entete_justif, DOWN, buff=0.35)
        groupe_justif = VGroup(entete_justif, contenu_justif)
        _fit(groupe_justif, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "À l'échelle microscopique, ce que dessine le gamma, c'est "
                "un transfert d'électrons : le réducteur le plus fort cède "
                "spontanément ses électrons, et l'oxydant le plus fort est "
                "précisément l'espèce qui les capte le plus facilement. Le "
                "gamma n'est donc pas qu'une astuce de dessin, il "
                "matérialise le sens réel du transfert électronique."
            )
        ) as tracker:
            self.play(FadeIn(entete_justif))
            self.play(Write(transfert))
            self.play(FadeIn(texte_justif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_justif))

        # --- Exemple traité : application 1, acides sur métaux ------------------
        entete_app1 = Text("Application 1 — Action des acides sur les métaux", font_size=20, color=YELLOW, weight="BOLD")
        entete_app1.next_to(titre, DOWN, buff=0.3)

        app1 = _bullets(
            [
                "Un métal placé sous H₃O⁺/H₂ dans la classification "
                "(Zn, Fe, ...) est un réducteur plus fort que H₂ : le γ "
                "existe, la réaction avec un acide se produit.",
                "L'or et l'argent sont placés AU-DESSUS de H₃O⁺/H₂ : ils "
                "sont moins réducteurs que H₂, aucun γ possible, d'où leur "
                "résistance aux acides usuels.",
            ],
            font_size=19, width=56,
        )
        app1.next_to(entete_app1, DOWN, buff=0.3)
        groupe_app1 = VGroup(entete_app1, app1)
        _fit(groupe_app1, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Première application : l'action des acides sur les "
                "métaux, que nous avions déjà observée. Un métal placé sous "
                "le couple H-trois-O-plus sur H-deux, comme le zinc ou le "
                "fer, est un réducteur plus fort que le dihydrogène : le "
                "gamma existe, la réaction avec un acide se produit. L'or "
                "et l'argent, eux, sont placés au-dessus de ce couple : ils "
                "sont moins réducteurs que le dihydrogène, aucun gamma "
                "n'est possible, ce qui explique leur résistance aux acides "
                "usuels."
            )
        ) as tracker:
            self.play(FadeIn(entete_app1))
            self.play(FadeIn(app1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_app1))

        # --- À retenir : application 2, métallurgie ------------------------------
        entete_app2 = Text("Application 2 — La métallurgie", font_size=20, color=YELLOW, weight="BOLD")
        entete_app2.next_to(titre, DOWN, buff=0.3)

        texte_metal = Text(
            _wrap(
                "Un oxyde métallique MO peut être réduit par un réducteur "
                "chimique plus fort que le métal M (souvent le carbone) :",
                width=54,
            ),
            font_size=19, color=WHITE,
        )
        eq_metal = MathTex(r"ZnO + C \longrightarrow Zn + CO", font_size=27, color=ORANGE)
        texte_electrolyse = Text(
            _wrap(
                "Les métaux très réducteurs (Na, Mg, Al, Ca) n'ont aucun "
                "réducteur chimique usuel assez fort : on les obtient par "
                "électrolyse.",
                width=54,
            ),
            font_size=19, color=WHITE,
        )
        contenu_app2 = VGroup(texte_metal, eq_metal, texte_electrolyse).arrange(DOWN, buff=0.3)
        contenu_app2.next_to(entete_app2, DOWN, buff=0.3)
        groupe_app2 = VGroup(entete_app2, contenu_app2)
        _fit(groupe_app2, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Deuxième application : la métallurgie, c'est-à-dire "
                "l'obtention des métaux à partir de leurs minerais. Un "
                "oxyde métallique, M-O, peut être réduit par un réducteur "
                "chimique plus fort que le métal M, souvent le carbone : "
                "oxyde de zinc, plus carbone, donne zinc, plus monoxyde de "
                "carbone. Mais les métaux très réducteurs, comme le "
                "sodium, le magnésium, l'aluminium ou le calcium, n'ont "
                "aucun réducteur chimique usuel assez fort pour les "
                "obtenir ainsi : on doit alors recourir à l'électrolyse."
            )
        ) as tracker:
            self.play(FadeIn(entete_app2))
            self.play(FadeIn(texte_metal))
            self.play(Write(eq_metal))
            self.play(FadeIn(texte_electrolyse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_app2))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas croire qu'un métal quelconque peut réduire "
                    "n'importe quel oxyde : il faut que le réducteur employé "
                    "(ici le carbone) soit chimiquement plus fort que le "
                    "métal à extraire, sinon aucune réaction ne se produit.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas croire qu'un réducteur quelconque peut "
                "réduire n'importe quel oxyde métallique. Il faut, comme "
                "toujours, que le réducteur employé, ici le carbone, soit "
                "chimiquement plus fort que le métal que l'on cherche à "
                "extraire, sinon aucune réaction ne se produit."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
