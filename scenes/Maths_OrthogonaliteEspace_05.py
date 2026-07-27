"""
scenes/Maths_OrthogonaliteEspace_05.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 05.

§ Propriétés d'existence et d'unicité (admises) + orthogonalité et
parallélisme : 3 propriétés (avec démonstrations) reliant droites/plans
parallèles et orthogonalité, puis un récapitulatif « à retenir » pour
démontrer un parallélisme via l'orthogonalité (avec le piège de la scène 1
en contraste).
Source : 1ereC/Maths.pdf, chapitre 10, pages 118-129.
"""

from manim import (
    DOWN,
    UP,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


class ProprietesExistenceParallelisme(NotionScene):
    def construct(self):
        titre = scene_title("Existence, unicité et parallélisme")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : propriétés d'existence et d'unicité (admises) ------------
        prop_exist1 = property_box(
            VGroup(
                Text("Existence et unicité (1) — admise", font_size=22, weight="BOLD"),
                MathTex(
                    r"\forall A, \ \forall d, \ \exists !\ \text{plan } P \ni A \ \text{tel que } P \perp d",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        prop_exist1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux propriétés d'existence et d'unicité, admises sans "
                "démonstration à ce niveau. Première propriété : par un "
                "point A donné, il passe un unique plan P orthogonal à une "
                "droite d donnée."
            )
        ) as tracker:
            self.play(FadeIn(prop_exist1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_exist1))

        prop_exist2 = property_box(
            VGroup(
                Text("Existence et unicité (2) — admise", font_size=22, weight="BOLD"),
                MathTex(
                    r"\forall A, \ \forall P, \ \exists !\ \text{droite } d \ni A \ \text{tel que } d \perp P",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        prop_exist2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième propriété, symétrique de la première : par un "
                "point A donné, il passe une unique droite d orthogonale à "
                "un plan P donné. Ces deux résultats fondent tout ce qui "
                "suit."
            )
        ) as tracker:
            self.play(FadeIn(prop_exist2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_exist2))

        # --- Raisonnement : les 3 propriétés parallélisme / orthogonalité ------
        propA = property_box(
            VGroup(
                MathTex(r"d \parallel d' \ \text{et} \ P \perp d \ \Longrightarrow\ P \perp d'", font_size=25),
                Text("(d'après une propriété de la scène 1 : d ⟂ Δ et d ∥ d' ⟹ d' ⟂ Δ, pour toute droite Δ de P)", font_size=18),
            ).arrange(DOWN, buff=0.18),
        )
        propA.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici trois propriétés qui relient orthogonalité et "
                "parallélisme, très utiles pour la suite. Propriété une : "
                "si deux droites d et d prime sont parallèles, et que P "
                "est orthogonal à d, alors P est aussi orthogonal à d "
                "prime. La preuve est immédiate : P orthogonal à d "
                "signifie que d est orthogonale à toute droite de P ; "
                "comme d prime est parallèle à d, elle hérite de cette "
                "orthogonalité pour chacune de ces droites, donc P est "
                "aussi orthogonal à d prime."
            )
        ) as tracker:
            self.play(FadeIn(propA))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propA))

        propB = property_box(
            VGroup(
                MathTex(r"P \parallel P' \ \text{et} \ d \perp P \ \Longrightarrow\ d \perp P'", font_size=25),
                Text("(toute droite de P′ est parallèle à une droite de P)", font_size=18),
            ).arrange(DOWN, buff=0.18),
        )
        propB.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Propriété deux, la version « plans » de la précédente : si "
                "deux plans P et P prime sont parallèles, et que d est "
                "orthogonale à P, alors d est aussi orthogonale à P prime. "
                "En effet, toute droite de P prime est parallèle à une "
                "droite de P, et d est orthogonale à cette dernière : d "
                "est donc orthogonale à toute droite de P prime."
            )
        ) as tracker:
            self.play(FadeIn(propB))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propB))

        propC = property_box(
            VGroup(
                MathTex(r"d \perp P \ \text{et} \ d' \perp P \ \Longrightarrow\ d \parallel d'", font_size=26, color=YELLOW),
                Text("(unicité de la direction orthogonale à un plan donné)", font_size=18),
            ).arrange(DOWN, buff=0.18),
        )
        propC.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Propriété trois, la plus utile pour démontrer un "
                "parallélisme : si deux droites d et d prime sont toutes "
                "deux orthogonales à un même plan P, alors elles sont "
                "parallèles entre elles. C'est une conséquence directe de "
                "l'unicité vue plus haut : il n'existe qu'une seule "
                "direction orthogonale à un plan donné."
            )
        ) as tracker:
            self.play(FadeIn(propC))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propC))

        # --- Exemple traité : et pour deux plans orthogonaux à une droite ------
        propD = property_box(
            MathTex(r"P \perp d \ \text{et} \ P' \perp d \ \Longrightarrow\ P \parallel P'", font_size=26),
        )
        propD.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Et symétriquement : si deux plans P et P prime sont tous "
                "deux orthogonaux à une même droite d, alors ils sont "
                "parallèles entre eux, toujours par unicité du plan "
                "orthogonal à une droite passant par un point donné."
            )
        ) as tracker:
            self.play(FadeIn(propD))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propD))

        # --- À retenir -----------------------------------------------------------
        retenir = warning_box(
            VGroup(
                Text("À retenir : pour démontrer un PARALLÉLISME, on peut passer par l'orthogonalité.", font_size=22, weight="BOLD"),
                MathTex(r"\bullet \ \ d \perp P \ \text{et} \ d' \perp P \ \Longrightarrow\ d \parallel d'", font_size=23),
                MathTex(r"\bullet \ \ P \perp d \ \text{et} \ P' \perp d \ \Longrightarrow\ P \parallel P'", font_size=23),
                Text(
                    "⚠️ Cela marche avec un PLAN (ou une droite) commun de référence — mais PAS avec\n"
                    "une simple droite commune côté « deux droites » : voir le piège de la scène 1\n"
                    "(d ⟂ Δ et d′ ⟂ Δ n'implique PAS d ∥ d′, sauf si Δ est un plan, pas une droite).",
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résumons : pour démontrer que deux droites, ou que deux "
                "plans, sont parallèles, il suffit souvent de montrer "
                "qu'ils sont tous deux orthogonaux à un même plan, ou à "
                "une même droite. Mais attention à ne pas confondre avec "
                "le piège vu à la scène précédente : deux droites toutes "
                "deux orthogonales à une même TROISIÈME DROITE ne sont "
                "pas nécessairement parallèles. C'est uniquement quand la "
                "référence commune est un PLAN — ou, symétriquement, une "
                "droite pour deux plans — que la conclusion de "
                "parallélisme est valide."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
