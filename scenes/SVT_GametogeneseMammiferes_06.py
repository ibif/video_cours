"""
scenes/SVT_GametogeneseMammiferes_06.py — Chapitre 3 (1ereC, SVT), scène 06.

Comparaison spermatogenèse / ovogenèse : grand tableau de synthèse (14
critères, scindé en deux sous-tableaux de 7 pour tenir à l'écran — voir
le garde-fou d'auto-scale utilisé dans SVT_FonctionsGonades_09.py) et
schéma comparatif (mâle : 4 gamètes égaux ; femelle : 1 ovule + globules
polaires dégénérés).
Source : 1ereC/SVT.pdf, pages 28-29.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    GREY,
    LEFT,
    ORANGE,
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
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=17, color=WHITE, width=32):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit_to_screen(mobject, top_anchor, margin=0.3):
    """Garde-fou d'auto-scale (pattern SVT_FonctionsGonades_09.py) : réduit
    le mobject si sa hauteur dépasse l'espace visible sous `top_anchor`."""
    bas_visible = -config.frame_height / 2 + margin
    hauteur_dispo = top_anchor.get_bottom()[1] - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())


class ComparaisonSpermatogeneseOvogenese(NotionScene):
    def construct(self):
        titre = scene_title("3.6 — Comparaison spermatogenèse / ovogenèse")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        intro = Text(
            _wrap(
                "Nous avons décrit séparément les deux processus : "
                "confrontons-les maintenant point par point, dans un "
                "grand tableau de synthèse.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Nous avons décrit séparément la spermatogenèse et "
                "l'ovogenèse : confrontons-les maintenant, critère par "
                "critère, dans un grand tableau de synthèse."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : sous-tableau 1 (7 premiers critères) --
        entete_t1 = Text("Tableau (1/2) : lieu, cellules, rythme, stock", font_size=22, color=YELLOW, weight="BOLD")
        entete_t1.next_to(titre, DOWN, buff=0.4)

        spermato1_titre = Text("Spermatogenèse", font_size=22, color=YELLOW, weight="BOLD")
        spermato1_lignes = _bullets(
            [
                "Lieu : tubules séminifères des testicules",
                "Cellules souches : spermatogonies",
                "Période d'activité : puberté → vieillesse",
                "Rythme : continu (permanent)",
                "Multiplication : pendant toute la vie",
                "Stock germinal : illimité (renouvelé)",
                "Durée d'un cycle complet : ~70-75 jours",
            ],
        )
        spermato1 = VGroup(spermato1_titre, spermato1_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        ovo1_titre = Text("Ovogenèse", font_size=22, color=YELLOW, weight="BOLD")
        ovo1_lignes = _bullets(
            [
                "Lieu : follicules ovariques des ovaires",
                "Cellules souches : ovogonies",
                "Période d'activité : puberté → ménopause",
                "Rythme : cyclique (1 ovule/cycle de 28 j)",
                "Multiplication : seulement en vie fœtale",
                "Stock germinal : limité (~1-2 M à la naissance)",
                "Durée d'un cycle complet : 12 à 50 ans",
            ],
        )
        ovo1 = VGroup(ovo1_titre, ovo1_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        tableau1 = VGroup(spermato1, ovo1).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        tableau1.next_to(entete_t1, DOWN, buff=0.4)
        _fit_to_screen(tableau1, entete_t1)

        with self.voiceover(
            text=(
                "Premier sous-tableau. Le lieu : tubules séminifères des "
                "testicules chez le mâle, follicules ovariques des "
                "ovaires chez la femelle. Les cellules souches : "
                "spermatogonies contre ovogonies. La période d'activité : "
                "de la puberté à la vieillesse chez l'homme, de la "
                "puberté à la ménopause chez la femme. Le rythme : "
                "continu et permanent chez l'homme, cyclique, un ovule par "
                "cycle d'environ vingt-huit jours, chez la femme. La "
                "multiplication par mitoses : pendant toute la vie chez "
                "l'homme, seulement pendant la vie fœtale chez la femme. "
                "Le stock germinal : illimité et renouvelé chez l'homme, "
                "limité à un ou deux millions à la naissance chez la "
                "femme, et jamais renouvelé. Enfin, la durée d'un cycle "
                "complet : environ soixante-dix à soixante-quinze jours "
                "chez l'homme, contre douze à cinquante ans chez la "
                "femme, à cause des blocages."
            )
        ) as tracker:
            self.play(FadeIn(entete_t1))
            self.play(FadeIn(tableau1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_t1), FadeOut(tableau1))

        # --- Exemple traité : sous-tableau 2 (7 critères suivants) -------------
        entete_t2 = Text("Tableau (2/2) : blocages, rendement, gamète", font_size=22, color=YELLOW, weight="BOLD")
        entete_t2.next_to(titre, DOWN, buff=0.4)

        spermato2_titre = Text("Spermatogenèse", font_size=22, color=YELLOW, weight="BOLD")
        spermato2_lignes = _bullets(
            [
                "Blocages méiotiques : aucun",
                "Divisions cytoplasmiques : égales",
                "Rendement : 4 spermatozoïdes fonctionnels",
                "Taille du gamète : très petit (~60 µm), mobile",
                "Mobilité : mobile (flagelle)",
                "Réserves nutritives : quasi nulles",
                "Achèvement de la méiose : dans le testicule",
            ],
        )
        spermato2 = VGroup(spermato2_titre, spermato2_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        ovo2_titre = Text("Ovogenèse", font_size=22, color=YELLOW, weight="BOLD")
        ovo2_lignes = _bullets(
            [
                "Blocages méiotiques : prophase I puis métaphase II",
                "Divisions cytoplasmiques : inégales",
                "Rendement : 1 ovule + 2-3 globules polaires dégénérés",
                "Taille du gamète : très gros (~100-150 µm), immobile",
                "Mobilité : immobile (cils de la trompe)",
                "Réserves nutritives : abondantes (vitellus)",
                "Achèvement de la méiose : seulement si fécondation",
            ],
        )
        ovo2 = VGroup(ovo2_titre, ovo2_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        tableau2 = VGroup(spermato2, ovo2).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        tableau2.next_to(entete_t2, DOWN, buff=0.4)
        _fit_to_screen(tableau2, entete_t2)

        with self.voiceover(
            text=(
                "Second sous-tableau. Les blocages méiotiques : aucun chez "
                "l'homme, deux chez la femme, prophase un puis métaphase "
                "deux. Les divisions cytoplasmiques : égales chez "
                "l'homme, inégales chez la femme. Le rendement par "
                "méiose : quatre spermatozoïdes fonctionnels contre un "
                "seul ovule et deux à trois globules polaires dégénérés. "
                "La taille du gamète final : très petit, environ soixante "
                "micromètres, et mobile chez l'homme ; très gros, cent à "
                "cent cinquante micromètres, et immobile chez la femme, "
                "transporté par les cils de la trompe. Les réserves "
                "nutritives : quasi nulles chez le spermatozoïde, "
                "abondantes, le vitellus, chez l'ovule. Enfin, "
                "l'achèvement de la méiose : dans le testicule chez "
                "l'homme, seulement si fécondation chez la femme."
            )
        ) as tracker:
            self.play(FadeIn(entete_t2))
            self.play(FadeIn(tableau2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_t2), FadeOut(tableau2))

        # --- Schéma comparatif final -----------------------------------------
        entete_schema = Text("Vue d'ensemble : 4 gamètes égaux vs 1 seul gamète", font_size=21, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.4)

        # Mâle : 4 petites cellules vertes égales.
        male_titre = Text("Mâle", font_size=20, color=WHITE, weight="BOLD")
        male_gametes = VGroup(*[Circle(radius=0.28, color=GREEN, fill_color=GREEN, fill_opacity=0.85) for _ in range(4)])
        male_gametes.arrange(RIGHT, buff=0.35)
        male_bloc = VGroup(male_titre, male_gametes).arrange(DOWN, buff=0.3)

        # Femelle : 1 grosse cellule orange + 3 petites cellules grises (dégénèrent).
        femelle_titre = Text("Femelle", font_size=20, color=WHITE, weight="BOLD")
        ovule_final = Circle(radius=0.42, color=ORANGE, fill_color=ORANGE, fill_opacity=0.9)
        gp_degenere = VGroup(*[Circle(radius=0.14, color=GREY, fill_color=GREY, fill_opacity=0.6) for _ in range(3)])
        gp_degenere.arrange(RIGHT, buff=0.15)
        gp_degenere.next_to(ovule_final, DOWN, buff=0.25)
        femelle_gametes = VGroup(ovule_final, gp_degenere)
        femelle_bloc = VGroup(femelle_titre, femelle_gametes).arrange(DOWN, buff=0.3)

        deux_blocs = VGroup(male_bloc, femelle_bloc).arrange(RIGHT, buff=2.0, aligned_edge=UP)
        deux_blocs.next_to(entete_schema, DOWN, buff=0.5)

        label_male = Text("4 spermatozoïdes égaux et fonctionnels", font_size=15, color=WHITE)
        label_male.next_to(male_bloc, DOWN, buff=0.3)
        label_femelle = Text("1 ovule fonctionnel + globules polaires dégénérés", font_size=15, color=WHITE)
        label_femelle.next_to(femelle_bloc, DOWN, buff=0.3)

        schema_final = VGroup(deux_blocs, label_male, label_femelle)

        with self.voiceover(
            text=(
                "Ce contraste se résume en une image. Chez le mâle, des "
                "divisions cytoplasmiques équilibrées produisent quatre "
                "spermatozoïdes égaux et tous fonctionnels. Chez la "
                "femelle, des divisions inéquilibrées ne donnent qu'un "
                "seul gamète fonctionnel, l'ovule, les globules polaires "
                "dégénérant tous."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(male_bloc), FadeIn(femelle_bloc))
            self.play(FadeIn(label_male), FadeIn(label_femelle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(schema_final))

        # --- À retenir ----------------------------------------------------------
        retenir = property_box(
            Text(
                _wrap(
                    "L'écart de rendement (4 gamètes vs 1) vient d'une "
                    "seule différence mécanique : les divisions "
                    "cytoplasmiques sont égales dans la spermatogenèse, "
                    "inégales dans l'ovogenèse. Tout le reste (blocages, "
                    "durée, rythme) découle du calendrier hormonal "
                    "différent des deux sexes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de cette comparaison : l'écart de "
                "rendement, quatre gamètes contre un seul, vient d'une "
                "seule différence mécanique, le caractère égal ou inégal "
                "des divisions cytoplasmiques. Tout le reste, les "
                "blocages, la durée, le rythme, découle du calendrier "
                "hormonal différent des deux sexes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne crois pas que la méiose donne toujours 4 gamètes : "
                    "elle donne bien 4 cellules haploïdes dans les deux "
                    "sexes, mais chez la femelle, 3 d'entre elles sont des "
                    "globules polaires qui dégénèrent — un seul gamète "
                    "fonctionnel est obtenu.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : ne crois pas que la méiose donne "
                "toujours quatre gamètes. Elle donne bien quatre cellules "
                "haploïdes dans les deux sexes, mais chez la femelle, "
                "trois d'entre elles sont des globules polaires qui "
                "dégénèrent : un seul gamète fonctionnel est obtenu. "
                "C'est l'inégalité des divisions cytoplasmiques qui fait "
                "toute la différence."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
