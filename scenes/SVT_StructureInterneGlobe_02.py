"""
scenes/SVT_StructureInterneGlobe_02.py — Chapitre 7 (1ereC, SVT), scène 02.

§ I.2 Les indices indirects (1/2) : la densité moyenne de la Terre (calcul
complet M, V, ρ_moy ≈ 5,5, comparaison avec les roches de surface 2,7-3,3,
conclusion « la Terre n'est pas homogène ») + les météorites (chondrites →
modèle du manteau, sidérites → modèle du noyau).
Source : 1ereC/SVT.pdf, page 71.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write, config

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


class DensiteMoyenneEtMeteorites(NotionScene):
    def construct(self):
        titre = scene_title("I.2 — Les indices indirects (1/2)")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : comment peser la Terre sans y aller -------------------
        intro = Text(
            _wrap(
                "On ne peut pas peser la Terre sur une balance. Mais on peut "
                "calculer sa masse à partir de l'attraction gravitationnelle "
                "(expérience de Cavendish, 1798) puis comparer cette masse "
                "au volume de la sphère terrestre.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On ne peut évidemment pas peser la Terre sur une balance. "
                "Mais on peut calculer sa masse à partir de l'attraction "
                "gravitationnelle qu'elle exerce, grâce à l'expérience de "
                "Cavendish, réalisée en dix-sept cent quatre-vingt-dix-huit. "
                "Il suffit ensuite de comparer cette masse au volume de la "
                "sphère terrestre pour obtenir sa densité moyenne."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : le calcul complet -------------------
        entete_calc = Text("a) La densité moyenne de la Terre", font_size=25, color=YELLOW, weight="BOLD")
        entete_calc.next_to(titre, DOWN, buff=0.4)

        masse = MathTex(r"M = 5{,}97 \times 10^{24}\ \text{kg}", font_size=30, color=WHITE)
        volume1 = MathTex(
            r"V = \dfrac{4}{3}\pi R^3 = \dfrac{4}{3}\pi \left(6{,}371 \times 10^{6}\ \text{m}\right)^3",
            font_size=28,
            color=WHITE,
        )
        volume2 = MathTex(r"V \approx 1{,}083 \times 10^{21}\ \text{m}^3", font_size=28, color=WHITE)
        densite = MathTex(
            r"\rho_{moy} = \dfrac{M}{V} \approx \dfrac{5{,}97 \times 10^{24}}{1{,}083 \times 10^{21}} \approx 5{,}5",
            font_size=28,
            color=YELLOW,
        )
        calc = VGroup(masse, volume1, volume2, densite).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        calc.next_to(entete_calc, DOWN, buff=0.4)
        _garde_fou(VGroup(entete_calc, calc))

        with self.voiceover(
            text=(
                "La masse de la Terre vaut environ cinq virgule quatre-vingt-"
                "dix-sept fois dix puissance vingt-quatre kilogrammes. Son "
                "volume, calculé pour une sphère de rayon R égale six mille "
                "trois cent soixante et onze kilomètres, vaut quatre tiers "
                "pi R cube, soit environ un virgule zéro huit trois fois dix "
                "puissance vingt et un mètres cube. La densité moyenne est "
                "donc le rapport de la masse sur le volume : elle vaut "
                "environ cinq virgule cinq."
            )
        ) as tracker:
            self.play(FadeIn(entete_calc))
            self.play(Write(masse))
            self.play(Write(volume1))
            self.play(Write(volume2))
            self.play(Write(densite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_calc), FadeOut(calc))

        # --- Comparaison et conclusion (propriété) ---------------------------
        conclusion = property_box(
            Text(
                _wrap(
                    "Les roches de surface ont une densité de 2,7 (granite) "
                    "à 3,3 (basalte, péridotite), très inférieure à la "
                    "densité moyenne du globe (5,5). Conclusion : "
                    "l'intérieur de la Terre contient des matériaux "
                    "beaucoup plus denses que ceux de la surface. La Terre "
                    "n'est pas homogène.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Or les roches de surface ont une densité de deux virgule "
                "sept pour le granite, à trois virgule trois pour le basalte "
                "ou la péridotite : bien inférieure à la densité moyenne du "
                "globe, cinq virgule cinq. La conclusion s'impose : "
                "l'intérieur de la Terre contient des matériaux beaucoup "
                "plus denses que ceux de la surface. La Terre n'est donc pas "
                "homogène : elle cache, en profondeur, des matériaux "
                "compacts que nous ne voyons jamais directement."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Exemple traité : les météorites, modèles du manteau et noyau ---
        meteorites = definition_box(
            Text(
                _wrap(
                    "Les météorites, témoins de la matière primitive du "
                    "système solaire, sont de deux grands types : les "
                    "chondrites (roches silicatées comparables aux "
                    "péridotites → modèle possible du manteau) ; les "
                    "sidérites, alliage de fer et de nickel → modèle "
                    "possible du noyau.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        meteorites.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un deuxième indice indirect confirme cette hétérogénéité : "
                "les météorites, témoins de la matière primitive du système "
                "solaire. On en distingue deux grands types. Les chondrites "
                "sont des roches silicatées comparables aux péridotites : "
                "elles fournissent un modèle possible pour le manteau. Les "
                "sidérites, elles, sont des météorites ferreuses, un "
                "alliage de fer et de nickel : elles fournissent un modèle "
                "possible pour le noyau."
            )
        ) as tracker:
            self.play(FadeIn(meteorites))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meteorites))

        # --- Exemple numérique traité : comparer deux échantillons -----------
        exemple = example_box(
            Text(
                _wrap(
                    "Un échantillon de granite a une masse de 270 g pour un "
                    "volume de 100 cm³ ; un échantillon de péridotite a une "
                    "masse de 330 g pour le même volume. Comparer leurs "
                    "densités à celle, moyenne, du globe.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : un échantillon de granite a une masse de "
                "deux cent soixante-dix grammes pour un volume de cent "
                "centimètres cube ; un échantillon de péridotite a une "
                "masse de trois cent trente grammes pour le même volume. "
                "Comparons leurs densités à celle, moyenne, du globe."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        resolution = MathTex(
            r"\rho_{\text{granite}} = \dfrac{270}{100} = 2{,}7 \quad ; \quad \rho_{\text{péridotite}} = \dfrac{330}{100} = 3{,}3 \; \ll \; 5{,}5",
            font_size=26,
            color=YELLOW,
        )
        resolution.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La densité du granite vaut deux cent soixante-dix sur cent, "
                "soit deux virgule sept. Celle de la péridotite vaut trois "
                "cent trente sur cent, soit trois virgule trois. Ces deux "
                "valeurs restent très inférieures à cinq virgule cinq, la "
                "densité moyenne du globe : même les roches les plus denses "
                "de la surface ne suffisent pas à expliquer la masse totale "
                "de la Terre. Il faut donc des matériaux bien plus denses en "
                "profondeur, comme le suggèrent les sidérites."
            )
        ) as tracker:
            self.play(Write(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(resolution))

        # --- À retenir --------------------------------------------------------
        retenir = _bullets(
            [
                "ρ_moy(Terre) ≈ 5,5 alors que les roches de surface valent 2,7 à 3,3.",
                "La Terre n'est pas homogène : des matériaux denses existent en profondeur.",
                "Chondrites → modèle du manteau ; sidérites (Fe-Ni) → modèle du noyau.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : la densité moyenne de la Terre vaut environ "
                "cinq virgule cinq, alors que les roches de surface valent "
                "seulement deux virgule sept à trois virgule trois. La Terre "
                "n'est donc pas homogène : des matériaux denses existent en "
                "profondeur. Les chondrites fournissent un modèle du "
                "manteau, les sidérites, alliage de fer et de nickel, un "
                "modèle du noyau."
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
                    "Ne pas confondre la densité MOYENNE du globe (5,5, qui "
                    "mélange toutes les couches) avec la densité des roches "
                    "de SURFACE (2,7 à 3,3) : c'est justement leur écart qui "
                    "prouve que la Terre est différenciée en couches de "
                    "densités croissantes vers le centre.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : ne confondez jamais la densité "
                "moyenne du globe, cinq virgule cinq, qui mélange toutes les "
                "couches internes, avec la densité des roches de surface "
                "seulement, deux virgule sept à trois virgule trois. C'est "
                "justement leur écart qui prouve que la Terre est "
                "différenciée en couches de densités croissantes vers le "
                "centre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
