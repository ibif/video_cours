"""
scenes/Chimie_Electrolyse_08.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 08.

§ 8. Électrolyse à électrode soluble : anode de cuivre + raffinage du
cuivre. Expérience : anode de cuivre (au lieu de graphite) et cathode de
cuivre, dans une solution de sulfate de cuivre II. Observations : l'anode
s'amincit, la cathode s'épaissit, la concentration en Cu²⁺ reste
constante, aucun gaz ne se dégage. Demi-équations (anode : Cu → Cu²⁺ +
2e⁻ ; cathode : Cu²⁺ + 2e⁻ → Cu) et bilan global : transfert net de
cuivre de l'anode vers la cathode, sans consommation nette d'électrolyte.
Application industrielle : le raffinage électrolytique du cuivre (anode
en cuivre impur issu de la métallurgie, cathode en cuivre pur, boues
anodiques contenant les métaux précieux Ag/Au qui ne s'oxydent pas et
tombent au fond de la cuve), schéma complet.
Source : 1ereC/Chimie.pdf, chapitre 14, pages 141-142.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GRAY,
    GOLD,
    LEFT,
    LIGHT_GRAY,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
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


def _schema_anode_soluble():
    """Cuve à électrolyse avec anode de cuivre (qui s'amincit) et cathode
    de cuivre (qui s'épaissit), sans dégagement gazeux."""
    largeur, hauteur = 3.2, 1.8
    cuve = Rectangle(width=largeur, height=hauteur, color=LIGHT_GRAY, stroke_width=3)
    cuve.move_to([0, -0.9, 0])

    solution = Rectangle(width=largeur - 0.1, height=hauteur - 0.2, fill_color=BLUE, fill_opacity=0.22, stroke_width=0)
    solution.move_to(cuve.get_center())

    electrode_a = Rectangle(width=0.14, height=1.5, fill_color=ORANGE, fill_opacity=0.9, stroke_width=1)
    electrode_a.move_to(cuve.get_center() + RIGHT * 1.0)
    electrode_c = Rectangle(width=0.34, height=1.5, fill_color=ORANGE, fill_opacity=0.9, stroke_width=1)
    electrode_c.move_to(cuve.get_center() + LEFT * 1.0)

    label_a = Text("anode Cu\n(s'amincit)", font_size=13, color=ORANGE)
    label_a.next_to(electrode_a, UP, buff=0.15)
    label_c = Text("cathode Cu\n(s'épaissit)", font_size=13, color=ORANGE)
    label_c.next_to(electrode_c, UP, buff=0.15)

    fleche = Line(electrode_a.get_center() + UP * 1.3, electrode_c.get_center() + UP * 1.3, color=YELLOW, stroke_width=2)
    label_transfert = Text("transfert net de cuivre", font_size=13, color=YELLOW)
    label_transfert.next_to(fleche, UP, buff=0.08)

    label_anode = Text("(+)", font_size=13, color=RED)
    label_anode.next_to(electrode_a, DOWN, buff=0.6)
    label_cathode = Text("(−)", font_size=13, color=BLUE)
    label_cathode.next_to(electrode_c, DOWN, buff=0.6)

    return VGroup(
        cuve, solution, electrode_a, electrode_c, label_a, label_c,
        fleche, label_transfert, label_anode, label_cathode,
    )


def _schema_raffinage():
    """Schéma du raffinage électrolytique du cuivre : anode en cuivre
    impur, cathode en cuivre pur, boues anodiques (Ag/Au) qui tombent au
    fond de la cuve."""
    largeur, hauteur = 4.4, 2.0
    cuve = Rectangle(width=largeur, height=hauteur, color=LIGHT_GRAY, stroke_width=3)
    cuve.move_to([0, -1.0, 0])

    solution = Rectangle(width=largeur - 0.1, height=hauteur - 0.2, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
    solution.move_to(cuve.get_center())
    label_sol = Text("CuSO₄ (aq)", font_size=14, color=WHITE)
    label_sol.move_to(cuve.get_top() + DOWN * 0.25)

    electrode_a = Rectangle(width=0.22, height=1.5, fill_color=GRAY, fill_opacity=0.9, stroke_width=1)
    electrode_a.move_to(cuve.get_center() + RIGHT * 1.3 + UP * 0.15)
    electrode_c = Rectangle(width=0.22, height=1.5, fill_color=ORANGE, fill_opacity=0.95, stroke_width=1)
    electrode_c.move_to(cuve.get_center() + LEFT * 1.3 + UP * 0.15)

    label_a = Text("anode : Cu IMPUR", font_size=13, color=GRAY, weight="BOLD")
    label_a.next_to(electrode_a, UP, buff=0.5)
    label_c = Text("cathode : Cu PUR", font_size=13, color=ORANGE, weight="BOLD")
    label_c.next_to(electrode_c, UP, buff=0.5)

    boues = VGroup(*[
        Circle(radius=0.05, fill_color=GOLD, fill_opacity=1, stroke_width=0)
        .move_to(electrode_a.get_bottom() + [0.05 * ((-1) ** i), -0.25 - 0.08 * (i % 3), 0])
        for i in range(7)
    ])
    label_boues = Text("boues anodiques (Ag, Au)", font_size=12, color=GOLD)
    label_boues.next_to(boues, DOWN, buff=0.1)

    label_anode = Text("(+)", font_size=13, color=RED)
    label_anode.next_to(electrode_a, DOWN, buff=1.0)
    label_cathode = Text("(−)", font_size=13, color=BLUE)
    label_cathode.next_to(electrode_c, DOWN, buff=1.0)

    return VGroup(
        cuve, solution, label_sol,
        electrode_a, electrode_c, label_a, label_c,
        boues, label_boues, label_anode, label_cathode,
    )


class ElectrodeSolubleRaffinageCuivre(NotionScene):
    def construct(self):
        titre = scene_title("14.8 Électrode soluble : anode de cuivre et raffinage")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : le montage ---------------------------------------------------
        intro = Text(
            _wrap(
                "Remplaçons les électrodes de graphite par deux électrodes "
                "de cuivre, toujours dans une solution de sulfate de "
                "cuivre II. Que change ce choix de matériau ?",
                width=58,
            ),
            font_size=21,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Remplaçons maintenant les électrodes inertes de graphite "
                "par deux électrodes de cuivre, toujours plongées dans une "
                "solution de sulfate de cuivre deux. Qu'est-ce que ce "
                "simple choix de matériau va changer ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : observations + schéma -----------------------------------
        entete_obs = Text("Observations expérimentales", font_size=21, color=YELLOW, weight="BOLD")
        entete_obs.next_to(titre, DOWN, buff=0.3)

        schema = _schema_anode_soluble()
        schema.next_to(entete_obs, DOWN, buff=0.35).shift(LEFT * 2.6)

        observations = _bullets(
            [
                "l'ANODE de cuivre s'AMINCIT progressivement ;",
                "la CATHODE de cuivre s'ÉPAISSIT progressivement ;",
                "la concentration en Cu²⁺ reste CONSTANTE ;",
                "AUCUN gaz ne se dégage à aucune des deux électrodes.",
            ],
            width=32,
        )
        observations.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "On observe que l'anode de cuivre s'amincit "
                "progressivement, que la cathode de cuivre s'épaissit "
                "progressivement, que la concentration en ions cuivre "
                "deux plus de la solution reste constante, et surtout, "
                "qu'aucun gaz ne se dégage à aucune des deux électrodes."
            )
        ) as tracker:
            self.play(FadeIn(entete_obs))
            self.play(FadeIn(schema))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_obs), FadeOut(schema), FadeOut(observations))

        # --- Exemple traité : demi-équations et bilan --------------------------------
        entete_eq = Text("Interprétation : l'anode elle-même s'oxyde", font_size=20, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.3)

        anode_eq = VGroup(
            Text("Anode SOLUBLE (le cuivre métal s'oxyde) :", font_size=17, color=RED, weight="BOLD"),
            MathTex(r"Cu \longrightarrow Cu^{2+} + 2\,e^-", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        cathode_eq = VGroup(
            Text("Cathode (Cu²⁺ redéposé) :", font_size=17, color=BLUE, weight="BOLD"),
            MathTex(r"Cu^{2+} + 2\,e^- \longrightarrow Cu", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        bilan = VGroup(
            Text("Bilan global : simple transfert de matière", font_size=17, color=YELLOW, weight="BOLD"),
            MathTex(r"Cu_{(anode)} \longrightarrow Cu_{(cathode)}", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        groupe_eq = VGroup(anode_eq, cathode_eq, bilan).arrange(DOWN, buff=0.3)
        groupe_eq.next_to(entete_eq, DOWN, buff=0.3)
        _fit(groupe_eq, entete_eq.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "L'électrode de cuivre à l'anode n'est pas inerte : "
                "puisque le cuivre s'oxyde plus facilement que l'eau, "
                "c'est le métal de l'électrode lui-même qui est oxydé : "
                "Cu donne Cu deux plus, plus deux électrons. À la "
                "cathode, les ions cuivre deux plus, apportés en même "
                "quantité par l'anode, sont réduits et se redéposent. Le "
                "bilan global n'est donc rien d'autre qu'un transfert net "
                "de cuivre métallique de l'anode vers la cathode, sans "
                "aucune consommation nette d'électrolyte : voilà pourquoi "
                "la concentration en Cu deux plus reste constante et "
                "qu'aucun gaz ne se dégage."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(anode_eq))
            self.play(Write(cathode_eq))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(groupe_eq))

        # --- À retenir : application industrielle (raffinage) ------------------------
        entete_raff = Text("Application : le raffinage électrolytique du cuivre", font_size=19, color="#288073", weight="BOLD")
        entete_raff.next_to(titre, DOWN, buff=0.3)

        schema_raff = _schema_raffinage()
        schema_raff.scale(0.85)
        schema_raff.next_to(entete_raff, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Ce principe de transfert par anode soluble est exploité "
                "industriellement pour purifier le cuivre : c'est le "
                "raffinage électrolytique. On place à l'anode du cuivre "
                "impur, issu de la métallurgie, et à la cathode une fine "
                "feuille de cuivre pur. Le courant fait passer le cuivre, "
                "et lui seul, de l'anode vers la cathode, qui s'épaissit "
                "en cuivre très pur, à plus de 99,9 pour cent. Les "
                "métaux précieux comme l'argent et l'or, présents en "
                "faible quantité dans le cuivre impur, ne s'oxydent pas à "
                "l'anode : ils se détachent et tombent au fond de la cuve, "
                "formant les boues anodiques, ensuite récupérées et "
                "revendues séparément."
            )
        ) as tracker:
            self.play(FadeIn(entete_raff))
            self.play(FadeIn(schema_raff))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_raff), FadeOut(schema_raff), FadeOut(titre))
