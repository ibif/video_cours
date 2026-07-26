"""
scenes/SVT_StructureInterneGlobe_05.py — Chapitre 7 (1ereC, SVT), scène 05.

§ II.2.b Les ondes S (ondes secondaires : transversales, SEULEMENT dans les
solides, plus lentes, vitesses 3,5 → 7,3 km/s, les plus destructrices) +
propriété des vitesses vS=√(μ/ρ) et vP=√((K+4μ/3)/ρ), conséquence "dans un
liquide μ=0 donc vS=0" + § II.2.c les ondes de surface (ondes L).
Source : 1ereC/SVT.pdf, page 72.
"""

import textwrap

import numpy as np

from manim import DOWN, LEFT, ORANGE, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, FunctionGraph, MathTex, Text, VGroup, Write, config

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


def _garde_fou(mobject):
    bas_visible = -config.frame_height / 2 + 0.3
    hauteur_dispo = mobject.get_top()[1] - bas_visible
    if mobject.height > hauteur_dispo > 0:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())


class OndesSVitessesEtOndesL(NotionScene):
    def construct(self):
        titre = scene_title("II.2 — Les ondes S et les ondes de surface")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : un deuxième type d'onde arrive après les P -------------
        intro = Text(
            _wrap(
                "Sur un sismogramme, une deuxième arrivée d'ondes suit "
                "toujours les ondes P. Ce sont les ondes S : de nature "
                "différente, elles ne se comportent pas du tout comme les "
                "ondes P.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Sur un sismogramme, une deuxième arrivée d'ondes suit "
                "toujours les ondes P. Ce sont les ondes S : de nature "
                "différente, elles ne se comportent pas du tout comme les "
                "ondes P."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définition des ondes S -------------------------------------------
        ondes_s_def = definition_box(
            Text(
                _wrap(
                    "Ondes S (secondaires) : ondes transversales (de "
                    "cisaillement), vibration perpendiculaire au sens de "
                    "propagation. Elles ne se propagent QUE dans les "
                    "solides — impossibles dans les liquides, qui ne "
                    "possèdent pas de rigidité. Plus lentes que P, elles "
                    "sont les plus destructrices.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        ondes_s_def.next_to(titre, DOWN, buff=0.5)

        # Schéma comparatif : onde longitudinale (P) vs onde transversale (S)
        sine_p = FunctionGraph(lambda x: 0.4 * np.sin(3 * x), x_range=[-1.8, 1.8], color="#4DABF7", stroke_width=3)
        label_p = Text("Onde P : compression parallèle", font_size=14, color="#4DABF7")
        label_p.next_to(sine_p, DOWN, buff=0.2)
        bloc_p = VGroup(sine_p, label_p)

        sine_s = FunctionGraph(lambda x: 0.4 * np.sin(3 * x), x_range=[-1.8, 1.8], color=ORANGE, stroke_width=3).rotate(1.5708)
        label_s = Text("Onde S : cisaillement perpendiculaire", font_size=14, color=ORANGE)
        label_s.next_to(sine_s, DOWN, buff=0.2)
        bloc_s = VGroup(sine_s, label_s)

        comparatif = VGroup(bloc_p, bloc_s).arrange(RIGHT, buff=1.2)

        with self.voiceover(
            text=(
                "Les ondes S, ou secondaires, sont des ondes transversales, "
                "dites de cisaillement : la vibration des particules se "
                "fait perpendiculairement au sens de propagation, comme une "
                "vague à la surface de l'eau, mais en volume. Elles ne se "
                "propagent que dans les solides : elles sont impossibles "
                "dans les liquides, car un liquide ne peut pas être "
                "cisaillé, il ne possède pas de rigidité. Plus lentes que "
                "les ondes P, elles arrivent en second sur les "
                "sismogrammes, et ce sont les ondes les plus destructrices, "
                "car elles font osciller le sol horizontalement."
            )
        ) as tracker:
            self.play(FadeIn(ondes_s_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ondes_s_def))

        comparatif.next_to(titre, DOWN, buff=0.6)
        with self.voiceover(
            text="Voici, schématiquement, la différence de vibration entre une onde P et une onde S."
        ) as tracker:
            self.play(FadeIn(bloc_p))
            self.play(FadeIn(bloc_s))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(comparatif))

        # --- Animation du raisonnement : la propriété physique des vitesses --
        propriete = property_box(
            Text(
                _wrap(
                    "Les vitesses des ondes dépendent de la rigidité (module "
                    "de cisaillement μ) et de la densité ρ du milieu. Dans "
                    "un liquide, le cisaillement est impossible : μ=0, donc "
                    "vS=0. Les ondes S ne traversent jamais un liquide, "
                    "alors que les ondes P y subsistent (vitesse réduite).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        formules = MathTex(
            r"v_S = \sqrt{\dfrac{\mu}{\rho}} \qquad ; \qquad v_P = \sqrt{\dfrac{K + \frac{4}{3}\mu}{\rho}}",
            font_size=28,
            color=YELLOW,
        )
        formules.next_to(propriete, DOWN, buff=0.4)

        consequence = MathTex(r"\text{liquide} \Rightarrow \mu = 0 \Rightarrow v_S = 0", font_size=28, color=WHITE)
        consequence.next_to(formules, DOWN, buff=0.35)

        bloc_propriete = VGroup(propriete, formules, consequence)
        _garde_fou(bloc_propriete)

        with self.voiceover(
            text=(
                "Une propriété physique explique tout cela : les vitesses "
                "des ondes dépendent de la rigidité, notée mu, le module de "
                "cisaillement, et de la densité rho du milieu traversé. La "
                "vitesse des ondes S vaut la racine carrée de mu sur rho ; "
                "la vitesse des ondes P vaut la racine carrée de K plus "
                "quatre tiers mu, le tout sur rho, où K est le module "
                "d'incompressibilité. Or, dans un liquide, le cisaillement "
                "est impossible : mu est nul, donc la vitesse des ondes S "
                "est nulle. Les ondes S ne traversent donc jamais un "
                "liquide, alors que les ondes P y subsistent, à vitesse "
                "réduite."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.play(Write(formules))
            self.play(Write(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete), FadeOut(formules), FadeOut(consequence))

        # --- Exemple traité : comparer vP et vS à une même profondeur --------
        exemple = example_box(
            Text(
                _wrap(
                    "Dans la croûte continentale : vP ≈ 6 km/s, vS ≈ 3,5 "
                    "km/s. À la base du manteau : vP ≈ 13,7 km/s, vS ≈ 7,3 "
                    "km/s. Calculer le rapport vP/vS dans les deux cas.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : dans la croûte continentale, vP vaut "
                "environ six kilomètres par seconde et vS environ trois "
                "virgule cinq kilomètres par seconde. À la base du manteau, "
                "vP vaut environ treize virgule sept kilomètres par seconde "
                "et vS environ sept virgule trois kilomètres par seconde. "
                "Calculons le rapport vP sur vS dans les deux cas."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        calc = MathTex(
            r"\dfrac{v_P}{v_S}\bigg|_{\text{croûte}} = \dfrac{6}{3{,}5} \approx 1{,}7 "
            r"\qquad ; \qquad \dfrac{v_P}{v_S}\bigg|_{\text{manteau}} = \dfrac{13{,}7}{7{,}3} \approx 1{,}9",
            font_size=24,
            color=YELLOW,
        )
        calc.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Dans la croûte, le rapport vaut six divisé par trois "
                "virgule cinq, soit environ un virgule sept. À la base du "
                "manteau, il vaut treize virgule sept divisé par sept "
                "virgule trois, soit environ un virgule neuf. Dans les deux "
                "cas, les ondes P restent toujours plus rapides que les "
                "ondes S, d'un facteur proche de un virgule sept à deux, "
                "quelle que soit la profondeur."
            )
        ) as tracker:
            self.play(Write(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(calc))

        # --- Les ondes de surface (ondes L) ------------------------------------
        ondes_l = definition_box(
            Text(
                _wrap(
                    "Les ondes de surface (ondes L) sont guidées le long de "
                    "la surface du globe. Plus lentes mais se propageant "
                    "sur de grandes distances, elles provoquent des "
                    "mouvements amples et durables, responsables de dégâts "
                    "étendus. On ne les utilise pas pour explorer "
                    "l'intérieur du globe.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        ondes_l.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Il existe un troisième type d'ondes, les ondes de surface, "
                "ou ondes L. Guidées le long de la surface du globe, elles "
                "se propagent plus lentement que les ondes P et S, mais sur "
                "de grandes distances ; elles provoquent des mouvements "
                "amples et durables, responsables de dégâts étendus. "
                "Contrairement aux ondes P et S, on ne les utilise pas pour "
                "explorer l'intérieur du globe, car elles restent en "
                "surface."
            )
        ) as tracker:
            self.play(FadeIn(ondes_l))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ondes_l))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Ondes S : transversales, seulement dans les solides, plus lentes que P.",
                "vS=√(μ/ρ) ; dans un liquide μ=0 → vS=0.",
                "Ondes L : ondes de surface, les plus lentes, les plus destructrices, non exploitées ici.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : les ondes S sont transversales, ne se "
                "propagent que dans les solides, et sont plus lentes que "
                "les ondes P. La formule vS égale racine de mu sur rho "
                "montre que dans un liquide, mu est nul, donc vS est nul. "
                "Les ondes L, ondes de surface, sont les plus lentes mais "
                "les plus destructrices, et ne sont pas exploitées pour "
                "explorer l'intérieur du globe."
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
                    "Ne pas confondre vitesse et pouvoir destructeur : les "
                    "ondes S sont plus lentes que les ondes P mais plus "
                    "destructrices ; les ondes L, encore plus lentes, "
                    "causent souvent le plus de dégâts en surface. La "
                    "vitesse la plus élevée n'est pas toujours la plus "
                    "dangereuse.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : ne confondez pas vitesse et "
                "pouvoir destructeur. Les ondes S sont plus lentes que les "
                "ondes P mais plus destructrices ; les ondes L, encore plus "
                "lentes, causent souvent le plus de dégâts en surface. La "
                "vitesse la plus élevée n'est donc pas toujours la plus "
                "dangereuse."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
