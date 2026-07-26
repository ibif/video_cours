"""
scenes/SVT_EchangesCationiquesSol_04.py — Chapitre 9 (1ereC, SVT), scène 04.

L'adsorption et la désorption : définitions, réversibilité, mécanisme
d'échange cationique à charge égale (électroneutralité), deux exemples
d'échanges avec équations (Ca2+ chasse 2K+ ; 2H+ chasse Ca2+), et méthode
point clé « équilibre dynamique ». Source : 1ereC/SVT.pdf, pages 98-99.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class AdsorptionEtDesorption(NotionScene):
    def construct(self):
        titre = scene_title("9.3 — Adsorption et désorption des ions")
        titre.scale(0.66)
        titre.to_edge(UP)

        # --- Énoncé : les cations ne sont pas prisonniers -------------------
        intro = Text(
            _wrap(
                "Les charges négatives du complexe argilo-humique "
                "attirent les cations : mais ces cations restent-ils "
                "prisonniers du complexe pour toujours, ou peuvent-ils en "
                "repartir ?",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les charges négatives du complexe argilo-humique "
                "attirent les cations de la solution du sol. Mais ces "
                "cations restent-ils prisonniers du complexe pour "
                "toujours, ou peuvent-ils en repartir ? C'est tout "
                "l'objet des deux phénomènes que nous allons étudier : "
                "l'adsorption et la désorption."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définitions adsorption / désorption ------------
        def_adsorption = definition_box(
            Text(
                _wrap(
                    "L'adsorption est la fixation des cations de la "
                    "solution du sol sur la surface chargée négativement "
                    "du complexe argilo-humique. Les cations ainsi fixés "
                    "sont dits cations échangeables, ou ions adsorbés. "
                    "Attention : l'adsorption est une fixation en "
                    "surface, jamais à l'intérieur des particules.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_adsorption.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'adsorption est la fixation des cations de la solution "
                "du sol sur la surface chargée négativement du complexe "
                "argilo-humique. Les cations ainsi fixés sont dits "
                "cations échangeables, ou ions adsorbés. Attention : "
                "l'adsorption est une fixation en surface, et non à "
                "l'intérieur des particules. Elle est réversible."
            )
        ) as tracker:
            self.play(FadeIn(def_adsorption))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_adsorption))

        def_desorption = definition_box(
            Text(
                _wrap(
                    "La désorption est la libération, dans la solution "
                    "du sol, des cations précédemment adsorbés sur le "
                    "complexe argilo-humique. Ils sont remplacés sur le "
                    "complexe par d'autres cations : c'est le phénomène "
                    "d'échange cationique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_desorption.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "À l'inverse, la désorption est la libération, dans la "
                "solution du sol, des cations précédemment adsorbés sur "
                "le complexe argilo-humique. Ils sont alors remplacés sur "
                "le complexe par d'autres cations : c'est ce qu'on appelle "
                "le phénomène d'échange cationique."
            )
        ) as tracker:
            self.play(FadeIn(def_desorption))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_desorption))

        # --- Mécanisme : échange à charge égale + deux exemples ------------
        mecanisme_titre = Text(
            "Un échange à charge égale (électroneutralité)", font_size=24, color=YELLOW, weight="BOLD"
        )
        mecanisme_titre.next_to(titre, DOWN, buff=0.5)

        mecanisme_texte = Text(
            _wrap(
                "Un cation qui se fixe pousse un ou plusieurs cations "
                "porteurs d'une charge positive équivalente vers la "
                "solution.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        mecanisme_texte.next_to(mecanisme_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les échanges d'ions au niveau du sol sont donc des "
                "échanges de cations entre la solution du sol et le "
                "complexe argilo-humique. Cet échange se fait toujours à "
                "charge égale, on parle d'électroneutralité : un cation "
                "qui se fixe pousse un ou plusieurs cations porteurs "
                "d'une charge positive équivalente vers la solution."
            )
        ) as tracker:
            self.play(FadeIn(mecanisme_titre))
            self.play(FadeIn(mecanisme_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mecanisme_titre), FadeOut(mecanisme_texte))

        exemple1_label = Text("Exemple 1 : Ca2+ chasse deux K+", font_size=22, color=YELLOW, weight="BOLD")
        equation1 = MathTex(
            r"Ca^{2+}_{(solution)} + 2\,K^+_{(adsorb\acute{e})} "
            r"\;\rightleftharpoons\; Ca^{2+}_{(adsorb\acute{e})} + 2\,K^+_{(solution)}",
            font_size=28,
            color=WHITE,
        )
        bloc1 = VGroup(exemple1_label, equation1).arrange(DOWN, buff=0.3)
        bloc1.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Premier exemple : un ion calcium deux plus de la "
                "solution peut chasser deux ions potassium plus du "
                "complexe. L'équation montre bien l'équilibre des "
                "charges : une charge deux plus contre deux charges "
                "plus."
            )
        ) as tracker:
            self.play(FadeIn(exemple1_label))
            self.play(Write(equation1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc1))

        exemple2_label = Text("Exemple 2 : deux H+ chassent Ca2+", font_size=22, color=YELLOW, weight="BOLD")
        equation2 = MathTex(
            r"2\,H^+_{(solution)} + Ca^{2+}_{(adsorb\acute{e})} "
            r"\;\rightleftharpoons\; 2\,H^+_{(adsorb\acute{e})} + Ca^{2+}_{(solution)}",
            font_size=28,
            color=WHITE,
        )
        bloc2 = VGroup(exemple2_label, equation2).arrange(DOWN, buff=0.3)
        bloc2.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deuxième exemple : deux ions hydrogène de la solution, "
                "apportés par des pluies acides, peuvent chasser un ion "
                "calcium deux plus du complexe. Là encore, deux charges "
                "plus contre une charge deux plus : l'électroneutralité "
                "est respectée."
            )
        ) as tracker:
            self.play(FadeIn(exemple2_label))
            self.play(Write(equation2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc2))

        # --- À retenir : équilibre dynamique ---------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Point clé : les échanges cationiques sont "
                    "réversibles (double flèche). Il s'établit un "
                    "équilibre dynamique entre les cations adsorbés sur "
                    "le complexe et les cations libres dans la solution "
                    "du sol.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé : les échanges cationiques sont "
                "réversibles, comme le montre la double flèche des "
                "équations. Il s'établit en permanence un équilibre "
                "dynamique entre les cations adsorbés sur le complexe et "
                "les cations libres dans la solution du sol."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : adsorption n'est pas absorption ----------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : ne pas confondre adsorption "
                    "(fixation à la surface du complexe, dans le sol) et "
                    "absorption (entrée dans la racine, côté plante). Ce "
                    "sont deux phénomènes différents.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : ne confondez pas "
                "adsorption et absorption. L'adsorption est la fixation "
                "des cations à la surface du complexe, un phénomène qui "
                "se passe dans le sol. L'absorption, elle, est l'entrée "
                "des ions dans la racine, un phénomène qui se passe côté "
                "plante. Nous reviendrons sur cette distinction dans la "
                "scène suivante."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
