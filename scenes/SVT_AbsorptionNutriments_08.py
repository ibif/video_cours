"""
scenes/SVT_AbsorptionNutriments_08.py — Chapitre 13 (1ereD, SVT), scène 08.

§ 13.4 Le devenir immédiat des nutriments absorbés : voie sanguine (veine
porte hépatique → foie : filtre, régulateur, stockage de glycogène) et
voie lymphatique (chylomicrons, vaisseau chylifère, canal thoracique, veine
sous-clavière gauche), et piège « tous les nutriments ne passent pas dans
le sang ». Source : 1ereD/SVT.pdf, pages 176-177.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREEN,
    RED,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class DevenirNutriments(NotionScene):
    def construct(self):
        titre = scene_title("13.4 — Le devenir immédiat des nutriments")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : deux portes de sortie de la villosité --------------------
        intro = Text(
            _wrap(
                "Une fois entrés dans l'entérocyte, les nutriments ne "
                "suivent pas tous le même chemin : il existe deux portes "
                "de sortie de la villosité, le sang et la lymphe.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fois entrés dans l'entérocyte, les nutriments ne "
                "suivent pas tous le même chemin : il existe deux portes "
                "de sortie de la villosité, le sang et la lymphe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : schéma des deux voies ------------------
        enterocyte = Circle(radius=0.5, color=WHITE, fill_color=WHITE, fill_opacity=0.2, stroke_width=3)
        enterocyte_label = Text("entérocyte", font_size=16, color=WHITE)
        enterocyte_label.move_to(enterocyte.get_center())
        enterocyte.move_to(UP * 1.6)
        enterocyte_label.move_to(enterocyte.get_center())

        # voie sanguine (gauche)
        fleche_sang = Arrow(enterocyte.get_bottom() + LEFT * 0.05, enterocyte.get_bottom() + LEFT * 2.2 + DOWN * 1.3, color=RED, stroke_width=5, buff=0.1)
        vpt = Text("veine porte hépatique", font_size=15, color=RED)
        vpt.next_to(fleche_sang.get_end(), DOWN, buff=0.1)
        foie = Text("→ FOIE", font_size=18, color=RED, weight="BOLD")
        foie.next_to(vpt, DOWN, buff=0.15)
        voie_sang = VGroup(fleche_sang, vpt, foie)
        sang_label = Text("glucose, a. aminés,\neau, sels, vit. hydrosolubles", font_size=13, color=RED, line_spacing=0.8)
        sang_label.next_to(fleche_sang, LEFT, buff=0.1).shift(UP*0.3)

        # voie lymphatique (droite)
        fleche_lymphe = Arrow(enterocyte.get_bottom() + RIGHT * 0.05, enterocyte.get_bottom() + RIGHT * 2.2 + DOWN * 1.3, color=BLUE, stroke_width=5, buff=0.1)
        chylif = Text("vaisseau chylifère", font_size=15, color=BLUE)
        chylif.next_to(fleche_lymphe.get_end(), DOWN, buff=0.1)
        coeur = Text("→ canal thoracique", font_size=15, color=BLUE, weight="BOLD")
        coeur.next_to(chylif, DOWN, buff=0.15)
        voie_lymphe = VGroup(fleche_lymphe, chylif, coeur)
        lymphe_label = Text("acides gras, glycérol,\nvit. liposolubles", font_size=13, color=BLUE, line_spacing=0.8)
        lymphe_label.next_to(fleche_lymphe, RIGHT, buff=0.1).shift(UP*0.3)

        schema = VGroup(enterocyte, enterocyte_label, voie_sang, sang_label, voie_lymphe, lymphe_label)
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici les deux voies. À gauche, la voie sanguine : le "
                "glucose, les acides aminés, les sels minéraux, les "
                "vitamines hydrosolubles et l'eau traversent la paroi des "
                "capillaires sanguins de la villosité, qui se réunissent "
                "en une veine, la veine porte hépatique, laquelle conduit "
                "le sang directement au foie. À droite, la voie "
                "lymphatique : les acides gras et le glycérol, "
                "resynthétisés en chylomicrons, passent dans le vaisseau "
                "chylifère central de la villosité, puis rejoignent le "
                "canal thoracique."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : le rôle du foie et le trajet lymphatique ----------
        entete_foie = Text("La voie sanguine : le passage obligé par le foie", font_size=20, color=YELLOW, weight="BOLD")
        entete_foie.next_to(titre, DOWN, buff=0.5)

        role_foie = _bullets(
            [
                "Prélève l'excédent de glucose, le stocke sous forme de glycogène.",
                "Maintient la glycémie voisine de 1 g/L.",
                "Transforme une partie des acides aminés.",
                "Détruit les substances toxiques absorbées (alcool, médicaments).",
            ],
            font_size=18,
            width=56,
        )
        role_foie.next_to(entete_foie, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cette veine conduit le sang riche en nutriments "
                "directement au foie, avant tout retour vers le cœur. Le "
                "foie joue alors un rôle de filtre et de régulateur : il "
                "prélève l'excédent de glucose pour le stocker sous forme "
                "de glycogène, maintient la glycémie voisine d'un gramme "
                "par litre, transforme une partie des acides aminés, et "
                "détruit les substances toxiques éventuellement absorbées "
                "— alcool, additifs, médicaments. Le sang qui quitte le "
                "foie rejoint ensuite la circulation générale, qui "
                "distribue les nutriments à toutes les cellules du corps."
            )
        ) as tracker:
            self.play(FadeIn(entete_foie))
            self.play(FadeIn(role_foie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_foie), FadeOut(role_foie))

        entete_lymphe = Text("La voie lymphatique : le chemin des lipides", font_size=20, color=YELLOW, weight="BOLD")
        entete_lymphe.next_to(titre, DOWN, buff=0.5)

        trajet_lymphe = _bullets(
            [
                "Acides gras + glycérol → resynthèse en triglycérides, enrobés de protéines : les chylomicrons.",
                "Chylomicrons trop gros pour les capillaires sanguins → vaisseau chylifère → lymphe (chyle laiteux).",
                "Canal thoracique → veine sous-clavière gauche, près du cœur : les lipides rejoignent le sang sans passer par le foie.",
            ],
            font_size=17,
            width=58,
        )
        trajet_lymphe.next_to(entete_lymphe, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les acides gras et le glycérol entrent dans l'entérocyte "
                "par diffusion simple. À l'intérieur de la cellule, ils "
                "sont resynthétisés en triglycérides, les grosses "
                "molécules lipidiques de réserve, qui sont enrobés de "
                "protéines pour former de fines gouttelettes appelées "
                "chylomicrons. Ces chylomicrons, trop gros pour pénétrer "
                "dans les capillaires sanguins, passent dans le vaisseau "
                "chylifère central de la villosité. Ils gagnent ainsi la "
                "lymphe, qui devient laiteuse après un repas gras : c'est "
                "le chyle. Les vaisseaux lymphatiques de l'intestin "
                "convergent vers un grand canal, le canal thoracique, qui "
                "remonte le long de la colonne vertébrale et déverse la "
                "lymphe dans le sang au niveau de la veine sous-clavière "
                "gauche, près du cœur. Les lipides alimentaires rejoignent "
                "donc la circulation générale sans passer d'abord par le "
                "foie. Les vitamines liposolubles, A, D, E, K, dissoutes "
                "dans les graisses, suivent ce même itinéraire."
            )
        ) as tracker:
            self.play(FadeIn(entete_lymphe))
            self.play(FadeIn(trajet_lymphe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_lymphe), FadeOut(trajet_lymphe))

        # --- À retenir --------------------------------------------------------------
        a_retenir = _bullets(
            [
                "Voie sanguine : glucose, acides aminés, eau, sels, vitamines hydrosolubles → veine porte → foie.",
                "Voie lymphatique : acides gras, glycérol, vitamines liposolubles → vaisseau chylifère → canal thoracique.",
            ],
            font_size=20,
            width=56,
        )
        entete_retenir = Text("À retenir", font_size=26, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.55)
        a_retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : par la voie sanguine, glucose, acides "
                "aminés, eau, sels minéraux et vitamines hydrosolubles "
                "gagnent la veine porte hépatique puis le foie. Par la "
                "voie lymphatique, acides gras, glycérol et vitamines "
                "liposolubles gagnent le vaisseau chylifère puis le canal "
                "thoracique."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(a_retenir))

        # --- Piège à éviter : tous les nutriments ne passent pas dans le sang --
        piege = warning_box(
            Text(
                _wrap(
                    "Erreur fréquente : écrire que « tous les nutriments "
                    "absorbés gagnent le sang des capillaires ». Faux pour "
                    "les acides gras et le glycérol (transformés en "
                    "chylomicrons) ainsi que les vitamines liposolubles, "
                    "qui passent dans le vaisseau chylifère et la lymphe. "
                    "Règle simple : les sucres et les protéines digérées "
                    "prennent le sang, les graisses digérées prennent la "
                    "lymphe.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à une erreur fréquente : écrire que tous les "
                "nutriments absorbés gagnent le sang des capillaires. "
                "C'est faux pour les produits de la digestion des lipides "
                ": acides gras et glycérol, transformés en chylomicrons, "
                "ainsi que les vitamines liposolubles, passent dans le "
                "vaisseau chylifère et la lymphe, et ne rejoignent le sang "
                "qu'au niveau de la veine sous-clavière gauche. Retenons "
                "la règle simple : les sucres et les protéines digérées "
                "prennent le sang, les graisses digérées prennent la "
                "lymphe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
