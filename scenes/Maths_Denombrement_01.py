"""
scenes/Maths_Denombrement_01.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 01.

§ Ensembles finis et cardinal : définition, notation Card(E), 3 techniques
de dénombrement (comptage direct, diagrammes, arbres). Ensemble des parties
𝒫(E), exemple E={a,b,c}. Propriété (admise) Card(𝒫(E))=2ⁿ.
Source : 1ereC/Maths.pdf, chapitre 6, pages 66-67.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    ORIGIN,
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
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _technique_comptage() -> VGroup:
    titre = Text("Comptage direct", font_size=20, weight="BOLD", color=YELLOW)
    liste = Text("a, b, c\n→ 3 éléments", font_size=20)
    bloc = VGroup(titre, liste).arrange(DOWN, buff=0.25)
    return bloc


def _technique_diagramme() -> VGroup:
    titre = Text("Diagramme", font_size=20, weight="BOLD", color=YELLOW)
    cercle = Circle(radius=0.7, color=WHITE)
    pts = VGroup(
        *[
            VGroup(Dot(p, radius=0.05), MathTex(lab, font_size=22)).arrange(RIGHT, buff=0.1)
            for p, lab in zip(
                [cercle.point_at_angle(1.5), cercle.point_at_angle(3.6), cercle.point_at_angle(5.6)],
                ["a", "b", "c"],
            )
        ]
    ).arrange(DOWN, buff=0.15)
    pts.move_to(cercle.get_center())
    schema = VGroup(cercle, pts)
    bloc = VGroup(titre, schema).arrange(DOWN, buff=0.25)
    return bloc


def _technique_arbre() -> VGroup:
    titre = Text("Arbre", font_size=20, weight="BOLD", color=YELLOW)
    racine = Dot(ORIGIN, radius=0.05)
    feuilles = [Dot(racine.get_center() + DOWN * 0.9 + RIGHT * dx, radius=0.05) for dx in (-0.7, 0, 0.7)]
    branches = VGroup(*[Line(racine.get_center(), f.get_center(), color=WHITE) for f in feuilles])
    labels = VGroup(
        *[
            MathTex(lab, font_size=22).next_to(f, DOWN, buff=0.1)
            for f, lab in zip(feuilles, ["a", "b", "c"])
        ]
    )
    schema = VGroup(branches, racine, *feuilles, labels)
    bloc = VGroup(titre, schema).arrange(DOWN, buff=0.25)
    return bloc


class EnsemblesFinisCardinal(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ----------------------------------
        titre = scene_title("Dénombrement — Ensembles finis et cardinal")
        titre.scale(0.5)
        titre.to_edge(UP)

        mise_en_situation = Text(
            _wrap(
                "Compter le nombre d'élèves d'une classe, le nombre de "
                "façons de s'habiller le matin, le nombre de codes "
                "possibles d'un cadenas : dénombrer, c'est compter le "
                "nombre d'éléments d'un ensemble fini.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Compter le nombre d'élèves d'une classe, le nombre de "
                "façons de s'habiller le matin, ou le nombre de codes "
                "possibles d'un cadenas : dans tous ces cas, on cherche à "
                "dénombrer, c'est-à-dire à compter le nombre d'éléments "
                "d'un ensemble fini. C'est tout l'objet de ce chapitre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition ensemble fini + cardinal ----------
        def_ensemble = definition_box(
            VGroup(
                Text("Ensemble fini — Cardinal", font_size=24, weight="BOLD"),
                MathTex(
                    r"E \text{ est fini s'il possède un nombre fini d'éléments.}",
                    font_size=25,
                ),
                MathTex(
                    r"\mathrm{Card}(E) \text{ (ou } \#E \text{) : le nombre d'éléments de } E.",
                    font_size=25,
                ),
                MathTex(r"E=\{a\,;\,b\,;\,c\} \ \Rightarrow\ \mathrm{Card}(E)=3", font_size=26, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
        )
        def_ensemble.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un ensemble E est dit fini s'il possède un nombre fini "
                "d'éléments. Ce nombre d'éléments s'appelle le cardinal de "
                "E, noté Card de E, ou parfois dièse E. Par exemple, si E "
                "est l'ensemble a, b, c, alors Card de E vaut 3."
            )
        ) as tracker:
            self.play(FadeIn(def_ensemble))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ensemble))

        # --- 3 techniques de dénombrement ---------------------------------
        soustitre = Text("Trois techniques de dénombrement", font_size=26, weight="BOLD")
        soustitre.next_to(titre, DOWN, buff=0.4)

        techniques = VGroup(
            _technique_comptage(), _technique_diagramme(), _technique_arbre()
        ).arrange(RIGHT, buff=1.0)
        techniques.next_to(soustitre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour dénombrer un ensemble, on dispose de trois "
                "techniques principales. Le comptage direct, quand la "
                "liste des éléments est courte. Les diagrammes, qui "
                "représentent visuellement les éléments à l'intérieur "
                "d'un contour. Et les arbres, qui listent les éléments "
                "comme les feuilles d'une structure ramifiée. Nous "
                "utiliserons ces trois outils tout au long du chapitre."
            )
        ) as tracker:
            self.play(Write(soustitre))
            self.play(Create(techniques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(soustitre), FadeOut(techniques))

        # --- Exemple traité : ensemble des parties -------------------------
        def_parties = definition_box(
            VGroup(
                Text("Ensemble des parties de E", font_size=24, weight="BOLD"),
                MathTex(
                    r"\mathcal{P}(E) = \{\, A \ /\ A \subset E \,\}",
                    font_size=27,
                ),
                Text(
                    _wrap("𝒫(E) est l'ensemble de TOUS les sous-ensembles de E, y compris ∅ et E lui-même.", width=46),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_parties.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Introduisons maintenant l'ensemble des parties de E, "
                "noté P calligraphié de E. C'est l'ensemble de TOUS les "
                "sous-ensembles de E, y compris l'ensemble vide et E "
                "lui-même."
            )
        ) as tracker:
            self.play(FadeIn(def_parties))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_parties))

        exemple_parties = MathTex(
            r"E=\{a\,;\,b\,;\,c\} \ \Rightarrow\ \mathcal{P}(E) = \Big\{\ "
            r"\emptyset,\ \{a\},\ \{b\},\ \{c\},\ \{a,b\},\ \{a,c\},\ \{b,c\},\ \{a,b,c\}\ \Big\}",
            font_size=24,
        )
        exemple_parties.next_to(titre, DOWN, buff=0.6)
        compte_parties = MathTex(r"\mathrm{Card}\big(\mathcal{P}(E)\big) = 8", font_size=28, color=YELLOW)
        compte_parties.next_to(exemple_parties, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons E égale a, b, c. Ses huit parties sont : "
                "l'ensemble vide, les trois singletons a, b et c, les "
                "trois paires a-b, a-c et b-c, et enfin E tout entier. "
                "On compte donc huit parties en tout."
            )
        ) as tracker:
            self.play(Write(exemple_parties))
            self.play(FadeIn(compte_parties))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_parties), FadeOut(compte_parties))

        # --- À retenir : propriété admise -----------------------------------
        prop_card = property_box(
            VGroup(
                Text("Cardinal de l'ensemble des parties (admise)", font_size=23, weight="BOLD"),
                MathTex(
                    r"\mathrm{Card}(E) = n \ \Longrightarrow\ \mathrm{Card}\big(\mathcal{P}(E)\big) = 2^{n}",
                    font_size=28,
                ),
                MathTex(r"\text{Ici : } n=3 \ \Rightarrow\ 2^3 = 8 \ \checkmark", font_size=25, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
        )
        prop_card.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons cette propriété, admise pour l'instant, nous la "
                "justifierons plus tard dans le chapitre grâce au binôme "
                "de Newton : si E a n éléments, alors l'ensemble des "
                "parties de E a exactement 2 puissance n éléments. "
                "Vérification sur notre exemple : n égale 3, et 2 "
                "puissance 3 égale bien 8, le compte que nous avions "
                "trouvé à la main."
            )
        ) as tracker:
            self.play(FadeIn(prop_card))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_card), FadeOut(titre))
