"""
scenes/SVT_StructureInterneGlobe_07.py — Chapitre 7 (1ereC, SVT), scène 07.

§ III.1 La discontinuité de Mohorovicic (Moho) : découverte (Mohorovičić,
1909), profondeur (5-12 km océans, 30-70 km continents), sépare
croûte/manteau, signature sismique (vP: 6 → 8 km/s) + remarque « racines
crustales des chaînes de montagnes ». Source : 1ereC/SVT.pdf, page 73.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Line, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class DiscontinuiteDeMoho(NotionScene):
    def construct(self):
        titre = scene_title("III.1 — La discontinuité de Mohorovicic (Moho)")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : la découverte d'Andrija Mohorovičić ---------------------
        intro = Text(
            _wrap(
                "En 1909, le sismologue croate Andrija Mohorovičić étudie un "
                "séisme de la région de Zagreb. Il remarque un saut brutal "
                "de la vitesse des ondes à une certaine profondeur : la "
                "première grande discontinuité vient d'être découverte.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En mille neuf cent neuf, le sismologue croate Andrija "
                "Mohorovičić étudie les ondes d'un séisme de la région de "
                "Zagreb. Il remarque un saut brutal de la vitesse des ondes "
                "à une certaine profondeur : la première grande "
                "discontinuité de l'histoire de la sismologie vient d'être "
                "découverte."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définition / caractérisation de la discontinuité de Moho --------
        definition = definition_box(
            Text(
                _wrap(
                    "Le Moho sépare la croûte du manteau. Sa profondeur est "
                    "variable : 5 à 12 km sous les océans (moyenne ~7 km) et "
                    "30 à 70 km sous les continents (moyenne 35-40 km ; "
                    "jusqu'à 70 km sous les jeunes chaînes de montagnes "
                    "comme l'Himalaya). Signature : vP passe brutalement "
                    "d'environ 6 à 8 km/s.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le Moho sépare la croûte du manteau. Sa profondeur est "
                "variable : cinq à douze kilomètres sous les océans, en "
                "moyenne sept kilomètres, et trente à soixante-dix "
                "kilomètres sous les continents, en moyenne trente-cinq à "
                "quarante kilomètres, jusqu'à soixante-dix kilomètres sous "
                "les jeunes chaînes de montagnes comme l'Himalaya. Sa "
                "signature sismique est une augmentation brutale de la "
                "vitesse des ondes P, qui passe d'environ six à huit "
                "kilomètres par seconde."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : coupe océan / continent avec Moho ---
        surface_oc = Line(LEFT * 3.4, LEFT * 0.3, color="#4DABF7", stroke_width=4)
        surface_oc.shift(UP * 1.3)
        croute_oc = VGroup(
            Line(LEFT * 3.4, LEFT * 0.3, color="#A9A9A9", stroke_width=30).shift(UP * 1.15),
        )
        moho_oc = Line(LEFT * 3.4, LEFT * 0.3, color=YELLOW, stroke_width=3).shift(UP * 1.0)
        label_moho_oc = Text("Moho (~7 km)", font_size=14, color=YELLOW)
        label_moho_oc.next_to(moho_oc, DOWN, buff=0.12).shift(LEFT * 0.4)

        surface_cont = Line(RIGHT * 0.3, RIGHT * 3.4, color="#87862B", stroke_width=4)
        surface_cont.shift(UP * 1.3)
        croute_cont = Line(RIGHT * 0.3, RIGHT * 3.4, color="#C2B280", stroke_width=30).shift(UP * 0.6)
        moho_cont = Line(RIGHT * 0.3, RIGHT * 3.4, color=YELLOW, stroke_width=3).shift(DOWN * 0.15)
        label_moho_cont = Text("Moho (~35-40 km)", font_size=14, color=YELLOW)
        label_moho_cont.next_to(moho_cont, DOWN, buff=0.12)

        manteau_label = Text("Manteau", font_size=15, color="#E8A33D")
        manteau_label.move_to(DOWN * 1.6)

        schema = VGroup(
            surface_oc, croute_oc, moho_oc, label_moho_oc,
            surface_cont, croute_cont, moho_cont, label_moho_cont,
            manteau_label,
        )
        schema.next_to(titre, DOWN, buff=0.4)

        label_oc = Text("Croûte océanique", font_size=15, color=WHITE)
        label_oc.next_to(schema, DOWN, buff=0.15).shift(LEFT * 2.0)
        label_cont = Text("Croûte continentale", font_size=15, color=WHITE)
        label_cont.next_to(schema, DOWN, buff=0.15).shift(RIGHT * 2.0)

        with self.voiceover(
            text=(
                "Ce schéma compare une coupe sous un océan et une coupe sous "
                "un continent. Sous l'océan, à gauche, la croûte est mince "
                "et le Moho se trouve tout près de la surface, vers sept "
                "kilomètres. Sous le continent, à droite, la croûte est "
                "beaucoup plus épaisse, et le Moho descend jusqu'à trente-"
                "cinq ou quarante kilomètres, formant une véritable racine "
                "plongeant dans le manteau."
            )
        ) as tracker:
            self.play(FadeIn(surface_oc), FadeIn(croute_oc))
            self.play(FadeIn(moho_oc), FadeIn(label_moho_oc))
            self.play(FadeIn(surface_cont), FadeIn(croute_cont))
            self.play(FadeIn(moho_cont), FadeIn(label_moho_cont))
            self.play(FadeIn(manteau_label), FadeIn(label_oc), FadeIn(label_cont))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(label_oc), FadeOut(label_cont))

        # --- Exemple traité : lire un profil de vitesse au passage du Moho ---
        exemple = example_box(
            Text(
                _wrap(
                    "Un sismomètre enregistre vP=5,9 km/s jusqu'à 38 km de "
                    "profondeur, puis vP=8,1 km/s juste en dessous. Où se "
                    "situe le Moho, et quelle croûte est traversée ?",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : un sismomètre enregistre une vitesse des "
                "ondes P de cinq virgule neuf kilomètres par seconde "
                "jusqu'à trente-huit kilomètres de profondeur, puis huit "
                "virgule un kilomètres par seconde juste en dessous. Où se "
                "situe le Moho, et quelle croûte est traversée ?"
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        resolution = Text(
            _wrap(
                "Résolution : le saut brutal de vitesse à 38 km signe le "
                "Moho. Une profondeur de 38 km, comprise entre 30 et 70 km, "
                "correspond à une croûte continentale.",
                width=52,
            ),
            font_size=21,
            color=YELLOW,
        )
        resolution.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résolution : le saut brutal de la vitesse à trente-huit "
                "kilomètres de profondeur signe le passage du Moho. Une "
                "profondeur de trente-huit kilomètres, comprise entre "
                "trente et soixante-dix kilomètres, correspond bien à une "
                "croûte continentale, et non océanique."
            )
        ) as tracker:
            self.play(FadeIn(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(resolution))

        # --- À retenir + remarque des racines crustales -----------------------
        retenir = _bullets(
            [
                "Moho (1909, Mohorovičić) : sépare croûte et manteau.",
                "Profondeur : 5-12 km (océans) ; 30-70 km (continents).",
                "Signature : vP saute brutalement de ~6 à ~8 km/s.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : le Moho, découvert par Mohorovičić en mille "
                "neuf cent neuf, sépare la croûte du manteau. Sa profondeur "
                "varie de cinq à douze kilomètres sous les océans, à trente "
                "à soixante-dix kilomètres sous les continents. Sa "
                "signature est un saut brutal de la vitesse des ondes P, "
                "d'environ six à huit kilomètres par seconde."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège / remarque : le Moho n'est pas plat -------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le Moho est plus profond sous les continents que sous "
                    "les océans : la croûte continentale est donc beaucoup "
                    "plus épaisse. Les chaînes de montagnes possèdent des "
                    "« racines » crustales enfoncées dans le manteau — ne "
                    "pas imaginer une croûte d'épaisseur constante partout.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : ne pas imaginer une croûte "
                "d'épaisseur constante partout sur le globe. Le Moho est "
                "bien plus profond sous les continents que sous les "
                "océans : la croûte continentale est donc beaucoup plus "
                "épaisse. Les chaînes de montagnes possèdent même des "
                "racines crustales, enfoncées dans le manteau, à l'image "
                "d'un iceberg dont la partie immergée est bien plus "
                "importante que la partie visible."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
