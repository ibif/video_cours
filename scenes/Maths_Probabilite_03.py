"""
scenes/Maths_Probabilite_03.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 03.

§ Opérations sur les événements : intersection A∩B, réunion A∪B,
événement contraire Ā (A∪Ā=Ω, A∩Ā=∅), événements incompatibles
(A∩B=∅). Piège : contraires ⟹ incompatibles, mais la réciproque est
fausse (contre-exemple « obtenir 1 » et « obtenir 2 »). Tableau
langage courant / notation ensembliste. Exemple résolu : dé cubique,
A={2,4,6}, B={4,5,6}, C={1,3} — A∩B, A∪B, Ā, A∩C (A et C incompatibles).
Source : 1ereC/Maths.pdf, chapitre 12, pages 144-145.
"""

import textwrap

from manim import DOWN, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class OperationsEvenements(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Opérations sur les événements")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "« A et B », « A ou B », « non A » : le langage courant "
                "des événements se traduit directement en opérations sur "
                "les ensembles — intersection, réunion, complémentaire.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les phrases « A et B », « A ou B », « non A » que l'on "
                "rencontre dans les énoncés de probabilité se traduisent "
                "directement en opérations sur les ensembles : "
                "intersection, réunion, complémentaire. C'est ce que nous "
                "allons formaliser."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définitions ---------------------------------------
        def_inter_reunion = definition_box(
            VGroup(
                Text("Intersection et réunion", font_size=23, weight="BOLD"),
                MathTex(r"A \cap B \ : \ \text{« A ET B » sont réalisés simultanément}", font_size=22),
                MathTex(r"A \cup B \ : \ \text{« A OU B » (au moins l'un des deux) est réalisé}", font_size=22),
            ).arrange(DOWN, buff=0.25),
        )
        def_inter_reunion.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'intersection de A et B, notée A inter B, est "
                "l'événement « A et B », réalisé lorsque les deux "
                "événements se produisent simultanément. La réunion de A "
                "et B, notée A union B, est l'événement « A ou B », "
                "réalisé dès qu'au moins l'un des deux se produit."
            )
        ) as tracker:
            self.play(FadeIn(def_inter_reunion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_inter_reunion))

        def_contraire = definition_box(
            VGroup(
                Text("Événement contraire", font_size=23, weight="BOLD"),
                MathTex(r"\overline{A} \ : \ \text{« NON A », réalisé quand A ne l'est pas}", font_size=23),
                MathTex(r"A \cup \overline{A} = \Omega \qquad A \cap \overline{A} = \emptyset", font_size=25, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
        )
        def_contraire.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'événement contraire de A, noté A surmonté d'une barre, "
                "est l'événement « non A », réalisé exactement quand A ne "
                "l'est pas. Il vérifie deux propriétés fondamentales : la "
                "réunion de A et de son contraire redonne tout l'univers "
                "Ω, et leur intersection est toujours vide."
            )
        ) as tracker:
            self.play(FadeIn(def_contraire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_contraire))

        def_incompatibles = definition_box(
            VGroup(
                Text("Événements incompatibles", font_size=23, weight="BOLD"),
                MathTex(r"A \text{ et } B \text{ incompatibles} \ \Longleftrightarrow\ A \cap B = \emptyset", font_size=25),
                Text(
                    _wrap("A et B ne peuvent JAMAIS se réaliser en même temps.", width=44),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_incompatibles.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux événements A et B sont dits incompatibles lorsque "
                "leur intersection est vide : ils ne peuvent jamais se "
                "réaliser en même temps."
            )
        ) as tracker:
            self.play(FadeIn(def_incompatibles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_incompatibles))

        # --- Tableau langage courant / notation --------------------------------
        tableau_titre = Text("Langage courant ↔ notation ensembliste", font_size=24, weight="BOLD")
        lignes = VGroup(
            MathTex(r"\text{« A et B »} \ \to\ A \cap B", font_size=23),
            MathTex(r"\text{« A ou B »} \ \to\ A \cup B", font_size=23),
            MathTex(r"\text{« non A »} \ \to\ \overline{A}", font_size=23),
            MathTex(r"\text{« A implique B »} \ \to\ A \subset B", font_size=23),
            MathTex(r"\text{« A et B incompatibles »} \ \to\ A \cap B = \emptyset", font_size=23),
        ).arrange(DOWN, buff=0.2)
        tableau = VGroup(tableau_titre, lignes).arrange(DOWN, buff=0.35)
        tableau.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le tableau de correspondance à connaître par "
                "cœur : « A et B » se traduit par A inter B. « A ou B » "
                "par A union B. « non A » par A barre. « A implique B », "
                "c'est-à-dire A entraîne B, par A inclus dans B. Et « A "
                "et B incompatibles » par A inter B égale l'ensemble vide."
            )
        ) as tracker:
            self.play(Write(tableau_titre))
            self.play(Write(lignes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Exemple traité : dé cubique ----------------------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu : dé cubique, Ω={1;...;6}. "
                "A={2;4;6}, B={4;5;6}, C={1;3}.",
                width=54,
            ),
            font_size=23,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Appliquons cela sur le dé cubique. On pose A égale 2, 4, "
                "6, B égale 4, 5, 6, et C égale 1, 3."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calculs = VGroup(
            MathTex(r"A \cap B = \{4\,;\,6\}", font_size=27),
            MathTex(r"A \cup B = \{2\,;\,4\,;\,5\,;\,6\}", font_size=27),
            MathTex(r"\overline{A} = \{1\,;\,3\,;\,5\}", font_size=27),
            MathTex(r"A \cap C = \emptyset \ \Rightarrow\ A \text{ et } C \text{ incompatibles}", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.3)
        calculs.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'intersection A inter B contient les issues communes, 4 "
                "et 6. La réunion A union B contient toutes les issues des "
                "deux, soit 2, 4, 5, 6. Le contraire de A contient les "
                "issues qui ne sont pas dans A, soit 1, 3, 5. Enfin, A "
                "inter C est vide : A et C sont donc incompatibles, ils ne "
                "partagent aucune issue commune."
            )
        ) as tracker:
            self.play(Write(calculs[0]))
            self.play(Write(calculs[1]))
            self.play(Write(calculs[2]))
            self.play(Write(calculs[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calculs))

        # --- À retenir : exemple récapitulatif -----------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"A \text{ et } \overline{A} \text{ sont incompatibles ET partagent } \Omega.", font_size=22),
            ).arrange(DOWN, buff=0.22),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons que A et son contraire sont toujours "
                "incompatibles, et qu'ils partagent à eux deux tout "
                "l'univers Ω : c'est ce double lien qui rend le passage "
                "au contraire si utile en calcul de probabilité."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Contraires ⟹ incompatibles, PAS l'inverse", font_size=19, weight="BOLD"),
                MathTex(
                    r"\text{« obtenir 1 » et « obtenir 2 » : incompatibles, mais PAS contraires}",
                    font_size=20,
                ),
                Text(
                    _wrap("Leur réunion n'est pas Ω tout entier — il manque 3, 4, 5, 6.", width=46),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège classique à retenir : deux événements contraires "
                "sont toujours incompatibles, mais la réciproque est "
                "fausse. Sur notre dé, « obtenir 1 » et « obtenir 2 » sont "
                "incompatibles, ils ne peuvent pas se réaliser ensemble, "
                "mais ils ne sont pas contraires, car leur réunion ne "
                "redonne pas tout l'univers : il manque les issues 3, 4, "
                "5 et 6."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
