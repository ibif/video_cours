"""
scenes/SVT_MouvementsPlaques_09.py — Chapitre 7 (1ereD, SVT), scène 09.

§ 7.5 Le moteur des mouvements des plaques : convection mantellique
(définition, remarque sur l'image de la marmite), forces motrices
(poussée aux dorsales, traction des plaques plongeantes), bilan nul de
création/destruction, exemple chiffré, méthode de raisonnement de
synthèse en géologie. Source : 1ereD/SVT.pdf, pages 98-99.
"""

import textwrap

from manim import (
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    BLUE_E,
    DOWN,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


def _schema_convection():
    """Cellule de convection : montée chaude sous la dorsale, descente froide en subduction."""
    manteau = Rectangle(width=9.0, height=2.2, fill_color=ORANGE, fill_opacity=0.35, stroke_color=WHITE, stroke_width=1)

    montee = Arrow(start=[0, -1.0, 0], end=[0, 1.0, 0], color=RED, buff=0, stroke_width=5)
    label_montee = Text("remontée chaude", font_size=14, color=RED)
    label_montee.next_to(montee, LEFT, buff=0.15).shift(UP * 0.3)

    etale_g = Arrow(start=[0, 1.0, 0], end=[-3.3, 1.0, 0], color=WHITE, buff=0, stroke_width=3)
    etale_d = Arrow(start=[0, 1.0, 0], end=[3.3, 1.0, 0], color=WHITE, buff=0, stroke_width=3)

    descente_g = Arrow(start=[-3.3, 1.0, 0], end=[-3.3, -1.0, 0], color=BLUE_E, buff=0, stroke_width=5)
    descente_d = Arrow(start=[3.3, 1.0, 0], end=[3.3, -1.0, 0], color=BLUE_E, buff=0, stroke_width=5)
    label_descente = Text("plongée froide", font_size=14, color=BLUE_E)
    label_descente.next_to(descente_d, RIGHT, buff=0.15)

    return VGroup(manteau, montee, label_montee, etale_g, etale_d, descente_g, descente_d, label_descente)


class MoteurConvectionMantellique(NotionScene):
    def construct(self):
        titre = scene_title("7.5 — Le moteur des mouvements des plaques")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : la convection mantellique --------------------------------
        definition_convection = definition_box(
            Text(
                _wrap(
                    "Convection : mouvement de matière dû à une différence de "
                    "température : matériau chaud, moins dense, monte ; "
                    "matériau froid, plus dense, descend. Cellules de "
                    "convection. Chaleur interne héritée de la formation de "
                    "la Terre + radioactivité naturelle. Le manteau, presque "
                    "entièrement solide mais ductile, se déforme et circule "
                    "lentement.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=11.8,
        )
        definition_convection.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une dernière question reste posée depuis le début de ce "
                "chapitre : quelle force peut bien déplacer des continents "
                "entiers ? La réponse est la convection mantellique. La "
                "convection est un mouvement de matière dû à une différence "
                "de température : le matériau chaud, moins dense, monte ; "
                "le matériau froid, plus dense, descend, formant des "
                "cellules de convection. Cette chaleur interne provient à "
                "la fois de la formation de la Terre et de la radioactivité "
                "naturelle des roches. Le manteau, bien que presque "
                "entièrement solide, reste ductile : il se déforme et "
                "circule très lentement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_convection))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_convection))

        schema_conv = _schema_convection()
        schema_conv.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Sous les dorsales, le matériau mantellique chaud remonte, "
                "s'étale horizontalement, entraînant les plaques avec lui, "
                "puis se refroidit et redescend, plus loin, dans les zones "
                "de subduction : voilà le circuit complet d'une cellule de "
                "convection."
            )
        ) as tracker:
            self.play(FadeIn(schema_conv))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_conv))

        remarque_marmite = warning_box(
            Text(
                _wrap(
                    "Une image utile, mais avec précaution : le manteau n'est "
                    "pas liquide, il est solide et ductile, avec des "
                    "mouvements en cm/an sur des Ma (comme l'eau frémissante "
                    "d'une marmite, mais des millions de fois plus "
                    "lentement). 2 cm/an pendant 100 Ma = 2000 km.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        remarque_marmite.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'image de l'eau frémissante d'une marmite est utile pour "
                "comprendre la convection, mais à utiliser avec précaution "
                ": le manteau n'est pas liquide, il reste solide et "
                "ductile, avec des mouvements de quelques centimètres par "
                "an, mais étalés sur des millions d'années, des millions de "
                "fois plus lentement que dans une marmite. Et ce n'est pas "
                "négligeable : deux centimètres par an, pendant cent "
                "millions d'années, cela représente deux mille kilomètres "
                "parcourus."
            )
        ) as tracker:
            self.play(FadeIn(remarque_marmite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_marmite))

        # --- Animation du raisonnement : forces motrices + bilan nul ----------
        propriete_forces = property_box(
            Text(
                _wrap(
                    "Deux forces complètent la convection : la poussée "
                    "gravitaire aux dorsales (lithosphère chaude, surélevée, "
                    "glisse de part et d'autre du bombement) et la traction "
                    "de la plaque plongeante (partie déjà en subduction, "
                    "froide et dense, s'enfonce et tire le reste, comme un "
                    "poids suspendu).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        propriete_forces.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux forces mécaniques complètent la convection "
                "mantellique. La poussée gravitaire aux dorsales : la "
                "lithosphère chaude et surélevée y glisse de part et "
                "d'autre du bombement, sous l'effet de son propre poids. Et "
                "la traction de la plaque plongeante : la partie de la "
                "plaque déjà engagée en subduction, froide et dense, "
                "s'enfonce dans le manteau et tire derrière elle le reste "
                "de la plaque, comme un poids suspendu au bout d'une corde."
            )
        ) as tracker:
            self.play(FadeIn(propriete_forces))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_forces))

        propriete_bilan = property_box(
            Text(
                _wrap(
                    "Le bilan est nul : la Terre garde son rayon. La surface "
                    "créée aux dorsales égale la surface détruite en "
                    "subduction chaque année. La Terre ne gonfle ni ne "
                    "rétrécit.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        propriete_bilan.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une conséquence remarquable de tout ce mécanisme : le "
                "bilan global est nul, et la Terre garde un rayon constant. "
                "La surface de lithosphère créée chaque année aux dorsales "
                "égale exactement la surface détruite chaque année dans les "
                "zones de subduction. La Terre ne gonfle donc ni ne "
                "rétrécit."
            )
        ) as tracker:
            self.play(FadeIn(propriete_bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_bilan))

        # --- Exemple traité : vérification chiffrée du bilan -------------------
        enonce = Text(
            _wrap(
                "Vérifions ce bilan : longueur des dorsales 60 000 km, "
                "expansion moyenne 5 cm/an ; longueur des fosses 40 000 km, "
                "convergence moyenne 7,5 cm/an.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Vérifions ce bilan avec des chiffres réalistes. La "
                "longueur totale des dorsales est d'environ soixante mille "
                "kilomètres, pour une expansion moyenne de cinq "
                "centimètres par an. La longueur totale des fosses est "
                "d'environ quarante mille kilomètres, pour une convergence "
                "moyenne de sept virgule cinq centimètres par an."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc1 = MathTex(
            r"S_{\text{créée}} = 60\,000\ \text{km} \times 0{,}00005\ \text{km/an} = 3\ \text{km}^2/\text{an}",
            font_size=28, color=WHITE,
        )
        calc2 = MathTex(
            r"S_{\text{détruite}} = 40\,000\ \text{km} \times 0{,}000075\ \text{km/an} = 3\ \text{km}^2/\text{an}",
            font_size=28, color=WHITE,
        )
        calc3 = MathTex(
            r"S_{\text{créée}} = S_{\text{détruite}} = 3\ \text{km}^2/\text{an}",
            font_size=32, color=YELLOW,
        )
        calculs = VGroup(calc1, calc2, calc3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        calculs.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Convertissons cinq centimètres par an en zéro virgule "
                "zéro zéro zéro zéro cinq kilomètre par an : la surface "
                "créée vaut soixante mille fois zéro virgule zéro zéro zéro "
                "zéro cinq, soit trois kilomètres carrés par an. "
                "Convertissons de même sept virgule cinq centimètres par "
                "an en zéro virgule zéro zéro zéro zéro sept cinq "
                "kilomètre par an : la surface détruite vaut quarante "
                "mille fois zéro virgule zéro zéro zéro zéro sept cinq, "
                "soit encore trois kilomètres carrés par an. Les deux "
                "valeurs sont rigoureusement égales : ce calcul confirme "
                "que le rayon de la Terre reste constant."
            )
        ) as tracker:
            self.play(Write(calc1))
            self.play(Write(calc2))
            self.play(Write(calc3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calculs))

        # --- À retenir : méthode de raisonnement de synthèse --------------------
        methode = method_box(
            _bullets(
                [
                    "Étape 1 : dégager les faits (âges, profondeurs, "
                    "localisations).",
                    "Étape 2 : nommer le phénomène (expansion, subduction, "
                    "collision, coulissage, convection).",
                    "Étape 3 : enchaîner cause et conséquence (« donc », "
                    "« ce qui explique »).",
                    "Étape 4 : conclure en revenant à la question posée.",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour construire un raisonnement de synthèse en géologie, "
                "suis toujours ces quatre étapes. Un : dégage les faits, "
                "âges, profondeurs, localisations. Deux : nomme le "
                "phénomène en jeu, expansion, subduction, collision, "
                "coulissage ou convection. Trois : enchaîne cause et "
                "conséquence, avec des mots comme donc, ou ce qui explique. "
                "Quatre : conclus en revenant explicitement à la question "
                "posée au départ."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
