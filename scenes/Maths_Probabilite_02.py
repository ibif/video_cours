"""
scenes/Maths_Probabilite_02.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 02.

§ Événements : définition d'un événement (sous-ensemble de l'univers Ω),
événement élémentaire (singleton), événement certain (Ω lui-même),
événement impossible (∅). Exemple résolu : dé cubique, A="obtenir un
nombre pair"={2,4,6}, B="obtenir 5"={5} (événement élémentaire).
Source : 1ereC/Maths.pdf, chapitre 12, pages 143-144.
"""

import textwrap

from manim import DOWN, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, RoundedRectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _de_avec_marquage(issues_marquees) -> VGroup:
    """Les 6 faces d'un dé ; les issues dans `issues_marquees` sont en jaune."""
    faces = VGroup()
    for k in range(1, 7):
        couleur = YELLOW if k in issues_marquees else WHITE
        carre = RoundedRectangle(width=0.8, height=0.8, corner_radius=0.08, color=couleur, stroke_width=2)
        chiffre = MathTex(str(k), font_size=28, color=couleur)
        chiffre.move_to(carre.get_center())
        faces.add(VGroup(carre, chiffre))
    faces.arrange(RIGHT, buff=0.25)
    return faces


class Evenements(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Événements")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "« Obtenir un nombre pair », « tirer un roi » : ces "
                "phrases décrivent chacune un sous-ensemble de résultats "
                "possibles parmi tout l'univers Ω. C'est ce qu'on appelle "
                "un événement.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Des phrases comme « obtenir un nombre pair » en lançant "
                "un dé, ou « tirer un roi » dans un jeu de cartes, "
                "décrivent chacune un sous-ensemble de résultats possibles "
                "parmi tout l'univers Ω. C'est précisément ce qu'on appelle "
                "un événement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition événement -----------------------------
        def_evenement = definition_box(
            VGroup(
                Text("Événement", font_size=24, weight="BOLD"),
                MathTex(r"\text{Un événement } A \text{ est un sous-ensemble de } \Omega \ : \ A \subset \Omega.", font_size=25),
                Text(
                    _wrap("« L'événement A est réalisé » signifie : l'issue obtenue appartient à A.", width=46),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_evenement.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un événement A, associé à une expérience aléatoire "
                "d'univers Ω, est un sous-ensemble de Ω : A inclus dans Ω. "
                "Dire que « l'événement A est réalisé » signifie que "
                "l'issue effectivement obtenue appartient à A."
            )
        ) as tracker:
            self.play(FadeIn(def_evenement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_evenement))

        # --- Cas particuliers --------------------------------------------------
        cas_particuliers = definition_box(
            VGroup(
                Text("Cas particuliers d'événements", font_size=23, weight="BOLD"),
                MathTex(r"\{a\} \ : \ \text{événement ÉLÉMENTAIRE (une seule issue)}", font_size=23),
                MathTex(r"\Omega \ : \ \text{événement CERTAIN (toujours réalisé)}", font_size=23),
                MathTex(r"\emptyset \ : \ \text{événement IMPOSSIBLE (jamais réalisé)}", font_size=23),
            ).arrange(DOWN, buff=0.22),
        )
        cas_particuliers.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Trois cas particuliers méritent un nom. Un singleton, "
                "c'est-à-dire un événement réduit à une seule issue, "
                "s'appelle un événement élémentaire. L'univers Ω tout "
                "entier, toujours réalisé quelle que soit l'issue "
                "obtenue, s'appelle l'événement certain. Et l'ensemble "
                "vide, jamais réalisé, s'appelle l'événement impossible."
            )
        ) as tracker:
            self.play(Write(cas_particuliers))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_particuliers))

        # --- Exemple traité : dé cubique --------------------------------------
        enonce = Text(
            _wrap("On reprend le dé cubique : Ω={1;2;3;4;5;6}. Considérons deux événements A et B.", width=54),
            font_size=23,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons le dé cubique de la scène précédente, "
                "d'univers Ω égale 1, 2, 3, 4, 5, 6. Considérons deux "
                "événements A et B."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        de_A = _de_avec_marquage({2, 4, 6})
        de_A.next_to(titre, DOWN, buff=0.55)
        texte_A = MathTex(r"A = \text{« obtenir un nombre pair » } = \{2\,;\,4\,;\,6\}", font_size=26)
        texte_A.next_to(de_A, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Soit A l'événement « obtenir un nombre pair ». Les "
                "issues qui réalisent A sont 2, 4 et 6 : A égale l'ensemble "
                "2, 4, 6."
            )
        ) as tracker:
            self.play(Write(de_A))
            self.play(Write(texte_A))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(de_A), FadeOut(texte_A))

        de_B = _de_avec_marquage({5})
        de_B.next_to(titre, DOWN, buff=0.55)
        texte_B = MathTex(r"B = \text{« obtenir 5 » } = \{5\}\ \ (\text{événement ÉLÉMENTAIRE})", font_size=26)
        texte_B.next_to(de_B, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Soit B l'événement « obtenir 5 ». Une seule issue le "
                "réalise : B égale le singleton 5. B est donc un événement "
                "élémentaire."
            )
        ) as tracker:
            self.play(Write(de_B))
            self.play(Write(texte_B))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(de_B), FadeOut(texte_B))

        # --- À retenir : exemple récapitulatif --------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"\text{Un événement} = \text{un ENSEMBLE d'issues, jamais un nombre.}", font_size=22),
                MathTex(r"\mathrm{Card}(A) \le \mathrm{Card}(\Omega) \quad \text{toujours}", font_size=22),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : un événement est toujours un "
                "ensemble d'issues, jamais un simple nombre. Et son "
                "cardinal est toujours inférieur ou égal à celui de "
                "l'univers tout entier."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Événement élémentaire ≠ issue seule", font_size=20, weight="BOLD"),
                Text(
                    _wrap(
                        "Ne pas confondre l'issue 5 (un élément de Ω) et "
                        "l'événement élémentaire {5} (un sous-ensemble de "
                        "Ω) : l'écriture ensembliste avec les accolades "
                        "est indispensable.",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un piège fréquent : ne confondez pas l'issue 5, qui est "
                "un simple élément de Ω, et l'événement élémentaire "
                "accolade 5 fermante accolade, qui est un sous-ensemble de "
                "Ω contenant cet unique élément. L'écriture avec les "
                "accolades n'est pas une coquetterie : elle marque bien "
                "qu'un événement est toujours un ensemble."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
