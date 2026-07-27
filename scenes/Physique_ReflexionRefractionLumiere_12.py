"""
scenes/Physique_ReflexionRefractionLumiere_12.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 12 (synthèse
finale du chapitre).

§ Synthèse : méthode pour résoudre un exercice de miroir plan en 4 étapes,
méthode pour résoudre un exercice de réfraction en 4 étapes. Pièges :
angle par rapport à la surface, calculatrice en mode degrés, sin i2 > 1
signale une réflexion totale, réflexion totale oubliée, fibre
optique/fontaine lumineuse (milieu plus réfringent que l'environnant),
lame à faces parallèles (rayon non dévié, seulement déplacé).
Source : 1ereC/Physique.pdf, pages 117-129 (synthèse de chapitre).
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
                "Ce chapitre a introduit la réflexion, le miroir plan, la "
                "réfraction, la réflexion totale et ses applications, "
                "ainsi que la lame à faces parallèles. Terminons par des "
                "méthodes de résolution et les pièges classiques.",
                width=58,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce chapitre a introduit la réflexion, le miroir plan, la "
                "réfraction, la réflexion totale et ses applications, "
                "ainsi que la lame à faces parallèles. Terminons par deux "
                "méthodes de résolution, puis par les pièges classiques à "
                "éviter absolument."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Méthode 1 : exercice de miroir plan en 4 étapes --------------------------
        methode1 = method_box(
            VGroup(
                Text("Résoudre un exercice de miroir plan en 4 étapes :", font_size=20, weight="BOLD"),
                Text("1. Identifier le ou les points objets et le plan du miroir.", font_size=19),
                Text("2. Construire l'image de chaque point : symétrique par", font_size=19),
                Text("   rapport au plan du miroir (perpendiculaire, distance", font_size=19),
                Text("   conservée).", font_size=19),
                Text("3. Tracer les rayons utiles si nécessaire, en appliquant", font_size=19),
                Text("   i1' = i1 en chaque point d'incidence.", font_size=19),
                Text("4. Lire les caractéristiques de l'image (virtuelle, même", font_size=19),
                Text("   grandeur, distance).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.6,
        )
        methode1.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Première méthode : résoudre un exercice de miroir plan "
                "en quatre étapes. Un : identifier le ou les points "
                "objets, et le plan du miroir. Deux : construire l'image "
                "de chaque point, en prenant son symétrique par rapport "
                "au plan du miroir, la perpendiculaire au miroir et la "
                "distance étant conservées. Trois : tracer les rayons "
                "utiles si nécessaire, en appliquant i'1 égale i1 en "
                "chaque point d'incidence. Quatre : lire les "
                "caractéristiques de l'image obtenue, virtuelle, de même "
                "grandeur, à la distance calculée."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : exercice de réfraction en 4 étapes ----------------------------
        methode2 = method_box(
            VGroup(
                Text("Résoudre un exercice de réfraction en 4 étapes :", font_size=20, weight="BOLD"),
                Text("1. Identifier les deux milieux et leurs indices n1, n2", font_size=19),
                Text("   (lequel est le plus réfringent ?).", font_size=19),
                Text("2. Si n1 > n2 : calculer d'abord l'angle limite λ", font_size=19),
                MathTex(r"(\sin\lambda = n_2/n_1) \text{ et le comparer à } i_1.", font_size=20),
                Text("3. Si i1 < λ (ou n2 > n1) : appliquer n1 sin i1 = n2 sin i2", font_size=19),
                Text("   pour trouver i2.", font_size=19),
                Text("4. Si i1 > λ : conclure à une réflexion totale, il n'y a", font_size=19),
                Text("   PAS de rayon réfracté.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.6,
        )
        methode2.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Deuxième méthode : résoudre un exercice de réfraction en "
                "quatre étapes. Un : identifier les deux milieux "
                "traversés et leurs indices n1 et n2, en repérant lequel "
                "est le plus réfringent. Deux : si n1 est supérieur à n2, "
                "calculer d'abord l'angle limite lambda, et le comparer à "
                "i1, avant tout autre calcul. Trois : si i1 est inférieur "
                "à lambda, ou si n2 est supérieur à n1, appliquer "
                "directement la loi de Snell-Descartes pour trouver i2. "
                "Quatre : si i1 est supérieur à lambda, conclure à une "
                "réflexion totale, il n'y a alors pas de rayon réfracté "
                "du tout."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Piège 1 : angle par rapport à la surface --------------------------------
        piege1 = warning_box(
            VGroup(
                Text("Un angle donné dans un énoncé peut être mesuré par", font_size=20),
                Text("rapport à la SURFACE, pas à la normale : il faut alors", font_size=20),
                Text("le convertir en calculant 90° moins cet angle.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premier piège, très fréquent : un angle donné dans un "
                "énoncé peut être mesuré par rapport à la surface, et non "
                "par rapport à la normale. Il faut alors le convertir, en "
                "calculant quatre-vingt-dix degrés moins cet angle, avant "
                "d'utiliser les lois de Snell-Descartes."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        # --- Piège 2 : calculatrice en degrés, sin i2 > 1 ---------------------------------
        piege2 = warning_box(
            VGroup(
                Text("Toujours régler la calculatrice en mode DEGRÉS.", font_size=20),
                Text("Si un calcul donne sin i2 > 1, ce n'est PAS une erreur :", font_size=20),
                Text("c'est le signal qu'il y a réflexion totale (voir piège 3).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deuxième piège : toujours régler la calculatrice en mode "
                "degrés. Et si un calcul intermédiaire donne un sinus de "
                "i2 supérieur à un, ce n'est pas une erreur de calcul : "
                "c'est justement le signal qu'il y a réflexion totale, et "
                "non un rayon réfracté à trouver."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        # --- Piège 3 : réflexion totale oubliée --------------------------------------------
        piege3 = warning_box(
            VGroup(
                Text("Dès que n1 > n2, TOUJOURS calculer l'angle limite λ", font_size=20),
                Text("AVANT de chercher i2 : oublier cette vérification mène", font_size=20),
                Text("à un calcul impossible (arcsin d'un nombre > 1).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege3.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Troisième piège : dès que n1 est supérieur à n2, il faut "
                "toujours calculer l'angle limite lambda avant de "
                "chercher i2. Oublier cette vérification mène directement "
                "à un calcul impossible, un arc sinus d'un nombre "
                "supérieur à un."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- Piège 4 : fibre optique / fontaine lumineuse ------------------------------
        piege4 = warning_box(
            VGroup(
                Text("Fibre optique, fontaine lumineuse : le milieu où se", font_size=20),
                Text("propage la lumière doit TOUJOURS être plus réfringent", font_size=20),
                Text("que le milieu environnant (cœur > gaine, eau > air).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        piege4.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quatrième piège : pour la fibre optique comme pour la "
                "fontaine lumineuse, le milieu où se propage la lumière "
                "doit toujours être plus réfringent que le milieu "
                "environnant, le cœur plus que la gaine, l'eau plus que "
                "l'air. Sans cette condition, aucune réflexion totale, "
                "donc aucun guidage."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- Piège 5 : lame à faces parallèles ------------------------------------------
        piege5 = warning_box(
            VGroup(
                Text("Lame à faces parallèles : le rayon émergent N'EST PAS", font_size=20),
                Text("dévié (même direction que l'incident) — il est", font_size=20),
                Text("seulement déplacé latéralement d'une distance d.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        piege5.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Cinquième et dernier piège : pour une lame à faces "
                "parallèles, le rayon émergent n'est pas dévié, il "
                "conserve la même direction que le rayon incident. Il est "
                "seulement déplacé latéralement d'une distance d, jamais "
                "dévié angulairement."
            )
        ) as tracker:
            self.play(FadeIn(piege5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege5))

        # --- L'essentiel à retenir (synthèse finale du chapitre) -------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre", font_size=24, weight="BOLD"),
                MathTex(r"i_1' = i_1 \quad ; \quad n = \dfrac{c}{v} \quad ; \quad n_1 \sin i_1 = n_2 \sin i_2", font_size=22),
                MathTex(r"\sin \lambda = \dfrac{n_2}{n_1} \ , \quad \text{réflexion totale} \Leftrightarrow n_1 > n_2 \ \text{et} \ i_1 > \lambda", font_size=20, color=YELLOW),
                MathTex(r"\text{lame} : i_1' = i_1 \ , \quad d = e\dfrac{\sin(i_1-i_2)}{\cos i_2}", font_size=22),
            ).arrange(DOWN, buff=0.22),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de tout ce chapitre : l'angle de "
                "réflexion égale l'angle d'incidence, l'indice de "
                "réfraction vaut c sur v, et la loi de Snell-Descartes de "
                "la réfraction relie n1 sinus i1 à n2 sinus i2. L'angle "
                "limite vérifie sinus lambda égale n2 sur n1, et la "
                "réflexion totale exige à la fois n1 supérieur à n2 et i1 "
                "supérieur à lambda. Enfin, une lame à faces parallèles "
                "ne dévie pas le rayon, elle le déplace seulement "
                "latéralement d'une distance d."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
