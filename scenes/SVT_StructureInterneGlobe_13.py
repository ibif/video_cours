"""
scenes/SVT_StructureInterneGlobe_13.py — Chapitre 7 (1ereC, SVT), scène 13.

§ VI. Densité, pression et température internes : densité par couches
(2,7 à 13) + pression lithostatique (définition, formule P=ρgh, ordres de
grandeur 3 GPa à 100 km, 360 GPa au centre) + gradient géothermique
(définition, formule G=ΔT/Δz, ~3°C/100m, T(z)=T0+Gz) + piège (gradient non
valable jusqu'au centre) + tableau températures estimées par profondeur +
origine de la chaleur + méthode « le paradoxe de la graine ».
Source : 1ereC/SVT.pdf, pages 77-78.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(rows, font_size=17, header_color=YELLOW, body_color=WHITE, col_alignments=None, buff=(0.45, 0.2)):
    ncols = len(rows[0])
    cells = []
    for i, row in enumerate(rows):
        for c in row:
            cells.append(
                Text(
                    c,
                    font_size=font_size,
                    color=header_color if i == 0 else body_color,
                    weight="BOLD" if i == 0 else "NORMAL",
                )
            )
    grid = VGroup(*cells)
    align = col_alignments or ("l" * ncols)
    grid.arrange_in_grid(rows=len(rows), cols=ncols, buff=buff, col_alignments=align)
    return grid


def _garde_fou(mobject):
    bas_visible = -config.frame_height / 2 + 0.3
    hauteur_dispo = mobject.get_top()[1] - bas_visible
    if mobject.height > hauteur_dispo > 0:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())


class DensitePressionEtTemperature(NotionScene):
    def construct(self):
        titre = scene_title("VI — Densité, pression et température internes")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : trois grandeurs qui varient avec la profondeur ---------
        intro = Text(
            _wrap(
                "Trois grandeurs physiques varient avec la profondeur : la "
                "densité, la pression et la température. Elles expliquent "
                "à la fois la stratification du globe et l'état physique "
                "de chaque enveloppe.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Trois grandeurs physiques varient avec la profondeur : la "
                "densité, la pression et la température. Elles expliquent à "
                "la fois la stratification du globe et l'état physique de "
                "chaque enveloppe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- VI.1 Densité par couches ------------------------------------------
        densite = _bullets(
            [
                "Croûte continentale : 2,7",
                "Croûte océanique : 3,0 à 3,3",
                "Manteau : de 3,3 (haut) à 5,7 (base)",
                "Noyau : de 10 à 13",
            ],
            font_size=21,
            width=44,
        )
        entete_densite = Text("VI.1 — La densité interne", font_size=25, color=YELLOW, weight="BOLD")
        entete_densite.next_to(titre, DOWN, buff=0.5)
        densite.next_to(entete_densite, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La densité augmente avec la profondeur, par couches : deux "
                "virgule sept pour la croûte continentale ; trois à trois "
                "virgule trois pour la croûte océanique ; de trois virgule "
                "trois à cinq virgule sept pour le manteau ; et de dix à "
                "treize pour le noyau. La densité moyenne du globe, cinq "
                "virgule cinq, s'explique par la concentration des "
                "matériaux denses, fer et nickel, vers le centre : la Terre "
                "est différenciée en enveloppes concentriques."
            )
        ) as tracker:
            self.play(FadeIn(entete_densite))
            self.play(FadeIn(densite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_densite), FadeOut(densite))

        # --- VI.2 Pression lithostatique ----------------------------------------
        pression_def = definition_box(
            Text(
                _wrap(
                    "Pression lithostatique : à une profondeur donnée, la "
                    "pression correspond au poids de la colonne de roches "
                    "située au-dessus. En 1ère approximation (densité "
                    "constante) : P=ρ×g×h, avec P en Pa, ρ en kg.m⁻³, "
                    "g=9,81 m.s⁻², h en mètres.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        pression_def.next_to(titre, DOWN, buff=0.5)

        formule_pression = MathTex(r"P = \rho \times g \times h", font_size=32, color=YELLOW)
        formule_pression.next_to(pression_def, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La pression lithostatique, à une profondeur donnée, "
                "correspond au poids de la colonne de roches située "
                "au-dessus. En première approximation, en supposant la "
                "densité constante : P égale rho fois g fois h, avec P en "
                "pascals, rho la densité en kilogrammes par mètre cube, g "
                "égale neuf virgule quatre-vingt-un mètres par seconde "
                "carré, et h la profondeur en mètres."
            )
        ) as tracker:
            self.play(FadeIn(pression_def))
            self.play(Write(formule_pression))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pression_def), FadeOut(formule_pression))

        # --- Exemple traité : calcul de pression à 100 km ---------------------
        exemple_pression = example_box(
            Text(
                _wrap(
                    "Calculer la pression à 100 km de profondeur, en "
                    "prenant ρ ≈ 3 300 kg.m⁻³ (manteau supérieur).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple_pression.next_to(titre, DOWN, buff=0.5)

        calc_pression = MathTex(
            r"P = 3\,300 \times 9{,}81 \times 100\,000 \approx 3{,}2 \times 10^{9}\ \text{Pa} \approx 3\ \text{GPa}",
            font_size=26,
            color=YELLOW,
        )
        calc_pression.next_to(exemple_pression, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple traité : calculons la pression à cent kilomètres "
                "de profondeur, en prenant une densité d'environ trois "
                "mille trois cents kilogrammes par mètre cube pour le "
                "manteau supérieur. P égale trois mille trois cents fois "
                "neuf virgule quatre-vingt-un fois cent mille mètres, soit "
                "environ trois virgule deux fois dix puissance neuf "
                "pascals, c'est-à-dire environ trois gigapascals. On "
                "retrouve l'ordre de grandeur attendu. Au centre de la "
                "Terre, en intégrant la densité croissante sur toute la "
                "profondeur, la pression atteint environ trois cent "
                "soixante gigapascals, soit trois virgule six millions de "
                "fois la pression atmosphérique."
            )
        ) as tracker:
            self.play(FadeIn(exemple_pression))
            self.play(Write(calc_pression))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_pression), FadeOut(calc_pression))

        # --- VI.3 Gradient géothermique ------------------------------------------
        gradient_def = definition_box(
            Text(
                _wrap(
                    "Gradient géothermique G : augmentation moyenne de la "
                    "température par unité de profondeur, près de la "
                    "surface. G=ΔT/Δz ≈ 3°C/100 m (croûte continentale). "
                    "Température à la profondeur z, en 1ère approximation : "
                    "T(z)=T0+G×z.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        gradient_def.next_to(titre, DOWN, buff=0.5)

        formules_gradient = MathTex(
            r"G = \dfrac{\Delta T}{\Delta z} \qquad ; \qquad T(z) = T_0 + G \times z",
            font_size=28,
            color=YELLOW,
        )
        formules_gradient.next_to(gradient_def, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le gradient géothermique G est l'augmentation moyenne de "
                "la température par unité de profondeur, près de la "
                "surface : G égale delta T sur delta z. En moyenne, G vaut "
                "environ trois degrés tous les cent mètres dans la croûte "
                "continentale, avec de fortes variations régionales, de un "
                "à cinq degrés pour cent mètres. La température à la "
                "profondeur z s'écrit alors, en première approximation : T "
                "de z égale T zéro plus G fois z."
            )
        ) as tracker:
            self.play(FadeIn(gradient_def))
            self.play(Write(formules_gradient))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(gradient_def), FadeOut(formules_gradient))

        # --- Piège : le gradient n'est pas valable jusqu'au centre -----------
        piege_gradient = warning_box(
            Text(
                _wrap(
                    "Ce gradient n'est valable que près de la surface ! "
                    "S'il restait de 30°C/km jusqu'au centre, la "
                    "température y dépasserait 190 000°C. En réalité, le "
                    "gradient diminue fortement avec la profondeur.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege_gradient.next_to(titre, DOWN, buff=0.5)

        calc_absurde = MathTex(
            r"30\,{}^{\circ}\text{C/km} \times 6\,371\ \text{km} \approx 191\,000\,{}^{\circ}\text{C} \; \text{(absurde)}",
            font_size=24,
            color="#FF6B6B",
        )
        calc_absurde.next_to(piege_gradient, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Attention, piège majeur à éviter : ce gradient de trente "
                "degrés par kilomètre n'est valable que près de la surface. "
                "S'il restait constant jusqu'au centre, la température y "
                "dépasserait cent quatre-vingt-onze mille degrés, ce qui "
                "est totalement absurde. En réalité, le gradient diminue "
                "fortement avec la profondeur : on ne peut jamais "
                "extrapoler une loi valable en surface jusqu'au centre du "
                "globe."
            )
        ) as tracker:
            self.play(FadeIn(piege_gradient))
            self.play(Write(calc_absurde))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_gradient), FadeOut(calc_absurde))

        # --- Tableau des températures estimées + origine de la chaleur -------
        entete_tab = Text("Températures estimées par profondeur", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        tableau = _tableau(
            [
                ["Profondeur", "Température estimée"],
                ["100 km", "1 000 à 1 400°C"],
                ["700 km", "~1 900°C"],
                ["2 900 km", "~3 700°C"],
                ["6 371 km (centre)", "5 000 à 6 000°C"],
            ],
            font_size=19,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        bloc_tab = VGroup(entete_tab, tableau)
        _garde_fou(bloc_tab)

        with self.voiceover(
            text=(
                "Voici les températures réellement estimées : environ mille "
                "à mille quatre cents degrés à cent kilomètres, là où les "
                "péridotites commencent à fondre partiellement ; environ "
                "mille neuf cents degrés à sept cents kilomètres ; environ "
                "trois mille sept cents degrés à deux mille neuf cents "
                "kilomètres ; et cinq mille à six mille degrés au centre, "
                "comparable à la surface du Soleil. L'origine de cette "
                "chaleur est double : la chaleur primordiale, conservée "
                "depuis la formation de la Terre par accrétion il y a "
                "quatre virgule six milliards d'années, et surtout la "
                "radioactivité, la désintégration de l'uranium deux cent "
                "trente-huit, du thorium deux cent trente-deux et du "
                "potassium quarante, qui dégage en permanence de la "
                "chaleur."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Méthode point clé : le paradoxe de la graine ----------------------
        paradoxe = method_box(
            Text(
                _wrap(
                    "Le paradoxe de la graine : au centre, la température "
                    "(5 000-6 000°C) dépasse le point de fusion du fer à "
                    "pression normale (1 538°C). Pourtant la graine est "
                    "solide : la pression colossale (360 GPa) élève le "
                    "point de fusion du fer au-dessus de la température "
                    "régnante. L'état physique dépend à la fois de T et P.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=11.9,
        )
        paradoxe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons par le paradoxe de la graine, point clé de ce "
                "chapitre. Au centre de la Terre, la température, cinq "
                "mille à six mille degrés, dépasse largement le point de "
                "fusion du fer à pression normale, mille cinq cent "
                "trente-huit degrés. Et pourtant, la graine est solide : la "
                "pression colossale, trois cent soixante gigapascals, élève "
                "le point de fusion du fer bien au-dessus de la température "
                "régnante. L'état physique d'une enveloppe dépend donc "
                "toujours à la fois de la température et de la pression, "
                "jamais de l'une seule."
            )
        ) as tracker:
            self.play(FadeIn(paradoxe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(paradoxe))
