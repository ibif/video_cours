"""
scenes/SVT_HerediteMendelienne_14.py — Chapitre 6 (1ereC, SVT), scène 14
(clôture du chapitre).

§ IX. Applications : le conseil génétique (exemples Côte d'Ivoire) et la
sélection agricole ; méthodes et astuces (3 méthodes) ; les 4 pièges à
éviter ; L'ESSENTIEL DU CHAPITRE. Source : 1ereC/SVT.pdf, pages 64-65.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ApplicationsEtEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("6.14 — Applications et essentiel du chapitre")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : le conseil génétique -----------------------------------------
        def_conseil = definition_box(
            Text(
                _wrap(
                    "Le conseil génétique est une démarche médicale qui "
                    "informe un couple (ou une famille) sur le risque de "
                    "transmission d'une maladie héréditaire à leurs "
                    "enfants, à partir de l'étude des arbres "
                    "généalogiques et des tests de dépistage.",
                    width=50,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        def_conseil.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par ses applications pratiques, en "
                "commençant par le conseil génétique. C'est une démarche "
                "médicale qui informe un couple, ou une famille, sur le "
                "risque de transmission d'une maladie héréditaire à leurs "
                "enfants, à partir de l'étude des arbres généalogiques et "
                "des tests de dépistage."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_conseil))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_conseil))

        # --- Animation du raisonnement : exemples concrets en Côte d'Ivoire -------
        entete_ci = Text("Applications concrètes en Côte d'Ivoire", font_size=21, color=YELLOW, weight="BOLD")
        entete_ci.next_to(titre, DOWN, buff=0.5)

        exemples_ci = _bullets(
            [
                "Dépistage de la drépanocytose avant le mariage ou avant "
                "une naissance : si les deux futurs parents sont AS, "
                "l'enfant a 1/4 de risque d'être SS et 1/2 de chance "
                "d'être AS.",
                "Information des familles touchées par des maladies "
                "liées au sexe (hémophilie) : une femme conductrice sait "
                "que ses fils ont une chance sur deux d'être atteints.",
            ],
            font_size=21,
            width=54,
        )
        exemples_ci.next_to(entete_ci, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En Côte d'Ivoire, le conseil génétique a des "
                "applications très concrètes. Le dépistage de la "
                "drépanocytose avant le mariage, ou avant une naissance : "
                "si les deux futurs parents sont porteurs sains, A S, ils "
                "sont informés qu'à chaque grossesse, l'enfant a une "
                "probabilité d'un quart d'être S S, atteint, et d'un "
                "demi d'être A S, porteur sain. Le conseil génétique "
                "informe aussi les familles touchées par des maladies "
                "liées au sexe, comme l'hémophilie : une femme "
                "conductrice sait que ses fils ont une chance sur deux "
                "d'être atteints."
            )
        ) as tracker:
            self.play(FadeIn(entete_ci))
            self.play(FadeIn(exemples_ci))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ci), FadeOut(exemples_ci))

        # --- Exemple traité : la sélection agricole ---------------------------------
        entete_agri = Text("La sélection agricole", font_size=23, color=YELLOW, weight="BOLD")
        entete_agri.next_to(titre, DOWN, buff=0.5)

        agri = _bullets(
            [
                "Le sélectionneur croise des variétés aux caractères "
                "intéressants (rendement, résistance, précocité), puis "
                "choisit dans la descendance les individus voulus.",
                "Le test-cross vérifie qu'un individu de phénotype "
                "dominant est bien de race pure (homozygote) avant de "
                "l'utiliser comme reproducteur.",
                "Chez les animaux (bovins, volailles), on choisit comme "
                "reproducteurs les individus dont la descendance "
                "confirme la pureté des caractères recherchés.",
            ],
            font_size=20,
            width=54,
        )
        agri.next_to(entete_agri, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les lois de la génétique sont aussi à la base de "
                "l'amélioration des plantes cultivées et des animaux "
                "d'élevage. Le sélectionneur croise des variétés "
                "possédant des caractères intéressants, haut rendement, "
                "résistance aux maladies, précocité, puis sélectionne "
                "dans les descendances les individus présentant les "
                "caractères voulus. Le test-cross permet de vérifier "
                "qu'un individu de phénotype dominant est bien de race "
                "pure, homozygote, avant de l'utiliser comme "
                "reproducteur ou de multiplier ses semences. Chez les "
                "animaux, bovins ou volailles, on choisit comme "
                "reproducteurs les individus dont les descendances "
                "confirment la pureté des caractères recherchés."
            )
        ) as tracker:
            self.play(FadeIn(entete_agri))
            self.play(FadeIn(agri))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_agri), FadeOut(agri))

        methode_agri = method_box(
            Text(
                "La sélection agricole consiste à orienter l'hérédité en\n"
                "choisissant les croisements, là où la nature les laisse\n"
                "au hasard.",
                font_size=22,
            ),
            box_width=10.5,
        )
        methode_agri.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé : la sélection agricole consiste à "
                "orienter l'hérédité en choisissant les croisements, là "
                "où la nature les laisse au hasard."
            )
        ) as tracker:
            self.play(FadeIn(methode_agri))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_agri))

        # --- Méthodes et astuces ------------------------------------------------------
        methodes_astuces = method_box(
            Text(
                _wrap(
                    "1. Réussir un échiquier : écrire phénotypes puis "
                    "génotypes des parents ; écrire les gamètes (un "
                    "allèle chacun, X/Y pour un gène lié au sexe) ; "
                    "construire l'échiquier et compter les cases ; "
                    "conclure par une phrase.\n"
                    "2. Trouver l'allèle dominant : une F1 uniforme "
                    "révèle le phénotype dominant ; deux parents de même "
                    "phénotype donnant un descendant différent → parents "
                    "hétérozygotes, phénotype des parents dominant.\n"
                    "3. Reconnaître un test-cross : croisement d'un "
                    "phénotype dominant avec un phénotype récessif ; "
                    "descendance mixte → parent hétérozygote ; "
                    "descendance homogène → parent homozygote.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=12.3,
        )
        methodes_astuces.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résumons trois méthodes et astuces essentielles pour ce "
                "chapitre. Première méthode, réussir un échiquier à coup "
                "sûr : écrire les phénotypes puis les génotypes des "
                "parents, écrire leurs gamètes, un seul allèle chacun, en "
                "n'oubliant pas que les gamètes d'un homme sont X ou Y "
                "pour un gène lié au sexe, construire l'échiquier, "
                "compter les cases, et toujours conclure par une phrase "
                "qui répond à la question posée. Deuxième méthode, "
                "trouver l'allèle dominant dans un énoncé : une F un "
                "uniforme révèle le phénotype dominant ; si deux parents "
                "de même phénotype donnent un descendant de phénotype "
                "différent, les parents étaient hétérozygotes et leur "
                "phénotype est le dominant. Troisième méthode, reconnaître "
                "un test-cross : repérez le croisement d'un phénotype "
                "dominant avec un phénotype récessif ; si la descendance "
                "est mixte, le parent testé était hétérozygote ; si elle "
                "est homogène, il était homozygote."
            )
        ) as tracker:
            self.play(FadeIn(methodes_astuces))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methodes_astuces))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            _bullets(
                [
                    "Confondre génotype et phénotype : le phénotype est "
                    "ce qu'on observe (entre crochets), le génotype "
                    "s'écrit en lettres.",
                    "Oublier que les proportions (3/4-1/4, 1/2-1/2) sont "
                    "des probabilités, valables seulement sur de grands "
                    "effectifs.",
                    "Croire qu'un père transmet le daltonisme à son "
                    "fils : il lui donne toujours Y, jamais X.",
                    "Mal gérer les 3 allèles ABO : un individu n'en "
                    "porte toujours que 2 ; seul [O] impose OO, seul "
                    "[AB] impose AB.",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.3,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avant de conclure, quatre pièges à éviter absolument. "
                "Premier piège : confondre génotype et phénotype ; le "
                "phénotype est ce qu'on observe, noté entre crochets, le "
                "génotype s'écrit en lettres, il ne se voit pas. "
                "Deuxième piège : oublier que les proportions trois "
                "quarts, un quart, ou un demi, un demi, sont des "
                "probabilités, valables seulement sur de grands "
                "effectifs. Troisième piège : croire qu'un père transmet "
                "le daltonisme à son fils ; un père donne toujours Y à "
                "ses fils, jamais X, donc jamais directement le "
                "caractère. Quatrième piège : mal gérer les trois "
                "allèles du système A B O ; un individu n'en porte "
                "toujours que deux à la fois ; seul le groupe O impose le "
                "génotype O O, et seul le groupe A B impose le génotype A "
                "B."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE ------------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Gène = segment de chromosome ; allèles = versions du "
                    "gène ; locus = son emplacement. Majuscule = "
                    "dominant, minuscule = récessif.",
                    "Génotype (LL, Ll, ll) se déduit ; phénotype ([L], "
                    "[l]) se voit. Homozygote = race pure ; hétérozygote "
                    "= hybride.",
                    "1ère loi de Mendel : F1 uniforme, phénotype "
                    "dominant. 2e loi : F2 en 3/4-1/4 (disjonction des "
                    "allèles).",
                    "L'échiquier de croisement prévoit toutes les "
                    "combinaisons ; le test-cross (x ll) révèle un "
                    "génotype caché (1/2-1/2 → hétérozygote).",
                    "Codominance (ABO, 3 allèles) : les 2 allèles "
                    "s'expriment ensemble chez l'hétérozygote.",
                    "Transmission autosomique : mêmes fréquences filles/"
                    "garçons (drépanocytose). Liée à X récessive : "
                    "garçons surtout touchés (daltonisme, hémophilie).",
                    "L'arbre généalogique retrouve le mode de "
                    "transmission par 3 questions : récessif/dominant ? "
                    "autosomique/lié à X ? vérification des génotypes.",
                    "Applications : conseil génétique (risque pour un "
                    "couple) et sélection agricole (orienter l'hérédité).",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        # Garde-fou : si le contenu dépasse la hauteur visible du cadre,
        # on réduit l'échelle globale de la boîte pour qu'elle tienne.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel de ce chapitre. Le gène est un "
                "segment de chromosome ; les allèles en sont les "
                "différentes versions ; le locus, leur emplacement. "
                "Majuscule pour l'allèle dominant, minuscule pour le "
                "récessif. Le génotype se déduit, le phénotype se voit. "
                "L'homozygote est de race pure, l'hétérozygote est un "
                "hybride. La première loi de Mendel donne une F un "
                "uniforme, de phénotype dominant ; la seconde donne, en F "
                "deux, trois quarts contre un quart, par disjonction des "
                "allèles à la méiose. L'échiquier de croisement prévoit "
                "toutes les combinaisons possibles ; le test-cross, "
                "croisement avec un récessif homozygote, révèle un "
                "génotype caché. La codominance, comme pour les groupes "
                "sanguins A B O, fait s'exprimer les deux allèles "
                "ensemble chez l'hétérozygote. La transmission "
                "autosomique touche également filles et garçons, comme "
                "la drépanocytose ; la transmission récessive liée au "
                "chromosome X touche surtout les garçons, comme le "
                "daltonisme ou l'hémophilie. L'arbre généalogique permet "
                "de retrouver le mode de transmission en trois "
                "questions. Enfin, ces lois trouvent deux applications "
                "majeures : le conseil génétique, qui évalue le risque "
                "pour un couple, et la sélection agricole, qui oriente "
                "l'hérédité au service de l'agriculture."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
