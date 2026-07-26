"""
scenes/SVT_ProductionMatiere_09.py — Chapitre 11 (1ereD, SVT), scène 09.

§ 11.5 L'importance de la production de matière : pour le végétal
lui-même, pour les autres êtres vivants et l'équilibre de la nature
(producteurs, source d'énergie, équilibre atmosphérique), danger de la
déforestation (forêt de Taï, parc d'Azagny) — retour aux questions
d'Aya posées en scène 01 — puis L'ESSENTIEL DU CHAPITRE.
Source : 1ereD/SVT.pdf, pages 153-154.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Star, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ImportanceProductionEtEssentiel(NotionScene):
    def construct(self):
        # --- Énoncé : pour le végétal lui-même ------------------------------
        titre = scene_title("11.5 — L'importance de la production de matière")
        titre.scale(0.5)
        titre.to_edge(UP)

        pour_le_vegetal = property_box(
            Text(
                _wrap(
                    "Grâce à l'assimilation chlorophyllienne, le végétal "
                    "vert construit toute sa matière : feuilles, tige, "
                    "racines, fleurs, fruits et graines. C'est elle qui "
                    "permet au plant de maïs de Kouadio de passer de "
                    "quelques grammes à plusieurs kilogrammes, et qui "
                    "constitue les réserves permettant à la graine de "
                    "germer.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        pour_le_vegetal.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Grâce à l'assimilation chlorophyllienne, le végétal vert "
                "construit toute sa matière : ses feuilles, sa tige, ses "
                "racines, ses fleurs, ses fruits et ses graines. C'est "
                "elle qui permet au plant de maïs de Kouadio de passer de "
                "quelques grammes à plusieurs kilogrammes. Elle assure "
                "aussi les réserves qui permettront à la graine de germer, "
                "et à la plante vivace de repartir après la saison sèche."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(pour_le_vegetal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pour_le_vegetal))

        # --- Animation du raisonnement : rôle dans la nature -------------------------
        role_nature = property_box(
            _bullets(
                [
                    "Source de matière organique : les végétaux verts "
                    "sont les producteurs, à la base de toutes les "
                    "chaînes alimentaires.",
                    "Source d'énergie : toute l'énergie des êtres vivants "
                    "vient, directement ou non, de l'énergie solaire "
                    "stockée par la photosynthèse (bois, charbon, "
                    "pétrole).",
                    "Équilibre de l'atmosphère : en absorbant du CO2 et "
                    "en rejetant du O2, les végétaux renouvellent l'air "
                    "respirable et limitent le réchauffement climatique.",
                ],
                font_size=19,
                width=56,
            ),
            box_width=12.0,
        )
        role_nature.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les végétaux verts jouent aussi un rôle fondamental pour "
                "les autres êtres vivants et pour l'équilibre de la "
                "nature. D'abord, ils sont source de matière organique : "
                "les végétaux verts sont les producteurs, ils sont à la "
                "base de toutes les chaînes alimentaires ; l'homme se "
                "nourrit de végétaux, riz, igname, maïs, manioc, ou "
                "d'animaux qui ont mangé des végétaux. Ensuite, ils sont "
                "source d'énergie : toute l'énergie des êtres vivants "
                "provient, directement ou non, de l'énergie solaire "
                "stockée par la photosynthèse, y compris le bois de "
                "chauffe et, à l'échelle des temps géologiques, le charbon "
                "et le pétrole. Enfin, ils assurent l'équilibre de "
                "l'atmosphère : en absorbant du CO2 et en rejetant du O2, "
                "les végétaux verts renouvellent l'air respirable et "
                "limitent l'augmentation du dioxyde de carbone "
                "atmosphérique, gaz qui contribue au réchauffement "
                "climatique."
            )
        ) as tracker:
            self.play(FadeIn(role_nature))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(role_nature))

        # --- Exemple traité : retour à la 3e question d'Aya, la déforestation -----
        exemple_deforestation = example_box(
            Text(
                _wrap(
                    "Revenons à la question d'Aya : pourquoi les forêts, "
                    "comme celle de Taï, sont-elles le « poumon » de la "
                    "planète ? La déforestation, qui réduit les forêts "
                    "ivoiriennes (Taï, parc d'Azagny), supprime à la fois "
                    "des producteurs de matière et des régulateurs de "
                    "l'atmosphère.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        exemple_deforestation.next_to(titre, DOWN, buff=0.5)

        etoile_taï = Star(color=YELLOW, fill_color=YELLOW, fill_opacity=1.0).scale(0.18)
        etiquette_taï = Text("forêt de Taï / parc d'Azagny\n(danger : déforestation)", font_size=15, color=YELLOW)
        mini_carte = VGroup(etoile_taï, etiquette_taï).arrange(DOWN, buff=0.15)
        mini_carte.next_to(exemple_deforestation, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Revenons à la troisième question d'Aya posée au début du "
                "chapitre : pourquoi dit-on que les grandes forêts, comme "
                "celle de Taï, sont le poumon de la planète ? C'est "
                "pourquoi la déforestation massive, comme celle qui réduit "
                "les forêts ivoiriennes, la forêt de Taï, le parc "
                "d'Azagny, supprime à la fois des producteurs de matière "
                "et des régulateurs de l'atmosphère. Reboiser et protéger "
                "les forêts, c'est protéger la machine qui produit la "
                "matière et l'oxygène de la planète."
            )
        ) as tracker:
            self.play(FadeIn(exemple_deforestation))
            self.play(FadeIn(mini_carte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_deforestation), FadeOut(mini_carte))

        # --- L'ESSENTIEL DU CHAPITRE (clôture) --------------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "À la lumière : absorption de CO2, dégagement de O2 ; "
                    "à l'obscurité : seule la respiration (O2 absorbé, "
                    "CO2 dégagé), qui a lieu en réalité jour et nuit.",
                    "Matière produite à partir de CO2 de l'air (carbone) "
                    "et d'eau + sels minéraux du sol (racines).",
                    "4 conditions indispensables : lumière, chlorophylle, "
                    "CO2, eau — chacune prouvée par une expérience avec "
                    "témoin.",
                    "Test à l'eau iodée (bleu-noir = amidon) : révélateur "
                    "de la production ; feuille décolorée au préalable.",
                    "Feuille = organe de production ; stomates = passage "
                    "des gaz ; chloroplastes = siège des réactions.",
                    "Photosynthèse : 6CO2 + 6H2O → C6H12O6 + 6O2 (lumière "
                    "+ chlorophylle) ; convertit énergie lumineuse en "
                    "énergie chimique.",
                    "Respiration (équation inverse) : C6H12O6 + 6O2 → "
                    "6CO2 + 6H2O — à ne jamais confondre avec la "
                    "photosynthèse.",
                    "Végétal vert autotrophe : producteur, à la base des "
                    "chaînes alimentaires, régulateur de l'atmosphère.",
                ],
                font_size=16,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. À la lumière, le végétal "
                "vert absorbe du CO2 et dégage du O2 ; à l'obscurité, on "
                "n'observe plus que la respiration, absorption de O2, "
                "dégagement de CO2, laquelle a en réalité lieu jour et "
                "nuit. Le végétal vert produit sa matière à partir de "
                "matière minérale, le CO2 de l'air pour le carbone, l'eau "
                "et les sels minéraux du sol absorbés par les racines. "
                "Quatre conditions sont indispensables : lumière, "
                "chlorophylle, CO2, eau ; chacune se prouve par une "
                "expérience avec témoin. Le test à l'eau iodée, bleu-noir "
                "en présence d'amidon, est le révélateur de la production "
                "de matière ; la feuille est décolorée au préalable. La "
                "feuille est l'organe de la production, les stomates "
                "laissent passer les gaz, les chloroplastes sont les "
                "sièges des réactions. L'équation bilan de l'assimilation "
                "chlorophyllienne, six CO2 plus six H2O donnent C6H12O6 "
                "plus six O2, en présence de lumière et de chlorophylle, "
                "convertit l'énergie lumineuse en énergie chimique "
                "stockée dans la matière organique. La respiration est "
                "l'équation inverse, elle ne doit jamais être confondue "
                "avec la photosynthèse. Enfin, le végétal vert est "
                "autotrophe : il produit lui-même sa matière, il est à la "
                "base des chaînes alimentaires et régule l'atmosphère."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
