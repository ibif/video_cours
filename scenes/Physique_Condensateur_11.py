"""
scenes/Physique_Condensateur_11.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 11.

§ 7. Synthèse : applications, méthodes et pièges à éviter. Applications
usuelles (flash d'appareil photo, lissage des tensions redressées,
minuteries/temporisateurs, accord des récepteurs radio, réserve
d'énergie). Méthodes récapitulatives : charge à courant constant,
réduction d'un groupement de condensateurs, choix de la formule
d'énergie, exploitation de τ=RC. Synthèse des pièges du chapitre.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 7, synthèse).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseApplicationsMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Le condensateur : synthèse et applications")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Nous avons vu toute la théorie du condensateur : "
                "constitution, capacité, associations, énergie, régime "
                "RC. Où le rencontre-t-on concrètement, et comment "
                "aborder méthodiquement un exercice sur ce chapitre ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Nous avons vu toute la théorie du condensateur : sa "
                "constitution, sa capacité, ses associations, son énergie, "
                "et son comportement dans un circuit R C. Où le "
                "rencontre-t-on concrètement, et comment aborder "
                "méthodiquement un exercice sur ce chapitre ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : applications -----------------------------------------
        applications = property_box(
            VGroup(
                Text("• Flash d'un appareil photo : décharge rapide, forte puissance.", font_size=19),
                Text("• Lissage des tensions redressées (alimentations électriques).", font_size=19),
                Text("• Minuteries et temporisateurs (exploitent τ = RC).", font_size=19),
                Text("• Accord des récepteurs radio (association avec une bobine).", font_size=19),
                Text("• Réserve d'énergie de secours (mémoires, appareils portables).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=12.4,
        )
        applications.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le condensateur intervient dans de nombreuses "
                "applications. Le flash d'un appareil photo se décharge "
                "rapidement pour fournir une forte puissance lumineuse "
                "instantanée. Les condensateurs lissent les tensions "
                "redressées dans les alimentations électriques. Ils "
                "servent aussi dans les minuteries et temporisateurs, en "
                "exploitant justement la constante de temps tau égale R C. "
                "On les retrouve dans l'accord des récepteurs radio, "
                "associés à une bobine, et comme réserve d'énergie de "
                "secours dans les mémoires ou appareils portables."
            )
        ) as tracker:
            self.play(FadeIn(applications))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(applications))

        # --- Méthodes récapitulatives ---------------------------------------------
        methodes = method_box(
            VGroup(
                Text("1. Charge à courant constant : utiliser q = It, puis u = q/C.", font_size=19),
                Text("2. Groupement de condensateurs : réduire étape par étape", font_size=19),
                Text("   (parallèle : on additionne ; série : on prend l'inverse).", font_size=19),
                Text("3. Énergie : choisir E=½qu, ½Cu² ou q²/(2C) selon les", font_size=19),
                Text("   données connues de l'énoncé.", font_size=19),
                Text("4. Régime RC : calculer τ = RC, puis situer l'instant étudié", font_size=19),
                Text("   par rapport aux repères 63 % / 37 % / 5τ.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.6,
        )
        methodes.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quatre méthodes à mobiliser selon le type d'exercice. "
                "Pour une charge à courant constant, on utilise q égale I "
                "t, puis u égale q sur C. Pour un groupement de "
                "condensateurs, on réduit étape par étape : on additionne "
                "en parallèle, on prend l'inverse de la somme des inverses "
                "en série. Pour l'énergie, on choisit la formule adaptée "
                "aux données connues. Et pour un régime R C, on calcule "
                "d'abord tau égale R C, puis on situe l'instant étudié par "
                "rapport aux repères soixante-trois pourcents, trente-sept "
                "pourcents, et cinq tau."
            )
        ) as tracker:
            self.play(FadeIn(methodes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methodes))

        # --- Exemple de synthèse (application combinée) -----------------------------
        exemple = example_box(
            VGroup(
                Text("Flash d'appareil photo : C = 150 µF chargé sous u = 300 V,", font_size=19),
                Text("puis déchargé dans une lampe de résistance R = 10 Ω.", font_size=19),
                MathTex(r"E = \dfrac{1}{2} C u^2 = \dfrac{1}{2}\times150\times10^{-6}\times300^2 \approx 6{,}75\ \text{J}", font_size=22),
                MathTex(r"\tau = R\,C = 10 \times 150\times10^{-6} = 1{,}5\ \text{ms}", font_size=24),
                Text("→ 6,75 J libérés en environ 5τ ≈ 7,5 ms : un éclair bref et intense.", font_size=18, color=YELLOW),
            ).arrange(DOWN, buff=0.18),
            box_width=12.8,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple de synthèse : le flash d'un appareil photo utilise "
                "un condensateur de cent cinquante microfarads, chargé sous "
                "trois cents volts, puis déchargé dans la lampe du flash, "
                "de résistance dix ohms. Son énergie vaut un demi C u "
                "carré, soit environ six virgule soixante-quinze joules. Sa "
                "constante de temps de décharge vaut R C, soit un virgule "
                "cinq milliseconde. Ces six virgule soixante-quinze joules "
                "sont donc libérés en environ cinq tau, soit sept virgule "
                "cinq millisecondes seulement : voilà pourquoi l'éclair du "
                "flash est aussi bref qu'intense."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : formulaire complet du chapitre -----------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir — formulaire complet", font_size=23, weight="BOLD"),
                MathTex(r"C = \dfrac{q}{u}\ (\text{F}), \qquad q = It \ (\text{courant constant})", font_size=22),
                MathTex(r"\text{Parallèle : } C_{\text{éq}} = \sum C_i \qquad \text{Série : } \dfrac{1}{C_{\text{éq}}} = \sum \dfrac{1}{C_i}", font_size=22),
                MathTex(r"E = \dfrac{1}{2} q u = \dfrac{1}{2} C u^2 = \dfrac{q^2}{2C} \qquad \tau = R\,C", font_size=22),
            ).arrange(DOWN, buff=0.2),
            box_width=12.6,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le formulaire complet du chapitre à retenir. La "
                "capacité C égale q sur u, en farads. Sous courant "
                "constant, q égale I t. En parallèle, les capacités "
                "s'additionnent ; en série, ce sont leurs inverses. "
                "L'énergie s'exprime sous trois formes équivalentes, un "
                "demi q u, un demi C u carré, ou q carré sur deux C. Et la "
                "constante de temps d'un circuit R C vaut R C."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter : synthèse de tout le chapitre --------------------------
        pieges = warning_box(
            VGroup(
                Text("• LE piège n°1 : ne pas inverser les formules série/parallèle", font_size=18),
                Text("   des condensateurs (inversées par rapport aux résistors).", font_size=18),
                Text("• Toujours convertir les unités (µF, nF, pF, kΩ, cm² → m²)", font_size=18),
                Text("   avant tout calcul.", font_size=18),
                Text("• En série, le PLUS PETIT condensateur supporte la PLUS", font_size=18),
                Text("   GRANDE tension.", font_size=18),
                Text("• Ne pas confondre les deux régimes de charge : droite sous", font_size=18),
                Text("   courant constant, courbe exponentielle à travers un résistor.", font_size=18),
                Text("• Respecter la polarité d'un condensateur ÉLECTROLYTIQUE.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.8,
        )
        pieges.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Pour finir, récapitulons tous les pièges du chapitre. Le "
                "piège numéro un : ne jamais inverser les formules de "
                "série et de parallèle des condensateurs, qui sont "
                "inversées par rapport à celles des résistors. Toujours "
                "convertir les unités avant tout calcul : microfarads, "
                "nanofarads, picofarads, kilohms, centimètres carrés en "
                "mètres carrés. En série, c'est le plus petit condensateur "
                "qui supporte la plus grande tension. Il ne faut pas "
                "confondre les deux régimes de charge : une droite sous "
                "courant constant, une courbe exponentielle à travers un "
                "résistor. Et il faut toujours respecter la polarité d'un "
                "condensateur électrolytique."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
