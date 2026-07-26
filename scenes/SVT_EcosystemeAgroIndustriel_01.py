"""
scenes/SVT_EcosystemeAgroIndustriel_01.py — Chapitre 11 (1ereC, SVT), scène 01.

§ 1.1-1.2 Introduction du chapitre : définition de l'écosystème (biotope +
biocénose + interactions, Arthur Tansley 1935, système ouvert), objectifs
pédagogiques du chapitre, puis définition du biotope (facteurs
physico-chimiques). Source : 1ereC/SVT.pdf, pages 119-120.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
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


class DefinitionEcosystemeEtBiotope(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 11 — L'écosystème naturel et l'agrosystème")
        titre.scale(0.52)
        titre.to_edge(UP)

        # --- Énoncé : contexte + objectifs du chapitre --------------------
        intro = Text(
            _wrap(
                "Tous les êtres vivants d'un même lieu vivent en relation "
                "permanente avec leur milieu : ils y puisent leur "
                "nourriture, y rejettent leurs déchets, y naissent et y "
                "meurent. Cet ensemble « milieu + êtres vivants » "
                "constitue ce que les biologistes appellent un écosystème.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dernier chapitre du programme de première C : l'écosystème "
                "naturel et l'écosystème agro-industriel. Tous les êtres "
                "vivants d'un même lieu vivent en relation permanente avec "
                "leur milieu : ils y puisent leur nourriture, y rejettent "
                "leurs déchets, y naissent et y meurent. Cet ensemble, "
                "milieu plus êtres vivants, constitue ce que les "
                "biologistes appellent un écosystème."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        objectifs_titre = Text("Objectifs de ce chapitre", font_size=26, color=YELLOW, weight="BOLD")
        objectifs_titre.next_to(titre, DOWN, buff=0.5)
        objectifs = _bullets(
            [
                "Définir écosystème, biotope, biocénose, station (exemples ivoiriens : Taï, Lamto, un étang).",
                "Construire une chaîne et un réseau alimentaires.",
                "Calculer un rendement écologique, représenter des pyramides écologiques.",
                "Expliquer les cycles du carbone et de l'azote et l'équilibre dynamique des écosystèmes.",
                "Comparer écosystème naturel et agrosystème, viser une agriculture durable.",
                "Analyser les impacts humains (déforestation, pollution, érosion).",
            ],
            font_size=19,
            width=58,
        )
        objectifs.next_to(objectifs_titre, DOWN, buff=0.35)
        groupe_obj = VGroup(objectifs_titre, objectifs)
        _fit(groupe_obj, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, vous devrez être capables de "
                "définir les notions d'écosystème, de biotope, de "
                "biocénose et de station, en les illustrant par des "
                "exemples ivoiriens comme la forêt de Taï, la savane de "
                "Lamto ou un étang ; de construire une chaîne et un réseau "
                "alimentaires ; de calculer et interpréter un rendement "
                "écologique et de représenter les pyramides écologiques ; "
                "d'expliquer les cycles du carbone et de l'azote et "
                "l'équilibre dynamique des écosystèmes ; de comparer un "
                "écosystème naturel à un agrosystème et de dégager les "
                "conditions d'une agriculture durable en Côte d'Ivoire ; "
                "et enfin d'analyser les impacts des activités humaines, "
                "déforestation, pollution, érosion, sur les écosystèmes."
            )
        ) as tracker:
            self.play(FadeIn(objectifs_titre))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(objectifs_titre), FadeOut(objectifs))

        # --- Raisonnement : la définition de l'écosystème + schéma --------
        definition = definition_box(
            Text(
                _wrap(
                    "Un écosystème est un ensemble formé par une "
                    "communauté d'êtres vivants (la biocénose) et le "
                    "milieu physico-chimique dans lequel elle vit (le "
                    "biotope), ainsi que par les interactions réciproques "
                    "qui s'établissent entre eux. Terme proposé par le "
                    "botaniste anglais Arthur Tansley en 1935.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un écosystème est un ensemble formé par une communauté "
                "d'êtres vivants, la biocénose, et le milieu "
                "physico-chimique dans lequel elle vit, le biotope, ainsi "
                "que par l'ensemble des interactions réciproques qui "
                "s'établissent entre eux. Ce terme a été proposé par le "
                "botaniste anglais Arthur Tansley, en mille neuf cent "
                "trente-cinq."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # Schéma : biotope + biocénose -> écosystème (diagramme de Venn simplifié)
        cercle_biotope = Circle(radius=1.5, color="#288073", fill_color="#E0F5F6", fill_opacity=0.85, stroke_width=3)
        cercle_biotope.shift(LEFT * 1.1)
        cercle_bioceno = Circle(radius=1.5, color="#1E5FA8", fill_color="#E3F3FF", fill_opacity=0.6, stroke_width=3)
        cercle_bioceno.shift(RIGHT * 1.1)
        label_biotope = Text("BIOTOPE\n(milieu)", font_size=20, color="#1A1A1A", weight="BOLD")
        label_biotope.move_to(cercle_biotope.get_center() + LEFT * 0.6)
        label_bioceno = Text("BIOCÉNOSE\n(êtres vivants)", font_size=20, color="#1A1A1A", weight="BOLD")
        label_bioceno.move_to(cercle_bioceno.get_center() + RIGHT * 0.6)
        label_inter = Text("interactions", font_size=16, color="#1A1A1A", weight="BOLD")
        label_inter.move_to((cercle_biotope.get_center() + cercle_bioceno.get_center()) / 2)
        schema = VGroup(cercle_biotope, cercle_bioceno, label_biotope, label_bioceno, label_inter)
        legende_schema = Text("ÉCOSYSTÈME = biotope + biocénose + interactions", font_size=22, color=YELLOW, weight="BOLD")
        groupe_schema = VGroup(schema, legende_schema).arrange(DOWN, buff=0.4)
        groupe_schema.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un écosystème est un système ouvert : il reçoit de "
                "l'énergie, le rayonnement solaire, et échange en "
                "permanence de la matière avec l'extérieur, eau de pluie, "
                "gaz atmosphériques, animaux migrateurs, sédiments. "
                "Retenez ce schéma : l'écosystème, c'est le recouvrement "
                "du biotope et de la biocénose, relié par leurs "
                "interactions constantes."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(Write(legende_schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- À retenir : le biotope --------------------------------------
        biotope_def = definition_box(
            Text(
                _wrap(
                    "Le biotope est l'ensemble des facteurs "
                    "physico-chimiques (abiotiques) du milieu de vie : le "
                    "climat (température, pluviométrie, lumière), le sol "
                    "(texture, pH, sels minéraux), l'eau et l'air.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        biotope_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voyons maintenant la première moitié de l'écosystème : le "
                "biotope. Le biotope est l'ensemble des facteurs "
                "physico-chimiques, dits abiotiques, du milieu de vie : le "
                "climat, avec la température, la pluviométrie et la "
                "lumière ; le sol, avec sa texture, son pH, ses sels "
                "minéraux ; l'eau et l'air. Le biotope est le théâtre dans "
                "lequel se déroule la vie : ses caractéristiques "
                "déterminent quelles espèces peuvent s'y installer. Un sol "
                "sableux et sec n'accueillera pas les mêmes plantes qu'un "
                "sol argileux et humide."
            )
        ) as tracker:
            self.play(FadeIn(biotope_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(biotope_def))
