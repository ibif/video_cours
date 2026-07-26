"""
scenes/SVT_EchangesCationiquesSol_11.py — Chapitre 9 (1ereC, SVT), scène 11.

Les engrais (définition, 3 types : simples, composés NPK, organiques), les
amendements et le chaulage (définitions, mécanisme du CaCO3, effets sur le
sol), piège du chaulage excessif, et Exemple résolu 3 (calcul de la masse
de chaux CaO à épandre par hectare). Source : 1ereC/SVT.pdf, pages
104-105.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, definition_box, exercise_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class EngraisAmendementsChaulage(NotionScene):
    def construct(self):
        titre = scene_title("9.10 — Engrais, amendements et chaulage")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : restituer ce que le sol a perdu ------------------------
        intro = Text(
            _wrap(
                "Le lessivage et les récoltes appauvrissent le sol. "
                "L'agriculteur dispose de plusieurs outils pour restituer "
                "ce qui a été perdu, ou même corriger l'acidité "
                "installée.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le lessivage et les récoltes successives appauvrissent "
                "le sol. Pour maintenir sa fertilité, l'agriculteur "
                "dispose de plusieurs outils : les engrais, les "
                "amendements, et le chaulage."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : les engrais et leurs 3 types --------------------
        def_engrais = definition_box(
            Text(
                _wrap(
                    "Un engrais est une substance qui apporte au sol un "
                    "ou plusieurs éléments nutritifs directement "
                    "assimilables par les plantes, afin d'augmenter les "
                    "rendements.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_engrais.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un engrais est une substance qui apporte au sol un ou "
                "plusieurs éléments nutritifs directement assimilables "
                "par les plantes, afin d'augmenter les rendements."
            )
        ) as tracker:
            self.play(FadeIn(def_engrais))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_engrais))

        types_engrais = property_box(
            _bullets(
                [
                    "Engrais simples : un seul élément majeur (urée ou "
                    "sulfate d'ammonium pour N ; superphosphate pour P ; "
                    "chlorure de potassium KCl pour K)",
                    "Engrais composés : plusieurs éléments (NPK 15-15-15, "
                    "très utilisé en Côte d'Ivoire sur cacaoyer et "
                    "palmier à huile)",
                    "Engrais organiques : fumier, compost, déjections de "
                    "volailles (apportent aussi de la matière organique, "
                    "qui entretient l'humus et donc la CEC)",
                ],
                font_size=18,
                width=56,
            ),
            box_width=12.2,
        )
        types_engrais.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On distingue trois types d'engrais. Les engrais "
                "simples, qui n'apportent qu'un seul élément majeur : "
                "urée ou sulfate d'ammonium pour l'azote, superphosphate "
                "pour le phosphore, chlorure de potassium pour le "
                "potassium. Les engrais composés, qui apportent plusieurs "
                "éléments à la fois, comme le fameux NPK 15-15-15, très "
                "utilisé en Côte d'Ivoire sur le cacaoyer et le palmier à "
                "huile. Et les engrais organiques, fumier, compost, "
                "déjections de volailles, qui apportent à la fois des "
                "éléments nutritifs et de la matière organique, "
                "entretenant l'humus et donc la CEC."
            )
        ) as tracker:
            self.play(FadeIn(types_engrais))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(types_engrais))

        # --- Amendements et chaulage -------------------------------------------
        def_amendement = definition_box(
            Text(
                _wrap(
                    "Un amendement est une substance ajoutée au sol pour "
                    "améliorer ses propriétés physiques ou chimiques "
                    "(structure, pH), sans viser directement la "
                    "nutrition de la plante.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_amendement.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un amendement, lui, est une substance ajoutée au sol "
                "pour améliorer ses propriétés physiques ou chimiques, "
                "sa structure, son pH, sans viser directement la "
                "nutrition de la plante."
            )
        ) as tracker:
            self.play(FadeIn(def_amendement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_amendement))

        def_chaulage = definition_box(
            Text(
                _wrap(
                    "Le chaulage est l'apport au sol d'amendements "
                    "calcaires ou basiques (chaux vive CaO, chaux "
                    "éteinte Ca(OH)2, carbonate de calcium CaCO3, "
                    "dolomie) afin de corriger l'acidité d'un sol, "
                    "c'est-à-dire d'élever son pH.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_chaulage.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le principal amendement utilisé est le chaulage : "
                "l'apport au sol d'amendements calcaires ou basiques, "
                "chaux vive, chaux éteinte, carbonate de calcium, ou "
                "dolomie, afin de corriger l'acidité d'un sol, "
                "c'est-à-dire d'élever son pH."
            )
        ) as tracker:
            self.play(FadeIn(def_chaulage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_chaulage))

        # Mécanisme du chaulage (CaCO3)
        meca_titre = Text("Mécanisme du chaulage (exemple du CaCO3)", font_size=21, color=YELLOW, weight="BOLD")
        meca_titre.next_to(titre, DOWN, buff=0.45)

        eq1 = MathTex(
            r"Ca^{2+} + 2\,H^+_{(adsorb\acute{e})} \;\longrightarrow\; Ca^{2+}_{(adsorb\acute{e})} + 2\,H^+",
            font_size=26,
            color=WHITE,
        )
        eq2 = MathTex(
            r"2\,H^+ + CO_3^{2-} \;\longrightarrow\; H_2O + CO_2",
            font_size=26,
            color=WHITE,
        )
        equations = VGroup(eq1, eq2).arrange(DOWN, buff=0.35)
        equations.next_to(meca_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voyons le mécanisme du chaulage, avec l'exemple du "
                "carbonate de calcium. D'abord, les ions calcium apportés "
                "se fixent sur le complexe en chassant les ions H+ : "
                "calcium deux plus plus deux H+ adsorbés donne calcium "
                "adsorbé plus deux H+. Ensuite, les ions H+ désorbés sont "
                "neutralisés dans la solution : deux H+ plus l'ion "
                "carbonate donne de l'eau plus du dioxyde de carbone."
            )
        ) as tracker:
            self.play(FadeIn(meca_titre))
            self.play(Write(eq1))
            self.play(Write(eq2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meca_titre), FadeOut(equations))

        effets = property_box(
            _bullets(
                [
                    "Élève le pH du sol vers la neutralité",
                    "Sature le complexe en calcium (augmentation de V)",
                    "Améliore la structure du sol (floculation de "
                    "l'argile, meilleure aération)",
                    "Réduit la toxicité de l'aluminium et du manganèse",
                    "Rend le phosphore à nouveau disponible",
                ],
                font_size=19,
                width=54,
            ),
            box_width=11.8,
        )
        effets.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le chaulage produit plusieurs effets bénéfiques : il "
                "élève le pH du sol vers la neutralité ; il sature le "
                "complexe en calcium, augmentant le taux de saturation V "
                "; il améliore la structure du sol, par floculation de "
                "l'argile et meilleure aération ; il réduit la toxicité "
                "de l'aluminium et du manganèse ; et il rend le "
                "phosphore à nouveau disponible pour les plantes."
            )
        ) as tracker:
            self.play(FadeIn(effets))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(effets))

        # --- Piège à éviter : chaulage excessif ---------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : un chaulage excessif peut rendre le "
                    "sol basique et bloquer le fer, le bore et le zinc. "
                    "Il faut chauler avec modération, en se basant sur "
                    "une analyse de sol.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mais attention à un piège fréquent : un chaulage "
                "excessif peut rendre le sol basique et bloquer à son "
                "tour le fer, le bore et le zinc. Il faut donc chauler "
                "avec modération, toujours en se basant sur une analyse "
                "de sol préalable."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- Exemple traité 3 : masse de chaux CaO à épandre --------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Exemple résolu 3 : il manque 4 cmol+ de Ca2+ par kg "
                    "de sol. Couche labourée d'un hectare : profondeur "
                    "20 cm, masse volumique 1,3 g/cm3. Quelle masse de "
                    "chaux CaO épandre par hectare ? (Ca = 40 g/mol ; "
                    "O = 16 g/mol)",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.0,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Terminons par un exemple résolu complet. Un agronome "
                "veut saturer en calcium un sol dont il manque quatre "
                "cmol plus de Ca2+ par kilogramme de sol. On considère la "
                "couche labourée d'un hectare : profondeur vingt "
                "centimètres, masse volumique du sol un virgule trois "
                "gramme par centimètre cube. Quelle masse de chaux CaO "
                "faut-il épandre par hectare ? Masses molaires : calcium "
                "quarante grammes par mole, oxygène seize grammes par "
                "mole."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        etape1 = MathTex(
            r"\text{Masse de sol/ha} = 10000\,m^2 \times 0{,}20\,m \times 1{,}3\ t/m^3",
            font_size=22,
            color=WHITE,
        )
        etape1b = MathTex(
            r"= 2600\ t = 2{,}6\times 10^{6}\ kg",
            font_size=22,
            color=WHITE,
        )
        etape2 = MathTex(
            r"4\ cmol^+/kg = 0{,}02\ mol\ Ca^{2+}/kg",
            font_size=22,
            color=WHITE,
        )
        etape2b = MathTex(
            r"0{,}02 \times 2{,}6\times10^{6} = 52000\ mol\ Ca^{2+}/ha",
            font_size=22,
            color=WHITE,
        )
        bloc1 = VGroup(etape1, etape1b, etape2, etape2b).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        bloc1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première étape : calculons la masse de sol par hectare. "
                "Le volume vaut dix mille mètres carrés fois zéro "
                "virgule vingt mètre, fois une masse volumique de un "
                "virgule trois, soit deux mille six cents tonnes, ou deux "
                "virgule six fois dix puissance six kilogrammes. Deuxième "
                "étape : la quantité de calcium à apporter. Quatre cmol "
                "plus par kilogramme équivaut à zéro virgule zéro deux "
                "mole de calcium par kilogramme, car une mole de calcium "
                "deux plus porte deux moles de charges positives. Soit, "
                "pour tout l'hectare, cinquante-deux mille moles de "
                "calcium."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape1b))
            self.play(Write(etape2))
            self.play(Write(etape2b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc1))

        etape3 = MathTex(
            r"M(CaO) = 40+16 = 56\ g/mol",
            font_size=24,
            color=WHITE,
        )
        etape3b = MathTex(
            r"52000 \times 56 = 2\,912\,000\ g \approx 2{,}9\ t\ de\ CaO/ha",
            font_size=24,
            color=WHITE,
        )
        bloc2 = VGroup(etape3, etape3b).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        bloc2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième étape : la masse de chaux CaO. Une mole de "
                "CaO, de masse molaire quarante plus seize, soit "
                "cinquante-six grammes, apporte une mole de calcium. Il "
                "faut donc cinquante-deux mille fois cinquante-six, soit "
                "deux millions neuf cent douze mille grammes, environ "
                "deux virgule neuf tonnes de chaux CaO par hectare."
            )
        ) as tracker:
            self.play(Write(etape3))
            self.play(Write(etape3b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc2))

        conclusion = corrige_box(
            Text(
                _wrap(
                    "Conclusion : il faut épandre environ 2,9 tonnes de "
                    "chaux CaO par hectare pour combler le déficit de "
                    "4 cmol+ de Ca2+ par kg sur la couche labourée.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Conclusion : il faut épandre environ deux virgule neuf "
                "tonnes de chaux CaO par hectare, pour combler le "
                "déficit de quatre cmol plus de calcium par kilogramme "
                "sur toute la couche labourée."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(conclusion))
