"""
scenes/SVT_EchangesCationiquesSol_09.py — Chapitre 9 (1ereC, SVT), scène 09.

Conséquences du pH sur la disponibilité des éléments nutritifs : tableau
(azote, phosphore, potassium, calcium/magnésium, fer/manganèse/bore/
cuivre/zinc, molybdène), méthode point clé (toxicité Al3+/Mn en sol acide,
zone optimale pH 6-7), et schéma de disponibilité en fonction du pH.
Source : 1ereC/SVT.pdf, page 103.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
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
from shapes.boxes import method_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
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


class ConsequencesPHDisponibilite(NotionScene):
    def construct(self):
        titre = scene_title("9.8 — pH et disponibilité des éléments")
        titre.scale(0.64)
        titre.to_edge(UP)

        # --- Énoncé : le pH « ouvre » ou « ferme » l'accès aux éléments -----
        intro = Text(
            _wrap(
                "Un élément peut être présent dans le sol sans être "
                "disponible pour la plante : le pH contrôle sa forme "
                "chimique, soluble ou bloquée.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un élément peut très bien être présent dans le sol sans "
                "être disponible pour la plante : le pH contrôle sa "
                "forme chimique, soluble et absorbable, ou au contraire "
                "bloquée, insoluble. Voyons cela élément par élément."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : tableau des 6 éléments ---------------------------
        tab_titre = Text("Disponibilité des éléments selon le pH", font_size=22, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.35)

        roles = property_box(
            _bullets(
                [
                    "Azote (N), zone pH 6-8 : sol acide → nitrification "
                    "ralentie ; sol basique → pertes par volatilisation "
                    "(NH3)",
                    "Phosphore (P), zone pH 6-7 : sol acide → bloqué par "
                    "Fe/Al ; sol basique → bloqué par le calcium",
                    "Potassium (K), zone pH > 6 : sol acide → fortement "
                    "lessivé ; sol basique → bonne disponibilité",
                    "Calcium et magnésium, zone pH > 6 : sol acide → "
                    "carences fréquentes ; sol basique → excès possible",
                    "Fer, manganèse, bore, cuivre, zinc, zone pH 5-6,5 : "
                    "sol acide → excès toxiques ; sol basique → carences",
                    "Molybdène (Mo), zone pH > 6 : sol acide → carence "
                    "fréquente ; sol basique → bonne disponibilité",
                ],
                font_size=16,
                width=60,
            ),
            box_width=12.6,
        )
        roles.next_to(tab_titre, DOWN, buff=0.3)

        groupe_tableau = VGroup(tab_titre, roles)
        _fit(groupe_tableau, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "L'azote est le mieux disponible entre pH six et huit : "
                "en sol acide, sa nitrification est ralentie ; en sol "
                "basique, il se perd par volatilisation sous forme "
                "d'ammoniac. Le phosphore est le mieux disponible entre "
                "pH six et sept : en sol acide, il est bloqué par le fer "
                "et l'aluminium ; en sol basique, il est bloqué par le "
                "calcium. Le potassium est bien disponible au-dessus de "
                "pH six : en sol acide, il est fortement lessivé et "
                "désorbé par les H+. Le calcium et le magnésium, "
                "au-dessus de pH six également, manquent souvent en sol "
                "acide par lessivage, et peuvent être en excès en sol "
                "basique. Le fer, le manganèse, le bore, le cuivre et le "
                "zinc sont bien disponibles entre pH cinq et six virgule "
                "cinq : en sol trop acide, ils deviennent toxiques en "
                "excès ; en sol basique, ils manquent, devenus "
                "insolubles. Enfin le molybdène, mieux disponible "
                "au-dessus de pH six, manque fréquemment en sol acide."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(roles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(roles))

        # Schéma graphique : disponibilité en fonction du pH -----------------
        axe = Line(LEFT * 4.5, RIGHT * 4.5, color=WHITE, stroke_width=3)
        axe.next_to(titre, DOWN, buff=1.1)

        ph_min, ph_max = 4.0, 8.5
        graduations = VGroup()
        for ph in [4, 5, 6, 7, 8, 8.5]:
            x = axe.get_start()[0] + (ph - ph_min) / (ph_max - ph_min) * (axe.get_end()[0] - axe.get_start()[0])
            tick = Line([x, axe.get_y() - 0.1, 0], [x, axe.get_y() + 0.1, 0], color=WHITE)
            label = Text(str(ph), font_size=15, color=WHITE).next_to(tick, DOWN, buff=0.1)
            graduations.add(tick, label)

        def _x_of(ph):
            return axe.get_start()[0] + (ph - ph_min) / (ph_max - ph_min) * (axe.get_end()[0] - axe.get_start()[0])

        zone_optimale = Rectangle(
            width=_x_of(7) - _x_of(6),
            height=0.5,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.4,
            stroke_width=0,
        )
        zone_optimale.move_to([(_x_of(6) + _x_of(7)) / 2, axe.get_y() + 0.5, 0])
        label_optimale = Text("Zone optimale (pH 6-7)", font_size=16, color=GREEN)
        label_optimale.next_to(zone_optimale, UP, buff=0.1)

        zone_acide = Rectangle(
            width=_x_of(6) - _x_of(4),
            height=0.3,
            color=RED,
            fill_color=RED,
            fill_opacity=0.3,
            stroke_width=0,
        )
        zone_acide.move_to([(_x_of(4) + _x_of(6)) / 2, axe.get_y() - 0.5, 0])
        label_acide = Text("Al3+, Mn toxiques", font_size=14, color=RED).next_to(zone_acide, DOWN, buff=0.1)

        zone_basique = Rectangle(
            width=_x_of(8.5) - _x_of(7),
            height=0.3,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.3,
            stroke_width=0,
        )
        zone_basique.move_to([(_x_of(7) + _x_of(8.5)) / 2, axe.get_y() - 0.5, 0])
        label_basique = Text("Fe, P bloqués", font_size=14, color=YELLOW).next_to(zone_basique, DOWN, buff=0.1)

        schema = VGroup(
            axe, graduations, zone_optimale, label_optimale, zone_acide, label_acide, zone_basique, label_basique
        )

        with self.voiceover(
            text=(
                "Ce schéma résume la situation : sur l'axe du pH, de "
                "quatre à huit virgule cinq, une zone optimale se "
                "dégage nettement entre pH six et sept, où la plupart des "
                "éléments sont disponibles. En dessous, en sol trop "
                "acide, l'aluminium et le manganèse deviennent toxiques. "
                "Au-dessus, en sol trop basique, le fer et le phosphore "
                "deviennent bloqués et indisponibles."
            )
        ) as tracker:
            self.play(FadeIn(axe), FadeIn(graduations))
            self.play(FadeIn(zone_optimale), FadeIn(label_optimale))
            self.play(FadeIn(zone_acide), FadeIn(label_acide), FadeIn(zone_basique), FadeIn(label_basique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir : méthode point clé ------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Point clé : en sol trop acide, l'aluminium Al3+ et "
                    "le manganèse deviennent très solubles et toxiques "
                    "pour les racines, tandis que le phosphore devient "
                    "indisponible. En sol trop basique, le fer et le "
                    "phosphore deviennent indisponibles. La zone optimale "
                    "pour la plupart des cultures se situe entre pH 6 "
                    "et 7.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenez ce point clé. En sol trop acide, l'aluminium et "
                "le manganèse deviennent très solubles et toxiques pour "
                "les racines, tandis que le phosphore devient "
                "indisponible. En sol trop basique, le fer et le "
                "phosphore deviennent eux aussi indisponibles. La zone "
                "optimale pour la plupart des cultures se situe donc "
                "entre pH six et sept, légèrement acide à neutre."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
