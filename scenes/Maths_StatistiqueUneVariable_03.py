"""
scenes/Maths_StatistiqueUneVariable_03.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 03.

§ Regroupement en classes et histogramme : définition classe / amplitude /
centre. Remarque : hypothèse de répartition régulière (on remplace chaque
classe par son centre). Définition histogramme (aire proportionnelle à
l'effectif ; hauteur = effectif si amplitudes égales, hauteur = densité =
n_i / amplitude si amplitudes inégales). Exemple résolu 2 complet : 60 sacs
de cacao pesés à Daloa, 5 classes de masse (amplitude égale 5 kg),
histogramme.
Source : 1ereC/Maths.pdf, chapitre 17, pages 202-203.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, Axes, FadeIn, FadeOut, MathTex, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box

# --- Données de l'exemple résolu 2 (60 sacs de cacao pesés à Daloa) --------
# Classes de masse (kg), amplitude égale 5 kg.
BORNES = [60, 65, 70, 75, 80, 85]
EFFECTIFS = [4, 10, 24, 14, 8]
CENTRES = [62.5, 67.5, 72.5, 77.5, 82.5]
N_TOTAL = 60  # = sum(EFFECTIFS)


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _histogramme() -> VGroup:
    axes = Axes(
        x_range=[58, 87, 5],
        y_range=[0, 26, 5],
        x_length=8.5,
        y_length=3.4,
        axis_config={"color": WHITE, "include_tip": False, "font_size": 16},
    )
    barres = VGroup()
    for i in range(5):
        coin_bas_gauche = axes.c2p(BORNES[i], 0)
        coin_haut_droit = axes.c2p(BORNES[i + 1], EFFECTIFS[i])
        largeur = coin_haut_droit[0] - coin_bas_gauche[0]
        hauteur = coin_haut_droit[1] - coin_bas_gauche[1]
        barre = Rectangle(
            width=largeur,
            height=hauteur,
            fill_color=YELLOW,
            fill_opacity=0.55,
            stroke_color=YELLOW,
            stroke_width=2,
        )
        barre.move_to(coin_bas_gauche, aligned_edge=LEFT + DOWN)
        label = MathTex(str(EFFECTIFS[i]), font_size=16).next_to(barre, UP, buff=0.06)
        borne_label = MathTex(str(BORNES[i]), font_size=15).next_to(coin_bas_gauche, DOWN, buff=0.12)
        barres.add(barre, label, borne_label)
    derniere_borne = MathTex(str(BORNES[-1]), font_size=15).next_to(axes.c2p(BORNES[-1], 0), DOWN, buff=0.12)
    barres.add(derniere_borne)
    return VGroup(axes, barres)


class RegroupementClassesHistogramme(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Regroupement en classes et histogramme")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Pour un caractère continu, ou avec beaucoup de "
                "modalités distinctes, un tableau modalité par "
                "modalité devient illisible. On regroupe alors les "
                "données en CLASSES.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour un caractère continu, ou dès qu'il y a beaucoup "
                "de modalités distinctes, un tableau modalité par "
                "modalité devient illisible. On regroupe alors les "
                "données en classes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : classe / amplitude / centre -----------------------
        def_classe = definition_box(
            VGroup(
                Text("Classe, amplitude, centre", font_size=22, weight="BOLD"),
                MathTex(r"\text{Classe} \ [a_i \,;\, a_{i+1}[ \quad \text{amplitude} = a_{i+1} - a_i", font_size=22),
                MathTex(r"\text{centre de la classe} = \dfrac{a_i + a_{i+1}}{2}", font_size=23),
            ).arrange(DOWN, buff=0.25),
        )
        def_classe.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une classe est un intervalle de la forme a indice i, "
                "fermé à gauche, a indice i plus 1, ouvert à droite. Son "
                "amplitude est la différence de ses bornes, et son "
                "centre est la demi-somme de ces deux bornes."
            )
        ) as tracker:
            self.play(FadeIn(def_classe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_classe))

        remarque = definition_box(
            VGroup(
                Text("Remarque — Répartition régulière", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "On suppose les individus d'une classe RÉPARTIS "
                        "RÉGULIÈREMENT à l'intérieur de celle-ci : c'est "
                        "pourquoi on remplace chaque classe par son "
                        "centre pour tout calcul de moyenne ou de "
                        "variance.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        remarque.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une remarque essentielle : on suppose toujours les "
                "individus d'une classe répartis régulièrement à "
                "l'intérieur de celle-ci. C'est cette hypothèse qui "
                "justifie de remplacer chaque classe par son centre dès "
                "qu'on calcule une moyenne ou une variance."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        def_histogramme = definition_box(
            VGroup(
                Text("Histogramme", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "Diagramme fait de rectangles accolés, un par "
                        "classe, dont l'AIRE est proportionnelle à "
                        "l'effectif de la classe.",
                        width=46,
                    ),
                    font_size=20,
                ),
                MathTex(r"\text{Amplitudes ÉGALES} \Rightarrow \text{hauteur} = n_i", font_size=21),
                MathTex(r"\text{Amplitudes INÉGALES} \Rightarrow \text{hauteur} = \text{densité} = \dfrac{n_i}{\text{amplitude}_i}", font_size=21),
            ).arrange(DOWN, buff=0.22),
        )
        def_histogramme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'histogramme est un diagramme fait de rectangles "
                "accolés, un par classe, dont c'est l'AIRE — et non la "
                "hauteur — qui est proportionnelle à l'effectif de la "
                "classe. Quand toutes les classes ont la même amplitude, "
                "la hauteur peut directement être l'effectif. Mais si "
                "les amplitudes sont inégales, il faut prendre pour "
                "hauteur la densité, c'est-à-dire l'effectif divisé par "
                "l'amplitude de la classe, pour que l'aire reste "
                "correcte."
            )
        ) as tracker:
            self.play(FadeIn(def_histogramme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_histogramme))

        # --- Exemple résolu 2 : 60 sacs de cacao à Daloa ----------------------
        enonce = Text(
            _wrap(
                "Exemple résolu 2 : à Daloa, on pèse N=60 sacs de "
                "cacao. Les masses (en kg) sont regroupées en 5 classes "
                "d'amplitude égale à 5 kg, de 60 kg à 85 kg.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu numéro 2. À Daloa, on pèse 60 sacs de "
                "cacao. Les masses en kilogrammes sont regroupées en 5 "
                "classes d'amplitude égale à 5 kilogrammes, de 60 à 85 "
                "kilogrammes."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        tableau_classes = MathTex(
            r"""\begin{array}{c|ccccc}
            \text{Classe} & [60\,;65[ & [65\,;70[ & [70\,;75[ & [75\,;80[ & [80\,;85[ \\
            \hline
            \text{Centre} & 62{,}5 & 67{,}5 & 72{,}5 & 77{,}5 & 82{,}5 \\
            n_i & 4 & 10 & 24 & 14 & 8
            \end{array}""",
            font_size=22,
        )
        tableau_classes.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Comme toutes les amplitudes sont égales, à 5 "
                "kilogrammes, la hauteur des barres pourra directement "
                "être l'effectif de chaque classe. Voici le tableau des "
                "5 classes, avec leur centre et leur effectif : 4, 10, "
                "24, 14, puis 8 sacs. On vérifie que leur somme fait "
                "bien 60."
            )
        ) as tracker:
            self.play(Write(tableau_classes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_classes))

        histo = _histogramme()
        histo.scale(0.92)
        histo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici l'histogramme correspondant : cinq rectangles "
                "accolés, chacun de largeur 5, la classe la plus "
                "peuplée étant nettement celle des 70 à 75 kilogrammes, "
                "avec 24 sacs."
            )
        ) as tracker:
            self.play(FadeIn(histo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(histo))

        # --- À retenir --------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"\text{Histogramme} : \text{AIRE} \propto \text{effectif} \quad (\text{jamais la hauteur seule})", font_size=22),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel sur l'histogramme : c'est "
                "toujours l'aire qui est proportionnelle à l'effectif, "
                "jamais la hauteur seule — un réflexe indispensable dès "
                "que les amplitudes ne sont plus toutes égales."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Amplitudes inégales : ne pas lire la hauteur brute", font_size=17, weight="BOLD"),
                Text(
                    _wrap(
                        "Si une classe est deux fois plus large qu'une "
                        "autre pour le même effectif, sa hauteur doit "
                        "être DEUX FOIS PLUS PETITE : c'est la densité "
                        "n_i / amplitude qui donne la hauteur, pas n_i "
                        "seul.",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège classique à anticiper, même s'il ne se manifeste "
                "pas dans cet exemple aux amplitudes égales : si une "
                "classe est deux fois plus large qu'une autre pour le "
                "même effectif, sa hauteur doit être deux fois plus "
                "petite. C'est la densité, l'effectif divisé par "
                "l'amplitude, qui donne la hauteur correcte — jamais "
                "l'effectif brut dès que les amplitudes diffèrent."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
