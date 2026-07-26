"""
scenes/SVT_FonctionsGonades_09.py — Chapitre 1 (1ereD, SVT), scène 09.

§ 1.5 Synthèse : les deux fonctions liées tout au long de la vie, tableau
de synthèse final, exemple du calcul d'atrésie folliculaire, et
L'ESSENTIEL DU CHAPITRE en clôture. Source : 1ereD/SVT.pdf, pages 15-17.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class SyntheseFonctionsDesGonades(NotionScene):
    def construct(self):
        titre = scene_title("1.5 — Synthèse : deux fonctions liées à vie")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : les deux fonctions coopèrent -----------------------------
        synthese = Text(
            _wrap(
                "Les deux fonctions des gonades sont distinctes par leurs "
                "produits et leurs voies de sortie, mais elles coopèrent "
                "étroitement : la testostérone, produit endocrine, est "
                "nécessaire à la spermatogenèse, fonction exocrine ; chez "
                "la femme, les structures exocrines (follicule, corps "
                "jaune) portent aussi la fonction endocrine.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        synthese.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Les deux fonctions des gonades sont distinctes par leurs "
                "produits et leurs voies de sortie, mais elles coopèrent "
                "étroitement. La testostérone, produit de la fonction "
                "endocrine, est nécessaire à la spermatogenèse, fonction "
                "exocrine ; chez la femme, ce sont les structures de la "
                "fonction exocrine, le follicule et le corps jaune, qui "
                "portent aussi la fonction endocrine."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(synthese))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(synthese))

        calendrier = Text(
            _wrap(
                "Même calendrier : allumage à la puberté, puis, chez la "
                "femme, extinction à la ménopause (45-55 ans) quand le "
                "stock de follicules est épuisé - cycles arrêtés, taux "
                "d'œstrogènes et de progestérone effondrés. Chez l'homme, "
                "pas d'arrêt brutal : les spermatogonies se renouvellent "
                "toute la vie, la production diminue seulement avec l'âge.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        calendrier.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Les deux fonctions suivent aussi le même calendrier : "
                "allumage à la puberté, puis, chez la femme, extinction à la "
                "ménopause, vers quarante-cinq à cinquante-cinq ans, lorsque "
                "le stock de follicules est épuisé : les cycles s'arrêtent et "
                "les taux d'œstrogènes et de progestérone s'effondrent. "
                "L'homme, lui, ne connaît pas d'arrêt aussi brutal : ses "
                "spermatogonies se renouvellent toute la vie, et la "
                "production diminue seulement avec l'âge."
            )
        ) as tracker:
            self.play(FadeIn(calendrier))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calendrier))

        # --- Raisonnement : tableau de synthèse final ---------------------------
        entete_tab = Text("Tableau de synthèse", font_size=27, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        testicule_titre = Text("Testicule", font_size=25, color=YELLOW, weight="BOLD")
        testicule_lignes = _bullets(
            [
                "Fonction exocrine : spermatozoïdes, en continu",
                "Sortie des gamètes : canaux déférents",
                "Fonction endocrine : testostérone (Leydig)",
                "Sortie des hormones : sang (veines testiculaires)",
                "Début - Fin : puberté -> âge avancé, progressif",
            ],
            font_size=19,
            width=38,
        )
        testicule = VGroup(testicule_titre, testicule_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        ovaire_titre = Text("Ovaire", font_size=25, color=YELLOW, weight="BOLD")
        ovaire_lignes = _bullets(
            [
                "Fonction exocrine : ovocytes, de façon cyclique",
                "Sortie des gamètes : trompes de Fallope",
                "Fonction endocrine : œstrogènes (follicules),\nprogestérone (corps jaune)",
                "Sortie des hormones : sang (veines ovariennes)",
                "Début - Fin : puberté -> ménopause (~50 ans)",
            ],
            font_size=19,
            width=38,
        )
        ovaire = VGroup(ovaire_titre, ovaire_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        tableau = VGroup(testicule, ovaire).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        tableau.scale(0.92)

        with self.voiceover(
            text=(
                "Résumons dans un tableau de synthèse. Le testicule assure "
                "une fonction exocrine continue, des spermatozoïdes sortant "
                "par les canaux déférents, et une fonction endocrine, la "
                "testostérone des cellules de Leydig, libérée par les veines "
                "testiculaires, de la puberté à un âge avancé. L'ovaire "
                "assure une fonction exocrine cyclique, des ovocytes sortant "
                "par les trompes de Fallope, et une fonction endocrine, "
                "œstrogènes des follicules et progestérone du corps jaune, "
                "libérées par les veines ovariennes, de la puberté à la "
                "ménopause."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(testicule))
            self.play(FadeIn(ovaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : atrésie folliculaire -------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Femme avec 12 cycles/an, de 12 à 52 ans : 40 ans de "
                    "vie reproductive, soit 40×12=480 cycles, donc environ "
                    "480 ovocytes II libérés. Comparé au stock de la "
                    "puberté : 480/400000 ≈ 0,12 %. À peine un follicule "
                    "sur mille arrive à l'ovulation ; tous les autres "
                    "dégénèrent (atrésie folliculaire).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Évaluons le nombre d'ovulations au cours d'une vie de femme "
                "qui présente douze cycles par an, de douze à cinquante-deux "
                "ans. Durée de la vie reproductive : quarante ans, soit "
                "quarante fois douze égale quatre cent quatre-vingts cycles, "
                "donc environ quatre cent quatre-vingts ovocytes seconds "
                "libérés. Comparé au stock de la puberté, cela ne représente "
                "qu'environ zéro virgule douze pour cent des follicules : à "
                "peine un follicule sur mille arrive à l'ovulation, tous les "
                "autres dégénèrent, un phénomène appelé atrésie "
                "folliculaire. L'économie de la reproduction féminine "
                "repose sur un immense tri."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) -----------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Les gonades assurent une double fonction : exocrine "
                    "(gamètes) et endocrine (hormones sexuelles).",
                    "Castration = perte des deux fonctions ; greffe / "
                    "injection d'extraits = preuve du passage sanguin.",
                    "Ligature des voies génitales = gamètes bloqués, "
                    "hormones intactes : deux voies de sortie distinctes.",
                    "Spermatogenèse : 1 spermatocyte I -> 4 "
                    "spermatozoïdes ; continue, ~100 millions/jour, à "
                    "35°C.",
                    "Ovogenèse : 1 ovocyte I -> 1 ovule + globules "
                    "polaires ; cyclique, stock fixé avant la naissance.",
                    "Testostérone (Leydig) : caractères mâles + "
                    "spermatogenèse. Œstrogènes (follicules) : "
                    "caractères féminins. Progestérone (corps jaune) : "
                    "gestation.",
                    "La ménopause marque l'épuisement du stock "
                    "folliculaire et l'arrêt des deux fonctions ovariennes.",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si le contenu (7 points) dépasse la hauteur visible du
        # cadre malgré le petit corps de police, on réduit l'échelle globale
        # de la boîte pour qu'elle tienne entièrement à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. Les gonades, testicules et "
                "ovaires, assurent une double fonction : exocrine, la "
                "production de gamètes, et endocrine, la production "
                "d'hormones sexuelles. La castration supprime les deux "
                "fonctions ; la greffe ou l'injection d'extraits restaure les "
                "caractères sexuels, preuve que des substances voyagent dans "
                "le sang. La ligature des voies génitales bloque la sortie "
                "des gamètes sans affecter les hormones : les deux fonctions "
                "ont des voies de sortie différentes. La spermatogenèse "
                "transforme un spermatocyte premier en quatre "
                "spermatozoïdes, en continu, à raison d'environ cent "
                "millions par jour, à trente-cinq degrés. L'ovogenèse "
                "transforme un ovocyte premier en un seul ovule et des "
                "globules polaires, de façon cyclique, sur un stock fixé "
                "avant la naissance. La testostérone, des cellules de "
                "Leydig, assure les caractères sexuels mâles et l'entretien "
                "de la spermatogenèse ; les œstrogènes, des follicules, "
                "assurent les caractères féminins ; la progestérone, du "
                "corps jaune, prépare et maintient la gestation. Enfin, la "
                "ménopause marque l'épuisement du stock folliculaire et "
                "l'arrêt des deux fonctions de l'ovaire. Retenez la démarche "
                "expérimentale type : castration, puis greffe ou injection "
                "d'extraits, puis ligature des canaux, pour distinguer les "
                "deux fonctions des gonades."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
