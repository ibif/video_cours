"""
scenes/Maths_Probabilite_08.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 08.

§ Variable aléatoire réelle et loi de probabilité : définition d'une
variable aléatoire X:Ω→ℝ, ensemble image X(Ω), notation (X=x_i).
Exemple résolu : deux pièces, X=nombre de Face obtenues, Ω={PP,PF,FP,FF},
X(Ω)={0,1,2}. Définition de la loi de probabilité (tableau x_i/P(X=x_i)),
vérification obligatoire somme des p_i=1. Reprise de l'exemple : loi de
X avec P(X=0)=1/4, P(X=1)=1/2, P(X=2)=1/4, diagramme en bâtons.
Source : 1ereC/Maths.pdf, chapitre 12, pages 150-151.
"""

import textwrap

from manim import DOWN, RIGHT, UP, WHITE, YELLOW, Axes, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _diagramme_batons() -> VGroup:
    """Diagramme en bâtons de la loi de X : P(X=0)=1/4, P(X=1)=1/2, P(X=2)=1/4."""
    axes = Axes(
        x_range=[-0.5, 2.5, 1],
        y_range=[0, 0.6, 0.25],
        x_length=5,
        y_length=2.6,
        axis_config={"color": WHITE, "include_tip": False, "font_size": 16},
    )
    valeurs = [0, 1, 2]
    probas = [0.25, 0.5, 0.25]
    fractions = [r"\tfrac{1}{4}", r"\tfrac{1}{2}", r"\tfrac{1}{4}"]
    batons = VGroup()
    for x, p, frac in zip(valeurs, probas, fractions):
        base = axes.c2p(x, 0)
        sommet = axes.c2p(x, p)
        barre = Line(base, sommet, color=YELLOW, stroke_width=6)
        label_x = MathTex(str(x), font_size=20).next_to(base, DOWN, buff=0.15)
        label_p = MathTex(frac, font_size=18).next_to(sommet, UP, buff=0.1)
        batons.add(barre, label_x, label_p)
    return VGroup(axes, batons)


