"""
scenes/SVT_DivisionMeiotique_03.py — Chapitre 2 (1ereD, SVT), scène 03.

§ 2.2.1-2.2.2 Généralités sur la méiose (définition, localisation,
réplication préalable) et première division, réductionnelle : prophase I,
métaphase I, anaphase I, télophase I - séparation des homologues (pas des
chromatides). Source : 1ereD/SVT.pdf, pages 20-21.
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
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _chr(color, height=1.0, width=0.2, gap=0.07):
    """Chromosome dédoublé : 2 chromatides sœurs + 1 centromère (point)."""
    left = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    right = left.copy()
    paire = VGroup(left, right).arrange(RIGHT, buff=gap)
    dot = Dot(radius=0.05, color=YELLOW)
    dot.move_to(paire.get_center())
    return VGroup(left, right, dot)


class PremiereDivisionReductionnelle(NotionScene):
    def construct(self):
        titre = scene_title("2.2 — La 1ère division de la méiose")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : qu'est-ce que la méiose ? ------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La méiose est une division cellulaire qui, à partir "
                    "d'une seule cellule mère diploïde (2n), produit quatre "
                    "cellules filles haploïdes (n) génétiquement "
                    "différentes. Elle comporte deux divisions successives, "
                    "précédées d'une seule réplication de l'ADN.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La méiose est une division cellulaire particulière qui, à "
                "partir d'une seule cellule mère diploïde, à deux n, produit "
                "quatre cellules filles haploïdes, à n, génétiquement "
                "différentes entre elles et différentes de la cellule mère. "
                "Elle comporte deux divisions successives, précédées d'une "
                "seule réplication de l'ADN. Chez l'être humain et les "
                "animaux, elle se déroule dans les gonades, au moment de la "
                "gamétogenèse ; chez les plantes à fleurs, dans les anthères "
                "des étamines et dans l'ovaire du pistil."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        interphase = Text(
            _wrap(
                "Avant la méiose, la cellule réplique son ADN en interphase : "
                "chaque chromosome passe de simple à dédoublé. Point capital : "
                "il n'y aura AUCUNE autre réplication entre les deux "
                "divisions. Une seule réplication, mais deux divisions : "
                "voilà ce qui permet de diviser le nombre de chromosomes par "
                "deux.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        interphase.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant que la méiose ne commence, la cellule traverse une "
                "interphase pendant laquelle elle réplique son ADN : chaque "
                "chromosome passe de l'état simple à l'état dédoublé. Point "
                "capital : il n'y aura aucune autre réplication entre les "
                "deux divisions de la méiose. C'est précisément ce qui "
                "permet de diviser le nombre de chromosomes par deux : une "
                "seule réplication, mais deux divisions."
            )
        ) as tracker:
            self.play(FadeIn(interphase))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interphase))

        # --- Animation du raisonnement : les 4 phases de la division I ------
        sous_titre = Text(
            "1ère division = division RÉDUCTIONNELLE (2n → n)",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        sous_titre.next_to(titre, DOWN, buff=0.45)
        self.play(FadeIn(sous_titre))

        # Cellule mère 2n=4 : une paire longue (bleu/bordeaux), une paire courte.
        cellule = Ellipse(width=4.4, height=3.0, color=WHITE, stroke_width=2)
        cellule.next_to(sous_titre, DOWN, buff=0.4)

        # --- Prophase I : bivalents formés, dispersés ------------------------
        long_pat = _chr(BLUE, height=1.3)
        long_mat = _chr(MAROON, height=1.3)
        biv_long = VGroup(long_pat, long_mat).arrange(RIGHT, buff=0.12)
        court_pat = _chr(BLUE, height=0.75)
        court_mat = _chr(MAROON, height=0.75)
        biv_court = VGroup(court_pat, court_mat).arrange(RIGHT, buff=0.12)

        biv_long.move_to(cellule.get_center() + LEFT * 0.9 + UP * 0.3)
        biv_court.move_to(cellule.get_center() + RIGHT * 0.9 + DOWN * 0.4)
        label_p1 = Text("Prophase I : bivalents (appariement)", font_size=20, color=WHITE)
        label_p1.next_to(cellule, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Prophase I. Les chromosomes, déjà dédoublés, se condensent et "
                "deviennent visibles. Puis se produit l'événement capital de "
                "toute la méiose : les chromosomes homologues s'apparient "
                "intimement, deux à deux, pour former des bivalents - ici, en "
                "bleu les chromosomes d'origine paternelle, en bordeaux ceux "
                "d'origine maternelle. Des enjambements peuvent s'y produire. "
                "Enfin, la membrane nucléaire disparaît et le fuseau se met en "
                "place."
            )
        ) as tracker:
            self.play(FadeIn(cellule))
            self.play(FadeIn(biv_long), FadeIn(biv_court))
            self.play(FadeIn(label_p1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_p1))

        # --- Métaphase I : alignement sur le plan équatorial -----------------
        plan_eq = Line(cellule.get_left() + RIGHT * 0.15, cellule.get_right() + LEFT * 0.15, color=YELLOW)
        self.play(
            biv_long.animate.move_to(cellule.get_center() + LEFT * 1.0),
            biv_court.animate.move_to(cellule.get_center() + RIGHT * 1.0),
            FadeIn(plan_eq),
        )
        label_m1 = Text("Métaphase I : alignement au hasard sur le plan équatorial", font_size=18, color=WHITE)
        label_m1.next_to(cellule, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Métaphase I. Les bivalents se rangent sur le plan équatorial "
                "de la cellule, à égale distance des deux pôles. Détail "
                "décisif : l'orientation de chaque bivalent est le fruit du "
                "hasard, et cela indépendamment des autres paires - c'est le "
                "premier mécanisme du brassage génétique, que nous détaillerons "
                "plus loin."
            )
        ) as tracker:
            self.play(FadeIn(label_m1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_m1), FadeOut(plan_eq))

        # --- Anaphase I : séparation des HOMOLOGUES (centromères intacts) ---
        label_a1 = Text(
            "Anaphase I : les HOMOLOGUES se séparent\n(centromères intacts, chromosomes encore dédoublés)",
            font_size=17,
            color=WHITE,
        )
        label_a1.next_to(cellule, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Anaphase I. Les deux homologues de chaque paire se séparent "
                "et migrent vers les pôles opposés, tirés par les filaments "
                "du fuseau. Point essentiel : les centromères ne se scindent "
                "pas. Chaque chromosome qui migre est donc encore dédoublé, "
                "formé de deux chromatides sœurs."
            )
        ) as tracker:
            self.play(
                long_pat.animate.shift(UP * 1.1),
                court_pat.animate.shift(UP * 1.1),
                long_mat.animate.shift(DOWN * 1.1),
                court_mat.animate.shift(DOWN * 1.1),
            )
            self.play(FadeIn(label_a1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_a1))

        # --- Télophase I : deux cellules filles haploïdes ---------------------
        cellule_haut = Ellipse(width=3.0, height=1.3, color=WHITE, stroke_width=2)
        cellule_bas = Ellipse(width=3.0, height=1.3, color=WHITE, stroke_width=2)
        cellule_haut.move_to(cellule.get_center() + UP * 0.85)
        cellule_bas.move_to(cellule.get_center() + DOWN * 0.85)

        label_t1 = Text(
            "Télophase I : 2 cellules filles, déjà n\n(chromosomes encore dédoublés)",
            font_size=18,
            color=WHITE,
        )

        with self.voiceover(
            text=(
                "Télophase I. Les chromosomes arrivent aux pôles, la cellule "
                "se creuse puis se partage en deux cellules filles. Chaque "
                "cellule fille ne contient plus qu'un seul homologue de "
                "chaque paire : elle est déjà haploïde, à n, même si ses "
                "chromosomes sont encore dédoublés."
            )
        ) as tracker:
            self.play(FadeOut(cellule), FadeIn(cellule_haut), FadeIn(cellule_bas))
            self.play(
                VGroup(long_pat, court_pat).animate.scale(0.55).move_to(cellule_haut.get_center()),
                VGroup(long_mat, court_mat).animate.scale(0.55).move_to(cellule_bas.get_center()),
            )
            label_t1.next_to(cellule_bas, DOWN, buff=0.3)
            self.play(FadeIn(label_t1))
            self.wait(tracker.get_remaining_duration())

        schema_complet = VGroup(
            cellule_haut, cellule_bas, long_pat, long_mat, court_pat, court_mat, label_t1
        )
        self.play(FadeOut(schema_complet), FadeOut(sous_titre))

        # --- Exemple traité : bilan de la 1ère division ------------------------
        bilan = MathTex(
            r"2n = 4 \;\text{(mère)} \;\longrightarrow\; 2 \text{ cellules à } n = 2",
            font_size=30,
            color=WHITE,
        )
        bilan_texte = Text(
            _wrap(
                "Chaque cellule à n=2 possède encore des chromosomes "
                "dédoublés : la réduction porte sur le nombre de "
                "chromosomes (donc de centromères), pas encore sur le "
                "nombre de chromatides.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        bloc_bilan = VGroup(bilan, bilan_texte).arrange(DOWN, buff=0.4)
        bloc_bilan.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Faisons le bilan sur notre exemple : une cellule mère à deux "
                "n égale quatre donne, après cette première division, deux "
                "cellules à n égale deux. Chaque cellule possède encore des "
                "chromosomes dédoublés : la réduction porte sur le nombre de "
                "chromosomes, donc de centromères, pas encore sur le nombre "
                "de chromatides."
            )
        ) as tracker:
            self.play(Write(bilan))
            self.play(FadeIn(bilan_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_bilan))

        # --- À retenir ----------------------------------------------------------
        essentiel = _bullets(
            [
                "Ordre des étapes : prophase I, métaphase I, anaphase I, "
                "télophase I.",
                "Prophase I : appariement des homologues en bivalents "
                "(possibilité d'enjambements).",
                "Anaphase I : séparation des homologues, centromères "
                "intacts -> c'est la division réductionnelle (2n vers n).",
            ],
            width=54,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        essentiel.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'ordre des étapes : prophase I, métaphase I, "
                "anaphase I, télophase I. En prophase I, les homologues "
                "s'apparient en bivalents, avec de possibles enjambements. En "
                "anaphase I, ce sont les homologues qui se séparent, avec des "
                "centromères intacts : c'est cette étape qui réalise la "
                "division réductionnelle, de deux n vers n."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(essentiel))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas ce qui se sépare en anaphase I : ce sont "
                    "les chromosomes HOMOLOGUES (centromères intacts, "
                    "chromosomes encore dédoublés) - et non les chromatides "
                    "sœurs, qui ne se sépareront qu'en anaphase II (scène "
                    "suivante).",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre ce qui se sépare en anaphase "
                "un : ce sont les chromosomes homologues, avec des "
                "centromères qui restent intacts, et des chromosomes encore "
                "dédoublés - et non les chromatides sœurs, qui, elles, ne se "
                "sépareront qu'en anaphase deux, dans la deuxième division "
                "que nous verrons dans la prochaine scène."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
