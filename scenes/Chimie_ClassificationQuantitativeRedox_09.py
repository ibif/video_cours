"""
scenes/Chimie_ClassificationQuantitativeRedox_09.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 09.

§ 9. Cas limite + comparaison avec la règle du gamma. Exemple résolu 4 :
couples Pb²⁺/Pb et Sn²⁺/Sn, ΔE° = 0,01 V → réaction très limitée,
quasiment à l'équilibre. Comparaison entre la règle du gamma et le
critère des potentiels standard (les deux méthodes sont équivalentes sur
le sens de la réaction) et ce que l'approche quantitative apporte de
plus : chiffrer l'écart ΔE°, prévoir si la réaction est totale ou
équilibrée, calculer la f.é.m. d'une pile. Limites communes aux deux
approches : elles ne disent rien sur la VITESSE de la réaction (exemple
de l'aluminium passivé, thermodynamiquement très réducteur mais
cinétiquement inerte à l'air) ; elles ne valent que dans les conditions
standard.
Source : 1ereC/Chimie.pdf, chapitre 11, pages 110-111.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    GREEN,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


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


class CasLimiteComparaisonRegleGamma(NotionScene):
    def construct(self):
        titre = scene_title("11.9 Cas limite et comparaison avec la règle du gamma")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : cas limite --------------------------------------------------------
        intro = Text(
            _wrap(
                "Que se passe-t-il quand deux couples ont des potentiels "
                "standard presque identiques ? C'est justement là que la "
                "règle du gamma seule montrait ses limites.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Que se passe-t-il lorsque deux couples ont des "
                "potentiels standard presque identiques ? C'est "
                "justement dans ce cas limite que la règle du gamma, "
                "utilisée seule, montrait ses limites : elle donnait un "
                "sens, mais sans jamais préciser si ce sens correspondait "
                "à une réaction franche ou à peine amorcée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Exemple résolu 4 : Pb2+/Pb et Sn2+/Sn ---------------------------------------
        exemple4 = example_box(
            VGroup(
                Text("Exemple résolu — couples Sn²⁺/Sn et Pb²⁺/Pb", font_size=20, weight="BOLD"),
                MathTex(
                    r"E^{\circ}(Sn^{2+}/Sn) = -0{,}14\ V \; > \; E^{\circ}(Pb^{2+}/Pb) = -0{,}13\ V",
                    font_size=21,
                    color="#1A1A1A",
                ),
                MathTex(r"\Delta E^{\circ} = |-0{,}13 - (-0{,}14)| = 0{,}01\ V", font_size=23, color="#1A1A1A"),
                Text(
                    "→ ΔE° très faible : la réaction entre ces deux couples est "
                    "très limitée, quasiment à l'équilibre dès le départ.",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.6,
        )
        exemple4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Prenons les couples ion étain deux plus sur étain, et "
                "ion plomb deux plus sur plomb, dont les potentiels "
                "standard valent respectivement moins zéro virgule "
                "quatorze volt et moins zéro virgule treize volt. L'écart "
                "delta E rond ne vaut que zéro virgule zéro un volt : "
                "extrêmement faible. La règle du gamma indiquerait "
                "toujours un sens de réaction, mais le calcul montre que "
                "cette réaction est en réalité très limitée, presque "
                "immédiatement à l'équilibre, avec coexistence "
                "significative des espèces des deux côtés."
            )
        ) as tracker:
            self.play(FadeIn(exemple4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple4))

        # --- Raisonnement : comparaison gamma / E° --------------------------------------
        entete_comp = Text("Règle du gamma vs critère des E° : équivalence, mais...", font_size=20, color=YELLOW, weight="BOLD")
        entete_comp.next_to(titre, DOWN, buff=0.35)

        comparaison = _bullets(
            [
                "Sur le SENS de la réaction spontanée, les deux méthodes "
                "sont rigoureusement équivalentes : la règle du gamma "
                "n'est qu'une lecture graphique du critère des E°.",
                "L'approche quantitative apporte en plus : chiffrer "
                "l'écart ΔE°, prévoir si la réaction sera totale ou "
                "seulement à l'équilibre, et calculer la f.é.m. exacte "
                "d'une pile formée par les deux couples.",
            ],
            font_size=19,
            width=56,
        )
        comparaison.next_to(entete_comp, DOWN, buff=0.3)
        _fit(VGroup(entete_comp, comparaison), entete_comp.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Faisons maintenant le bilan. Sur le sens de la réaction "
                "spontanée, la règle du gamma et le critère des "
                "potentiels standard sont rigoureusement équivalents : la "
                "règle du gamma n'est en réalité qu'une lecture "
                "graphique, simplifiée, du critère quantitatif. Mais "
                "l'approche quantitative apporte trois choses en plus, "
                "que la règle du gamma seule ne peut pas donner : "
                "chiffrer précisément l'écart delta E rond, prévoir si la "
                "réaction sera totale ou seulement à l'équilibre, et "
                "calculer la force électromotrice exacte d'une pile "
                "formée par les deux couples."
            )
        ) as tracker:
            self.play(FadeIn(entete_comp))
            self.play(FadeIn(comparaison))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_comp), FadeOut(comparaison))

        # --- À retenir : limites communes -------------------------------------------------
        entete_limites = Text("Limites communes aux deux approches", font_size=20, color=RED, weight="BOLD")
        entete_limites.next_to(titre, DOWN, buff=0.35)

        limites = _bullets(
            [
                "Ni la règle du gamma ni le critère des E° ne renseignent "
                "sur la VITESSE de la réaction : l'aluminium, très "
                "réducteur (E° = -1,66 V), devrait s'oxyder violemment à "
                "l'air, mais une fine couche d'oxyde protectrice "
                "(passivation) le rend cinétiquement inerte.",
                "Ces deux critères ne valent que dans les CONDITIONS "
                "STANDARD (25 °C, c = 1 mol/L) : hors de ces conditions, "
                "les valeurs de E° peuvent évoluer.",
            ],
            font_size=18,
            width=58,
        )
        limites.next_to(entete_limites, DOWN, buff=0.3)
        _fit(VGroup(entete_limites, limites), entete_limites.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Deux limites, enfin, restent communes aux deux "
                "approches. D'abord, ni l'une ni l'autre ne renseigne sur "
                "la vitesse de la réaction : c'est la thermodynamique, "
                "pas la cinétique. L'aluminium en est un excellent "
                "exemple : très réducteur, avec un potentiel standard de "
                "moins un virgule soixante-six volt, il devrait s'oxyder "
                "violemment au contact de l'air, mais une fine couche "
                "d'oxyde protectrice se forme instantanément à sa "
                "surface et le rend, en pratique, quasiment inerte : "
                "c'est le phénomène de passivation. Ensuite, ces deux "
                "critères ne sont rigoureusement valables que dans les "
                "conditions standard : vingt-cinq degrés, concentrations "
                "d'un mole par litre."
            )
        ) as tracker:
            self.play(FadeIn(entete_limites))
            self.play(FadeIn(limites))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_limites), FadeOut(limites))

        # --- Piège à éviter -----------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre spontanéité (ΔE° > 0, question "
                    "thermodynamique) et rapidité (question cinétique, "
                    "hors du champ de ce chapitre) : une réaction "
                    "spontanée peut être extrêmement lente.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ce piège fondamental avant de conclure ce "
                "chapitre : ne jamais confondre spontanéité, une "
                "question purement thermodynamique liée au signe de "
                "delta E rond, et rapidité, une question de cinétique "
                "chimique. Une réaction peut être parfaitement "
                "spontanée, tout en étant extrêmement lente."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
