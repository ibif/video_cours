"""
scenes/Chimie_Electrolyse_10.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 10.

§ 10. Applications industrielles de l'électrolyse. Affinage des métaux
(principe du raffinage vu en 14.8, généralisé à d'autres métaux).
Galvanoplastie : dépôt d'une fine couche de métal précieux sur un objet
(argenture, chromage), l'objet à recouvrir servant de cathode.
Électrozingage : dépôt de zinc sur des tôles d'acier (tôles zinguées),
protection anti-corrosion par effet de barrière et protection cathodique.
Production industrielle de dichlore, de soude et de dihydrogène
(industrie chlore-soude, cf. scène 06). Autres applications : électrolyse
de l'eau pour produire H₂ et O₂ purs, anodisation de l'aluminium (couche
d'oxyde protectrice), production de métaux très réducteurs (Al, Na, Mg)
par électrolyse de sels fondus (impossible en solution aqueuse, cf.
règle des ions spectateurs).
Source : 1ereC/Chimie.pdf, chapitre 14, pages 143 et suivantes.
"""

import textwrap

from manim import (
    DOWN,
    GOLD,
    GREEN,
    LEFT,
    LIGHT_GRAY,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
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


def _bloc_application(titre_txt, description, couleur):
    entete = Text(titre_txt, font_size=20, color=couleur, weight="BOLD")
    corps = Text(_wrap(description, width=52), font_size=18, color=WHITE)
    corps.next_to(entete, DOWN, buff=0.18, aligned_edge=LEFT)
    return VGroup(entete, corps)


class ApplicationsIndustriellesElectrolyse(NotionScene):
    def construct(self):
        titre = scene_title("14.10 Applications industrielles de l'électrolyse")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : panorama ---------------------------------------------------
        intro = Text(
            _wrap(
                "L'électrolyse n'est pas qu'une expérience de laboratoire : "
                "elle est au cœur de nombreux procédés industriels. "
                "Passons-les en revue.",
                width=58,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'électrolyse n'est pas qu'une expérience de "
                "laboratoire : elle est au cœur de nombreux procédés "
                "industriels, que nous allons passer en revue."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : affinage + galvanoplastie ------------------------------
        bloc_affinage = _bloc_application(
            "1. Affinage des métaux",
            "Généralisation du raffinage du cuivre (scène 8) : l'anode "
            "impure se dissout, le métal pur se redépose à la cathode. "
            "Utilisé aussi pour le nickel, le plomb, le zinc.",
            YELLOW,
        )
        bloc_galvano = _bloc_application(
            "2. Galvanoplastie (argenture, chromage)",
            "L'objet à recouvrir sert de CATHODE, dans une solution "
            "contenant les ions du métal précieux. Un fin dépôt métallique "
            "se forme à sa surface : couverts argentés, pare-chocs "
            "chromés.",
            YELLOW,
        )
        groupe1 = VGroup(bloc_affinage, bloc_galvano).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        groupe1.next_to(titre, DOWN, buff=0.4)
        _fit(groupe1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Premièrement, l'affinage des métaux : c'est la "
                "généralisation du principe de raffinage du cuivre vu "
                "précédemment. L'anode impure se dissout, le métal pur se "
                "redépose à la cathode. On l'utilise aussi pour le "
                "nickel, le plomb, le zinc. Deuxièmement, la "
                "galvanoplastie, qui regroupe l'argenture et le chromage. "
                "L'objet à recouvrir sert de cathode, plongé dans une "
                "solution contenant les ions du métal précieux : un fin "
                "dépôt métallique se forme à sa surface, comme sur des "
                "couverts argentés ou des pare-chocs chromés."
            )
        ) as tracker:
            self.play(FadeIn(bloc_affinage))
            self.play(FadeIn(bloc_galvano))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        # --- Exemple traité : électrozingage + chlore-soude -------------------------
        bloc_zinc = _bloc_application(
            "3. Électrozingage",
            "Dépôt de zinc sur des tôles d'acier (tôles zinguées) : le "
            "zinc, plus réducteur que le fer, protège l'acier de la "
            "rouille (protection dite « sacrificielle »).",
            GREEN,
        )
        bloc_chlore = _bloc_application(
            "4. Industrie chlore-soude",
            "Électrolyse industrielle de saumure (NaCl concentré, cf. "
            "scène 6) : production à grande échelle de dichlore, de "
            "dihydrogène, et de soude (NaOH).",
            GREEN,
        )
        groupe2 = VGroup(bloc_zinc, bloc_chlore).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        groupe2.next_to(titre, DOWN, buff=0.4)
        _fit(groupe2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisièmement, l'électrozingage : on dépose une fine "
                "couche de zinc sur des tôles d'acier, qui deviennent des "
                "tôles zinguées. Le zinc, plus réducteur que le fer, "
                "s'oxyde à sa place et protège ainsi l'acier de la "
                "rouille : on parle de protection sacrificielle. "
                "Quatrièmement, l'industrie chlore-soude, que nous avons "
                "déjà rencontrée : l'électrolyse industrielle de saumure, "
                "c'est-à-dire de chlorure de sodium concentré, produit à "
                "grande échelle du dichlore, du dihydrogène, et de la "
                "soude."
            )
        ) as tracker:
            self.play(FadeIn(bloc_zinc))
            self.play(FadeIn(bloc_chlore))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir : autres applications -----------------------------------------
        autres = _bullets(
            [
                "ÉLECTROLYSE DE L'EAU : production de H₂ et O₂ purs (pile "
                "à combustible, propulsion spatiale) ;",
                "ANODISATION DE L'ALUMINIUM : l'aluminium sert d'ANODE, "
                "s'oxyde en surface et forme une couche d'oxyde "
                "protectrice et décorative ;",
                "métaux TRÈS RÉDUCTEURS (Al, Na, Mg) : impossibles à "
                "obtenir par électrolyse en solution aqueuse (ce sont des "
                "ions spectateurs, scène 7) — on électrolyse alors un SEL "
                "FONDU, sans eau.",
            ],
            font_size=18,
            width=56,
        )
        entete_autres = Text("5. Autres applications", font_size=21, color="#288073", weight="BOLD")
        entete_autres.next_to(titre, DOWN, buff=0.4)
        autres.next_to(entete_autres, DOWN, buff=0.3)
        _fit(VGroup(entete_autres, autres), entete_autres.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Enfin, retenons trois autres applications. L'électrolyse "
                "de l'eau, pour produire du dihydrogène et du dioxygène "
                "très purs, utilisés par exemple dans les piles à "
                "combustible. L'anodisation de l'aluminium, où "
                "l'aluminium sert d'anode et s'oxyde volontairement en "
                "surface pour former une couche d'oxyde protectrice et "
                "décorative. Et enfin, la production de métaux très "
                "réducteurs comme l'aluminium, le sodium ou le magnésium, "
                "impossibles à obtenir par électrolyse en solution "
                "aqueuse, puisque ce sont des ions spectateurs : on "
                "électrolyse alors un sel fondu, sans eau du tout."
            )
        ) as tracker:
            self.play(FadeIn(entete_autres))
            self.play(FadeIn(autres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_autres), FadeOut(autres), FadeOut(titre))
