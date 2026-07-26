"""
scenes/SVT_EchangesCationiquesSol_06.py — Chapitre 9 (1ereC, SVT), scène 06.

Les cations retenus par le complexe (nature et rôle de Ca2+, Mg2+, K+,
Na+, H+, Al3+), définition des bases échangeables vs cations acidifiants,
définition de la CEC (formule, unité cmol+/kg), tableau d'appréciation des
valeurs, et remarque sur l'humus. Source : 1ereC/SVT.pdf, pages 100-101.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class CationsRetenusEtCEC(NotionScene):
    def construct(self):
        titre = scene_title("9.5 — Les cations retenus et la CEC")
        titre.scale(0.66)
        titre.to_edge(UP)

        # --- Énoncé : quels cations, et quel réservoir ? --------------------
        intro = Text(
            _wrap(
                "Tous les cations ne jouent pas le même rôle pour la "
                "plante. Et tous les sols n'ont pas la même capacité à "
                "les retenir : comment mesurer cette capacité ?",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Tous les cations retenus par le complexe ne jouent pas "
                "le même rôle pour la plante. Et tous les sols n'ont pas "
                "la même capacité à les retenir. Comment mesurer cette "
                "capacité ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : nature et rôle des cations retenus --------------
        tab_titre = Text("Les cations retenus par le complexe", font_size=24, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.4)

        roles = property_box(
            _bullets(
                [
                    "Ca2+ (calcium) : base échangeable, améliore la "
                    "structure du sol",
                    "Mg2+ (magnésium) : base échangeable, entre dans la "
                    "chlorophylle",
                    "K+ (potassium) : base échangeable, élément nutritif "
                    "majeur",
                    "Na+ (sodium) : base échangeable, nuisible en excès",
                    "H+ (hydrogène) : cation acidifiant, abaisse le pH",
                    "Al3+ (aluminium) : cation acidifiant, toxique pour "
                    "les plantes en excès",
                ],
                font_size=17,
                width=58,
            ),
            box_width=12.4,
        )
        roles.next_to(tab_titre, DOWN, buff=0.3)

        groupe_roles = VGroup(tab_titre, roles)
        _fit(groupe_roles, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Voici les principaux cations retenus par le complexe "
                "argilo-humique. Le calcium améliore la structure du sol. "
                "Le magnésium entre dans la composition de la "
                "chlorophylle. Le potassium est un élément nutritif "
                "majeur. Le sodium, lui, devient nuisible en excès. Ces "
                "quatre cations sont appelés des bases échangeables. En "
                "revanche, l'ion hydrogène abaisse le pH du sol, et "
                "l'aluminium devient toxique pour les plantes en excès : "
                "ce sont des cations acidifiants, et non des bases."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(roles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(roles))

        def_bases = definition_box(
            Text(
                _wrap(
                    "On appelle bases échangeables les cations "
                    "métalliques fixés sur le complexe : Ca2+, Mg2+, K+ "
                    "et Na+. Les ions H+ et Al3+ ne sont pas des bases : "
                    "ce sont des cations acidifiants.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_bases.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons cette définition importante : on appelle bases "
                "échangeables les cations métalliques fixés sur le "
                "complexe, calcium, magnésium, potassium et sodium. Les "
                "ions hydrogène et aluminium ne sont pas des bases : ce "
                "sont des cations acidifiants. Cette distinction sera "
                "essentielle pour calculer le taux de saturation d'un "
                "sol."
            )
        ) as tracker:
            self.play(FadeIn(def_bases))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_bases))

        # --- Définition de la CEC + formule ----------------------------------
        def_cec = definition_box(
            Text(
                _wrap(
                    "La capacité d'échange cationique (CEC) est la "
                    "quantité totale de cations (bases échangeables + "
                    "cations acidifiants) qu'un sol est capable de "
                    "retenir sur son complexe argilo-humique. Elle "
                    "s'exprime en cmol+/kg de sol.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_cec.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "On appelle capacité d'échange cationique, ou CEC, la "
                "quantité totale de cations, bases échangeables plus "
                "cations acidifiants, qu'un sol est capable de retenir "
                "sur son complexe argilo-humique. Elle s'exprime en "
                "centimoles de charge positive par kilogramme de sol, "
                "noté cmol plus par kilogramme."
            )
        ) as tracker:
            self.play(FadeIn(def_cec))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_cec))

        formule = MathTex(
            r"CEC = Ca^{2+} + Mg^{2+} + K^+ + Na^+ + H^+",
            font_size=32,
            color=YELLOW,
        )
        formule_unite = Text("(chaque terme exprimé en cmol+/kg)", font_size=18, color=WHITE)
        bloc_formule = VGroup(formule, formule_unite).arrange(DOWN, buff=0.3)
        bloc_formule.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "La CEC représente la taille du réservoir d'éléments "
                "nutritifs du sol. Elle se calcule en additionnant les "
                "quantités de tous les cations échangeables : CEC égale "
                "calcium deux plus, plus magnésium deux plus, plus "
                "potassium plus, plus sodium plus, plus hydrogène plus, "
                "chaque terme étant exprimé en cmol plus par kilogramme."
            )
        ) as tracker:
            self.play(Write(formule))
            self.play(FadeIn(formule_unite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_formule))

        # --- Tableau d'appréciation de la CEC --------------------------------
        appreciation_titre = Text("Appréciation de la valeur de la CEC", font_size=23, color=YELLOW, weight="BOLD")
        appreciation_titre.next_to(titre, DOWN, buff=0.5)

        col1 = VGroup(
            Text("CEC < 10 cmol+/kg", font_size=20, color=WHITE),
            Text("10 ≤ CEC ≤ 25 cmol+/kg", font_size=20, color=WHITE),
            Text("CEC > 25 cmol+/kg", font_size=20, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        col2 = VGroup(
            Text("Faible (sol sableux)", font_size=20, color=RED),
            Text("Moyenne (réserve correcte)", font_size=20, color=YELLOW),
            Text("Élevée (riche en argile/humus)", font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        tableau = VGroup(col1, col2).arrange(RIGHT, buff=0.7, aligned_edge=UP)
        tableau.next_to(appreciation_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Comment apprécier la valeur d'une CEC ? En dessous de "
                "dix cmol plus par kilogramme, elle est faible : le sol "
                "est pauvre en argile et en humus, souvent sableux, avec "
                "une faible réserve nutritive. Entre dix et vingt-cinq, "
                "elle est moyenne : la réserve est correcte, pour un bon "
                "fonctionnement cultural. Au-dessus de vingt-cinq, elle "
                "est élevée : le sol est riche en argile et/ou en humus, "
                "avec une grande réserve nutritive."
            )
        ) as tracker:
            self.play(FadeIn(appreciation_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(appreciation_titre), FadeOut(tableau))

        # --- Remarque : l'humus a une CEC plus élevée que les argiles -------
        remarque = warning_box(
            Text(
                _wrap(
                    "L'humus a une CEC beaucoup plus élevée que les "
                    "argiles. Un sol riche en humus retient donc mieux "
                    "les éléments nutritifs.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.5,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une remarque à retenir : l'humus a une CEC beaucoup plus "
                "élevée que les argiles. Un sol riche en humus retient "
                "donc mieux les éléments nutritifs qu'un sol riche "
                "seulement en argile. C'est pourquoi l'entretien de la "
                "matière organique est un levier essentiel de la "
                "fertilité."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(remarque))
