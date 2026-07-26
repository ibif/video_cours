"""
scenes/SVT_EchangesIonsSol_06.py — Chapitre 8 (1ereD, SVT), scène 06.

§ 8.3.1-8.3.2 Les poils absorbants et le trajet des ions : les zones de la
jeune racine, définition du poil absorbant, propriété (surface d'échange
démultipliée), trajet des ions jusqu'au xylème (sève brute), attention à
la confusion sève brute / sève élaborée. Source : 1ereD/SVT.pdf,
pages 109-110.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class PoilsAbsorbantsEtTrajetDesIons(NotionScene):
    def construct(self):
        titre = scene_title("8.3 — Poils absorbants et trajet des ions")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : les zones de la jeune racine --------------------------
        intro = Text(
            _wrap(
                "L'extrémité d'une jeune racine n'est pas uniforme : de la "
                "pointe vers le haut, elle présente plusieurs zones aux "
                "rôles bien distincts.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'extrémité d'une jeune racine n'est pas uniforme : de la "
                "pointe vers le haut, elle présente plusieurs zones aux "
                "rôles bien distincts. Voyons lesquelles, avant de "
                "chercher où se fait l'absorption."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # Schéma : racine verticale divisée en 5 zones (de bas en haut)
        zones = [
            ("coiffe", "protège la pointe", GREEN),
            ("zone de croissance", "division cellulaire active", GREEN),
            ("zone d'élongation", "cellules s'allongent", GREEN),
            ("zone pilifère", "poils absorbants", ORANGE),
            ("zone de conduction", "tissus vers la tige", GREEN),
        ]
        segs = VGroup()
        for nom, role, color in zones:
            rect = Rectangle(width=0.8, height=0.9, color=color, fill_color=color, fill_opacity=0.25)
            segs.add(rect)
        segs.arrange(UP, buff=0.05)
        segs.move_to(RIGHT * 3.0)

        labels = VGroup()
        for rect, (nom, role, color) in zip(segs, zones):
            lbl = Text(f"{nom} — {role}", font_size=17, color=WHITE)
            lbl.next_to(rect, LEFT, buff=0.3)
            fleche = Arrow(lbl.get_right(), rect.get_left(), buff=0.05, stroke_width=2, color=WHITE)
            labels.add(VGroup(lbl, fleche))

        # petits poils sur la zone pilifère (4e segment)
        zone_pilifere_rect = segs[3]
        poils = VGroup(
            *[
                Line(
                    zone_pilifere_rect.get_right() + UP * (0.3 - 0.15 * i),
                    zone_pilifere_rect.get_right() + UP * (0.3 - 0.15 * i) + RIGHT * 0.35,
                    color=ORANGE,
                    stroke_width=2,
                )
                for i in range(5)
            ]
        )

        schema_racine = VGroup(segs, labels, poils)
        schema_racine.scale(0.85)
        schema_racine.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "De la pointe vers le haut : la coiffe, qui protège la "
                "pointe de la racine ; la zone de croissance, où les "
                "cellules se divisent activement ; la zone d'élongation, "
                "où les cellules s'allongent ; la zone pilifère, couverte "
                "de fins poils absorbants ; et enfin la zone de "
                "conduction, avec les tissus conducteurs qui relient la "
                "racine à la tige."
            )
        ) as tracker:
            self.play(FadeIn(schema_racine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_racine))

        # --- Raisonnement : définition + propriété du poil absorbant -------
        def_poil = definition_box(
            Text(
                _wrap(
                    "Un poil absorbant est une élongation d'une cellule "
                    "de l'épiderme (rhizoderme), dans la zone pilifère. "
                    "Fin, il s'insinue entre les particules du sol et "
                    "baigne dans la solution du sol. C'est le siège de "
                    "l'essentiel de l'absorption de l'eau et des ions.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_poil.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un poil absorbant est une élongation d'une cellule de "
                "l'épiderme de la racine, appelé rhizoderme, situé dans la "
                "zone pilifère. Très fin, il s'insinue entre les "
                "particules du sol et baigne dans la solution du sol. "
                "C'est le siège de l'essentiel de l'absorption de l'eau et "
                "des ions."
            )
        ) as tracker:
            self.play(FadeIn(def_poil))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_poil))

        prop_poil = property_box(
            Text(
                _wrap(
                    "Les poils absorbants sont extrêmement nombreux "
                    "(plusieurs centaines par mm²), ils multiplient "
                    "considérablement la surface d'échange (jusqu'à "
                    "10-20 fois la surface de la racine nue). Éphémères, "
                    "renouvelés en permanence, la zone pilifère « voyage » "
                    "dans le sol au contact de zones non épuisées.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        prop_poil.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "C'est une adaptation remarquable : les poils absorbants "
                "sont extrêmement nombreux, plusieurs centaines par "
                "millimètre carré, et multiplient considérablement la "
                "surface d'échange, jusqu'à dix à vingt fois la surface de "
                "la racine nue. Ils sont aussi éphémères, renouvelés en "
                "permanence : la zone pilifère progresse ainsi dans le "
                "sol, au contact de zones toujours non épuisées en "
                "éléments minéraux."
            )
        ) as tracker:
            self.play(FadeIn(prop_poil))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_poil))

        # --- Exemple traité : le trajet des ions jusqu'aux feuilles ---------
        etapes = ["Poil absorbant", "Parenchyme\ncortical", "Cylindre\ncentral", "Xylème\n(sève brute)", "Tige, feuilles"]
        boites = VGroup()
        for etape in etapes:
            rect = Rectangle(width=1.9, height=0.9, color=ORANGE, fill_color=ORANGE, fill_opacity=0.2)
            txt = Text(etape, font_size=16, color=WHITE).move_to(rect.get_center())
            boites.add(VGroup(rect, txt))
        boites.arrange(RIGHT, buff=0.55)

        trajet_titre = Text("Le trajet des ions absorbés", font_size=26, color=YELLOW, weight="BOLD")
        trajet_titre.next_to(titre, DOWN, buff=0.5)
        boites.next_to(trajet_titre, DOWN, buff=0.6)
        fleches = VGroup(
            *[
                Arrow(boites[i].get_right(), boites[i + 1].get_left(), buff=0.05, color=WHITE, stroke_width=3)
                for i in range(len(boites) - 1)
            ]
        )
        schema_trajet = VGroup(boites, fleches)
        schema_trajet.scale(0.85)
        schema_trajet.next_to(trajet_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fois dans un poil absorbant, les ions franchissent le "
                "parenchyme cortical, c'est-à-dire l'écorce de la racine, "
                "puis gagnent le cylindre central, où ils rejoignent le "
                "xylème, les vaisseaux ligneux. Ils sont alors entraînés "
                "par la sève brute, mélange d'eau et de sels minéraux, qui "
                "monte vers la tige et les feuilles. Là, en pleine "
                "photosynthèse, les ions sont utilisés : l'azote pour "
                "fabriquer des protéines, le magnésium pour la "
                "chlorophylle, le phosphore pour l'ATP et les acides "
                "nucléiques."
            )
        ) as tracker:
            self.play(FadeIn(trajet_titre))
            self.play(FadeIn(schema_trajet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(trajet_titre), FadeOut(schema_trajet))

        # --- Piège à éviter : sève brute ≠ sève élaborée ---------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Les ions minéraux circulent dans la sève brute "
                    "(xylème, montante). La sève élaborée (riche en "
                    "saccharose, fabriquée par les feuilles) circule dans "
                    "le phloème, et redescend. « Les sels minéraux "
                    "montent par la sève élaborée » est une erreur "
                    "classique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à une confusion très fréquente. Les ions "
                "minéraux circulent dans la sève brute, montante, dans le "
                "xylème. La sève élaborée, riche en saccharose et "
                "fabriquée par les feuilles, circule elle dans le phloème, "
                "et redescend vers le reste de la plante. Écrire que les "
                "sels minéraux montent par la sève élaborée est une "
                "erreur classique à éviter absolument."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
