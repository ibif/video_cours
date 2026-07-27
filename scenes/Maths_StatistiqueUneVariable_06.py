"""
scenes/Maths_StatistiqueUneVariable_06.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 06.

§ Médiane par interpolation linéaire : propriété — formule
M = a_{k-1} + ((N/2 - N_{k-1}) / n_k) × (a_k - a_{k-1}), avec justification
(hypothèse de répartition régulière dans la classe médiane). Exemple
résolu 3 complet : reprise des sacs de cacao (scène 03), tableau des
cumulés croissants, identification de la classe médiane [70;75[, calcul
M≈73,3 kg, interprétation.
Source : 1ereC/Maths.pdf, chapitre 17, pages 205-206.
"""

import textwrap

from manim import DOWN, RIGHT, UP, WHITE, YELLOW, Dot, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box

# --- Données reprises de la scène 03 (60 sacs de cacao pesés à Daloa) -----
BORNES = [60, 65, 70, 75, 80, 85]
EFFECTIFS = [4, 10, 24, 14, 8]
ECC = [4, 14, 38, 52, 60]
N_TOTAL = 60


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _schema_interpolation() -> VGroup:
    """Petit schéma : segment [70;75] avec la position proportionnelle de M."""
    gauche = Dot(RIGHT * -2.2, radius=0.05, color=WHITE)
    droite = Dot(RIGHT * 2.2, radius=0.05, color=WHITE)
    segment = Line(gauche.get_center(), droite.get_center(), color=WHITE)
    # M se situe à (30-14)/24 = 2/3 du segment [70;75]
    position_M = gauche.get_center() + (droite.get_center() - gauche.get_center()) * (2 / 3)
    point_M = Dot(position_M, radius=0.06, color=YELLOW)
    label_gauche = MathTex(r"70\ (N_{k-1}=14)", font_size=20).next_to(gauche, DOWN, buff=0.2)
    label_droite = MathTex(r"75\ (\text{ECC}=38)", font_size=20).next_to(droite, DOWN, buff=0.2)
    label_M = MathTex(r"M \approx 73{,}3", font_size=22, color=YELLOW).next_to(point_M, UP, buff=0.2)
    label_cible = MathTex(r"N/2=30", font_size=18, color=YELLOW).next_to(point_M, DOWN, buff=0.35)
    return VGroup(segment, gauche, droite, point_M, label_gauche, label_droite, label_M, label_cible)


