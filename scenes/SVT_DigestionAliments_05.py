"""
scenes/SVT_DigestionAliments_05.py — Chapitre 12 (1ereD, SVT), scène 05.

§ 12.3 Les transformations mécaniques des aliments : mastication,
insalivation, bol alimentaire, déglutition, péristaltisme, brassage
gastrique (chyme), mouvements de l'intestin grêle (chyle), gros intestin
(fèces), vocabulaire, méthode « pourquoi bien mastiquer ».
Source : 1ereD/SVT.pdf, pages 158-159.
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
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LesTransformationsMecaniques(NotionScene):
    def construct(self):
        titre = scene_title("12.3 — Les transformations mécaniques")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : dans la bouche, mastication et insalivation -----------
        intro = Text(
            _wrap(
                "Les actions mécaniques préparent et accompagnent l'action "
                "chimique tout au long du tube digestif.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les actions mécaniques préparent et accompagnent l'action "
                "chimique tout au long du tube digestif. Suivons-les, "
                "organe après organe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : bouche → pharynx/œsophage ----------
        entete1 = Text("Dans la bouche", font_size=25, color=YELLOW, weight="BOLD")
        entete1.next_to(titre, DOWN, buff=0.45)

        bouche_txt = _bullets(
            [
                "Mastication : incisives coupent, canines déchirent, prémolaires/molaires broient.",
                "Insalivation : la langue mélange les fragments à la salive.",
                "Il se forme une pâte souple : le bol alimentaire.",
            ],
            font_size=21,
            width=52,
        )
        bouche_txt.next_to(entete1, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans la bouche, les dents réalisent la mastication : les "
                "incisives coupent, les canines déchirent, les prémolaires "
                "et molaires broient. La langue mélange les fragments à la "
                "salive : c'est l'insalivation. Il se forme une pâte "
                "souple appelée bol alimentaire."
            )
        ) as tracker:
            self.play(FadeIn(entete1))
            self.play(FadeIn(bouche_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete1), FadeOut(bouche_txt))

        entete2 = Text("Déglutition et péristaltisme", font_size=25, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.45)

        degl_txt = _bullets(
            [
                "Déglutition : réflexe qui fait passer le bol de la bouche au pharynx puis à l'œsophage.",
                "L'épiglotte ferme le passage vers les voies respiratoires (ne pas parler bouche pleine).",
            ],
            font_size=21,
            width=52,
        )
        degl_txt.next_to(entete2, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La déglutition est le réflexe qui fait passer le bol "
                "alimentaire de la bouche dans le pharynx, puis dans "
                "l'œsophage. Un petit clapet, l'épiglotte, ferme le "
                "passage vers les voies respiratoires : c'est pourquoi il "
                "ne faut ni parler ni rire la bouche pleine."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(degl_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete2), FadeOut(degl_txt))

        peristaltisme = definition_box(
            Text(
                _wrap(
                    "Le péristaltisme est l'ensemble des contractions "
                    "ondulatoires des muscles lisses de la paroi du tube "
                    "digestif. Ces ondes propulsent le contenu alimentaire "
                    "de la bouche vers l'anus et contribuent au brassage "
                    "avec les sucs digestifs.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        peristaltisme.next_to(titre, DOWN, buff=0.5)

        # Petit schéma d'onde péristaltique : suite de cercles qui se déplacent
        tube = VGroup(*[Circle(radius=0.28, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5) for _ in range(5)])
        tube.arrange(RIGHT, buff=0.15)
        tube.next_to(peristaltisme, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans l'œsophage, et tout le long du tube, le contenu "
                "avance grâce au péristaltisme : l'ensemble des "
                "contractions ondulatoires des muscles lisses de la paroi "
                "du tube digestif. Ces ondes propulsent le contenu "
                "alimentaire de la bouche vers l'anus, et contribuent au "
                "brassage des aliments avec les sucs digestifs."
            )
        ) as tracker:
            self.play(FadeIn(peristaltisme))
            self.play(FadeIn(tube))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(peristaltisme), FadeOut(tube))

        # --- Estomac : brassage gastrique → chyme ----------------------------
        entete3 = Text("Dans l'estomac : le brassage gastrique", font_size=24, color=YELLOW, weight="BOLD")
        entete3.next_to(titre, DOWN, buff=0.45)

        estomac_txt = _bullets(
            [
                "De puissantes contractions mélangent le bol au suc gastrique, pendant 3 à 4 heures.",
                "Le contenu devient une pâte semi-liquide et acide : le chyme.",
                "Le chyme franchit le pylore et gagne le duodénum.",
            ],
            font_size=21,
            width=52,
        )
        estomac_txt.next_to(entete3, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans l'estomac, de puissantes contractions mélangent le "
                "bol alimentaire au suc gastrique pendant trois à quatre "
                "heures : c'est le brassage gastrique. Le contenu devient "
                "une pâte semi-liquide et acide, le chyme, qui franchit "
                "progressivement le pylore, orifice de sortie de "
                "l'estomac, pour gagner le duodénum."
            )
        ) as tracker:
            self.play(FadeIn(entete3))
            self.play(FadeIn(estomac_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete3), FadeOut(estomac_txt))

        # --- Intestin grêle et gros intestin ----------------------------------
        entete4 = Text("Intestin grêle et gros intestin", font_size=24, color=YELLOW, weight="BOLD")
        entete4.next_to(titre, DOWN, buff=0.45)

        intestin_txt = _bullets(
            [
                "Intestin grêle : segmentation + péristaltisme mélangent le chyme aux 3 sucs ; le contenu devient laiteux → chyle.",
                "Gros intestin : péristaltisme lent, absorption d'une grande partie de l'eau restante.",
                "Les résidus non digérés forment les fèces, stockées dans le rectum jusqu'à la défécation.",
            ],
            font_size=20,
            width=54,
        )
        intestin_txt.next_to(entete4, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans l'intestin grêle, les mouvements de segmentation et "
                "le péristaltisme mélangent le chyme à la bile, au suc "
                "pancréatique et au suc intestinal. Au fur et à mesure que "
                "la digestion s'achève et que l'absorption commence, le "
                "contenu prend un aspect laiteux : c'est le chyle. Dans le "
                "gros intestin, le péristaltisme, beaucoup plus lent, "
                "permet l'absorption d'une grande partie de l'eau "
                "restante. Les résidus non digérés forment les fèces, "
                "stockées dans le rectum puis évacuées lors de la "
                "défécation."
            )
        ) as tracker:
            self.play(FadeIn(entete4))
            self.play(FadeIn(intestin_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete4), FadeOut(intestin_txt))

        # --- Exemple traité / vocabulaire -------------------------------------
        vocabulaire = definition_box(
            Text(
                _wrap(
                    "Vocabulaire : bol alimentaire = pâte formée en bouche "
                    "(mastication + insalivation) ; chyme = pâte "
                    "semi-liquide et acide sortant de l'estomac ; chyle = "
                    "liquide laiteux de l'intestin grêle après digestion ; "
                    "fèces = résidus non digérés, évacués par l'anus.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        vocabulaire.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ce vocabulaire précis : le bol alimentaire est "
                "la pâte formée dans la bouche par la mastication et "
                "l'insalivation ; le chyme est la pâte semi-liquide et "
                "acide qui sort de l'estomac ; le chyle est le liquide "
                "laiteux riche en nutriments, contenu de l'intestin grêle "
                "après digestion ; les fèces sont les résidus non digérés "
                "et déshydratés, évacués par l'anus."
            )
        ) as tracker:
            self.play(FadeIn(vocabulaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vocabulaire))

        # --- À retenir / méthode : pourquoi bien mastiquer ? ------------------
        methode = method_box(
            Text(
                _wrap(
                    "Étape 1 : la mastication fragmente les aliments, ce "
                    "qui multiplie la surface offerte aux enzymes. "
                    "Étape 2 : l'insalivation enrobe chaque fragment "
                    "d'amylase salivaire : la digestion chimique de "
                    "l'amidon commence dès la bouche. Étape 3 : un bol "
                    "bien mastiqué arrive en petits morceaux faciles à "
                    "brasser ; l'estomac travaille moins et mieux. "
                    "Conclusion : la grand-mère d'Awa a raison !",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode : pourquoi faut-il bien mastiquer ? Étape un : la "
                "mastication fragmente les aliments, ce qui multiplie la "
                "surface de contact offerte aux enzymes. Étape deux : "
                "l'insalivation enrobe chaque fragment de salive, donc "
                "d'amylase salivaire : la digestion chimique de l'amidon "
                "commence ainsi dès la bouche. Étape trois : un bol bien "
                "mastiqué arrive dans l'estomac sous forme de petits "
                "morceaux faciles à brasser ; l'estomac travaille moins et "
                "mieux. Conclusion : avaler de gros morceaux sans mâcher "
                "ralentit toute la digestion et fatigue l'estomac. La "
                "grand-mère d'Awa a raison !"
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
