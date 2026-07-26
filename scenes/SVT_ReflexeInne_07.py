"""
scenes/SVT_ReflexeInne_07.py — Chapitre 10 (1ereD, SVT), scène 07.

§ 10.3.3-10.3.4 : structure de la moelle épinière (substance grise en H,
substance blanche, canal épendymaire, racines dorsale/ventrale, nerf
rachidien mixte), piège sur les racines, puis neurones et synapses.
Source : 1ereD/SVT.pdf, pages 137-139.
"""

import textwrap

from manim import (
    DOWN,
    GRAY_B,
    GRAY_E,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Polygon,
    Text,
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
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


def _coupe_moelle():
    """Schéma simplifié d'une coupe transversale de moelle épinière."""
    subst_blanche = Circle(radius=1.5, fill_color=GRAY_B, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2)

    # Substance grise en forme de H / papillon, approximée par un polygone.
    subst_grise = Polygon(
        [-0.35, 1.0, 0], [0.35, 1.0, 0], [0.35, 0.25, 0], [0.9, 0.55, 0],
        [0.9, -0.1, 0], [0.2, -0.15, 0], [0.35, -1.0, 0], [-0.35, -1.0, 0],
        [-0.2, -0.15, 0], [-0.9, -0.1, 0], [-0.9, 0.55, 0], [-0.35, 0.25, 0],
        fill_color=GRAY_E, fill_opacity=1.0, stroke_color=WHITE, stroke_width=1.5,
    )

    canal = Dot(point=[0, 0, 0], radius=0.06, color=WHITE)

    label_blanche = Text("substance blanche", font_size=13, color=WHITE)
    label_blanche.next_to(subst_blanche, UP, buff=0.15)
    label_grise = Text("substance grise\n(H / papillon)", font_size=12, color=YELLOW)
    label_grise.next_to(subst_blanche, DOWN, buff=0.2)

    # Racine dorsale (sensitive) : à gauche, avec ganglion spinal.
    racine_dorsale = Line([-1.5, 0.55, 0], [-2.7, 0.55, 0], color=ORANGE, stroke_width=3)
    ganglion = Circle(radius=0.13, fill_color=ORANGE, fill_opacity=1.0, stroke_color=WHITE).move_to([-2.2, 0.55, 0])
    label_dorsale = Text("racine dorsale\n(sensitive)", font_size=12, color=ORANGE)
    label_dorsale.next_to(racine_dorsale, LEFT, buff=0.1).shift(UP * 0.35)
    label_ganglion = Text("ganglion spinal", font_size=10, color=ORANGE)
    label_ganglion.next_to(ganglion, DOWN, buff=0.08)

    # Racine ventrale (motrice) : à gauche, en dessous.
    racine_ventrale = Line([-1.5, -0.55, 0], [-2.7, -0.55, 0], color="#1E90FF", stroke_width=3)
    label_ventrale = Text("racine ventrale\n(motrice)", font_size=12, color="#1E90FF")
    label_ventrale.next_to(racine_ventrale, LEFT, buff=0.1).shift(DOWN * 0.35)

    # Nerf rachidien mixte : réunion des deux racines.
    nerf = Line([-2.7, 0.55, 0], [-3.3, 0, 0], color=WHITE, stroke_width=3)
    nerf2 = Line([-2.7, -0.55, 0], [-3.3, 0, 0], color=WHITE, stroke_width=3)
    label_nerf = Text("nerf rachidien\n(mixte)", font_size=12, color=WHITE, weight="BOLD")
    label_nerf.next_to(VGroup(nerf, nerf2), LEFT, buff=0.15)

    schema = VGroup(
        subst_blanche, subst_grise, canal, label_blanche, label_grise,
        racine_dorsale, ganglion, label_dorsale, label_ganglion,
        racine_ventrale, label_ventrale,
        nerf, nerf2, label_nerf,
    )
    return schema


class StructureDeLaMoelleEpiniere(NotionScene):
    def construct(self):
        titre = scene_title("10.3.3 — Structure de la moelle épinière")
        titre.scale(0.56)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        intro = Text(
            _wrap(
                "La moelle épinière est un cordon nerveux cylindrique, "
                "long d'environ 42 à 45 cm chez l'adulte, logé et protégé "
                "dans le canal vertébral de la colonne vertébrale, le "
                "rachis. Sur une coupe transversale, on distingue deux "
                "régions.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La moelle épinière est un cordon nerveux cylindrique, "
                "long d'environ quarante-deux à quarante-cinq centimètres "
                "chez l'adulte, logé et protégé dans le canal vertébral de "
                "la colonne vertébrale, le rachis. Sur une coupe "
                "transversale, on distingue deux régions."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : construction du schéma -----------------
        schema = _coupe_moelle()
        schema.scale(1.05)
        schema.move_to([0.8, -0.3, 0])
        schema.next_to(titre, DOWN, buff=0.5)

        (
            subst_blanche, subst_grise, canal, label_blanche, label_grise,
            racine_dorsale, ganglion, label_dorsale, label_ganglion,
            racine_ventrale, label_ventrale,
            nerf, nerf2, label_nerf,
        ) = schema

        with self.voiceover(
            text=(
                "À la périphérie, la substance blanche, formée de "
                "faisceaux de fibres nerveuses qui montent vers le "
                "cerveau, les voies ascendantes, ou qui en descendent, les "
                "voies descendantes."
            )
        ) as tracker:
            self.play(FadeIn(subst_blanche), FadeIn(label_blanche))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Au centre, la substance grise, en forme de papillon, ou "
                "de H, qui contient les corps cellulaires des neurones ; "
                "elle présente des cornes dorsales, vers le dos, par où "
                "arrivent les fibres sensitives, et des cornes ventrales, "
                "vers le ventre, où se trouvent les corps cellulaires des "
                "motoneurones. Au milieu, le canal épendymaire, qui "
                "contient du liquide céphalo-rachidien."
            )
        ) as tracker:
            self.play(FadeIn(subst_grise), FadeIn(label_grise), FadeIn(canal))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "À chaque niveau de la moelle partent, de chaque côté, "
                "deux racines rachidiennes. La racine dorsale, sensitive, "
                "conduit l'influx des récepteurs vers la corne dorsale ; "
                "elle porte un renflement, le ganglion spinal, qui contient "
                "les corps cellulaires des neurones sensitifs."
            )
        ) as tracker:
            self.play(FadeIn(racine_dorsale), FadeIn(ganglion), FadeIn(label_dorsale), FadeIn(label_ganglion))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "La racine ventrale, motrice, conduit l'influx moteur des "
                "motoneurones, dont les corps cellulaires sont dans la "
                "corne ventrale, vers l'extérieur."
            )
        ) as tracker:
            self.play(FadeIn(racine_ventrale), FadeIn(label_ventrale))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Les deux racines se réunissent pour former le nerf "
                "rachidien, dit nerf mixte, car il contient à la fois des "
                "fibres sensitives et des fibres motrices."
            )
        ) as tracker:
            self.play(FadeIn(nerf), FadeIn(nerf2), FadeIn(label_nerf))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Piège à éviter : ne pas inverser les racines ------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La racine dorsale est sensitive (l'information entre "
                    "dans la moelle) et la racine ventrale est motrice "
                    "(l'ordre sort de la moelle). Moyen mnémotechnique : "
                    "« dorsale = dedans », « ventrale = va vers le "
                    "muscle ». Le nerf rachidien, formé des deux racines "
                    "réunies, n'est ni sensitif ni moteur : il est mixte.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas inverser les racines. La racine "
                "dorsale est sensitive, l'information entre dans la "
                "moelle ; et la racine ventrale est motrice, l'ordre sort "
                "de la moelle. Moyen mnémotechnique : dorsale, dedans ; "
                "ventrale, va vers le muscle. Erreur classique à éviter : "
                "le nerf rachidien, formé des deux racines réunies, n'est "
                "ni sensitif ni moteur, il est mixte."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- Exemple traité : le neurone et ses prolongements --------------------
        entete_neurone = Text("10.3.4 — Neurones et synapses", font_size=26, color=YELLOW, weight="BOLD")
        entete_neurone.next_to(titre, DOWN, buff=0.5)

        neurone_texte = _bullets(
            [
                "Le neurone comprend un corps cellulaire (avec le noyau) et des prolongements.",
                "Les dendrites, courtes et ramifiées, reçoivent l'influx.",
                "L'axone, prolongement unique et long, conduit l'influx vers une autre cellule (une fibre nerveuse = un axone ; un nerf = un faisceau de fibres).",
                "Trois catégories : neurone sensitif (afférent), motoneurone (efférent), interneurone (liaison dans le centre).",
            ],
            font_size=19,
            width=58,
        )
        neurone_texte.next_to(entete_neurone, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le neurone est la cellule nerveuse. Il comprend un corps "
                "cellulaire, avec le noyau, et des prolongements : les "
                "dendrites, courtes et ramifiées, qui reçoivent l'influx, "
                "et l'axone, prolongement unique et long, qui conduit "
                "l'influx vers une autre cellule. Une fibre nerveuse est un "
                "axone ; un nerf est un faisceau de nombreuses fibres "
                "nerveuses réunies dans une gaine. On distingue trois "
                "catégories de neurones dans l'arc réflexe : le neurone "
                "sensitif, ou afférent, qui porte l'influx du récepteur "
                "vers le centre ; le motoneurone, ou efférent, qui porte "
                "l'ordre du centre vers le muscle ; et l'interneurone, "
                "neurone de liaison intercalé dans le centre nerveux entre "
                "les deux précédents."
            )
        ) as tracker:
            self.play(FadeIn(entete_neurone))
            self.play(FadeIn(neurone_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_neurone), FadeOut(neurone_texte))

        # --- À retenir : définition de la synapse ---------------------------------
        def_synapse = definition_box(
            Text(
                _wrap(
                    "Une synapse est la zone de contact entre deux neurones "
                    "(ou entre un neurone et une fibre musculaire) par "
                    "laquelle l'influx nerveux est transmis. La "
                    "transmission ne s'y fait que dans un seul sens et "
                    "s'accompagne d'un très bref retard, de l'ordre de "
                    "1 ms par synapse.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        def_synapse.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : une synapse est la zone de contact entre deux "
                "neurones, ou entre un neurone et une fibre musculaire, par "
                "laquelle l'influx nerveux est transmis. La transmission ne "
                "s'y fait que dans un seul sens et s'accompagne d'un très "
                "bref retard, de l'ordre d'une milliseconde par synapse. "
                "Rappel : afférent signifie qui apporte au centre, la voie "
                "sensitive est afférente ; efférent signifie qui emporte "
                "depuis le centre, la voie motrice est efférente."
            )
        ) as tracker:
            self.play(FadeIn(def_synapse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(def_synapse))
