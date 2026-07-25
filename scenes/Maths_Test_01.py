"""
scenes/Maths_Test_01.py — Scène de test minimale pour valider toute la
chaîne technique (Manim, LaTeX/MathTex, voix off EdgeTTS, boîtes de
contenu, assemblage ffmpeg) avant d'écrire les vrais chapitres.

Ne correspond à aucune notion du programme : ce n'est pas un chapitre,
juste un test de bout en bout du pipeline (voir CLAUDE.md, "Pipeline
autonome").
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


class TestChaineTechnique(NotionScene):
    def construct(self):
        # --- Énoncé -----------------------------------------------------
        titre = scene_title("Test de la chaîne technique")
        titre.to_edge(UP)

        enonce = definition_box(
            Text(
                "Cette scène ne traite aucune notion du programme : elle sert "
                "uniquement à vérifier que Manim, le LaTeX, la voix off et "
                "l'assemblage vidéo fonctionnent ensemble.",
                font_size=28,
            )
        )
        enonce.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Avant d'écrire les vrais chapitres, on vérifie que toute la "
                "chaîne technique fonctionne : Manim, le LaTeX, la voix off, "
                "et l'assemblage vidéo."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement -----------------------------------
        formule_depart = MathTex("f(x) = x^2")
        formule_derivee = MathTex("f'(x) = 2x")
        formule_derivee.next_to(formule_depart, DOWN, buff=0.5)
        raisonnement = VGroup(formule_depart, formule_derivee)
        raisonnement.next_to(titre, DOWN, buff=1.2)

        with self.voiceover(
            text=(
                "Prenons un exemple simple : la fonction f de x égale x carré. "
                "Sa dérivée est f prime de x égale deux x."
            )
        ) as tracker:
            self.play(Write(formule_depart))
            self.play(Write(formule_derivee))
            self.wait(tracker.get_remaining_duration())

        # --- Exemple traité ------------------------------------------------
        exemple = example_box(MathTex(r"f'(3) = 2 \times 3 = 6"))
        exemple.next_to(raisonnement, DOWN, buff=0.6)

        with self.voiceover(
            text="Par exemple, pour x égale 3, f prime de 3 vaut 2 fois 3, soit 6."
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(raisonnement), FadeOut(exemple))

        # --- À retenir -------------------------------------------------
        retenir = essentiel_box(
            Text("La chaîne Manim + LaTeX + voix off + ffmpeg fonctionne de bout en bout.", font_size=28)
        )
        retenir.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text="À retenir : la chaîne Manim, LaTeX, voix off et ffmpeg fonctionne de bout en bout."
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text("Cette scène n'est pas un chapitre : elle ne sera jamais publiée comme cours.", font_size=28)
        )
        piege.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre cette scène avec un vrai chapitre : "
                "elle ne sert qu'à valider le pipeline technique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
