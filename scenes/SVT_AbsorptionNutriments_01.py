"""
scenes/SVT_AbsorptionNutriments_01.py — Chapitre 13 (1ereD, SVT), scène 01.

Introduction du chapitre « L'absorption des nutriments » : activité d'Awa à
Yopougon (repas attiéké / poisson braisé / sauce graine), questions guides,
objectifs du chapitre, prérequis à réviser.
Source : 1ereD/SVT.pdf, page 168.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class IntroductionAbsorptionNutriments(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 13 — L'absorption des nutriments")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------
        sous_titre = Text("Un repas à Yopougon", font_size=28, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "Il est 13 h à Yopougon. Après le service de sa boutique, "
                "Awa mange un plat d'attiéké accompagné de poisson braisé "
                "et de sauce graine préparée à l'huile de palme. Une heure "
                "plus tard, elle se sent de nouveau pleine d'énergie pour "
                "retourner travailler.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Il est treize heures à Yopougon, à Abidjan. Après le "
                "service de sa boutique, Awa mange un plat d'attiéké "
                "accompagné de poisson braisé et de sauce graine préparée "
                "à l'huile de palme. Une heure plus tard, elle se sent de "
                "nouveau pleine d'énergie pour retourner travailler."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        etapes = Text(
            _wrap(
                "Pourtant, entre l'assiette et les cellules de ses "
                "muscles, les aliments ont dû franchir deux grandes "
                "étapes : la digestion, qui transforme les aliments en "
                "nutriments, puis l'absorption, qui fait passer ces "
                "nutriments du tube digestif vers le milieu intérieur.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        etapes.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pourtant, entre l'assiette et les cellules de ses "
                "muscles, les aliments ont dû franchir deux grandes "
                "étapes : la digestion, qui a transformé les aliments en "
                "nutriments — nous l'avons étudiée au chapitre douze — "
                "puis l'absorption, qui fait passer ces nutriments du tube "
                "digestif vers le milieu intérieur de l'organisme."
            )
        ) as tracker:
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(etapes))

        # --- Animation du raisonnement : les questions guides --------------
        entete_questions = Text(
            "Trois questions guideront notre étude :", font_size=27, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. Où exactement les nutriments quittent-ils le tube digestif ?", font_size=21, color=WHITE)
        q2 = Text("2. Comment traversent-ils la paroi de l'intestin ?", font_size=21, color=WHITE)
        q3 = Text("3. Par quels chemins gagnent-ils le foie, le cœur et les muscles ?", font_size=21, color=WHITE)
        questions = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text="Première question : où exactement les nutriments quittent-ils le tube digestif ?"
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Deuxième question : comment traversent-ils la paroi de l'intestin ?"
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Troisième question : par quels chemins gagnent-ils "
                "ensuite le foie, le cœur et les muscles ? Ce chapitre "
                "répond à ces trois questions."
            )
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre --------------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=27, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir l'absorption intestinale et citer son organe principal.",
                "Décrire l'organisation de la paroi de l'intestin grêle et son adaptation à l'absorption.",
                "Décrire la structure d'une villosité intestinale et le rôle de chacun de ses éléments.",
                "Distinguer transport passif (diffusion, osmose) et transport actif, avec des exemples.",
                "Indiquer le devenir des nutriments : voie sanguine (veine porte) et voie lymphatique.",
                "Exploiter des documents expérimentaux sur l'absorption.",
            ],
            font_size=19,
            width=56,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, l'élève doit être capable de "
                "définir l'absorption intestinale et de citer son organe "
                "principal ; de décrire l'organisation de la paroi de "
                "l'intestin grêle — plis circulaires, villosités, "
                "microvillosités — et d'expliquer en quoi elle est adaptée "
                "à l'absorption ; de décrire la structure d'une villosité "
                "intestinale et le rôle de chacun de ses éléments ; de "
                "distinguer le transport passif, diffusion et osmose, du "
                "transport actif, en les illustrant par des exemples de "
                "nutriments ; d'indiquer le devenir immédiat des nutriments "
                "absorbés, par la voie sanguine et par la voie lymphatique "
                "; et enfin d'exploiter des documents expérimentaux sur "
                "l'absorption."
            )
        ) as tracker:
            self.play(FadeIn(entete_objectifs))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_objectifs), FadeOut(objectifs))

        # --- À retenir : prérequis à réviser ----------------------------------
        prerequis = essentiel_box(
            Text(
                _wrap(
                    "Prérequis à réviser : le trajet des aliments dans le "
                    "tube digestif (bouche, œsophage, estomac, intestin "
                    "grêle, côlon) ; les nutriments produits par la "
                    "digestion (glucose, acides aminés, acides gras et "
                    "glycérol, chapitre 12) ; la cellule (membrane, "
                    "cytoplasme) et la respiration cellulaire productrice "
                    "d'ATP ; le sang et la lymphe ; lecture d'un tableau et "
                    "d'une courbe.",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        prerequis.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : "
                "le trajet des aliments dans le tube digestif — bouche, "
                "œsophage, estomac, intestin grêle, côlon ; les nutriments "
                "produits par la digestion, glucose, acides aminés, acides "
                "gras et glycérol, étudiés au chapitre douze ; la cellule, "
                "sa membrane, son cytoplasme, et la respiration cellulaire "
                "qui produit de l'énergie sous forme d'ATP ; les deux "
                "grands liquides de l'organisme, le sang et la lymphe ; et "
                "enfin savoir lire et exploiter un tableau de données et "
                "une courbe."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter : ce chapitre n'est pas un retour à la digestion --
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre suppose la digestion déjà acquise "
                    "(chapitre 12) : il ne s'agit pas de refaire comment "
                    "les nutriments sont produits, mais de comprendre "
                    "comment ils traversent la paroi intestinale, où "
                    "exactement cela se produit, et par quels chemins ils "
                    "gagnent ensuite le sang ou la lymphe puis le reste du "
                    "corps d'Awa.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : ce chapitre suppose la digestion déjà "
                "acquise, vue au chapitre douze. Il ne s'agit plus de "
                "refaire comment les nutriments sont produits, mais de "
                "comprendre comment ils traversent la paroi intestinale, "
                "où exactement cela se produit, et par quels chemins ils "
                "gagnent ensuite le sang ou la lymphe, puis le reste du "
                "corps d'Awa."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
