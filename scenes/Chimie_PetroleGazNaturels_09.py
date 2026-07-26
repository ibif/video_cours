"""
scenes/Chimie_PetroleGazNaturels_09.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 09.

§ 9. Méthodes, pièges à éviter et essentiel : 4 method_box (reconnaître
l'opération décrite via mots-clés, équilibrer une équation de craquage
ou de combustion dans l'ordre C→H→O, apprendre le tableau des fractions
dans l'ordre croissant de température d'ébullition, structurer une
réponse APC en 3 temps), 3 warning_box (distillation ≠ réaction
chimique ; indice d'octane ≠ pourcentage d'octane ; gaz naturel ≠
butane), puis essentiel_box récapitulatif final du chapitre.
Source : synthèse du chapitre 5, 1ereC/Chimie.pdf, pages 45-53.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class MethodesPiegesEtEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("9. Méthodes, pièges à éviter et essentiel")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : reprenons les méthodes clés du chapitre --------------------
        intro = Text(
            _wrap(
                "Avant de conclure ce chapitre, reprenons quatre méthodes "
                "clés, trois pièges classiques, puis l'essentiel à "
                "retenir sur le pétrole et le gaz naturel.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant de conclure ce chapitre, reprenons quatre méthodes "
                "clés, trois pièges classiques, puis l'essentiel à "
                "retenir sur le pétrole et le gaz naturel."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : les 4 méthodes ---------------------------------------
        methode1 = method_box(
            Text(
                _wrap(
                    "Méthode 1 — Reconnaître l'opération décrite : "
                    "repérer les mots-clés (« séparer selon la "
                    "température » → distillation ; « casser une grosse "
                    "molécule » → craquage ; « réorganiser sans changer "
                    "le nombre de C » → reformage).",
                    width=48,
                ),
                font_size=20,
            ),
            box_width=11.0,
        )
        methode1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode un : pour reconnaître l'opération décrite dans "
                "un énoncé, repérez les mots-clés. « Séparer selon la "
                "température d'ébullition » signale une distillation. "
                "« Casser une grosse molécule » signale un craquage. "
                "« Réorganiser la structure sans changer le nombre de "
                "carbones » signale un reformage."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            Text(
                _wrap(
                    "Méthode 2 — Équilibrer une équation de craquage ou "
                    "de combustion : ajuster les coefficients dans "
                    "l'ordre C, puis H, puis O (jamais un autre ordre).",
                    width=46,
                ),
                font_size=21,
            ),
            box_width=10.5,
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode deux : pour équilibrer une équation de craquage "
                "ou de combustion, ajustez toujours les coefficients dans "
                "le même ordre : d'abord le carbone, ensuite l'hydrogène, "
                "et enfin l'oxygène. Ne changez jamais cet ordre, sous "
                "peine de vous perdre dans les calculs."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            Text(
                _wrap(
                    "Méthode 3 — Retenir le tableau des fractions dans "
                    "l'ordre CROISSANT de température d'ébullition : GPL, "
                    "essences, kérosène, gasoil, fiouls lourds, bitume.",
                    width=46,
                ),
                font_size=21,
            ),
            box_width=10.5,
        )
        methode3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode trois : apprenez le tableau des fractions dans "
                "l'ordre croissant de température d'ébullition : gaz de "
                "raffinerie et G-P-L, puis essences, puis kérosène, puis "
                "gasoil, puis fiouls lourds, et enfin le bitume, tout en "
                "bas de la colonne."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        methode4 = method_box(
            Text(
                _wrap(
                    "Méthode 4 — Structurer une réponse APC en 3 temps : "
                    "1) identifier la notion et le vocabulaire précis ; "
                    "2) mobiliser la définition ou l'équation adaptée ; "
                    "3) conclure en reliant au contexte concret (SIR, "
                    "PETROCI, environnement…).",
                    width=48,
                ),
                font_size=19,
            ),
            box_width=11.2,
        )
        methode4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode quatre, pour structurer une réponse selon "
                "l'approche par compétences : premier temps, identifier "
                "la notion en jeu et le vocabulaire précis attendu ; "
                "deuxième temps, mobiliser la définition ou l'équation "
                "adaptée ; troisième temps, conclure en reliant votre "
                "réponse au contexte concret, qu'il s'agisse de la S-I-R, "
                "de la PETROCI ou d'un enjeu environnemental."
            )
        ) as tracker:
            self.play(FadeIn(methode4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode4))

        # --- Exemple traité : les 3 pièges classiques ----------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 : la distillation fractionnée est une "
                    "séparation PHYSIQUE, pas une réaction chimique.",
                    width=46,
                ),
                font_size=21,
            ),
            box_width=10.0,
        )
        piege1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Premier piège classique : la distillation fractionnée "
                "est une séparation physique, ce n'est pas une réaction "
                "chimique."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            Text(
                _wrap(
                    "Piège 2 : l'indice d'octane n'est PAS un pourcentage "
                    "d'octane réellement présent, c'est une échelle de "
                    "comparaison avec un mélange de référence "
                    "heptane/isooctane.",
                    width=46,
                ),
                font_size=21,
            ),
            box_width=10.0,
        )
        piege2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Deuxième piège : l'indice d'octane n'est pas un "
                "pourcentage d'octane réellement présent dans l'essence. "
                "C'est une échelle de comparaison avec un mélange de "
                "référence d'heptane et d'isooctane."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            Text(
                _wrap(
                    "Piège 3 : le gaz naturel (méthane, extrait d'un "
                    "gisement) n'est PAS le même produit que le butane du "
                    "GPL (obtenu par raffinage).",
                    width=46,
                ),
                font_size=21,
            ),
            box_width=10.0,
        )
        piege3.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Troisième et dernier piège : le gaz naturel, "
                "essentiellement du méthane extrait d'un gisement, n'est "
                "pas le même produit que le butane du G-P-L, qui lui est "
                "obtenu par raffinage du pétrole."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- À retenir : essentiel_box récapitulatif du chapitre -----------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Le pétrole et le gaz naturel, énergies fossiles non "
                    "renouvelables, se forment en millions d'années",
                    "Le raffinage sépare (distillation) puis transforme "
                    "(craquage, reformage) le brut en produits utiles",
                    "La Côte d'Ivoire produit et raffine son pétrole "
                    "(PETROCI, SIR) et en tire une part de son électricité",
                    "Leur exploitation et leur combustion posent des "
                    "enjeux environnementaux majeurs (CO₂, marées noires…)",
                ],
                font_size=18,
                width=52,
            ),
            box_width=11.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.45)
        _fit(essentiel, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de ce chapitre. Le pétrole et le "
                "gaz naturel sont des énergies fossiles non renouvelables, "
                "qui se forment en plusieurs millions d'années. Le "
                "raffinage sépare d'abord le brut par distillation, puis "
                "le transforme par craquage et reformage, pour obtenir "
                "des produits toujours plus utiles. La Côte d'Ivoire "
                "produit et raffine son pétrole, grâce à la PETROCI et à "
                "la S-I-R, et en tire même une part de son électricité. "
                "Enfin, leur exploitation comme leur combustion posent des "
                "enjeux environnementaux majeurs, du dioxyde de carbone "
                "aux marées noires, qu'il ne faut jamais perdre de vue."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
