"""
scenes/SVT_DigestionAliments_10.py — Chapitre 12 (1ereD, SVT), scène 10.

§ 12.7 Hygiène du système digestif : troubles fréquents (carie, gastrite /
ulcère, diarrhées / typhoïde / choléra, constipation, hépatites), les
règles d'or, application au choléra en Côte d'Ivoire, puis L'ESSENTIEL DU
CHAPITRE.
Source : 1ereD/SVT.pdf, pages 165-167.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class HygieneDuSystemeDigestif(NotionScene):
    def construct(self):
        titre = scene_title("12.7 — Hygiène du système digestif")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : un système digestif qui travaille bien -------------------
        intro = Text(
            _wrap(
                "Un système digestif qui travaille bien est le premier "
                "garant d'une bonne nutrition. Quelques troubles fréquents "
                "montrent l'importance des règles d'hygiène.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un système digestif qui travaille bien est le premier "
                "garant d'une bonne nutrition. Quelques troubles fréquents "
                "montrent l'importance des règles d'hygiène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les troubles fréquents -----------------
        entete_troubles = Text("Troubles fréquents du système digestif", font_size=23, color=YELLOW, weight="BOLD")
        entete_troubles.next_to(titre, DOWN, buff=0.45)

        troubles = _bullets(
            [
                "Carie dentaire (sucres + microbes de la plaque) : gêne la mastication, donc toute la digestion.",
                "Gastrite et ulcère gastroduodénal : excès d'acidité, Helicobacter pylori, anti-inflammatoires, tabac, alcool.",
                "Diarrhées infectieuses, fièvre typhoïde, choléra : transmis par l'eau et les aliments souillés.",
                "Constipation : favorisée par le manque de fibres et d'eau.",
                "Hépatites (virales ou liées à l'alcool) : endommagent le foie, glande digestive majeure.",
            ],
            font_size=18,
            width=58,
        )
        troubles.next_to(entete_troubles, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La carie dentaire, provoquée par les sucres et les "
                "microbes de la plaque dentaire, gêne la mastication, donc "
                "toute la digestion. La gastrite, inflammation de la "
                "muqueuse de l'estomac, et l'ulcère gastroduodénal sont "
                "favorisés par l'excès d'acidité, une bactérie, "
                "Helicobacter pylori, l'abus d'anti-inflammatoires, le "
                "tabac et l'alcool. Les diarrhées infectieuses, la fièvre "
                "typhoïde et le choléra se transmettent par l'eau et les "
                "aliments souillés. La constipation est favorisée par le "
                "manque de fibres et d'eau. Les hépatites, virales ou "
                "liées à l'alcool, endommagent le foie, glande digestive "
                "majeure."
            )
        ) as tracker:
            self.play(FadeIn(entete_troubles))
            self.play(FadeIn(troubles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_troubles), FadeOut(troubles))

        # --- Exemple traité : les règles d'or de l'hygiène digestive -----------
        regles = method_box(
            Text(
                _wrap(
                    "1. Se laver les mains à l'eau et au savon avant de "
                    "manger et après les toilettes. 2. Boire une eau saine "
                    "; laver soigneusement fruits et légumes crus. 3. Bien "
                    "cuire viandes et poissons ; éviter les aliments "
                    "avariés. 4. Mastiquer lentement, repas équilibrés à "
                    "heures régulières. 5. Éviter alcool, tabac et "
                    "automédication. 6. Se brosser les dents, consulter en "
                    "cas de trouble persistant.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=12.0,
        )
        regles.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les règles d'or de l'hygiène digestive. Un : se laver les "
                "mains à l'eau et au savon avant de préparer ou de prendre "
                "un repas, et après être allé aux toilettes. Deux : boire "
                "une eau saine, potable, bouillie ou traitée ; laver "
                "soigneusement fruits et légumes consommés crus. Trois : "
                "bien cuire les viandes et les poissons ; éviter les "
                "aliments avariés ou mal conservés. Quatre : mastiquer "
                "lentement, manger à heures régulières et composer des "
                "repas équilibrés. Cinq : éviter l'alcool, le tabac et "
                "l'automédication. Six : se brosser les dents après les "
                "repas et consulter un médecin en cas de douleur ou de "
                "trouble persistant."
            )
        ) as tracker:
            self.play(FadeIn(regles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regles))

        cholera = example_box(
            Text(
                _wrap(
                    "En Côte d'Ivoire, lors des épidémies de choléra, "
                    "l'application stricte des trois premières règles "
                    "suffit à protéger efficacement une famille : la "
                    "plupart des microbes responsables des diarrhées "
                    "graves pénètrent dans le corps par la bouche, avec "
                    "l'eau ou les aliments contaminés.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        cholera.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Application directe : en Côte d'Ivoire, lors des "
                "épidémies de choléra, l'application stricte des trois "
                "premières règles suffit à protéger efficacement une "
                "famille : la plupart des microbes responsables des "
                "diarrhées graves pénètrent dans le corps par la bouche, "
                "avec l'eau ou les aliments contaminés."
            )
        ) as tracker:
            self.play(FadeIn(cholera))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cholera))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne crois pas que le choléra ou les diarrhées graves "
                    "relèvent de la « malchance » : ce sont des maladies "
                    "évitables, transmises par l'eau et les aliments "
                    "souillés — l'hygiène des mains et de l'eau les "
                    "prévient efficacement.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention : ne crois pas que le choléra ou les diarrhées "
                "graves relèvent de la malchance. Ce sont des maladies "
                "évitables, transmises par l'eau et les aliments souillés "
                "— l'hygiène des mains et de l'eau les prévient "
                "efficacement."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE -------------------------------------
        essentiel1 = essentiel_box(
            Text(
                _wrap(
                    "La digestion transforme les aliments en nutriments "
                    "par des actions mécaniques (mastication, "
                    "insalivation, péristaltisme, brassage) et chimiques "
                    "(enzymes des sucs digestifs). Le tube digestif : "
                    "bouche, pharynx, œsophage, estomac, intestin grêle "
                    "(duodénum, jéjunum, iléon), gros intestin, rectum, "
                    "anus. Glandes : salivaires, foie (bile → vésicule "
                    "biliaire), pancréas, glandes gastriques et "
                    "intestinales.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=12.2,
        )
        essentiel1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'essentiel du chapitre. La digestion transforme les "
                "aliments en nutriments assimilables par des actions "
                "mécaniques — mastication, insalivation, péristaltisme, "
                "brassage — et des actions chimiques, les enzymes des sucs "
                "digestifs. Le tube digestif comprend, dans l'ordre : "
                "bouche, pharynx, œsophage, estomac, intestin grêle, "
                "avec duodénum, jéjunum et iléon, gros intestin, rectum, "
                "anus. Les glandes sont les glandes salivaires, le foie, "
                "avec la bile stockée dans la vésicule biliaire, le "
                "pancréas, ainsi que les glandes gastriques et "
                "intestinales."
            )
        ) as tracker:
            self.play(FadeIn(essentiel1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel1))

        essentiel2 = essentiel_box(
            Text(
                _wrap(
                    "Bouche : amylase salivaire → maltose (bol "
                    "alimentaire). Estomac : suc gastrique acide (pH "
                    "1,5-2) + pepsine → polypeptides (chyme). Intestin "
                    "grêle : bile (émulsion) + suc pancréatique (amylase, "
                    "trypsine, lipase) + suc intestinal (peptidases, "
                    "maltase, saccharase, lactase) → glucose, acides "
                    "aminés, acides gras, glycérol (chyle). Enzymes : "
                    "protéines spécifiques, sensibles à T° et pH.",
                    width=54,
                ),
                font_size=17,
            ),
            box_width=12.2,
        )
        essentiel2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Dans la bouche, l'amylase salivaire transforme l'amidon "
                "en maltose ; le bol alimentaire se forme. Dans l'estomac, "
                "le suc gastrique très acide, pH un virgule cinq à deux, "
                "et la pepsine transforment les protéines en "
                "polypeptides ; le chyme se forme. Dans l'intestin grêle, "
                "la bile émulsionne les graisses, le suc pancréatique — "
                "amylase, trypsine, lipase — et le suc intestinal — "
                "peptidases, maltase, saccharase, lactase — achèvent la "
                "digestion ; le chyle se forme. Les nutriments finaux "
                "absorbables sont le glucose, les acides aminés, les "
                "acides gras et le glycérol ; l'eau, les sels minéraux et "
                "les vitamines sont absorbés sans digestion. Les enzymes "
                "sont des protéines spécifiques d'un substrat, sensibles à "
                "la température, avec un optimum vers trente-sept degrés, "
                "et au pH."
            )
        ) as tracker:
            self.play(FadeIn(essentiel2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel2))

        essentiel3 = essentiel_box(
            Text(
                _wrap(
                    "L'absorption a lieu dans l'intestin grêle (≈4-5 "
                    "millions de villosités, surface ≈200-300 m²) : "
                    "glucose et acides aminés → sang (veine porte → foie) "
                    "; acides gras et glycérol → lymphe. Le gros intestin "
                    "absorbe l'eau et les sels minéraux ; les résidus "
                    "forment les fèces. Hygiène : mains propres, eau "
                    "saine, aliments lavés et bien cuits, mastication "
                    "lente, repas équilibrés, pas d'alcool ni "
                    "d'automédication.",
                    width=54,
                ),
                font_size=17,
            ),
            box_width=12.2,
        )
        essentiel3.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'absorption a lieu dans l'intestin grêle, environ "
                "quatre à cinq millions de villosités, surface totale de "
                "deux cents à trois cents mètres carrés : le glucose et "
                "les acides aminés passent dans le sang, via la veine "
                "porte hépatique et le foie ; les acides gras et le "
                "glycérol passent dans la lymphe. Le gros intestin "
                "absorbe l'eau et les sels minéraux ; les résidus forment "
                "les fèces. Enfin, l'hygiène du système digestif repose "
                "sur des mains propres, une eau saine, des aliments lavés "
                "et bien cuits, une mastication lente, des repas "
                "équilibrés, et l'absence d'alcool et d'automédication."
            )
        ) as tracker:
            self.play(FadeIn(essentiel3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel3))
