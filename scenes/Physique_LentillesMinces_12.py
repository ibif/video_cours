"""
scenes/Physique_LentillesMinces_12.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 12 — DERNIÈRE scène du chapitre et du programme de
Physique 1ereC.

§ Synthèse : méthode pour résoudre un exercice de conjugaison en 5 étapes
(schéma, données algébriques, Descartes, conclure nature/sens/taille,
vérifier) ; méthode pour une construction graphique propre ; astuce pour
un système à deux lentilles séparées (traiter successivement, γ_total =
γ1×γ2) ; récapitulatif des pièges classiques de tout le chapitre.
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, synthèse).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
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
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse : méthodes et pièges à éviter")
        titre.scale(0.44)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé -----------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Ce chapitre sur les lentilles minces conclut le programme "
                "de Physique. Faisons la synthèse des méthodes à "
                "appliquer, et récapitulons les pièges les plus fréquents "
                "rencontrés tout au long du chapitre.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Ce chapitre sur les lentilles minces conclut le programme "
                "de Physique de cette année. Faisons la synthèse des "
                "méthodes à appliquer, et récapitulons les pièges les "
                "plus fréquents rencontrés tout au long du chapitre."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Méthode 1 : résoudre un exercice de conjugaison en 5 étapes -------------
        methode1 = method_box(
            VGroup(
                Text("Résoudre un exercice de conjugaison en 5 étapes", font_size=21, weight="BOLD"),
                Text("1. Faire un schéma clair (axe, lentille, O, F, F').", font_size=18),
                Text("2. Lister les données en mesures ALGÉBRIQUES.", font_size=18),
                Text("3. Appliquer la formule de Descartes (ou Newton).", font_size=18),
                Text("4. Conclure sur la nature, le sens et la taille", font_size=18),
                Text("    de l'image (signes de OA' et de γ).", font_size=18),
                Text("5. Vérifier la cohérence avec le schéma tracé.", font_size=18),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=11.6,
        )
        methode1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première méthode : pour résoudre un exercice de "
                "conjugaison, suivre cinq étapes. Un, faire un schéma "
                "clair avec l'axe, la lentille, O, F et F prime. Deux, "
                "lister toutes les données en mesures algébriques, avec "
                "leur signe. Trois, appliquer la formule de Descartes, ou "
                "celle de Newton selon les données disponibles. Quatre, "
                "conclure sur la nature, le sens et la taille de l'image, "
                "à partir des signes de O A prime et de gamma. Cinq, "
                "vérifier que le résultat est cohérent avec le schéma "
                "tracé."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : construction graphique propre + astuce système 2 lentilles --
        methode2 = method_box(
            VGroup(
                Text("Construction graphique propre", font_size=20, weight="BOLD"),
                Text("Tracer deux des trois rayons particuliers depuis un", font_size=17),
                Text("même point de l'objet ; le troisième vérifie.", font_size=17),
                Text("Système de deux lentilles séparées", font_size=20, weight="BOLD"),
                Text("Traiter les lentilles SUCCESSIVEMENT : l'image de L1", font_size=17),
                Text("devient l'objet de L2.", font_size=17),
                MathTex(r"\gamma_{\text{total}} = \gamma_1 \times \gamma_2", font_size=24, color=YELLOW),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=11.4,
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour une construction graphique propre, tracer deux des "
                "trois rayons particuliers depuis un même point de "
                "l'objet ; le troisième sert à vérifier. Pour un système "
                "de deux lentilles séparées, les traiter successivement : "
                "l'image donnée par la première lentille devient l'objet "
                "de la seconde. Le grandissement total est alors le "
                "produit des deux grandissements, gamma total égale "
                "gamma 1 fois gamma 2."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Exemple : contrôles rapides -----------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Contrôles rapides utiles en fin d'exercice", font_size=20, weight="BOLD"),
                Text("Objet très éloigné → l'image se forme près de F' :", font_size=18),
                MathTex(r"\overline{OA'} \approx f'", font_size=22, color=YELLOW),
                Text("Le produit de Newton doit toujours redonner :", font_size=18),
                MathTex(r"\overline{FA}\cdot\overline{F'A'} = -f'^2", font_size=22, color=YELLOW),
            ).arrange(DOWN, buff=0.18),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux contrôles rapides très utiles en fin d'exercice. "
                "Si l'objet est très éloigné, l'image doit se former tout "
                "près de F prime, soit O A prime environ égal à f prime. "
                "Et le produit de Newton doit toujours redonner F A fois "
                "F prime A prime égale moins f prime au carré : si ce "
                "n'est pas le cas, il y a une erreur de calcul quelque "
                "part."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : synthèse finale du chapitre ---------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre", font_size=23, weight="BOLD"),
                MathTex(r"C = \dfrac{1}{f'} \qquad \dfrac{1}{\overline{OA'}}-\dfrac{1}{\overline{OA}} = \dfrac{1}{f'} \qquad \gamma = \dfrac{\overline{OA'}}{\overline{OA}}", font_size=20),
                MathTex(r"\overline{FA}\cdot\overline{F'A'} = -f'^2 \qquad C_{\text{accolées}} = C_1+C_2", font_size=20),
                Text("Toujours des mesures ALGÉBRIQUES, toujours un schéma.", font_size=18, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de tout le chapitre : la vergence C "
                "égale un sur f prime ; la formule de Descartes, un sur O "
                "A prime moins un sur O A égale un sur f prime ; le "
                "grandissement gamma égale O A prime sur O A ; la formule "
                "de Newton, F A fois F prime A prime égale moins f prime "
                "au carré ; et pour des lentilles accolées, les vergences "
                "s'additionnent. Dans tous les cas : toujours des mesures "
                "algébriques, et toujours un schéma."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter : récapitulatif de tout le chapitre ----------------------
        piege = warning_box(
            VGroup(
                Text("• Vergence : f' TOUJOURS en mètres (f'=40cm → C=2,5δ,", font_size=17),
                Text("   jamais 0,025 δ).", font_size=17),
                Text("• Lentille divergente : garder f' < 0 et C < 0 partout,", font_size=17),
                Text("   jamais de valeur absolue substituée.", font_size=17),
                Text("• Ne pas confondre les foyers : rayon // axe → sort", font_size=17),
                Text("   par F' ; rayon passant par F → sort // axe.", font_size=17),
                Text("• Formule de Newton : distances depuis F et F',", font_size=17),
                Text("   PAS depuis O (ne pas mélanger avec Descartes).", font_size=17),
                Text("• Image virtuelle : prolongements en POINTILLÉS,", font_size=17),
                Text("   jamais de rayons réels qui se croiseraient.", font_size=17),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.09),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Récapitulons les pièges à éviter absolument. Pour la "
                "vergence, f prime doit toujours être exprimée en "
                "mètres. Pour une lentille divergente, garder f prime "
                "négatif et C négatif partout, sans jamais substituer une "
                "valeur absolue. Ne pas confondre les foyers : le rayon "
                "parallèle à l'axe sort par F prime, le rayon qui passe "
                "par F sort parallèle à l'axe. Dans la formule de Newton, "
                "les distances se mesurent depuis F et F prime, pas "
                "depuis O. Et une image virtuelle se construit toujours "
                "avec des prolongements en pointillés, jamais avec des "
                "rayons réels qui se croiseraient."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
