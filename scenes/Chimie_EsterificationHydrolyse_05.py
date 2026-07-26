"""
scenes/Chimie_EsterificationHydrolyse_05.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 05.

§ Catalyse par les ions H+ et rôle de l'acide sulfurique : constat
expérimental (H2SO4/HCl accélère sans changer la composition finale),
definition_box catalyseur, rôle double de H2SO4 (fournit H+ catalyseur +
pouvoir déshydratant qui peut déplacer l'équilibre). warning_box piège : ne
pas dire que H2SO4 « permet » la réaction ou « augmente le rendement » en
tant que catalyseur.
Source : 1ereC/Chimie.pdf, chapitre 8, page 78.
"""

import textwrap

from manim import (
    DOWN,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
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


class CatalyseIonsHPlusAcideSulfurique(NotionScene):
    def construct(self):
        titre = scene_title("5. Catalyse par les ions H⁺ et rôle de H₂SO₄")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Nous avons vu que le chauffage accélère l'estérification. "
                "Un autre moyen, chimique cette fois, permet lui aussi de "
                "gagner du temps : l'ajout d'acide sulfurique.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons vu que le chauffage accélère l'estérification. "
                "Un autre moyen, chimique cette fois, permet lui aussi de "
                "gagner du temps : l'ajout d'acide sulfurique. Comment "
                "agit-il exactement ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : constat expérimental -----------------------------------
        entete = Text("Constat expérimental", font_size=26, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        constat = Text(
            _wrap(
                "En ajoutant de l'acide sulfurique concentré (H2SO4), ou "
                "de l'acide chlorhydrique, au mélange acide + alcool : "
                "l'équilibre est atteint beaucoup plus vite, MAIS la "
                "composition finale (quantité d'ester à l'équilibre) "
                "reste EXACTEMENT LA MÊME qu'en leur absence.",
                width=48,
            ),
            font_size=22,
            color=WHITE,
        )
        constat.next_to(entete, DOWN, buff=0.4)
        groupe = VGroup(entete, constat)
        _fit(groupe, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "L'expérience montre ceci : en ajoutant de l'acide "
                "sulfurique concentré, ou de l'acide chlorhydrique, au "
                "mélange acide plus alcool, l'équilibre est atteint "
                "beaucoup plus vite. Mais la composition finale, la "
                "quantité d'ester obtenue à l'équilibre, reste exactement "
                "la même qu'en leur absence."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(constat))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple traité : definition_box catalyseur ------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un catalyseur est une espèce chimique qui augmente la "
                    "vitesse d'une réaction, sans apparaître dans "
                    "l'équation bilan (il n'est pas consommé), et SANS "
                    "modifier l'état d'équilibre final.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ces ions hydrogène, H plus, agissent donc comme des "
                "catalyseurs. Retenons cette définition : un catalyseur "
                "est une espèce chimique qui augmente la vitesse d'une "
                "réaction, sans apparaître dans l'équation bilan puisqu'il "
                "n'est pas consommé, et sans modifier l'état d'équilibre "
                "final."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Rôle double de H2SO4 -----------------------------------------------------
        entete2 = Text("Le double rôle de l'acide sulfurique", font_size=24, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        role1 = Text(
            "1) Il fournit des ions H⁺ : rôle de CATALYSEUR",
            font_size=22,
            color=WHITE,
            weight="BOLD",
        )
        role1b = Text(
            "(accélère, ne change pas la composition finale).",
            font_size=20,
            color=WHITE,
        )
        role2 = Text(
            "2) Concentré, il a un pouvoir DÉSHYDRATANT :",
            font_size=22,
            color=WHITE,
            weight="BOLD",
        )
        role2b = Text(
            _wrap(
                "il peut piéger l'eau formée, ce qui, cette fois, "
                "DÉPLACE l'équilibre (effet distinct de la catalyse).",
                width=46,
            ),
            font_size=20,
            color=WHITE,
        )
        bloc2 = VGroup(role1, role1b, role2, role2b).arrange(DOWN, buff=0.2)
        bloc2.next_to(entete2, DOWN, buff=0.4)
        groupe2 = VGroup(entete2, bloc2)
        _fit(groupe2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "En réalité, l'acide sulfurique joue un double rôle, qu'il "
                "faut bien distinguer. Premièrement, il fournit des ions "
                "H plus, qui jouent le rôle de catalyseur : ils "
                "accélèrent la réaction sans changer sa composition "
                "finale. Deuxièmement, concentré, il possède aussi un "
                "puissant pouvoir déshydratant : il peut piéger l'eau "
                "formée au fur et à mesure, et cette fois, cet effet "
                "déplace réellement l'équilibre. Ce sont deux effets "
                "bien distincts."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(role1), FadeIn(role1b))
            self.play(FadeIn(role2), FadeIn(role2b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text(
                    _wrap(
                        "Ne jamais dire que H2SO4 « permet » la réaction "
                        "(elle a lieu même sans lui, juste plus lentement).",
                        width=46,
                    ),
                    font_size=21,
                ),
                Text(
                    _wrap(
                        "Ne jamais dire qu'un catalyseur « augmente le "
                        "rendement » : EN TANT QUE CATALYSEUR, il ne "
                        "change QUE la vitesse, jamais la composition à "
                        "l'équilibre.",
                        width=46,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège très fréquent : il ne faut jamais "
                "dire que l'acide sulfurique « permet » la réaction "
                "d'estérification — elle a lieu même sans lui, "
                "simplement beaucoup plus lentement. Et il ne faut "
                "surtout jamais dire qu'un catalyseur « augmente le "
                "rendement » : en tant que catalyseur, il ne change QUE "
                "la vitesse de la réaction, jamais la quantité d'ester "
                "obtenue à l'équilibre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
