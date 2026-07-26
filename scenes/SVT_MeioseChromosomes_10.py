"""
scenes/SVT_MeioseChromosomes_10.py — Chapitre 2 (1ereC, SVT), scène 10.

§ Méthodes et astuces : les 3 méthodes clés (identifier une phase sur un
schéma, compter chromosomes/chromatides/ADN, calculer le nombre de types
de gamètes) + les 3 pièges à éviter (réduction "à la fin de la méiose II"
est faux, confondre chromosome/chromatide, confondre les deux brassages) +
phrase-clé de synthèse, puis L'ESSENTIEL DU CHAPITRE.
Source : 1ereC/SVT.pdf, pages 20-21.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class MethodesAstucesEtEssentielDuChapitre(NotionScene):
    def construct(self):
        titre = scene_title("2.8 — Méthodes et astuces")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi des méthodes --------------------------------
        enonce = Text(
            _wrap(
                "Avant de conclure ce chapitre, voici les trois méthodes "
                "clés à maîtriser, puis les trois pièges les plus fréquents "
                "à l'examen.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avant de conclure ce chapitre, voici les trois méthodes "
                "clés à maîtriser, puis les trois pièges les plus fréquents "
                "à l'examen."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : Méthode 1 --------------------------
        methode1 = method_box(
            _bullets(
                [
                    "1. Les chromosomes sont-ils appariés en bivalents ? "
                    "Oui → méiose I (prophase I ou métaphase I). Sinon → "
                    "méiose II ou mitose.",
                    "2. Que se sépare-t-il ? Homologues (entiers, à 2 "
                    "chromatides) → anaphase I. Chromatides sœurs → "
                    "anaphase II (ou mitose).",
                    "3. Combien y a-t-il de cellules en division ? 1 → "
                    "méiose I. 2 → méiose II.",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.2,
        )
        methode1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode un : identifier une phase de la méiose sur un "
                "schéma. Posez-vous trois questions, toujours dans le même "
                "ordre. Un : les chromosomes sont-ils appariés en bivalents "
                "? Si oui, c'est la méiose I, prophase ou métaphase I ; "
                "sinon, c'est la méiose II ou une mitose. Deux : que se "
                "sépare-t-il ? Des homologues entiers, à deux chromatides, "
                "c'est l'anaphase I ; des chromatides sœurs, c'est "
                "l'anaphase II, ou une anaphase de mitose. Trois : combien y "
                "a-t-il de cellules en division ? Une seule cellule, c'est "
                "la méiose I ; deux cellules, c'est la méiose II."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 --------------------------------------------------------
        methode2 = method_box(
            _bullets(
                [
                    "1 centromère = 1 chromosome (peu importe le nombre de "
                    "chromatides).",
                    "Après l'interphase et jusqu'à la métaphase II : 1 "
                    "chromosome = 2 chromatides.",
                    "ADN : réplication ⇒ Q→2Q ; méiose I ⇒ 2Q→Q ; méiose "
                    "II ⇒ Q→Q/2.",
                    "Dressez toujours un petit tableau (comme dans "
                    "l'Exemple résolu 1) pour sécuriser le raisonnement.",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.2,
        )
        methode2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode deux : compter les chromosomes, les chromatides et "
                "l'ADN. Un centromère égale un chromosome, peu importe le "
                "nombre de chromatides. Après l'interphase, et jusqu'à la "
                "métaphase II, un chromosome égale deux chromatides. Pour "
                "l'ADN : la réplication fait passer de Q à deux Q ; la "
                "méiose I fait retomber de deux Q à Q ; la méiose II fait "
                "passer de Q à Q sur deux. Dressez toujours un petit "
                "tableau, comme dans l'exemple résolu un : cela sécurise le "
                "raisonnement."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Méthode 3 --------------------------------------------------------
        methode3 = method_box(
            _bullets(
                [
                    "1. Repérez le nombre n de paires d'homologues "
                    "(attention : n = moitié du nombre total de "
                    "chromosomes).",
                    "2. Appliquez 2ⁿ pour le brassage interchromosomique "
                    "seul.",
                    "3. Si l'énoncé mentionne des crossing-over, précisez "
                    "que le nombre réel est supérieur à 2ⁿ.",
                    "4. Pour un couple, multipliez les possibilités des "
                    "deux parents.",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.2,
        )
        methode3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode trois : calculer le nombre de types de gamètes. "
                "Un : repérez le nombre n de paires d'homologues — attention, "
                "n est la moitié du nombre total de chromosomes. Deux : "
                "appliquez deux puissance n pour le seul brassage "
                "interchromosomique. Trois : si l'énoncé mentionne des "
                "crossing-over, précisez que le nombre réel est supérieur à "
                "deux puissance n. Quatre : pour un couple, multipliez les "
                "possibilités des deux parents."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Exemple traité : les 3 pièges à éviter -------------------------
        pieges = warning_box(
            _bullets(
                [
                    "Piège 1 — « La réduction a lieu à la fin de la méiose "
                    "II » : FAUX. Le passage de 2n à n est réalisé dès la "
                    "fin de la méiose I (anaphase I). La méiose II est "
                    "équationnelle (n→n).",
                    "Piège 2 — Confondre chromosome et chromatide : fin "
                    "d'interphase, la cellule humaine a 46 chromosomes ET "
                    "92 chromatides — pas 92 chromosomes. Comptez les "
                    "centromères.",
                    "Piège 3 — Confondre les deux brassages : "
                    "interchromosomique = hasard de la séparation des "
                    "homologues (anaphase I) ⇒ formule 2ⁿ. "
                    "Intrachromosomique = crossing-over (prophase I) ⇒ "
                    "chromosomes recombinés.",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.6,
        )
        pieges.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Passons maintenant aux trois pièges à éviter absolument. "
                "Premier piège : dire que la réduction a lieu à la fin de la "
                "méiose II est faux. Le passage de deux n à n est réalisé "
                "dès la fin de la méiose I, à l'anaphase I ; la méiose II ne "
                "fait que séparer des chromatides dans des cellules déjà "
                "haploïdes, elle est équationnelle, n reste n. Deuxième "
                "piège : confondre chromosome et chromatide. À la fin de "
                "l'interphase, la cellule humaine possède quarante-six "
                "chromosomes et quatre-vingt-douze chromatides, et non "
                "quatre-vingt-douze chromosomes : comptez toujours les "
                "centromères. Troisième piège : confondre les deux "
                "brassages. Le brassage interchromosomique, c'est le hasard "
                "de la séparation des homologues en anaphase I, qui donne la "
                "formule deux puissance n. Le brassage intrachromosomique, "
                "ce sont les crossing-over de la prophase I, qui donnent des "
                "chromosomes recombinés. Dans une copie, citez toujours les "
                "deux mécanismes avec leur phase."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges))

        # --- À retenir : phrase-clé de synthèse -------------------------------
        phrase_cle = method_box(
            Text(
                _wrap(
                    "« La méiose est une double division précédée d'une "
                    "seule réplication de l'ADN : elle produit quatre "
                    "cellules haploïdes toutes différentes. Elle assure "
                    "ainsi, avec la fécondation, la constance du nombre de "
                    "chromosomes d'une génération à l'autre, tout en étant, "
                    "par les brassages génétiques, une source de diversité "
                    "au sein de l'espèce. »",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        phrase_cle.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici l'astuce finale : une phrase-clé de synthèse à savoir "
                "rédiger en devoir. La méiose est une double division "
                "précédée d'une seule réplication de l'ADN : elle produit "
                "quatre cellules haploïdes toutes différentes. Elle assure "
                "ainsi, avec la fécondation, la constance du nombre de "
                "chromosomes d'une génération à l'autre, tout en étant, par "
                "les brassages génétiques, une source de diversité au sein "
                "de l'espèce."
            )
        ) as tracker:
            self.play(FadeIn(phrase_cle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(phrase_cle))

        # --- L'ESSENTIEL DU CHAPITRE (clôture) ---------------------------------
        titre_fin = scene_title("L'essentiel du chapitre 2")
        titre_fin.scale(0.65)
        titre_fin.to_edge(UP)
        self.play(FadeOut(titre), FadeIn(titre_fin))
        titre = titre_fin

        essentiel = essentiel_box(
            _bullets(
                [
                    "Méiose : 1 cellule mère diploïde (2n) → 4 cellules "
                    "filles haploïdes (n), différentes ; 2 divisions, 1 "
                    "seule réplication de l'ADN avant.",
                    "Ordre : prophase I, métaphase I, anaphase I, télophase "
                    "I, puis prophase II à télophase II.",
                    "Anaphase I : séparation des homologues, centromères "
                    "intacts → réduction (2n vers n).",
                    "Anaphase II : séparation des chromatides sœurs, "
                    "centromères divisés.",
                    "On compte les chromosomes en comptant les "
                    "centromères : un chromosome à 2 chromatides reste 1 "
                    "chromosome.",
                    "Caryotype humain : 2n=46 (22 paires d'autosomes + 1 "
                    "paire de gonosomes XX/XY).",
                    "Brassage interchromosomique (métaphase I, 2ⁿ "
                    "gamètes) + brassage intrachromosomique (crossing-over, "
                    "prophase I) : source de diversité.",
                    "Méiose/mitose : 2 divisions vs 1 ; 4 cellules "
                    "haploïdes différentes vs 2 cellules diploïdes "
                    "identiques.",
                    "Cycle méiose (2n→n) - fécondation (n→2n) : caryotype "
                    "constant + diversité des individus.",
                    "Anomalie : non-disjonction → trisomie 21 (47 "
                    "chromosomes, +21), risque croissant avec l'âge "
                    "maternel.",
                ],
                font_size=16,
                width=56,
            ),
            box_width=13.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si le contenu (10 points) dépasse la hauteur visible du
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
                "divisés. On compte toujours les chromosomes en comptant les "
                "centromères. Le caryotype humain compte deux n égale "
                "quarante-six chromosomes : vingt-deux paires d'autosomes et "
                "une paire de gonosomes, X X ou X Y. La diversité génétique "
                "vient de deux mécanismes : le brassage interchromosomique, "
                "en métaphase I, qui donne deux puissance n types de "
                "gamètes, et le brassage intrachromosomique, les "
                "crossing-over, en prophase I. Comparée à la mitose, une "
                "seule division qui produit deux cellules diploïdes "
                "identiques, la méiose comporte deux divisions et produit "
                "quatre cellules haploïdes différentes. Enfin, l'alternance "
                "entre méiose, qui réduit de deux n à n, et fécondation, qui "
                "ramène de n à deux n, assure à la fois la constance du "
                "nombre de chromosomes et la diversité des individus. Une "
                "anomalie, la non-disjonction, peut provoquer une trisomie "
                "vingt-et-un, à quarante-sept chromosomes, dont le risque "
                "augmente avec l'âge maternel — la solution des deux "
                "énigmes de la famille d'Abidjan."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
