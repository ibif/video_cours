"""
scenes/Maths_GeometrieAnalytiquePlan_07.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 07.

§ Vecteur normal à une droite (repère orthonormé) : définition, théorème
(D):ax+by+c=0 admet n(a;b) pour vecteur normal, avec démonstration (rappel
produit scalaire). Théorème parallélisme (D)∥(D') ⟺ ab'-a'b=0 (tout
repère), perpendicularité (D)⟂(D') ⟺ aa'+bb'=0 (repère orthonormé), avec
démonstrations. Conséquences pratiques.
Source : 1ereC/Maths.pdf, chapitre 14, pages 170-171.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, Axes, Create, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class VecteurNormalParallelismePerpendicularite(NotionScene):
    def construct(self):
        titre = scene_title("Vecteur normal — parallélisme et perpendicularité")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : définition du vecteur normal --------------------------------
        axes = Axes(
            x_range=[-2, 3, 1], y_range=[-2, 3, 1], x_length=4.2, y_length=4.2,
            axis_config={"include_tip": False, "color": WHITE},
        ).move_to(LEFT * 3.3 + DOWN * 0.2)
        droite = axes.plot(lambda x: -x + 1, x_range=[-2, 3], color=WHITE)
        n_arrow = Arrow(axes.c2p(0.5, 0.5), axes.c2p(1.5, 1.5), buff=0, color="#B42E41", stroke_width=4)
        n_label = MathTex(r"\vec{n}", font_size=28, color="#B42E41").next_to(n_arrow, RIGHT, buff=0.1)
        schema = VGroup(axes, droite, n_arrow, n_label)

        definition = definition_box(
            VGroup(
                Text("Vecteur normal (repère orthonormé)", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Un vecteur non nul n est normal à une droite (D) "
                        "s'il est orthogonal à tout vecteur directeur "
                        "de (D).",
                        width=40,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=6.4,
        )
        definition.move_to(RIGHT * 3.4 + DOWN * 0.2)

        with self.voiceover(
            text=(
                "Dans un repère orthonormé, on peut aussi caractériser une "
                "droite par un vecteur normal : un vecteur non nul n est "
                "normal à une droite (D) s'il est orthogonal à tout vecteur "
                "directeur de cette droite. Voyons comment le lire "
                "directement sur l'équation cartésienne."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(definition))

        # --- Raisonnement : théorème vecteur normal + démonstration --------------
        theoreme = theorem_box(
            MathTex(
                r"(D): ax+by+c=0 \ \Rightarrow\ \vec{n}(a\,;\,b) \text{ est un vecteur normal à } (D)",
                font_size=27,
            ),
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Théorème : si (D) a pour équation a x plus b y plus c "
                "égale zéro, alors le vecteur n de coordonnées a, b est un "
                "vecteur normal à (D)."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        rappel_ps = Text(
            _wrap(
                "Rappel : en repère orthonormé, u(x;y)·v(x';y') = xx'+yy'."
                " u ⊥ v ⟺ u·v = 0.",
                width=52,
            ),
            font_size=23,
            color=YELLOW,
        )
        rappel_ps.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappelons d'abord le produit scalaire en repère "
                "orthonormé : pour u de coordonnées x, y et v de "
                "coordonnées x prime, y prime, le produit scalaire u point "
                "v vaut x x prime plus y y prime, et u est orthogonal à v "
                "si et seulement si ce produit scalaire est nul."
            )
        ) as tracker:
            self.play(FadeIn(rappel_ps))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel_ps))

        demo_normal = VGroup(
            MathTex(
                r"\vec{u}(-b;a) \text{ est un vecteur directeur de } (D) \text{ (mnémotechnique)}",
                font_size=25,
            ),
            MathTex(
                r"\vec{n}(a;b)\cdot\vec{u}(-b;a) = a\times(-b) + b\times a = -ab+ab = 0",
                font_size=25,
            ),
            MathTex(
                r"\Rightarrow\ \vec{n}\perp\vec{u} \ \Rightarrow\ \vec{n} \text{ est normal à } (D)",
                font_size=26,
                color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.32)
        demo_normal.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On sait déjà que u de coordonnées moins b, a est un "
                "vecteur directeur de (D). Calculons le produit scalaire de "
                "n et u : a fois moins b, plus b fois a, ce qui vaut moins "
                "a b plus a b, donc zéro. n est donc orthogonal à u, ce qui "
                "prouve que n est bien normal à la droite (D)."
            )
        ) as tracker:
            self.play(Write(demo_normal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_normal))

        # --- Parallélisme et perpendicularité de deux droites --------------------
        parallelisme = theorem_box(
            VGroup(
                Text("Parallélisme (tout repère)", font_size=22, weight="BOLD"),
                MathTex(
                    r"(D):ax+by+c=0,\ (D'):a'x+b'y+c'=0"
                    r"\\[4pt]"
                    r"(D)\parallel(D') \iff ab'-a'b=0",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        parallelisme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avec les vecteurs directeurs u de coordonnées moins b, a, "
                "et u prime de coordonnées moins b prime, a prime, la "
                "colinéarité s'écrit par déterminant : moins b fois a "
                "prime, moins moins b prime fois a, égale zéro, ce qui se "
                "simplifie en a b prime moins a prime b égale zéro. Ce "
                "critère de parallélisme est valable dans TOUT repère, "
                "puisqu'il découle directement du déterminant."
            )
        ) as tracker:
            self.play(FadeIn(parallelisme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(parallelisme))

        perpendicularite = theorem_box(
            VGroup(
                Text("Perpendicularité (repère orthonormé)", font_size=22, weight="BOLD"),
                MathTex(
                    r"(D)\perp(D') \iff \vec{n}\perp\vec{n'} \iff \vec{n}\cdot\vec{n'}=0"
                    r"\\[4pt]"
                    r"\iff aa'+bb'=0",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=8.0,
        )
        perpendicularite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour la perpendicularité, on raisonne cette fois sur les "
                "vecteurs normaux : deux droites sont perpendiculaires si "
                "et seulement si leurs vecteurs normaux le sont, "
                "c'est-à-dire si leur produit scalaire est nul. Avec n de "
                "coordonnées a, b et n prime de coordonnées a prime, b "
                "prime, cela s'écrit a a prime plus b b prime égale zéro. "
                "Ce critère, lui, nécessite impérativement un repère "
                "orthonormé, puisqu'il utilise le produit scalaire."
            )
        ) as tracker:
            self.play(FadeIn(perpendicularite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(perpendicularite))

        # --- Exemple : conséquences pratiques ---------------------------------------
        consequences = method_box(
            VGroup(
                Text("Conséquences pratiques", font_size=23, weight="BOLD"),
                MathTex(
                    r"(D): ax+by+c=0,\ A(x_0;y_0)"
                    r"\\[4pt]"
                    r"\text{Parallèle à } (D) \text{ par } A: \ ax+by+(-ax_0-by_0)=0"
                    r"\\[4pt]"
                    r"\text{Perpendiculaire à } (D) \text{ par } A: \ bx-ay+(-bx_0+ay_0)=0",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        consequences.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En pratique, pour écrire l'équation de la parallèle à (D) "
                "passant par un point A, on garde les mêmes coefficients a "
                "et b, et on ajuste la constante pour que A vérifie "
                "l'équation. Pour la perpendiculaire, on échange a et b en "
                "changeant un signe, exactement comme pour passer d'un "
                "vecteur directeur à un vecteur normal, puis on ajuste de "
                "même la constante."
            )
        ) as tracker:
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequences))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(r"(D):ax+by+c=0 \ \Rightarrow\ \vec{n}(a;b) \text{ normal à } (D)", font_size=25),
                MathTex(r"(D)\parallel(D') \iff ab'-a'b=0 \quad \text{(tout repère)}", font_size=25),
                MathTex(r"(D)\perp(D') \iff aa'+bb'=0 \quad \text{(orthonormé)}", font_size=25),
            ).arrange(DOWN, buff=0.28),
            box_width=10.2,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : le vecteur a, b lu sur l'équation est normal à "
                "la droite. Le parallélisme se teste avec a b prime moins a "
                "prime b, valable dans tout repère ; la perpendicularité se "
                "teste avec a a prime plus b b prime, uniquement en repère "
                "orthonormé."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre vecteur DIRECTEUR (-b;a) et vecteur "
                    "NORMAL (a;b) — ils sont orthogonaux entre eux ! Et la "
                    "perpendicularité (aa'+bb'=0) exige un repère "
                    "orthonormé, contrairement au parallélisme.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : ne confondez pas le vecteur directeur, "
                "moins b, a, et le vecteur normal, a, b — ce sont deux "
                "vecteurs orthogonaux entre eux, pas le même objet. Et "
                "n'oubliez pas que la formule de perpendicularité exige un "
                "repère orthonormé, alors que celle de parallélisme "
                "fonctionne dans n'importe quel repère."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
