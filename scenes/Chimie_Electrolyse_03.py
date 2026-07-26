"""
scenes/Chimie_Electrolyse_03.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 03.

§ 3. Sens des porteurs de charge et réactions aux électrodes. Distinction
entre le déplacement des électrons (dans les fils métalliques et les
électrodes uniquement) et la double migration des ions dans l'électrolyte
(cations vers la cathode, anions vers l'anode). Réactions génériques :
anode = oxydation (Réd → Ox + n e⁻), cathode = réduction
(Ox + n e⁻ → Réd). Règle : les électrons n'apparaissent jamais dans
l'équation bilan (ils doivent être éliminés par combinaison des deux
demi-équations). Piège : en électrolyse l'anode est le pôle + (inverse de
la pile où l'anode est le pôle −).
Source : 1ereC/Chimie.pdf, chapitre 14, pages 136-137.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    LIGHT_GRAY,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, warning_box


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


def _schema_migrations():
    """Schéma du montage avec flèches indiquant le sens des électrons dans
    les fils et le sens de migration des cations/anions dans l'électrolyte."""
    largeur, hauteur = 3.6, 2.0
    cuve = Rectangle(width=largeur, height=hauteur, color=LIGHT_GRAY, stroke_width=3)
    cuve.move_to([0, -0.9, 0])

    solution = Rectangle(width=largeur - 0.1, height=hauteur - 0.3, fill_color=BLUE, fill_opacity=0.14, stroke_width=0)
    solution.move_to(cuve.get_bottom() + UP * (hauteur - 0.3) / 2 + UP * 0.1)

    electrode_a = Rectangle(width=0.22, height=hauteur + 0.5, fill_color=RED, fill_opacity=0.85, stroke_width=1)
    electrode_a.move_to(cuve.get_center() + RIGHT * 1.3 + UP * 0.35)
    electrode_c = Rectangle(width=0.22, height=hauteur + 0.5, fill_color=BLUE, fill_opacity=0.85, stroke_width=1)
    electrode_c.move_to(cuve.get_center() + LEFT * 1.3 + UP * 0.35)

    label_a = Text("ANODE (+)", font_size=15, color=RED, weight="BOLD")
    label_a.next_to(electrode_a, UP, buff=0.6)
    label_c = Text("CATHODE (−)", font_size=15, color=BLUE, weight="BOLD")
    label_c.next_to(electrode_c, UP, buff=0.6)

    # Fils + flèches d'électrons : de la cathode vers le générateur (-),
    # du générateur (+) vers l'anode... électrons réels : du générateur (-)
    # vers la cathode, et de l'anode vers le générateur (+).
    fil_c = Line(electrode_c.get_top(), electrode_c.get_top() + UP * 0.9, color=YELLOW, stroke_width=2)
    fil_a = Line(electrode_a.get_top(), electrode_a.get_top() + UP * 0.9, color=YELLOW, stroke_width=2)

    fleche_e_c = Arrow(
        fil_c.get_top() + UP * 0.05, electrode_c.get_top() + UP * 0.15,
        color=YELLOW, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.35,
    )
    label_e_c = Text("e⁻", font_size=16, color=YELLOW, weight="BOLD")
    label_e_c.next_to(fleche_e_c, LEFT, buff=0.08)

    fleche_e_a = Arrow(
        electrode_a.get_top() + UP * 0.15, fil_a.get_top() + UP * 0.05,
        color=YELLOW, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.35,
    )
    label_e_a = Text("e⁻", font_size=16, color=YELLOW, weight="BOLD")
    label_e_a.next_to(fleche_e_a, RIGHT, buff=0.08)

    # Migration des ions dans l'électrolyte : cations (+) vers la cathode
    # (gauche), anions (−) vers l'anode (droite).
    fleche_cation = Arrow(
        [0.5, -1.1, 0], [-0.85, -1.1, 0], color=RED, stroke_width=3, buff=0,
        max_tip_length_to_length_ratio=0.15,
    )
    label_cation = Text("cations (+)", font_size=14, color=RED)
    label_cation.next_to(fleche_cation, UP, buff=0.06)

    fleche_anion = Arrow(
        [-0.5, -0.5, 0], [0.85, -0.5, 0], color=BLUE, stroke_width=3, buff=0,
        max_tip_length_to_length_ratio=0.15,
    )
    label_anion = Text("anions (−)", font_size=14, color=BLUE)
    label_anion.next_to(fleche_anion, UP, buff=0.06)

    return VGroup(
        cuve, solution,
        electrode_a, electrode_c, label_a, label_c,
        fil_c, fil_a, fleche_e_c, label_e_c, fleche_e_a, label_e_a,
        fleche_cation, label_cation, fleche_anion, label_anion,
    )


