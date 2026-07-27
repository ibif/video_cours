"""
scenes/Physique_PuissanceEnergieElectriques_11.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 11 (synthèse finale du
chapitre).

§ Synthèse : méthode pour faire le bilan énergétique d'un dipôle en 4
étapes ; méthode pour déterminer expérimentalement E et r d'un
générateur/récepteur (pente et ordonnée à l'origine à partir de deux
mesures) ; méthode pour calculer un rendement sans se tromper (utile/total
selon le type de dipôle) ; méthode pour convertir J et kWh rapidement.
Pièges : P=UI valable pour tout dipôle mais P=RI²=U²/R valable seulement
pour un conducteur ohmique ; ne pas confondre f.é.m. E (volts) et énergie
W (joules) ; unités de temps (s pour J, h pour kWh) ; dans la loi de
Pouillet, ne pas oublier r et r' au dénominateur.
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, synthèse).
"""

import textwrap

from manim import DOWN, LEFT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

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
                "Ce chapitre a introduit l'énergie et la puissance "
                "électriques, l'effet Joule, les bilans énergétiques du "
                "générateur et du récepteur, la loi de Pouillet, et la "
                "facturation en kilowattheures. Terminons par des méthodes "
                "de résolution et les pièges classiques.",
                width=58,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce chapitre a introduit l'énergie et la puissance "
                "électriques, l'effet Joule, les bilans énergétiques du "
                "générateur et du récepteur, la loi de Pouillet, et la "
                "facturation en kilowattheures. Terminons par quatre "
                "méthodes de résolution, puis par les pièges classiques à "
                "éviter absolument."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Méthode 1 : bilan énergétique d'un dipôle en 4 étapes -----------------
        methode1 = method_box(
            VGroup(
                Text("Faire le bilan énergétique d'un dipôle en 4 étapes :", font_size=20, weight="BOLD"),
                Text("1. Identifier le type de dipôle (générateur, récepteur,", font_size=19),
                Text("   conducteur ohmique) et sa convention (I, U).", font_size=19),
                Text("2. Écrire sa loi d'Ohm (U=RI, U=E-rI ou U=E'+r'I).", font_size=19),
                Text("3. Multiplier par I pour obtenir le bilan de puissances.", font_size=19),
                Text("4. Identifier puissance échangée, utile et perdue par Joule.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.4,
        )
        methode1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Première méthode : faire le bilan énergétique d'un dipôle "
                "en quatre étapes. Un : identifier le type de dipôle, "
                "générateur, récepteur ou conducteur ohmique, et sa "
                "convention. Deux : écrire sa loi d'Ohm correspondante. "
                "Trois : multiplier cette loi par l'intensité I pour "
                "obtenir le bilan de puissances. Quatre : identifier "
                "clairement la puissance échangée, la puissance utile, et "
                "la puissance perdue par effet Joule."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : déterminer E et r expérimentalement ------------------------
        methode2 = method_box(
            VGroup(
                Text("Déterminer E (ou E') et r (ou r') expérimentalement :", font_size=20, weight="BOLD"),
                Text("Mesurer U et I pour DEUX points de fonctionnement,", font_size=19),
                Text("puis tracer (ou calculer) la droite U=f(I) :", font_size=19),
                MathTex(r"|\text{pente}| = r \ (\text{ou } r'), \qquad \text{ordonnée à l'origine} = E \ (\text{ou } E')", font_size=21),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=12.2,
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : déterminer expérimentalement E et r "
                "d'un générateur, ou E prime et r prime d'un récepteur. On "
                "mesure la tension U et l'intensité I pour deux points de "
                "fonctionnement différents, puis on trace, ou on calcule, "
                "la droite U égale f de I. La valeur absolue de la pente "
                "donne la résistance interne, et l'ordonnée à l'origine "
                "donne la f é m ou la f c é m."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Méthode 3 : calculer un rendement sans se tromper ----------------------
        methode3 = method_box(
            VGroup(
                Text("Calculer un rendement sans se tromper :", font_size=20, weight="BOLD"),
                MathTex(r"\eta = \dfrac{\text{puissance UTILE}}{\text{puissance TOTALE échangée}}", font_size=25),
                Text("Générateur : η_g = P_f/P_e = U/E (ce qu'il FOURNIT).", font_size=19),
                Text("Récepteur : η_r = P_u/P_r = E'/U (ce qu'il UTILISE).", font_size=19),
            ).arrange(DOWN, buff=0.18),
            box_width=11.6,
        )
        methode3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième méthode : calculer un rendement sans se "
                "tromper. Dans tous les cas, le rendement est le rapport de "
                "la puissance utile sur la puissance totale échangée. Pour "
                "un générateur, c'est ce qu'il fournit au circuit divisé "
                "par ce qu'il engendre, U sur E. Pour un récepteur, c'est "
                "ce qu'il utilise réellement divisé par ce qu'il reçoit, E "
                "prime sur U : la formule s'inverse selon le dipôle étudié."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Méthode 4 : convertir J et kWh rapidement -------------------------------
        methode4 = method_box(
            VGroup(
                Text("Convertir joules et kilowattheures rapidement :", font_size=20, weight="BOLD"),
                MathTex(r"W(\text{J}) = P(\text{W}) \times t(\text{s}), \qquad W(\text{kWh}) = P(\text{kW}) \times t(\text{h})", font_size=23),
                MathTex(r"1\ \text{kWh} = 3{,}6\times10^6\ \text{J}", font_size=25, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        methode4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatrième méthode : convertir joules et kilowattheures "
                "rapidement. En unités du système international, l'énergie "
                "en joules vaut la puissance en watts fois la durée en "
                "secondes. En unités pratiques, l'énergie en kilowattheures "
                "vaut la puissance en kilowatts fois la durée en heures. Et "
                "le facteur de conversion entre les deux vaut toujours trois "
                "virgule six millions."
            )
        ) as tracker:
            self.play(FadeIn(methode4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode4))

        # --- Piège 1 : P=UI vs P_J=RI² --------------------------------------------
        piege1 = warning_box(
            VGroup(
                Text("P = UI est valable pour TOUT dipôle, sans exception.", font_size=20),
                Text("Mais P_J = RI² et P_J = U²/R ne sont valables QUE pour", font_size=20),
                Text("un conducteur ohmique — jamais pour un générateur ou", font_size=20),
                Text("un moteur, où U n'est pas proportionnelle à I.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        piege1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier piège, le plus fréquent : la formule P égale U I "
                "est valable pour absolument tout dipôle. Mais les "
                "écritures P J égale R I carré et P J égale U carré sur R "
                "ne sont valables que pour un conducteur ohmique — jamais "
                "pour un générateur ou un moteur, où la tension n'est pas "
                "proportionnelle à l'intensité."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        # --- Piège 2 : E (f.é.m.) vs W (énergie) -----------------------------------
        piege2 = warning_box(
            VGroup(
                Text("Ne pas confondre la f.é.m. E, en VOLTS, avec l'énergie", font_size=20),
                Text("W, en JOULES : E n'est pas une énergie, c'est une tension.", font_size=20),
                Text("La puissance engendrée P_e = EI, elle, EST en watts.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        piege2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième piège : ne jamais confondre la f é m E, exprimée "
                "en volts, avec une énergie W, exprimée en joules. E n'est "
                "pas une énergie, c'est une tension. En revanche, la "
                "puissance engendrée, P e égale E I, est bien exprimée en "
                "watts."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        # --- Piège 3 : unités de temps ------------------------------------------------
        piege3 = warning_box(
            VGroup(
                Text("Unités de temps : la seconde (s) pour obtenir des joules,", font_size=20),
                Text("l'heure (h) pour obtenir des kilowattheures. Ne JAMAIS", font_size=20),
                Text("mélanger les deux systèmes dans un même calcul.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège : les unités de temps. Utiliser la seconde "
                "pour obtenir des joules, l'heure pour obtenir des "
                "kilowattheures, et ne jamais mélanger les deux systèmes "
                "dans un même calcul, sous peine d'une erreur d'un facteur "
                "trois mille six cents."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- Piège 4 : loi de Pouillet, ne pas oublier r et r' ----------------------
        piege4 = warning_box(
            VGroup(
                Text("Dans la loi de Pouillet, I = (E-E')/(R+r+r'), ne JAMAIS", font_size=20),
                Text("oublier les résistances internes r et r' au dénominateur :", font_size=20),
                Text("ce sont des résistances comme R, elles s'additionnent.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        piege4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatrième et dernier piège : dans la loi de Pouillet, I "
                "égale E moins E prime, sur R plus r plus r prime, il ne "
                "faut jamais oublier les résistances internes r et r prime "
                "au dénominateur. Ce sont des résistances comme R, elles "
                "s'additionnent avec elle, même si l'énoncé ne les rappelle "
                "pas explicitement."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- L'essentiel à retenir (synthèse finale du chapitre) -------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre", font_size=24, weight="BOLD"),
                MathTex(r"W = UIt, \quad P = UI, \quad P_J = RI^2 = \dfrac{U^2}{R} \ (\text{ohmique})", font_size=22),
                MathTex(r"U = E - rI \ (\text{générateur}), \quad U = E' + r'I \ (\text{récepteur})", font_size=22),
                MathTex(r"I = \dfrac{E-E'}{R+r+r'} \ (\text{Pouillet}), \quad 1\ \text{kWh} = 3{,}6\times10^6\ \text{J}", font_size=22, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de tout ce chapitre : l'énergie "
                "électrique vaut U I t, la puissance vaut U I, et la "
                "puissance Joule d'un conducteur ohmique vaut R I carré, "
                "égale U carré sur R. La loi d'Ohm s'écrit U égale E moins "
                "r I pour un générateur, U égale E prime plus r prime I "
                "pour un récepteur. La loi de Pouillet donne l'intensité "
                "d'un circuit série, et un kilowattheure vaut trois virgule "
                "six millions de joules."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
