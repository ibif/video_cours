"""
scenes/Physique_PuissanceEnergieElectriques_09.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 09.

§ 7 (partie 2). Facturation de l'électricité en Côte d'Ivoire (CIE).
Principe de facturation par tranches (tranche sociale à tarif réduit,
tranche suivante plus chère) + taxes. Exemple résolu complet : index
12458 → 12623 kWh (165 kWh consommés), tarif simplifié 100 premiers kWh à
60 F, reste à 80 F, taxes 10 % → 12 320 FCFA au total.
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 7).
"""

import textwrap

from manim import DOWN, LEFT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class FacturationCIE(NotionScene):
    def construct(self):
        titre = scene_title("La facturation de l'électricité (CIE)")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "En Côte d'Ivoire, la Compagnie Ivoirienne d'Électricité "
                "(CIE) facture l'énergie consommée par tranches, pas à un "
                "tarif unique. Comment lire une facture et retrouver le "
                "montant à payer à partir de l'index du compteur ?",
                width=56,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En Côte d'Ivoire, la Compagnie Ivoirienne d'Électricité, "
                "la C I E, facture l'énergie consommée par tranches, et non "
                "à un tarif unique pour tous les kilowattheures. Comment "
                "lire une facture, et retrouver le montant à payer à partir "
                "de l'index relevé sur le compteur ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : principe de la facturation par tranches --------------
        principe = definition_box(
            VGroup(
                Text("Facturation par tranches :", font_size=21, weight="BOLD"),
                Text("• tranche sociale (premiers kWh) : tarif réduit ;", font_size=20),
                Text("• tranche(s) suivante(s) : tarif plus élevé au kWh ;", font_size=20),
                Text("• des taxes (ex. 10 %) s'ajoutent au sous-total.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.2,
        )
        principe.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le principe de la facturation par tranches est le "
                "suivant. Une première tranche, dite tranche sociale, "
                "couvre les premiers kilowattheures consommés à un tarif "
                "réduit, pour protéger les petits foyers. Au-delà, chaque "
                "kilowattheure supplémentaire est facturé à un tarif plus "
                "élevé. Enfin, des taxes, par exemple dix pour cent, "
                "s'ajoutent au sous-total pour obtenir le montant final."
            )
        ) as tracker:
            self.play(FadeIn(principe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(principe))

        methode = method_box(
            VGroup(
                Text("Méthode pour lire une facture :", font_size=21, weight="BOLD"),
                Text("1. Consommation = index nouveau − index ancien.", font_size=20),
                Text("2. Répartir la consommation entre les tranches tarifaires.", font_size=20),
                Text("3. Calculer le coût de chaque tranche, les additionner.", font_size=20),
                Text("4. Ajouter les taxes au sous-total pour le montant final.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la méthode en quatre étapes pour lire une facture. "
                "Un : calculer la consommation, différence entre le "
                "nouvel index et l'ancien index. Deux : répartir cette "
                "consommation entre les différentes tranches tarifaires. "
                "Trois : calculer le coût de chaque tranche, puis les "
                "additionner pour obtenir le sous-total. Quatre : ajouter "
                "les taxes à ce sous-total pour obtenir le montant final à "
                "payer."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple résolu complet -----------------------------------------------
        exemple1 = example_box(
            VGroup(
                Text("Index ancien : 12458 kWh — Index nouveau : 12623 kWh.", font_size=20),
                Text("Tarif simplifié : 100 premiers kWh à 60 F, le reste à 80 F.", font_size=20),
                Text("Taxes : 10 % du sous-total.", font_size=20),
                MathTex(r"\text{Consommation} = 12623 - 12458 = 165\ \text{kWh}", font_size=25),
            ).arrange(DOWN, buff=0.22),
            box_width=12.2,
        )
        exemple1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu complet. Une facture indique un ancien "
                "index de douze mille quatre cent cinquante-huit "
                "kilowattheures, et un nouvel index de douze mille six cent "
                "vingt-trois kilowattheures. Le tarif simplifié applique "
                "soixante francs pour les cent premiers kilowattheures, "
                "puis quatre-vingts francs au-delà, avec des taxes de dix "
                "pour cent sur le sous-total. La consommation vaut la "
                "différence des index, soit cent soixante-cinq "
                "kilowattheures."
            )
        ) as tracker:
            self.play(FadeIn(exemple1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple1))

        exemple2 = example_box(
            VGroup(
                MathTex(r"\text{Tranche 1 : } 100\ \text{kWh} \times 60\ \text{F} = 6\,000\ \text{F}", font_size=24),
                MathTex(r"\text{Tranche 2 : } (165-100)\ \text{kWh} \times 80\ \text{F} = 65 \times 80 = 5\,200\ \text{F}", font_size=24),
                MathTex(r"\text{Sous-total} = 6\,000 + 5\,200 = 11\,200\ \text{F}", font_size=25),
                MathTex(r"\text{Taxes} = 11\,200 \times 0{,}10 = 1\,120\ \text{F}", font_size=25),
                MathTex(r"\text{Total} = 11\,200 + 1\,120 = 12\,320\ \text{FCFA}", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
            box_width=12.4,
        )
        exemple2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Détaillons le calcul. La première tranche, les cent "
                "premiers kilowattheures, coûte cent fois soixante francs, "
                "soit six mille francs. La deuxième tranche, les "
                "soixante-cinq kilowattheures restants, coûte "
                "soixante-cinq fois quatre-vingts francs, soit cinq mille "
                "deux cents francs. Le sous-total vaut donc onze mille deux "
                "cents francs. Les taxes, dix pour cent de ce sous-total, "
                "valent mille cent vingt francs. Le montant final de la "
                "facture est donc de douze mille trois cent vingt francs "
                "C F A."
            )
        ) as tracker:
            self.play(FadeIn(exemple2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple2))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Consommation = nouvel index − ancien index (en kWh).", font_size=20),
                Text("Facturation par tranches : tarif croissant + taxes finales.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la consommation facturée est "
                "toujours la différence entre le nouvel index et l'ancien "
                "index, exprimée en kilowattheures. La facturation se fait "
                "par tranches à tarif croissant, et des taxes s'ajoutent "
                "toujours en dernier, sur le sous-total."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas appliquer le tarif de la 2e tranche à TOUTE la", font_size=20),
                Text("   consommation : seule la partie AU-DELÀ de la 1re", font_size=20),
                Text("   tranche est facturée au tarif supérieur.", font_size=20),
                Text("• Les taxes s'appliquent au SOUS-TOTAL, jamais tranche", font_size=20),
                Text("   par tranche séparément.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges fréquents à éviter. Il ne faut jamais appliquer "
                "le tarif de la deuxième tranche à l'ensemble de la "
                "consommation : seule la partie qui dépasse la première "
                "tranche est facturée au tarif supérieur, le reste garde le "
                "tarif réduit. Et les taxes s'appliquent une seule fois, "
                "sur le sous-total complet, jamais tranche par tranche "
                "séparément."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
