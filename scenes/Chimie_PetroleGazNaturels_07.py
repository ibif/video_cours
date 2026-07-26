"""
scenes/Chimie_PetroleGazNaturels_07.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 07.

§ 7. Importance économique : le pétrole en Côte d'Ivoire. Usages
généraux (carburants, GPL, fiouls, bitume, pétrochimie), gisements
offshore ivoiriens (Espoir, Baobab, Lion, Panthère, Foxtrot, Baleine,
Calao), PETROCI (1975), SIR (Vridi, Port-Bouët, depuis 1965), centrales
thermiques Azito et Ciprel. Source : 1ereC/Chimie.pdf, chapitre 5,
pages 51-52.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREEN,
    ORANGE,
    Dot,
    FadeIn,
    FadeOut,
    Polygon,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _carte_gisements():
    # Schéma stylisé et simplifié du littoral ivoirien avec des points
    # figurant la localisation approximative des principaux gisements
    # offshore, disposés le long d'une côte représentée par un polygone.
    cote = Polygon(
        [-3.5, -0.3, 0], [-2.0, 0.1, 0], [-0.5, -0.1, 0], [1.0, 0.2, 0], [3.5, -0.2, 0],
        [3.5, -1.6, 0], [-3.5, -1.6, 0],
        color=GREEN, fill_color="#2E6B34", fill_opacity=0.6, stroke_width=2,
    )
    mer = Polygon(
        [-3.5, -0.3, 0], [-2.0, 0.1, 0], [-0.5, -0.1, 0], [1.0, 0.2, 0], [3.5, -0.2, 0],
        [3.5, 1.6, 0], [-3.5, 1.6, 0],
        color=BLUE, fill_color="#1B4F72", fill_opacity=0.6, stroke_width=2,
    )

    gisements = {
        "Espoir": (-2.6, 0.7),
        "Baobab": (-1.6, 0.55),
        "Lion": (-0.6, 0.9),
        "Panthère": (0.2, 0.6),
        "Foxtrot": (1.1, 0.75),
        "Baleine": (2.1, 0.55),
        "Calao": (2.9, 0.9),
    }

    points = VGroup()
    for nom, (x, y) in gisements.items():
        point = Dot([x, y, 0], color=ORANGE, radius=0.07)
        label = Text(nom, font_size=13, color=WHITE)
        label.next_to(point, UP, buff=0.08)
        points.add(point, label)

    label_cote = Text("Côte d'Ivoire", font_size=15, color=WHITE, weight="BOLD")
    label_cote.move_to(cote.get_center() + DOWN * 0.4)

    return VGroup(mer, cote, label_cote, points)


class ImportanceEconomiqueEnCoteDIvoire(NotionScene):
    def construct(self):
        titre = scene_title("7. Importance économique : le pétrole en Côte d'Ivoire")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : usages généraux du pétrole raffiné -------------------------
        usages = example_box(
            _bullets(
                [
                    "Carburants : essences, kérosène, gasoil",
                    "GPL : butane, propane (cuisine, chauffage)",
                    "Fiouls : centrales thermiques, transport maritime",
                    "Bitume : revêtement des routes",
                    "Pétrochimie : plastiques, textiles, engrais",
                ],
                font_size=20,
                width=46,
            ),
            box_width=10.5,
        )
        usages.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le pétrole raffiné irrigue l'ensemble de l'économie : "
                "carburants pour les transports, G-P-L pour la cuisine et "
                "le chauffage, fiouls pour les centrales thermiques et le "
                "transport maritime, bitume pour les routes, et matières "
                "premières pour toute la pétrochimie, des plastiques aux "
                "engrais. Voyons maintenant ce que cela représente pour "
                "la Côte d'Ivoire."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(usages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(usages))

        # --- Raisonnement : carte des gisements offshore ivoiriens --------------
        entete_carte = Text("Les gisements offshore ivoiriens", font_size=22, color=YELLOW, weight="BOLD")
        entete_carte.next_to(titre, DOWN, buff=0.3)

        carte = _carte_gisements()
        carte.next_to(entete_carte, DOWN, buff=0.35)
        _fit(carte, entete_carte.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "La Côte d'Ivoire exploite plusieurs gisements de pétrole "
                "et de gaz au large de ses côtes, en offshore : Espoir, "
                "Baobab, Lion, Panthère, Foxtrot, Baleine, découvert plus "
                "récemment, et Calao. Ces gisements font du pays un "
                "acteur pétrolier reconnu dans la sous-région."
            )
        ) as tracker:
            self.play(FadeIn(entete_carte))
            self.play(FadeIn(carte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_carte), FadeOut(carte))

        # --- Exemple traité : PETROCI et la SIR ----------------------------------
        entete_acteurs = Text("Deux acteurs clés : PETROCI et la SIR", font_size=22, color=YELLOW, weight="BOLD")
        entete_acteurs.next_to(titre, DOWN, buff=0.35)

        acteurs = _bullets(
            [
                "PETROCI (Société Nationale d'Opérations Pétrolières de "
                "Côte d'Ivoire), créée en 1975 : gère les intérêts de "
                "l'État dans l'exploration et la production",
                "SIR (Société Ivoirienne de Raffinage), implantée à "
                "Vridi, Port-Bouët, depuis 1965 : raffine le brut en "
                "produits pétroliers",
            ],
            font_size=19,
            width=50,
        )
        acteurs.next_to(entete_acteurs, DOWN, buff=0.35)
        _fit(acteurs, entete_acteurs.get_bottom()[1] - 0.25)

        groupe_acteurs = VGroup(entete_acteurs, acteurs)

        with self.voiceover(
            text=(
                "Deux acteurs structurent le secteur pétrolier ivoirien. "
                "La PETROCI, Société Nationale d'Opérations Pétrolières "
                "de Côte d'Ivoire, créée en mille neuf cent soixante-"
                "quinze, gère les intérêts de l'État dans l'exploration "
                "et la production. La SIR, Société Ivoirienne de "
                "Raffinage, implantée à Vridi, dans la commune de "
                "Port-Bouët, depuis mille neuf cent soixante-cinq, raffine "
                "le pétrole brut en produits utilisables."
            )
        ) as tracker:
            self.play(FadeIn(entete_acteurs))
            self.play(FadeIn(acteurs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_acteurs))

        # --- À retenir : les centrales thermiques Azito et Ciprel ---------------
        centrales = example_box(
            Text(
                _wrap(
                    "Le gaz naturel ivoirien alimente aussi les centrales "
                    "thermiques Azito et Ciprel, qui produisent une part "
                    "essentielle de l'électricité du pays.",
                    width=46,
                ),
                font_size=22,
            ),
            box_width=10.5,
        )
        centrales.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Enfin, retenons que le gaz naturel extrait au large "
                "d'Abidjan alimente les centrales thermiques Azito et "
                "Ciprel, qui produisent une part essentielle de "
                "l'électricité consommée en Côte d'Ivoire : le pétrole et "
                "le gaz ne servent donc pas qu'aux transports, ils sont "
                "aussi au cœur de la production électrique nationale."
            )
        ) as tracker:
            self.play(FadeIn(centrales))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(centrales), FadeOut(titre))
