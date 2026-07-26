"""
scenes/Maths_Denombrement_05.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 05.

§ Les p-listes (p-uplets) : définition (ordonné, répétitions possibles),
théorème du nombre de p-listes = n^p avec démonstration. Exemple résolu 3
(code de serrure, 3 chiffres + 2 voyelles, 36000 codes). Propriété admise
du nombre d'applications de E vers F.
Source : 1ereC/Maths.pdf, chapitre 6, pages 70-71.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class PListes(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Les p-listes")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définition -------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("p-liste (ou p-uplet) d'un ensemble E", font_size=23, weight="BOLD"),
                MathTex(
                    r"(x_1, x_2, \dots, x_p) \text{ avec } x_i \in E \text{ pour tout } i",
                    font_size=25,
                ),
                Text(
                    _wrap(
                        "C'est une liste ORDONNÉE de p éléments de E : "
                        "l'ordre compte, et les répétitions sont autorisées "
                        "(un même élément peut apparaître plusieurs fois).",
                        width=50,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici une nouvelle famille d'objets à dénombrer : les "
                "p-listes, aussi appelées p-uplets, d'un ensemble E. Une "
                "p-liste est une liste ordonnée de p éléments de E, notée "
                "x-1, x-2, jusqu'à x-p. Deux points essentiels : l'ordre "
                "compte, et un même élément de E peut apparaître "
                "plusieurs fois dans la liste, les répétitions sont "
                "autorisées."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : théorème n^p avec démonstration -----------------------
        theo = theorem_box(
            VGroup(
                Text("Nombre de p-listes", font_size=23, weight="BOLD"),
                MathTex(
                    r"\mathrm{Card}(E)=n \ \Longrightarrow\ \text{nombre de } p\text{-listes de } E \ = \ n^{p}",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le théorème est le suivant : si E a n éléments, alors le "
                "nombre de p-listes de E vaut n puissance p."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        demo1 = MathTex(
            r"\text{Une } p\text{-liste } (x_1,\dots,x_p) \in E^p \text{ : } p \text{ choix successifs indépendants}",
            font_size=23,
        )
        demo2 = MathTex(
            r"x_1 : n \text{ choix} \quad x_2 : n \text{ choix} \quad \cdots \quad x_p : n \text{ choix}",
            font_size=24,
        )
        demo3 = MathTex(
            r"\text{Principe multiplicatif : } \underbrace{n \times n \times \cdots \times n}_{p \text{ facteurs}} = n^{p}",
            font_size=25,
            color="#DE7C1F",
        )
        demo = VGroup(demo1, demo2, demo3).arrange(DOWN, buff=0.35)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démontrons-le. Une p-liste x-1 jusqu'à x-p est un élément "
                "du produit cartésien E puissance p : la construire "
                "revient à faire p choix successifs et indépendants, "
                "puisque les répétitions sont permises. Pour x-1, il y a n "
                "choix ; pour x-2, encore n choix, et ainsi de suite "
                "jusqu'à x-p, toujours n choix. Le principe multiplicatif "
                "donne alors n fois n, répété p fois, soit n puissance p."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité : code de serrure ------------------------------------
        enonce_code = Text(
            _wrap(
                "Exemple résolu 3 : un code de serrure est formé de 3 "
                "chiffres (parmi 0 à 9, répétitions permises) suivis de 2 "
                "voyelles (parmi a, e, i, o, u, y). Combien de codes "
                "distincts existe-t-il ?",
                width=54,
            ),
            font_size=23,
        )
        enonce_code.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Appliquons ceci à un exemple concret. Un code de serrure "
                "est formé de 3 chiffres, choisis parmi 0 à 9 avec "
                "répétitions permises, suivis de 2 voyelles, choisies "
                "parmi les six voyelles françaises a, e, i, o, u, y. "
                "Combien de codes distincts existe-t-il ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_code))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_code))

        calcul_code = MathTex(
            r"\underbrace{10^{3}}_{\text{3 chiffres}} \times \underbrace{6^{2}}_{\text{2 voyelles}}"
            r" = 1000 \times 36 = 36\,000 \text{ codes}",
            font_size=25,
            color="#DE7C1F",
        )
        calcul_code.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le bloc de 3 chiffres est une 3-liste de l'ensemble des "
                "dix chiffres : il y a 10 puissance 3, soit mille "
                "possibilités. Le bloc de 2 voyelles est une 2-liste de "
                "l'ensemble des 6 voyelles : il y a 6 puissance 2, soit "
                "trente-six possibilités. Par le principe multiplicatif, "
                "le nombre total de codes est mille fois trente-six, soit "
                "trente-six mille codes distincts."
            )
        ) as tracker:
            self.play(Write(calcul_code))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_code))

        # --- À retenir : propriété admise des applications ------------------------
        prop_applications = property_box(
            VGroup(
                Text("Nombre d'applications (admise)", font_size=23, weight="BOLD"),
                MathTex(
                    r"\mathrm{Card}(E)=p,\ \ \mathrm{Card}(F)=n \ \Longrightarrow\ "
                    r"\text{nombre d'applications de } E \text{ vers } F \ = \ n^{p}",
                    font_size=24,
                ),
                Text(
                    _wrap(
                        "Une application de E vers F associe à chacun des p "
                        "éléments de E une image dans F : c'est exactement une "
                        "p-liste d'éléments de F.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        prop_applications.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir enfin, une propriété admise, très proche du "
                "résultat sur les p-listes : si E a p éléments et F a n "
                "éléments, le nombre d'applications de E vers F vaut lui "
                "aussi n puissance p. En effet, se donner une application "
                "de E vers F revient à choisir, pour chacun des p éléments "
                "de E, une image dans F : c'est exactement une p-liste "
                "d'éléments de F."
            )
        ) as tracker:
            self.play(FadeIn(prop_applications))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_applications), FadeOut(titre))
