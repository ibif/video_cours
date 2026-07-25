"""
scenes/SVT_FonctionsGonades_02.py — Chapitre 1 (1ereD, SVT), scène 02.

§ 1.1 Les gonades, organes reproducteurs : définition, position anatomique,
tableau des deux appareils, caractères sexuels primaires/secondaires,
piège gonade vs gamète. Source : 1ereD/SVT.pdf, pages 6-7.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class GonadesOrganesReproducteurs(NotionScene):
    def construct(self):
        titre = scene_title("1.1 — Les gonades, organes reproducteurs")
        titre.scale(0.75)
        titre.to_edge(UP)

        # --- Énoncé : définition + position anatomique --------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une gonade est une glande génitale : c'est l'organe qui "
                    "produit les gamètes. Chez l'être humain, les gonades "
                    "mâles sont les testicules, les gonades femelles sont "
                    "les ovaires.",
                    width=54,
                ),
                font_size=26,
            ),
            box_width=11.5,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une gonade est une glande génitale, c'est-à-dire l'organe "
                "essentiel de la reproduction : c'est elle qui produit les "
                "gamètes, les cellules reproductrices. Chez l'espèce humaine, "
                "les gonades mâles sont les testicules, et les gonades "
                "femelles sont les ovaires."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        position = Text(
            _wrap(
                "Les testicules sont logés hors de l'abdomen, dans le "
                "scrotum, à environ 35°C : une température inférieure de "
                "2 à 3° à celle du corps, nécessaire à la fabrication des "
                "gamètes mâles. Les ovaires, de la taille d'une amande "
                "(environ 3 cm), sont situés dans la cavité pelvienne, de "
                "part et d'autre de l'utérus.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        position.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À l'extérieur de la cavité abdominale, dans le scrotum, sont "
                "logés les deux testicules : cette position n'est pas un "
                "hasard, la fabrication des gamètes mâles exige une "
                "température d'environ trente-cinq degrés, inférieure de deux "
                "à trois degrés à la température interne du corps. Chez la "
                "femme, les deux ovaires, de la taille d'une amande, sont "
                "situés dans la cavité pelvienne, de part et d'autre de "
                "l'utérus."
            )
        ) as tracker:
            self.play(FadeIn(position))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(position))

        # --- Animation du raisonnement : tableau des deux appareils -------
        entete_tableau = Text(
            "Organisation des deux appareils génitaux", font_size=27, color=YELLOW, weight="BOLD"
        )
        entete_tableau.next_to(titre, DOWN, buff=0.5)

        masc_titre = Text("Appareil masculin", font_size=26, color=YELLOW, weight="BOLD")
        masc_lignes = _bullets(
            [
                "Gonades : testicules",
                "Voies génitales : épididymes, canaux déférents,\ncanaux éjaculateurs, urètre",
                "Glandes annexes : vésicules séminales, prostate",
            ],
            font_size=22,
            width=32,
        )
        masc = VGroup(masc_titre, masc_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        fem_titre = Text("Appareil féminin", font_size=26, color=YELLOW, weight="BOLD")
        fem_lignes = _bullets(
            [
                "Gonades : ovaires",
                "Voies génitales : trompes de Fallope,\nutérus, vagin",
                "Glandes annexes : glandes vulvo-vaginales",
            ],
            font_size=22,
            width=32,
        )
        fem = VGroup(fem_titre, fem_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        tableau = VGroup(masc, fem).arrange(RIGHT, buff=1.2, aligned_edge=UP)
        tableau.next_to(entete_tableau, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les gonades ne travaillent pas seules : elles sont reliées à "
                "des voies génitales, qui acheminent les gamètes, et à des "
                "glandes annexes, qui produisent des liquides nourriciers et "
                "protecteurs. Chez l'homme, le testicule est relié aux "
                "épididymes, aux canaux déférents, aux canaux éjaculateurs et "
                "à l'urètre, avec les vésicules séminales et la prostate comme "
                "glandes annexes. Chez la femme, l'ovaire est relié aux "
                "trompes de Fallope, à l'utérus et au vagin, avec les glandes "
                "vulvo-vaginales comme glandes annexes."
            )
        ) as tracker:
            self.play(FadeIn(entete_tableau))
            self.play(FadeIn(masc))
            self.play(FadeIn(fem))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tableau), FadeOut(tableau))

        # --- Vocabulaire : gamète, caractères primaires/secondaires -------
        entete_vocab = Text("Vocabulaire à connaître", font_size=27, color=YELLOW, weight="BOLD")
        entete_vocab.next_to(titre, DOWN, buff=0.5)

        vocab = _bullets(
            [
                "Gamète : cellule reproductrice haploïde (n=23). Le "
                "spermatozoïde (petit, mobile) est le gamète mâle ; l'ovule "
                "(gros, immobile) est le gamète femelle.",
                "Caractères sexuels primaires : les organes génitaux "
                "eux-mêmes, présents dès la naissance.",
                "Caractères sexuels secondaires : les traits qui "
                "apparaissent à la puberté sous l'action des hormones "
                "(voix grave, barbe, seins, pilosité...).",
            ],
            font_size=23,
            width=52,
        )
        vocab.next_to(entete_vocab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux mots de vocabulaire sont essentiels. Le gamète est une "
                "cellule reproductrice haploïde, à vingt-trois chromosomes : "
                "le spermatozoïde, petit et mobile, chez l'homme ; l'ovule, "
                "gros et immobile, chez la femme. Les caractères sexuels "
                "primaires sont les organes génitaux eux-mêmes, présents dès "
                "la naissance. Les caractères sexuels secondaires sont les "
                "traits qui apparaissent ou s'accentuent à la puberté sous "
                "l'action des hormones : voix grave et barbe chez le garçon, "
                "seins et élargissement du bassin chez la fille."
            )
        ) as tracker:
            self.play(FadeIn(entete_vocab))
            self.play(FadeIn(vocab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_vocab), FadeOut(vocab))

        # --- Exemple traité : classement des caractères -------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Classons : barbe, trompes de Fallope, seins développés, "
                    "vagin, voix grave, testicules. Présents dès la "
                    "naissance -> primaires : trompes, vagin, testicules. "
                    "Apparus à la puberté -> secondaires : barbe, seins, "
                    "voix grave.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Prenons un exemple : classons la barbe, les trompes de "
                "Fallope, les seins développés, le vagin, la voix grave et "
                "les testicules. Les trompes, le vagin et les testicules sont "
                "des organes formés avant la naissance : ce sont des "
                "caractères sexuels primaires. La barbe, les seins développés "
                "et la voix grave apparaissent à la puberté : ce sont des "
                "caractères sexuels secondaires."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : méthode pour distinguer primaire / secondaire ----
        methode = method_box(
            Text(
                _wrap(
                    "Étape 1 : le caractère est-il présent dès la "
                    "naissance ? Si oui, il est primaire. Étape 2 : "
                    "apparaît-il ou s'accentue-t-il à la puberté ? Alors il "
                    "est secondaire. Étape 3 : pour vérifier, observer "
                    "l'effet d'une castration - un caractère secondaire "
                    "régresse, car il dépend des hormones des gonades.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Pour distinguer un caractère sexuel primaire d'un caractère "
                "secondaire, procédons en trois étapes. Étape un : le "
                "caractère est-il présent dès la naissance ? Si oui, c'est un "
                "caractère primaire. Étape deux : apparaît-il ou s'accentue-t-"
                "il à la puberté ? Alors c'est un caractère secondaire. Étape "
                "trois, pour vérifier : on observe ce qui se passe après une "
                "castration ; un caractère secondaire régresse, car il dépend "
                "des hormones produites par les gonades."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : gonade vs gamète -----------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez jamais « gonade » et « gamète ». La gonade "
                    "est un organe (testicule, ovaire) ; le gamète est une "
                    "cellule produite par cet organe (spermatozoïde, "
                    "ovule). Les voies génitales transportent les gamètes, "
                    "jamais les hormones.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne jamais confondre gonade et gamète : la gonade "
                "est un organe, le testicule ou l'ovaire ; le gamète est une "
                "cellule produite par cet organe, le spermatozoïde ou "
                "l'ovule. Autre confusion fréquente : les voies génitales, "
                "comme les canaux déférents ou les trompes, transportent les "
                "gamètes, jamais les hormones."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
