"""
scenes/SVT_ActivitesInternesGlobe_06.py — Chapitre 6 (1ereD, SVT), scène 06.

§ 6.3.1-6.3.2 Structure interne du globe : les trois enveloppes
concentriques (croûte, manteau, noyau), tableau récapitulatif, les
discontinuités (Moho, Gutenberg, Lehmann), la zone d'ombre des ondes S et
la preuve que le noyau externe est liquide.
Source : 1ereD/SVT.pdf, pages 79-80.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Annulus,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

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


class StructureInterneDuGlobe(NotionScene):
    def construct(self):
        titre = scene_title("6.3 — La structure interne du globe terrestre")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : le forage de Kola, dérisoire face au rayon terrestre --
        intro = Text(
            _wrap(
                "Le forage le plus profond (Kola, Russie) atteint ~12 km, "
                "500 fois moins que le rayon terrestre. On utilise donc les "
                "ondes sismiques pour connaître l'intérieur : la Terre a "
                "trois enveloppes concentriques séparées par des "
                "discontinuités.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le forage le plus profond jamais réalisé, à Kola en "
                "Russie, atteint environ douze kilomètres : cinq cents fois "
                "moins que le rayon terrestre. Impossible donc de creuser "
                "jusqu'au centre de la Terre. On utilise alors les ondes "
                "sismiques, qui traversent tout le globe, pour connaître ce "
                "qu'il cache : la Terre est faite de trois enveloppes "
                "concentriques, séparées par des discontinuités."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : schéma en cercles concentriques ----
        noyau_interne = Circle(radius=0.55, color=YELLOW, fill_color="#F2C230", fill_opacity=1.0, stroke_width=0)
        noyau_externe = Annulus(inner_radius=0.55, outer_radius=1.05, color=ORANGE, fill_color=ORANGE, fill_opacity=1.0)
        manteau = Annulus(inner_radius=1.05, outer_radius=2.15, color="#8B5A2B", fill_color="#8B5A2B", fill_opacity=1.0)
        croute = Annulus(inner_radius=2.15, outer_radius=2.3, color="#288073", fill_color="#288073", fill_opacity=1.0)
        globe = VGroup(manteau, noyau_externe, noyau_interne, croute)
        globe.move_to(LEFT * 3.1 + DOWN * 0.1)

        label_croute = Text("Croûte", font_size=17, color=WHITE)
        label_croute.next_to(globe, RIGHT, buff=1.6).shift(UP * 1.9)
        label_manteau = Text("Manteau\n(solide, déformable)", font_size=16, color=WHITE)
        label_manteau.next_to(globe, RIGHT, buff=1.6).shift(UP * 0.75)
        label_noyau_ext = Text("Noyau externe\n(liquide)", font_size=16, color=WHITE)
        label_noyau_ext.next_to(globe, RIGHT, buff=1.6).shift(DOWN * 0.5)
        label_noyau_int = Text("Noyau interne\n(solide, graine)", font_size=16, color=WHITE)
        label_noyau_int.next_to(globe, RIGHT, buff=1.6).shift(DOWN * 1.75)

        labels = VGroup(label_croute, label_manteau, label_noyau_ext, label_noyau_int)

        with self.voiceover(
            text=(
                "Au centre, le noyau interne, ou graine, de cinq mille cent "
                "kilomètres au centre, six mille trois cent soixante et onze "
                "kilomètres : fer et nickel à l'état solide, malgré une "
                "température extrême. Autour, le noyau externe, de deux "
                "mille neuf cents à cinq mille cent kilomètres : même "
                "composition, fer et nickel, mais à l'état liquide. "
                "Au-dessus, le manteau, de la base de la croûte jusqu'à deux "
                "mille neuf cents kilomètres : des roches denses, les "
                "péridotites, solides mais capables de se déformer très "
                "lentement. Enfin, la croûte, l'enveloppe la plus "
                "superficielle et la plus fine, rigide."
            )
        ) as tracker:
            self.play(FadeIn(noyau_interne))
            self.play(FadeIn(label_noyau_int))
            self.play(FadeIn(noyau_externe))
            self.play(FadeIn(label_noyau_ext))
            self.play(FadeIn(manteau))
            self.play(FadeIn(label_manteau))
            self.play(FadeIn(croute))
            self.play(FadeIn(label_croute))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(globe), FadeOut(labels))

        definition = definition_box(
            Text(
                _wrap(
                    "La croûte : 5-10 km sous les océans (basaltique), "
                    "30-70 km sous les continents (granitique). Le manteau "
                    ": jusqu'à 2900 km, péridotites solides déformables. Le "
                    "noyau : de 2900 km au centre, fer et nickel — noyau "
                    "externe liquide (2900-5100 km), noyau interne solide "
                    "(5100-6371 km).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Résumons. La croûte : cinq à dix kilomètres d'épaisseur "
                "sous les océans, de nature basaltique ; trente à soixante-"
                "dix kilomètres sous les continents, de nature granitique. "
                "Le manteau : jusqu'à deux mille neuf cents kilomètres, "
                "constitué de péridotites, solides mais déformables. Le "
                "noyau : de deux mille neuf cents kilomètres jusqu'au "
                "centre, fer et nickel, avec un noyau externe liquide entre "
                "deux mille neuf cents et cinq mille cent kilomètres, et un "
                "noyau interne solide de cinq mille cent à six mille trois "
                "cent soixante et onze kilomètres."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Les discontinuités -----------------------------------------------
        entete_disc = Text("Les discontinuités", font_size=27, color=YELLOW, weight="BOLD")
        entete_disc.next_to(titre, DOWN, buff=0.5)

        discontinuites = _bullets(
            [
                "Moho (Mohorovicic) : sépare croûte et manteau (5-70 km).",
                "Gutenberg : sépare manteau et noyau (2900 km).",
                "Lehmann : sépare noyau externe et noyau interne (5100 km).",
            ],
            width=50,
        )
        discontinuites.next_to(entete_disc, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quand une onde passe d'une enveloppe à une autre, sa "
                "vitesse change brutalement et sa direction se dévie : "
                "c'est une discontinuité. La discontinuité de Mohorovicic, "
                "ou Moho, sépare la croûte du manteau, entre cinq et "
                "soixante-dix kilomètres de profondeur. La discontinuité de "
                "Gutenberg, à deux mille neuf cents kilomètres, sépare le "
                "manteau du noyau. La discontinuité de Lehmann, à cinq "
                "mille cent kilomètres, sépare le noyau externe du noyau "
                "interne."
            )
        ) as tracker:
            self.play(FadeIn(entete_disc))
            self.play(FadeIn(discontinuites))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_disc), FadeOut(discontinuites))

        # --- Exemple traité : la zone d'ombre prouve un noyau liquide --------
        exemple = example_box(
            Text(
                _wrap(
                    "Une station à 80° reçoit ondes P et S ; une station à "
                    "120° ne reçoit aucune onde S. Pourquoi le noyau externe "
                    "est-il liquide ?",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : après un grand séisme, une station située "
                "à quatre-vingts degrés de distance angulaire reçoit à la "
                "fois les ondes P et les ondes S. Une station située à cent "
                "vingt degrés ne reçoit aucune onde S : c'est ce qu'on "
                "appelle la zone d'ombre. Pourquoi peut-on en déduire que "
                "le noyau externe est liquide ?"
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        resolution = Text(
            _wrap(
                "Résolution : les ondes S ne se propagent que dans les "
                "solides. Si elles n'arrivent jamais à 120°, c'est qu'elles "
                "ont rencontré un milieu liquide qui les a absorbées. "
                "Au-delà de 105°, plus aucune onde S n'arrive ; entre 105° "
                "et 142°, les ondes P directes disparaissent aussi.",
                width=52,
            ),
            font_size=21,
            color=YELLOW,
        )
        resolution.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résolution : les ondes S ne se propagent que dans les "
                "solides. Si elles n'arrivent jamais à cent vingt degrés, "
                "c'est qu'elles ont rencontré, en profondeur, un milieu "
                "liquide qui les a totalement absorbées. Au-delà de cent "
                "cinq degrés de distance angulaire, plus aucune onde S "
                "n'arrive ; entre cent cinq et cent quarante-deux degrés, "
                "même les ondes P directes disparaissent, déviées par ce "
                "même milieu. Conclusion : à partir de deux mille neuf "
                "cents kilomètres de profondeur, la Terre contient une "
                "couche liquide, le noyau externe."
            )
        ) as tracker:
            self.play(FadeIn(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(resolution))

        # --- À retenir : la sismologie, échographie de la planète -----------
        echographie = Text(
            _wrap(
                "À retenir : cette méthode est comme une échographie "
                "médicale — la sismologie est « l'échographie » de la "
                "planète, elle révèle une structure invisible sans jamais "
                "y accéder directement.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        echographie.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : cette méthode s'apparente à une échographie "
                "médicale. La sismologie est en quelque sorte "
                "l'échographie de la planète : elle révèle une structure "
                "invisible, sans jamais y accéder directement."
            )
        ) as tracker:
            self.play(FadeIn(echographie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(echographie))

        # --- Piège à éviter : deux idées fausses ------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "L'intérieur de la Terre n'est pas une boule de feu "
                    "liquide : seul le noyau externe est liquide ; le "
                    "manteau (>80% du volume) est solide. La croûte "
                    "continentale n'est pas partout identique : plus "
                    "épaisse sous les montagnes (jusqu'à 70 km) que sous "
                    "les plaines (~30 km).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention, deux idées fausses à éliminer. Premièrement, "
                "l'intérieur de la Terre n'est pas une boule de feu "
                "liquide : seul le noyau externe est liquide, alors que le "
                "manteau, qui représente plus de quatre-vingts pour cent du "
                "volume du globe, est bien solide. Deuxièmement, la croûte "
                "continentale n'est pas partout identique : elle est plus "
                "épaisse sous les montagnes, jusqu'à soixante-dix "
                "kilomètres, que sous les plaines, environ trente "
                "kilomètres seulement."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
