"""
scenes/Chimie_ClassificationQuantitativeRedox_06.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 06.

§ 6. Vérification avec la pile Daniell + échelle des E°. `theorem_box` de
la relation E = E°(cathode) - E°(anode), vérification numérique sur la
pile Daniell (0,34 - (-0,76) = 1,10 V, valeur mesurée en scène 02).
Construction de l'échelle verticale des potentiels standard, de
F₂/F⁻ (+2,87 V) en haut jusqu'à K⁺/K (-2,93 V) en bas, avec plusieurs
couples intermédiaires (dont Cu²⁺/Cu et Zn²⁺/Zn replacés). Mention du
« potentiel standard apparent » pour les couples faisant intervenir
H₃O⁺ (valeur qui dépend du pH, à distinguer du E° véritable).
Source : 1ereC/Chimie.pdf, chapitre 11, pages 107-108.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    ORANGE,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _echelle_potentiels(couples, e_min=-3.1, e_max=3.1, hauteur=6.0):
    """Échelle verticale des potentiels standard : axe vertical gradué en
    volts avec, pour chaque (nom, valeur), une graduation et une étiquette
    positionnées proportionnellement à leur E° — construite avec Line/Text
    uniquement (aucune bibliothèque externe)."""
    axe = Line([0, -hauteur / 2, 0], [0, hauteur / 2, 0], color=WHITE, stroke_width=3)
    fleche_haut = Arrow(
        [0, hauteur / 2 - 0.3, 0], [0, hauteur / 2 + 0.35, 0],
        color=WHITE, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.5,
    )
    label_oxyd = Text("Ox. fort", font_size=14, color=YELLOW)
    label_oxyd.next_to(fleche_haut, UP, buff=0.05)
    label_bas = Text("Réd. fort", font_size=14, color=YELLOW)
    label_bas.next_to(axe.get_bottom(), DOWN, buff=0.1)

    def y_de(e):
        return -hauteur / 2 + (e - e_min) / (e_max - e_min) * hauteur

    graduations = VGroup(axe, fleche_haut, label_oxyd, label_bas)
    for nom, valeur in couples:
        y = y_de(valeur)
        trait = Line([-0.12, y, 0], [0.12, y, 0], color=WHITE, stroke_width=2)
        etiquette = MathTex(nom, font_size=18, color=WHITE)
        etiquette.next_to(trait, LEFT, buff=0.15)
        valeur_txt = Text(f"{valeur:+.2f} V", font_size=14, color=YELLOW)
        valeur_txt.next_to(trait, RIGHT, buff=0.15)
        graduations.add(trait, etiquette, valeur_txt)

    return graduations


COUPLES_ECHELLE = [
    (r"F_2/F^{-}", 2.87),
    (r"MnO_4^{-}/Mn^{2+}", 1.51),
    (r"Cl_2/Cl^{-}", 1.36),
    (r"Ag^{+}/Ag", 0.80),
    (r"Cu^{2+}/Cu", 0.34),
    (r"H_3O^{+}/H_2", 0.00),
    (r"Zn^{2+}/Zn", -0.76),
    (r"Al^{3+}/Al", -1.66),
    (r"K^{+}/K", -2.93),
]


class VerificationDaniellEchelleE0(NotionScene):
    def construct(self):
        titre = scene_title("11.6 Vérification (pile Daniell) et échelle des E°")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : relation générale E = E°cathode - E°anode --------------------
        intro = Text(
            _wrap(
                "Nos deux valeurs, E°(Cu²⁺/Cu) et E°(Zn²⁺/Zn), doivent "
                "permettre de retrouver la f.é.m. mesurée de la pile "
                "Daniell : 1,10 V. Vérifions-le.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les potentiels standard que nous venons d'établir ne "
                "sont pas de simples curiosités : ils doivent permettre "
                "de retrouver la force électromotrice mesurée de la pile "
                "Daniell, un virgule dix volt. Vérifions-le grâce à une "
                "relation générale."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : théorème + vérification numérique -----------------------
        theo = theorem_box(
            VGroup(
                Text("Pour toute pile en fonctionnement spontané :", font_size=21, weight="BOLD"),
                MathTex(r"E = E^{\circ}(\text{cathode}) - E^{\circ}(\text{anode})", font_size=30, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour toute pile en fonctionnement spontané, la force "
                "électromotrice est égale au potentiel standard de la "
                "cathode, le pôle positif, siège de la réduction, moins "
                "le potentiel standard de l'anode, le pôle négatif, "
                "siège de l'oxydation."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        verif = VGroup(
            Text("Pile Daniell : cathode = Cu²⁺/Cu, anode = Zn²⁺/Zn", font_size=21, color=WHITE),
            MathTex(
                r"E = E^{\circ}(Cu^{2+}/Cu) - E^{\circ}(Zn^{2+}/Zn) = 0{,}34 - (-0{,}76)",
                font_size=26,
                color=WHITE,
            ),
            MathTex(r"E = 1{,}10\ V", font_size=32, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        verif.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans la pile Daniell, la cathode est l'électrode de "
                "cuivre, l'anode l'électrode de zinc. On calcule donc E "
                "égale zéro virgule trente-quatre, moins moins zéro "
                "virgule soixante-seize, soit zéro virgule trente-quatre "
                "plus zéro virgule soixante-seize, ce qui donne un "
                "virgule dix volt : exactement la valeur mesurée "
                "expérimentalement au voltmètre. Le modèle est validé."
            )
        ) as tracker:
            self.play(Write(verif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(verif))

        # --- Exemple traité : échelle des potentiels standard ------------------------
        entete_echelle = Text("Échelle des potentiels standard E°", font_size=21, color=YELLOW, weight="BOLD")
        entete_echelle.to_edge(UP).shift(DOWN * 0.75)

        echelle = _echelle_potentiels(COUPLES_ECHELLE)
        echelle.scale(0.92)
        echelle.next_to(entete_echelle, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On peut alors ranger tous les couples oxydant sur "
                "réducteur connus sur une échelle verticale unique, "
                "graduée en volts, classée par potentiel standard "
                "croissant. Le fluor sur ion fluorure occupe le sommet, à "
                "plus deux virgule quatre-vingt-sept volts : c'est "
                "l'oxydant le plus fort de cette échelle. Le potassium "
                "occupe la base, à moins deux virgule quatre-vingt-treize "
                "volts : c'est le réducteur le plus fort. Entre les deux, "
                "on retrouve nos couples déjà connus, cuivre et zinc, "
                "ainsi que la référence, ion oxonium sur dihydrogène, "
                "fixée à zéro."
            )
        ) as tracker:
            self.play(FadeOut(titre), FadeIn(entete_echelle))
            self.play(Write(echelle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_echelle), FadeOut(echelle))

        # --- Piège / remarque : potentiel standard apparent -----------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Pour les couples faisant intervenir H₃O⁺ (ex. MnO₄⁻/"
                    "Mn²⁺), la valeur affichée dépend du pH de la solution : "
                    "on parle alors de potentiel standard APPARENT, à "
                    "distinguer du véritable E° défini dans les conditions "
                    "standard strictes ([H₃O⁺] = 1 mol/L, donc pH = 0).",
                    width=48,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        remarque.to_edge(UP).shift(DOWN * 0.4)

        with self.voiceover(
            text=(
                "Une remarque importante avant de conclure : pour les "
                "couples faisant intervenir l'ion oxonium, comme l'ion "
                "permanganate sur ion manganèse deux plus, la valeur "
                "affichée dans les tables usuelles dépend en réalité du "
                "pH de la solution étudiée. On parle alors de potentiel "
                "standard apparent, à distinguer du véritable potentiel "
                "standard, défini uniquement dans les conditions "
                "standard strictes, c'est-à-dire pour un pH égal à zéro."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))
