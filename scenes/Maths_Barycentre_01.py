"""
scenes/Maths_Barycentre_01.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 01.

§ Mise en situation (tige en équilibre, centre de gravité, moyenne
pondérée), théorème d'existence et d'unicité du barycentre de deux points
pondérés, définitions (point pondéré, barycentre de deux points pondérés),
remarque sur le cas α+β=0.
Source : 1ereC/Maths.pdf, chapitre 4, pages 41-42.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    Triangle,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=30, dot_color=YELLOW):
    d = Dot(point, color=dot_color)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class ExistenceUniciteDeuxPoints(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation -------------------------------------
        titre = scene_title("Barycentre — Existence et unicité (2 points)")
        titre.scale(0.5)
        titre.to_edge(UP)

        tige = Line(LEFT * 2.5, RIGHT * 2.5, color=WHITE)
        appui = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1).scale(0.25)
        appui.next_to(tige, DOWN, buff=0)
        masse_a = Dot(tige.get_left(), color="#DE7C1F", radius=0.18)
        masse_b = Dot(tige.get_right(), color="#1E5FA8", radius=0.12)
        label_a = MathTex("A", font_size=30).next_to(masse_a, UP, buff=0.2)
        label_b = MathTex("B", font_size=30).next_to(masse_b, UP, buff=0.2)
        schema_tige = VGroup(tige, appui, masse_a, masse_b, label_a, label_b)
        schema_tige.move_to(DOWN * 1.0)

        mise_en_situation = Text(
            _wrap(
                "Une tige tient en équilibre sur un point d'appui quand ce "
                "point est placé au bon endroit, selon les masses fixées à "
                "chaque extrémité. En mathématiques, on retrouve la même "
                "idée dans la moyenne pondérée d'un élève : chaque note "
                "compte avec un « poids » différent (coefficient).",
                width=54,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une tige tient en équilibre sur un point d'appui lorsque "
                "ce point est placé au bon endroit, en fonction des masses "
                "fixées à chaque extrémité. En mathématiques, on retrouve "
                "exactement la même idée dans la moyenne pondérée d'un "
                "élève : chaque note compte avec un poids différent, un "
                "coefficient. Le point d'équilibre de la tige, comme la "
                "moyenne pondérée, sont deux exemples d'un seul et même "
                "objet mathématique : le barycentre. Existe-t-il toujours, "
                "et est-il toujours unique ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(Create(schema_tige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(schema_tige))

        # --- Raisonnement : théorème d'existence et unicité -----------------
        enonce_theoreme = MathTex(
            r"\text{Soient } A, B \text{ deux points et } \alpha,\beta \in \mathbb{R}"
            r"\text{ tels que } \alpha+\beta \neq 0.",
            font_size=26,
        )
        formule_theoreme = MathTex(
            r"\exists !\ G \ \big/\ \alpha\,\overrightarrow{GA} + \beta\,\overrightarrow{GB} = \vec{0}",
            font_size=30,
        )
        theoreme_content = VGroup(enonce_theoreme, formule_theoreme).arrange(DOWN, buff=0.3)
        theoreme = theorem_box(theoreme_content)
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le théorème fondamental. Soient A et B deux points, "
                "et alpha, bêta deux réels tels que leur somme ne soit pas "
                "nulle. Alors il existe un unique point G tel que alpha "
                "fois le vecteur G-A, plus bêta fois le vecteur G-B, soit "
                "égal au vecteur nul. Démontrons ce résultat."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        chasles = MathTex(
            r"\overrightarrow{GB} = \overrightarrow{GA} + \overrightarrow{AB} \quad (\text{relation de Chasles})",
            font_size=27,
        )
        etape2 = MathTex(
            r"\alpha\,\overrightarrow{GA} + \beta\left(\overrightarrow{GA}+\overrightarrow{AB}\right) = \vec{0}",
            font_size=27,
        )
        etape3 = MathTex(
            r"(\alpha+\beta)\,\overrightarrow{GA} = -\beta\,\overrightarrow{AB}",
            font_size=27,
        )
        etape4 = MathTex(
            r"\overrightarrow{AG} = \dfrac{\beta}{\alpha+\beta}\,\overrightarrow{AB} \quad (\alpha+\beta \neq 0)",
            font_size=29,
            color=YELLOW,
        )
        demo = VGroup(chasles, etape2, etape3, etape4).arrange(DOWN, buff=0.4)
        demo.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On remplace le vecteur G-B grâce à la relation de Chasles "
                "par le vecteur G-A plus le vecteur A-B. L'équation devient "
                "alpha G-A plus bêta, fois G-A plus A-B, égal au vecteur "
                "nul. En regroupant les termes en G-A, on obtient : alpha "
                "plus bêta, fois le vecteur G-A, égal à moins bêta fois le "
                "vecteur A-B. Comme alpha plus bêta est non nul, on peut "
                "diviser : le vecteur A-G est égal à bêta sur alpha plus "
                "bêta, fois le vecteur A-B. Cette égalité détermine un "
                "unique point G, entièrement défini à partir de A et B : "
                "c'est à la fois la preuve de l'existence et de l'unicité."
            )
        ) as tracker:
            self.play(Write(chasles))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.play(Write(etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité : définitions + cas α=β=1 (milieu) ---------------
        def_point_pondere = definition_box(
            VGroup(
                Text("Point pondéré", font_size=25, weight="BOLD"),
                MathTex(r"(A\,;\,\alpha),\ \alpha \in \mathbb{R}", font_size=28),
                Text(
                    _wrap("Un couple formé d'un point et d'un réel appelé coefficient (ou masse) du point.", width=44),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_point_pondere.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Précisons le vocabulaire. Un point pondéré est un couple "
                "formé d'un point, A par exemple, et d'un nombre réel alpha "
                "appelé coefficient, ou masse, de ce point. On le note "
                "A, point-virgule, alpha, entre parenthèses."
            )
        ) as tracker:
            self.play(FadeIn(def_point_pondere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_point_pondere))

        def_barycentre = definition_box(
            VGroup(
                Text("Barycentre de deux points pondérés", font_size=24, weight="BOLD"),
                MathTex(
                    r"\alpha+\beta \neq 0 \ \Rightarrow\ G = \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\}",
                    font_size=27,
                ),
                Text(
                    _wrap("G est l'unique point tel que α GA⃗ + β GB⃗ = 0⃗.", width=44),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_barycentre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le barycentre des points pondérés A-alpha et B-bêta, "
                "lorsque alpha plus bêta est non nul, est ce point G, noté "
                "G égale bar, ouvre accolade, A virgule alpha, "
                "point-virgule, B virgule bêta, ferme accolade."
            )
        ) as tracker:
            self.play(FadeIn(def_barycentre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_barycentre))

        a_pt = LEFT * 3
        b_pt = RIGHT * 3
        ligne_ab = Line(a_pt, b_pt, color=WHITE)
        pa = _dot_label(a_pt, "A")
        pb = _dot_label(b_pt, "B")
        pg = _dot_label((a_pt + b_pt) / 2, "G", dot_color="#288073", label_dir=DOWN)
        figure_milieu = VGroup(ligne_ab, pa, pb, pg)
        figure_milieu.move_to(DOWN * 0.5)

        calcul_milieu = MathTex(
            r"\alpha=\beta=1 \ \Rightarrow\ \overrightarrow{AG} = \dfrac{1}{2}\,\overrightarrow{AB}"
            r"\ \Rightarrow\ G = \text{milieu de } [AB]",
            font_size=26,
        )
        calcul_milieu.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Regardons un cas particulier familier : si alpha égale "
                "bêta égale un, la formule donne le vecteur A-G égale un "
                "demi, fois le vecteur A-B : G est alors le milieu du "
                "segment A-B. Le barycentre généralise donc la notion de "
                "milieu."
            )
        ) as tracker:
            self.play(FadeIn(calcul_milieu))
            self.play(Create(figure_milieu))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_milieu), FadeOut(figure_milieu))

        # --- À retenir ---------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(
                    r"\alpha+\beta \neq 0 \ \Longrightarrow\ \exists !\ G = \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\}",
                    font_size=27,
                ),
                MathTex(
                    r"\alpha\,\overrightarrow{GA} + \beta\,\overrightarrow{GB} = \vec{0}",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : dès que la somme des coefficients alpha plus "
                "bêta est non nulle, il existe un unique barycentre G des "
                "points pondérés A-alpha et B-bêta, caractérisé par la "
                "relation vectorielle alpha G-A plus bêta G-B égale le "
                "vecteur nul."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter : cas α+β=0 -----------------------------------------
        piege = warning_box(
            VGroup(
                MathTex(r"\alpha+\beta=0 \text{ et } A\neq B \ \Rightarrow\ \text{aucun point } G \text{ ne convient}", font_size=25),
                Text(
                    _wrap(
                        "Le vecteur α GA⃗+β GB⃗ devient alors constant, égal à α BA⃗ "
                        "(non nul) : il ne peut donc jamais être nul.",
                        width=46,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention au piège : avant de parler du barycentre de deux "
                "points, vérifiez toujours que la somme des coefficients "
                "n'est pas nulle. Si alpha plus bêta est nul et que A est "
                "différent de B, aucun point G ne convient : le vecteur "
                "alpha G-A plus bêta G-B devient constant, égal à alpha "
                "fois le vecteur B-A, qui est non nul, et ne peut donc "
                "jamais s'annuler. Nous reviendrons sur ce cas particulier "
                "un peu plus loin dans le chapitre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
