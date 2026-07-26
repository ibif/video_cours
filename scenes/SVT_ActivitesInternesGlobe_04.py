"""
scenes/SVT_ActivitesInternesGlobe_04.py — Chapitre 6 (1ereD, SVT), scène 04.

§ 6.2.1-6.2.2 Les séismes : définition, foyer, épicentre, profondeur
focale ; les ondes sismiques (P, S, L) et leur enregistrement ; méthode de
calcul de la distance épicentrale ; exemple d'un séisme ressenti à Accra
(210 km). Source : 1ereD/SVT.pdf, pages 78-79.
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
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LesSeismesEtLesOndesSismiques(NotionScene):
    def construct(self):
        titre = scene_title("6.2 — Les séismes et les ondes sismiques")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : de la rupture au séisme --------------------------------
        intro = Text(
            _wrap(
                "Les roches subissent des contraintes qui les déforment sans "
                "casser, puis se rompent brutalement le long d'une faille : "
                "l'énergie est libérée en quelques secondes sous forme de "
                "vibrations, c'est un séisme.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Les roches de l'écorce terrestre subissent des contraintes "
                "qui les déforment lentement, sans casser. Un jour, elles se "
                "rompent brutalement le long d'une faille : l'énergie "
                "accumulée est libérée en quelques secondes, sous forme de "
                "vibrations. C'est un séisme."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        definition = definition_box(
            Text(
                _wrap(
                    "Un séisme est un ensemble de vibrations brèves et "
                    "brusques de l'écorce terrestre, provoqué par la rupture "
                    "brutale des roches en profondeur. Le foyer (hypocentre) "
                    "est le point de rupture. L'épicentre est le point de "
                    "surface à la verticale du foyer.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un séisme est un ensemble de vibrations brèves et brusques "
                "de l'écorce terrestre, provoqué par la rupture brutale des "
                "roches en profondeur. Le foyer, ou hypocentre, est le point "
                "exact de la rupture. L'épicentre est le point de la surface "
                "situé à la verticale du foyer."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma foyer / épicentre -----------
        surface = Line(LEFT * 3.2, RIGHT * 3.2, color=WHITE, stroke_width=4)
        surface.shift(UP * 1.3)
        foyer = Dot(point=DOWN * 1.0, color=RED, radius=0.09)
        epicentre_pos = foyer.get_center()[0] * RIGHT + surface.get_center()[1] * UP
        epicentre = Dot(point=epicentre_pos, color=YELLOW, radius=0.09)
        verticale = Line(foyer.get_center(), epicentre.get_center(), color=YELLOW, stroke_width=3)

        label_surface = Text("Surface", font_size=18, color=WHITE)
        label_surface.next_to(surface, LEFT, buff=0.2).shift(UP * 0.1)
        label_foyer = Text("Foyer (hypocentre)", font_size=18, color=RED)
        label_foyer.next_to(foyer, DOWN, buff=0.3)
        label_epicentre = Text("Épicentre", font_size=18, color=YELLOW)
        label_epicentre.next_to(epicentre, UP, buff=0.3)

        ondes = VGroup(
            *[Circle(radius=r, color=ORANGE, stroke_width=2).move_to(foyer.get_center()) for r in [0.5, 0.9, 1.3]]
        )

        schema = VGroup(surface, foyer, epicentre, verticale, label_surface, label_foyer, label_epicentre)
        schema.next_to(titre, DOWN, buff=0.5).shift(LEFT * 0.2)
        ondes.move_to(foyer.get_center())

        with self.voiceover(
            text=(
                "Sur ce schéma, la surface du sol est en haut. Le foyer, en "
                "profondeur, est le point où les roches se rompent. "
                "L'épicentre est le point de la surface situé juste à la "
                "verticale du foyer : c'est là que les secousses sont "
                "généralement les plus fortes. On distingue des séismes "
                "superficiels, à moins de soixante kilomètres de "
                "profondeur, des séismes intermédiaires, entre soixante et "
                "trois cents kilomètres, et des séismes profonds, entre "
                "trois cents et sept cents kilomètres : c'est la profondeur "
                "focale."
            )
        ) as tracker:
            self.play(FadeIn(surface), FadeIn(label_surface))
            self.play(FadeIn(foyer), FadeIn(label_foyer))
            self.play(FadeIn(verticale), FadeIn(epicentre), FadeIn(label_epicentre))
            self.play(FadeIn(ondes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(ondes))

        # --- Les trois types d'ondes sismiques -------------------------------
        ondes_def = definition_box(
            Text(
                _wrap(
                    "Ondes P (primaires) : compression-dilatation, les plus "
                    "rapides (~6 km/s dans la croûte), traversent solides et "
                    "liquides. Ondes S (secondaires) : cisaillement, ~1,7 "
                    "fois plus lentes que P, uniquement dans les solides. "
                    "Ondes L (surface) : les plus lentes, les plus "
                    "destructrices.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        ondes_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'énergie libérée au foyer se propage sous forme d'ondes "
                "sismiques, comme des rides circulaires. Les ondes P, ou "
                "primaires, sont des ondes de compression-dilatation : ce "
                "sont les plus rapides, environ six kilomètres par seconde "
                "dans la croûte, et elles traversent aussi bien les solides "
                "que les liquides. Les ondes S, ou secondaires, sont des "
                "ondes de cisaillement, environ une fois et sept dixièmes "
                "plus lentes que les ondes P, et elles ne se propagent que "
                "dans les solides. Les ondes L, ou de surface, sont les "
                "plus lentes, mais aussi les plus destructrices."
            )
        ) as tracker:
            self.play(FadeIn(ondes_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ondes_def))

        sismogramme = Text(
            _wrap(
                "Les sismographes enregistrent un sismogramme : les ondes "
                "arrivent successivement, d'abord les P, puis les S, puis "
                "les L.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        sismogramme.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Les sismographes enregistrent un sismogramme sur lequel "
                "les ondes arrivent dans un ordre toujours identique : "
                "d'abord les ondes P, les plus rapides, puis les ondes S, "
                "puis enfin les ondes L, les plus lentes."
            )
        ) as tracker:
            self.play(FadeIn(sismogramme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sismogramme))

        # --- Méthode : calculer la distance à l'épicentre --------------------
        methode = method_box(
            Text(
                _wrap(
                    "Étape 1 : mesurer le décalage Δt entre l'arrivée des "
                    "ondes P et S sur le sismogramme. Étape 2 : noter vP et "
                    "vS. Étape 3 : écrire tP=d/vP et tS=d/vS. Étape 4 : comme "
                    "Δt=tS-tP, on tire d = (vP×vS)/(vP-vS) × Δt. Étape 5 : "
                    "vérifier en recalculant tP et tS séparément.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        formule = MathTex(
            r"d = \dfrac{v_P \times v_S}{v_P - v_S} \times \Delta t",
            font_size=34,
            color=YELLOW,
        )
        formule.next_to(methode, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour calculer la distance d'une station à l'épicentre, "
                "cinq étapes. Étape un : mesurer, sur le sismogramme, le "
                "décalage delta t entre l'arrivée des ondes P et des ondes "
                "S. Étape deux : noter les vitesses vP et vS. Étape trois : "
                "écrire que le temps de trajet des ondes P vaut d sur vP, et "
                "celui des ondes S vaut d sur vS. Étape quatre : comme delta "
                "t est égal à tS moins tP, on en tire la distance d, égale à "
                "vP fois vS, divisé par vP moins vS, le tout multiplié par "
                "delta t. Étape cinq : on vérifie en recalculant tP et tS "
                "séparément."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.play(Write(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode), FadeOut(formule))

        # --- Exemple traité : distance d'un séisme ressenti à Accra ---------
        exemple = example_box(
            Text(
                _wrap(
                    "Une station d'Accra enregistre : ondes P à 6 km/s, "
                    "ondes S à 3,5 km/s, S arrive 25 s après P. Calculer la "
                    "distance d à l'épicentre.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : une station d'Accra enregistre des ondes "
                "P à six kilomètres par seconde, des ondes S à trois "
                "virgule cinq kilomètres par seconde, et les ondes S "
                "arrivent vingt-cinq secondes après les ondes P. Calculons "
                "la distance d à l'épicentre."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        calcul = MathTex(
            r"d = \dfrac{6 \times 3{,}5}{6 - 3{,}5} \times 25 = \dfrac{21}{2{,}5} \times 25 = 210 \text{ km}",
            font_size=28,
            color=WHITE,
        )
        calcul.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On applique la formule : d égale six fois trois virgule "
                "cinq, divisé par six moins trois virgule cinq, le tout "
                "fois vingt-cinq. Cela donne vingt et un divisé par deux "
                "virgule cinq, fois vingt-cinq, soit deux cent dix "
                "kilomètres. Vérification : tP égale deux cent dix divisé "
                "par six, soit trente-cinq secondes ; tS égale deux cent dix "
                "divisé par trois virgule cinq, soit soixante secondes ; "
                "soixante moins trente-cinq égale bien vingt-cinq secondes. "
                "Le résultat est confirmé. Pour localiser précisément "
                "l'épicentre, il faut trois stations : l'épicentre se "
                "trouve à l'intersection de trois cercles."
            )
        ) as tracker:
            self.play(Write(calcul))
            self.wait(tracker.get_remaining_duration())

        verification = Text(
            "Vérification : tP=35s, tS=60s, 60-35=25s ✓",
            font_size=20,
            color=YELLOW,
        )
        verification.next_to(calcul, DOWN, buff=0.3)
        self.play(FadeIn(verification))

        # Garde-fou : si le bloc exemple + calcul + vérification déborde du
        # cadre visible, on réduit son échelle en gardant l'ancrage en haut.
        bloc_exemple = VGroup(exemple, calcul, verification)
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = bloc_exemple.get_top()[1] - _bas_visible
        if bloc_exemple.height > _hauteur_dispo:
            bloc_exemple.scale(_hauteur_dispo / bloc_exemple.height, about_point=bloc_exemple.get_top())

        self.wait(1.5)
        self.play(FadeOut(exemple), FadeOut(calcul), FadeOut(verification))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Foyer = point de rupture en profondeur ; épicentre = sa projection en surface.",
                "Ordre d'arrivée toujours identique : ondes P, puis ondes S, puis ondes L.",
                "Formule clé : d = (vP×vS)/(vP-vS) × Δt, avec Δt le décalage P-S mesuré.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : le foyer est le point de rupture en "
                "profondeur, l'épicentre sa projection à la verticale, en "
                "surface. L'ordre d'arrivée des ondes est toujours "
                "identique : d'abord les ondes P, puis les ondes S, puis "
                "les ondes L. Et la formule clé à mémoriser : d égale vP "
                "fois vS, divisé par vP moins vS, le tout multiplié par "
                "delta t, le décalage entre l'arrivée des ondes P et des "
                "ondes S mesuré sur le sismogramme."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Une seule station ne permet jamais de localiser "
                    "l'épicentre : elle ne donne qu'une distance, donc un "
                    "cercle de positions possibles. Il faut au moins trois "
                    "stations pour obtenir un point unique, à l'intersection "
                    "des trois cercles.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention, piège fréquent : une seule station ne permet "
                "jamais de localiser l'épicentre. Elle ne donne qu'une "
                "distance, donc tout un cercle de positions possibles "
                "autour d'elle. Il faut au moins trois stations pour "
                "obtenir un point unique, à l'intersection des trois "
                "cercles."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
