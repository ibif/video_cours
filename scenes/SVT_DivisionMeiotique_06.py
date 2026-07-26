"""
scenes/SVT_DivisionMeiotique_06.py — Chapitre 2 (1ereD, SVT), scène 06.

§ 2.3.2-2.3.3 Le brassage intrachromosomique : l'enjambement (crossing-
over), exemple du maïs (allèles A/B, a/b), conséquences du brassage
génétique, méthode de calcul du nombre de gamètes/zygotes différents.
Source : 1ereD/SVT.pdf, pages 24-26.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    MAROON,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class BrassageIntrachromosomique(NotionScene):
    def construct(self):
        titre = scene_title("2.3 — Le brassage intrachromosomique")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : définition de l'enjambement -------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "En prophase I, au sein d'un bivalent, deux chromatides "
                    "non sœurs (l'une paternelle, l'autre maternelle) "
                    "peuvent se rompre au même point et échanger des "
                    "segments : c'est un enjambement, ou crossing-over. Les "
                    "chromatides ayant échangé des segments sont dites "
                    "recombinées.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En prophase I, au sein d'un bivalent, deux chromatides non "
                "sœurs - l'une appartenant à l'homologue d'origine "
                "paternelle, l'autre à l'homologue d'origine maternelle - "
                "peuvent se rompre au même point et échanger des segments : "
                "c'est un enjambement, appelé aussi crossing-over. Les "
                "chromatides qui ont échangé des segments sont dites "
                "recombinées : elles portent un assemblage nouveau d'allèles "
                "paternels et maternels. Ce mécanisme constitue le brassage "
                "intrachromosomique, à l'intérieur d'un même couple "
                "d'homologues."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma avant / après enjambement -------
        sous_titre = Text("Avant / après l'enjambement (2 gènes A/B)", font_size=23, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.45)

        def _chromatide(color, top_label, bot_label):
            rect = Rectangle(width=0.22, height=1.3, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
            top = Text(top_label, font_size=18, color=YELLOW).next_to(rect, UP, buff=0.1)
            bot = Text(bot_label, font_size=18, color=YELLOW).next_to(rect, DOWN, buff=0.1)
            return VGroup(rect, top, bot)

        # Avant : 2 chromatides paternelles (A,B) + 2 maternelles (a,b), reliées par 1 centromère
        pat1 = _chromatide(BLUE, "A", "B")
        pat2 = _chromatide(BLUE, "A", "B")
        mat1 = _chromatide(MAROON, "a", "b")
        mat2 = _chromatide(MAROON, "a", "b")
        avant = VGroup(pat1, pat2, mat1, mat2).arrange(RIGHT, buff=0.1)
        dot_avant = Dot(radius=0.06, color=YELLOW).move_to(avant.get_center())
        avant.add(dot_avant)
        label_avant = Text("Bivalent avant enjambement (4 chromatides)", font_size=17, color=WHITE)
        bloc_avant = VGroup(avant, label_avant).arrange(DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Illustrons avec deux gènes situés sur la même paire "
                "d'homologues : le gène d'allèles A ou a, et le gène "
                "d'allèles B ou b. Avant l'enjambement, le bivalent contient "
                "quatre chromatides : les deux chromatides paternelles "
                "portent A et B, les deux chromatides maternelles portent a "
                "et b."
            )
        ) as tracker:
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(bloc_avant))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_avant))

        # Après : chromatides internes (pat2, mat1) échangent leur partie basse (B <-> b)
        pat1_ap = _chromatide(BLUE, "A", "B")
        pat2_ap = _chromatide(BLUE, "A", "b")   # recombinée
        mat1_ap = _chromatide(MAROON, "a", "B")  # recombinée
        mat2_ap = _chromatide(MAROON, "a", "b")
        apres = VGroup(pat1_ap, pat2_ap, mat1_ap, mat2_ap).arrange(RIGHT, buff=0.3)
        dot_apres = Dot(radius=0.06, color=YELLOW).move_to(apres.get_center())
        apres.add(dot_apres)
        # Étiquettes courtes (AB / Ab / aB / ab), en jaune pour les 2
        # chromatides recombinées ; espacées comme les chromatides
        # elles-mêmes pour ne jamais se chevaucher.
        etiquettes = VGroup(
            Text("AB", font_size=16, color=WHITE),
            Text("Ab", font_size=16, color=YELLOW),
            Text("aB", font_size=16, color=YELLOW),
            Text("ab", font_size=16, color=WHITE),
        )
        for et, chromatide in zip(etiquettes, [pat1_ap, pat2_ap, mat1_ap, mat2_ap]):
            et.next_to(chromatide, DOWN, buff=0.55)
        legende_recombinees = Text("(en jaune : chromatides recombinées)", font_size=15, color=YELLOW)
        label_apres = Text("Bivalent après enjambement : 2 parentales + 2 recombinées", font_size=17, color=WHITE)

        bloc_apres = VGroup(apres, etiquettes, legende_recombinees, label_apres).arrange(DOWN, buff=0.25)
        bloc_apres.move_to(bloc_avant.get_center())

        with self.voiceover(
            text=(
                "Après l'enjambement, deux chromatides non sœurs internes "
                "ont échangé un segment : deux chromatides recombinées "
                "apparaissent. L'une porte désormais A avec b, l'autre a "
                "avec B. Au total, le bivalent porte quatre types de "
                "chromatides : deux parentales, A B et a b, non modifiées, et "
                "deux recombinées, A b et a B, nouvelles - qui donneront "
                "quatre types de gamètes différents."
            )
        ) as tracker:
            self.play(FadeIn(bloc_apres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_apres), FadeOut(sous_titre))

        # --- Exemple traité : le maïs -------------------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Maïs : chromosome paternel porte A et B, maternel porte "
                    "a et b. Sans enjambement : 2 types de gamètes, AB et ab "
                    "(parentaux). Avec un enjambement entre les 2 gènes : 4 "
                    "types de gamètes, AB, ab (parentaux) + Ab, aB "
                    "(recombinés) - nouvelle diversité.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons un plant de maïs qui possède, sur une même paire "
                "d'homologues, les allèles A et B sur le chromosome "
                "paternel, et a et b sur le chromosome maternel. Sans "
                "enjambement, les chromatides ne sont pas modifiées : les "
                "gamètes reçoivent soit le chromosome paternel complet, soit "
                "le maternel complet - seulement deux types de gamètes, A B "
                "et a b, dits parentaux. Avec un enjambement entre les deux "
                "gènes, deux chromatides échangent leurs extrémités : la "
                "cellule produit alors quatre types de gamètes, A B et a b "
                "parentaux, plus A b et a B recombinés. De nouvelles "
                "combinaisons d'allèles apparaissent, ce qui augmente encore "
                "la diversité."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : méthode de calcul --------------------------------------
        methode = method_box(
            _bullets(
                [
                    "Détermine n, la moitié de 2n.",
                    "Assortiment indépendant seul : 2^n types de gamètes "
                    "pour un individu.",
                    "Pour un couple (ou un croisement) : 2^n×2^n=2^(2n) "
                    "zygotes différents possibles.",
                    "Précise toujours que les enjambements augmentent "
                    "encore ces nombres.",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour calculer un nombre de gamètes ou de zygotes "
                "différents, procède ainsi. Un : détermine n, la moitié de "
                "deux n. Deux : par le seul assortiment indépendant, applique "
                "la formule deux puissance n pour obtenir le nombre de types "
                "de gamètes d'un individu. Trois : pour un couple ou un "
                "croisement entre deux individus, multiplie les possibilités "
                "des deux partenaires, ce qui donne deux puissance deux n "
                "zygotes différents possibles. Quatre : précise toujours, "
                "dans ta réponse, que les enjambements augmentent encore ces "
                "nombres."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter -----------------------------------------------------------
        piege = warning_box(
            _bullets(
                [
                    "L'enjambement a lieu en prophase I, entre chromatides "
                    "non sœurs de chromosomes HOMOLOGUES - jamais entre "
                    "chromosomes non homologues.",
                    "L'enjambement n'est PAS une mutation : aucun gène "
                    "n'est créé, détruit ou modifié ; seule la combinaison "
                    "des allèles change.",
                    "Toutes les chromatides ne sont pas touchées : dans un "
                    "bivalent, seules 2 chromatides non sœurs participent à "
                    "un enjambement donné.",
                ],
                font_size=19,
                width=52,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois précisions à ne jamais oublier sur l'enjambement. "
                "D'abord, il a lieu en prophase I, entre chromatides non "
                "sœurs de chromosomes homologues ; il n'a jamais lieu entre "
                "des chromosomes non homologues. Ensuite, l'enjambement "
                "n'est pas une mutation : aucun gène n'est créé, détruit ou "
                "modifié, seule la combinaison des allèles sur les "
                "chromosomes change. Enfin, toutes les chromatides ne sont "
                "pas touchées : dans un bivalent, seules deux chromatides non "
                "sœurs participent à un enjambement donné, les deux autres "
                "restent parentales. Grâce à l'assortiment indépendant "
                "multiplié par les enjambements, chaque gamète est "
                "pratiquement unique, ce qui est une richesse pour "
                "l'adaptation de l'espèce et pour le travail des "
                "sélectionneurs de maïs, de riz ou de cacaoyers."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
