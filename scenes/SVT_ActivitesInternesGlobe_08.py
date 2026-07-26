"""
scenes/SVT_ActivitesInternesGlobe_08.py — Chapitre 6 (1ereD, SVT), scène 08.

§ 6.4.2 Les plaques lithosphériques et leurs limites (définition, tableau
des 4 types de limites) + § 6.4.3 Le moteur des plaques : la convection
mantellique + piège « la plaque n'est pas un radeau ».
Source : 1ereD/SVT.pdf, pages 81-82.
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
    Arrow,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    Triangle,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _plaque(color=WHITE, width=1.4, height=0.4):
    return Rectangle(width=width, height=height, color=color, fill_color=color, fill_opacity=0.85)


class PlaquesEtConvectionMantellique(NotionScene):
    def construct(self):
        titre = scene_title("6.4.2 / 6.4.3 — Plaques et convection mantellique")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : la lithosphère découpée en plaques ---------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La lithosphère est découpée en une douzaine de grands "
                    "morceaux rigides, les plaques lithosphériques "
                    "(africaine, sud-américaine, eurasiatique, pacifique, "
                    "etc.), qui se déplacent de quelques cm/an en glissant "
                    "sur l'asthénosphère. Les activités internes se "
                    "concentrent aux limites, dont il existe trois types.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Vers mille neuf cent soixante-huit naît la théorie de la "
                "tectonique des plaques. La lithosphère est découpée en une "
                "douzaine de grands morceaux rigides, les plaques "
                "lithosphériques — africaine, sud-américaine, eurasiatique, "
                "pacifique, et bien d'autres — qui se déplacent de quelques "
                "centimètres par an en glissant sur l'asthénosphère. Les "
                "activités internes du globe se concentrent à leurs "
                "limites, dont il existe trois grands types."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : limite divergente et transformante --
        # Divergente
        p1a = _plaque(color="#288073").shift(LEFT * 0.9)
        p1b = _plaque(color="#288073").shift(RIGHT * 0.9)
        fl1a = Arrow((-0.15, 0.35, 0), (-0.9, 0.35, 0), buff=0, color=YELLOW, stroke_width=3)
        fl1b = Arrow((0.15, 0.35, 0), (0.9, 0.35, 0), buff=0, color=YELLOW, stroke_width=3)
        magma1 = Triangle(color=RED, fill_color=RED, fill_opacity=0.9).scale(0.22).rotate(0).move_to(DOWN * 0.05)
        bloc_divergente = VGroup(p1a, p1b, fl1a, fl1b, magma1)
        titre_divergente = Text("Divergente (dorsale)", font_size=17, color=YELLOW, weight="BOLD")
        titre_divergente.next_to(bloc_divergente, DOWN, buff=0.3)
        legende_divergente = Text("Écartement, volcanisme\neffusif, création de croûte", font_size=13, color=WHITE)
        legende_divergente.next_to(titre_divergente, DOWN, buff=0.15)
        groupe_divergente = VGroup(bloc_divergente, titre_divergente, legende_divergente)

        # Transformante
        p2a = _plaque(color="#A42A5A").shift(LEFT * 0.7 + UP * 0.15)
        p2b = _plaque(color="#A42A5A").shift(RIGHT * 0.7 + DOWN * 0.15)
        fl2a = Arrow((-0.3, 0.15 + 0.35, 0), (0.3, 0.15 + 0.35, 0), buff=0, color=YELLOW, stroke_width=3)
        fl2b = Arrow((0.3, -0.15 - 0.35, 0), (-0.3, -0.15 - 0.35, 0), buff=0, color=YELLOW, stroke_width=3)
        bloc_transformante = VGroup(p2a, p2b, fl2a, fl2b)
        titre_transformante = Text("Transformante (faille)", font_size=17, color=YELLOW, weight="BOLD")
        titre_transformante.next_to(bloc_transformante, DOWN, buff=0.3)
        legende_transformante = Text("Coulissage horizontal,\nséismes superficiels", font_size=13, color=WHITE)
        legende_transformante.next_to(titre_transformante, DOWN, buff=0.15)
        groupe_transformante = VGroup(bloc_transformante, titre_transformante, legende_transformante)

        premiere_paire = VGroup(groupe_divergente, groupe_transformante).arrange(RIGHT, buff=1.8)
        premiere_paire.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Première limite : divergente, ou dorsale. Deux plaques "
                "s'écartent, laissant remonter du magma qui se solidifie en "
                "nouvelle croûte : volcanisme effusif, séismes superficiels, "
                "exemple la dorsale médio-atlantique. Deuxième limite : "
                "transformante, ou faille. Deux plaques coulissent "
                "horizontalement l'une contre l'autre, sans écartement ni "
                "rapprochement : cela provoque des séismes superficiels "
                "fréquents, comme le long de la faille de San Andreas, en "
                "Californie."
            )
        ) as tracker:
            self.play(FadeIn(bloc_divergente), FadeIn(titre_divergente), FadeIn(legende_divergente))
            self.play(FadeIn(bloc_transformante), FadeIn(titre_transformante), FadeIn(legende_transformante))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(premiere_paire))

        # Convergente (subduction) et convergente (collision)
        p3a = _plaque(color="#B42E41").shift(LEFT * 0.9)
        p3b = _plaque(color="#B42E41", width=1.6).shift(RIGHT * 0.6 + DOWN * 0.3).rotate(-0.25)
        fl3a = Arrow((-0.9, 0.35, 0), (-0.2, 0.35, 0), buff=0, color=YELLOW, stroke_width=3)
        fl3b = Arrow((1.3, 0.2, 0), (0.5, -0.15, 0), buff=0, color=YELLOW, stroke_width=3)
        magma3 = Triangle(color=RED, fill_color=RED, fill_opacity=0.9).scale(0.2).move_to(RIGHT * 0.4 + UP * 0.55)
        bloc_subduction = VGroup(p3a, p3b, fl3a, fl3b, magma3)
        titre_subduction = Text("Convergente (subduction)", font_size=16, color=YELLOW, weight="BOLD")
        titre_subduction.next_to(bloc_subduction, DOWN, buff=0.3)
        legende_subduction = Text("Une plaque plonge,\nvolcanisme explosif,\nfosse océanique", font_size=13, color=WHITE)
        legende_subduction.next_to(titre_subduction, DOWN, buff=0.15)
        groupe_subduction = VGroup(bloc_subduction, titre_subduction, legende_subduction)

        p4a = _plaque(color=ORANGE).shift(LEFT * 0.75)
        p4b = _plaque(color=ORANGE).shift(RIGHT * 0.75)
        montagne = Triangle(color=WHITE, fill_color="#8B5A2B", fill_opacity=0.9).scale(0.35).move_to(UP * 0.55)
        fl4a = Arrow((-0.9, 0.35, 0), (-0.25, 0.35, 0), buff=0, color=YELLOW, stroke_width=3)
        fl4b = Arrow((0.9, 0.35, 0), (0.25, 0.35, 0), buff=0, color=YELLOW, stroke_width=3)
        bloc_collision = VGroup(p4a, p4b, montagne, fl4a, fl4b)
        titre_collision = Text("Convergente (collision)", font_size=16, color=YELLOW, weight="BOLD")
        titre_collision.next_to(bloc_collision, DOWN, buff=0.3)
        legende_collision = Text("Deux continents se\nrapprochent : chaîne de\nmontagnes, pas de volcanisme", font_size=13, color=WHITE)
        legende_collision.next_to(titre_collision, DOWN, buff=0.15)
        groupe_collision = VGroup(bloc_collision, titre_collision, legende_collision)

        deuxieme_paire = VGroup(groupe_subduction, groupe_collision).arrange(RIGHT, buff=1.6)
        deuxieme_paire.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Troisième limite : convergente par subduction. Deux "
                "plaques se rapprochent, l'une plonge sous l'autre : "
                "volcanisme explosif, séismes de toute profondeur, "
                "formation d'une fosse océanique — c'est la situation de la "
                "ceinture de feu du Pacifique. Quatrième limite : "
                "convergente par collision. Deux continents se rapprochent "
                "et se percutent, sans qu'aucun ne puisse plonger, trop "
                "légers tous les deux : cela soulève une chaîne de "
                "montagnes, avec des séismes mais sans volcanisme — c'est "
                "le cas de l'Himalaya, né de la collision entre l'Inde et "
                "l'Asie."
            )
        ) as tracker:
            self.play(FadeIn(bloc_subduction), FadeIn(titre_subduction), FadeIn(legende_subduction))
            self.play(FadeIn(bloc_collision), FadeIn(titre_collision), FadeIn(legende_collision))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(deuxieme_paire))

        # --- Exemple traité : reconnaître un type de limite -------------------
        entete_ex = Text("Exemple traité", font_size=27, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        enonce_ex = Text(
            _wrap(
                "Au Japon : séismes fréquents jusqu'à 600 km de profondeur, "
                "volcans explosifs alignés, fosse océanique toute proche. "
                "Quel type de limite ?",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce_ex.next_to(entete_ex, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple traité : au Japon, on observe des séismes "
                "fréquents jusqu'à six cents kilomètres de profondeur, des "
                "volcans explosifs alignés, et une fosse océanique toute "
                "proche. Quel type de limite de plaques reconnaît-on ?"
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        reponse_ex = Text(
            _wrap(
                "Réponse : des séismes profonds + volcanisme explosif + "
                "fosse = limite convergente de subduction. La plaque "
                "Pacifique plonge sous la plaque eurasiatique.",
                width=52,
            ),
            font_size=21,
            color=YELLOW,
        )
        reponse_ex.next_to(enonce_ex, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Réponse : des séismes qui atteignent une grande "
                "profondeur, associés à un volcanisme explosif et à une "
                "fosse océanique, signent une limite convergente de "
                "subduction. Ici, la plaque Pacifique plonge sous la "
                "plaque eurasiatique."
            )
        ) as tracker:
            self.play(FadeIn(reponse_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(enonce_ex), FadeOut(reponse_ex))

        # --- À retenir : le moteur, la convection mantellique -----------------
        entete_convection = Text("Le moteur : la convection mantellique", font_size=24, color=YELLOW, weight="BOLD")
        entete_convection.next_to(titre, DOWN, buff=0.5)

        chaud = Text("Chaud, moins dense\n→ monte", font_size=16, color=RED)
        froid = Text("Refroidi, plus dense\n→ redescend", font_size=16, color="#1E5FA8")
        fleche_montante = Arrow(DOWN * 0.6, UP * 0.6, color=RED, stroke_width=5)
        fleche_descendante = Arrow(UP * 0.6, DOWN * 0.6, color="#1E5FA8", stroke_width=5)
        montee = VGroup(fleche_montante, chaud).arrange(RIGHT, buff=0.3)
        descente = VGroup(fleche_descendante, froid).arrange(RIGHT, buff=0.3)
        convection = VGroup(montee, descente).arrange(DOWN, buff=0.6)
        convection.next_to(entete_convection, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : ce qui fait bouger les plaques, c'est la "
                "convection mantellique. La Terre possède une chaleur "
                "interne, héritée de sa formation et entretenue par la "
                "radioactivité naturelle, qui met le manteau en mouvement. "
                "Le matériau chaud, moins dense, monte ; le matériau "
                "refroidi, plus dense, redescend : ce sont des courants de "
                "convection, comme l'eau qui chauffe dans une casserole. "
                "Les courants ascendants écartent les plaques aux dorsales "
                "; les courants descendants accompagnent la plongée aux "
                "zones de subduction."
            )
        ) as tracker:
            self.play(FadeIn(entete_convection))
            self.play(FadeIn(montee))
            self.play(FadeIn(descente))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_convection), FadeOut(convection))

        # --- Piège à éviter : la plaque n'est pas un radeau -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas dire « les continents flottent sur la lave et "
                    "dérivent ». C'est la plaque lithosphérique entière "
                    "(croûte + manteau supérieur rigide soudés) qui se "
                    "déplace en glissant sur l'asthénosphère plastique. "
                    "L'Atlantique s'élargit parce que les plaques "
                    "sud-américaine et africaine s'écartent.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention, piège fréquent : ne dites jamais que les "
                "continents flottent sur la lave et dérivent tout seuls. "
                "C'est la plaque lithosphérique entière, croûte et manteau "
                "supérieur rigide soudés, qui se déplace, en glissant sur "
                "l'asthénosphère plastique. Si l'océan Atlantique "
                "s'élargit, ce n'est pas parce que les continents flottent "
                "; c'est parce que les plaques sud-américaine et africaine, "
                "tout entières, s'écartent l'une de l'autre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
