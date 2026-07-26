"""
scenes/SVT_EchangesIonsSol_08.py — Chapitre 8 (1ereD, SVT), scène 08.

§ 8.4 Applications agricoles : fumure et conservation de la fertilité.
Pourquoi fertiliser, types de fumure (minérale, organique, amendements),
exemple de calcul d'un apport d'engrais NPK, pratiques qui préservent la
fertilité des sols ivoiriens. Source : 1ereD/SVT.pdf, pages 112-113.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ApplicationsAgricoles(NotionScene):
    def construct(self):
        titre = scene_title("8.4 — Fumure et conservation de la fertilité")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi fertiliser un sol ? --------------------------
        intro = Text(
            _wrap(
                "À chaque récolte, l'agriculteur exporte les éléments "
                "minéraux accumulés dans les grains, tubercules et "
                "fruits. Les pluies lessivent, l'érosion emporte la terre "
                "fertile de surface. Sans restitution, le sol s'épuise : "
                "on parle de « terre fatiguée ».",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À chaque récolte, l'agriculteur exporte les éléments "
                "minéraux accumulés dans les grains, les tubercules et les "
                "fruits. Les pluies lessivent les éléments non retenus, "
                "l'érosion emporte la terre fertile de surface. Sans "
                "restitution, le sol s'épuise : on parle alors de terre "
                "fatiguée. La fumure restitue au sol ce que les cultures "
                "lui ont pris."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : les types de fumure ------------------------------
        fumure_minerale = property_box(
            Text(
                _wrap(
                    "La fumure minérale : engrais de synthèse (NPK "
                    "15-15-15 = 15% azote, 15% acide phosphorique P2O5, "
                    "15% potasse K2O ; urée 46% azote). Avantage : "
                    "éléments directement disponibles. Limites : aucun "
                    "apport d'humus, risque de lessivage sur sol sableux, "
                    "acidification en cas d'abus.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        fumure_minerale.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Il existe plusieurs types de fumure. La fumure minérale "
                "utilise des engrais de synthèse, comme le NPK "
                "quinze-quinze-quinze, c'est-à-dire quinze pour cent "
                "d'azote, quinze pour cent d'acide phosphorique et quinze "
                "pour cent de potasse, ou l'urée, à quarante-six pour cent "
                "d'azote. Son avantage : les éléments sont directement "
                "disponibles pour la plante. Ses limites : elle n'apporte "
                "aucun humus, elle risque d'être lessivée sur un sol "
                "sableux, et elle peut acidifier le sol en cas d'abus."
            )
        ) as tracker:
            self.play(FadeIn(fumure_minerale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(fumure_minerale))

        fumure_organique = property_box(
            Text(
                _wrap(
                    "La fumure organique : fumier, compost, résidus "
                    "enfouis. Nourrit le sol en humus, augmente la CEC, "
                    "améliore la structure, libère lentement. Les "
                    "amendements : chaulage des sols acides (relève le "
                    "pH, rend les éléments disponibles). Meilleure "
                    "stratégie : la fumure organo-minérale, les deux "
                    "associées.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        fumure_organique.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La fumure organique, elle, utilise le fumier, le "
                "compost, ou des résidus enfouis. Elle nourrit le sol en "
                "humus, augmente la capacité d'échange de cations, "
                "améliore la structure du sol, et libère ses éléments "
                "lentement. On distingue enfin les amendements, comme le "
                "chaulage des sols acides, qui relève le pH et rend les "
                "éléments minéraux disponibles. La meilleure stratégie "
                "reste la fumure organo-minérale, qui associe les deux "
                "types d'apport."
            )
        ) as tracker:
            self.play(FadeIn(fumure_organique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(fumure_organique))

        # --- Exemple traité : calculer un apport d'engrais ------------------
        exemple = example_box(
            _bullets(
                [
                    "150 kg/ha d'engrais NPK 15-15-15 sur une cacaoyère "
                    "de 2 ha.",
                    "Étape 1 : masse totale = 150 × 2 = 300 kg.",
                    "Étape 2 : masse d'azote = 300 × 15/100 = 45 kg.",
                    "Étape 3 : de même, 45 kg de P2O5 et 45 kg de K2O.",
                    "Conclusion : 45 kg de chacun des trois éléments "
                    "majeurs, pour les 2 hectares.",
                ],
                font_size=19,
                width=56,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Calculons un apport d'engrais. Un agriculteur épand cent "
                "cinquante kilogrammes par hectare d'engrais NPK "
                "quinze-quinze-quinze sur une cacaoyère de deux hectares. "
                "Étape un : la masse totale d'engrais épandue est de cent "
                "cinquante fois deux, soit trois cents kilogrammes. Étape "
                "deux : la masse d'azote est de trois cents fois quinze "
                "divisé par cent, soit quarante-cinq kilogrammes. Étape "
                "trois : de la même façon, on obtient quarante-cinq "
                "kilogrammes d'acide phosphorique et quarante-cinq "
                "kilogrammes de potasse. Conclusion : cet épandage apporte "
                "quarante-cinq kilogrammes de chacun des trois éléments "
                "majeurs, sur les deux hectares."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : les pratiques qui préservent la fertilité ---------
        pratiques = method_box(
            _bullets(
                [
                    "Rotation avec légumineuses (niébé, arachide, soja) : "
                    "nodosités enrichissent le sol en azote gratuitement.",
                    "Jachère et couverture végétale : reconstitue "
                    "l'humus, paillage protège des pluies battantes.",
                    "Lutte contre l'érosion : haies vives, cultures en "
                    "courbes de niveau.",
                    "Limitation des brûlis : le feu détruit l'humus et "
                    "fait fuir les éléments minéraux.",
                    "Fumure raisonnée : doses adaptées après analyse, "
                    "apports fractionnés sur sols sableux à faible CEC.",
                ],
                font_size=18,
                width=58,
            ),
            box_width=12.6,
        )
        pratiques.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons enfin les pratiques qui préservent durablement "
                "la fertilité des sols ivoiriens. La rotation avec des "
                "légumineuses, comme le niébé, l'arachide ou le soja : les "
                "bactéries de leurs nodosités racinaires enrichissent le "
                "sol en azote, gratuitement. La jachère et la couverture "
                "végétale, qui laissent le sol reconstituer son humus, le "
                "paillage protégeant des pluies battantes. La lutte "
                "contre l'érosion, avec des haies vives et des cultures en "
                "courbes de niveau. La limitation des brûlis, car le feu "
                "détruit l'humus et fait fuir les éléments minéraux. Et "
                "enfin, la fumure raisonnée, avec des doses adaptées après "
                "analyse du sol, et des apports fractionnés sur les sols "
                "sableux à faible CEC."
            )
        ) as tracker:
            self.play(FadeIn(pratiques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pratiques))

        # --- Piège à éviter : la fumure minérale seule ne suffit pas -------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège classique : croire qu'ajouter de l'engrais "
                    "minéral seul règle tout. Sans matière organique, la "
                    "CEC du sol ne s'améliore pas : sur un sol sableux "
                    "pauvre, une bonne partie de l'engrais est lessivée "
                    "avant même que la plante ne l'absorbe.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège classique : croire qu'ajouter de "
                "l'engrais minéral seul règle tout. Sans apport de matière "
                "organique, la capacité d'échange de cations du sol ne "
                "s'améliore pas : sur un sol sableux pauvre, une bonne "
                "partie de l'engrais est lessivée avant même que la "
                "plante n'ait pu l'absorber. La fertilisation efficace "
                "combine toujours restitution minérale et entretien de "
                "l'humus."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
