"""
scenes/Maths_Probabilite_05.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 05.

§ Équiprobabilité : définition (toutes les issues ont la même
probabilité 1/Card(Ω)), mots-clés qui la signalent (dé équilibré, pièce
non truquée, boules indiscernables, tirer au hasard). Théorème
P(A)=Card(A)/Card(Ω) = cas favorables/cas possibles, avec démonstration
courte. Exemple résolu : urne de 8 boules (4 rouges, 3 vertes, 1 noire),
P(R), P(V), P(N), P(D)=P(rouge ou verte) calculée de deux façons.
Source : 1ereC/Maths.pdf, chapitre 12, pages 147-148.
"""

import textwrap

from manim import DOWN, RIGHT, UP, WHITE, YELLOW, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _urne_boules(rouges: int, vertes: int, noires: int) -> VGroup:
    boules = VGroup()
    for _ in range(rouges):
        boules.add(Dot(radius=0.16, color="#B42E41"))
    for _ in range(vertes):
        boules.add(Dot(radius=0.16, color="#267540"))
    for _ in range(noires):
        boules.add(Dot(radius=0.16, color=WHITE))
    boules.arrange(RIGHT, buff=0.2)
    return boules


class Equiprobabilite(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Équiprobabilité")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Un dé « bien équilibré », une pièce « non truquée » : "
                "ces expressions signifient que toutes les issues ont "
                "exactement la même probabilité de se produire.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un dé « bien équilibré », une pièce « non truquée » : "
                "ces expressions, très fréquentes dans les énoncés, "
                "signifient que toutes les issues ont exactement la même "
                "probabilité de se produire. C'est ce qu'on appelle "
                "l'équiprobabilité."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition + mots-clés -----------------------------
        definition = definition_box(
            VGroup(
                Text("Situation d'équiprobabilité", font_size=23, weight="BOLD"),
                MathTex(r"\text{Toutes les issues ont la MÊME probabilité : } p_i = \dfrac{1}{\mathrm{Card}(\Omega)}", font_size=24),
            ).arrange(DOWN, buff=0.25),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On dit qu'il y a équiprobabilité lorsque toutes les "
                "issues de Ω ont la même probabilité, égale à 1 sur le "
                "cardinal de Ω."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        mots_cles_titre = Text("Mots-clés qui signalent l'équiprobabilité", font_size=23, weight="BOLD")
        mots_cles = Text(
            _wrap(
                "« dé équilibré », « pièce non truquée », « boules "
                "indiscernables au toucher », « tirer au hasard »",
                width=48,
            ),
            font_size=22,
        )
        bloc_mots = VGroup(mots_cles_titre, mots_cles).arrange(DOWN, buff=0.3)
        bloc_mots.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Certains mots-clés, dans un énoncé, signalent presque "
                "toujours une situation d'équiprobabilité : « dé "
                "équilibré », « pièce non truquée », « boules "
                "indiscernables au toucher », ou encore « tirer au "
                "hasard ». Il faut apprendre à les repérer immédiatement."
            )
        ) as tracker:
            self.play(Write(mots_cles_titre))
            self.play(Write(mots_cles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_mots))

        # --- Théorème : cas favorables / cas possibles --------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Probabilité en situation d'équiprobabilité", font_size=22, weight="BOLD"),
                MathTex(r"P(A) = \dfrac{\mathrm{Card}(A)}{\mathrm{Card}(\Omega)} = \dfrac{\text{nombre de cas favorables}}{\text{nombre de cas possibles}}", font_size=25),
            ).arrange(DOWN, buff=0.28),
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        demo = MathTex(
            r"P(A) = \sum_{e_i \in A} p_i = \sum_{e_i \in A} \dfrac{1}{\mathrm{Card}(\Omega)} = \dfrac{\mathrm{Card}(A)}{\mathrm{Card}(\Omega)}",
            font_size=23,
        )
        demo.next_to(theoreme, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "En situation d'équiprobabilité, la probabilité d'un "
                "événement A vaut le cardinal de A sur le cardinal de Ω, "
                "c'est-à-dire le nombre de cas favorables sur le nombre de "
                "cas possibles. Démonstration courte : P de A est la somme "
                "des p-i des issues de A ; chaque p-i valant 1 sur Card de "
                "Ω, on additionne Card de A fois ce même terme, ce qui "
                "donne directement Card de A sur Card de Ω."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme), FadeOut(demo))

        # --- Exemple traité : urne de 8 boules -------------------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu : une urne contient 8 boules "
                "indiscernables au toucher : 4 rouges, 3 vertes, 1 noire. "
                "On en tire une au hasard.",
                width=52,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.5)
        urne = _urne_boules(4, 3, 1)
        urne.next_to(enonce, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu : une urne contient 8 boules "
                "indiscernables au toucher, 4 rouges, 3 vertes et 1 noire. "
                "On en tire une au hasard."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.play(FadeIn(urne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce), FadeOut(urne))

        calcul1 = MathTex(
            r"P(R) = \dfrac{4}{8} = \dfrac{1}{2} \qquad P(V) = \dfrac{3}{8} \qquad P(N) = \dfrac{1}{8}",
            font_size=24,
        )
        calcul1.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le tirage étant au hasard parmi des boules "
                "indiscernables, il y a équiprobabilité. On a donc : P de "
                "R égale 4 huitièmes, soit un demi ; P de V égale 3 "
                "huitièmes ; et P de N égale 1 huitième."
            )
        ) as tracker:
            self.play(Write(calcul1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul1))

        # P(D) de deux façons
        methode1_titre = Text("P(D) = P(« rouge ou verte ») — méthode 1 : addition", font_size=20, weight="BOLD")
        methode1 = MathTex(r"D = R \cup V, \ \ R \cap V = \emptyset \ \Rightarrow\ P(D) = \dfrac{4}{8} + \dfrac{3}{8} = \dfrac{7}{8}", font_size=23)
        bloc1 = VGroup(methode1_titre, methode1).arrange(DOWN, buff=0.3)
        bloc1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Calculons maintenant P de D, la probabilité de tirer une "
                "boule rouge ou verte, de deux façons différentes. "
                "Première méthode, par addition : D est la réunion de R et "
                "V, deux événements incompatibles puisqu'une boule ne peut "
                "être à la fois rouge et verte. On additionne donc "
                "simplement : 4 huitièmes plus 3 huitièmes, égale 7 "
                "huitièmes."
            )
        ) as tracker:
            self.play(Write(methode1_titre))
            self.play(Write(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc1))

        methode2_titre = Text("Même calcul — méthode 2 : complémentaire", font_size=20, weight="BOLD")
        methode2 = MathTex(r"\overline{D} = N \ \Rightarrow\ P(D) = 1 - P(N) = 1 - \dfrac{1}{8} = \dfrac{7}{8}", font_size=23, color=YELLOW)
        bloc2 = VGroup(methode2_titre, methode2).arrange(DOWN, buff=0.3)
        bloc2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Deuxième méthode, par le complémentaire, souvent plus "
                "rapide : le contraire de D, « ni rouge ni verte », c'est "
                "exactement N, « noire ». On a donc P de D égale 1 moins P "
                "de N, égale 1 moins 1 huitième, égale 7 huitièmes. On "
                "retrouve bien le même résultat."
            )
        ) as tracker:
            self.play(Write(methode2_titre))
            self.play(Write(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc2))

        # --- À retenir -----------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"\text{Vérifier l'équiprobabilité AVANT toute chose.}", font_size=22),
                MathTex(r"\text{« au moins/ni l'un ni l'autre »} \to \text{souvent plus rapide par le complémentaire.}", font_size=20),
            ).arrange(DOWN, buff=0.22),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons deux réflexes. D'abord, toujours vérifier "
                "l'équiprobabilité avant d'appliquer la formule cas "
                "favorables sur cas possibles. Ensuite, dès qu'un énoncé "
                "évoque « au moins » ou « ni l'un ni l'autre », le passage "
                "par le complémentaire est souvent la voie la plus rapide."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap), FadeOut(titre))
