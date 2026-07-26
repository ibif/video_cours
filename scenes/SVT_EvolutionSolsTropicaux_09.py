"""
scenes/SVT_EvolutionSolsTropicaux_09.py — Chapitre 9 (1ereD, SVT), scène 09.

§ 9.7 La dégradation et la conservation des sols tropicaux — définition
dégradation/érosion, causes et conséquences, propriété des techniques de
conservation, exemple de la perte de terre de M. Konan, méthode pour
rédiger une étude de cas en quatre temps. Source : 1ereD/SVT.pdf, pages
126-129.
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
from shapes.boxes import definition_box, example_box, method_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class DegradationEtConservationDesSols(NotionScene):
    def construct(self):
        titre = scene_title("9.7 — Dégradation et conservation des sols")
        titre.scale(0.65)
        titre.to_edge(UP)

        _bas_visible = -config.frame_height / 2 + 0.3

        # --- Énoncé : définitions dégradation / érosion -----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La dégradation : ensemble des processus qui diminuent "
                    "la qualité et la fertilité d'un sol. L'érosion : la "
                    "forme la plus spectaculaire, enlèvement et transport "
                    "des particules par l'eau (hydrique), le vent "
                    "(éolienne) ou la gravité.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La dégradation est l'ensemble des processus qui diminuent "
                "la qualité et la fertilité d'un sol. L'érosion en est la "
                "forme la plus spectaculaire : l'enlèvement et le transport "
                "des particules par l'eau, on parle d'érosion hydrique, par "
                "le vent, l'érosion éolienne, ou par la gravité."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : causes et conséquences --------------
        entete_causes = Text("Causes et conséquences de la dégradation", font_size=22, color=YELLOW, weight="BOLD")
        entete_causes.next_to(titre, DOWN, buff=0.4)

        causes_conseq = _bullets(
            [
                "Érosion hydrique : ruissellement en nappe → rigoles → ravines (pistes latéritiques).",
                "Érosion éolienne : Nord, saison sèche, sol nu balayé par l'harmattan.",
                "Causes : déforestation, défriche-brûlis, feux tardifs, surpâturage, culture dans le sens de la pente.",
                "Conséquences : chute des rendements, ensablement des cours d'eau, inondations, insécurité alimentaire.",
            ],
            font_size=19,
            width=54,
        )
        causes_conseq.next_to(entete_causes, DOWN, buff=0.35)

        _hauteur_dispo = causes_conseq.get_top()[1] - _bas_visible
        if causes_conseq.height > _hauteur_dispo:
            causes_conseq.scale(_hauteur_dispo / causes_conseq.height, about_point=causes_conseq.get_top())

        with self.voiceover(
            text=(
                "L'érosion hydrique commence par un simple ruissellement en "
                "nappe qui décolle la couche superficielle, puis se "
                "concentre en rigoles, puis en ravines profondes, "
                "spectaculaires le long des pistes latéritiques après la "
                "saison des pluies. L'érosion éolienne sévit surtout dans "
                "l'extrême Nord en saison sèche, quand le sol nu est balayé "
                "par l'harmattan. Les causes principales sont la "
                "déforestation, la défriche-brûlis, les feux de brousse "
                "tardifs, le surpâturage, et les cultures en rangs dans le "
                "sens de la pente. Les conséquences sont lourdes : chute "
                "des rendements, ensablement des cours d'eau et des "
                "barrages, inondations, recul de la forêt, et au bout du "
                "compte, insécurité alimentaire."
            )
        ) as tracker:
            self.play(FadeIn(entete_causes))
            self.play(FadeIn(causes_conseq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_causes), FadeOut(causes_conseq))

        # --- Propriété : techniques de conservation ---------------------------
        conservation = property_box(
            Text(
                _wrap(
                    "Trois principes : couvrir le sol, ralentir l'eau, "
                    "restituer la matière. Techniques mécaniques : labour "
                    "et semis en courbes de niveau, bandes enherbées "
                    "(vétiver), terrasses, cordons pierreux. Techniques "
                    "biologiques : couverts végétaux, agroforesterie, "
                    "rotations avec légumineuses, jachère améliorée. "
                    "Amendements : compost, fumier, chaulage. "
                    "Organisation : lutte contre les feux, reboisement, "
                    "formation des producteurs.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=12.2,
        )
        conservation.next_to(titre, DOWN, buff=0.4)

        _hauteur_dispo2 = conservation.get_top()[1] - _bas_visible
        if conservation.height > _hauteur_dispo2:
            conservation.scale(_hauteur_dispo2 / conservation.height, about_point=conservation.get_top())

        with self.voiceover(
            text=(
                "Face à cela, trois principes guident la conservation des "
                "sols : couvrir le sol pour le protéger de l'impact des "
                "gouttes de pluie et du soleil, ralentir l'eau pour "
                "l'obliger à s'infiltrer plutôt que de ruisseler, et "
                "restituer la matière pour rendre au sol ce que les "
                "récoltes lui ont pris. Les techniques mécaniques : labour "
                "et semis suivant les courbes de niveau, bandes enherbées "
                "de vétiver, terrasses et cordons pierreux sur les pentes "
                "fortes. Les techniques biologiques et agronomiques : "
                "couverts végétaux et paillage, agroforesterie comme le "
                "cacao sous ombrage, rotations avec des légumineuses telles "
                "que l'arachide, le niébé ou le soja, jachère améliorée. "
                "Les amendements : matière organique, fumier, compost, "
                "engrais minéraux raisonnés, chaulage. Et des mesures "
                "d'organisation : lutte contre les feux de brousse, "
                "reboisement, planification, formation des producteurs."
            )
        ) as tracker:
            self.play(FadeIn(conservation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conservation))

        # --- Exemple traité : perte de terre de M. Konan -----------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Champ de manioc de M. Konan, 6 hectares sur une pente. "
                    "Perte par érosion : 30 t/ha/an. Densité apparente : "
                    "1,5. Épaisseur perdue par an ? Sur 10 ans ?",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple traité : le champ de manioc de monsieur Konan "
                "s'étend sur six hectares en pente, avec une perte par "
                "érosion de trente tonnes par hectare et par an, et une "
                "densité apparente du sol de un virgule cinq, soit mille "
                "cinq cents kilogrammes par mètre cube. Quelle épaisseur de "
                "sol perd-il chaque année, et sur dix ans ?"
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        calcul = MathTex(
            r"30 \times 6 = 180\,000 \text{ kg} \;\rightarrow\; \dfrac{180\,000}{1500} = 120\ m^3",
            font_size=24,
            color=WHITE,
        )
        calcul2 = MathTex(
            r"\dfrac{120}{60\,000} = 0{,}002\ m = 2\ mm/an \;\rightarrow\; 2 \times 10 = 20\ mm = 2\ cm \text{ en 10 ans}",
            font_size=22,
            color=YELLOW,
        )
        calculs = VGroup(calcul, calcul2).arrange(DOWN, buff=0.35)
        calculs.next_to(titre, DOWN, buff=0.7)

        _hauteur_dispo3 = calculs.get_top()[1] - _bas_visible
        if calculs.height > _hauteur_dispo3:
            calculs.scale(_hauteur_dispo3 / calculs.height, about_point=calculs.get_top())

        with self.voiceover(
            text=(
                "Étape un : la masse perdue par an vaut trente fois six, "
                "soit cent quatre-vingts tonnes, c'est-à-dire cent "
                "quatre-vingt mille kilogrammes ; le volume correspondant "
                "vaut cent quatre-vingt mille divisé par mille cinq cents, "
                "soit cent vingt mètres cubes. Étape deux : la parcelle "
                "fait six hectares, soit soixante mille mètres carrés ; "
                "l'épaisseur perdue vaut donc cent vingt divisé par "
                "soixante mille, soit zéro virgule zéro zéro deux mètre, "
                "c'est-à-dire deux millimètres par an. Étape trois : sur "
                "dix ans, cela représente vingt millimètres, soit deux "
                "centimètres. Or la nature met des siècles à fabriquer deux "
                "centimètres de sol : la perte est considérable."
            )
        ) as tracker:
            self.play(Write(calcul))
            self.play(Write(calcul2))
            self.wait(tracker.get_remaining_duration())

        conseil = Text(
            _wrap(
                "M. Konan doit planter des bandes de vétiver suivant les "
                "courbes de niveau et pailler ses rangs de manioc.",
                width=54,
            ),
            font_size=20,
            color=WHITE,
        )
        conseil.next_to(calculs, DOWN, buff=0.35)
        self.play(FadeIn(conseil))
        self.wait(1.5)

        self.play(FadeOut(calculs), FadeOut(conseil))

        # --- À retenir : méthode pour rédiger une étude de cas -----------------
        methode = method_box(
            _bullets(
                [
                    "Situer : localiser, décrire le contexte (climat, relief, sol, activités).",
                    "Décrire les faits observés (rigoles, couleurs, rendements).",
                    "Expliquer en reliant les faits aux processus du cours (lessivage, ferralitisation, érosion).",
                    "Proposer des solutions réalistes (court terme : couverture ; long terme : agroforesterie, fumure).",
                ],
                font_size=19,
                width=52,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Méthode pour rédiger une étude de cas, en quatre temps. "
                "Un, situer : localiser et décrire le contexte, climat, "
                "relief, sol, activités humaines. Deux, décrire les faits "
                "observés : rigoles, couleurs, rendements. Trois, "
                "expliquer, en reliant ces faits aux processus du cours, "
                "lessivage, ferralitisation, érosion. Quatre, proposer des "
                "solutions réalistes : à court terme, couvrir le sol et "
                "installer des bandes enherbées ; à long terme, "
                "agroforesterie, fumure, organisation du territoire."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
