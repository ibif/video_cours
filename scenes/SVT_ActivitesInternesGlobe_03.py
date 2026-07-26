"""
scenes/SVT_ActivitesInternesGlobe_03.py — Chapitre 6 (1ereD, SVT), scène 03.

§ 6.1.3 La répartition des volcans à la surface du globe (ceinture de feu
du Pacifique, dorsales océaniques, points chauds) + application directe :
le drame du lac Nyos (Cameroun, 1986).
Source : 1ereD/SVT.pdf, page 78.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    Triangle,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _volcan_icone(color=RED, taille=0.22):
    return Triangle(color=color, fill_color=color, fill_opacity=0.9).scale(taille)


class RepartitionMondialeDesVolcans(NotionScene):
    def construct(self):
        titre = scene_title("6.1.3 — La répartition des volcans dans le monde")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : ~1500 volcans actifs, pas répartis au hasard ---------
        intro = Text(
            _wrap(
                "Environ 1 500 volcans actifs dans le monde. Ils ne sont pas "
                "répartis au hasard : ils se concentrent en bandes étroites, "
                "selon trois grandes situations géologiques.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On compte environ mille cinq cents volcans actifs dans le "
                "monde. Ils ne sont pas répartis au hasard : ils se "
                "concentrent en bandes étroites, selon trois grandes "
                "situations géologiques que nous allons découvrir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les 3 situations -------------------
        # 1. Ceinture de feu du Pacifique : anneau de volcans
        ocean = Circle(radius=0.9, color="#1E5FA8", fill_color="#1E5FA8", fill_opacity=0.5)
        anneau_volcans = VGroup(
            *[_volcan_icone().move_to(ocean.point_at_angle(a)) for a in
              [i * 0.5236 for i in range(12)]]  # 12 points autour du cercle
        )
        bloc1 = VGroup(ocean, anneau_volcans)
        label1 = Text("Ceinture de feu\ndu Pacifique", font_size=18, color=WHITE)
        label1.next_to(bloc1, DOWN, buff=0.35)
        groupe1 = VGroup(bloc1, label1)

        # 2. Dorsale océanique : ligne avec volcans effusifs
        dorsale = Line(LEFT * 1.1, RIGHT * 1.1, color=ORANGE, stroke_width=6)
        volcans_dorsale = VGroup(
            *[_volcan_icone(color=ORANGE).move_to(dorsale.point_from_proportion(p)).shift(UP * 0.15)
              for p in [0.15, 0.35, 0.5, 0.65, 0.85]]
        )
        bloc2 = VGroup(dorsale, volcans_dorsale)
        label2 = Text("Dorsales\nocéaniques", font_size=18, color=WHITE)
        label2.next_to(bloc2, DOWN, buff=0.35)
        groupe2 = VGroup(bloc2, label2)

        # 3. Point chaud : volcan isolé
        continent = Line(LEFT * 1.1, RIGHT * 1.1, color="#595959", stroke_width=6)
        point_chaud = _volcan_icone(color=RED, taille=0.3).move_to(UP * 0.15)
        marqueur = Dot(point=point_chaud.get_bottom() + DOWN * 0.05, color=YELLOW)
        bloc3 = VGroup(continent, point_chaud, marqueur)
        label3 = Text("Points chauds", font_size=18, color=WHITE)
        label3.next_to(bloc3, DOWN, buff=0.35)
        groupe3 = VGroup(bloc3, label3)

        groupes = VGroup(groupe1, groupe2, groupe3).arrange(RIGHT, buff=1.3)
        groupes.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Première situation : la ceinture de feu du Pacifique, un "
                "anneau presque continu de volcans explosifs qui entoure "
                "l'océan Pacifique — Andes, Amérique centrale, Alaska, "
                "Japon, Indonésie. Elle concentre la majorité des volcans "
                "actifs du globe."
            )
        ) as tracker:
            self.play(FadeIn(bloc1), FadeIn(label1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Deuxième situation : les dorsales océaniques, ces longues "
                "chaînes sous-marines de l'Atlantique et de l'océan Indien, "
                "siège d'un volcanisme effusif permanent mais peu visible "
                "car immergé. L'Islande est un cas particulier : une "
                "dorsale émergée, visible à l'air libre."
            )
        ) as tracker:
            self.play(FadeIn(bloc2), FadeIn(label2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Troisième situation : les points chauds, des volcans "
                "isolés au milieu des continents ou des océans, loin de "
                "toute autre activité — Hawaï, l'île de la Réunion, ou la "
                "ligne du Cameroun. Volcans et reliefs océaniques se "
                "répartissent donc en bandes étroites, jamais uniformément "
                "; nous verrons pourquoi à la fin de ce chapitre, avec la "
                "tectonique des plaques."
            )
        ) as tracker:
            self.play(FadeIn(bloc3), FadeIn(label3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupes))

        # --- Application directe : le drame du lac Nyos ---------------------
        nyos = example_box(
            Text(
                _wrap(
                    "Le 21 août 1986, le lac Nyos (Cameroun) a brusquement "
                    "dégagé un énorme nuage de CO₂ d'origine volcanique, "
                    "invisible et inodore, plus lourd que l'air : environ "
                    "1 700 personnes et des milliers de têtes de bétail "
                    "étouffés. Depuis, des tuyaux dégazent le fond du lac en "
                    "continu.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        nyos.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Application directe : le drame du lac Nyos, au Cameroun. "
                "Le vingt et un août mille neuf cent quatre-vingt-six, ce "
                "lac a brusquement dégagé un énorme nuage de dioxyde de "
                "carbone d'origine volcanique, invisible et inodore, plus "
                "lourd que l'air : il s'est répandu dans les vallées "
                "voisines et a étouffé environ mille sept cents personnes "
                "et des milliers de têtes de bétail. Depuis ce drame, des "
                "tuyaux dégazent en permanence le fond du lac pour éviter "
                "une nouvelle accumulation de gaz."
            )
        ) as tracker:
            self.play(FadeIn(nyos))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(nyos))

        # --- À retenir -------------------------------------------------------
        retenir = _bullets(
            [
                "Ceinture de feu du Pacifique : anneau de volcans explosifs, majorité des volcans actifs.",
                "Dorsales océaniques : volcanisme effusif permanent (Islande = dorsale émergée).",
                "Points chauds : volcans isolés, loin de toute limite (Hawaï, ligne du Cameroun).",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : la ceinture de feu du Pacifique concentre des "
                "volcans explosifs et la majorité des volcans actifs ; les "
                "dorsales océaniques portent un volcanisme effusif "
                "permanent, l'Islande en étant la partie émergée ; les "
                "points chauds forment des volcans isolés, loin de toute "
                "limite de plaque, comme à Hawaï ou sur la ligne du "
                "Cameroun."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Un gaz volcanique n'a pas besoin d'une éruption "
                    "spectaculaire pour tuer : au lac Nyos, aucune lave "
                    "n'est sortie — c'est un dégazage brutal et invisible "
                    "qui a fait le plus grand nombre de victimes.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : un gaz volcanique n'a pas "
                "besoin d'une éruption spectaculaire pour tuer. Au lac "
                "Nyos, aucune lave n'est sortie ; c'est un dégazage brutal "
                "et invisible de dioxyde de carbone qui a fait le plus "
                "grand nombre de victimes de toute l'histoire volcanique "
                "récente de l'Afrique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
