"""
scenes/Maths_GeometrieAnalytiquePlan_03.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 03.

§ Déterminant de deux vecteurs : définition det(u,v)=xy'-x'y, propriétés
(antisymétrie, det(u,u)=0, linéarité), critère de colinéarité (théorème et
démonstration complète, sens direct et réciproque). Valable dans TOUT
repère.
Source : 1ereC/Maths.pdf, chapitre 14, pages 167-168.
"""

import textwrap

from manim import DOWN, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DeterminantColinearite(NotionScene):
    def construct(self):
        titre = scene_title("Déterminant de deux vecteurs et colinéarité")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : définition --------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Déterminant de deux vecteurs", font_size=24, weight="BOLD"),
                MathTex(
                    r"\vec{u}(x;y),\ \vec{v}(x';y') \ \Rightarrow\ "
                    r"\det(\vec{u},\vec{v}) = \begin{vmatrix} x & x' \\ y & y' \end{vmatrix} = xy'-x'y",
                    font_size=27,
                ),
                Text(
                    _wrap("Formule valable dans TOUT repère (pas besoin d'orthonormé).", width=44),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici un nouvel outil très puissant : le déterminant de "
                "deux vecteurs. Pour u de coordonnées x et y, et v de "
                "coordonnées x prime et y prime, on définit le déterminant "
                "de u et v, noté avec des barres verticales, comme le "
                "nombre x fois y prime moins x prime fois y. Contrairement "
                "à la norme, cette formule est valable dans n'importe quel "
                "repère, pas seulement orthonormé."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Propriétés -----------------------------------------------------------
        proprietes = property_box(
            VGroup(
                MathTex(r"\det(\vec{v},\vec{u}) = -\det(\vec{u},\vec{v}) \quad \text{(antisymétrie)}", font_size=25),
                MathTex(r"\det(\vec{u},\vec{u}) = 0", font_size=25),
                MathTex(
                    r"\det(k\vec{u},\vec{v}) = k\det(\vec{u},\vec{v})"
                    r"\qquad \det(\vec{u}+\vec{u'},\vec{v}) = \det(\vec{u},\vec{v})+\det(\vec{u'},\vec{v})",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.5,
        )
        proprietes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le déterminant possède plusieurs propriétés utiles. "
                "D'abord, il est antisymétrique : échanger l'ordre des deux "
                "vecteurs change le signe du résultat. Ensuite, le "
                "déterminant d'un vecteur avec lui-même est toujours nul. "
                "Enfin, il est linéaire par rapport à chacun de ses deux "
                "vecteurs : multiplier un vecteur par un réel k multiplie "
                "le déterminant par k, et il se distribue sur une somme de "
                "vecteurs."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Raisonnement : critère de colinéarité + démonstration ---------------
        theoreme = theorem_box(
            MathTex(
                r"\vec{u} \text{ et } \vec{v} \text{ colinéaires} \iff \det(\vec{u},\vec{v}) = 0",
                font_size=29,
            ),
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Ce déterminant sert avant tout à tester la colinéarité de "
                "deux vecteurs : u et v sont colinéaires si et seulement si "
                "leur déterminant est nul. Démontrons cette double "
                "implication."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        sens_direct = VGroup(
            Text("Sens direct : u, v colinéaires ⇒ det(u,v)=0", font_size=22, color=YELLOW),
            MathTex(
                r"\vec{u} = \vec{0} \ \Rightarrow\ x=y=0 \ \Rightarrow\ \det(\vec{u},\vec{v})=0",
                font_size=23,
            ),
            MathTex(
                r"\vec{u}\neq\vec{0} \ \Rightarrow\ \exists\,k \ /\ \vec{v}=k\vec{u} \Rightarrow x'=kx,\ y'=ky",
                font_size=23,
            ),
            MathTex(
                r"\det(\vec{u},\vec{v}) = x(ky) - (kx)y = kxy - kxy = 0",
                font_size=23,
            ),
        ).arrange(DOWN, buff=0.25)
        sens_direct.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Sens direct : supposons u et v colinéaires. Si u est le "
                "vecteur nul, alors x égale y égale zéro, et le déterminant "
                "est automatiquement nul. Sinon, il existe un réel k tel "
                "que v égale k fois u, donc x prime égale k fois x, et y "
                "prime égale k fois y. Le déterminant devient x fois k y, "
                "moins k x fois y, ce qui se simplifie en k x y moins k x "
                "y, soit zéro."
            )
        ) as tracker:
            self.play(Write(sens_direct))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sens_direct))

        reciproque = VGroup(
            Text("Réciproque : det(u,v)=0 ⇒ u, v colinéaires", font_size=22, color=YELLOW),
            MathTex(r"xy'-x'y = 0 \ \Rightarrow\ xy' = x'y", font_size=25),
            Text(
                _wrap(
                    "Si u≠0, une de ses coordonnées est non nulle, par ex. "
                    "x≠0 : on pose k=x'/x, et l'égalité xy'=x'y donne "
                    "y'=ky, donc v=ku : u et v sont colinéaires.",
                    width=48,
                ),
                font_size=21,
            ),
        ).arrange(DOWN, buff=0.28)
        reciproque.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Réciproquement, supposons le déterminant nul, c'est-à-dire "
                "x y prime égale x prime y. Si u est non nul, l'une de ses "
                "coordonnées, disons x, est non nulle : on pose k égale x "
                "prime sur x. L'égalité x y prime égale x prime y donne "
                "alors y prime égale k y, donc le vecteur v est égal à k "
                "fois u : les deux vecteurs sont colinéaires, ce qui achève "
                "la démonstration."
            )
        ) as tracker:
            self.play(Write(reciproque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reciproque))

        # --- Exemple traité ---------------------------------------------------
        exemple = example_box(
            MathTex(
                r"\vec{u}(3;-2),\ \vec{v}(-6;4)"
                r"\\[6pt]"
                r"\det(\vec{u},\vec{v}) = 3\times 4 - (-6)\times(-2) = 12-12 = 0"
                r"\\[4pt]"
                r"\Rightarrow\ \vec{u} \text{ et } \vec{v} \text{ colinéaires } (\vec{v}=-2\vec{u})",
                font_size=25,
            ),
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : soit u de coordonnées 3 et moins 2, et v de "
                "coordonnées moins 6 et 4. Le déterminant vaut 3 fois 4, "
                "moins moins 6 fois moins 2, soit 12 moins 12, donc zéro. "
                "Les vecteurs u et v sont colinéaires ; on vérifie d'ailleurs "
                "que v est égal à moins deux fois u."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(r"\det(\vec{u},\vec{v}) = xy'-x'y", font_size=27),
                MathTex(r"\vec{u},\vec{v} \text{ colinéaires} \iff \det(\vec{u},\vec{v}) = 0", font_size=27),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : le déterminant xy prime moins x prime y "
                "s'annule exactement quand les deux vecteurs sont "
                "colinéaires. C'est le test de colinéarité le plus rapide, "
                "utilisable dans tout repère."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas mélanger l'ordre des coordonnées dans la "
                    "formule (x y' − x' y, pas x' y − x y'), et se rappeler "
                    "que det(u,v) = −det(v,u) : l'ordre des deux vecteurs "
                    "compte pour le SIGNE, mais pas pour la nullité.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à l'ordre dans la formule : c'est x y prime "
                "moins x prime y, pas l'inverse. Et souvenez-vous que "
                "déterminant de v, u est l'opposé de déterminant de u, v : "
                "l'ordre des deux vecteurs change le signe du résultat, "
                "mais ne change jamais le fait qu'il soit nul ou non — donc "
                "sans incidence sur le test de colinéarité."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
