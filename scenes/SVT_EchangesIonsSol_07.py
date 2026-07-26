"""
scenes/SVT_EchangesIonsSol_07.py — Chapitre 8 (1ereD, SVT), scène 07.

§ 8.3.3-8.3.4 Absorption passive et absorption active, sélectivité de
l'absorption : définitions, trois preuves expérimentales de l'absorption
active, propriété de sélectivité, exemple du tableau de dosages
K+/NO3-/Ca2+/Na+, méthode pour analyser un tableau de dosages.
Source : 1ereD/SVT.pdf, pages 110-112.
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
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class AbsorptionActiveEtSelective(NotionScene):
    def construct(self):
        titre = scene_title("8.3 — Absorption passive, active et sélective")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : deux définitions -------------------------------------
        def_passive = definition_box(
            Text(
                _wrap(
                    "L'absorption passive : entrée d'ions dans les "
                    "cellules racinaires sans dépense d'énergie, dans le "
                    "sens du gradient de concentration (diffusion, du "
                    "plus concentré vers le moins concentré). Certains "
                    "ions sont entraînés passivement par le courant "
                    "d'eau absorbée.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_passive.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Comment les ions entrent-ils exactement dans les cellules "
                "de la racine ? On distingue deux mécanismes. L'absorption "
                "passive : c'est l'entrée d'ions dans les cellules "
                "racinaires sans dépense d'énergie, dans le sens du "
                "gradient de concentration, c'est-à-dire par simple "
                "diffusion, du milieu le plus concentré vers le moins "
                "concentré. Certains ions sont aussi simplement entraînés "
                "par le courant d'eau absorbée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_passive))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_passive))

        def_active = definition_box(
            Text(
                _wrap(
                    "L'absorption active : entrée d'ions contre le "
                    "gradient de concentration (du moins concentré vers "
                    "le plus concentré). Exige de l'énergie (ATP de la "
                    "respiration cellulaire) et des transporteurs "
                    "membranaires spécifiques.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_active.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'absorption active, à l'inverse : c'est l'entrée d'ions "
                "contre le gradient de concentration, du milieu le moins "
                "concentré vers le plus concentré. Ce mécanisme exige de "
                "l'énergie, fournie par l'ATP de la respiration "
                "cellulaire, ainsi que des transporteurs membranaires "
                "spécifiques, de véritables pompes moléculaires."
            )
        ) as tracker:
            self.play(FadeIn(def_active))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_active))

        # --- Raisonnement / exemple : trois preuves de l'absorption active -
        preuves = example_box(
            _bullets(
                [
                    "1. Accumulation contre gradient : la sève des "
                    "cellules racinaires peut être 10-100x plus "
                    "concentrée en K+ que le sol -> diffusion seule ne "
                    "l'explique pas.",
                    "2. Rôle de la respiration : plantules barbotées "
                    "d'air absorbent presque tout le K+ en 24h ; sans "
                    "O2, presque rien (pas d'ATP).",
                    "3. Effet de la température : à 5°C, absorption très "
                    "ralentie vs 25°C -> processus enzymatique, pas une "
                    "simple diffusion.",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.2,
        )
        preuves.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Trois preuves expérimentales démontrent l'existence de "
                "cette absorption active. Première preuve : l'accumulation "
                "contre le gradient. La sève des cellules racinaires peut "
                "être dix à cent fois plus concentrée en potassium que la "
                "solution du sol : la diffusion seule ne peut pas "
                "l'expliquer, il faut un pompage actif. Deuxième preuve : "
                "le rôle de la respiration. On compare deux lots de "
                "plantules dans la même solution ; un lot est barboté "
                "d'air, l'autre d'azote, sans dioxygène. Résultat : le "
                "premier lot absorbe presque tout le potassium en "
                "vingt-quatre heures, le second presque rien - sans "
                "dioxygène, pas d'ATP, et l'absorption s'effondre. "
                "Troisième preuve : l'effet de la température. À cinq "
                "degrés, l'absorption est très ralentie par rapport à "
                "vingt-cinq degrés, signe d'un processus enzymatique, et "
                "non d'une simple diffusion physique."
            )
        ) as tracker:
            self.play(FadeIn(preuves))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(preuves))

        # --- Raisonnement : la sélectivité de l'absorption ------------------
        prop_selectivite = property_box(
            Text(
                _wrap(
                    "L'absorption est sélective : la plante n'absorbe pas "
                    "les ions dans les proportions de la solution du sol. "
                    "Grâce à ses transporteurs spécifiques, elle pompe un "
                    "ion utile même rare (contre gradient), et ne retient "
                    "qu'une faible part d'un ion abondant mais peu utile "
                    "(sodium).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        prop_selectivite.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Autre propriété remarquable : l'absorption est "
                "sélective. La plante n'absorbe pas les ions dans les "
                "mêmes proportions que la solution du sol. Grâce à ses "
                "transporteurs spécifiques, elle pompe un ion utile même "
                "s'il est rare, contre son gradient, et ne retient qu'une "
                "faible part d'un ion abondant mais peu utile, comme le "
                "sodium."
            )
        ) as tracker:
            self.play(FadeIn(prop_selectivite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_selectivite))

        # --- Exemple traité : tableau des dosages avant/après --------------
        tab_titre = Text("Dosages avant / après 8 jours de culture (mg/L)", font_size=22, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.4)

        entetes = VGroup(
            Text("Ion", font_size=20, color=WHITE, weight="BOLD"),
            Text("Initial", font_size=20, color=WHITE, weight="BOLD"),
            Text("Après 8j", font_size=20, color=WHITE, weight="BOLD"),
        )
        lignes_data = [
            ("K+", "39", "4", RED),
            ("NO3−", "62", "6", RED),
            ("Ca2+", "80", "70", GREEN),
            ("Na+", "23", "21", GREEN),
        ]
        col_ion = VGroup(entetes[0], *[Text(l[0], font_size=19, color=l[3]) for l in lignes_data])
        col_init = VGroup(entetes[1], *[Text(l[1], font_size=19, color=WHITE) for l in lignes_data])
        col_final = VGroup(entetes[2], *[Text(l[2], font_size=19, color=WHITE) for l in lignes_data])
        col_ion.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        col_init.arrange(DOWN, buff=0.28)
        col_final.arrange(DOWN, buff=0.28)
        tableau = VGroup(col_ion, col_init, col_final).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        tableau.next_to(tab_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici la preuve expérimentale de cette sélectivité. On "
                "dose quatre ions dans une solution nutritive, avant et "
                "après huit jours de culture. Le potassium passe de "
                "trente-neuf à quatre milligrammes par litre. Le nitrate "
                "passe de soixante-deux à six. Le calcium, lui, passe "
                "seulement de quatre-vingts à soixante-dix. Le sodium, de "
                "vingt-trois à vingt et un. Le potassium et le nitrate ont "
                "presque disparu, preuve d'une forte absorption ; le "
                "calcium et le sodium ont peu varié. La plante a bel et "
                "bien choisi ses ions - et l'on remarque que l'absorption "
                "des ions est indépendante de l'absorption de l'eau."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- À retenir / méthode : analyser un tableau de dosages -----------
        methode = method_box(
            _bullets(
                [
                    "1. Pour chaque ion, calculer la variation "
                    "Δ = c finale − c initiale (ou % absorbé).",
                    "2. Comparer les variations entre les différents "
                    "ions.",
                    "3. Conclure à la sélectivité si les variations "
                    "diffèrent nettement.",
                    "4. Conclure à une absorption active si la "
                    "concentration externe finale d'un ion absorbé est "
                    "inférieure à sa concentration interne.",
                ],
                font_size=19,
                width=56,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons la méthode pour analyser un tableau de dosages "
                "d'ions avant et après culture. Étape un : pour chaque "
                "ion, calculer la variation, c'est-à-dire la "
                "concentration finale moins la concentration initiale, ou "
                "le pourcentage absorbé. Étape deux : comparer les "
                "variations entre les différents ions. Étape trois : "
                "conclure à la sélectivité si les variations diffèrent "
                "nettement d'un ion à l'autre. Étape quatre : conclure à "
                "une absorption active si un ion absorbé se retrouve, à "
                "l'extérieur, à une concentration finale inférieure à sa "
                "concentration à l'intérieur de la racine."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : sélectivité ≠ absorption active ----------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre les deux notions. La sélectivité "
                    "répond à « quel ion ? » (la plante choisit certains "
                    "ions plutôt que d'autres). Le caractère actif "
                    "répond à « comment ? » (contre le gradient, avec "
                    "dépense d'énergie). Un ion peut être absorbé "
                    "sélectivement sans que ce soit forcément actif, et "
                    "inversement.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre ces deux notions. La "
                "sélectivité répond à la question quel ion : la plante "
                "choisit certains ions plutôt que d'autres. Le caractère "
                "actif répond à la question comment : contre le gradient "
                "de concentration, avec une dépense d'énergie. Un ion peut "
                "être absorbé sélectivement sans que ce soit forcément un "
                "transport actif, et inversement : les deux notions sont "
                "liées mais distinctes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
