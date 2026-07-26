"""
scenes/Chimie_Electrolyse_02.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 02.

§ 2. Pile vs électrolyse — montage et vocabulaire. Tableau comparatif
entre une pile (réaction spontanée, conversion d'énergie chimique en
énergie électrique, le générateur c'est la pile elle-même, sens de
réaction spontané) et une électrolyse (réaction forcée, conversion
d'énergie électrique en énergie chimique, générateur externe imposant le
sens, sens de réaction imposé par le générateur, contraire au sens
spontané). Définitions de l'anode (pôle + du générateur en électrolyse,
siège de l'oxydation) et de la cathode (pôle − du générateur, siège de la
réduction), moyen mnémotechnique. Schéma complet et légendé du montage
d'électrolyse.
Source : 1ereC/Chimie.pdf, chapitre 14, pages 135-136.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    LIGHT_GRAY,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


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


def _tableau_comparatif():
    """Tableau comparatif pile / électrolyse, construit avec Line/Text."""
    col1_x, col2_x, col3_x = -3.6, -0.1, 3.4
    ligne_titre = VGroup(
        Text("Critère", font_size=18, color=YELLOW, weight="BOLD"),
        Text("Pile", font_size=18, color=GREEN, weight="BOLD"),
        Text("Électrolyse", font_size=18, color=ORANGE, weight="BOLD"),
    )
    ligne_titre[0].move_to([col1_x, 1.35, 0])
    ligne_titre[1].move_to([col2_x, 1.35, 0])
    ligne_titre[2].move_to([col3_x, 1.35, 0])

    lignes_txt = [
        ("Sens de la\nréaction", "spontané", "forcé, imposé"),
        ("Conversion\nd'énergie", "chimique → électrique", "électrique → chimique"),
        ("Rôle du\ngénérateur", "la pile EST le\ngénérateur", "générateur EXTERNE\nqui impose le sens"),
    ]
    lignes = VGroup()
    y = 0.6
    for crit, pile, electro in lignes_txt:
        l = VGroup(
            Text(crit, font_size=16, color=WHITE),
            Text(pile, font_size=16, color=WHITE),
            Text(electro, font_size=16, color=WHITE),
        )
        l[0].move_to([col1_x, y, 0])
        l[1].move_to([col2_x, y, 0])
        l[2].move_to([col3_x, y, 0])
        lignes.add(l)
        y -= 0.85

    trait_h = Line([-5.0, 1.0, 0], [5.0, 1.0, 0], color=LIGHT_GRAY, stroke_width=1.5)
    trait_v1 = Line([-1.9, 1.8, 0], [-1.9, -2.0, 0], color=LIGHT_GRAY, stroke_width=1)
    trait_v2 = Line([1.7, 1.8, 0], [1.7, -2.0, 0], color=LIGHT_GRAY, stroke_width=1)

    return VGroup(ligne_titre, lignes, trait_h, trait_v1, trait_v2)


def _schema_montage_electrolyse():
    """Schéma complet du montage d'électrolyse : cuve, deux électrodes de
    graphite, générateur avec pôles + et −, fils de connexion — construit
    uniquement avec des primitives Manim de base."""
    largeur, hauteur = 3.4, 2.0
    cuve = Rectangle(width=largeur, height=hauteur, color=LIGHT_GRAY, stroke_width=3)
    cuve.move_to([0, -0.9, 0])

    solution = Rectangle(width=largeur - 0.1, height=hauteur - 0.3, fill_color=BLUE, fill_opacity=0.16, stroke_width=0)
    solution.move_to(cuve.get_bottom() + UP * (hauteur - 0.3) / 2 + UP * 0.1)
    label_sol = Text("électrolyte", font_size=15, color=WHITE)
    label_sol.move_to(cuve.get_bottom() + UP * 0.3)

    electrode_a = Rectangle(width=0.22, height=hauteur + 0.5, fill_color=RED, fill_opacity=0.85, stroke_width=1)
    electrode_a.move_to(cuve.get_center() + RIGHT * 1.1 + UP * 0.35)
    electrode_c = Rectangle(width=0.22, height=hauteur + 0.5, fill_color=BLUE, fill_opacity=0.85, stroke_width=1)
    electrode_c.move_to(cuve.get_center() + LEFT * 1.1 + UP * 0.35)

    label_a = Text("ANODE (A)", font_size=15, color=RED, weight="BOLD")
    label_a.next_to(electrode_a, UP, buff=0.12)
    label_c = Text("CATHODE (C)", font_size=15, color=BLUE, weight="BOLD")
    label_c.next_to(electrode_c, UP, buff=0.12)

    barre_longue = Line([0.9, 2.55, 0], [0.9, 2.95, 0], color=WHITE, stroke_width=2)
    barre_courte = Line([-0.9, 2.6, 0], [-0.9, 2.9, 0], color=WHITE, stroke_width=6)
    generateur = VGroup(barre_longue, barre_courte)
    label_plus = Text("pôle +", font_size=16, color=RED, weight="BOLD")
    label_plus.next_to(barre_longue, UP, buff=0.08)
    label_moins = Text("pôle −", font_size=16, color=BLUE, weight="BOLD")
    label_moins.next_to(barre_courte, UP, buff=0.08)

    fil_a = Line(electrode_a.get_top(), [0.9, 2.75, 0], color=YELLOW, stroke_width=2)
    fil_c = Line(electrode_c.get_top(), [-0.9, 2.75, 0], color=YELLOW, stroke_width=2)

    return VGroup(
        cuve, solution, label_sol,
        electrode_a, electrode_c, label_a, label_c,
        generateur, label_plus, label_moins, fil_a, fil_c,
    )


class PileVsElectrolyseMontageVocabulaire(NotionScene):
    def construct(self):
        titre = scene_title("14.2 Pile ou électrolyse ? Montage et vocabulaire")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : la question -------------------------------------------------
        intro = Text(
            _wrap(
                "Une pile et une électrolyse ont toutes deux deux "
                "électrodes plongées dans un électrolyte. Mais leur "
                "fonctionnement est en réalité opposé. Comparons-les.",
                width=58,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une pile et une électrolyse se ressemblent beaucoup au "
                "premier regard : deux électrodes plongées dans un "
                "électrolyte, un courant qui circule. Mais leur "
                "fonctionnement est en réalité opposé. Comparons-les "
                "précisément."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : tableau comparatif ------------------------------------
        entete_tab = Text("Tableau comparatif pile / électrolyse", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.3)

        tableau = _tableau_comparatif()
        tableau.scale(0.85)
        tableau.next_to(entete_tab, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Dans une pile, la réaction d'oxydoréduction est "
                "spontanée : elle se produit toute seule, dès qu'on "
                "réalise le montage, et convertit de l'énergie chimique en "
                "énergie électrique. La pile est elle-même son propre "
                "générateur. Dans une électrolyse, au contraire, la "
                "réaction est forcée : elle ne se produit que parce qu'un "
                "générateur externe impose sa tension, et convertit cette "
                "fois de l'énergie électrique en énergie chimique. C'est "
                "le générateur, et lui seul, qui impose le sens de la "
                "réaction — un sens qui est en général contraire au sens "
                "spontané."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : le schéma du montage --------------------------------
        entete_schema = Text("Le montage d'une électrolyse", font_size=22, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.3)

        schema = _schema_montage_electrolyse()
        schema.scale(0.95)
        schema.next_to(entete_schema, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le montage type d'une électrolyse : une cuve "
                "contenant l'électrolyte, deux électrodes reliées à un "
                "générateur de tension continue. L'électrode reliée au "
                "pôle plus du générateur s'appelle l'anode. L'électrode "
                "reliée au pôle moins du générateur s'appelle la cathode."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(Write(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(schema))

        # --- À retenir : définitions anode / cathode ------------------------------
        def_anode = definition_box(
            Text(
                _wrap(
                    "En électrolyse, l'ANODE est l'électrode reliée au pôle "
                    "POSITIF du générateur : c'est le siège de "
                    "l'OXYDATION.",
                    width=44,
                ),
                font_size=22,
            ),
        )
        def_anode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons précisément ces deux définitions. En "
                "électrolyse, l'anode est l'électrode reliée au pôle "
                "positif du générateur, et c'est le siège de l'oxydation."
            )
        ) as tracker:
            self.play(FadeIn(def_anode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_anode))

        def_cathode = definition_box(
            Text(
                _wrap(
                    "En électrolyse, la CATHODE est l'électrode reliée au "
                    "pôle NÉGATIF du générateur : c'est le siège de la "
                    "RÉDUCTION.",
                    width=44,
                ),
                font_size=22,
            ),
        )
        def_cathode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La cathode, elle, est l'électrode reliée au pôle négatif "
                "du générateur, et c'est le siège de la réduction."
            )
        ) as tracker:
            self.play(FadeIn(def_cathode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_cathode))

        # --- Moyen mnémotechnique -------------------------------------------------
        mnemo = _bullets(
            [
                "« ANODE » et « OXYDATION » : deux voyelles qui se "
                "correspondent (A → OX).",
                "« CATHODE » et « RÉDUCTION » : deux mots qui commencent "
                "par une consonne dure (C → RED).",
                "ATTENTION : cette association ANODE = OXYDATION reste "
                "vraie dans TOUS les cas (pile ou électrolyse) — seule "
                "la POLARITÉ de l'anode change entre les deux !",
            ],
            font_size=19,
            width=54,
        )
        entete_mnemo = Text("Moyen mnémotechnique", font_size=22, color=GREEN, weight="BOLD")
        entete_mnemo.next_to(titre, DOWN, buff=0.4)
        mnemo.next_to(entete_mnemo, DOWN, buff=0.3)
        _fit(VGroup(entete_mnemo, mnemo), entete_mnemo.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Pour ne jamais confondre anode et cathode, voici un "
                "moyen mnémotechnique. Anode et oxydation vont toujours "
                "ensemble, que l'on soit dans une pile ou dans une "
                "électrolyse. Cathode et réduction vont toujours ensemble. "
                "Ce qui change entre pile et électrolyse, ce n'est jamais "
                "cette association, mais uniquement la polarité de "
                "l'anode : positive en électrolyse, négative dans une "
                "pile."
            )
        ) as tracker:
            self.play(FadeIn(entete_mnemo))
            self.play(FadeIn(mnemo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_mnemo), FadeOut(mnemo), FadeOut(titre))
