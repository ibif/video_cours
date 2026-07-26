"""
scenes/SVT_EcosystemeAgroIndustriel_08.py — Chapitre 11 (1ereC, SVT), scène 08.

§ 4.1-4.2 Les flux de matière et d'énergie (1/2) : la source d'énergie
(Soleil, photosynthèse, PPB/PPN), le devenir de l'énergie à chaque niveau
trophique (non consommée / égestée / assimilée -> respiration +
production), et le théorème de la loi de Lindeman (flux unidirectionnel
et décroissant, 80-95% perdu). Source : 1ereC/SVT.pdf, pages 124-125.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, FadeIn, FadeOut, MathTex, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class FluxMatiereEtEnergie1(NotionScene):
    def construct(self):
        titre = scene_title("4.1-4.2 — Les flux de matière et d'énergie (1/2)")
        titre.scale(0.52)
        titre.to_edge(UP)

        # --- Énoncé : le Soleil, source d'énergie ---------------------------
        intro = Text(
            _wrap(
                "L'énergie entre dans l'écosystème sous forme de "
                "rayonnement solaire. Seuls les producteurs peuvent la "
                "capter, grâce à la photosynthèse.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous savons maintenant qui mange qui. Reste à comprendre "
                "comment la matière et l'énergie circulent réellement dans "
                "l'écosystème. L'énergie entre dans l'écosystème sous "
                "forme de rayonnement solaire, et seuls les producteurs "
                "peuvent la capter, grâce à la photosynthèse."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        equation = MathTex(
            r"6\,CO_2 + 6\,H_2O \longrightarrow C_6H_{12}O_6 + 6\,O_2",
            font_size=32,
            color=YELLOW,
        )
        equation.next_to(titre, DOWN, buff=0.6)
        legende_eq = Text("en présence de lumière et de chlorophylle", font_size=18, color=WHITE)
        legende_eq.next_to(equation, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "La réaction globale de la photosynthèse : six molécules "
                "de dioxyde de carbone et six molécules d'eau donnent une "
                "molécule de glucose et six molécules de dioxygène, en "
                "présence de lumière et de chlorophylle. L'énergie "
                "lumineuse est ainsi convertie en énergie chimique, "
                "stockée dans la matière organique : glucose, puis "
                "cellulose, protéines, lipides."
            )
        ) as tracker:
            self.play(Write(equation))
            self.play(FadeIn(legende_eq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation), FadeOut(legende_eq))

        # --- Raisonnement : PPB et PPN ----------------------------------------
        ppb_ppn = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Productivité primaire brute (PPB) : quantité "
                        "totale de matière organique (ou d'énergie) "
                        "fabriquée par les producteurs par unité de "
                        "surface et de temps.",
                        width=52,
                    ),
                    font_size=19,
                ),
                Text(
                    _wrap(
                        "Productivité primaire nette (PPN) : ce qui reste "
                        "après la respiration des producteurs.",
                        width=52,
                    ),
                    font_size=19,
                ),
                MathTex(r"PPN = PPB - R", font_size=28, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
            box_width=11.8,
        )
        ppb_ppn.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "On distingue deux grandeurs. La productivité primaire "
                "brute, PPB, est la quantité totale de matière organique, "
                "ou d'énergie, fabriquée par les producteurs, par unité de "
                "surface et de temps. La productivité primaire nette, PPN, "
                "est ce qui reste après que les producteurs ont consommé "
                "une partie de leur production pour leur propre "
                "respiration : PPN égale PPB moins R, où R est la "
                "respiration."
            )
        ) as tracker:
            self.play(FadeIn(ppb_ppn))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ppb_ppn))

        # --- Exemple traité : le devenir de l'énergie chez un consommateur ---
        devenir_titre = Text("Le devenir de l'énergie ingérée par un consommateur", font_size=21, color=YELLOW, weight="BOLD")
        devenir_titre.next_to(titre, DOWN, buff=0.45)

        bloc_ingeree = Rectangle(width=8.5, height=0.7, fill_color="#5C6BC0", fill_opacity=0.85, stroke_color=WHITE, stroke_width=2)
        label_ingeree = Text("Énergie ingérée (100 %)", font_size=17, color=WHITE, weight="BOLD")
        label_ingeree.move_to(bloc_ingeree)

        bloc_nonconso = Rectangle(width=1.8, height=0.6, fill_color="#8D6E63", fill_opacity=0.85, stroke_width=1.5, stroke_color=WHITE)
        bloc_egestee = Rectangle(width=2.2, height=0.6, fill_color="#A1887F", fill_opacity=0.85, stroke_width=1.5, stroke_color=WHITE)
        bloc_respiration = Rectangle(width=2.7, height=0.6, fill_color="#EF5350", fill_opacity=0.85, stroke_width=1.5, stroke_color=WHITE)
        bloc_production = Rectangle(width=1.5, height=0.6, fill_color="#66BB6A", fill_opacity=0.85, stroke_width=1.5, stroke_color=WHITE)

        label_nonconso = Text("non\nconsommée", font_size=12, color=WHITE)
        label_egestee = Text("égestée\n(excréments)", font_size=12, color=WHITE)
        label_respiration = Text("respiration\n(perdue)", font_size=12, color=WHITE)
        label_production = Text("production\n(transmise)", font_size=12, color="#1A1A1A", weight="BOLD")

        for bloc, label in [
            (bloc_nonconso, label_nonconso),
            (bloc_egestee, label_egestee),
            (bloc_respiration, label_respiration),
            (bloc_production, label_production),
        ]:
            label.move_to(bloc)

        ligne_sortie = VGroup(bloc_nonconso, bloc_egestee, bloc_respiration, bloc_production).arrange(RIGHT, buff=0.15)
        groupe_labels = VGroup(label_nonconso, label_egestee, label_respiration, label_production)
        for bloc, label in [
            (bloc_nonconso, label_nonconso),
            (bloc_egestee, label_egestee),
            (bloc_respiration, label_respiration),
            (bloc_production, label_production),
        ]:
            label.move_to(bloc)

        fleche_repartition = Arrow(bloc_ingeree.get_bottom(), ligne_sortie.get_top() + UP * 0.05, buff=0.05, color=YELLOW, stroke_width=3)

        schema_energie = VGroup(bloc_ingeree, label_ingeree, fleche_repartition, ligne_sortie, groupe_labels)
        schema_energie.arrange(DOWN, buff=0.35)
        schema_energie.next_to(devenir_titre, DOWN, buff=0.4)

        seule_prod_note = Text(
            "Seule la part « production » (croissance, reproduction) est transmise au niveau suivant.",
            font_size=16,
            color="#FFD54F",
        )
        seule_prod_note.next_to(schema_energie, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Quand un consommateur mange un organisme, l'énergie "
                "contenue dans sa proie se répartit en trois parts : "
                "l'énergie non consommée, os, poils, racines ; l'énergie "
                "égestée dans les excréments ; et l'énergie assimilée, qui "
                "sert d'une part à la respiration, chaleur, mouvement, "
                "fonctionnement des organes, une part perdue pour "
                "l'écosystème, et d'autre part à la production de "
                "nouvelle matière vivante, croissance, reproduction. Seule "
                "cette dernière part, la production, est transmissible au "
                "niveau trophique suivant."
            )
        ) as tracker:
            self.play(FadeIn(devenir_titre))
            self.play(FadeIn(bloc_ingeree), FadeIn(label_ingeree))
            self.play(FadeIn(fleche_repartition))
            self.play(FadeIn(ligne_sortie), FadeIn(groupe_labels))
            self.play(FadeIn(seule_prod_note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(devenir_titre), FadeOut(schema_energie), FadeOut(seule_prod_note))

        # --- À retenir : le théorème de Lindeman -------------------------------
        lindeman = theorem_box(
            Text(
                _wrap(
                    "Loi de Lindeman (1942) : le flux d'énergie dans un "
                    "écosystème est unidirectionnel et décroissant : il va "
                    "toujours des producteurs vers les consommateurs, en "
                    "diminuant à chaque niveau trophique. L'énergie ne "
                    "peut pas être recyclée ; seule la matière l'est. À "
                    "chaque transfert, environ 80 à 95 % de l'énergie est "
                    "perdue.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        lindeman.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la loi de Lindeman, énoncée en mille neuf cent "
                "quarante-deux : le flux d'énergie dans un écosystème est "
                "unidirectionnel et décroissant. Il va toujours des "
                "producteurs vers les consommateurs, en diminuant à chaque "
                "niveau trophique. L'énergie ne peut pas être recyclée ; "
                "seule la matière l'est. Conséquence fondamentale : à "
                "chaque passage d'un niveau trophique au suivant, environ "
                "quatre-vingts à quatre-vingt-quinze pour cent de "
                "l'énergie est perdue, surtout par la respiration, et "
                "seulement cinq à vingt pour cent est transmise. C'est "
                "pourquoi les chaînes alimentaires comptent peu de "
                "maillons."
            )
        ) as tracker:
            self.play(FadeIn(lindeman))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(lindeman))
