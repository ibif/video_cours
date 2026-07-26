"""
scenes/SVT_StructureInterneGlobe_08.py — Chapitre 7 (1ereC, SVT), scène 08.

§ III.2 La discontinuité de Gutenberg : découverte (1914), profondeur
2900 km, sépare manteau/noyau, signature (chute vP 13,7 → 8, disparition
des ondes S) + interprétation (noyau externe liquide) + zones d'ombre en
détail (103°-142° pour ondes P, au-delà de 103° aucune onde S).
Source : 1ereC/SVT.pdf, page 73-74.
"""

import textwrap

from manim import (
    DEGREES,
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class DiscontinuiteDeGutenberg(NotionScene):
    def construct(self):
        titre = scene_title("III.2 — La discontinuité de Gutenberg")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : une deuxième discontinuité, bien plus profonde --------
        intro = Text(
            _wrap(
                "En 1914, le sismologue allemand Beno Gutenberg étudie la "
                "propagation des ondes bien plus profondément que Moho ne "
                "l'avait fait : il découvre une nouvelle discontinuité "
                "majeure, à 2 900 km de profondeur.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En mille neuf cent quatorze, le sismologue allemand Beno "
                "Gutenberg étudie la propagation des ondes bien plus "
                "profondément que Mohorovičić ne l'avait fait : il découvre "
                "une nouvelle discontinuité majeure, à deux mille neuf cents "
                "kilomètres de profondeur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définition / signature de la discontinuité de Gutenberg ---------
        definition = definition_box(
            Text(
                _wrap(
                    "La discontinuité de Gutenberg sépare le manteau du "
                    "noyau, à 2 900 km de profondeur. Signature : chute "
                    "brutale de vP, d'environ 13,7 à 8 km/s, et disparition "
                    "TOTALE des ondes S en dessous de cette limite.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La discontinuité de Gutenberg sépare le manteau du noyau, "
                "à deux mille neuf cents kilomètres de profondeur. Elle se "
                "traduit par une chute brutale de la vitesse des ondes P, "
                "d'environ treize virgule sept à huit kilomètres par "
                "seconde, et surtout par la disparition totale des ondes S "
                "en dessous de cette limite."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Interprétation : noyau externe liquide (propriété) --------------
        interpretation = property_box(
            Text(
                _wrap(
                    "L'absence des ondes S dans le noyau externe prouve que "
                    "celui-ci est LIQUIDE (les ondes S ne se propagent pas "
                    "dans les liquides). La chute de vitesse des ondes P "
                    "confirme le passage à un milieu de nature différente "
                    "(métallique liquide au lieu de roche solide).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        interpretation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'interprétation est directe : l'absence des ondes S dans "
                "le noyau externe prouve que celui-ci est liquide, puisque "
                "les ondes S ne se propagent jamais dans les liquides. La "
                "chute de la vitesse des ondes P confirme le passage à un "
                "milieu de nature différente, métallique et liquide, au "
                "lieu d'une roche solide."
            )
        ) as tracker:
            self.play(FadeIn(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interpretation))

        # --- Animation du raisonnement : les zones d'ombre en détail ---------
        globe = Circle(radius=2.0, color="#595959", fill_color="#2B2B2B", fill_opacity=1.0)
        noyau = Circle(radius=0.95, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
        noyau.move_to(globe.get_center())
        foyer = Dot(globe.point_at_angle(90 * DEGREES), color=RED, radius=0.07)
        label_foyer = Text("Foyer (0°)", font_size=13, color=RED).next_to(foyer, UP, buff=0.1)

        # Zone d'ombre P : 103° à 142° (mesurée depuis le foyer, deux côtés)
        zone_ombre_p_droite = Arc(
            radius=2.0, start_angle=90 * DEGREES - 103 * DEGREES, angle=-(142 - 103) * DEGREES,
            color="#FF6B6B", stroke_width=10,
        )
        zone_ombre_p_gauche = Arc(
            radius=2.0, start_angle=90 * DEGREES + 103 * DEGREES, angle=(142 - 103) * DEGREES,
            color="#FF6B6B", stroke_width=10,
        )
        label_ombre_p = Text("Zone d'ombre P : 103°-142°", font_size=13, color="#FF6B6B")
        label_ombre_p.next_to(globe, DOWN, buff=0.55)

        marker_103 = Dot(globe.point_at_angle(90 * DEGREES - 103 * DEGREES), color=YELLOW, radius=0.05)
        label_103 = Text("103°", font_size=12, color=YELLOW).next_to(marker_103, RIGHT, buff=0.08)
        marker_142 = Dot(globe.point_at_angle(90 * DEGREES - 142 * DEGREES), color=YELLOW, radius=0.05)
        label_142 = Text("142°", font_size=12, color=YELLOW).next_to(marker_142, DOWN, buff=0.08)

        schema = VGroup(
            globe, noyau, foyer, label_foyer,
            zone_ombre_p_droite, zone_ombre_p_gauche, label_ombre_p,
            marker_103, label_103, marker_142, label_142,
        )
        schema.scale(0.9)
        schema.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Détaillons les zones d'ombre. En raison de la réflexion, et "
                "surtout de la réfraction des ondes P à l'entrée du noyau "
                "liquide — leur vitesse chute, ce qui dévie les rayons vers "
                "le centre — il existe une zone d'ombre pour les ondes P "
                "entre environ cent trois et cent quarante-deux degrés de "
                "distance angulaire par rapport à l'épicentre : aucune onde "
                "P directe n'y est enregistrée. Au-delà de cent trois "
                "degrés, aucune onde S directe n'est plus jamais "
                "enregistrée non plus, car elles sont totalement stoppées "
                "par le noyau liquide : c'est la zone d'ombre totale des "
                "ondes S."
            )
        ) as tracker:
            self.play(FadeIn(globe), FadeIn(noyau), FadeIn(foyer), FadeIn(label_foyer))
            self.play(FadeIn(zone_ombre_p_droite), FadeIn(zone_ombre_p_gauche), FadeIn(label_ombre_p))
            self.play(FadeIn(marker_103), FadeIn(label_103), FadeIn(marker_142), FadeIn(label_142))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : que reçoit une station à 120° ? -----------------
        exemple = example_box(
            Text(
                _wrap(
                    "Une station est située à 120° de distance angulaire de "
                    "l'épicentre d'un séisme. Que reçoit-elle : des ondes P "
                    "directes ? des ondes S directes ? Justifier.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : une station est située à cent vingt "
                "degrés de distance angulaire de l'épicentre d'un séisme. "
                "Que reçoit-elle : des ondes P directes ? des ondes S "
                "directes ? Justifions."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        resolution = Text(
            _wrap(
                "Résolution : 120° est compris entre 103° et 142° → zone "
                "d'ombre des ondes P (aucune P directe). Et 120° > 103° → "
                "zone d'ombre totale des S (aucune S directe non plus).",
                width=52,
            ),
            font_size=20,
            color=YELLOW,
        )
        resolution.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résolution : cent vingt degrés est compris entre cent "
                "trois et cent quarante-deux degrés, donc cette station est "
                "dans la zone d'ombre des ondes P : elle ne reçoit aucune "
                "onde P directe. Et comme cent vingt degrés est supérieur à "
                "cent trois degrés, elle est aussi dans la zone d'ombre "
                "totale des ondes S : elle ne reçoit aucune onde S directe "
                "non plus. Cette station ne reçoit donc, au mieux, que des "
                "ondes réfléchies ou très retardées."
            )
        ) as tracker:
            self.play(FadeIn(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(resolution))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Gutenberg (1914) : sépare manteau et noyau, à 2 900 km.",
                "vP chute de 13,7 à 8 km/s ; ondes S totalement absentes en dessous.",
                "Interprétation : le noyau externe est liquide (Fe-Ni).",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : la discontinuité de Gutenberg, découverte en "
                "mille neuf cent quatorze, sépare le manteau du noyau, à "
                "deux mille neuf cents kilomètres de profondeur. La vitesse "
                "des ondes P chute d'environ treize virgule sept à huit "
                "kilomètres par seconde, et les ondes S disparaissent "
                "totalement en dessous. Cette signature prouve que le noyau "
                "externe est liquide."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre les deux zones d'ombre : celle des "
                    "ondes P est une bande limitée, entre 103° et 142° ; "
                    "celle des ondes S est TOTALE au-delà de 103° (aucune "
                    "onde S directe n'est plus jamais reçue, quelle que "
                    "soit la distance, au-delà de cette limite).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : ne confondez pas les deux "
                "zones d'ombre. Celle des ondes P est une bande limitée, "
                "entre cent trois et cent quarante-deux degrés seulement. "
                "Celle des ondes S est totale au-delà de cent trois degrés "
                ": aucune onde S directe n'est plus jamais reçue, quelle "
                "que soit la distance, au-delà de cette limite."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
