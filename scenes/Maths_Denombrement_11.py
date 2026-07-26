"""
scenes/Maths_Denombrement_11.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 11.

§ Modélisation des tirages : situation type (urne de 12 boules, tirer 3),
3 types de tirage (avec remise → p-liste nᵖ ; sans remise → arrangement
Aₙᵖ ; simultané → combinaison (n p)), tableau récapitulatif. Exemple
résolu 8 (urne 5 rouges/4 vertes/3 blanches, tirage simultané de 3, « au
moins une blanche » et « au plus deux couleurs »). 4 method_box et 4
warning_box. essentiel_box récapitulatif final du chapitre.
Source : 1ereC/Maths.pdf, chapitre 6, pages 77-79.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ModelisationTirages(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Modélisation des tirages")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : situation type -------------------------------------------------
        situation = Text(
            _wrap(
                "Situation type : une urne contient 12 boules. On en "
                "tire 3. Selon la façon de tirer, le nombre de résultats "
                "possibles change complètement — c'est tout l'enjeu de "
                "cette dernière notion.",
                width=54,
            ),
            font_size=23,
        )
        situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par la modélisation des tirages, "
                "l'application la plus fréquente du dénombrement. "
                "Situation type : une urne contient 12 boules, et l'on en "
                "tire 3. Selon la façon exacte de réaliser ce tirage, le "
                "nombre de résultats possibles change complètement. "
                "Voyons les trois cas."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(situation))

        # --- Raisonnement : les 3 types de tirage + tableau récapitulatif -----------
        type1_titre = Text("1) Tirage successif AVEC remise", font_size=22, weight="BOLD", color="#1E5FA8")
        type1_formule = MathTex(r"\text{ordonné, répétitions possibles} \ \to\ n^{p} \ \text{p-liste}", font_size=22)
        type1 = VGroup(type1_titre, type1_formule).arrange(DOWN, buff=0.15)

        type2_titre = Text("2) Tirage successif SANS remise", font_size=22, weight="BOLD", color="#A42A5A")
        type2_formule = MathTex(r"\text{ordonné, sans répétition} \ \to\ A_n^{p} \ \text{arrangement}", font_size=22)
        type2 = VGroup(type2_titre, type2_formule).arrange(DOWN, buff=0.15)

        type3_titre = Text("3) Tirage SIMULTANÉ", font_size=22, weight="BOLD", color="#288073")
        type3_formule = MathTex(r"\text{non ordonné, sans répétition} \ \to\ \binom{n}{p} \ \text{combinaison}", font_size=22)
        type3 = VGroup(type3_titre, type3_formule).arrange(DOWN, buff=0.15)

        tableau = VGroup(type1, type2, type3).arrange(DOWN, buff=0.4)
        tableau.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Premier cas : le tirage successif avec remise. On tire "
                "une boule, on note sa couleur, puis on la remet dans "
                "l'urne avant de tirer la suivante. Le résultat est "
                "ordonné, et les répétitions sont possibles : c'est une "
                "p-liste, le nombre de résultats est n puissance p. "
                "Deuxième cas : le tirage successif sans remise. On tire "
                "une boule, on la garde de côté, puis on tire la "
                "suivante parmi les boules restantes. Le résultat est "
                "ordonné, sans répétition : c'est un arrangement, A-n-p. "
                "Troisième cas : le tirage simultané. On saisit "
                "directement p boules d'un coup, en une seule poignée. "
                "Le résultat n'est pas ordonné : c'est une combinaison, n "
                "choisir p."
            )
        ) as tracker:
            self.play(Write(type1))
            self.play(Write(type2))
            self.play(Write(type3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Exemple traité : urne colorée, tirage simultané -----------------------
        enonce_urne = Text(
            _wrap(
                "Exemple résolu 8 : une urne contient 5 boules rouges, 4 "
                "vertes et 3 blanches (12 boules). On tire simultanément "
                "3 boules.",
                width=54,
            ),
            font_size=23,
        )
        enonce_urne.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Passons à l'exemple résolu 8. Une urne contient 5 boules "
                "rouges, 4 vertes et 3 blanches, soit 12 boules en tout. "
                "On en tire simultanément 3. Posons deux questions "
                "classiques."
            )
        ) as tracker:
            self.play(FadeIn(enonce_urne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_urne))

        total_tirages = MathTex(r"\text{Total des tirages : } \binom{12}{3} = 220", font_size=25)
        total_tirages.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le nombre total de tirages simultanés de 3 boules parmi "
                "les 12 est 12 choisir 3, soit 220."
            )
        ) as tracker:
            self.play(Write(total_tirages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(total_tirages))

        # Question a) au moins une blanche : disjonction puis complémentaire
        q1_titre = Text("« Au moins une boule blanche » — par disjonction", font_size=21, weight="BOLD")
        q1_calc1 = MathTex(
            r"1\text{ blanche}: \binom{3}{1}\binom{9}{2}=3\times 36=108 \quad"
            r"2\text{ blanches}: \binom{3}{2}\binom{9}{1}=3\times 9=27",
            font_size=18,
        )
        q1_calc2 = MathTex(r"3\text{ blanches}: \binom{3}{3}\binom{9}{0}=1", font_size=18)
        q1_calc3 = MathTex(r"108+27+1 = 136", font_size=23, color=YELLOW)
        q1 = VGroup(q1_titre, q1_calc1, q1_calc2, q1_calc3).arrange(DOWN, buff=0.22)
        q1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première question : combien de tirages contiennent au "
                "moins une boule blanche ? Par disjonction, on distingue "
                "les tirages avec exactement 1 blanche, avec exactement 2 "
                "blanches, et avec exactement 3 blanches. On calcule "
                "chaque cas séparément : 3 choisir 1 fois 9 choisir 2, "
                "égale 108. Puis 3 choisir 2 fois 9 choisir 1, égale 27. "
                "Puis 3 choisir 3 fois 9 choisir 0, égale 1. En "
                "additionnant : 108 plus 27 plus 1, égale 136."
            )
        ) as tracker:
            self.play(Write(q1_titre))
            self.play(Write(q1_calc1))
            self.play(Write(q1_calc2))
            self.play(Write(q1_calc3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(q1))

        q1b_titre = Text("Même question — par complémentaire (plus rapide)", font_size=21, weight="BOLD")
        q1b_calc = MathTex(
            r"\overline{\text{« au moins une blanche »}} = \text{« aucune blanche »} = \binom{9}{3} = 84",
            font_size=21,
        )
        q1b_calc2 = MathTex(r"220 - 84 = 136 \ \checkmark", font_size=25, color=YELLOW)
        q1b = VGroup(q1b_titre, q1b_calc, q1b_calc2).arrange(DOWN, buff=0.28)
        q1b.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "On retrouve le même résultat, bien plus vite, en passant "
                "par le complémentaire. Le complémentaire de « au moins "
                "une blanche » est « aucune blanche », c'est-à-dire "
                "choisir les 3 boules uniquement parmi les 9 non "
                "blanches : 9 choisir 3, égale 84. Il suffit alors de "
                "soustraire au total : 220 moins 84, égale 136. On "
                "retrouve exactement le même résultat, avec beaucoup "
                "moins de calculs."
            )
        ) as tracker:
            self.play(Write(q1b_titre))
            self.play(Write(q1b_calc))
            self.play(Write(q1b_calc2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(q1b))

        # Question b) au plus deux couleurs : complémentaire
        q2_titre = Text("« Au plus deux couleurs » — par complémentaire", font_size=21, weight="BOLD")
        q2_calc1 = MathTex(
            r"\overline{\text{« au plus 2 couleurs »}} = \text{« les 3 couleurs présentes »}",
            font_size=21,
        )
        q2_calc2 = MathTex(
            r"\binom{5}{1}\binom{4}{1}\binom{3}{1} = 5\times 4\times 3 = 60",
            font_size=23,
        )
        q2_calc3 = MathTex(r"220 - 60 = 160", font_size=25, color=YELLOW)
        q2 = VGroup(q2_titre, q2_calc1, q2_calc2, q2_calc3).arrange(DOWN, buff=0.28)
        q2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième question : combien de tirages contiennent au "
                "plus deux couleurs différentes ? Le complémentaire de "
                "« au plus deux couleurs » est « les trois couleurs sont "
                "présentes », c'est-à-dire exactement une boule de chaque "
                "couleur. Cela se compte par le principe multiplicatif : "
                "5 choisir 1, fois 4 choisir 1, fois 3 choisir 1, égale 5 "
                "fois 4 fois 3, soit 60. Il reste à soustraire au total : "
                "220 moins 60, égale 160 tirages avec au plus deux "
                "couleurs."
            )
        ) as tracker:
            self.play(Write(q2_titre))
            self.play(Write(q2_calc1))
            self.play(Write(q2_calc2))
            self.play(Write(q2_calc3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(q2))

        # --- À retenir : 4 method_box -------------------------------------------------
        meth1 = method_box(
            VGroup(
                Text("Méthode — Bien poser le problème", font_size=20, weight="BOLD"),
                Text(
                    _wrap("Se poser 3 questions : Avec ou sans remise ? Ordonné ou pas ? Successif ou simultané ?", width=46),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        meth1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avant de conclure, retenons quatre méthodes et quatre "
                "pièges. Méthode 1 : bien poser le problème en se posant "
                "trois questions. Le tirage se fait-il avec ou sans "
                "remise ? Le résultat est-il ordonné ou non ? Le tirage "
                "est-il successif ou simultané ? Ces trois réponses "
                "déterminent immédiatement la formule à utiliser."
            )
        ) as tracker:
            self.play(FadeIn(meth1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth1))

        meth2 = method_box(
            VGroup(
                Text("Méthode — Traduire les mots-clés", font_size=20, weight="BOLD"),
                Text(
                    _wrap('« équipe », « poignée », « ensemble » → simultané. « code », « rang », « podium » → ordonné.', width=46),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        meth2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode 2 : traduire les mots-clés de l'énoncé. Les mots "
                "« équipe », « poignée », « ensemble » signalent un "
                "tirage simultané, donc une combinaison. Les mots "
                "« code », « rang », « podium », « classement » "
                "signalent un tirage ordonné, donc une p-liste ou un "
                "arrangement."
            )
        ) as tracker:
            self.play(FadeIn(meth2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth2))

        meth3 = method_box(
            VGroup(
                Text("Méthode — « au moins un »", font_size=20, weight="BOLD"),
                Text(_wrap('« au moins un » → passer systématiquement au complémentaire, en général bien plus simple.', width=46), font_size=19),
            ).arrange(DOWN, buff=0.2),
        )
        meth3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode 3 : dès que l'énoncé contient « au moins un », "
                "le réflexe à avoir est de passer systématiquement au "
                "complémentaire, comme nous venons de le voir sur la "
                "boule blanche : c'est presque toujours plus simple que "
                "la disjonction directe."
            )
        ) as tracker:
            self.play(FadeIn(meth3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth3))

        meth4 = method_box(
            VGroup(
                Text("Méthode — « et » / « ou »", font_size=20, weight="BOLD"),
                Text(_wrap('« et » (choix indépendants) → on MULTIPLIE. « ou » (cas disjoints) → on ADDITIONNE.', width=46), font_size=19),
            ).arrange(DOWN, buff=0.2),
        )
        meth4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode 4, enfin : le mot « et », entre deux choix "
                "indépendants, signale une multiplication. Le mot « ou », "
                "entre deux cas qui s'excluent, signale une addition."
            )
        ) as tracker:
            self.play(FadeIn(meth4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth4))

        # --- Pièges à éviter : 4 warning_box --------------------------------------
        piege1 = warning_box(
            VGroup(
                Text("Piège 1 — Confondre Aₙᵖ et (n p)", font_size=20, weight="BOLD"),
                MathTex(r"A_n^p \text{ compte l'ORDRE} \quad\neq\quad \binom{n}{p} \text{ l'ignore}", font_size=21),
            ).arrange(DOWN, buff=0.2),
        )
        piege1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège 1 : ne jamais confondre A-n-p et n choisir p. "
                "L'arrangement A-n-p tient compte de l'ordre, la "
                "combinaison n choisir p l'ignore complètement — une "
                "confusion entre les deux fausse tous les calculs."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            VGroup(
                Text("Piège 2 — Ne pas tout développer", font_size=20, weight="BOLD"),
                MathTex(r"\binom{n}{p} = \dfrac{n!}{p!\,(n-p)!}\ : \text{ 2 factorielles au dénominateur}", font_size=21),
                Text(_wrap("Toujours SIMPLIFIER avant de développer n! entièrement (surtout si n est grand).", width=46), font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        piege2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège 2 : la formule n choisir p comporte deux "
                "factorielles au dénominateur, p factorielle et n moins p "
                "factorielle. Ne développez jamais n factorielle "
                "entièrement pour n grand : simplifiez d'abord, comme "
                "nous l'avons fait pour 15 choisir 6 ou 20 choisir 18, "
                "sous peine de calculs interminables."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            VGroup(
                Text("Piège 3 — Anagrammes avec lettres répétées", font_size=20, weight="BOLD"),
                Text(_wrap("Toujours DIVISER par la factorielle du nombre de répétitions de chaque lettre.", width=46), font_size=19),
            ).arrange(DOWN, buff=0.2),
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège 3, déjà rencontré : pour les anagrammes d'un mot "
                "avec des lettres répétées, comme BAOBAB, il faut "
                "toujours diviser par la factorielle du nombre de "
                "répétitions de chaque lettre, sinon on surcompte les "
                "mots identiques."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            VGroup(
                Text("Piège 4 — Signes alternés dans (a−b)ⁿ", font_size=20, weight="BOLD"),
                MathTex(r"(a-b)^n = \sum_{p=0}^n \binom{n}{p} a^{n-p}(-b)^p = \sum_{p=0}^n (-1)^p\binom{n}{p}a^{n-p}b^p", font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        piege4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège 4, enfin : dans le développement de a moins b, "
                "exposant n, n'oubliez jamais le facteur moins 1 "
                "puissance p, qui alterne les signes plus et moins terme "
                "après terme, comme on l'a vu avec 2x moins 1 au cube."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- L'essentiel à retenir : récapitulatif du chapitre ------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre Dénombrement", font_size=22, weight="BOLD"),
                MathTex(r"\text{p-listes : } n^{p} \qquad \text{Arrangements : } A_n^p = \dfrac{n!}{(n-p)!}", font_size=20),
                MathTex(r"\text{Permutations : } n! \qquad \text{Combinaisons : } \binom{n}{p} = \dfrac{n!}{p!(n-p)!}", font_size=20),
                MathTex(r"\text{Pascal : } \binom{n}{p}=\binom{n-1}{p-1}+\binom{n-1}{p} \qquad \binom{n}{p}=\binom{n}{n-p}", font_size=19),
                MathTex(r"\text{Binôme : } (a+b)^n = \sum_{p=0}^{n}\binom{n}{p}a^{n-p}b^{p}", font_size=20),
                MathTex(r"\text{Tirages : avec remise } n^p,\ \text{ sans remise } A_n^p,\ \text{ simultané } \binom{n}{p}", font_size=19),
            ).arrange(DOWN, buff=0.22),
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, voici l'essentiel à retenir. "
                "Les p-listes se comptent avec n puissance p. Les "
                "arrangements avec A-n-p, égal à n factorielle sur n "
                "moins p factorielle. Les permutations avec n factorielle. "
                "Les combinaisons avec n choisir p, égal à n factorielle "
                "sur p factorielle fois n moins p factorielle. Le "
                "triangle de Pascal repose sur la formule de récurrence "
                "et la symétrie des coefficients. La formule du binôme de "
                "Newton développe a plus b puissance n grâce à ces mêmes "
                "coefficients. Et pour les tirages dans une urne : avec "
                "remise, n puissance p ; sans remise, A-n-p ; simultané, "
                "n choisir p. Avec ces outils, vous êtes prêts à résoudre "
                "tous les problèmes de dénombrement du programme."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
