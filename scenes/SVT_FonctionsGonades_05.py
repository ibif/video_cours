"""
scenes/SVT_FonctionsGonades_05.py — Chapitre 1 (1ereD, SVT), scène 05.

§ 1.3.3 Structure de l'ovaire et ovogenèse : follicules ovariens, cycle de
28 jours, définition, calendrier fœtal -> ménopause, ovocyte I / II,
blocages de la méiose. Source : 1ereD/SVT.pdf, pages 11-12.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    Ellipse,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class StructureOvaireEtOvogenese(NotionScene):
    def construct(self):
        titre = scene_title("1.3 — Structure de l'ovaire et ovogenèse")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : schéma de l'ovaire et des follicules -----------------
        ovaire = Ellipse(width=7.5, height=3.2, color=WHITE, stroke_width=3)
        ovaire.next_to(titre, DOWN, buff=0.55)

        f_primordial = Circle(radius=0.18, color=ORANGE, fill_opacity=0.9).move_to(
            ovaire.get_center() + LEFT * 2.6 + UP * 0.4
        )
        f_primaire = Circle(radius=0.3, color=ORANGE, fill_opacity=0.9).move_to(
            ovaire.get_center() + LEFT * 1.2 + UP * 0.7
        )
        f_secondaire = Circle(radius=0.45, color=ORANGE, fill_opacity=0.9).move_to(
            ovaire.get_center() + UP * 0.5
        )
        f_mur = Circle(radius=0.65, color=YELLOW, fill_opacity=0.9).move_to(
            ovaire.get_center() + RIGHT * 1.6 + UP * 0.2
        )
        corps_jaune = Circle(radius=0.5, color=GREEN, fill_opacity=0.9).move_to(
            ovaire.get_center() + RIGHT * 2.6 + DOWN * 0.7
        )

        follicules = VGroup(f_primordial, f_primaire, f_secondaire, f_mur, corps_jaune)

        labels = VGroup(
            Text("primordial", font_size=15, color=WHITE).next_to(f_primordial, DOWN, buff=0.15),
            Text("primaire", font_size=15, color=WHITE).next_to(f_primaire, UP, buff=0.15),
            Text("secondaire", font_size=15, color=WHITE).next_to(f_secondaire, UP, buff=0.15),
            Text("mûr (De Graaf)", font_size=15, color=WHITE).next_to(f_mur, UP, buff=0.15),
            Text("corps jaune", font_size=15, color=WHITE).next_to(corps_jaune, DOWN, buff=0.15),
        )

        schema = VGroup(ovaire, follicules, labels)

        with self.voiceover(
            text=(
                "L'ovaire contient des follicules ovariens, de petites "
                "structures qui abritent chacune un ovocyte. Leur destin se "
                "déroule au rythme d'un cycle d'environ vingt-huit jours : un "
                "follicule primordial entre en croissance, devient follicule "
                "primaire puis secondaire, où apparaît une cavité, l'antrum, "
                "puis follicule mûr, dit follicule de De Graaf. Au "
                "quatorzième jour environ, la paroi de l'ovaire se rompt : "
                "c'est l'ovulation, qui libère l'ovocyte dans la trompe "
                "voisine. Le reste du follicule se transforme en corps "
                "jaune, qui régressera en corps blanc en l'absence de "
                "fécondation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(ovaire))
            self.play(FadeIn(follicules), FadeIn(labels))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        definition = definition_box(
            Text(
                _wrap(
                    "L'ovogenèse est l'ensemble des phénomènes qui, dans les "
                    "follicules ovariens, transforment une ovogonie en "
                    "ovule. Contrairement à la spermatogenèse, elle est "
                    "cyclique et ses produits sont peu nombreux.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'ovogenèse est l'ensemble des phénomènes qui, dans les "
                "follicules ovariens, transforment une ovogonie en ovule. "
                "Contrairement à la spermatogenèse, elle est cyclique et ses "
                "produits sont peu nombreux."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : le calendrier et les blocages de la méiose -----
        entete_cal = Text("Le calendrier de l'ovogenèse", font_size=26, color=YELLOW, weight="BOLD")
        entete_cal.next_to(titre, DOWN, buff=0.5)

        calendrier = _bullets(
            [
                "Vie fœtale : les ovogonies (2n=46) se multiplient, "
                "entrent en méiose, puis s'arrêtent : les ovocytes I "
                "restent bloqués en prophase de méiose I, dans les "
                "follicules primordiaux.",
                "Naissance : stock déjà constitué, environ 2 millions "
                "de follicules. Ce stock ne se renouvelle jamais.",
                "Puberté : il n'en reste qu'environ 400 000. À chaque "
                "cycle, un follicule arrive à maturité.",
            ],
            width=50,
        )
        calendrier.next_to(entete_cal, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le calendrier de l'ovogenèse distingue profondément les deux "
                "sexes. Pendant la vie fœtale, les ovogonies, à deux n égale "
                "quarante-six, se multiplient par mitoses puis entrent en "
                "méiose ; mais la première division s'interrompt : les "
                "ovocytes premiers restent bloqués en prophase de méiose un, "
                "à l'intérieur des follicules primordiaux. À la naissance, le "
                "stock est déjà constitué, environ deux millions de "
                "follicules, et il ne se renouvelle jamais. À la puberté, il "
                "n'en reste qu'environ quatre cent mille, et à chaque cycle, "
                "un seul follicule, en général, arrive à maturité."
            )
        ) as tracker:
            self.play(FadeIn(entete_cal))
            self.play(FadeIn(calendrier))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_cal), FadeOut(calendrier))

        # Chaîne des blocages de la méiose
        blocs_labels = [
            ("Ovocyte I", "2n=46", "bloqué en\nprophase I"),
            ("Ovocyte II", "n=23", "bloqué en\nmétaphase II"),
            ("Ovule", "n=23", "si fécondation"),
        ]
        blocs = VGroup()
        for nom, formule, blocage in blocs_labels:
            nom_txt = Text(nom, font_size=22, color=WHITE)
            formule_txt = MathTex(formule.replace("n=", "n = "), font_size=28, color=YELLOW)
            blocage_txt = Text(blocage, font_size=15, color=RED)
            bloc = VGroup(nom_txt, formule_txt, blocage_txt).arrange(DOWN, buff=0.12)
            blocs.add(bloc)
        blocs.arrange(RIGHT, buff=1.3)
        blocs.next_to(titre, DOWN, buff=0.9)

        fleches_b = VGroup(
            *[
                Arrow(blocs[i].get_right(), blocs[i + 1].get_left(), buff=0.1, color=WHITE)
                for i in range(len(blocs) - 1)
            ]
        )

        globules = Text(
            "(+ 2 à 3 globules polaires, qui dégénèrent)", font_size=18, color=WHITE
        )
        globules.next_to(blocs, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À chaque cycle, l'ovocyte premier achève la méiose un juste "
                "avant l'ovulation et donne deux cellules inégales : un gros "
                "ovocyte second, à n égale vingt-trois, et un tout petit "
                "premier globule polaire, sans avenir. L'ovocyte second "
                "commence la méiose deux, mais se bloque en métaphase : cette "
                "deuxième division ne s'achève que s'il y a fécondation, "
                "produisant alors l'ovule et un deuxième globule polaire. Les "
                "globules polaires dégénèrent."
            )
        ) as tracker:
            self.play(FadeIn(blocs))
            self.play(FadeIn(fleches_b))
            self.play(FadeIn(globules))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(blocs), FadeOut(fleches_b), FadeOut(globules))

        # --- Exemple traité : bilan d'un ovocyte I ---------------------------
        entete_ex = Text("Exemple traité", font_size=27, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        bilan = MathTex(
            r"1 \text{ ovocyte I} \;\longrightarrow\; 1 \text{ ovule} + 2\text{-}3 \text{ globules polaires}",
            font_size=28,
            color=WHITE,
        )
        bilan.next_to(entete_ex, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Bilan : un ovocyte premier ne donne qu'un seul gamète "
                "fonctionnel, l'ovule, accompagné de deux à trois globules "
                "polaires voués à disparaître. Au cours de sa vie, une femme "
                "n'ovule qu'environ quatre cent cinquante à cinq cents fois."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(bilan))

        # --- À retenir : chiffres clés du stock ovarien ----------------------
        entete_chiffres = Text("À retenir — le stock ovarien", font_size=26, color=YELLOW, weight="BOLD")
        entete_chiffres.next_to(titre, DOWN, buff=0.5)

        chiffres = _bullets(
            [
                "Environ 2 millions de follicules à la naissance.",
                "Environ 400 000 à la puberté ; le stock ne se "
                "renouvelle jamais.",
                "Environ 450 à 500 ovulations au cours d'une vie de "
                "femme.",
            ],
            width=48,
        )
        chiffres.next_to(entete_chiffres, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : environ deux millions de follicules sont "
                "présents à la naissance, il n'en reste qu'environ quatre "
                "cent mille à la puberté, et le stock ne se renouvelle "
                "jamais ; au total, une femme n'ovule qu'environ quatre cent "
                "cinquante à cinq cents fois dans sa vie."
            )
        ) as tracker:
            self.play(FadeIn(entete_chiffres))
            self.play(FadeIn(chiffres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_chiffres), FadeOut(chiffres))

        # --- Piège à éviter : ovocyte II n'est pas encore un ovule ----------
        piege = warning_box(
            Text(
                _wrap(
                    "L'ovaire libère à l'ovulation un ovocyte II, pas un "
                    "ovule : l'ovocyte II ne devient un ovule qu'après la "
                    "fécondation, quand la méiose II s'achève enfin. Avant "
                    "cela, il reste bloqué en métaphase II.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention : l'ovaire libère à l'ovulation un ovocyte second, "
                "pas encore un ovule. L'ovocyte second ne devient un ovule "
                "qu'après la fécondation, quand la méiose deux s'achève "
                "enfin. Avant cela, il reste bloqué en métaphase deux."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
