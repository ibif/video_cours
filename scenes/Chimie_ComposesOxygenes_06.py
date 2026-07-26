"""
scenes/Chimie_ComposesOxygenes_06.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 06.

§ Les acides carboxyliques : groupe carboxyle -COOH, formule générale
R-COOH, CₙH₂ₙO₂, M=14n+32, nomenclature « acide ...oïque », exemples
naturels, acidité faible (équilibre, justification du pH mesuré).
Source : 1ereC/Chimie.pdf, chapitre 6, pages 60-61.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
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
from shapes.boxes import definition_box, method_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class AcidesCarboxyliques(NotionScene):
    def construct(self):
        titre = scene_title("Les acides carboxyliques")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : le groupe carboxyle -------------------------------------------
        def_carboxyle = definition_box(
            VGroup(
                Text(
                    "Le groupe carboxyle réunit un groupe carbonyle et un",
                    font_size=22,
                ),
                Text("groupe hydroxyle SUR LE MÊME carbone :", font_size=22),
                MathTex(r"-COOH \qquad R-COOH", font_size=30, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25),
        )
        def_carboxyle.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les acides carboxyliques sont caractérisés par le groupe "
                "carboxyle, qui réunit sur un même atome de carbone un "
                "groupe carbonyle et un groupe hydroxyle. On le note "
                "moins C-O-O-H, et un acide carboxylique s'écrit R-C-O-O-H."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_carboxyle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_carboxyle))

        # --- Raisonnement : formule brute + nomenclature ----------------------------
        entete_formule = Text("Formule brute et masse molaire", font_size=24, color=YELLOW, weight="BOLD")
        entete_formule.next_to(titre, DOWN, buff=0.4)

        formule = MathTex(r"C_nH_{2n}O_2 \quad (n \geq 1) \qquad M = 14n+32", font_size=28, color=WHITE)
        formule.next_to(entete_formule, DOWN, buff=0.45)

        groupe_formule = VGroup(entete_formule, formule)

        with self.voiceover(
            text=(
                "Sa formule brute générale est C indice n, H indice deux "
                "n, O-2, avec n supérieur ou égal à un, et sa masse "
                "molaire vaut quatorze n plus trente-deux grammes par "
                "mole."
            )
        ) as tracker:
            self.play(FadeIn(entete_formule))
            self.play(Write(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_formule))

        methode = method_box(
            Text(
                _wrap(
                    "Nomenclature : le carbone fonctionnel (celui du "
                    "carboxyle) est TOUJOURS le carbone n°1. On nomme "
                    "« acide » suivi du nom de l'alcane correspondant, dont "
                    "le « e » final est remplacé par le suffixe « -oïque ».",
                    width=48,
                ),
                font_size=21,
            ),
        )
        methode.next_to(titre, DOWN, buff=0.4)
        _fit(methode, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pour nommer un acide carboxylique, le carbone fonctionnel "
                "est toujours le carbone numéro un, comme pour les "
                "aldéhydes. On écrit acide, suivi du nom de l'alcane "
                "correspondant dont le e final est remplacé par le "
                "suffixe -oïque."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : tableau + exemples naturels ---------------------------
        tab_titre = Text("Exemples, et où les trouver", font_size=23, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.35)

        tab = VGroup(
            VGroup(MathTex(r"HCOOH", font_size=26), Text("acide méthanoïque — piqûres de fourmi", font_size=19)).arrange(RIGHT, buff=0.6),
            VGroup(MathTex(r"CH_3-COOH", font_size=26), Text("acide éthanoïque — vinaigre", font_size=19)).arrange(RIGHT, buff=0.6),
            VGroup(MathTex(r"CH_3-CH_2-COOH", font_size=26), Text("acide propanoïque", font_size=19)).arrange(RIGHT, buff=0.6),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        tab.next_to(tab_titre, DOWN, buff=0.4)

        note_citron = Text("(le citron doit son acidité principalement à l'acide citrique)", font_size=18, color=WHITE)
        note_citron.next_to(tab, DOWN, buff=0.35)

        groupe_tab = VGroup(tab_titre, tab, note_citron)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "H-C-O-O-H se nomme acide méthanoïque : c'est lui qui "
                "provoque la douleur des piqûres de fourmi. C-H-3, C-O-O-H "
                "se nomme acide éthanoïque, celui du vinaigre. C-H-3, "
                "C-H-2, C-O-O-H se nomme acide propanoïque. Le citron, "
                "quant à lui, doit son acidité principalement à l'acide "
                "citrique, un acide carboxylique plus complexe."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tab))
            self.play(FadeIn(note_citron))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- À retenir : acidité faible ----------------------------------------------
        acidite = property_box(
            VGroup(
                Text("Un acide carboxylique est un ACIDE FAIBLE : il ne réagit", font_size=21),
                Text("que PARTIELLEMENT avec l'eau (équilibre chimique) :", font_size=21),
                MathTex(r"R-COOH + H_2O \; \rightleftharpoons \; R-COO^- + H_3O^+", font_size=26, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.28),
            box_width=12.0,
        )
        acidite.next_to(titre, DOWN, buff=0.4)
        _fit(acidite, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Propriété essentielle : un acide carboxylique est un acide "
                "faible. Il ne réagit que partiellement avec l'eau, "
                "contrairement à un acide fort : la réaction est un "
                "équilibre chimique, symbolisé par une double flèche. "
                "R-C-O-O-H plus H-2-O est en équilibre avec R-C-O-O moins "
                "plus H-3-O plus."
            )
        ) as tracker:
            self.play(FadeIn(acidite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(acidite))

        # --- Piège / justification : pH mesuré vs pH théorique -----------------------
        justification = property_box(
            Text(
                _wrap(
                    "Pour une solution d'acide éthanoïque à c=10⁻² mol/L, le "
                    "pH mesuré vaut environ 3,4, alors qu'un acide FORT de "
                    "même concentration donnerait un pH théorique de 2 "
                    "(pH=-log c). Le pH mesuré est supérieur : preuve que "
                    "la dissociation n'est que partielle.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        justification.next_to(titre, DOWN, buff=0.4)
        _fit(justification, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici la preuve expérimentale de cette faiblesse. Pour une "
                "solution d'acide éthanoïque à la concentration de dix "
                "puissance moins deux mole par litre, le pH mesuré vaut "
                "environ trois virgule quatre. Or, un acide fort de même "
                "concentration donnerait un pH théorique de deux, puisque "
                "pH égale moins logarithme de c. Le pH mesuré, plus élevé "
                "que ce pH théorique, prouve que seule une partie des "
                "molécules d'acide éthanoïque s'est dissociée dans l'eau."
            )
        ) as tracker:
            self.play(FadeIn(justification))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(justification), FadeOut(titre))
