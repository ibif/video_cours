"""
scenes/Maths_StatistiqueUneVariable_01.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 01.

§ Population, individu, caractère statistique : définitions population /
individu / échantillon / effectif total N. Définition caractère statistique
et modalités : caractère QUALITATIF vs QUANTITATIF (discret / continu). Le
chapitre ne traite QUE les caractères quantitatifs. Exemples ivoiriens :
élèves du lycée moderne de Bouaké, sacs de cacao à Daloa, ménages de
Yamoussoukro.
Source : 1ereC/Maths.pdf, chapitre 17, pages 200-201.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class PopulationCaractereStatistique(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Population et caractère statistique")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Dernier chapitre de l'année : la statistique. Elle "
                "consiste à recueillir, organiser puis résumer des "
                "données chiffrées portant sur un ensemble d'individus, "
                "pour en tirer des informations utiles.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous abordons le dernier chapitre de l'année : la "
                "statistique à une variable. Faire de la statistique, "
                "c'est recueillir, organiser puis résumer des données "
                "chiffrées portant sur un ensemble d'individus, afin d'en "
                "tirer des informations utiles."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : population / individu / échantillon / N --------
        def_population = definition_box(
            VGroup(
                Text("Population, individu, échantillon", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "La POPULATION est l'ensemble sur lequel porte "
                        "l'étude. Chaque élément de cette population est "
                        "un INDIVIDU. Un ÉCHANTILLON est un "
                        "sous-ensemble de la population, choisi pour la "
                        "représenter.",
                        width=46,
                    ),
                    font_size=21,
                ),
                MathTex(r"N = \text{effectif total} = \text{nombre d'individus de la population}", font_size=22),
            ).arrange(DOWN, buff=0.25),
        )
        def_population.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La population est l'ensemble sur lequel porte l'étude "
                "statistique. Chaque élément de cette population est "
                "appelé un individu. Un échantillon est un sous-ensemble "
                "de la population, choisi pour la représenter quand on ne "
                "peut pas étudier tous les individus. On note N "
                "l'effectif total, c'est-à-dire le nombre d'individus de "
                "la population étudiée."
            )
        ) as tracker:
            self.play(FadeIn(def_population))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_population))

        def_caractere = definition_box(
            VGroup(
                Text("Caractère statistique et modalités", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Le CARACTÈRE (ou VARIABLE) statistique est "
                        "l'aspect étudié chez chaque individu. Les "
                        "valeurs qu'il peut prendre sont ses MODALITÉS.",
                        width=46,
                    ),
                    font_size=21,
                ),
                MathTex(
                    r"\text{QUALITATIF (non chiffré)} \quad / \quad \text{QUANTITATIF (chiffré)}",
                    font_size=22,
                ),
                MathTex(
                    r"\text{Quantitatif DISCRET (valeurs isolées)} \quad / \quad \text{CONTINU (intervalle)}",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_caractere.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le caractère, ou la variable statistique, est l'aspect "
                "précis que l'on étudie chez chaque individu. Les "
                "valeurs qu'il peut prendre s'appellent ses modalités. "
                "On distingue le caractère qualitatif, qui n'est pas "
                "chiffré, comme une couleur ou une profession, du "
                "caractère quantitatif, qui est chiffré. Ce dernier se "
                "divise en deux : discret, quand ses valeurs sont "
                "isolées, comme un nombre d'enfants ; et continu, quand "
                "ses valeurs remplissent un intervalle, comme une masse "
                "ou une taille. Ce chapitre ne traite QUE les caractères "
                "quantitatifs."
            )
        ) as tracker:
            self.play(FadeIn(def_caractere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_caractere))

        # --- Exemple traité : trois situations ivoiriennes -------------------
        enonce = Text(
            _wrap(
                "Trois situations pour s'entraîner à repérer population, "
                "individu et type de caractère.",
                width=54,
            ),
            font_size=23,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons trois situations concrètes pour s'entraîner à "
                "repérer la population, l'individu, et le type de "
                "caractère étudié."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        exemples = example_box(
            VGroup(
                Text("Trois exemples", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "1. Élèves du lycée moderne de Bouaké — "
                        "individu : un élève. Caractère : note de "
                        "mathématiques (quantitatif CONTINU).",
                        width=48,
                    ),
                    font_size=19,
                ),
                Text(
                    _wrap(
                        "2. Sacs de cacao pesés à Daloa — individu : un "
                        "sac. Caractère : masse en kg (quantitatif "
                        "CONTINU).",
                        width=48,
                    ),
                    font_size=19,
                ),
                Text(
                    _wrap(
                        "3. Ménages de Yamoussoukro — individu : un "
                        "ménage. Caractère : nombre d'enfants "
                        "(quantitatif DISCRET).",
                        width=48,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        exemples.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier exemple : les élèves du lycée moderne de "
                "Bouaké forment la population, un élève est un individu, "
                "et l'on peut étudier sa note de mathématiques, un "
                "caractère quantitatif continu. Deuxième exemple : les "
                "sacs de cacao pesés à Daloa, où un sac est un individu, "
                "et sa masse en kilogrammes est également un caractère "
                "quantitatif continu. Troisième exemple : les ménages de "
                "Yamoussoukro, où un ménage est un individu, et son "
                "nombre d'enfants est cette fois un caractère "
                "quantitatif discret, car il ne prend que des valeurs "
                "isolées : 0, 1, 2, 3, et ainsi de suite."
            )
        ) as tracker:
            self.play(Write(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples))

        # --- À retenir --------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(
                    r"\text{Population} \to \text{Individu} \to \text{Caractère} \to \text{Modalités}",
                    font_size=23,
                ),
                Text(
                    _wrap(
                        "Ce chapitre étudie exclusivement les caractères "
                        "QUANTITATIFS (discrets ou continus).",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la chaîne des notions : une population est "
                "constituée d'individus, chez qui l'on observe un "
                "caractère, qui prend différentes modalités. Et rappelons "
                "que ce chapitre étudie exclusivement les caractères "
                "quantitatifs, discrets ou continus."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Discret ou continu ?", font_size=20, weight="BOLD"),
                Text(
                    _wrap(
                        "Un nombre d'enfants (0, 1, 2, 3…) est DISCRET "
                        "même s'il est illimité. Une masse ou une taille "
                        "est CONTINUE même si on l'arrondit à l'affichage. "
                        "Le critère est la NATURE des valeurs possibles, "
                        "pas leur nombre.",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un piège fréquent : un nombre d'enfants, 0, 1, 2, 3 et "
                "ainsi de suite, reste discret même s'il n'y a pas de "
                "limite supérieure fixée. À l'inverse, une masse ou une "
                "taille reste continue même si on l'arrondit à "
                "l'affichage, par exemple à 71 kilogrammes. Le critère "
                "qui compte, c'est la nature des valeurs possibles — des "
                "valeurs isolées, ou tout un intervalle — jamais le "
                "nombre de valeurs observées."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
