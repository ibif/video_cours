"""
scenes/Maths_ComposeesTransformationsPlan_10.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 10.

§ Composée de deux homothéties de même centre : h'∘h = h(O, k'k)
(homothétie, rapport produit, commutative), démonstration, cas
particuliers (k'k=1 → identité ; k'k=-1 → symétrie centrale), exemple
résolu 6 (h1=h(Ω,2), h2=h(Ω,-3)).
Source : 1ereC/Maths.pdf, chapitre 8, pages 101-102.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Create, Dot, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.08)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class ComposeeHomothetiesMemeCentre(NotionScene):
    def construct(self):
        titre = scene_title("Composée de 2 homothéties — même centre")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : théorème --------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Composée de deux homothéties de même centre", font_size=22, weight="BOLD"),
                MathTex(r"h=h_{(O,k)}, \quad h'=h_{(O,k')}", font_size=27),
                MathTex(r"h'\circ h = h_{(O,\,k'k)}", font_size=32),
                Text(_wrap("Homothétie de même centre, de rapport le produit des rapports. Commutative."), font_size=21),
            ).arrange(DOWN, buff=0.22)
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attaquons maintenant les homothéties, en commençant par "
                "le cas où les deux centres coïncident. Soit h l'homothétie "
                "de centre O et de rapport k, et h prime celle de même "
                "centre O et de rapport k prime. Leur composée h prime "
                "rond h est encore une homothétie de centre O, dont le "
                "rapport est le produit k prime fois k. Et comme la "
                "multiplication est commutative, cette composition l'est "
                "aussi."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration -----------------------------------
        etape1 = MathTex(r"M_1 = h(M) \implies \overrightarrow{OM_1} = k\,\overrightarrow{OM}", font_size=26)
        etape2 = MathTex(r"M' = h'(M_1) \implies \overrightarrow{OM'} = k'\,\overrightarrow{OM_1} = k'k\,\overrightarrow{OM}", font_size=26)
        etape3 = MathTex(r"\implies h'\circ h = h_{(O,\,k'k)}", font_size=28, color=YELLOW)
        demo = VGroup(etape1, etape2, etape3).arrange(DOWN, buff=0.35)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La démonstration est directe. Pour un point M, son image "
                "M-un par h vérifie le vecteur O M-un égal k fois le "
                "vecteur OM. En appliquant ensuite h prime à M-un, on "
                "obtient M prime tel que le vecteur O M prime égale k "
                "prime fois le vecteur O M-un, c'est-à-dire k prime fois k "
                "fois le vecteur OM. Cette relation, valable pour tout "
                "point M avec un même centre O et un même coefficient k "
                "prime fois k, caractérise exactement l'homothétie de "
                "centre O et de rapport k prime fois k."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Cas particuliers ------------------------------------------------
        cas_part = theorem_box(
            VGroup(
                Text("Cas particuliers", font_size=23, weight="BOLD"),
                MathTex(r"k'k = 1 \implies h'\circ h = \mathrm{id} \quad (h' = h^{-1})", font_size=27),
                MathTex(r"k'k = -1 \implies h'\circ h = s_O \quad (\text{sym\'etrie centrale})", font_size=27),
            ).arrange(DOWN, buff=0.3)
        )
        cas_part.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux cas particuliers à retenir. Si le produit k prime "
                "fois k vaut 1, la composée est l'identité : h prime est "
                "alors la réciproque de h. Et si ce produit vaut moins 1, "
                "la composée est la symétrie centrale de centre O, "
                "puisqu'une homothétie de rapport moins 1 n'est autre "
                "qu'une symétrie centrale."
            )
        ) as tracker:
            self.play(FadeIn(cas_part))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_part))

        # --- Exemple résolu 6 -------------------------------------------------
        enonce = MathTex(r"h_1 = h_{(\Omega,\,2)}, \quad h_2 = h_{(\Omega,\,-3)}", font_size=27)
        calc = MathTex(r"h_2\circ h_1 = h_{(\Omega,\, -3\times 2)} = h_{(\Omega,\,-6)}", font_size=29, color=YELLOW)
        exemple = example_box(VGroup(enonce, calc).arrange(DOWN, buff=0.3))
        exemple.next_to(titre, DOWN, buff=0.4)

        omega_pt = LEFT * 2 + DOWN * 1.5
        pt_omega = _dot_label(omega_pt, "\\Omega", dot_color="#288073", label_dir=DOWN)
        m_pt = omega_pt + RIGHT * 0.8 + UP * 0.5
        pt_m = _dot_label(m_pt, "M")
        m1_pt = omega_pt + 2 * (m_pt - omega_pt)
        pt_m1 = _dot_label(m1_pt, "M_1=h_1(M)", font_size=22)
        seg1 = Line(omega_pt, m1_pt, color="#595959", stroke_width=1.5)
        figure = VGroup(pt_omega, pt_m, pt_m1, seg1)
        figure.scale(0.55)
        figure.next_to(exemple, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : soit h-un l'homothétie de centre Oméga et de "
                "rapport 2, et h-deux celle de même centre Oméga et de "
                "rapport moins 3. Leur composée h-deux rond h-un est "
                "l'homothétie de centre Oméga et de rapport le produit, "
                "moins 3 fois 2, soit moins 6."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.play(Create(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(figure))

        # --- À retenir + piège --------------------------------------------------
        retenir = theorem_box(MathTex(r"h'\circ h = h_{(O,\,k'k)} = h\circ h'", font_size=30))
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : quand le centre est commun, composer deux "
                "homothéties revient simplement à multiplier leurs "
                "rapports, et l'ordre n'a pas d'importance."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        piege = warning_box(
            Text(
                _wrap(
                    "Piège : ce résultat simple (rapport = produit, même centre) "
                    "ne s'applique QUE si les deux homothéties partagent le même "
                    "centre — sinon, tout change, comme le montre la scène suivante."
                ),
                font_size=22,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : ce résultat très simple ne s'applique que "
                "lorsque les deux homothéties partagent le même centre. "
                "Dès que les centres diffèrent, la situation devient plus "
                "riche, comme nous allons le voir dans la scène suivante."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
