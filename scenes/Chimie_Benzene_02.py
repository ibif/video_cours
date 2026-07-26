"""
scenes/Chimie_Benzene_02.py — Chapitre 4 (1ereC, Chimie), scène 02.

§ Le problème posé par la formule C6H6 : comparaison avec l'hexane C6H14
(8 hydrogènes de moins → forte insaturation attendue), mais les faits
expérimentaux contredisent l'hypothèse alcène/alcyne : pas de décoloration
de l'eau de brome, réactions de substitution (pas d'addition), molécule
plane hexagonale régulière, liaisons C-C toutes identiques à 140 pm
(valeur intermédiaire entre simple 154 pm et double 134 pm).
Source : 1ereC/Chimie.pdf, chapitre 4, pages 36-37.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    GREEN,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title


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


class ProblemeFormuleC6H6(NotionScene):
    def construct(self):
        titre = scene_title("2. Le problème posé par la formule C6H6")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé : comparaison avec l'hexane ---------------------------------
        comparaison = MathTex(
            r"C_6H_{14} \ (\text{hexane}) \quad \text{vs} \quad C_6H_6 \ (\text{benzène})",
            font_size=32,
            color=WHITE,
        )
        comparaison.next_to(titre, DOWN, buff=0.5)

        ecart = Text(
            _wrap(
                "Pour un même nombre de 6 atomes de carbone, le benzène "
                "possède 8 atomes d'hydrogène de moins que l'hexane. Une "
                "molécule saturée à 6 carbones devrait compter 14 "
                "hydrogènes, pas 6.",
                width=52,
            ),
            font_size=24,
            color=WHITE,
        )
        ecart.next_to(comparaison, DOWN, buff=0.5)

        groupe1 = VGroup(comparaison, ecart)

        with self.voiceover(
            text=(
                "Comparons le benzène à l'hexane, l'alcane saturé à six "
                "atomes de carbone, de formule C six H quatorze. Pour un "
                "même nombre de six carbones, le benzène possède huit "
                "atomes d'hydrogène de moins. Cet écart important laisse "
                "penser à une molécule très insaturée, comme un alcène ou "
                "un alcyne à plusieurs doubles ou triples liaisons."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(comparaison))
            self.play(FadeIn(ecart))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        # --- Animation du raisonnement : les faits expérimentaux qui contredisent
        entete = Text("Mais les faits expérimentaux le contredisent…", font_size=25, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        faits = _bullets(
            [
                "Le benzène ne décolore PAS l'eau de brome (test "
                "caractéristique des alcènes/alcynes)",
                "Le benzène subit des réactions de SUBSTITUTION, et non "
                "des réactions d'ADDITION",
                "La molécule est PLANE, de forme hexagonale RÉGULIÈRE",
                "Les 6 liaisons C–C sont toutes IDENTIQUES : 140 pm "
                "(valeur intermédiaire entre 154 pm pour C–C simple et "
                "134 pm pour C=C double)",
            ],
            font_size=22,
            width=54,
        )
        faits.next_to(entete, DOWN, buff=0.35)
        groupe_faits = VGroup(entete, faits)
        _fit(groupe_faits, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Or, l'expérience contredit clairement cette hypothèse. "
                "Premièrement, le benzène ne décolore pas l'eau de brome, "
                "alors que c'est le test caractéristique des alcènes et "
                "des alcynes. Deuxièmement, le benzène subit des réactions "
                "de substitution, et non des réactions d'addition. "
                "Troisièmement, la molécule est plane, de forme "
                "hexagonale parfaitement régulière. Enfin, les six "
                "liaisons carbone-carbone du cycle sont toutes "
                "identiques, avec une longueur de cent quarante "
                "picomètres — une valeur intermédiaire entre celle d'une "
                "liaison simple, cent cinquante-quatre picomètres, et "
                "celle d'une liaison double, cent trente-quatre "
                "picomètres."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(faits))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_faits))

        # --- Exemple traité : la longueur de liaison, indice clé ----------------
        entete2 = Text("La longueur de liaison, un indice décisif", font_size=25, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        echelle = VGroup(
            Text("C–C simple : 154 pm", font_size=24, color=GREEN),
            Text("C–C benzène : 140 pm", font_size=24, color=YELLOW),
            Text("C=C double : 134 pm", font_size=24, color=RED),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        echelle.next_to(entete2, DOWN, buff=0.5)

        groupe2 = VGroup(entete2, echelle)

        with self.voiceover(
            text=(
                "Cette valeur de cent quarante picomètres est l'indice "
                "décisif : elle n'est ni celle d'une liaison simple, ni "
                "celle d'une liaison double, mais se situe exactement "
                "entre les deux. Aucune formule alternée simple-double, "
                "comme celle d'un cyclohexatriène classique, ne peut "
                "expliquer à elle seule six liaisons parfaitement "
                "identiques."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(echelle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir -------------------------------------------------------------
        retenir = Text(
            _wrap(
                "À retenir : la formule brute C6H6 suggère une forte "
                "insaturation, mais le comportement chimique et la "
                "structure géométrique du benzène ne correspondent ni à "
                "un alcène, ni à un alcyne classique. Il faut imaginer "
                "une nouvelle structure — c'est ce que proposera Kekulé.",
                width=50,
            ),
            font_size=25,
            color=WHITE,
        )
        retenir.next_to(titre, DOWN, buff=0.6)
        _fit(retenir, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons donc que la formule brute C six H six suggère "
                "une forte insaturation, mais que le comportement "
                "chimique et la structure géométrique du benzène ne "
                "correspondent ni à un alcène, ni à un alcyne classique. "
                "Il faut imaginer une structure nouvelle — c'est "
                "précisément ce que va proposer le chimiste allemand "
                "Kekulé."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
