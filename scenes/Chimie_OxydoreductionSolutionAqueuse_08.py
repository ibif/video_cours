"""
scenes/Chimie_OxydoreductionSolutionAqueuse_08.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 08.

§ Réaction entre deux couples : sens spontané. 3 expériences (Cu dans Cu²⁺
rien, Fe dans Cu²⁺ réaction, Cu dans Fe²⁺ rien), règle du sens spontané
(l'oxydant le plus fort réagit avec le réducteur le plus fort), échelle
qualitative Fe > Cu comme réducteurs. Exemple résolu 7 : zinc dans sulfate
de cuivre.
Source : 1ereC/Chimie.pdf, chapitre 9, page 92.
"""

import textwrap

from manim import (
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _resultat_experience(reaction: bool):
    """Petit symbole (coche verte ou croix rouge) pour illustrer si une
    expérience réagit ou non — construit avec des primitives de base."""
    if reaction:
        symbole = MathTex(r"\checkmark", font_size=34, color=GREEN)
    else:
        symbole = Text("✗", font_size=30, color=RED)
    return symbole


class SensSpontaneReaction(NotionScene):
    def construct(self):
        titre = scene_title("9.8 Réaction entre deux couples — sens spontané")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : trois expériences comparatives ---------------------------------
        entete_exp = Text("Trois expériences comparatives", font_size=22, color=YELLOW, weight="BOLD")
        entete_exp.next_to(titre, DOWN, buff=0.4)

        exp1 = VGroup(
            Text("1. Cu métal dans Cu²⁺", font_size=20, color=WHITE),
            _resultat_experience(False),
            Text("aucune réaction", font_size=16, color=GRAY),
        ).arrange(RIGHT, buff=0.3)

        exp2 = VGroup(
            Text("2. Fe métal dans Cu²⁺", font_size=20, color=WHITE),
            _resultat_experience(True),
            Text("réaction (dépôt de Cu)", font_size=16, color=GRAY),
        ).arrange(RIGHT, buff=0.3)

        exp3 = VGroup(
            Text("3. Cu métal dans Fe²⁺", font_size=20, color=WHITE),
            _resultat_experience(False),
            Text("aucune réaction", font_size=16, color=GRAY),
        ).arrange(RIGHT, buff=0.3)

        experiences = VGroup(exp1, exp2, exp3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        experiences.next_to(entete_exp, DOWN, buff=0.45)
        groupe_exp = VGroup(entete_exp, experiences)

        with self.voiceover(
            text=(
                "Faisons trois expériences comparatives. Première "
                "expérience : on plonge du cuivre métal dans une solution "
                "d'ions cuivre deux plus — aucune réaction, rien ne se "
                "passe, c'est logique, c'est le même couple. Deuxième "
                "expérience : on plonge du fer métal dans une solution "
                "d'ions cuivre deux plus — nous l'avons vu, il y a "
                "réaction, avec dépôt de cuivre. Troisième expérience : on "
                "plonge du cuivre métal dans une solution d'ions fer deux "
                "plus — là encore, aucune réaction ne se produit."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_exp))
            self.play(FadeIn(exp1))
            self.play(FadeIn(exp2))
            self.play(FadeIn(exp3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_exp))

        # --- Raisonnement : la règle du sens spontané ---------------------------------
        regle = property_box(
            Text(
                _wrap(
                    "Une réaction d'oxydoréduction se produit "
                    "spontanément dans le sens où l'OXYDANT LE PLUS FORT "
                    "réagit avec le RÉDUCTEUR LE PLUS FORT, pris parmi "
                    "deux couples différents.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        regle.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Ces trois expériences illustrent une règle générale : une "
                "réaction d'oxydoréduction se produit spontanément dans le "
                "sens où l'oxydant le plus fort réagit avec le réducteur le "
                "plus fort, pris parmi deux couples différents. Le fer "
                "réagit avec les ions cuivre parce que le fer est un "
                "réducteur plus fort que le cuivre."
            )
        ) as tracker:
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle))

        # --- Exemple traité : échelle qualitative + exemple résolu 7 ------------------
        entete_echelle = Text("Échelle qualitative de pouvoir réducteur", font_size=21, color=YELLOW, weight="BOLD")
        entete_echelle.next_to(titre, DOWN, buff=0.35)

        echelle = MathTex(r"\text{Fe} \;>\; \text{Cu} \quad \text{(pouvoir réducteur décroissant)}", font_size=26, color=WHITE)
        echelle.next_to(entete_echelle, DOWN, buff=0.4)

        consequence = Text(
            "Donc, pour les oxydants associés : Fe²⁺ est un oxydant plus faible que Cu²⁺.",
            font_size=18, color=WHITE,
        )
        consequence.next_to(echelle, DOWN, buff=0.35)

        groupe_echelle = VGroup(entete_echelle, echelle, consequence)

        with self.voiceover(
            text=(
                "On peut donc classer le fer et le cuivre sur une échelle "
                "qualitative de pouvoir réducteur : le fer est un réducteur "
                "plus fort que le cuivre. Par conséquent, pour les "
                "oxydants associés, c'est l'inverse : l'ion fer deux plus "
                "est un oxydant plus faible que l'ion cuivre deux plus."
            )
        ) as tracker:
            self.play(FadeIn(entete_echelle))
            self.play(Write(echelle))
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_echelle))

        entete_ex7 = Text("Exemple résolu 7 — zinc dans le sulfate de cuivre", font_size=20, color=YELLOW, weight="BOLD")
        entete_ex7.next_to(titre, DOWN, buff=0.35)

        demi7a = MathTex(r"Zn \rightarrow Zn^{2+} + 2\,e^-", font_size=25, color=WHITE)
        demi7b = MathTex(r"Cu^{2+} + 2\,e^- \rightarrow Cu", font_size=25, color=WHITE)
        bilan7 = MathTex(r"Zn + Cu^{2+} \longrightarrow Zn^{2+} + Cu", font_size=28, color=YELLOW)
        observation7 = Text(
            "Observation : dépôt rouge de cuivre sur le zinc, décoloration du bleu (Zn est plus réducteur que Cu).",
            font_size=16, color=WHITE,
        )

        groupe7 = VGroup(entete_ex7, demi7a, demi7b, bilan7, observation7).arrange(DOWN, buff=0.3)
        groupe7.next_to(titre, DOWN, buff=0.35)
        _fit(groupe7, titre.get_bottom()[1] - 0.35)
        groupe7.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu sept : on plonge une lame de zinc dans une "
                "solution de sulfate de cuivre. Le zinc, tout comme le fer, "
                "est un réducteur plus fort que le cuivre : la réaction se "
                "produit spontanément. Le zinc cède deux électrons pour "
                "former des ions zinc deux plus, les ions cuivre deux plus "
                "captent ces deux électrons pour former du cuivre "
                "métallique. L'équation bilan est : zinc, plus ion cuivre "
                "deux plus, donne ion zinc deux plus, plus cuivre. On "
                "observe, comme avec le fer, un dépôt rouge de cuivre sur "
                "la lame de zinc et une décoloration progressive du bleu de "
                "la solution."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex7))
            self.play(Write(demi7a))
            self.play(Write(demi7b))
            self.play(Write(bilan7))
            self.play(FadeIn(observation7))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe7))

        # --- À retenir : la règle générale --------------------------------------------
        recap = example_box(
            Text(
                _wrap(
                    "Retenir : pour prévoir le sens spontané d'une "
                    "réaction entre deux couples, il suffit de comparer "
                    "les pouvoirs oxydant et réducteur des espèces en "
                    "présence — la réaction a lieu entre l'oxydant fort et "
                    "le réducteur fort.",
                    width=48,
                ),
                font_size=21,
                color="#1A1A1A",
            ),
        )
        recap.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : pour prévoir le sens spontané "
                "d'une réaction entre deux couples, il suffit de comparer "
                "les pouvoirs oxydant et réducteur des espèces en "
                "présence — la réaction a lieu entre l'oxydant fort et le "
                "réducteur fort."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : « rien ne se passe » ne veut pas dire couple identique -
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : l'absence de réaction (cuivre dans Fe²⁺) ne "
                    "signifie pas que les deux couples sont identiques, "
                    "mais que le sens inverse n'est PAS spontané. Il ne "
                    "faut jamais écrire une équation bilan dans le sens "
                    "non spontané.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Attention à un piège : l'absence de réaction, comme "
                "lorsqu'on plonge du cuivre dans une solution d'ions fer "
                "deux plus, ne signifie pas que les deux couples sont "
                "identiques, mais simplement que le sens inverse n'est pas "
                "spontané. Il ne faut donc jamais écrire une équation bilan "
                "dans le sens non spontané."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
