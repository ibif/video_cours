"""
scenes/SVT_Gametogenese_07.py — Chapitre 3 (1ereD, SVT), scène 07.

§ 3.5 L'ovogenèse : formation de l'ovule — les trois temps (vie fœtale,
chaque cycle, fécondation seulement), propriété du rendement, la
folliculogenèse et l'ovulation, exemple du calcul du nombre d'ovulations
et de l'atrésie folliculaire, structure de l'ovule.
Source : 1ereD/SVT.pdf, pages 40-43.
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
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class Ovogenese(NotionScene):
    def construct(self):
        titre = scene_title("3.5 — L'ovogenèse")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : définition ---------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'ovogenèse transforme, dans les ovaires, les "
                    "ovogonies (cellules diploïdes) en ovules (cellules "
                    "haploïdes). Contrairement à la spermatogenèse, elle "
                    "est discontinue : elle commence avant la naissance, "
                    "s'interrompt, reprend à la puberté et cesse à la "
                    "ménopause.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'ovogenèse est l'ensemble des phénomènes qui, dans les "
                "ovaires, transforment les ovogonies, cellules diploïdes, "
                "en ovules, cellules haploïdes. Contrairement à la "
                "spermatogenèse, elle est discontinue : elle commence avant "
                "la naissance, s'interrompt, reprend à la puberté et cesse "
                "à la ménopause."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les trois temps -------------------------------------
        entete_t1 = Text("1er temps — avant la naissance", font_size=23, color=YELLOW, weight="BOLD")
        entete_t1.next_to(titre, DOWN, buff=0.45)

        temps1 = _bullets(
            [
                "Les ovogonies (2n=46) se multiplient par mitoses puis "
                "grossissent : ovocytes du 1er ordre (2n=46).",
                "Vers le 5e mois fœtal : 6 à 7 millions d'ovocytes ; "
                "à la naissance : environ 2 millions ; à la puberté : "
                "environ 400 000.",
                "Tous ont commencé la méiose I, mais elle est bloquée en "
                "prophase I, parfois pendant des décennies.",
            ],
            font_size=20,
            width=50,
        )
        temps1.next_to(entete_t1, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'ovogenèse se déroule en trois temps. Premier temps : "
                "avant la naissance, pendant la vie fœtale. Dans les "
                "ovaires du fœtus de sexe féminin, les ovogonies, à deux n "
                "égale quarante-six, se multiplient par mitoses puis "
                "grossissent : elles deviennent des ovocytes du premier "
                "ordre, toujours à deux n égale quarante-six. Ce stock se "
                "constitue une fois pour toutes : vers le cinquième mois de "
                "la vie fœtale, l'ovaire contient six à sept millions "
                "d'ovocytes ; beaucoup dégénèrent ensuite, si bien qu'à la "
                "naissance il en reste environ deux millions, et à la "
                "puberté environ quatre cent mille. Tous ces ovocytes du "
                "premier ordre ont commencé la méiose un, mais elle est "
                "bloquée en prophase un, parfois pendant des décennies."
            )
        ) as tracker:
            self.play(FadeIn(entete_t1))
            self.play(FadeIn(temps1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_t1), FadeOut(temps1))

        entete_t2 = Text("2e temps — à chaque cycle (puberté → ménopause)", font_size=21, color=YELLOW, weight="BOLD")
        entete_t2.next_to(titre, DOWN, buff=0.45)

        temps2 = _bullets(
            [
                "L'ovocyte I achève enfin la méiose I juste avant "
                "l'ovulation — division inégale.",
                "Résultat : un ovocyte II (n=23, presque tout le "
                "cytoplasme) + 1er globule polaire (n=23, dégénère).",
                "La méiose II démarre aussitôt mais se bloque en "
                "métaphase II : c'est l'ovocyte II, ainsi bloqué, qui "
                "est expulsé à l'ovulation.",
            ],
            font_size=20,
            width=50,
        )
        temps2.next_to(entete_t2, DOWN, buff=0.35)

        # Petit schéma : division inégale
        gros = Circle(radius=0.5, color=ORANGE, fill_opacity=0.85)
        petit = Circle(radius=0.16, color=RED, fill_opacity=0.85)
        petit.next_to(gros, RIGHT, buff=0.15).align_to(gros, UP)
        division = VGroup(gros, petit)
        division.next_to(temps2, DOWN, buff=0.4)
        label_div = Text("Division inégale : ovocyte II (gros) + 1er globule polaire (petit)", font_size=16, color=WHITE)
        label_div.next_to(division, DOWN, buff=0.2)

        with self.voiceover(
            text=(
                "Deuxième temps : à chaque cycle, de la puberté à la "
                "ménopause. À partir de la puberté, vers douze ou treize "
                "ans, à chaque cycle menstruel, environ vingt-huit jours, "
                "quelques follicules se développent, mais en général un "
                "seul devient mûr. Dans ce follicule, l'ovocyte du premier "
                "ordre achève enfin la méiose un, juste avant l'ovulation. "
                "Mais cette division est inégale : elle produit une très "
                "grosse cellule, l'ovocyte du second ordre, qui garde "
                "presque tout le cytoplasme, et une minuscule cellule, le "
                "premier globule polaire, destinée à dégénérer. La méiose "
                "deux commence aussitôt mais se bloque en métaphase deux : "
                "c'est l'ovocyte du second ordre, ainsi bloqué, qui est "
                "expulsé au moment de l'ovulation."
            )
        ) as tracker:
            self.play(FadeIn(entete_t2))
            self.play(FadeIn(temps2))
            self.play(FadeIn(division), FadeIn(label_div))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_t2), FadeOut(temps2), FadeOut(division), FadeOut(label_div))

        entete_t3 = Text("3e temps — seulement s'il y a fécondation", font_size=21, color=YELLOW, weight="BOLD")
        entete_t3.next_to(titre, DOWN, buff=0.45)

        temps3 = _bullets(
            [
                "Si un spermatozoïde pénètre l'ovocyte II, la méiose II "
                "s'achève : elle donne l'ovule définitif (ovotide, n=23) "
                "et un 2e globule polaire.",
                "Sans fécondation, la méiose II ne s'achève jamais : "
                "l'ovocyte est éliminé avec les règles.",
            ],
            font_size=21,
            width=50,
        )
        temps3.next_to(entete_t3, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième temps, uniquement s'il y a fécondation. Si un "
                "spermatozoïde pénètre l'ovocyte du second ordre, la méiose "
                "deux s'achève enfin : elle donne l'ovule définitif, ou "
                "ovotide, à n égale vingt-trois, et un deuxième globule "
                "polaire. Sans fécondation, la méiose deux ne s'achève "
                "jamais et l'ovocyte est éliminé avec les règles."
            )
        ) as tracker:
            self.play(FadeIn(entete_t3))
            self.play(FadeIn(temps3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_t3), FadeOut(temps3))

        # --- Propriété : rendement de l'ovogenèse -------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Un ovocyte du premier ordre ne donne qu'un seul "
                    "gamète fonctionnel (l'ovule), les autres produits de "
                    "la méiose étant des globules polaires qui dégénèrent. "
                    "On retient souvent : « un ovocyte du 1er ordre donne "
                    "un ovule et trois globules polaires ».",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons cette propriété essentielle : un ovocyte du "
                "premier ordre ne donne qu'un seul gamète fonctionnel, "
                "l'ovule, les autres produits de la méiose étant des "
                "globules polaires qui dégénèrent. On retient souvent la "
                "formule : un ovocyte du premier ordre donne un ovule et "
                "trois globules polaires, le premier globule polaire "
                "pouvant lui-même se diviser en deux."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Raisonnement : folliculogenèse et ovulation -------------------------
        entete_follicule = Text("La folliculogenèse et l'ovulation", font_size=23, color=YELLOW, weight="BOLD")
        entete_follicule.next_to(titre, DOWN, buff=0.45)

        f1 = Circle(radius=0.22, color=BLUE, fill_opacity=0.7)
        f2 = Circle(radius=0.32, color=GREEN, fill_opacity=0.75)
        f3 = Circle(radius=0.42, color=ORANGE, fill_opacity=0.8)
        f4 = Circle(radius=0.55, color=RED, fill_opacity=0.85)
        follicules = VGroup(f1, f2, f3, f4).arrange(RIGHT, buff=0.5)
        follicules.next_to(entete_follicule, DOWN, buff=0.6)

        fleches_foll = VGroup(
            *[
                Arrow(follicules[i].get_right(), follicules[i + 1].get_left(), buff=0.06, color=WHITE)
                for i in range(len(follicules) - 1)
            ]
        )

        noms_foll = VGroup(
            Text("primordial", font_size=15, color=WHITE),
            Text("primaire", font_size=15, color=WHITE),
            Text("secondaire", font_size=15, color=WHITE),
            Text("mûr (De Graaf)", font_size=15, color=WHITE),
        )
        for i, lbl in enumerate(noms_foll):
            lbl.next_to(follicules[i], DOWN, buff=0.2)

        schema_foll = VGroup(follicules, fleches_foll, noms_foll)

        with self.voiceover(
            text=(
                "Pendant que l'ovocyte progresse dans sa méiose, le "
                "follicule qui l'entoure se transforme : c'est la "
                "folliculogenèse. Le follicule primordial devient follicule "
                "primaire, puis follicule secondaire, quand une cavité "
                "remplie de liquide apparaît, et enfin follicule mûr, ou "
                "follicule de De Graaf, qui mesure jusqu'à deux "
                "centimètres et fait saillie à la surface de l'ovaire. Vers "
                "le quatorzième jour d'un cycle de vingt-huit jours, le "
                "follicule mûr se rompt : c'est l'ovulation. L'ovocyte du "
                "second ordre est capté par le pavillon de la trompe, où la "
                "fécondation pourra avoir lieu. Le reste du follicule se "
                "transforme en corps jaune, qui sécrète de la "
                "progestérone."
            )
        ) as tracker:
            self.play(FadeIn(entete_follicule))
            self.play(FadeIn(follicules), FadeIn(noms_foll))
            self.play(FadeIn(fleches_foll))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_follicule), FadeOut(schema_foll))

        # --- Exemple traité : nombre d'ovulations et atrésie ---------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Femme de 13 à 49 ans, 13 cycles/an, sans grossesse. "
                    "1) Vie génitale : 49-13=36 ans. 2) Cycles : "
                    "36×13=468. 3) Ovulations : 468 au maximum. Sur les "
                    "400 000 follicules de la puberté : 468/400000≈0,12 %. "
                    "L'écrasante majorité dégénère (atrésie folliculaire).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Évaluons le nombre d'ovulations dans la vie d'une femme "
                "dont les règles débutent à treize ans et qui atteint la "
                "ménopause à quarante-neuf ans, avec treize cycles par an "
                "et sans grossesse. Un : la durée de la vie génitale est de "
                "quarante-neuf moins treize, soit trente-six ans. Deux : le "
                "nombre de cycles est de trente-six fois treize, soit "
                "quatre cent soixante-huit cycles. Trois : en admettant une "
                "ovulation par cycle, quatre cent soixante-huit ovulations "
                "au maximum. Sur les quatre cent mille follicules présents "
                "à la puberté, moins de cinq cents aboutissent donc à une "
                "ovulation, soit environ zéro virgule douze pour cent. "
                "L'écrasante majorité des follicules dégénère au cours de "
                "la vie, un phénomène appelé atrésie folliculaire."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : structure de l'ovule -------------------------------------
        entete_ovule = Text("L'ovule, un gamète riche en réserves", font_size=23, color=YELLOW, weight="BOLD")
        entete_ovule.next_to(titre, DOWN, buff=0.45)

        vitellus = Circle(radius=0.7, color=ORANGE, fill_opacity=0.85)
        zone_pellucide = Circle(radius=0.85, color=YELLOW, fill_opacity=0.0, stroke_width=4)
        noyau_ovule = Dot(color=RED, radius=0.1)
        noyau_ovule.move_to(vitellus.get_center())
        ovule_schema = VGroup(zone_pellucide, vitellus, noyau_ovule)
        ovule_schema.next_to(entete_ovule, DOWN, buff=0.6).shift(LEFT * 2.8)

        label_zp = Text("Zone pellucide\n(enveloppe transparente)", font_size=15, color=YELLOW)
        label_zp.next_to(ovule_schema, RIGHT, buff=1.2).shift(UP * 0.5)
        arrow_zp = Arrow(label_zp.get_left(), zone_pellucide.get_right(), buff=0.08, color=WHITE)

        label_vitellus = Text("Vitellus : cytoplasme\nriche en réserves", font_size=15, color=WHITE)
        label_vitellus.next_to(ovule_schema, RIGHT, buff=1.2).shift(DOWN * 0.7)
        arrow_vitellus = Arrow(label_vitellus.get_left(), vitellus.get_bottom() + RIGHT * 0.3, buff=0.08, color=WHITE)

        schema_ovule_full = VGroup(ovule_schema, label_zp, arrow_zp, label_vitellus, arrow_vitellus)

        taille_txt = MathTex(r"\varnothing \approx 120\ \mu m", font_size=26, color=WHITE)
        taille_txt.next_to(schema_ovule_full, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'ovule est une des plus grosses cellules du corps humain, "
                "environ cent vingt micromètres de diamètre, soit un "
                "volume des milliers de fois supérieur à celui du "
                "spermatozoïde. Il est entouré d'une enveloppe épaisse et "
                "transparente, la zone pellucide, et son cytoplasme, "
                "appelé vitellus, est chargé de substances de réserve qui "
                "nourriront le tout premier stade de l'embryon. Son noyau, "
                "à n égale vingt-trois, n'achève sa maturation qu'à la "
                "fécondation. Contrairement au spermatozoïde, l'ovule est "
                "immobile : il est transporté par les mouvements de la "
                "trompe."
            )
        ) as tracker:
            self.play(FadeIn(entete_ovule))
            self.play(FadeIn(ovule_schema))
            self.play(FadeIn(label_zp), FadeIn(arrow_zp))
            self.play(FadeIn(label_vitellus), FadeIn(arrow_vitellus))
            self.play(Write(taille_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ovule), FadeOut(schema_ovule_full), FadeOut(taille_txt))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne dis jamais que l'ovaire libère directement un "
                    "« ovule » à l'ovulation : c'est un ovocyte du second "
                    "ordre, bloqué en métaphase II, qui est expulsé. "
                    "L'ovule véritable n'existe que si la fécondation a "
                    "lieu et achève la méiose II.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : ne dis jamais que l'ovaire libère "
                "directement un ovule à l'ovulation. Ce qui est expulsé est "
                "un ovocyte du second ordre, bloqué en métaphase deux. "
                "L'ovule véritable n'existe que si la fécondation a lieu et "
                "permet à la méiose deux de s'achever."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
