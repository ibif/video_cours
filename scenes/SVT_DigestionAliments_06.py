"""
scenes/SVT_DigestionAliments_06.py — Chapitre 12 (1ereD, SVT), scène 06.

§ 12.4.1-12.4.2 La digestion chimique dans la bouche (amylase salivaire /
ptyaline sur l'amidon) et dans l'estomac (HCl + pepsine sur les protéines,
lipase gastrique, mucus). Piège : la pepsine ne digère pas les graisses et
n'agit qu'en milieu acide, dans l'estomac.
Source : 1ereD/SVT.pdf, pages 159-160.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class DigestionChimiqueBoucheEtEstomac(NotionScene):
    def construct(self):
        titre = scene_title("12.4 — Digestion chimique : bouche et estomac")
        titre.scale(0.56)
        titre.to_edge(UP)

        # --- Énoncé : la salive et son enzyme ---------------------------------
        salive_txt = Text(
            _wrap(
                "La salive (1 à 1,5 L/jour) contient eau, mucus "
                "(lubrifiant), sels, un antiseptique (le lysozyme) et une "
                "enzyme : l'amylase salivaire, dite ptyaline. Son pH est "
                "voisin de 7 (neutre).",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        salive_txt.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La salive, sécrétée au rythme d'un à un litre et demi par "
                "jour, contient de l'eau, du mucus qui lubrifie le bol, "
                "des sels, un antiseptique, le lysozyme, et une enzyme : "
                "l'amylase salivaire, encore appelée ptyaline. Son pH est "
                "voisin de sept, neutre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(salive_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(salive_txt))

        # --- Animation du raisonnement : amidon → maltose + dextrines ---------
        reaction1 = MathTex(
            r"\text{amidon} \xrightarrow{\;\text{amylase salivaire}\;} \text{maltose} + \text{dextrines}",
            font_size=32,
            color=WHITE,
        )
        reaction1.next_to(titre, DOWN, buff=0.7)

        note1 = Text(
            _wrap(
                "L'action de la ptyaline se poursuit un moment dans le "
                "haut de l'estomac, tant que le bol n'est pas encore "
                "acidifié.",
                width=52,
            ),
            font_size=21,
            color=WHITE,
        )
        note1.next_to(reaction1, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'amylase salivaire attaque les longues chaînes de "
                "l'amidon et les découpe en maltose et en fragments courts "
                "appelés dextrines. Le séjour des aliments dans la bouche "
                "est bref ; l'action de la ptyaline se poursuit toutefois "
                "un certain temps dans le haut de l'estomac, tant que le "
                "bol n'a pas été complètement acidifié."
            )
        ) as tracker:
            self.play(Write(reaction1))
            self.play(FadeIn(note1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reaction1), FadeOut(note1))

        # --- Dans l'estomac : le suc gastrique ---------------------------------
        entete_estomac = Text("Dans l'estomac : le suc gastrique", font_size=25, color=YELLOW, weight="BOLD")
        entete_estomac.next_to(titre, DOWN, buff=0.45)

        estomac_bullets = _bullets(
            [
                "Acide chlorhydrique (HCl) : pH très acide (1,5-2) ; désagrège les aliments, tue les microbes, active le pepsinogène en pepsine.",
                "Pepsine : découpe les grosses protéines en polypeptides (peptones).",
                "Lipase gastrique : action modeste chez l'adulte, importante chez le nourrisson.",
                "Mucus : tapisse et protège la paroi de l'acide et de la pepsine.",
            ],
            font_size=19,
            width=56,
        )
        estomac_bullets.next_to(entete_estomac, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le suc gastrique, deux à trois litres par jour, contient "
                "l'acide chlorhydrique, qui donne au contenu de l'estomac "
                "un pH très acide, compris entre un virgule cinq et deux ; "
                "cet acide désagrège les aliments, tue la plupart des "
                "microbes avalés, et transforme le pepsinogène, forme "
                "inactive, en pepsine, forme active. Il contient aussi la "
                "pepsine elle-même, une lipase gastrique d'action modeste "
                "chez l'adulte mais importante chez le nourrisson, et du "
                "mucus qui tapisse la paroi de l'estomac et la protège de "
                "l'acide et de la pepsine."
            )
        ) as tracker:
            self.play(FadeIn(entete_estomac))
            self.play(FadeIn(estomac_bullets))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_estomac), FadeOut(estomac_bullets))

        # --- Exemple traité : les protéines du poisson d'Awa ------------------
        reaction2 = MathTex(
            r"\text{prot\'eines} \xrightarrow{\;\text{pepsine (HCl)}\;} \text{polypeptides}",
            font_size=34,
            color=WHITE,
        )
        reaction2.next_to(titre, DOWN, buff=0.7)

        exemple = example_box(
            Text(
                _wrap(
                    "Les protéines du poisson braisé d'Awa arrivent dans "
                    "l'estomac. En présence d'acide chlorhydrique, la "
                    "pepsine les découpe en polypeptides — première étape "
                    "de leur digestion, qui s'achèvera dans l'intestin "
                    "grêle.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(reaction2, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La pepsine, enzyme qui découpe les grosses protéines en "
                "fragments plus courts, les polypeptides, appelés aussi "
                "peptones. Exemple traité : les protéines du poisson "
                "braisé d'Awa arrivent dans l'estomac. En présence d'acide "
                "chlorhydrique, la pepsine les découpe en polypeptides — "
                "première étape de leur digestion, qui s'achèvera plus "
                "loin, dans l'intestin grêle."
            )
        ) as tracker:
            self.play(Write(reaction2))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reaction2), FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------
        a_retenir = definition_box(
            Text(
                _wrap(
                    "À retenir : dans la bouche, l'amylase salivaire "
                    "attaque l'amidon (milieu neutre). Dans l'estomac, "
                    "l'acide chlorhydrique crée un milieu très acide qui "
                    "active la pepsine, laquelle attaque les protéines. "
                    "Chaque enzyme a son terrain d'action et son "
                    "substrat.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        a_retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : dans la bouche, l'amylase salivaire attaque "
                "l'amidon, en milieu neutre. Dans l'estomac, l'acide "
                "chlorhydrique crée un milieu très acide qui active la "
                "pepsine, laquelle attaque les protéines. Chaque enzyme a "
                "donc son terrain d'action et son substrat propre."
            )
        ) as tracker:
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(a_retenir))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La pepsine ne travaille qu'en milieu acide ; à pH "
                    "neutre ou basique, elle est inactive. Ne dis donc "
                    "jamais que « la pepsine digère les graisses » ni "
                    "qu'elle « agit dans l'intestin » : son terrain "
                    "d'action est l'estomac, et son substrat est la "
                    "protéine.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention : la pepsine ne travaille qu'en milieu acide. À "
                "pH neutre ou basique, elle est inactive. C'est l'acide "
                "chlorhydrique du suc gastrique qui crée les conditions de "
                "son action. Ne dis donc jamais que la pepsine digère les "
                "graisses, ni qu'elle agit dans l'intestin : son terrain "
                "d'action est l'estomac, et son substrat est la protéine."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