class MedianeInterpolationLineaire(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Médiane par interpolation linéaire")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Dans une série regroupée en classes, la médiane tombe "
                "presque toujours À L'INTÉRIEUR d'une classe, jamais "
                "pile sur une borne. Comment obtenir sa valeur exacte ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans une série regroupée en classes, la médiane tombe "
                "presque toujours à l'intérieur d'une classe, jamais "
                "pile sur une borne. Comment obtenir alors sa valeur "
                "exacte, et non plus seulement le nom de sa classe ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : formule d'interpolation + justification -----------
        formule = theorem_box(
            VGroup(
                Text("Formule d'interpolation linéaire de la médiane", font_size=20, weight="BOLD"),
                MathTex(
                    r"M = a_{k-1} + \dfrac{\frac{N}{2} - N_{k-1}}{n_k} \times (a_k - a_{k-1})",
                    font_size=26,
                ),
                Text(
                    _wrap(
                        "[a_{k-1} ; a_k[ = classe médiane · N_{k-1} = "
                        "ECC avant la classe médiane · n_k = effectif "
                        "de la classe médiane.",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        formule.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la formule d'interpolation linéaire de la "
                "médiane : M égale a indice k moins 1, plus le rapport "
                "de N sur 2 moins N indice k moins 1, sur n indice k, le "
                "tout multiplié par a indice k moins a indice k moins "
                "1. Ici, l'intervalle a indice k moins 1, a indice k est "
                "la classe médiane, N indice k moins 1 est l'effectif "
                "cumulé croissant juste avant cette classe, et n indice "
                "k est l'effectif de la classe médiane elle-même."
            )
        ) as tracker:
            self.play(FadeIn(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule))

        justification = theorem_box(
            VGroup(
                Text("Justification", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "Grâce à l'hypothèse de répartition régulière "
                        "(scène 03), on avance dans la classe médiane "
                        "PROPORTIONNELLEMENT à la fraction d'individus "
                        "restant à atteindre, (N/2 - N_{k-1}) / n_k, sur "
                        "toute l'amplitude a_k - a_{k-1}.",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        justification.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cette formule se justifie par l'hypothèse de "
                "répartition régulière posée dès la scène 3 : à "
                "l'intérieur de la classe médiane, les individus sont "
                "supposés uniformément répartis. On avance donc dans "
                "cette classe proportionnellement à la fraction "
                "d'individus qu'il reste à atteindre pour arriver à N "
                "sur 2, rapportée à l'effectif total de la classe, et "
                "on applique cette même proportion à toute l'amplitude "
                "de la classe."
            )
        ) as tracker:
            self.play(FadeIn(justification))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(justification))

        # --- Exemple résolu 3 : sacs de cacao ----------------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu 3 : calculons la médiane exacte des "
                "masses des 60 sacs de cacao pesés à Daloa (scène 03).",
                width=52,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu numéro 3. Calculons la médiane exacte "
                "des masses des 60 sacs de cacao pesés à Daloa, "
                "l'exemple de la scène 3."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        tableau_ecc = MathTex(
            r"""\begin{array}{c|ccccc}
            \text{Classe} & [60\,;65[ & [65\,;70[ & [70\,;75[ & [75\,;80[ & [80\,;85[ \\
            \hline
            n_i & 4 & 10 & 24 & 14 & 8 \\
            \text{ECC} & 4 & 14 & 38 & 52 & 60
            \end{array}""",
            font_size=21,
        )
        tableau_ecc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici, en troisième ligne, l'effectif cumulé croissant "
                "de chaque classe : 4, puis 14, puis 38, puis 52, puis "
                "60. Ici N vaut 60, donc N sur 2 vaut 30."
            )
        ) as tracker:
            self.play(Write(tableau_ecc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_ecc))

        identification = MathTex(
            r"\text{ECC}(70) = 14 < 30 \le \text{ECC}(75) = 38 \ \Rightarrow \ \text{classe médiane} = [70\,;75[",
            font_size=22,
            color=YELLOW,
        )
        identification.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On cherche la première classe où l'effectif cumulé "
                "croissant atteint ou dépasse 30. L'ECC vaut 14 à la "
                "borne 70, puis 38 à la borne 75 : 30 est dépassé dans "
                "l'intervalle 70 à 75, qui est donc la classe médiane."
            )
        ) as tracker:
            self.play(Write(identification))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(identification))

        calcul = MathTex(
            r"M = 70 + \dfrac{30 - 14}{24} \times (75-70) = 70 + \dfrac{16}{24}\times 5 = 70 + \dfrac{10}{3} \approx 73{,}3\text{ kg}",
            font_size=24,
            color=YELLOW,
        )
        calcul.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On applique la formule : a indice k moins 1 vaut 70, N "
                "indice k moins 1 vaut 14, n indice k vaut 24, et "
                "l'amplitude vaut 5. On obtient 70 plus 16 sur 24 fois "
                "5, soit 70 plus 10 tiers, environ 73,3 kilogrammes."
            )
        ) as tracker:
            self.play(Write(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul))

        schema = _schema_interpolation()
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Visuellement, la médiane se situe aux deux tiers de la "
                "classe 70 à 75, puisqu'il reste 16 sacs sur les 24 de "
                "la classe à atteindre pour parvenir à 30 : 16 sur 24, "
                "c'est bien deux tiers du chemin."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir --------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "4 étapes : (1) N/2, (2) classe médiane via "
                        "l'ECC, (3) formule d'interpolation, (4) "
                        "vérifier M dans l'intervalle de la classe.",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la méthode en quatre étapes : calculer N sur "
                "2, repérer la classe médiane grâce à l'effectif cumulé "
                "croissant, appliquer la formule d'interpolation, puis "
                "toujours vérifier que le résultat obtenu tombe bien à "
                "l'intérieur de l'intervalle de la classe médiane."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Ne pas confondre N_{k-1} et n_k", font_size=19, weight="BOLD"),
                Text(
                    _wrap(
                        "N_{k-1} est l'effectif CUMULÉ avant la classe "
                        "(38 ici serait FAUX), n_k est l'effectif PROPRE "
                        "à la classe médiane seule (24, pas 38 ni 60).",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège très fréquent dans cette formule : ne confondez "
                "pas N indice k moins 1, l'effectif cumulé AVANT la "
                "classe médiane, avec n indice k, l'effectif PROPRE à "
                "la seule classe médiane. Utiliser 38, l'effectif "
                "cumulé APRÈS la classe, à la place de 24 est une erreur "
                "classique qui fausse tout le résultat."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
