"""
scenes/Maths_GeneralitesFonctions_11.py — Chapitre 3 (1ereC, Maths), scène 11.

Fonctions associées et leurs courbes (translations, symétrie, valeur
absolue), exemple traité à partir de la parabole f(x) = x², puis synthèse
méthodologique du chapitre (6 method_box) et pièges classiques
(3 warning_box), conclue par un essentiel_box récapitulatif.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class FonctionsAssocieesSynthese(NotionScene):
    def construct(self):
        titre = scene_title("Fonctions associées et courbes — synthèse")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : tableau des transformations -----------------------
        theo_transfo = theorem_box(
            MathTex(
                r"""
                \begin{array}{ll}
                f(x)+k & \text{translation verticale de vecteur } k\vec{\jmath} \\
                f(x-a) & \text{translation horizontale de vecteur } a\vec{\imath} \\
                -f(x)  & \text{symétrie par rapport à l'axe des abscisses} \\
                |f(x)| & \text{repliement : partie négative reflétée vers le haut}
                \end{array}
                """,
                font_size=23,
            ),
            box_width=11.4,
        )
        theo_transfo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quatre transformations usuelles à connaître. f de x plus "
                "k : translation verticale de vecteur k fois le vecteur j. "
                "f de x moins a : translation horizontale de vecteur a "
                "fois le vecteur i. Moins f de x : symétrie par rapport à "
                "l'axe des abscisses. Et valeur absolue de f de x : "
                "repliement, la partie négative de la courbe est reflétée "
                "vers le haut."
            )
        ) as tracker:
            self.play(FadeIn(theo_transfo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_transfo))

        demos = example_box(
            Text(
                _wrap(
                    "Démonstrations courtes : M(x;f(x)+k) = translaté de "
                    "M(x;f(x)) par k·j. M(x;f(x-a)) : poser X=x-a, le point "
                    "(X+a ; f(X)) est translaté de a·i. M(x;-f(x)) = "
                    "symétrique de M(x;f(x)) par rapport à (Ox). "
                    "|f(x)| = f(x) si f(x)≥0, sinon -f(x) : la courbe "
                    "coïncide avec Cf en haut, avec son symétrique en bas.",
                    width=58,
                ),
                font_size=20,
            ),
            box_width=11.4,
        )
        demos.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Justification rapide de chaque cas : ajouter k décale "
                "chaque point verticalement de k. Remplacer x par x moins "
                "a, en posant X égale x moins a, décale chaque point "
                "horizontalement de a. Prendre l'opposé change le signe de "
                "l'ordonnée, donc symétrise par rapport à l'axe des "
                "abscisses. Et la valeur absolue laisse la courbe "
                "inchangée là où f est positive, et la reflète vers le "
                "haut là où f est négative."
            )
        ) as tracker:
            self.play(FadeIn(demos))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demos))

        # --- Exemple traité 12 : à partir de f(x) = x² -----------------------
        enonce_ex12 = Text(
            "Exemple 12 — à partir de f(x) = x², construire g, h, k, m",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex12.next_to(titre, DOWN, buff=0.45)

        formules_ex12 = MathTex(
            r"g(x)=x^2-2 \quad h(x)=(x+1)^2 \quad k(x)=-x^2 \quad m(x)=|x^2-2|",
            font_size=24,
        )
        formules_ex12.next_to(enonce_ex12, DOWN, buff=0.3)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 4, 1],
            x_length=8.5,
            y_length=4.0,
            axis_config={"color": WHITE, "font_size": 14},
        )
        axes.next_to(formules_ex12, DOWN, buff=0.3)

        courbe_f = axes.plot(lambda x: x**2, x_range=[-1.9, 1.9], color=WHITE)
        courbe_g = axes.plot(lambda x: x**2 - 2, x_range=[-2.15, 2.15], color=YELLOW)
        courbe_h = axes.plot(lambda x: (x + 1) ** 2, x_range=[-2.9, 0.9], color="#59B4FF")
        courbe_k = axes.plot(lambda x: -(x**2), x_range=[-1.9, 1.9], color="#E06666")
        schema = VGroup(axes, courbe_f, courbe_g, courbe_h, courbe_k)

        with self.voiceover(
            text=(
                "Exemple 12 : partons de la parabole f de x égale x carré, "
                "en blanc, et construisons quatre fonctions associées. g "
                "de x égale x carré moins deux, en jaune, translate la "
                "parabole de deux vers le bas. h de x égale x plus un au "
                "carré, en bleu, translate la parabole d'une unité vers la "
                "gauche. Et k de x égale moins x carré, en rouge, "
                "symétrise la parabole par rapport à l'axe des abscisses."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex12))
            self.play(Write(formules_ex12))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex12), FadeOut(formules_ex12), FadeOut(schema))

        axes2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            x_length=7.5,
            y_length=3.4,
            axis_config={"color": WHITE, "font_size": 14},
        )
        axes2.next_to(titre, DOWN, buff=0.6)
        courbe_m = axes2.plot(lambda x: abs(x**2 - 2), x_range=[-2.15, 2.15], color="#7DDA58")
        legende_m = MathTex(r"m(x) = |x^2-2|", font_size=26, color="#7DDA58")
        legende_m.next_to(axes2, RIGHT, buff=0.3)
        schema_m = VGroup(axes2, courbe_m, legende_m)

        with self.voiceover(
            text=(
                "Enfin, m de x égale la valeur absolue de x carré moins "
                "deux replie vers le haut la partie de la courbe de g qui "
                "était sous l'axe des abscisses, entre moins racine de "
                "deux et racine de deux : on obtient une courbe formée de "
                "deux arcs se rejoignant sur l'axe des abscisses."
            )
        ) as tracker:
            self.play(FadeIn(schema_m))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_m))

        # --- Synthèse méthodologique : 6 method_box ------------------------
        synthese_titre = Text("Synthèse — les 6 méthodes du chapitre", font_size=26, color=YELLOW, weight="BOLD")
        synthese_titre.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text="Récapitulons maintenant les six méthodes clés de ce chapitre."
        ) as tracker:
            self.play(FadeIn(synthese_titre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(synthese_titre))

        methodes = [
            (
                "1. Déterminer Df",
                "Combiner « dénominateur ≠ 0 » et « expression sous une racine ≥ 0 » avec un « et ».",
                "Pour trouver Df, on combine dénominateur différent de zéro et expression sous une racine positive ou nulle, avec un « et ».",
            ),
            (
                "2. Prouver la monotonie sans dérivée",
                "Étudier le signe du taux de variation τ(a,b) = (f(b)−f(a))/(b−a) après factorisation.",
                "Pour prouver la monotonie sans dérivée, on étudie le signe du taux de variation, après factorisation de f de b moins f de a.",
            ),
            (
                "3. Prouver que f est bornée",
                "Passer par la forme canonique (second degré) ou majorer/minorer chaque terme séparément.",
                "Pour prouver que f est bornée, on passe par la forme canonique pour un second degré, ou on majore et minore chaque terme séparément.",
            ),
            (
                "4. Composer et étudier g∘f",
                "Calculer g(f(x)), déterminer Dg∘f, puis appliquer le tableau des 4 cas de sens de variation.",
                "Pour étudier une composée, on calcule g de f de x, on détermine son domaine, puis on applique le tableau des quatre cas de sens de variation.",
            ),
            (
                "5. Démontrer une bijection et trouver f⁻¹",
                "Prouver la stricte monotonie sur I, puis résoudre y=f(x) en x pour obtenir f⁻¹.",
                "Pour démontrer une bijection et trouver sa réciproque, on prouve la stricte monotonie sur l'intervalle, puis on résout y égale f de x en x.",
            ),
            (
                "6. Construire des courbes associées",
                "Repérer k (vertical), a (horizontal), le signe (symétrie), ou | | (repliement) dans l'écriture de la fonction.",
                "Pour construire des courbes associées, on repère dans l'écriture de la fonction le décalage vertical, le décalage horizontal, un signe moins, ou une valeur absolue.",
            ),
        ]

        for titre_m, resume_m, narration_m in methodes:
            boite = method_box(
                Text(f"{titre_m}\n{_wrap(resume_m, width=54)}", font_size=21),
                box_width=11.0,
            )
            boite.next_to(titre, DOWN, buff=0.55)
            with self.voiceover(text=narration_m) as tracker:
                self.play(FadeIn(boite))
                self.wait(tracker.get_remaining_duration())
            self.play(FadeOut(boite))

        # --- Pièges à éviter : 3 warning_box ---------------------------------
        pieges = [
            (
                "Piège 1 — parité sans vérifier le domaine",
                "Toujours vérifier que Df est symétrique par rapport à 0 AVANT de calculer f(−x).",
                "Premier piège : ne jamais tester la parité sans d'abord vérifier que le domaine est symétrique par rapport à zéro.",
            ),
            (
                "Piège 2 — majorant n'est pas maximum",
                "Un majorant n'est un maximum que s'il est effectivement ATTEINT par f en un point de Df.",
                "Deuxième piège : un majorant n'est un maximum que s'il est effectivement atteint par la fonction en un point de son domaine.",
            ),
            (
                "Piège 3 — réciproque et bijection",
                "f⁻¹ n'existe que si f est bijective ; ne pas confondre f⁻¹(x) avec 1/f(x).",
                "Troisième piège : la réciproque f moins un n'existe que si f est bijective, et il ne faut jamais la confondre avec l'inverse un sur f de x.",
            ),
        ]

        for titre_p, resume_p, narration_p in pieges:
            boite = warning_box(
                Text(f"{titre_p}\n{_wrap(resume_p, width=54)}", font_size=21),
                box_width=11.0,
            )
            boite.next_to(titre, DOWN, buff=0.55)
            with self.voiceover(text=narration_p) as tracker:
                self.play(FadeIn(boite))
                self.wait(tracker.get_remaining_duration())
            self.play(FadeOut(boite))

        # --- Essentiel à retenir : récapitulatif final -----------------------
        recap = essentiel_box(
            Text(
                _wrap(
                    "Ce chapitre : Df et image/antécédent, parité et "
                    "périodicité, sens de variation par le taux, "
                    "extremums/majorant/minorant, composition, restriction "
                    "et prolongement, bijection et réciproque, courbes "
                    "associées. Ce sont les fondations de toute étude de "
                    "fonction à venir.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.4,
        )
        recap.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de ce chapitre : l'ensemble de "
                "définition et la notion d'image et d'antécédent, la "
                "parité et la périodicité, le sens de variation par le "
                "signe du taux de variation, les extremums, majorants et "
                "minorants, la composition de fonctions, la restriction et "
                "le prolongement, la bijection et la fonction réciproque, "
                "et enfin les courbes de fonctions associées. Ces notions "
                "sont les fondations sur lesquelles reposera toute étude "
                "de fonction dans les chapitres suivants."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(recap))
