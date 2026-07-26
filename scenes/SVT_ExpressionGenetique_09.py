"""
scenes/SVT_ExpressionGenetique_09.py — Chapitre 5 (1ereC, SVT), scène 09.

V. La traduction : de l'ARNm à la protéine. A. Les 3 acteurs (ribosome,
ARNt avec définition de l'anticodon, acides aminés). B. Les 3 étapes
(initiation, élongation, terminaison), avec schéma d'un ribosome en train
de traduire. Source : 1ereC/SVT.pdf, pages 49-50.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Ellipse,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    Triangle,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _codon_strip(codons, cell_w=1.15, cell_h=0.55):
    strip = VGroup()
    for c in codons:
        rect = Rectangle(width=cell_w, height=cell_h, fill_color="#1E5FA8", fill_opacity=0.4, stroke_color=WHITE, stroke_width=1)
        txt = Text(c, font_size=15, color=WHITE, weight="BOLD")
        txt.move_to(rect.get_center())
        strip.add(VGroup(rect, txt))
    strip.arrange(RIGHT, buff=0)
    return strip


def _arnt(anticodon, aa_label, aa_color):
    """Petit schéma d'un ARNt : triangle (structure repliée) + acide
    aminé accroché (cercle) + anticodon inscrit."""
    corps = Triangle(color=WHITE, fill_color="#595959", fill_opacity=0.6, stroke_width=1)
    corps.scale(0.35).rotate(3.14159)
    aa = Circle(radius=0.16, color=aa_color, fill_color=aa_color, fill_opacity=0.85, stroke_width=1)
    aa.next_to(corps, UP, buff=0.03)
    aa_txt = Text(aa_label, font_size=11, color="#1A1A1A", weight="BOLD")
    aa_txt.move_to(aa.get_center())
    anti_txt = Text(anticodon, font_size=12, color=YELLOW)
    anti_txt.next_to(corps, DOWN, buff=0.05)
    return VGroup(corps, aa, aa_txt, anti_txt)


class LaTraduction(NotionScene):
    def construct(self):
        titre = scene_title("V — La traduction : de l'ARNm à la protéine")
        titre.scale(0.5)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "La traduction a lieu dans le cytoplasme et met en jeu "
                "trois acteurs principaux. Découvrons-les avant de suivre "
                "les trois étapes de la traduction."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : les 3 acteurs ------------------------------------------------
        ribosome = VGroup(
            Ellipse(width=1.4, height=0.9, fill_color="#A42A5A", fill_opacity=0.5, stroke_color="#A42A5A"),
            Ellipse(width=1.1, height=0.6, fill_color="#A42A5A", fill_opacity=0.7, stroke_color="#A42A5A"),
        )
        ribosome[1].next_to(ribosome[0], DOWN, buff=-0.25)
        label_ribosome = Text("1. Ribosome (ARNr + protéines)", font_size=18, color=WHITE)
        label_ribosome.next_to(ribosome, DOWN, buff=0.2)
        bloc_ribosome = VGroup(ribosome, label_ribosome)

        arnt_demo = _arnt("CCG", "Gly", YELLOW)
        arnt_demo.scale(1.8)
        label_arnt = Text("2. ARNt (transporte 1 acide aminé)", font_size=18, color=WHITE)
        label_arnt.next_to(arnt_demo, DOWN, buff=0.25)
        bloc_arnt = VGroup(arnt_demo, label_arnt)

        aa_libres = VGroup(*[Circle(radius=0.14, color=YELLOW, fill_color=YELLOW, fill_opacity=0.7, stroke_width=1) for _ in range(5)])
        aa_libres.arrange(RIGHT, buff=0.15)
        label_aa = Text("3. Acides aminés libres du cytoplasme", font_size=18, color=WHITE)
        label_aa.next_to(aa_libres, DOWN, buff=0.2)
        bloc_aa = VGroup(aa_libres, label_aa)

        acteurs = VGroup(bloc_ribosome, bloc_arnt, bloc_aa).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        acteurs.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Premier acteur : le ribosome. C'est un atelier "
                "d'assemblage, formé d'ARN ribosomique et de protéines. Il "
                "se fixe sur l'ARNm, avance le long de celui-ci codon par "
                "codon, dans le sens cinq prime vers trois prime, et "
                "catalyse la formation des liaisons peptidiques entre les "
                "acides aminés. Deuxième acteur : l'ARN de transfert, ou "
                "ARNt. Chaque ARNt possède, à une extrémité, un site de "
                "fixation pour un acide aminé précis, et à l'autre "
                "extrémité, un anticodon. Troisième acteur : les acides "
                "aminés libres, présents dans le cytoplasme, les briques de "
                "la protéine."
            )
        ) as tracker:
            self.play(FadeIn(bloc_ribosome))
            self.play(FadeIn(bloc_arnt))
            self.play(FadeIn(bloc_aa))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(acteurs))

        # --- Définition : anticodon --------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "L'anticodon est un triplet de 3 nucléotides porté "
                        "par l'ARNt, complémentaire et antiparallèle du "
                        "codon de l'ARNm. Il permet à l'ARNt de reconnaître "
                        "« son » codon et de déposer le bon acide aminé au "
                        "bon endroit.",
                        width=54,
                    ),
                    font_size=22,
                ),
                MathTex(r"\text{codon ARNm } 5'\text{-GGC-}3' \;\leftrightarrow\; \text{anticodon ARNt } 3'\text{-CCG-}5' \;(\text{Gly})", font_size=22, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons cette définition clé. L'anticodon est un triplet "
                "de trois nucléotides porté par l'ARNt, complémentaire et "
                "antiparallèle du codon de l'ARNm. Il permet à l'ARNt de "
                "reconnaître son codon et de déposer le bon acide aminé au "
                "bon endroit. Exemple : au codon d'ARNm cinq prime, G G C, "
                "trois prime, qui code la glycine, correspond l'anticodon "
                "d'ARNt trois prime, C C G, cinq prime."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les 3 étapes + schéma sur un ARNm -------------------
        entete_etapes = Text("Les 3 étapes de la traduction", font_size=23, color=YELLOW, weight="BOLD")
        entete_etapes.next_to(titre, DOWN, buff=0.45)

        codons = ["AUG", "GGC", "UUU", "ACC", "UAA"]
        strip = _codon_strip(codons)
        strip.next_to(entete_etapes, DOWN, buff=1.1)

        rib = VGroup(
            Ellipse(width=1.6, height=1.0, fill_color="#A42A5A", fill_opacity=0.5, stroke_color="#A42A5A"),
            Ellipse(width=1.25, height=0.65, fill_color="#A42A5A", fill_opacity=0.7, stroke_color="#A42A5A"),
        )
        rib[1].next_to(rib[0], DOWN, buff=-0.3)
        rib.move_to(strip[1].get_center() + UP * 0.75)

        arnt_gly = _arnt("CCG", "Gly", YELLOW)
        arnt_gly.next_to(strip[1], DOWN, buff=0.15)

        chaine = VGroup(
            Circle(radius=0.13, color="#4FC3F7", fill_color="#4FC3F7", fill_opacity=0.8, stroke_width=1),
        )
        chaine.next_to(rib, UP, buff=0.15)
        chaine_label = Text("Met", font_size=12, color="#1A1A1A", weight="BOLD").move_to(chaine[0].get_center())

        schema = VGroup(strip, rib, arnt_gly, chaine, chaine_label)
        schema.move_to(entete_etapes.get_center() + DOWN * 2.0)

        with self.voiceover(
            text=(
                "Étape 1, l'initiation. Le ribosome se fixe sur l'ARNm au "
                "niveau du codon d'initiation AUG. Un premier ARNt, "
                "porteur d'une méthionine et d'anticodon trois prime, U A "
                "C, cinq prime, vient s'apparier avec ce codon AUG."
            )
        ) as tracker:
            self.play(FadeIn(entete_etapes))
            self.play(FadeIn(strip), FadeIn(rib), FadeIn(chaine), FadeIn(chaine_label))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Étape 2, l'élongation. Un deuxième ARNt, dont l'anticodon "
                "est complémentaire du codon suivant, ici G G C pour la "
                "glycine, se fixe à côté du premier, avec son acide aminé. "
                "Le ribosome forme une liaison peptidique entre les deux "
                "acides aminés ; le premier ARNt, libéré, quitte le "
                "ribosome. Le ribosome avance d'un codon, un troisième ARNt "
                "se fixe, et ainsi de suite : la chaîne polypeptidique "
                "s'allonge acide aminé après acide aminé."
            )
        ) as tracker:
            self.play(FadeIn(arnt_gly))
            self.play(rib.animate.shift(RIGHT * 1.15))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Étape 3, la terminaison. Lorsque le ribosome atteint un "
                "codon stop, ici U A A, aucun ARNt ne peut s'y fixer : la "
                "traduction s'arrête. La chaîne polypeptidique est libérée, "
                "puis se replie dans l'espace pour devenir une protéine "
                "fonctionnelle. Le ribosome se détache de l'ARNm."
            )
        ) as tracker:
            self.play(rib.animate.move_to(strip[4].get_center() + UP * 0.75), FadeOut(arnt_gly))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(entete_etapes))

        # --- À retenir -----------------------------------------------------------
        essentiel = definition_box(
            _bullets(
                [
                    "Ribosome : avance sur l'ARNm codon par codon (5'→3') "
                    "et forme les liaisons peptidiques.",
                    "ARNt : reconnaît un codon grâce à son anticodon, "
                    "dépose l'acide aminé correspondant.",
                    "Initiation (AUG) → Élongation (chaîne s'allonge) → "
                    "Terminaison (codon stop, protéine libérée).",
                ],
                font_size=20,
                width=54,
            ),
            box_width=11.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de la traduction. Le ribosome avance "
                "sur l'ARNm codon par codon, dans le sens cinq prime vers "
                "trois prime, et forme les liaisons peptidiques. L'ARNt "
                "reconnaît un codon grâce à son anticodon, et dépose "
                "l'acide aminé correspondant. Et les trois étapes "
                "s'enchaînent toujours dans le même ordre : initiation au "
                "codon AUG, élongation pendant laquelle la chaîne "
                "s'allonge, puis terminaison à un codon stop, qui libère la "
                "protéine."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
