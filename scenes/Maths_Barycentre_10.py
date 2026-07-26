"""
scenes/Maths_Barycentre_10.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 10.

§ Lignes de niveau aMA²+bMB²=k : théorème (cas a+b≠0 → ∅, point ou cercle
selon le signe d'un réel ρ ; cas a+b=0 → droite perpendiculaire à (AB)),
avec démonstration complète des deux cas.
Source : 1ereC/Maths.pdf, chapitre 4, pages 48-49.
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
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class LignesDeNiveauCarrees(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Lignes de niveau aMA² + bMB² = k")
        titre.scale(0.44)
        titre.to_edge(UP)

        question = Text(
            _wrap(
                "Quel est l'ensemble des points M du plan vérifiant "
                "a·MA² + b·MB² = k, pour a, b, k réels donnés ?",
                width=52,
            ),
            font_size=25,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étudions maintenant les lignes de niveau. Étant donnés "
                "deux points A et B et trois réels a, b et k, quel est "
                "l'ensemble des points M du plan vérifiant a fois M-A au "
                "carré, plus b fois M-B au carré, égale k ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : théorème complet ------------------------------------
        enonce = VGroup(
            MathTex(r"f(M) = a\,MA^2+b\,MB^2 = k, \quad G=\mathrm{bar}\{(A,a)\,;\,(B,b)\}", font_size=22),
            MathTex(r"a+b\neq 0 \ \Rightarrow\ \varnothing,\ \{G\} \text{ ou cercle de centre } G", font_size=22),
            MathTex(r"a+b = 0 \ \Rightarrow\ \text{droite perpendiculaire à } (AB)", font_size=22),
        ).arrange(DOWN, buff=0.28)
        theoreme = theorem_box(enonce)
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le théorème. Notons f de M cette quantité, et G le "
                "barycentre de A-a et B-b, lorsqu'il existe. Si a plus b "
                "est non nul, la ligne de niveau est, selon les cas, "
                "l'ensemble vide, un seul point G, ou un cercle de centre "
                "G. Si a plus b est nul, la ligne de niveau est une "
                "droite perpendiculaire à la droite A-B. Démontrons "
                "successivement ces deux cas."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Démonstration cas a+b ≠ 0 -------------------------------------------
        cas1_titre = Text("Cas a+b ≠ 0", font_size=25, color=YELLOW, weight="BOLD")
        cas1_titre.next_to(titre, DOWN, buff=0.35)

        etape1 = MathTex(
            r"\overrightarrow{MA}=\overrightarrow{MG}+\overrightarrow{GA}"
            r"\ \Rightarrow\ MA^2 = MG^2+2\,\overrightarrow{MG}\cdot\overrightarrow{GA}+GA^2",
            font_size=21,
        )
        etape2 = MathTex(
            r"a\,MA^2+b\,MB^2 = (a+b)MG^2 + 2\,\overrightarrow{MG}\cdot\underbrace{(a\overrightarrow{GA}+b\overrightarrow{GB})}_{=\ \vec{0}\ (\text{déf. de }G)} + \underbrace{a\,GA^2+b\,GB^2}_{=\ \rho}",
            font_size=18,
        )
        etape3 = MathTex(r"f(M) = (a+b)\,MG^2+\rho, \quad \rho = a\,GA^2+b\,GB^2 \ (\text{constante})", font_size=22, color=YELLOW)
        etape4 = MathTex(
            r"f(M)=k \ \Leftrightarrow\ MG^2 = \dfrac{k-\rho}{a+b}",
            font_size=25,
        )
        demo1 = VGroup(etape1, etape2, etape3, etape4).arrange(DOWN, buff=0.3)
        demo1.next_to(cas1_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premier cas : a plus b est non nul. On introduit G par "
                "Chasles dans M-A et dans M-B, puis on développe les "
                "carrés scalaires. Le terme croisé disparaît car a fois "
                "G-A, plus b fois G-B, est nul par définition de G. Il "
                "reste f de M égale a plus b, fois M-G au carré, plus une "
                "constante rho, égale à a G-A au carré plus b G-B au "
                "carré. L'équation f de M égale k équivaut donc à M-G au "
                "carré égale k moins rho, sur a plus b."
            )
        ) as tracker:
            self.play(FadeIn(cas1_titre))
            self.play(Write(demo1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas1_titre), FadeOut(demo1))

        discussion = VGroup(
            MathTex(r"\dfrac{k-\rho}{a+b} < 0 \ \Rightarrow\ \text{aucun point : } \varnothing", font_size=23),
            MathTex(r"\dfrac{k-\rho}{a+b} = 0 \ \Rightarrow\ MG=0 \ \Rightarrow\ \{G\}", font_size=23),
            MathTex(r"\dfrac{k-\rho}{a+b} > 0 \ \Rightarrow\ MG=\sqrt{\dfrac{k-\rho}{a+b}} \ \Rightarrow\ \text{cercle de centre } G", font_size=23),
        ).arrange(DOWN, buff=0.3)
        discussion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Il reste à discuter selon le signe de k moins rho, sur a "
                "plus b. Un carré ne peut pas être négatif : si cette "
                "quantité est strictement négative, aucun point M ne "
                "convient, l'ensemble est vide. Si elle est nulle, M-G "
                "vaut zéro, donc M est confondu avec G. Si elle est "
                "strictement positive, M-G est égal à sa racine carrée : "
                "l'ensemble cherché est le cercle de centre G et de ce "
                "rayon."
            )
        ) as tracker:
            self.play(Write(discussion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(discussion))

        # --- Démonstration cas a+b = 0 -------------------------------------------
        cas2_titre = Text("Cas a+b = 0 (soit b = -a, a≠0)", font_size=24, color=YELLOW, weight="BOLD")
        cas2_titre.next_to(titre, DOWN, buff=0.35)

        d_etape1 = MathTex(r"f(M) = a\,MA^2-a\,MB^2 = a\big(MA^2-MB^2\big)", font_size=23)
        d_etape2 = MathTex(
            r"MA^2-MB^2 = \big(\overrightarrow{MA}-\overrightarrow{MB}\big)\cdot\big(\overrightarrow{MA}+\overrightarrow{MB}\big)"
            r" = \overrightarrow{BA}\cdot 2\overrightarrow{MI}",
            font_size=21,
        )
        d_etape3 = Text("où I est le milieu de [AB] (car MA⃗+MB⃗=2 MI⃗).", font_size=19)
        d_etape4 = MathTex(r"f(M) = 2a\,\overrightarrow{BA}\cdot\overrightarrow{MI}", font_size=24, color=YELLOW)
        d_etape5 = MathTex(
            r"f(M)=k \ \Leftrightarrow\ \overrightarrow{BA}\cdot\overrightarrow{MI} = \dfrac{k}{2a} \ (\text{constante})",
            font_size=23,
        )
        d_etape6 = Text("→ droite perpendiculaire à (AB), car BA⃗ est un vecteur fixe non nul.", font_size=19)
        demo2 = VGroup(d_etape1, d_etape2, d_etape3, d_etape4, d_etape5, d_etape6).arrange(DOWN, buff=0.22)
        demo2.next_to(cas2_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Second cas : a plus b égale zéro, donc b égale moins a, "
                "avec a non nul. On factorise : f de M égale a, fois M-A "
                "au carré moins M-B au carré. On utilise l'identité "
                "remarquable : M-A au carré moins M-B au carré est le "
                "produit scalaire de M-A moins M-B, par M-A plus M-B. Or "
                "M-A moins M-B vaut B-A par Chasles, et M-A plus M-B vaut "
                "deux fois M-I, où I est le milieu de A-B. On obtient f "
                "de M égale deux a, fois le produit scalaire de B-A et "
                "M-I. L'équation f de M égale k équivaut alors à B-A "
                "scalaire M-I égale k sur deux a, une constante : c'est "
                "l'équation d'une droite perpendiculaire à A-B, puisque "
                "B-A est un vecteur fixe non nul."
            )
        ) as tracker:
            self.play(FadeIn(cas2_titre))
            self.play(Write(demo2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas2_titre), FadeOut(demo2))

        # --- Exemple traité : deux illustrations rapides ---------------------------
        a_pt = LEFT * 3
        b_pt = RIGHT * 1
        g_pt = a_pt + (2 / 3) * (b_pt - a_pt)
        cercle = Circle(radius=1.1, color="#288073").move_to(g_pt)
        pa = _dot_label(a_pt, "A")
        pb = _dot_label(b_pt, "B")
        pg = _dot_label(g_pt, "G", dot_color="#288073", label_dir=DOWN)
        illustration_cercle = VGroup(cercle, pa, pb, pg)
        illustration_cercle.scale(0.75).shift(LEFT * 3.2 + DOWN * 1.5)

        milieu = (a_pt + b_pt) / 2
        droite_perp = Line(milieu + UP * 1.3, milieu + DOWN * 1.3, color="#B42E41")
        pa2 = _dot_label(a_pt, "A")
        pb2 = _dot_label(b_pt, "B")
        illustration_droite = VGroup(Line(a_pt, b_pt, color=WHITE), droite_perp, pa2, pb2)
        illustration_droite.scale(0.75).shift(RIGHT * 3.2 + DOWN * 1.5)

        legende = Text("Cas cercle (a+b≠0)              Cas droite perpendiculaire (a+b=0)", font_size=20)
        legende.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux illustrations rapides : quand a plus b est non nul "
                "et que la quantité k moins rho sur a plus b est "
                "strictement positive, on obtient bien un cercle centré "
                "en G. Quand a plus b est nul, on obtient une droite, "
                "toujours perpendiculaire à A-B."
            )
        ) as tracker:
            self.play(FadeIn(legende))
            self.play(Create(illustration_cercle), Create(illustration_droite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(legende), FadeOut(illustration_cercle), FadeOut(illustration_droite))

        # --- À retenir -----------------------------------------------------------
        retenir = theorem_box(
            VGroup(
                MathTex(r"a+b\neq 0:\ MG^2=\dfrac{k-\rho}{a+b} \ \Rightarrow\ \varnothing,\ \{G\}\text{ ou cercle}", font_size=21),
                MathTex(r"a+b=0:\ \overrightarrow{BA}\cdot\overrightarrow{MI}=\text{cste} \ \Rightarrow\ \text{droite}\perp(AB)", font_size=21),
            ).arrange(DOWN, buff=0.25),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : selon le signe de a plus b, la ligne de "
                "niveau a M-A carré plus b M-B carré égale k est soit "
                "vide, réduite à un point, ou un cercle centré en G ; "
                "soit une droite perpendiculaire à A-B."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne concluez jamais « c'est un cercle » sans avoir "
                    "vérifié le signe de (k-ρ)/(a+b) : si cette quantité "
                    "est négative, l'ensemble est vide, pas un cercle "
                    "« de rayon imaginaire ».",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter : ne concluez jamais qu'il s'agit d'un "
                "cercle sans avoir vérifié le signe de k moins rho, sur a "
                "plus b. Si cette quantité est strictement négative, "
                "l'ensemble cherché est simplement vide, il n'existe pas "
                "de cercle de rayon imaginaire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
