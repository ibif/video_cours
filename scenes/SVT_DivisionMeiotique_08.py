"""
scenes/SVT_DivisionMeiotique_08.py — Chapitre 2 (1ereD, SVT), scène 08.

§ 2.4.3 Quand la méiose se dérègle : la trisomie 21 (non-disjonction en
anaphase I) ; L'ESSENTIEL DU CHAPITRE en clôture. Source : 1ereD/SVT.pdf,
pages 28-30.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, FadeIn, FadeOut, MathTex, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class TrisomieEtEssentielDuChapitre(NotionScene):
    def construct(self):
        titre = scene_title("2.4.3 — Quand la méiose se dérègle")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : la non-disjonction --------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Il arrive, rarement, que la méiose se déroule mal. Si, "
                    "en anaphase I, les deux homologues d'une paire ne se "
                    "séparent pas - on parle de non-disjonction -, l'un des "
                    "gamètes reçoit un chromosome en supplément (n+1) et "
                    "l'autre en perd un (n-1).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Il arrive, rarement, que la méiose se déroule mal. Si, en "
                "anaphase I, les deux homologues d'une paire ne se séparent "
                "pas, on parle de non-disjonction. L'un des gamètes reçoit "
                "alors un chromosome en supplément, n plus un, et l'autre en "
                "perd un, n moins un."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement / exemple traité : trisomie 21 ------------
        exemple = example_box(
            Text(
                _wrap(
                    "Gamète anormal à n+1=24 chromosomes (dont deux "
                    "chromosomes 21), fécondé par un gamète normal à 23 "
                    "chromosomes. Zygote : 24+23=47 chromosomes, avec "
                    "TROIS chromosomes 21 -> trisomie 21. La précision de "
                    "la méiose, notamment de la séparation des homologues "
                    "en anaphase I, est donc vitale.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        calcul = MathTex(r"n{+}1 = 24 \;+\; n = 23 \;\longrightarrow\; 47 \text{ chromosomes}", font_size=26, color=WHITE)
        calcul.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Chez l'être humain, si un gamète à n plus un égale "
                "vingt-quatre chromosomes, portant deux chromosomes vingt-et-"
                "un, est fécondé par un gamète normal à vingt-trois "
                "chromosomes, le zygote possède vingt-quatre plus vingt-trois "
                "égale quarante-sept chromosomes, avec trois chromosomes "
                "vingt-et-un : c'est la trisomie vingt-et-un. Cet exemple "
                "médical montre à quel point la précision de la méiose est "
                "vitale : la séparation des homologues en anaphase I doit "
                "être parfaite."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.play(Write(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(calcul))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas la trisomie 21 avec une mutation : "
                    "aucun gène n'est modifié, c'est un accident de "
                    "RÉPARTITION des chromosomes (un chromosome entier en "
                    "trop), pas un changement de l'ADN lui-même - la même "
                    "distinction que pour l'enjambement, qui n'est pas non "
                    "plus une mutation.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre la trisomie vingt-et-un avec "
                "une mutation : aucun gène n'est modifié, c'est un accident "
                "de répartition des chromosomes, un chromosome entier en "
                "trop, et non un changement de l'ADN lui-même - la même "
                "distinction que pour l'enjambement, qui n'est pas non plus "
                "une mutation."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) ------------------------
        titre_fin = scene_title("L'essentiel du chapitre 2")
        titre_fin.scale(0.65)
        titre_fin.to_edge(UP)
        self.play(FadeOut(titre), FadeIn(titre_fin))
        titre = titre_fin

        essentiel = essentiel_box(
            _bullets(
                [
                    "Méiose : 1 cellule mère diploïde (2n) -> 4 cellules "
                    "filles haploïdes (n), différentes ; 2 divisions, 1 "
                    "seule réplication de l'ADN avant.",
                    "Ordre : prophase I, métaphase I, anaphase I, télophase "
                    "I, puis prophase II à télophase II.",
                    "Anaphase I : séparation des homologues, centromères "
                    "intacts -> réduction (2n vers n).",
                    "Anaphase II : séparation des chromatides sœurs, "
                    "centromères scindés.",
                    "On compte les chromosomes en comptant les "
                    "centromères : un chromosome dédoublé reste 1 "
                    "chromosome.",
                    "Brassage interchromosomique (assortiment indépendant, "
                    "2^n gamètes) + brassage intrachromosomique "
                    "(enjambements, prophase I).",
                    "Quantité d'ADN : Q -> 2Q (réplication) -> Q (fin 1ère "
                    "division) -> Q/2 (fin 2ème division).",
                    "Alternance méiose (2n->n) / fécondation (n->2n) : "
                    "constance du nombre de chromosomes + diversité des "
                    "individus.",
                ],
                font_size=17,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si le contenu (8 points) dépasse la hauteur visible du
        # cadre, on réduit l'échelle globale de la boîte pour qu'elle tienne
        # entièrement à l'écran (technique de SVT_FonctionsGonades_09.py).
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. La méiose transforme une "
                "seule cellule mère diploïde, à deux n, en quatre cellules "
                "filles haploïdes, à n, génétiquement différentes ; elle "
                "comporte deux divisions, mais une seule réplication de "
                "l'ADN, avant la première. L'ordre des étapes est : prophase "
                "I, métaphase I, anaphase I, télophase I, puis prophase II, "
                "métaphase II, anaphase II, télophase II. En anaphase I, ce "
                "sont les homologues qui se séparent, centromères intacts : "
                "c'est la réduction, de deux n vers n. En anaphase II, ce "
                "sont les chromatides sœurs qui se séparent, centromères "
                "scindés. On compte toujours les chromosomes en comptant les "
                "centromères : un chromosome dédoublé reste un seul "
                "chromosome. La diversité génétique vient de deux "
                "mécanismes : le brassage interchromosomique, l'assortiment "
                "indépendant, qui donne deux puissance n types de gamètes, "
                "et le brassage intrachromosomique, les enjambements, en "
                "prophase I. La quantité d'ADN suit Q, puis deux Q après "
                "réplication, puis Q à la fin de la première division, puis "
                "Q sur deux à la fin de la deuxième. Enfin, l'alternance "
                "entre méiose, qui réduit de deux n à n, et fécondation, qui "
                "ramène de n à deux n, assure à la fois la constance du "
                "nombre de chromosomes de l'espèce et la diversité de tous "
                "les individus qu'elle produit - la solution des deux "
                "énigmes de la famille de Mamadou et Affoué."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
