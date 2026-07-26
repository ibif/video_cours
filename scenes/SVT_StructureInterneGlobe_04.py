"""
scenes/SVT_StructureInterneGlobe_04.py — Chapitre 7 (1ereC, SVT), scène 04.

§ II.1 Séisme, foyer, épicentre (définitions) + § II.2.a Les ondes P (ondes
primaires : longitudinales, se propagent dans les solides ET les liquides,
les plus rapides, vitesses 6 → 13,7 km/s). Source : 1ereC/SVT.pdf, page 72.
"""

import textwrap

from manim import DOWN, LEFT, ORANGE, RED, RIGHT, UP, WHITE, YELLOW, Circle, Dot, FadeIn, FadeOut, Line, Text, VGroup, Write

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


class SeismeFoyerEpicentreEtOndesP(NotionScene):
    def construct(self):
        titre = scene_title("II.1-II.2 — Séisme, foyer, épicentre et ondes P")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : qu'est-ce qu'un séisme ? --------------------------------
        intro = Text(
            _wrap(
                "Un séisme est une vibration brève et brutale du sol, "
                "provoquée par la rupture brutale des roches en profondeur, "
                "qui libère de l'énergie sous forme d'ondes.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un séisme, ou tremblement de terre, est une vibration "
                "brève et brutale du sol, provoquée par la rupture brutale "
                "des roches en profondeur, qui libère de l'énergie sous "
                "forme d'ondes sismiques."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définitions foyer / épicentre ------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le foyer (ou hypocentre) est le point, en profondeur, "
                    "où se produit la rupture des roches à l'origine du "
                    "séisme. L'épicentre est le point de la surface "
                    "terrestre situé à la verticale du foyer : c'est là que "
                    "les dégâts sont généralement les plus importants.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le foyer, ou hypocentre, est le point, en profondeur, où se "
                "produit la rupture des roches à l'origine du séisme. "
                "L'épicentre est le point de la surface terrestre situé à la "
                "verticale du foyer : c'est là que les dégâts sont "
                "généralement les plus importants."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma foyer / épicentre / ondes ----
        surface = Line(LEFT * 3.3, RIGHT * 3.3, color=WHITE, stroke_width=4)
        surface.shift(UP * 1.4)
        foyer = Dot(point=DOWN * 0.8 + LEFT * 0.6, color=RED, radius=0.09)
        epicentre_pos = foyer.get_center()[0] * RIGHT + surface.get_center()[1] * UP
        epicentre = Dot(point=epicentre_pos, color=YELLOW, radius=0.09)
        verticale = Line(foyer.get_center(), epicentre.get_center(), color=YELLOW, stroke_width=3)

        label_surface = Text("Surface", font_size=17, color=WHITE)
        label_surface.next_to(surface, LEFT, buff=0.2).shift(UP * 0.1)
        label_foyer = Text("Foyer (hypocentre)", font_size=17, color=RED)
        label_foyer.next_to(foyer, DOWN, buff=0.3)
        label_epicentre = Text("Épicentre", font_size=17, color=YELLOW)
        label_epicentre.next_to(epicentre, UP, buff=0.3)

        ondes = VGroup(
            *[Circle(radius=r, color=ORANGE, stroke_width=2).move_to(foyer.get_center()) for r in [0.45, 0.85, 1.25]]
        )
        sismographe = Dot(point=surface.get_center() + RIGHT * 2.6, color="#4DABF7", radius=0.08)
        label_sismo = Text("Sismographe", font_size=15, color="#4DABF7")
        label_sismo.next_to(sismographe, UP, buff=0.2)

        schema = VGroup(surface, foyer, epicentre, verticale, label_surface, label_foyer, label_epicentre, sismographe, label_sismo)
        schema.next_to(titre, DOWN, buff=0.5)
        ondes.move_to(foyer.get_center())

        with self.voiceover(
            text=(
                "Sur ce schéma, la surface du sol est en haut. Le foyer, en "
                "profondeur, est le point de rupture. L'épicentre, à sa "
                "verticale exacte en surface, est là où les secousses sont "
                "les plus fortes. Les vibrations émises au foyer se "
                "propagent dans toutes les directions : ce sont les ondes "
                "sismiques, enregistrées en surface par des appareils "
                "appelés sismographes, qui tracent des sismogrammes."
            )
        ) as tracker:
            self.play(FadeIn(surface), FadeIn(label_surface))
            self.play(FadeIn(foyer), FadeIn(label_foyer))
            self.play(FadeIn(verticale), FadeIn(epicentre), FadeIn(label_epicentre))
            self.play(FadeIn(ondes))
            self.play(FadeIn(sismographe), FadeIn(label_sismo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(ondes))

        # --- Les ondes P -------------------------------------------------------
        ondes_p_def = definition_box(
            Text(
                _wrap(
                    "Ondes P (primaires) : ondes longitudinales (compression"
                    "-dilatation), vibration parallèle au sens de "
                    "propagation. Elles se propagent dans les SOLIDES et les "
                    "LIQUIDES. Ce sont les ondes les plus rapides : elles "
                    "arrivent en premier sur les sismogrammes.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        ondes_p_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voyons maintenant les ondes P, ou ondes primaires. Ce sont "
                "des ondes longitudinales, de compression-dilatation : les "
                "roches sont alternativement comprimées et dilatées, la "
                "vibration des particules se fait parallèlement au sens de "
                "propagation, comme le son dans l'air. Elles se propagent "
                "aussi bien dans les solides que dans les liquides. Ce sont "
                "les ondes les plus rapides : elles arrivent donc toujours "
                "en premier sur les sismogrammes, d'où leur nom, P pour "
                "primaires."
            )
        ) as tracker:
            self.play(FadeIn(ondes_p_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ondes_p_def))

        # --- Exemple traité : vitesses des ondes P selon la profondeur -------
        exemple = example_box(
            Text(
                _wrap(
                    "Les vitesses des ondes P augmentent avec la profondeur "
                    "traversée : environ 6 km/s dans la croûte continentale, "
                    "8 km/s dans le manteau supérieur, jusqu'à 13,7 km/s à "
                    "la base du manteau.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        # Schéma : trois segments de profondeur avec vitesses croissantes
        seg1 = Line(LEFT * 3.0, LEFT * 1.0, color="#74C0FC", stroke_width=8)
        seg2 = Line(LEFT * 1.0, RIGHT * 1.2, color="#4DABF7", stroke_width=8)
        seg3 = Line(RIGHT * 1.2, RIGHT * 3.0, color="#1864AB", stroke_width=8)
        segments = VGroup(seg1, seg2, seg3).arrange(RIGHT, buff=0)
        segments.next_to(exemple, DOWN, buff=0.5)
        l1 = Text("6 km/s\n(croûte)", font_size=14, color=WHITE).next_to(seg1, DOWN, buff=0.15)
        l2 = Text("8 km/s\n(manteau sup.)", font_size=14, color=WHITE).next_to(seg2, DOWN, buff=0.15)
        l3 = Text("13,7 km/s\n(base manteau)", font_size=14, color=WHITE).next_to(seg3, DOWN, buff=0.15)
        labels = VGroup(l1, l2, l3)

        with self.voiceover(
            text=(
                "Exemple traité : les vitesses des ondes P augmentent avec "
                "la profondeur traversée, environ six kilomètres par "
                "seconde dans la croûte continentale, huit kilomètres par "
                "seconde dans le manteau supérieur, et jusqu'à treize "
                "virgule sept kilomètres par seconde à la base du manteau. "
                "Cette accélération progressive, nous le verrons, traduit "
                "l'augmentation de la densité et de la rigidité des roches "
                "avec la profondeur."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.play(FadeIn(segments), FadeIn(labels))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(segments), FadeOut(labels))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Foyer = point de rupture en profondeur ; épicentre = sa projection en surface.",
                "Ondes P : longitudinales, traversent solides ET liquides, les plus rapides.",
                "Vitesse P croissante avec la profondeur : 6 → 8 → 13,7 km/s.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : le foyer est le point de rupture en "
                "profondeur, l'épicentre sa projection verticale en "
                "surface. Les ondes P sont longitudinales, traversent "
                "aussi bien les solides que les liquides, et sont les plus "
                "rapides de toutes les ondes sismiques, avec une vitesse "
                "qui croît avec la profondeur, de six à treize virgule sept "
                "kilomètres par seconde."
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
                    "Erreur fréquente : croire que toute onde sismique "
                    "s'arrête dans un liquide. C'est faux pour les ondes P, "
                    "qui traversent aussi bien les liquides que les solides "
                    "— seules les ondes S (scène suivante) sont bloquées "
                    "par un milieu liquide.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : ne croyez pas que toute onde "
                "sismique s'arrête dans un liquide. C'est faux pour les "
                "ondes P, qui traversent aussi bien les liquides que les "
                "solides. Seules les ondes S, que nous étudierons dans la "
                "scène suivante, sont bloquées par un milieu liquide."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
