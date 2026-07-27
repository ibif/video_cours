"""
scenes/Physique_EnergieCinetique_09.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 09 (synthèse finale du chapitre).

§ Méthode pour résoudre un exercice avec le théorème de l'énergie cinétique
(6 étapes), méthode pour un solide qui roule sans glisser
(Ec=½m(1+k)v², J_Δ=kmR²). Pièges à éviter : unités (m/s, kg, rad/s,
conversion tr/min→rad/s), signe du travail du poids (moteur/résistant),
confusion des moments d'inertie usuels, tension du fil du pendule qui ne
travaille pas.
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, synthèse).
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse — Méthodes et pièges à éviter")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Ce chapitre a introduit l'énergie cinétique de translation "
                "et de rotation, le moment d'inertie, et le théorème de "
                "l'énergie cinétique. Terminons par une méthode de "
                "résolution et les pièges classiques à éviter.",
                width=58,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce chapitre a introduit l'énergie cinétique de "
                "translation et de rotation, le moment d'inertie, et le "
                "théorème de l'énergie cinétique. Terminons par une "
                "méthode de résolution en six étapes, et par les pièges "
                "classiques à éviter absolument."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Méthode : 6 étapes pour un exercice avec le TEC ------------------------
        methode = VGroup(
            Text("1. Définir le système étudié et le référentiel (galiléen).", font_size=20),
            Text("2. Faire le bilan des forces extérieures appliquées.", font_size=20),
            Text("3. Identifier clairement l'état initial A et l'état final B.", font_size=20),
            Text("4. Calculer le travail de CHAQUE force entre A et B.", font_size=20),
            Text("5. Écrire le théorème : ΔEc = ΣW(F_ext).", font_size=20),
            Text("6. Isoler l'inconnue cherchée (souvent une vitesse).", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        methode_box_ = method_box(methode, box_width=12.4)
        methode_box_.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici la méthode en six étapes pour résoudre un exercice "
                "avec le théorème de l'énergie cinétique. Un : définir "
                "clairement le système étudié et le référentiel, qui doit "
                "être galiléen. Deux : faire le bilan de toutes les forces "
                "extérieures appliquées. Trois : identifier précisément "
                "l'état initial A et l'état final B. Quatre : calculer le "
                "travail de chaque force, une par une, entre A et B. "
                "Cinq : écrire le théorème, la variation d'énergie "
                "cinétique égale la somme des travaux. Six : isoler "
                "l'inconnue cherchée, le plus souvent une vitesse."
            )
        ) as tracker:
            self.play(FadeIn(methode_box_))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_box_))

        # --- Méthode : solide qui roule sans glisser --------------------------------
        methode_roule = VGroup(
            Text("Solide qui roule sans glisser, avec J_Δ = k m R² :", font_size=21),
            MathTex(r"E_c = \dfrac{1}{2}mv^2 + \dfrac{1}{2}J_\Delta\omega^2 = \dfrac{1}{2}m(1+k)v^2", font_size=25),
            Text("(k = 1 anneau, k = 1/2 disque, k = 2/5 sphère, avec v = Rω)", font_size=19),
        ).arrange(DOWN, buff=0.25)
        methode_roule_box = method_box(methode_roule, box_width=12.2)
        methode_roule_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Astuce pratique pour un solide qui roule sans glisser : "
                "en écrivant son moment d'inertie sous la forme J delta "
                "égale k m R carré, où k est une constante qui dépend de "
                "la forme du solide, l'énergie cinétique totale se "
                "factorise en un demi m, un plus k, v carré. Par exemple, "
                "k vaut un pour un anneau, un demi pour un disque, et deux "
                "cinquièmes pour une sphère, en utilisant toujours la "
                "relation v égale R oméga."
            )
        ) as tracker:
            self.play(FadeIn(methode_roule_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_roule_box))

        # --- Piège 1 : unités ---------------------------------------------------------
        piege1 = warning_box(
            VGroup(
                Text("Toujours vérifier les unités avant de calculer :", font_size=21),
                Text("vitesses en m/s, masses en kg, ω en rad/s.", font_size=21),
                Text("Pour convertir des tr/min en rad/s, diviser D'ABORD", font_size=21),
                Text("par 60 (→ tr/s), PUIS multiplier par 2π.", font_size=21),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        piege1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier piège, le plus fréquent : les unités. Les "
                "vitesses doivent toujours être en mètres par seconde, "
                "les masses en kilogrammes, et les vitesses angulaires en "
                "radians par seconde. Pour convertir des tours par "
                "minute en radians par seconde, il faut d'abord diviser "
                "par soixante pour obtenir des tours par seconde, puis "
                "seulement ensuite multiplier par deux pi."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        # --- Piège 2 : signe du travail du poids ---------------------------------------
        piege2 = warning_box(
            VGroup(
                Text("Le travail du poids est MOTEUR (W > 0) si le corps", font_size=21),
                Text("descend, RÉSISTANT (W < 0) s'il monte. Toujours vérifier", font_size=21),
                Text("le sens réel du déplacement avant de fixer le signe.", font_size=21),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        piege2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième piège : le signe du travail du poids. Il est "
                "moteur, donc positif, si le corps descend ; il est "
                "résistant, donc négatif, s'il monte. Il faut toujours "
                "vérifier le sens réel du déplacement avant de fixer ce "
                "signe, ne jamais le deviner."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        # --- Piège 3 : confusion des moments d'inertie ----------------------------------
        piege3_texte = Text(
            "Ne pas confondre les moments d'inertie usuels selon le solide\n"
            "ET l'axe : (1/12)Mℓ² (tige, axe central) ≠ (1/3)Mℓ² (tige,\n"
            "axe à l'extrémité) ; MR² (cerceau) ≠ (1/2)MR² (disque).",
            font_size=20,
        )
        piege3 = warning_box(piege3_texte, box_width=12.2)
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège : ne jamais confondre les moments "
                "d'inertie usuels, qui dépendent à la fois du solide et "
                "de la position de l'axe. Un douzième M ℓ carré, pour une "
                "tige par son axe central, n'est pas égal à un tiers M ℓ "
                "carré, pour la même tige par son extrémité. De même, M R "
                "carré pour un cerceau n'est pas égal à un demi M R carré "
                "pour un disque."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- Piège 4 : tension du fil du pendule -----------------------------------------
        piege4 = warning_box(
            VGroup(
                Text("Ne pas oublier que la tension du fil du pendule ne", font_size=21),
                Text("travaille JAMAIS : elle est radiale, donc perpendiculaire", font_size=21),
                Text("au déplacement tangentiel à chaque instant (W = 0).", font_size=21),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        piege4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatrième et dernier piège : ne jamais oublier que la "
                "tension du fil d'un pendule ne travaille jamais, car "
                "elle est radiale, donc perpendiculaire au déplacement "
                "tangentiel à chaque instant du mouvement. Un travail "
                "toujours nul, à ne surtout pas inclure dans le bilan des "
                "travaux."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- L'essentiel à retenir (synthèse finale du chapitre) -------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre", font_size=24, weight="BOLD"),
                MathTex(r"E_c = \dfrac{1}{2}mv^2 \ (\text{translation}), \quad E_c = \dfrac{1}{2}J_\Delta\omega^2 \ (\text{rotation})", font_size=22),
                MathTex(r"\Delta E_c = \sum W_{A\to B}(\vec{F}_{ext})", font_size=24, color=YELLOW),
                Text("Applications : freinage (d ∝ v²), chute libre (v=√(2gh)), pendule.", font_size=20),
            ).arrange(DOWN, buff=0.24),
            box_width=12.6,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de tout ce chapitre : l'énergie "
                "cinétique de translation vaut un demi m v carré, celle de "
                "rotation vaut un demi J delta oméga carré, et dans tous "
                "les cas, le théorème de l'énergie cinétique relie la "
                "variation d'énergie cinétique à la somme des travaux des "
                "forces extérieures. Trois applications à maîtriser : le "
                "freinage, où la distance est proportionnelle au carré de "
                "la vitesse, la chute libre, avec v égale racine de deux g "
                "h, et le pendule simple."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
