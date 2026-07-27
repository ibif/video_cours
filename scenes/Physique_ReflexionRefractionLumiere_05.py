"""
scenes/Physique_ReflexionRefractionLumiere_05.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 05.

§ Lois de Snell-Descartes de la réfraction : tableau expérimental (sin
i1/sin i2 constant), théorème (1ère loi : plan d'incidence ; 2e loi :
n1 sin i1 = n2 sin i2), conséquences des trois cas (n2>n1, n2<n1,
incidence normale), exemple résolu air→eau, principe du retour inverse de
la lumière.
Source : 1ereC/Physique.pdf, pages 117-129.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREY,
    Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, property_box, theorem_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _refraction_schema(i1_deg: float, i2_deg: float, center: np.ndarray = ORIGIN, t: float = 2.0, surf_half: float = 2.2):
    i1 = np.radians(i1_deg)
    i2 = np.radians(i2_deg)
    I = center
    milieu1 = Rectangle(width=2 * surf_half, height=1.6, fill_color=BLUE, fill_opacity=0.06, stroke_width=0).move_to(I + UP * 0.8)
    milieu2 = Rectangle(width=2 * surf_half, height=1.6, fill_color=BLUE, fill_opacity=0.18, stroke_width=0).move_to(I + DOWN * 0.8)
    dioptre = Line(I + LEFT * surf_half, I + RIGHT * surf_half, color=GREY, stroke_width=4)
    normale = DashedLine(I + DOWN * 1.4, I + UP * 1.7, color=WHITE, stroke_width=2)
    S = I + t * np.array([-np.sin(i1), np.cos(i1), 0])
    T = I + t * np.array([np.sin(i2), -np.cos(i2), 0])
    rayon_incident = Line(S, I, color=YELLOW, stroke_width=4)
    rayon_refracte = Line(I, T, color=YELLOW, stroke_width=4)
    point_I = Dot(I, color=WHITE, radius=0.06)
    groupe = VGroup(milieu1, milieu2, dioptre, normale, rayon_incident, rayon_refracte, point_I)
    return groupe, S, I, T


class LoisSnellDescartesRefraction(NotionScene):
    def construct(self):
        titre = scene_title("Les lois de Snell-Descartes de la réfraction")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : question expérimentale --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "En faisant varier l'angle d'incidence i1 sur le "
                "demi-cylindre d'eau, on mesure à chaque fois l'angle de "
                "réfraction i2. Existe-t-il une relation mathématique "
                "simple entre les deux ?",
                width=48,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En faisant varier l'angle d'incidence i1 sur le "
                "demi-cylindre d'eau, on mesure à chaque fois l'angle de "
                "réfraction i2. Existe-t-il une relation mathématique "
                "simple entre les deux ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : tableau expérimental sin i1 / sin i2 --------------------
        table = VGroup(
            MathTex(r"i_1 = 20^\circ, i_2 \approx 14{,}9^\circ, \ \sin i_1/\sin i_2 \approx 1{,}33", font_size=20),
            MathTex(r"i_1 = 40^\circ, i_2 \approx 28{,}9^\circ, \ \sin i_1/\sin i_2 \approx 1{,}33", font_size=20),
            MathTex(r"i_1 = 60^\circ, i_2 \approx 40{,}6^\circ, \ \sin i_1/\sin i_2 \approx 1{,}33", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        table_box = property_box(table, box_width=10.6)
        table_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici des mesures typiques air-eau. Quel que soit l'angle "
                "d'incidence choisi, vingt, quarante ou soixante degrés, "
                "le rapport du sinus de i1 sur le sinus de i2 reste "
                "constant, environ un virgule trente-trois. Cette "
                "constante n'est autre que l'indice de réfraction de "
                "l'eau, rencontré dans la scène précédente."
            )
        ) as tracker:
            self.play(FadeIn(table_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(table_box))

        # --- Théorème : lois de Snell-Descartes de la réfraction ---------------------
        loi = theorem_box(
            VGroup(
                Text("Lois de Snell-Descartes de la réfraction", font_size=22, weight="BOLD"),
                Text("1ère loi : le rayon réfracté est dans le plan d'incidence", font_size=20),
                Text("(rayon incident, normale, rayon réfracté coplanaires).", font_size=20),
                MathTex(r"\text{2e loi : } n_1 \sin i_1 = n_2 \sin i_2", font_size=28, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        loi.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Ces observations se généralisent en deux lois de "
                "Snell-Descartes pour la réfraction. Première loi : le "
                "rayon réfracté est situé dans le plan d'incidence, comme "
                "pour la réflexion. Deuxième loi, la relation "
                "fondamentale : n1 fois sinus de i1 est égal à n2 fois "
                "sinus de i2, où n1 et n2 sont les indices des deux "
                "milieux traversés."
            )
        ) as tracker:
            self.play(FadeIn(loi))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi))

        # --- Conséquences : trois cas -------------------------------------------------
        cas1, _, _, _ = _refraction_schema(50, 32, center=LEFT * 4.4 + DOWN * 0.2, t=1.5, surf_half=1.2)
        cas1_txt = Text("n2 > n1 : rayon rapproché", font_size=15).next_to(cas1, DOWN, buff=0.2)

        cas2, _, _, _ = _refraction_schema(28, 45, center=DOWN * 0.2, t=1.5, surf_half=1.2)
        cas2_txt = Text("n2 < n1 : rayon écarté", font_size=15).next_to(cas2, DOWN, buff=0.2)

        cas3, _, _, _ = _refraction_schema(0.01, 0.01, center=RIGHT * 4.4 + DOWN * 0.2, t=1.5, surf_half=1.2)
        cas3_txt = Text("incidence normale : pas de déviation", font_size=15).next_to(cas3, DOWN, buff=0.2)

        cas_groupe = VGroup(
            VGroup(cas1, cas1_txt), VGroup(cas2, cas2_txt), VGroup(cas3, cas3_txt)
        )
        cas_groupe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois conséquences pratiques. Si le second milieu est "
                "plus réfringent que le premier, n2 supérieur à n1, le "
                "rayon se rapproche toujours de la normale, et il existe "
                "toujours un rayon réfracté, quel que soit i1. Si le "
                "second milieu est moins réfringent, n2 inférieur à n1, "
                "le rayon s'écarte de la normale, mais un rayon réfracté "
                "n'existe que sous certaines conditions, que nous "
                "détaillerons dans la prochaine scène. Enfin, en "
                "incidence normale, il n'y a aucune déviation, quel que "
                "soit le changement de milieu."
            )
        ) as tracker:
            self.play(Create(cas1), Write(cas1_txt))
            self.play(Create(cas2), Write(cas2_txt))
            self.play(Create(cas3), Write(cas3_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_groupe))

        # --- Exemple résolu 3 : air → eau ---------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un rayon passe de l'air (n1=1) à l'eau (n2=1,33)", font_size=20),
                Text("avec i1 = 30°. Calculer i2.", font_size=20),
                MathTex(r"\sin i_2 = \dfrac{n_1 \sin i_1}{n_2} = \dfrac{1 \times \sin 30^\circ}{1{,}33} \approx 0{,}376", font_size=22, color=YELLOW),
                MathTex(r"i_2 \approx 22{,}1^\circ \quad (< i_1, \ \text{rayon rapproché de la normale})", font_size=22, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.22),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. Un rayon passe de l'air, d'indice un, à "
                "l'eau, d'indice un virgule trente-trois, avec un angle "
                "d'incidence de trente degrés. Calculons i2. D'après la "
                "loi de Snell-Descartes, sinus de i2 est égal à n1 fois "
                "sinus de i1, le tout divisé par n2, ce qui donne environ "
                "zéro virgule trois cent soixante-seize. En prenant "
                "l'arc sinus, on trouve i2 environ égal à vingt-deux "
                "virgule un degrés, bien inférieur à i1 : le rayon s'est "
                "rapproché de la normale, comme attendu puisque l'eau est "
                "plus réfringente que l'air."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Retour inverse de la lumière (mention) -----------------------------------
        retour = property_box(
            VGroup(
                Text("Principe du retour inverse de la lumière", font_size=21, weight="BOLD"),
                Text("Un rayon qui suit un trajet donné dans un sens peut", font_size=19),
                Text("suivre exactement le même trajet en sens inverse.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.0,
        )
        retour.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Mentionnons enfin un principe utile, le principe du "
                "retour inverse de la lumière : un rayon qui suit un "
                "trajet donné dans un sens peut suivre exactement ce même "
                "trajet en sens inverse. Ainsi, un rayon d'eau vers l'air "
                "avec un angle i2 ressortira avec l'angle i1 initial, si "
                "l'on inverse le sens de propagation."
            )
        ) as tracker:
            self.play(FadeIn(retour))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retour))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"n_1 \sin i_1 = n_2 \sin i_2", font_size=28),
                Text("n2 > n1 : rayon rapproché, toujours réfracté.", font_size=20),
                Text("n2 < n1 : rayon écarté, sous condition (voir scène 6).", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : n1 sinus i1 égale n2 sinus i2. "
                "Quand n2 est supérieur à n1, le rayon se rapproche "
                "toujours de la normale et un rayon réfracté existe "
                "toujours. Quand n2 est inférieur à n1, le rayon s'écarte "
                "de la normale, mais sous une condition que nous verrons "
                "dans la prochaine scène."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Bien identifier n1 (milieu de départ du rayon) et n2", font_size=20),
                Text("   (milieu d'arrivée) : inverser n1 et n2 inverse le", font_size=20),
                Text("   résultat du calcul de i2.", font_size=20),
                Text("• sin i2 se calcule, mais i2 = arcsin(...) : la", font_size=20),
                Text("   calculatrice doit être en mode DEGRÉS.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : bien identifier n1, le milieu de départ "
                "du rayon, et n2, le milieu d'arrivée. Inverser les deux "
                "inverse complètement le résultat du calcul de i2. Et "
                "n'oubliez pas, une fois sinus de i2 calculé, de prendre "
                "l'arc sinus pour obtenir i2 lui-même, avec la "
                "calculatrice réglée en mode degrés."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
