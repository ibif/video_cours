"""
scenes/SVT_Gametogenese_06.py — Chapitre 3 (1ereD, SVT), scène 06.

§ 3.4 La spermatogenèse : formation des spermatozoïdes — les 4 phases
(multiplication, accroissement, maturation, différenciation), exemple du
bélier (500 → 2000), structure du spermatozoïde, caractères généraux,
attention spermatide/spermatozoïde. Source : 1ereD/SVT.pdf, pages 38-40.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

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


class Spermatogenese(NotionScene):
    def construct(self):
        titre = scene_title("3.4 — La spermatogenèse")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : définition et 4 phases ----------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La spermatogenèse transforme, dans les tubes "
                    "séminifères, les spermatogonies (cellules diploïdes) "
                    "en spermatozoïdes (cellules haploïdes). Elle comporte "
                    "quatre phases : multiplication, accroissement, "
                    "maturation, différenciation.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La spermatogenèse est l'ensemble des phénomènes qui, dans "
                "les tubes séminifères des testicules, transforment les "
                "spermatogonies, cellules diploïdes, en spermatozoïdes, "
                "cellules haploïdes. Elle comporte quatre phases : la "
                "multiplication, l'accroissement, la maturation et la "
                "différenciation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : chaîne des 4 phases ---------------------------------
        etapes_labels = [
            ("Spermatogonie", "2n=46"),
            ("Spermatocyte I", "2n=46"),
            ("Spermatocytes II", "n=23"),
            ("Spermatides", "n=23"),
            ("Spermatozoïdes", "n=23"),
        ]
        cellules = VGroup()
        for nom, formule in etapes_labels:
            nom_txt = Text(nom, font_size=18, color=WHITE)
            formule_txt = MathTex(formule.replace("n=", "n = "), font_size=24, color=YELLOW)
            bloc = VGroup(nom_txt, formule_txt).arrange(DOWN, buff=0.15)
            cellules.add(bloc)
        cellules.arrange(RIGHT, buff=0.85)
        cellules.next_to(titre, DOWN, buff=1.3)
        cellules.scale(0.78)

        fleches = VGroup(
            *[
                Arrow(cellules[i].get_right(), cellules[i + 1].get_left(), buff=0.06, color=WHITE)
                for i in range(len(cellules) - 1)
            ]
        )

        phases_labels = VGroup(
            Text("Multiplication\n(mitoses)", font_size=14, color=BLUE),
            Text("Accroissement", font_size=14, color=GREEN),
            Text("Maturation\n(méiose I)", font_size=14, color=ORANGE),
            Text("Méiose II +\ndifférenciation", font_size=14, color=RED),
        )
        for i, lbl in enumerate(phases_labels):
            lbl.next_to(fleches[i], UP, buff=0.12)

        with self.voiceover(
            text=(
                "Phase un, la multiplication : les spermatogonies, à deux "
                "n égale quarante-six, situées à la périphérie des tubes "
                "séminifères, se divisent par de nombreuses mitoses ; une "
                "partie reste en réserve, l'autre entre dans la phase "
                "suivante. Phase deux, l'accroissement : les spermatogonies "
                "grossissent et deviennent des spermatocytes du premier "
                "ordre, toujours à deux n égale quarante-six ; à la fin de "
                "cette phase, l'ADN de chaque chromosome est répliqué. "
                "Phase trois, la maturation : c'est la méiose proprement "
                "dite. Chaque spermatocyte du premier ordre subit la méiose "
                "un et donne deux spermatocytes du second ordre, à n égale "
                "vingt-trois, chromosomes à deux chromatides ; chaque "
                "spermatocyte du second ordre subit la méiose deux et donne "
                "deux spermatides, à n égale vingt-trois, chromosomes à une "
                "chromatide. Au total, un spermatocyte du premier ordre "
                "fournit quatre spermatides."
            )
        ) as tracker:
            self.play(FadeIn(cellules))
            self.play(FadeIn(fleches), FadeIn(phases_labels))
            self.wait(tracker.get_remaining_duration())

        note_diff = Text(
            _wrap(
                "Phase 4 — la différenciation (spermiogenèse) : les "
                "spermatides, rondes et immobiles, se transforment "
                "totalement (noyau condensé, acrosome, mitochondries en "
                "collerette, flagelle) pour devenir des spermatozoïdes "
                "mobiles, sans changer la formule chromosomique.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        note_diff.next_to(cellules, DOWN, buff=1.1)

        with self.voiceover(
            text=(
                "Phase quatre, la différenciation, ou spermiogenèse : les "
                "spermatides, petites cellules rondes et immobiles, se "
                "transforment totalement. Le noyau se condense, un "
                "acrosome se forme à l'avant, les mitochondries se "
                "rassemblent en collerette, un long flagelle apparaît. La "
                "cellule devient un spermatozoïde, gamète mobile, à n égale "
                "vingt-trois chromosomes. Cette transformation ne change "
                "pas la formule chromosomique."
            )
        ) as tracker:
            self.play(FadeIn(note_diff))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cellules), FadeOut(fleches), FadeOut(phases_labels), FadeOut(note_diff))

        # --- Exemple traité : le bélier -----------------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "500 spermatocytes I entrent en maturation. 1) Méiose "
                    "I : 500×2=1000 spermatocytes II. 2) Méiose II : "
                    "1000×2=2000 spermatides. 3) Différenciation : 2000 "
                    "spermatides → 2000 spermatozoïdes. Chaque "
                    "spermatocyte I donne 4 gamètes : rendement de 100 %.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans un tubule séminifère de bélier, on compte cinq cents "
                "spermatocytes du premier ordre qui entrent en maturation. "
                "Combien de spermatozoïdes peuvent-ils fournir ? Un : la "
                "méiose un donne cinq cents fois deux, soit mille "
                "spermatocytes du second ordre. Deux : la méiose deux donne "
                "mille fois deux, soit deux mille spermatides. Trois : la "
                "différenciation transforme les deux mille spermatides en "
                "deux mille spermatozoïdes. Chaque spermatocyte du premier "
                "ordre donne donc quatre gamètes : le rendement de la "
                "spermatogenèse est de cent pour cent, aucune cellule n'est "
                "perdue."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : structure du spermatozoïde -----------------------------
        entete_struct = Text("Le spermatozoïde, un gamète mobile", font_size=24, color=YELLOW, weight="BOLD")
        entete_struct.next_to(titre, DOWN, buff=0.45)

        tete = Circle(radius=0.35, color=RED, fill_opacity=0.85)
        acrosome = Ellipse(width=0.35, height=0.5, color=ORANGE, fill_opacity=0.85)
        acrosome.next_to(tete, LEFT, buff=-0.15)
        col = Line(tete.get_right(), tete.get_right() + RIGHT * 0.3, color=YELLOW, stroke_width=5)
        piece_int = Line(col.get_end(), col.get_end() + RIGHT * 0.6, color=GREEN, stroke_width=7)
        flagelle = Line(piece_int.get_end(), piece_int.get_end() + RIGHT * 2.2, color=BLUE, stroke_width=3)
        spermato = VGroup(tete, acrosome, col, piece_int, flagelle)
        spermato.next_to(entete_struct, DOWN, buff=0.55)

        label_tete = Text("Tête : noyau (n=23)\n+ acrosome (enzymes)", font_size=15, color=WHITE)
        label_tete.next_to(spermato, UP, buff=0.35).shift(LEFT * 2.4)
        arrow_tete = Arrow(label_tete.get_bottom(), tete.get_top(), buff=0.08, color=WHITE)

        label_piece = Text("Pièce intermédiaire :\nmitochondries (énergie)", font_size=15, color=WHITE)
        label_piece.next_to(spermato, DOWN, buff=0.35).shift(LEFT * 0.4)
        arrow_piece = Arrow(label_piece.get_top(), piece_int.get_center(), buff=0.08, color=WHITE)

        label_flagelle = Text("Flagelle : déplacement\n(1 à 4 mm/min)", font_size=15, color=WHITE)
        label_flagelle.next_to(spermato, UP, buff=0.35).shift(RIGHT * 2.2)
        arrow_flagelle = Arrow(label_flagelle.get_bottom(), flagelle.get_center(), buff=0.08, color=WHITE)

        schema_spermato = VGroup(
            spermato, label_tete, arrow_tete, label_piece, arrow_piece, label_flagelle, arrow_flagelle
        )

        with self.voiceover(
            text=(
                "Voyons maintenant la structure du spermatozoïde humain, "
                "cellule filiforme d'environ soixante micromètres. De "
                "l'avant vers l'arrière : la tête, qui contient le noyau à "
                "vingt-trois chromosomes, coiffée par l'acrosome, une "
                "vésicule d'enzymes capables de traverser les enveloppes de "
                "l'ovule ; le col, court segment contenant les centrioles, "
                "nécessaires à la première division de la cellule œuf ; la "
                "pièce intermédiaire, enroulée de mitochondries qui "
                "fabriquent l'énergie de la propulsion ; et le flagelle, "
                "long filament mobile dont les battements propulsent le "
                "spermatozoïde à une vitesse de un à quatre millimètres par "
                "minute."
            )
        ) as tracker:
            self.play(FadeIn(entete_struct))
            self.play(FadeIn(spermato))
            self.play(FadeIn(label_tete), FadeIn(arrow_tete))
            self.play(FadeIn(label_piece), FadeIn(arrow_piece))
            self.play(FadeIn(label_flagelle), FadeIn(arrow_flagelle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_struct), FadeOut(schema_spermato))

        # --- À retenir : caractères généraux -------------------------------------
        entete_carac = Text("Caractères généraux de la spermatogenèse", font_size=23, color=YELLOW, weight="BOLD")
        entete_carac.next_to(titre, DOWN, buff=0.45)

        caracteres = _bullets(
            [
                "Continue : de la puberté (12-13 ans) jusqu'à un âge avancé, sans interruption.",
                "Rapide : cycle complet d'environ 70 jours, près d'un millier de spermatozoïdes/seconde.",
                "Rendement élevé : 4 spermatozoïdes fonctionnels par spermatocyte I.",
                "Thermosensible : exige environ 35°C, d'où la position des testicules dans les bourses.",
            ],
            font_size=21,
            width=52,
        )
        caracteres.next_to(entete_carac, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La spermatogenèse présente quatre traits remarquables. "
                "Elle est continue : à partir de la puberté, vers douze ou "
                "treize ans, elle se déroule sans interruption, jour et "
                "nuit, jusqu'à un âge avancé. Elle est rapide : un cycle "
                "complet dure environ soixante-dix jours, et l'homme "
                "produit près d'un millier de spermatozoïdes par seconde. "
                "Son rendement est élevé : chaque spermatocyte du premier "
                "ordre donne quatre spermatozoïdes fonctionnels. Et elle "
                "exige une température d'environ trente-cinq degrés, "
                "légèrement inférieure à celle du corps, ce qui explique la "
                "position des testicules dans les bourses."
            )
        ) as tracker:
            self.play(FadeIn(entete_carac))
            self.play(FadeIn(caracteres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_carac), FadeOut(caracteres))

        # --- Piège à éviter : spermatide ≠ spermatozoïde --------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La spermatide est une cellule ronde, immobile, "
                    "achevée génétiquement (n=23) mais non fonctionnelle : "
                    "elle ne peut ni nager ni féconder. Ce n'est qu'après "
                    "la différenciation qu'elle devient un spermatozoïde "
                    "mobile. Dans un schéma, ne place jamais le flagelle "
                    "sur une spermatide.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre spermatide et spermatozoïde. "
                "La spermatide est une cellule ronde, immobile, achevée "
                "génétiquement, à n égale vingt-trois, mais non "
                "fonctionnelle : elle ne peut ni nager ni féconder. Ce "
                "n'est qu'après la différenciation, la spermiogenèse, "
                "qu'elle devient un spermatozoïde mobile. Dans un schéma, "
                "ne place donc jamais de flagelle sur une spermatide."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