class SensPorteursChargeReactionsElectrodes(NotionScene):
    def construct(self):
        titre = scene_title("14.3 Sens des porteurs de charge et réactions aux électrodes")
        titre.scale(0.38)
        titre.to_edge(UP)

        # --- Énoncé : deux porteurs de charge différents --------------------------
        intro = Text(
            _wrap(
                "Le courant électrique circule dans TOUT le circuit, mais "
                "les porteurs de charge ne sont pas les mêmes partout. "
                "Distinguons les fils et l'électrolyte.",
                width=58,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le courant électrique circule dans tout le circuit "
                "d'électrolyse, mais les porteurs de charge qui "
                "l'assurent ne sont pas les mêmes selon l'endroit du "
                "circuit. Distinguons bien les fils métalliques de "
                "l'électrolyte."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : schéma des migrations ---------------------------------
        entete_schema = Text("Deux sens de circulation à ne pas confondre", font_size=21, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.3)

        schema = _schema_migrations()
        schema.next_to(entete_schema, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Dans les fils métalliques et à l'intérieur même des "
                "électrodes, ce sont des électrons qui se déplacent : ils "
                "sortent du pôle négatif du générateur pour rejoindre la "
                "cathode, et ils quittent l'anode pour retourner vers le "
                "pôle positif du générateur. Dans l'électrolyte, en "
                "revanche, il n'y a pas d'électrons libres : ce sont les "
                "ions eux-mêmes qui migrent, dans une double migration. "
                "Les cations, chargés positivement, migrent vers la "
                "cathode. Les anions, chargés négativement, migrent vers "
                "l'anode."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(schema))

        # --- Exemple traité : réactions génériques aux électrodes -----------------
        entete_reac = Text("Réactions génériques aux électrodes", font_size=21, color=YELLOW, weight="BOLD")
        entete_reac.next_to(titre, DOWN, buff=0.35)

        anode_gen = VGroup(
            Text("À l'anode (oxydation) :", font_size=20, color=RED, weight="BOLD"),
            MathTex(r"\text{Réd} \longrightarrow \text{Ox} + n\,e^-", font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.25)

        cathode_gen = VGroup(
            Text("À la cathode (réduction) :", font_size=20, color=BLUE, weight="BOLD"),
            MathTex(r"\text{Ox} + n\,e^- \longrightarrow \text{Réd}", font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.25)

        reactions = VGroup(anode_gen, cathode_gen).arrange(DOWN, buff=0.6)
        reactions.next_to(entete_reac, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On peut maintenant écrire les réactions génériques aux "
                "électrodes. À l'anode, siège de l'oxydation, un "
                "réducteur cède des électrons : Réd donne Ox, plus n "
                "électrons. À la cathode, siège de la réduction, un "
                "oxydant capte ces électrons : Ox, plus n électrons, "
                "donne Réd."
            )
        ) as tracker:
            self.play(FadeIn(entete_reac))
            self.play(Write(anode_gen))
            self.play(Write(cathode_gen))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_reac), FadeOut(reactions))

        # --- À retenir : règle des électrons dans le bilan ------------------------
        regle = _bullets(
            [
                "Pour obtenir l'ÉQUATION-BILAN de l'électrolyse, on "
                "additionne les deux demi-équations, après les avoir "
                "multipliées si besoin pour égaliser le nombre "
                "d'électrons échangés ;",
                "les électrons se simplifient alors totalement : ils "
                "n'apparaissent JAMAIS dans une équation-bilan.",
            ],
            font_size=20,
            width=54,
        )
        entete_regle = Text("Règle à retenir", font_size=22, color="#288073", weight="BOLD")
        entete_regle.next_to(titre, DOWN, buff=0.4)
        regle.next_to(entete_regle, DOWN, buff=0.35)
        _fit(VGroup(entete_regle, regle), entete_regle.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Retenons cette règle essentielle. Pour obtenir "
                "l'équation-bilan complète de l'électrolyse, on additionne "
                "les deux demi-équations, en les multipliant au préalable "
                "si nécessaire, pour que le nombre d'électrons échangés à "
                "l'anode soit exactement égal à celui échangé à la "
                "cathode. Les électrons se simplifient alors "
                "complètement : ils ne doivent jamais apparaître dans "
                "l'équation-bilan finale."
            )
        ) as tracker:
            self.play(FadeIn(entete_regle))
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_regle), FadeOut(regle))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège fréquent : en ÉLECTROLYSE, l'anode est le pôle "
                    "POSITIF du générateur. C'est l'INVERSE de la pile, où "
                    "l'anode (siège de l'oxydation également) est le pôle "
                    "NÉGATIF. Ne jamais transposer machinalement la "
                    "polarité d'une pile à une électrolyse.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Attention à un piège très fréquent. En électrolyse, "
                "l'anode est le pôle positif du générateur. C'est "
                "exactement l'inverse de ce qui se passe dans une pile, "
                "où l'anode, également siège de l'oxydation, est le pôle "
                "négatif. Ne transposez jamais machinalement la polarité "
                "d'une pile à une électrolyse : seule l'association anode "
                "égale oxydation reste vraie dans les deux cas."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
