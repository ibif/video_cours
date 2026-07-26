"""
scenes/SVT_Monohybridisme_04.py — Chapitre 4 (1ereD, SVT), scène 04.

§ 4.3 L'expérience de Mendel : le croisement monohybride. Démarche
expérimentale du pois, résultats F1/F2, les deux lois de Mendel
(theorem_box — première boîte THÉORÈME du programme), exemple de
vérification des comptages (705/224), attention aux deux pièges F1/F2,
interprétation en termes d'allèles. Source : 1ereD/SVT.pdf, pages 51-53.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ExperienceDeMendel(NotionScene):
    def construct(self):
        titre = scene_title("4.3 — L'expérience de Mendel")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : la démarche expérimentale de Mendel -----------------------
        intro = Text(
            _wrap(
                "Grégoire Mendel (1822-1884), moine et professeur à Brünn, "
                "est le fondateur de la génétique. Entre 1856 et 1863, il "
                "réalise des milliers de croisements sur le pois.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Grégoire Mendel, moine et professeur à Brünn, dans "
                "l'actuelle République tchèque, est le fondateur de la "
                "génétique. Entre mille huit cent cinquante-six et mille "
                "huit cent soixante-trois, il réalise des milliers de "
                "croisements sur le pois."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        raisons = _bullets(
            [
                "Caractères nets, faciles à distinguer (fleurs violettes/"
                "blanches, graines lisses/ridées).",
                "Lignées pures disponibles (autofécondation répétée).",
                "Fécondation contrôlable : castration puis pollinisation "
                "manuelle au pinceau.",
                "Nombreux descendants -> comptages statistiques fiables.",
            ],
            font_size=22,
            width=54,
        )
        raisons.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mendel choisit le pois avec soin, pour quatre raisons. "
                "D'abord, le pois possède des caractères nets, faciles à "
                "distinguer : fleurs violettes ou blanches, graines lisses "
                "ou ridées, jaunes ou vertes. Ensuite, il existe des lignées "
                "pures de pois, obtenues par autofécondation répétée. De "
                "plus, la fécondation est contrôlable : Mendel enlève les "
                "étamines d'une fleur, c'est la castration, puis dépose "
                "dessus, avec un pinceau, le pollen de l'autre parent. "
                "Enfin, chaque croisement donne de nombreux descendants, ce "
                "qui autorise des comptages statistiques fiables. La force "
                "de Mendel, c'est d'avoir compté les descendants de chaque "
                "type au lieu de se contenter de descriptions."
            )
        ) as tracker:
            self.play(FadeIn(raisons))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(raisons))

        # --- Animation du raisonnement : résultats F1/F2 et les 2 lois --------
        resultat_f1 = Text(
            _wrap(
                "Mendel croise deux lignées pures de pois : fleurs "
                "violettes x fleurs blanches. En F1 : 100% des plants ont "
                "des fleurs violettes. La F1 est uniforme.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        resultat_f1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mendel croise deux lignées pures de pois différant par un "
                "seul caractère : des plants à fleurs violettes et des "
                "plants à fleurs blanches. En F1, il obtient cent pour cent "
                "de plants à fleurs violettes. La F1 est uniforme."
            )
        ) as tracker:
            self.play(FadeIn(resultat_f1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resultat_f1))

        loi1 = theorem_box(
            Text(
                _wrap(
                    "PREMIÈRE LOI DE MENDEL — UNIFORMITÉ DES HYBRIDES DE "
                    "F1 : le croisement de deux lignées pures différant "
                    "par un seul caractère donne une F1 uniforme, tous "
                    "les individus étant semblables entre eux et de "
                    "phénotype dominant.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        loi1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Ce résultat constitue la première loi de Mendel, la loi de "
                "l'uniformité des hybrides de F1 : le croisement de deux "
                "lignées pures différant par un seul caractère donne une "
                "génération F1 uniforme, tous les individus de la F1 étant "
                "semblables entre eux et présentant le phénotype de "
                "l'allèle dominant."
            )
        ) as tracker:
            self.play(FadeIn(loi1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi1))

        resultat_f2 = Text(
            _wrap(
                "En F2, obtenue en laissant les plants de la F1 se "
                "féconder eux-mêmes, Mendel compte 705 plants à fleurs "
                "violettes et 224 à fleurs blanches — des proportions "
                "très proches de 3/4 et 1/4.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        resultat_f2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En F2, obtenue en laissant les plants de la F1 se féconder "
                "eux-mêmes, Mendel compte sept cent cinq plants à fleurs "
                "violettes et deux cent vingt-quatre plants à fleurs "
                "blanches, soit des proportions très proches de trois "
                "quarts et un quart."
            )
        ) as tracker:
            self.play(FadeIn(resultat_f2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resultat_f2))

        loi2 = theorem_box(
            Text(
                _wrap(
                    "DEUXIÈME LOI DE MENDEL — SÉGRÉGATION DES ALLÈLES : "
                    "dans la F2 issue de F1 x F1, les allèles se séparent "
                    "à la formation des gamètes : on obtient 3/4 de "
                    "phénotype dominant et 1/4 de phénotype récessif "
                    "(pureté des gamètes).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        loi2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "C'est la deuxième loi de Mendel, la loi de ségrégation, ou "
                "disjonction, des allèles : dans la F2 issue du croisement "
                "des hybrides de F1 entre eux, les allèles se sont séparés "
                "au moment de la formation des gamètes ; on obtient trois "
                "quarts d'individus de phénotype dominant et un quart "
                "d'individus de phénotype récessif. Chaque gamète ne "
                "transporte qu'un seul allèle de chaque gène : c'est ce "
                "qu'on appelle la pureté des gamètes."
            )
        ) as tracker:
            self.play(FadeIn(loi2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi2))

        # --- Exemple traité : vérification des comptages de Mendel -------------
        exemple = example_box(
            Text(
                _wrap(
                    "705+224=929 plants en F2. Violettes : 705/929≈75,9% "
                    ". Blanches : 224/929≈24,1%. Théorie : 75% (3/4) et "
                    "25% (1/4). Effectifs attendus : (3/4)x929≈696,75 "
                    "violettes, (1/4)x929≈232,25 blanches. Écarts "
                    "faibles : résultats conformes à la 2e loi.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.3,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Vérifions que les nombres de Mendel correspondent bien aux "
                "proportions trois quarts et un quart. Effectif total : "
                "sept cent cinq plus deux cent vingt-quatre égale neuf cent "
                "vingt-neuf plants en F2. Proportions observées : les "
                "fleurs violettes représentent sept cent cinq sur neuf cent "
                "vingt-neuf, soit environ soixante-quinze virgule neuf pour "
                "cent ; les fleurs blanches représentent deux cent "
                "vingt-quatre sur neuf cent vingt-neuf, soit environ "
                "vingt-quatre virgule un pour cent. La théorie prévoit "
                "soixante-quinze pour cent et vingt-cinq pour cent : les "
                "valeurs observées en sont très proches. Les effectifs "
                "théoriques attendus sont d'environ six cent quatre-vingt- "
                "seize virgule sept cinq violettes et deux cent "
                "trente-deux virgule deux cinq blanches : les écarts avec "
                "les valeurs observées sont faibles. Conclusion : les "
                "résultats expérimentaux sont conformes aux proportions "
                "théoriques trois quarts, un quart, ce qui conforte la "
                "deuxième loi de Mendel."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : l'interprétation en termes d'allèles -------------------
        entete_interpretation = Text("Interprétation en termes d'allèles", font_size=25, color=YELLOW, weight="BOLD")
        entete_interpretation.next_to(titre, DOWN, buff=0.5)

        etapes = _bullets(
            [
                "P : V/V (violettes) x v/v (blanches).",
                "Gamètes des parents : V/V -> 100% V ; v/v -> 100% v.",
                "F1 : chaque zygote reçoit V et v -> V/v, [V] violet.",
                "Gamètes de la F1 : chaque V/v produit 1/2 V et 1/2 v.",
                "F2 : rencontre au hasard -> 1/4 V/V, 1/2 V/v, 1/4 v/v, "
                "soit 3/4 [V] et 1/4 [v].",
            ],
            font_size=21,
            width=54,
        )
        etapes.next_to(entete_interpretation, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Écrivons le mécanisme complet. Les parents P : une lignée "
                "pure à fleurs violettes, V sur V, croisée avec une lignée "
                "pure à fleurs blanches, v sur v. Gamètes des parents : le "
                "parent V sur V ne produit que des gamètes V ; le parent v "
                "sur v ne produit que des gamètes v. La F1 : chaque zygote "
                "reçoit un allèle V et un allèle v, génotype V sur v, "
                "phénotype violet — d'où l'uniformité de la F1. Gamètes de "
                "la F1 : chaque hybride V sur v produit un demi de gamètes "
                "V et un demi de gamètes v. La F2 : la rencontre au hasard "
                "de ces gamètes donne un quart V sur V, un demi V sur v, un "
                "quart v sur v, soit, en phénotypes, trois quarts violet et "
                "un quart blanc. Nous démontrerons ce calcul avec "
                "l'échiquier de croisement au paragraphe suivant."
            )
        ) as tracker:
            self.play(FadeIn(entete_interpretation))
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_interpretation), FadeOut(etapes))

        # --- Piège à éviter : ce que la F1 cache, la F2 le révèle -------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne jamais écrire « le caractère blanc a disparu dans "
                    "la F1 » : l'allèle v est toujours présent dans le "
                    "génotype V/v, simplement masqué. Et ne jamais dire "
                    "que la F2 contient « les 2 caractères en quantités "
                    "égales » : c'est 3/4-1/4, jamais 1/2-1/2 (signature "
                    "du croisement-test, § 4.5).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.3,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deux pièges reviennent dans les copies. Premier piège : "
                "écrire que le caractère blanc a disparu dans la F1. C'est "
                "faux : la modalité blanche n'est pas exprimée, mais "
                "l'allèle v est bien présent dans le génotype. Deuxième "
                "piège : affirmer que la F2 contient les deux caractères "
                "des parents en quantités égales. C'est faux aussi : la F2 "
                "contient trois quarts de dominants et un quart de "
                "récessifs, jamais un demi et un demi. Cette proportion "
                "moitié-moitié est la signature d'un autre croisement, le "
                "croisement-test, que nous verrons au paragraphe quatre "
                "point cinq."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
