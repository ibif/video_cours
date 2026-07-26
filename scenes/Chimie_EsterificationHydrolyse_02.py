"""
scenes/Chimie_EsterificationHydrolyse_02.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 02.

§ La réaction d'estérification : definition_box, équation générale
R-COOH + R'-OH ⇌ R-COO-R' + H2O, exemple éthanoate d'éthyle. Réversibilité
(double flèche), origine de l'oxygène de l'ester (vient de l'alcool, étude
isotopique O18). Protocole labo (chauffage à reflux + H2SO4 catalyseur).
Source : 1ereC/Chimie.pdf, chapitre 8, pages 76-77.
"""

import textwrap

from manim import (
    DOWN,
    UP,
    WHITE,
    YELLOW,
    ORANGE,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ReactionEsterificationEquationGenerale(NotionScene):
    def construct(self):
        titre = scene_title("2. La réaction d'estérification : équation générale")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Comment passe-t-on d'un acide carboxylique et d'un "
                "alcool à un ester ? Il faut les faire réagir ensemble : "
                "c'est la réaction d'estérification.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment passe-t-on d'un acide carboxylique et d'un "
                "alcool à un ester ? Il faut les faire réagir ensemble : "
                "c'est la réaction d'estérification, que nous allons "
                "maintenant écrire précisément."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : équation générale --------------------------------------
        entete = Text("Équation générale de l'estérification", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        eq_generale = MathTex(
            r"R-COOH + R'-OH \;\rightleftharpoons\; R-COO-R' + H_2O",
            font_size=36,
            color=WHITE,
        )
        legende = Text(
            "acide carboxylique + alcool ⇌ ester + eau",
            font_size=22,
            color=WHITE,
        )
        bloc = VGroup(eq_generale, legende).arrange(DOWN, buff=0.35)
        bloc.next_to(entete, DOWN, buff=0.4)
        groupe = VGroup(entete, bloc)

        with self.voiceover(
            text=(
                "L'équation générale s'écrit ainsi : R-C-O-O-H, l'acide "
                "carboxylique, plus R'-O-H, l'alcool, réagissent pour "
                "donner R-C-O-O-R', l'ester, plus de l'eau. Remarquez la "
                "double flèche : nous verrons dans une prochaine scène "
                "qu'elle traduit un aspect essentiel de cette réaction, "
                "sa réversibilité."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(Write(eq_generale))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple traité : éthanoate d'éthyle + origine de l'oxygène -----------
        entete2 = Text("Exemple : formation de l'éthanoate d'éthyle", font_size=22, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        eq_exemple = MathTex(
            r"CH_3-COOH + C_2H_5-OH \;\rightleftharpoons\; CH_3-COO-C_2H_5 + H_2O",
            font_size=30,
            color=WHITE,
        )
        eq_exemple.next_to(entete2, DOWN, buff=0.35)

        origine = Text(
            _wrap(
                "Une étude par marquage isotopique (alcool marqué à "
                "l'oxygène 18) montre que l'oxygène qui relie les deux "
                "groupes carbonés dans l'ester provient de l'ALCOOL, et "
                "non de l'acide : c'est le groupe -OH de l'acide qui part "
                "avec un hydrogène de l'alcool pour former l'eau.",
                width=50,
            ),
            font_size=21,
            color=WHITE,
        )
        origine.next_to(eq_exemple, DOWN, buff=0.4)

        groupe2 = VGroup(entete2, eq_exemple, origine)
        _fit(groupe2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Prenons l'exemple de l'acide éthanoïque et de l'éthanol : "
                "ils réagissent pour donner l'éthanoate d'éthyle et de "
                "l'eau. Une expérience historique, utilisant un alcool "
                "marqué à l'oxygène dix-huit, un isotope de l'oxygène, a "
                "permis de savoir d'où vient l'oxygène central de l'ester. "
                "Résultat : cet oxygène provient de l'alcool, et non de "
                "l'acide. Le groupe hydroxyle de l'acide part donc avec un "
                "atome d'hydrogène de l'alcool pour former la molécule "
                "d'eau libérée."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(Write(eq_exemple))
            self.play(FadeIn(origine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir : definition_box + protocole labo ---------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'estérification est la réaction, réversible, d'un "
                    "acide carboxylique avec un alcool pour former un "
                    "ester et de l'eau : acide + alcool ⇌ ester + eau.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons cette définition : l'estérification est la "
                "réaction, réversible, d'un acide carboxylique avec un "
                "alcool, pour former un ester et de l'eau."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        protocole = Text(
            _wrap(
                "Au laboratoire : on chauffe le mélange acide + alcool à "
                "reflux (le ballon est surmonté d'un réfrigérant vertical "
                "qui condense les vapeurs et les renvoie dans le milieu "
                "réactionnel, sans perte de matière), en présence d'acide "
                "sulfurique concentré comme catalyseur.",
                width=50,
            ),
            font_size=22,
            color=ORANGE,
        )
        protocole.next_to(titre, DOWN, buff=0.5)
        _fit(protocole, titre.get_bottom()[1] - 0.5)

        with self.voiceover(
            text=(
                "Au laboratoire, ce mélange acide plus alcool est chauffé "
                "à reflux : le ballon réactionnel est surmonté d'un "
                "réfrigérant vertical qui condense les vapeurs et les "
                "renvoie dans le milieu, sans aucune perte de matière, "
                "tout en accélérant la réaction. On ajoute aussi de "
                "l'acide sulfurique concentré, qui joue le rôle de "
                "catalyseur — nous détaillerons son rôle précis un peu "
                "plus loin dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(protocole), FadeOut(titre))
