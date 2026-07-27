"""
scenes/Maths_ComposeesTransformationsPlan_01.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 01.

§ Rappels sur les transformations usuelles (1/2) : transformation du plan
(application bijective), translation (expression analytique, propriétés),
symétrie axiale (expression analytique pour les 4 axes usuels, propriétés).
Source : 1ereC/Maths.pdf, chapitre 8, pages 91-93.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.08)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class RappelsTransformationsUsuelles1(NotionScene):
    def construct(self):
        # --- Énoncé : qu'est-ce qu'une transformation du plan -----------------
        titre = scene_title("Rappels — Transformations usuelles (1/2)")
        titre.scale(0.48)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Avant d'étudier les composées de transformations, "
                "reprenons les transformations usuelles du plan déjà "
                "rencontrées : translation et symétrie axiale dans cette "
                "vidéo, puis symétrie centrale, rotation et homothétie "
                "dans la suivante. Une transformation du plan est une "
                "application bijective du plan dans lui-même : à tout "
                "point M, elle associe un unique point M prime, appelé "
                "image de M, et tout point du plan est l'image d'un "
                "unique point."
            )
        ) as tracker:
            self.play(Write(titre))
            def_transfo = definition_box(
                VGroup(
                    Text("Transformation du plan", font_size=25, weight="BOLD"),
                    MathTex(r"f : \mathcal{P} \longrightarrow \mathcal{P} \text{ bijective}", font_size=28),
                    Text(
                        _wrap("À tout point M, f associe un unique point M' = f(M), et tout point du plan a un unique antécédent."),
                        font_size=22,
                    ),
                ).arrange(DOWN, buff=0.25)
            )
            def_transfo.next_to(titre, DOWN, buff=0.4)
            self.play(FadeIn(def_transfo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_transfo))

        # --- Raisonnement / figure : translation --------------------------------
        def_translation = definition_box(
            VGroup(
                Text("Translation de vecteur u⃗", font_size=25, weight="BOLD"),
                MathTex(r"M' = t_{\vec{u}}(M) \iff \overrightarrow{MM'} = \vec{u}", font_size=28),
                MathTex(r"\vec{u}(a\,;\,b): \quad x' = x+a, \quad y' = y+b", font_size=28),
                Text(
                    _wrap("Conserve distances, alignement, angles (orientés) et aires : c'est un déplacement."),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25)
        )
        def_translation.next_to(titre, DOWN, buff=0.4)

        u_start = LEFT * 3.5 + DOWN * 2.2
        u_end = LEFT * 1.8 + DOWN * 1.4
        u_vec = Arrow(u_start, u_end, color=YELLOW, buff=0)
        u_label = MathTex(r"\vec{u}", font_size=28, color=YELLOW).next_to(u_vec, UP, buff=0.1)
        deplacement = u_end - u_start
        pt_m = _dot_label(RIGHT * 1.2 + DOWN * 1.5, "M")
        pt_m1 = _dot_label(RIGHT * 1.2 + DOWN * 1.5 + deplacement, "M'")
        fleche_mm1 = Arrow(pt_m[0].get_center(), pt_m1[0].get_center(), color="#DE7C1F", buff=0.1)
        figure_translation = VGroup(u_vec, u_label, pt_m, pt_m1, fleche_mm1)

        with self.voiceover(
            text=(
                "La translation de vecteur u est la transformation qui, à "
                "tout point M, associe le point M prime tel que le vecteur "
                "M-M prime soit égal à u. Son expression analytique est "
                "simple : si u a pour coordonnées a et b, alors x prime "
                "égale x plus a, et y prime égale y plus b. La translation "
                "conserve les distances, l'alignement, les angles orientés "
                "et les aires : c'est ce qu'on appelle un déplacement."
            )
        ) as tracker:
            self.play(FadeIn(def_translation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_translation))
        with self.voiceover(
            text=(
                "Illustrons : le vecteur u déplace le point M jusqu'au "
                "point M prime, en conservant exactement la direction et "
                "la longueur du vecteur u."
            )
        ) as tracker:
            self.play(Create(figure_translation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure_translation))

        # --- Exemple traité : symétrie axiale --------------------------------
        def_sym_axiale = definition_box(
            VGroup(
                Text("Symétrie axiale d'axe Δ", font_size=25, weight="BOLD"),
                MathTex(
                    r"\Delta: x=a \Rightarrow \begin{cases} x'=2a-x \\ y'=y \end{cases} \qquad"
                    r"\Delta: y=b \Rightarrow \begin{cases} x'=x \\ y'=2b-y \end{cases}",
                    font_size=25,
                ),
                MathTex(
                    r"\Delta: y=x \Rightarrow \begin{cases} x'=y \\ y'=x \end{cases} \qquad"
                    r"\Delta: y=-x \Rightarrow \begin{cases} x'=-y \\ y'=-x \end{cases}",
                    font_size=25,
                ),
                Text(
                    _wrap("Antidéplacement (inverse les angles orientés), involutive : s∘s = id."),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25)
        )
        def_sym_axiale.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La symétrie axiale d'axe delta associe à M le point M "
                "prime tel que delta soit la médiatrice du segment M M "
                "prime. Pour les quatre axes usuels, l'expression "
                "analytique se retient facilement : pour l'axe x égale a, "
                "x prime égale 2a moins x et y prime égale y. Pour l'axe y "
                "égale b, on échange les rôles. Pour la première "
                "bissectrice y égale x, on échange x et y. Et pour la "
                "seconde bissectrice y égale moins x, on échange x et y "
                "puis on change les signes. Contrairement à la "
                "translation, la symétrie axiale est un antidéplacement : "
                "elle inverse les angles orientés. Elle est aussi "
                "involutive, c'est-à-dire que l'appliquer deux fois de "
                "suite redonne le point de départ."
            )
        ) as tracker:
            self.play(FadeIn(def_sym_axiale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_sym_axiale))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(r"t_{\vec u}:\ x'=x+a,\ y'=y+b \quad (\text{d\'eplacement})", font_size=26),
                MathTex(r"s_\Delta:\ \text{involutive} \quad (\text{antid\'eplacement})", font_size=26),
            ).arrange(DOWN, buff=0.3)
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : la translation est un déplacement défini par "
                "un vecteur constant, la symétrie axiale est un "
                "antidéplacement involutif défini par son axe."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège fréquent", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "Ne pas confondre les formules des 4 axes usuels : vérifier "
                        "systématiquement sur un point simple (par exemple l'origine, "
                        "ou un point de l'axe qui doit rester invariant)."
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25)
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre les quatre formules : le "
                "réflexe à avoir est de toujours vérifier sur un point "
                "particulier, par exemple un point situé sur l'axe, qui "
                "doit impérativement rester invariant par la symétrie."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
