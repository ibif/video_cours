"""
scenes/Chimie_DosagesOxydoreduction_01.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 01.

§ Généralités sur les dosages : définition du dosage (titrage), principe du
dosage direct d'oxydoréduction (solution titrante en burette graduée versée
dans la solution titrée placée dans un bécher ou un erlenmeyer), les 3
conditions que doit vérifier la réaction de dosage (totale, rapide, unique),
vocabulaire (solution titrante/burette graduée, solution titrée/pipette
jaugée, volume à l'équivalence Veq).
Source : 1ereC/Chimie.pdf, chapitre 12, pages 113-114.
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
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=54):
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


class DosageDefinitionEtPrincipeDirect(NotionScene):
    def construct(self):
        titre = scene_title("12.1 Dosage direct d'oxydoréduction : définition et principe")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------------
        intro = Text(
            _wrap(
                "On dispose d'une solution dont on ne connaît pas la "
                "concentration exacte : par exemple une eau de Javel, une "
                "eau oxygénée, ou un sel de fer. Comment déterminer "
                "précisément cette concentration inconnue ? Réponse : par "
                "un dosage d'oxydoréduction.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On dispose souvent d'une solution dont on ne connaît pas "
                "la concentration exacte : par exemple une eau de Javel, "
                "une eau oxygénée, ou une solution contenant des ions "
                "fer. Comment déterminer précisément cette concentration "
                "inconnue ? La réponse tient en un mot : le dosage, aussi "
                "appelé titrage. Dans ce chapitre, nous étudions les "
                "dosages qui reposent sur une réaction d'oxydoréduction."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition du dosage ---------------------------------
        def_dosage = definition_box(
            Text(
                _wrap(
                    "Un dosage, ou titrage, est une technique expérimentale "
                    "permettant de déterminer la concentration inconnue "
                    "d'une espèce chimique en solution (la solution "
                    "titrée), à l'aide d'une réaction chimique avec une "
                    "espèce de concentration connue (la solution "
                    "titrante).",
                    width=48,
                ),
                font_size=22,
            ),
        )
        def_dosage.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un dosage, que l'on appelle aussi un titrage, est une "
                "technique expérimentale permettant de déterminer la "
                "concentration inconnue d'une espèce chimique en solution, "
                "appelée la solution titrée, à l'aide d'une réaction "
                "chimique avec une espèce dont la concentration est "
                "connue avec précision, appelée la solution titrante."
            )
        ) as tracker:
            self.play(FadeIn(def_dosage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_dosage))

        def_direct = definition_box(
            Text(
                _wrap(
                    "Dans un dosage DIRECT d'oxydoréduction, la solution "
                    "titrante réagit directement, sans étape "
                    "intermédiaire, avec la solution titrée : elle est "
                    "placée dans une burette graduée et versée "
                    "progressivement dans la solution titrée, contenue "
                    "dans un bécher ou un erlenmeyer, jusqu'à ce que la "
                    "réaction soit terminée.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        def_direct.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans un dosage direct d'oxydoréduction, la solution "
                "titrante réagit directement, sans étape intermédiaire, "
                "avec la solution titrée. Concrètement : la solution "
                "titrante est placée dans une burette graduée, tenue "
                "verticalement au-dessus du récipient, et on la verse "
                "progressivement dans la solution titrée, contenue dans "
                "un bécher ou un erlenmeyer, jusqu'à ce que la réaction "
                "soit terminée."
            )
        ) as tracker:
            self.play(FadeIn(def_direct))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_direct))

        # --- Raisonnement : les 3 conditions de la réaction de dosage -----------
        entete_conditions = Text(
            "Les 3 conditions de la réaction de dosage", font_size=24, color=YELLOW, weight="BOLD"
        )
        entete_conditions.next_to(titre, DOWN, buff=0.35)

        conditions = property_box(
            _bullets(
                [
                    "TOTALE : les réactifs sont entièrement consommés (pas "
                    "d'équilibre) ; on peut donc relier n(réactif) et "
                    "n(produit) par les coefficients stœchiométriques.",
                    "RAPIDE (quasi instantanée) : le repérage de "
                    "l'équivalence, par changement de couleur, doit être "
                    "net et immédiat.",
                    "UNIQUE : aucune réaction secondaire parasite ne doit "
                    "se produire entre les espèces présentes.",
                ],
                font_size=20,
                width=50,
            ),
            box_width=12.2,
        )
        conditions.next_to(entete_conditions, DOWN, buff=0.35)
        groupe_cond = VGroup(entete_conditions, conditions)
        _fit(groupe_cond, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Pour qu'un dosage soit exploitable, la réaction utilisée "
                "doit vérifier trois conditions. Premièrement, elle doit "
                "être totale : les réactifs sont entièrement consommés, "
                "sans équilibre, ce qui permet de relier directement les "
                "quantités de matière par les coefficients "
                "stœchiométriques. Deuxièmement, elle doit être rapide, "
                "quasi instantanée, pour que le repérage de l'équivalence "
                "par changement de couleur soit net. Troisièmement, elle "
                "doit être unique : aucune réaction secondaire parasite ne "
                "doit se produire entre les espèces présentes dans le "
                "mélange."
            )
        ) as tracker:
            self.play(FadeIn(entete_conditions))
            self.play(FadeIn(conditions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_cond))

        # --- Exemple traité : vocabulaire du dosage ------------------------------
        entete_vocab = Text("Vocabulaire à connaître", font_size=24, color=YELLOW, weight="BOLD")
        entete_vocab.next_to(titre, DOWN, buff=0.35)

        vocab = _bullets(
            [
                "Solution TITRANTE (concentration connue) → placée dans "
                "la BURETTE GRADUÉE.",
                "Solution TITRÉE (concentration inconnue) → prélevée à la "
                "PIPETTE JAUGÉE, versée dans le bécher ou l'erlenmeyer.",
                "Volume à l'ÉQUIVALENCE, noté Veq : volume de solution "
                "titrante versé lorsque l'équivalence est atteinte.",
            ],
            font_size=21,
            width=52,
        )
        vocab.next_to(entete_vocab, DOWN, buff=0.35)
        groupe_vocab = VGroup(entete_vocab, vocab)
        _fit(groupe_vocab, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Retenons le vocabulaire indispensable. La solution "
                "titrante, de concentration connue, est placée dans la "
                "burette graduée. La solution titrée, de concentration "
                "inconnue, est prélevée à l'aide d'une pipette jaugée, "
                "puis versée dans le bécher ou l'erlenmeyer. Enfin, le "
                "volume à l'équivalence, noté V-e-q, est le volume de "
                "solution titrante versé au moment précis où "
                "l'équivalence est atteinte."
            )
        ) as tracker:
            self.play(FadeIn(entete_vocab))
            self.play(FadeIn(vocab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_vocab))

        # --- À retenir -------------------------------------------------------------
        retenir = property_box(
            VGroup(
                Text(
                    _wrap(
                        "Dosage direct : la solution titrante (burette) "
                        "réagit directement avec la solution titrée "
                        "(bécher/erlenmeyer).",
                        width=46,
                    ),
                    font_size=21,
                ),
                Text(
                    "Réaction de dosage : TOTALE, RAPIDE, UNIQUE.",
                    font_size=21,
                    weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : dans un dosage direct, la "
                "solution titrante, placée dans la burette, réagit "
                "directement avec la solution titrée, placée dans le "
                "bécher ou l'erlenmeyer. Et la réaction de dosage doit "
                "impérativement être totale, rapide et unique."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne jamais inverser solution titrante et solution "
                    "titrée : la titrante (concentration connue) est "
                    "TOUJOURS dans la burette ; la titrée (concentration "
                    "inconnue, celle qu'on cherche) est TOUJOURS dans le "
                    "bécher ou l'erlenmeyer. Une inversion fausse tout le "
                    "calcul final.",
                    width=48,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : il ne faut jamais "
                "inverser la solution titrante et la solution titrée. La "
                "titrante, dont la concentration est connue, est toujours "
                "dans la burette. La titrée, dont la concentration est "
                "inconnue, celle que l'on cherche justement à déterminer, "
                "est toujours dans le bécher ou l'erlenmeyer. Une "
                "inversion des deux fausse complètement le calcul final."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
