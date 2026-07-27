"""
scenes/Maths_ComposeesTransformationsPlan_11.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 11.

§ Composée de deux homothéties de centres distincts : si k'k≠1, homothétie
de rapport k'k, centre Ω barycentre de (O, k'(1-k)) et (O', 1-k') ; si
k'k=1, translation. Démonstration complète, remarque non-commutativité,
exemples résolus 7 et 8.
Source : 1ereC/Maths.pdf, chapitre 8, pages 102-103.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Create, Dot, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class ComposeeHomothetiesCentresDistincts(NotionScene):
    def construct(self):
        titre = scene_title("Composée de 2 homothéties — centres distincts")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : théorème fondamental --------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Théorème fondamental (O ≠ O')", font_size=22, weight="BOLD"),
                MathTex(r"h=h_{(O,k)}, \quad h'=h_{(O',k')}, \quad O\neq O'", font_size=25),
                MathTex(
                    r"k'k\neq 1 \implies h'\circ h = h_{(\Omega,\,k'k)}, \ \ "
                    r"\Omega = \mathrm{bar}\{(O,\,k'(1-k))\,;\,(O',\,1-k')\}",
                    font_size=21,
                ),
                MathTex(r"k'k = 1 \implies h'\circ h \text{ est une translation}", font_size=23),
            ).arrange(DOWN, buff=0.2)
        )
        theoreme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le cas le plus riche : deux homothéties de centres "
                "distincts O et O prime, de rapports k et k prime. Si le "
                "produit k prime fois k est différent de 1, la composée h "
                "prime rond h est une homothétie de rapport k prime fois "
                "k, dont le centre Oméga est le barycentre des points "
                "pondérés O, k prime fois 1 moins k, et O prime, 1 moins k "
                "prime — on retrouve ici la notion de barycentre étudiée "
                "précédemment. Si en revanche ce produit vaut exactement "
                "1, la composée n'est plus une homothétie : c'est une "
                "translation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration -----------------------------------
        etape1 = MathTex(r"M_1 = h(M): \quad M_1 = O + k(M-O)", font_size=23)
        etape2 = MathTex(r"M' = h'(M_1): \quad M' = O' + k'(M_1-O')", font_size=23)
        etape3 = MathTex(r"M' = k'k\,M + \underbrace{\big[k'O(1-k) + O'(1-k')\big]}_{C}", font_size=22)
        etape4 = MathTex(
            r"k'k\neq 1 \implies \Omega \text{ point fixe}: \ \Omega = \dfrac{C}{1-k'k}"
            r" \implies \Omega=\mathrm{bar}\{(O,k'(1-k));(O',1-k')\}",
            font_size=19,
            color=YELLOW,
        )
        demo = VGroup(etape1, etape2, etape3, etape4).arrange(DOWN, buff=0.25)
        demo.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Démontrons ce résultat en écrivant tout en coordonnées, "
                "assimilées à des vecteurs. L'image M-un de M par h "
                "s'écrit O plus k fois M moins O. En appliquant h prime à "
                "M-un, on obtient, après regroupement des termes, M prime "
                "égale k prime fois k, fois M, plus une constante C qui ne "
                "dépend que de O, O prime, k et k prime. C'est une "
                "application affine de rapport linéaire k prime fois k. "
                "Si ce rapport est différent de 1, elle admet un unique "
                "point fixe Oméga, qui est précisément le centre de "
                "l'homothétie cherchée, et l'on retrouve, après "
                "simplification, l'écriture barycentrique annoncée."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.play(Write(etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        remarque = Text(
            _wrap("Remarque : contrairement au cas de même centre, h'∘h ≠ h∘h' en général lorsque les centres sont distincts."),
            font_size=22,
        )
        remarque.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Remarque importante : à la différence du cas de même "
                "centre, ici h prime rond h et h rond h prime ont en "
                "général le même rapport, mais des centres différents : la "
                "composition n'est plus commutative."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Exemple résolu 7 --------------------------------------------------
        enonce7 = MathTex(r"O(0\,;\,0), \quad O'(3\,;\,0), \quad h=h_{(O,2)}, \quad h'=h_{(O',3)}", font_size=24)
        calc7a = MathTex(r"k'k = 6 \neq 1 \implies h'\circ h = h_{(\Omega,\,6)}", font_size=24)
        calc7b = MathTex(
            r"\Omega = \mathrm{bar}\{(O,\,3(1-2))\,;\,(O',\,1-3)\} = \mathrm{bar}\{(O,\,3)\,;\,(O',\,2)\}",
            font_size=20,
        )
        calc7c = MathTex(r"\Omega = \dfrac{3\,O + 2\,O'}{5} = (1{,}2\,;\,0)", font_size=24, color=YELLOW)
        calc7d = MathTex(r"\text{V\'erif. } M(1;0): h(M)=(2;0), \ h'(2;0)=(0;0) = 6\times 1 - 6 \ \checkmark", font_size=18)
        exemple7 = example_box(VGroup(enonce7, calc7a, calc7b, calc7c, calc7d).arrange(DOWN, buff=0.2))
        exemple7.scale(0.92)
        exemple7.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Traitons un exemple complet. Soit O l'origine, O prime le "
                "point de coordonnées 3 et 0, h l'homothétie de centre O "
                "et de rapport 2, h prime celle de centre O prime et de "
                "rapport 3. Le produit des rapports vaut 6, différent de "
                "1 : la composée est donc une homothétie de rapport 6. "
                "Son centre Oméga est le barycentre de O affecté du "
                "coefficient 3 fois 1 moins 2, et de O prime affecté du "
                "coefficient 1 moins 3, ce qui se simplifie en le "
                "barycentre de O pondéré 3 et O prime pondéré 2. On "
                "calcule alors Oméga égale 3 O plus 2 O prime, le tout "
                "divisé par 5, ce qui donne le point de coordonnées 1 "
                "virgule 2 et 0. Une vérification numérique sur un point "
                "particulier confirme ce résultat."
            )
        ) as tracker:
            self.play(FadeIn(exemple7))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple7))

        # --- Exemple résolu 8 (cas k'k=1) -------------------------------------
        enonce8 = MathTex(r"O(0\,;\,0), \quad O'(4\,;\,0), \quad h=h_{(O,2)}, \quad h'=h_{(O',1/2)}", font_size=24)
        calc8a = MathTex(r"k'k = 1 \implies h'\circ h \text{ est une translation}", font_size=24)
        calc8b = MathTex(r"h(O)=O=(0;0), \quad h'(0;0) = (2;0)", font_size=22)
        calc8c = MathTex(r"\implies h'\circ h = t_{(2\,;\,0)}", font_size=26, color=YELLOW)
        exemple8 = example_box(VGroup(enonce8, calc8a, calc8b, calc8c).arrange(DOWN, buff=0.25))
        exemple8.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Second exemple, cette fois avec un produit de rapports "
                "égal à 1 : soit O l'origine, O prime le point 4 et 0, h "
                "de rapport 2 et centre O, h prime de rapport un demi et "
                "centre O prime. Le produit vaut 1 : la composée est une "
                "translation. Pour trouver son vecteur, il suffit "
                "d'observer l'image d'un point commode : O est fixe par h, "
                "donc son image par la composée est directement l'image de "
                "O par h prime, qui vaut ici le point 2 et 0. La composée "
                "est donc la translation de vecteur 2, 0."
            )
        ) as tracker:
            self.play(FadeIn(exemple8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple8))

        # --- À retenir + piège --------------------------------------------------
        retenir = theorem_box(
            VGroup(
                MathTex(r"k'k\neq 1 \implies \text{homoth\'etie de rapport } k'k,\ \text{centre calcul\'e}", font_size=24),
                MathTex(r"k'k = 1 \implies \text{translation}", font_size=24),
            ).arrange(DOWN, buff=0.25)
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : quand les centres diffèrent, seul le produit "
                "des rapports détermine la nature de la composée — "
                "homothétie si ce produit est différent de 1, translation "
                "sinon — mais le centre de l'homothétie doit toujours être "
                "calculé, il n'est jamais donné d'avance."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        piege = warning_box(
            Text(
                _wrap(
                    "Piège : le centre Ω de la composée n'est en général NI O "
                    "NI O' — il faut le calculer, souvent aligné sur (OO') mais "
                    "distinct des deux centres de départ."
                ),
                font_size=22,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter absolument : le centre Oméga de la "
                "composée n'est en général ni O, ni O prime. Il est bien "
                "aligné avec ces deux points, mais distinct des deux, et "
                "doit systématiquement être calculé."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
