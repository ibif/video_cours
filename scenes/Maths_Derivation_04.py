"""
scenes/Maths_Derivation_04.py — Chapitre 9 (1ereC, Maths), scène 04.

Théorème : dérivable en a ⟹ continue en a, avec démonstration complète.
Remarque : la réciproque est fausse (|x| continue mais non dérivable en 0).
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DerivabiliteContinuite(NotionScene):
    def construct(self):
        titre = scene_title("Dérivabilité et continuité")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Nous avons vu des fonctions dérivables, et d'autres qui "
                "ne le sont pas en certains points. Quel lien existe-t-il "
                "entre dérivabilité et continuité ?",
                width=56,
            ),
            font_size=25,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons rencontré des fonctions dérivables en un point, "
                "et d'autres qui ne le sont pas, comme racine de x ou la "
                "valeur absolue en zéro. Une question se pose alors : quel "
                "lien existe-t-il entre la dérivabilité et une notion que "
                "vous connaissez déjà, la continuité ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Théorème avec démonstration ------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Si f est dérivable en a, alors f est continue en a.", font_size=24),
            ),
            box_width=10.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le théorème : si f est dérivable en a, alors f est "
                "nécessairement continue en a. La dérivabilité est donc une "
                "propriété plus exigeante que la continuité. Démontrons ce "
                "résultat."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        demo = theorem_box(
            VGroup(
                Text("Démonstration : pour h ≠ 0, on écrit", font_size=21),
                MathTex(
                    r"f(a+h) = f(a) + h \cdot \dfrac{f(a+h)-f(a)}{h}",
                    font_size=27,
                ),
                Text("Or f dérivable en a, donc quand h → 0 :", font_size=21),
                MathTex(
                    r"\dfrac{f(a+h)-f(a)}{h} \longrightarrow f'(a)"
                    r"\quad\text{et}\quad h \longrightarrow 0",
                    font_size=25,
                ),
                MathTex(
                    r"\text{donc } f(a+h) \longrightarrow f(a) + 0 \times f'(a) = f(a)",
                    font_size=25,
                ),
                Text("C'est exactement la définition de la continuité en a.", font_size=21),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour h non nul, on peut toujours écrire f de a plus h "
                "comme f de a, plus h fois le taux d'accroissement de f en "
                "a. Or, f étant dérivable en a, ce taux d'accroissement "
                "tend vers f prime de a quand h tend vers zéro, et h "
                "lui-même tend vers zéro. Donc le produit h fois le taux "
                "d'accroissement tend vers zéro, et f de a plus h tend vers "
                "f de a. C'est exactement la définition de la continuité de "
                "f en a. La démonstration est terminée."
            )
        ) as tracker:
            self.play(FadeIn(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Réciproque fausse ------------------------------------------------
        reciproque = warning_box(
            VGroup(
                Text("Attention : la réciproque est FAUSSE.", font_size=23),
                Text(
                    "f(x) = |x| est continue en 0 (pas de saut),\n"
                    "mais n'est pas dérivable en 0 (point anguleux).",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        reciproque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention cependant : la réciproque de ce théorème est "
                "fausse. Une fonction continue n'est pas forcément "
                "dérivable. L'exemple type est la valeur absolue en zéro : "
                "elle est parfaitement continue en zéro, il n'y a aucun "
                "saut sur la courbe, mais nous avons vu dans la scène "
                "précédente qu'elle n'est pas dérivable en zéro, à cause du "
                "point anguleux."
            )
        ) as tracker:
            self.play(FadeIn(reciproque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reciproque))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Dérivable en a ⟹ continue en a. La réciproque est "
                    "fausse : continue n'implique pas dérivable (contre-"
                    "exemple : |x| en 0). Pour étudier la dérivabilité, "
                    "il faut donc un critère plus fin que la continuité.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : dérivable en a entraîne continue en a, mais "
                "l'implication ne se retourne pas. La continuité seule ne "
                "suffit jamais à garantir la dérivabilité — il faut "
                "toujours revenir à l'étude directe du taux "
                "d'accroissement pour conclure."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
