"""
scenes/SVT_EchangesCationiquesSol_13.py — Chapitre 9 (1ereC, SVT), scène 13.

Méthodes et astuces de clôture du chapitre : calculer CEC/S/V à partir
d'une analyse de sol, raisonner sur un échange cationique, rédiger un
raisonnement de type situation-problème (APC), les 3 pièges classiques, et
L'ESSENTIEL DU CHAPITRE. Source : 1ereC/SVT.pdf, page 105.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class MethodesEtEssentielSol(NotionScene):
    def construct(self):
        titre = scene_title("9.12 — Méthodes, pièges et essentiel")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : trois méthodes-clés pour réussir --------------------
        intro = Text(
            _wrap(
                "Pour réussir un exercice sur ce chapitre, trois "
                "méthodes reviennent sans cesse : calculer CEC/S/V, "
                "raisonner sur un échange cationique, et rédiger une "
                "réponse structurée face à une situation-problème.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour réussir un exercice sur ce chapitre, trois "
                "méthodes reviennent sans cesse : calculer la CEC, la "
                "somme des bases et le taux de saturation ; raisonner sur "
                "un échange cationique ; et rédiger une réponse "
                "structurée face à une situation-problème. Passons-les "
                "en revue."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : les 3 méthodes ------------------------------------
        methode1 = method_box(
            _bullets(
                [
                    "1. Vérifier que toutes les valeurs sont dans la "
                    "même unité (cmol+/kg).",
                    "2. CEC = somme de tous les cations échangeables, y "
                    "compris H+ (et Al3+ si donné).",
                    "3. S = somme des bases uniquement : Ca2++Mg2++K++Na+ "
                    "(jamais H+ ni Al3+).",
                    "4. V = (S/CEC)×100.",
                    "5. Conclure : CEC élevée + V élevé ⇒ sol fertile ; "
                    "V faible ⇒ sol acide et désaturé.",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.0,
        )
        methode1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode un : calculer CEC, S et V à partir d'une "
                "analyse de sol. Un : vérifier que toutes les valeurs "
                "sont exprimées dans la même unité, cmol plus par "
                "kilogramme. Deux : la CEC est la somme de tous les "
                "cations échangeables, y compris H+, et l'aluminium s'il "
                "est donné. Trois : S est la somme des bases uniquement, "
                "calcium, magnésium, potassium, sodium, jamais H+ ni "
                "aluminium. Quatre : V égale S divisé par CEC, fois cent. "
                "Cinq : conclure. Une CEC élevée et un V élevé signalent "
                "un sol fertile ; un V faible signale un sol acide et "
                "désaturé."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            _bullets(
                [
                    "1. Identifier le cation qui arrive en abondance "
                    "(H+ des pluies, Ca2+ du chaulage, NH4+ d'un "
                    "engrais...).",
                    "2. Ce cation s'adsorbe et chasse les cations "
                    "déjà fixés, à charge égale : 1 cation bivalent = "
                    "2 cations monovalents échangés.",
                    "3. Déduire l'effet : sur le complexe (saturation/"
                    "désaturation) et sur la solution (ce qu'elle "
                    "gagne, ce que la plante absorbe ou ce qui sera "
                    "lessivé).",
                ],
                font_size=18,
                width=56,
            ),
            box_width=12.2,
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode deux : raisonner sur un échange cationique. Un "
                ": identifier le cation qui arrive en abondance dans la "
                "solution, H+ des pluies, Ca2+ du chaulage, NH4+ d'un "
                "engrais. Deux : ce cation s'adsorbe sur le complexe et "
                "chasse les cations déjà fixés, à charge égale, un "
                "cation bivalent en échange deux cations monovalents. "
                "Trois : en déduire l'effet, sur le complexe, "
                "saturation ou désaturation, et sur la solution, ce "
                "qu'elle gagne, ce que la plante peut absorber, ou ce "
                "qui sera lessivé."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            _bullets(
                [
                    "1. Identifier le problème (fatigue du sol, "
                    "acidité).",
                    "2. L'expliquer avec les notions du cours "
                    "(lessivage, désaturation, blocage du P).",
                    "3. S'appuyer sur les données fournies (pH, CEC, V).",
                    "4. Proposer des solutions argumentées (chaulage, "
                    "engrais, jachère, matière organique).",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.0,
        )
        methode3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode trois : rédiger un raisonnement de type "
                "situation-problème, comme demandé par l'approche par "
                "compétences. Devant un énoncé ivoirien, baisse de "
                "rendement d'un cacaoyer, jaunissement d'une culture, "
                "structurer la réponse en quatre temps. Un : identifier "
                "le problème, fatigue du sol, acidité. Deux : "
                "l'expliquer avec les notions du cours, lessivage, "
                "désaturation, blocage du phosphore. Trois : s'appuyer "
                "sur les données fournies, pH, CEC, V. Quatre : proposer "
                "des solutions argumentées, chaulage, engrais, jachère, "
                "matière organique."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Pièges à éviter : les 3 pièges classiques -----------------------
        pieges_titre = Text("Les 3 pièges classiques", font_size=25, color=YELLOW, weight="BOLD")
        pieges_titre.next_to(titre, DOWN, buff=0.45)

        pieges = warning_box(
            _bullets(
                [
                    "Ne pas confondre adsorption (fixation sur le "
                    "complexe, dans le sol) et absorption (entrée dans "
                    "la racine, côté plante).",
                    "H+ n'est pas une base échangeable : l'inclure dans "
                    "S fausse le calcul du taux de saturation.",
                    "Le pH est une échelle logarithmique : passer de "
                    "pH 5 à pH 6, c'est diviser par 10 la concentration "
                    "en H+, pas la diminuer d'une unité quelconque.",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.0,
        )
        pieges.next_to(pieges_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Avant de conclure, révisons les trois pièges classiques "
                "de ce chapitre. Premier piège : ne pas confondre "
                "adsorption, la fixation sur le complexe dans le sol, et "
                "absorption, l'entrée dans la racine, côté plante. "
                "Deuxième piège : H+ n'est pas une base échangeable, "
                "l'inclure dans S fausse le calcul du taux de "
                "saturation. Troisième piège : le pH est une échelle "
                "logarithmique, passer de pH cinq à pH six, c'est "
                "diviser par dix la concentration en ions H+, pas la "
                "diminuer d'une unité quelconque."
            )
        ) as tracker:
            self.play(FadeIn(pieges_titre))
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges_titre), FadeOut(pieges))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) --------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Le complexe argilo-humique (argile + humus), chargé "
                    "négativement, retient les cations : adsorption / "
                    "désorption = échange cationique à charge égale.",
                    "La racine libère des H+ qui chassent les cations "
                    "nutritifs (Ca2+, Mg2+, K+) vers la solution du sol.",
                    "CEC = Ca2++Mg2++K++Na++H+ (réservoir total). "
                    "S = bases échangeables seules. V=(S/CEC)×100 = "
                    "taux de saturation.",
                    "Le pH (0-14) contrôle la disponibilité des "
                    "éléments : zone optimale pH 6-7 ; toxicité "
                    "Al3+/Mn en sol trop acide.",
                    "Le lessivage désature et acidifie le sol ; les "
                    "anions (NO3-) sont les premiers perdus.",
                    "Engrais, amendements et chaulage (CaCO3) "
                    "restituent les éléments et corrigent l'acidité.",
                    "En Côte d'Ivoire : fatigue des sols (lessivage, "
                    "exportations, déforestation) ; jachère de plus en "
                    "plus courte, à compenser par engrais et chaulage.",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)
        _fit(essentiel, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. Le complexe "
                "argilo-humique, association de l'argile et de l'humus, "
                "chargé négativement, retient les cations : l'adsorption "
                "et la désorption forment un échange cationique, "
                "toujours à charge égale. La racine libère des ions H+ "
                "qui chassent les cations nutritifs, calcium, magnésium, "
                "potassium, vers la solution du sol. La CEC additionne "
                "tous les cations échangeables, c'est le réservoir "
                "total ; S ne compte que les bases échangeables ; le "
                "taux de saturation V égale S divisé par CEC, fois cent. "
                "Le pH, de zéro à quatorze, contrôle la disponibilité "
                "des éléments, avec une zone optimale entre pH six et "
                "sept, et une toxicité de l'aluminium et du manganèse en "
                "sol trop acide. Le lessivage désature et acidifie le "
                "sol, les anions comme le nitrate étant les premiers "
                "perdus. Les engrais, les amendements et le chaulage au "
                "carbonate de calcium restituent les éléments perdus et "
                "corrigent l'acidité. Enfin, en Côte d'Ivoire, la "
                "fatigue des sols résulte du lessivage, des exportations "
                "et de la déforestation ; la jachère, de plus en plus "
                "courte, doit être compensée par les engrais et le "
                "chaulage."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