class VariableAleatoireLoi(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Variable aléatoire et loi de probabilité")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Nous ouvrons ici une nouvelle partie du chapitre : au "
                "lieu de s'intéresser à un événement, on associe à "
                "chaque issue un NOMBRE — c'est une variable aléatoire.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous ouvrons maintenant une nouvelle partie du chapitre. "
                "Au lieu de s'intéresser uniquement à des événements, on "
                "associe désormais à chaque issue de l'expérience un "
                "nombre : c'est ce qu'on appelle une variable aléatoire."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition variable aléatoire -----------------------
        def_var = definition_box(
            VGroup(
                Text("Variable aléatoire réelle", font_size=23, weight="BOLD"),
                MathTex(r"X : \Omega \longrightarrow \mathbb{R}", font_size=27),
                Text(
                    _wrap("X associe à chaque issue de Ω un nombre réel. X(Ω) désigne l'ensemble des valeurs prises par X.", width=44),
                    font_size=21,
                ),
                MathTex(r"(X = x_i) \ : \ \text{« l'événement formé des issues où } X \text{ vaut } x_i \text{ »}", font_size=21),
            ).arrange(DOWN, buff=0.22),
        )
        def_var.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une variable aléatoire réelle X est une fonction qui "
                "associe à chaque issue de l'univers Ω un nombre réel. "
                "L'ensemble des valeurs effectivement prises par X se "
                "note X de Ω. Enfin, la notation X égale x-i désigne "
                "l'événement formé de toutes les issues où X prend "
                "exactement la valeur x-i."
            )
        ) as tracker:
            self.play(FadeIn(def_var))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_var))

        # --- Exemple : deux pièces, X = nombre de Face ---------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu : on lance deux pièces de monnaie "
                "équilibrées. On note X le nombre de Face obtenues.",
                width=52,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu : on lance deux pièces de monnaie "
                "équilibrées, et l'on note X le nombre de Face obtenues "
                "sur les deux lancers."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        univers_pieces = MathTex(r"\Omega = \{PP\,;\,PF\,;\,FP\,;\,FF\}", font_size=27)
        univers_pieces.next_to(titre, DOWN, buff=0.55)
        image_X = MathTex(r"X(PP)=0, \ \ X(PF)=X(FP)=1, \ \ X(FF)=2", font_size=23)
        image_X.next_to(univers_pieces, DOWN, buff=0.4)
        ensemble_image = MathTex(r"X(\Omega) = \{0\,;\,1\,;\,2\}", font_size=27, color=YELLOW)
        ensemble_image.next_to(image_X, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'univers est Ω égale P-P, P-F, F-P, F-F, où P désigne "
                "Pile et F désigne Face. On a X de P-P égale 0, X de P-F "
                "et X de F-P égale 1, et X de F-F égale 2. L'ensemble des "
                "valeurs prises par X, X de Ω, est donc 0, 1, 2."
            )
        ) as tracker:
            self.play(Write(univers_pieces))
            self.play(Write(image_X))
            self.play(FadeIn(ensemble_image))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(univers_pieces), FadeOut(image_X), FadeOut(ensemble_image))

        # --- Définition loi de probabilité ---------------------------------------
        def_loi = definition_box(
            VGroup(
                Text("Loi de probabilité de X", font_size=23, weight="BOLD"),
                Text(
                    _wrap("Définir la loi de X, c'est donner, pour chaque valeur x_i de X(Ω), la probabilité P(X=x_i) — souvent sous forme de tableau.", width=44),
                    font_size=21,
                ),
                MathTex(r"\text{Vérification OBLIGATOIRE : } \textstyle\sum_i P(X=x_i) = 1", font_size=23, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
        )
        def_loi.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Définir la loi de probabilité de X, c'est donner, pour "
                "chaque valeur x-i que X peut prendre, la probabilité P "
                "de X égale x-i, généralement présentée sous forme d'un "
                "tableau. Une vérification est absolument obligatoire "
                "avant de conclure : la somme de toutes ces probabilités "
                "doit toujours valoir exactement 1."
            )
        ) as tracker:
            self.play(FadeIn(def_loi))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_loi))

        # --- Reprise de l'exemple : loi de X + tableau ---------------------------
        calc_titre = Text("Loi de X (deux pièces équilibrées)", font_size=22, weight="BOLD")
        calc = VGroup(
            MathTex(r"P(X=0) = P(PP) = \dfrac{1}{4}", font_size=23),
            MathTex(r"P(X=1) = P(PF) + P(FP) = \dfrac{1}{4}+\dfrac{1}{4} = \dfrac{1}{2}", font_size=23),
            MathTex(r"P(X=2) = P(FF) = \dfrac{1}{4}", font_size=23),
        ).arrange(DOWN, buff=0.22)
        bloc_calc = VGroup(calc_titre, calc).arrange(DOWN, buff=0.3)
        bloc_calc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons notre exemple. L'univers étant équiprobable, "
                "chaque issue a probabilité 1 quart. P de X égale 0 "
                "correspond à la seule issue P-P, donc 1 quart. P de X "
                "égale 1 correspond à deux issues, P-F et F-P, donc 1 "
                "quart plus 1 quart, égale 1 demi. Et P de X égale 2 "
                "correspond à la seule issue F-F, donc 1 quart."
            )
        ) as tracker:
            self.play(Write(calc_titre))
            self.play(Write(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_calc))

        tableau_titre = Text("Tableau de la loi de X", font_size=22, weight="BOLD")
        ligne_x = MathTex(r"x_i", font_size=22)
        ligne_p = MathTex(r"P(X=x_i)", font_size=22)
        valeurs_x = VGroup(*[MathTex(v, font_size=22) for v in ["0", "1", "2"]]).arrange(RIGHT, buff=1.1)
        valeurs_p = VGroup(*[MathTex(v, font_size=22) for v in [r"\tfrac{1}{4}", r"\tfrac{1}{2}", r"\tfrac{1}{4}"]]).arrange(RIGHT, buff=1.1)
        ligne_x_group = VGroup(ligne_x, valeurs_x).arrange(RIGHT, buff=0.5)
        ligne_p_group = VGroup(ligne_p, valeurs_p).arrange(RIGHT, buff=0.5)
        tableau = VGroup(ligne_x_group, ligne_p_group).arrange(DOWN, buff=0.3)
        verif = MathTex(r"\tfrac{1}{4}+\tfrac{1}{2}+\tfrac{1}{4} = 1 \ \checkmark", font_size=24, color=YELLOW)
        bloc_tableau = VGroup(tableau_titre, tableau, verif).arrange(DOWN, buff=0.35)
        bloc_tableau.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On résume tout cela dans le tableau de la loi de X : en "
                "première ligne les valeurs x-i, 0, 1, 2 ; en seconde "
                "ligne les probabilités correspondantes, 1 quart, 1 demi, "
                "1 quart. On vérifie bien que la somme vaut 1, comme "
                "l'exige la définition."
            )
        ) as tracker:
            self.play(Write(tableau_titre))
            self.play(Write(tableau))
            self.play(FadeIn(verif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_tableau))

        # --- Diagramme en bâtons --------------------------------------------------
        diag_titre = Text("Représentation graphique : diagramme en bâtons", font_size=21, weight="BOLD")
        diagramme = _diagramme_batons()
        bloc_diag = VGroup(diag_titre, diagramme).arrange(DOWN, buff=0.35)
        bloc_diag.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La loi de X se représente aussi graphiquement par un "
                "diagramme en bâtons : la hauteur de chaque bâton, "
                "au-dessus de la valeur x-i, est proportionnelle à sa "
                "probabilité."
            )
        ) as tracker:
            self.play(Write(diag_titre))
            self.play(FadeIn(diagramme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_diag))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Regrouper les issues qui donnent la même valeur", font_size=18, weight="BOLD"),
                Text(
                    _wrap("P(X=1) = P(PF) + P(FP), PAS seulement P(PF) : PLUSIEURS issues peuvent donner la même valeur de X.", width=46),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège fréquent à éviter : pour calculer P de X égale 1, "
                "il ne faut pas oublier d'additionner TOUTES les issues "
                "qui donnent cette valeur, ici P-F et F-P, et non "
                "seulement l'une des deux. Plusieurs issues distinctes "
                "peuvent parfaitement donner la même valeur de X."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
