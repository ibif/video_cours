"""
scenes/SVT_FonctionsGonades_07.py — Chapitre 1 (1ereD, SVT), scène 07.

§ 1.4.1-1.4.2 Les hormones sexuelles : testostérone (cellules de Leydig),
œstrogènes et progestérone (follicules / corps jaune), tableau résumé.
Source : 1ereD/SVT.pdf, pages 13-14.

Note de structure : le texte source ne présente pas d'EXEMPLE dédié pour
cette sous-section (l'exemple du dosage hormonal est traité en scène 08,
§ 1.4.3) ; le "tableau résumé" du manuel tient ici le rôle d'« à retenir ».
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class HormonesSexuelles(NotionScene):
    def construct(self):
        titre = scene_title("1.4 — Les hormones sexuelles")
        titre.scale(0.75)
        titre.to_edge(UP)

        # --- Énoncé : définition de l'hormone sexuelle -----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une hormone sexuelle est une substance chimique "
                    "produite par une gonade, libérée dans le sang, et qui "
                    "agit à distance sur des organes cibles : appareil "
                    "génital, mais aussi larynx, peau, os, muscles, "
                    "cerveau.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une hormone sexuelle est une substance chimique produite par "
                "une gonade, libérée dans le sang, et qui agit à distance sur "
                "des organes cibles : l'appareil génital, mais aussi le "
                "larynx, la peau, les os, les muscles ou le cerveau."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement 1 : la testostérone ---------------------------------
        entete_t = Text("1.4.1 — La testostérone, hormone mâle", font_size=26, color=YELLOW, weight="BOLD")
        entete_t.next_to(titre, DOWN, buff=0.5)

        testosterone = _bullets(
            [
                "Sécrétée par les cellules interstitielles de Leydig, "
                "entre les tubes séminifères.",
                "Localisée grâce à la ligature (§1.2.3) : quand les "
                "tubes dégénèrent, l'hormone persiste tant que les "
                "cellules de Leydig demeurent.",
                "À la puberté : caractères sexuels secondaires mâles "
                "(voix, barbe, musculature).",
                "À l'âge adulte : entretient ces caractères, la "
                "spermatogenèse et le comportement sexuel.",
            ],
            width=50,
        )
        testosterone.next_to(entete_t, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La testostérone est sécrétée par les cellules interstitielles "
                "de Leydig, situées entre les tubes séminifères. C'est "
                "l'expérience de ligature qui a permis de localiser cette "
                "production : quand les tubes séminifères dégénèrent, "
                "l'hormone persiste tant que les cellules interstitielles "
                "demeurent. Ses rôles sont multiples : à la puberté, elle "
                "provoque l'apparition des caractères sexuels secondaires "
                "mâles ; à l'âge adulte, elle maintient ces caractères, "
                "entretient la spermatogenèse et soutient le comportement "
                "sexuel."
            )
        ) as tracker:
            self.play(FadeIn(entete_t))
            self.play(FadeIn(testosterone))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_t), FadeOut(testosterone))

        # --- Raisonnement 2 : œstrogènes et progestérone -----------------------
        entete_o = Text("1.4.2 — Œstrogènes et progestérone", font_size=26, color=YELLOW, weight="BOLD")
        entete_o.next_to(titre, DOWN, buff=0.5)

        oestro_progest = _bullets(
            [
                "Œstrogènes (dont l'estradiol) : sécrétés par les "
                "follicules ovariens en croissance. Rôles : caractères "
                "sexuels secondaires féminins, reconstruction de la "
                "muqueuse utérine.",
                "Progestérone : sécrétée par le corps jaune. « Pro-"
                "gestation » : prépare la nidation, maintient la "
                "gestation, bloque les ovulations suivantes.",
            ],
            width=50,
        )
        oestro_progest.next_to(entete_o, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les œstrogènes, dont le principal est l'estradiol, sont "
                "sécrétés par les follicules ovariens en croissance. Ils "
                "provoquent à la puberté les caractères sexuels secondaires "
                "féminins et, à chaque cycle, stimulent la reconstruction de "
                "la muqueuse utérine. La progestérone, elle, est sécrétée par "
                "le corps jaune : son nom dit son rôle, pro-gestation. Elle "
                "achève de préparer l'utérus à une éventuelle nidation et, en "
                "cas de fécondation, maintient l'état de gestation et bloque "
                "les ovulations suivantes."
            )
        ) as tracker:
            self.play(FadeIn(entete_o))
            self.play(FadeIn(oestro_progest))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_o), FadeOut(oestro_progest))

        # --- À retenir : tableau résumé -----------------------------------------
        entete_tab = Text("Tableau résumé", font_size=27, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        noms = ["Hormone", "Testostérone", "Œstrogènes", "Progestérone"]
        gonades = ["Gonade", "Testicule", "Ovaire", "Ovaire"]
        structures = ["Structure productrice", "Cellules de Leydig", "Follicules en croissance", "Corps jaune"]
        roles = [
            "Rôles",
            "Caractères 2nd. mâles,\nspermatogenèse",
            "Caractères 2nd. féminins,\ndébut du cycle utérin",
            "Préparation et maintien\nde la gestation",
        ]

        col1 = VGroup(*[Text(n, font_size=19, color=(YELLOW if n == "Hormone" else WHITE), weight="BOLD" if n == "Hormone" else "NORMAL") for n in noms])
        col2 = VGroup(*[Text(n, font_size=17, color=(YELLOW if n == "Gonade" else WHITE), weight="BOLD" if n == "Gonade" else "NORMAL") for n in gonades])
        col3 = VGroup(*[Text(n, font_size=17, color=(YELLOW if n == "Structure productrice" else WHITE), weight="BOLD" if n == "Structure productrice" else "NORMAL") for n in structures])
        col4 = VGroup(*[Text(n, font_size=16, color=(YELLOW if n == "Rôles" else WHITE), weight="BOLD" if n == "Rôles" else "NORMAL") for n in roles])

        col1.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        col2.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        col3.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        col4.arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        tableau = VGroup(col1, col2, col3, col4).arrange(RIGHT, buff=0.55, aligned_edge=UP)
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        tableau.scale(0.95)

        with self.voiceover(
            text=(
                "Résumons dans un tableau : la testostérone, produite par le "
                "testicule, précisément par les cellules de Leydig, assure "
                "les caractères sexuels secondaires mâles et l'entretien de "
                "la spermatogenèse. Les œstrogènes, produits par l'ovaire, "
                "précisément par les follicules en croissance, assurent les "
                "caractères sexuels secondaires féminins et le début du "
                "cycle utérin. La progestérone, produite par l'ovaire, "
                "précisément par le corps jaune, prépare et maintient la "
                "gestation."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège à éviter : ne pas confondre les trois structures --------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas les trois structures productrices : "
                    "cellules de Leydig (testostérone) ≠ follicules en "
                    "croissance (œstrogènes) ≠ corps jaune (progestérone). "
                    "Ce sont trois structures différentes, dont deux "
                    "appartiennent au même ovaire mais à des moments "
                    "différents du cycle.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre les trois structures "
                "productrices : les cellules de Leydig produisent la "
                "testostérone, les follicules en croissance produisent les "
                "œstrogènes, et le corps jaune produit la progestérone. Ce "
                "sont trois structures différentes, dont deux appartiennent "
                "au même ovaire, mais à des moments différents du cycle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
