"""
scenes/Maths_ComposeesTransformationsPlan_12.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 12.

§ Composée d'une homothétie et d'une translation (t∘h et h∘t sont des
homothéties de même rapport k), méthode de recherche analytique du centre,
exemple résolu 9. Décompositions à connaître (translation, rotation,
symétrie centrale, homothétie de rapport négatif), exemple résolu 10
(rotation d'angle π/3).
Source : 1ereC/Maths.pdf, chapitre 8, pages 103-104.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ComposeeHomothetieTranslationDecomposition(NotionScene):
    def construct(self):
        titre = scene_title("Homothétie ∘ translation, décompositions")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : théorème homothétie∘translation ---------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Composée d'une homothétie et d'une translation", font_size=22, weight="BOLD"),
                MathTex(r"h=h_{(\Omega,k)}, \quad t=t_{\vec w}, \quad k\neq 1", font_size=25),
                MathTex(r"t\circ h \ \text{ et } \ h\circ t \ \text{ sont des homoth\'eties de rapport } k", font_size=25),
            ).arrange(DOWN, buff=0.25)
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dernier cas de composée à étudier : une homothétie et une "
                "translation. Soit h l'homothétie de centre Oméga et de "
                "rapport k différent de 1, et t la translation de vecteur "
                "w. Alors t rond h, et aussi h rond t, sont toutes deux "
                "des homothéties, de même rapport k que h, mais avec des "
                "centres différents à calculer."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration + méthode ------------------------------
        demo = MathTex(
            r"(t\circ h)(M) = h(M)+\vec w = \Omega + k(M-\Omega) + \vec w = kM + \big[\Omega(1-k)+\vec w\big]",
            font_size=21,
        )
        demo2 = Text(
            _wrap("Application affine de rapport k ≠ 1 : c'est une homothétie de rapport k."),
            font_size=21,
        )
        demo_grp = VGroup(demo, demo2).arrange(DOWN, buff=0.3)
        demo_grp.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La démonstration reprend la même méthode que pour deux "
                "homothéties de centres distincts : on écrit t rond h "
                "comme fonction affine de M, ce qui donne k fois M, plus "
                "une constante. Comme le rapport linéaire k est différent "
                "de 1, cette application affine est une homothétie de "
                "rapport k, dont il reste à trouver le centre."
            )
        ) as tracker:
            self.play(Write(demo))
            self.play(FadeIn(demo2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_grp))

        methode = method_box(
            VGroup(
                Text("Méthode : recherche analytique du centre", font_size=23, weight="BOLD"),
                Text(
                    _wrap("On pose f(Ω') = Ω' (point invariant), puis on résout l'équation obtenue."),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25)
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En pratique, pour trouver le centre d'une telle composée, "
                "la méthode est toujours la même : on pose que le centre "
                "cherché, Oméga prime, est un point invariant, c'est-à-dire "
                "que f de Oméga prime égale Oméga prime, puis on résout "
                "cette équation."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple résolu 9 --------------------------------------------------
        enonce9 = MathTex(r"h=h_{(\Omega,2)}, \ \Omega(1\,;\,-1), \quad t = t_{(3\,;\,0)}, \quad f=t\circ h", font_size=24)
        calc9a = MathTex(r"f(M) = 2M + \big[\Omega(1-2)+(3;0)\big] = 2M + (2\,;\,1)", font_size=24)
        calc9b = MathTex(r"\Omega' = 2\Omega' + (2;1) \implies \Omega'=-(2;1) = (-2\,;\,-1)", font_size=24, color=YELLOW)
        exemple9 = example_box(VGroup(enonce9, calc9a, calc9b).arrange(DOWN, buff=0.25))
        exemple9.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : soit h l'homothétie de centre Oméga de "
                "coordonnées 1 et moins 1, de rapport 2, et t la "
                "translation de vecteur 3 et 0. Posons f égale t rond h. "
                "En développant, f de M vaut 2M plus le vecteur 2, 1. Le "
                "centre Oméga prime vérifie alors Oméga prime égale 2 fois "
                "Oméga prime plus 2, 1, ce qui donne Oméga prime égale "
                "moins 2, moins 1."
            )
        ) as tracker:
            self.play(FadeIn(exemple9))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple9))

        # --- Décompositions à connaître ------------------------------------------
        decomp = theorem_box(
            VGroup(
                Text("Décompositions à connaître", font_size=23, weight="BOLD"),
                MathTex(r"t_{\vec w} = s_{O'}\circ s_O, \ \ \overrightarrow{OO'}=\tfrac12\vec w \ \ (O \text{ arbitraire})", font_size=21),
                MathTex(r"r_{(O,\theta)} = s_{\Delta_2}\circ s_{\Delta_1}, \ \ (\widehat{\Delta_1,\Delta_2})=\tfrac{\theta}{2} \ \ (\Delta_1 \text{ arbitraire})", font_size=20),
                MathTex(r"s_O = s_{\Delta_2}\circ s_{\Delta_1}, \ \ \Delta_1\perp\Delta_2 \text{ en } O", font_size=21),
                MathTex(r"h_{(O,k)},\ k<0 \ = \ h_{(O,-1)}\circ h_{(O,\,|k|)} \ \ (\text{sym. centrale} \circ \text{homoth\'etie})", font_size=20),
            ).arrange(DOWN, buff=0.2)
        )
        decomp.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Réunissons maintenant les décompositions essentielles, "
                "vues au fil du chapitre, indispensables pour les "
                "problèmes de construction. Toute translation se "
                "décompose en deux symétries centrales, de centres "
                "distants de la moitié du vecteur, l'un des deux centres "
                "étant arbitraire. Toute rotation se décompose en deux "
                "symétries axiales d'axes sécants formant la moitié de "
                "l'angle, le premier axe étant arbitraire. La symétrie "
                "centrale, cas particulier de rotation d'angle pi, se "
                "décompose en deux symétries d'axes perpendiculaires. Et "
                "une homothétie de rapport négatif se décompose en une "
                "symétrie centrale composée avec une homothétie de rapport "
                "positif, la valeur absolue du rapport initial."
            )
        ) as tracker:
            self.play(FadeIn(decomp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(decomp))

        justif = Text(
            _wrap(
                "Justification du point 2 : pour tout axe Δ1 passant par O, il "
                "suffit de choisir Δ2 tel que l'angle orienté (Δ1,Δ2) vaille θ/2 "
                "— le théorème de la scène 8 donne alors sΔ2∘sΔ1 = r(O,θ)."
            ),
            font_size=22,
        )
        justif.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Justifions en particulier le point sur la rotation : pour "
                "n'importe quel axe delta 1 passant par O, il suffit de "
                "choisir delta 2 tel que l'angle orienté de delta 1 vers "
                "delta 2 vaille thêta sur deux — le théorème vu à propos "
                "des axes sécants garantit alors exactement que la "
                "composée redonne la rotation voulue."
            )
        ) as tracker:
            self.play(FadeIn(justif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(justif))

        # --- Exemple résolu 10 -----------------------------------------------
        enonce10 = MathTex(r"\text{D\'ecomposer } r_{(O,\,\pi/3)} \text{ en 2 sym\'etries axiales}", font_size=25)
        calc10a = MathTex(r"\Delta_1 = \text{axe des abscisses passant par } O", font_size=23)
        calc10b = MathTex(r"(\widehat{\Delta_1,\Delta_2}) = \dfrac{\pi/3}{2} = \dfrac{\pi}{6}", font_size=25)
        calc10c = MathTex(r"\implies r_{(O,\,\pi/3)} = s_{\Delta_2}\circ s_{\Delta_1}", font_size=26, color=YELLOW)
        exemple10 = example_box(VGroup(enonce10, calc10a, calc10b, calc10c).arrange(DOWN, buff=0.25))
        exemple10.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : décomposons la rotation de centre O et d'angle "
                "pi sur trois. On choisit un premier axe delta 1 "
                "arbitraire, disons l'axe des abscisses passant par O. "
                "L'angle entre delta 1 et le second axe delta 2 doit alors "
                "valoir la moitié de pi sur trois, c'est-à-dire pi sur "
                "six. La rotation est ainsi la composée de la symétrie "
                "d'axe delta 1, suivie de la symétrie d'axe delta 2, "
                "formant un angle de pi sur six avec delta 1."
            )
        ) as tracker:
            self.play(FadeIn(exemple10))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple10), FadeOut(titre))
