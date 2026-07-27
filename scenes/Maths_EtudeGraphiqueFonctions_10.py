"""
scenes/Maths_EtudeGraphiqueFonctions_10.py — Chapitre 11 (1ereC, Maths), scène 10.

Synthèse du chapitre : méthode de rédaction (les 8 points dans l'ordre),
méthode de contrôle rapide de l'asymptote oblique (lim f(x)/x = a),
méthode pour prouver un centre de symétrie, méthode du trinôme et racine
évidente, et récapitulatif des quatre pièges classiques du chapitre.
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Méthodes, astuces et pièges à éviter")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Synthèse du chapitre : les réflexes à avoir le jour du bac",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par une synthèse : les méthodes "
                "pratiques à automatiser, et les pièges les plus fréquents "
                "sur l'étude et la représentation graphique d'une "
                "fonction."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Méthode de rédaction --------------------------------------------
        methode_redaction = method_box(
            MathTex(
                r"""
                \begin{array}{l}
                D_f \ \to \ \text{parité/périodicité} \ \to \ \text{limites} \ \to \ \text{asymptotes} \\
                \to \ \text{dérivée et signe} \ \to \ \text{tableau} \ \to \ \text{points remarquables} \ \to \ \text{tracé}
                \end{array}
                """,
                font_size=22,
            ),
            box_width=11.4,
        )
        methode_redaction.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première méthode à automatiser : la rédaction complète, "
                "dans l'ordre — domaine, parité ou périodicité, limites, "
                "asymptotes, dérivée et signe, tableau de variation, "
                "points remarquables, puis tracé. C'est le fil conducteur "
                "de tout le chapitre, quelle que soit la famille de "
                "fonctions."
            )
        ) as tracker:
            self.play(FadeIn(methode_redaction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_redaction))

        # --- Méthode contrôle rapide asymptote oblique -----------------------
        methode_controle = method_box(
            MathTex(
                r"\text{Contrôle rapide : } a = \lim_{x\to\infty} \dfrac{f(x)}{x}"
                r"\ , \quad b = \lim_{x\to\infty} \big[f(x)-ax\big]",
                font_size=27,
            ),
            box_width=10.8,
        )
        methode_controle.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième méthode : pour contrôler rapidement une "
                "asymptote oblique trouvée par division euclidienne, on "
                "peut recalculer a comme la limite de f de x sur x, puis b "
                "comme la limite de f de x moins a x. Si on retrouve les "
                "mêmes valeurs, le résultat est confirmé."
            )
        ) as tracker:
            self.play(FadeIn(methode_controle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_controle))

        # --- Méthode prouver un centre de symétrie ---------------------------
        methode_centre = method_box(
            MathTex(
                r"\text{Poser } h(x) = f(\alpha+x)+f(\alpha-x)"
                r"\ ,\ \text{simplifier, et vérifier } h(x) = 2\beta \ \forall x",
                font_size=25,
            ),
            box_width=10.8,
        )
        methode_centre.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième méthode : pour prouver qu'un point oméga de "
                "coordonnées alpha, bêta est centre de symétrie, on pose h "
                "de x égale f de alpha plus x, plus f de alpha moins x, on "
                "simplifie complètement cette expression, et on vérifie "
                "qu'elle est constamment égale à deux bêta, quel que soit x."
            )
        ) as tracker:
            self.play(FadeIn(methode_centre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_centre))

        # --- Méthode trinôme et racine évidente ------------------------------
        methode_racine = method_box(
            MathTex(
                r"\text{Racines évidentes à tester : } \pm1,\ \pm2,\ \pm3,\ \pm\dfrac{1}{2}"
                r"\ \Longrightarrow \ \text{factoriser par } (x-x_0)",
                font_size=25,
            ),
            box_width=10.8,
        )
        methode_racine.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quatrième méthode : face à un trinôme ou à un polynôme "
                "dont on cherche une racine, on teste systématiquement les "
                "valeurs évidentes plus ou moins un, plus ou moins deux, "
                "plus ou moins trois, et plus ou moins un demi. Dès qu'une "
                "racine x zéro est trouvée, on factorise par x moins x "
                "zéro pour continuer."
            )
        ) as tracker:
            self.play(FadeIn(methode_racine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_racine))

        # --- Récapitulatif des 4 pièges classiques ---------------------------
        enonce_pieges = Text(
            "Les quatre pièges classiques du chapitre",
            font_size=27,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_pieges.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Récapitulons enfin les quatre pièges les plus fréquents "
                "de ce chapitre, ceux qui coûtent le plus de points au bac."
            )
        ) as tracker:
            self.play(FadeIn(enonce_pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_pieges))

        piege_a = warning_box(
            Text(
                _wrap(
                    "Piège (a) — homographique : jamais « croissante sur "
                    "ℝ\\{-1} », mais « sur chacun des deux intervalles ».",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        piege_a.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège a : pour une fonction homographique, ne jamais "
                "écrire « croissante sur ℝ privé de moins un », mais bien "
                "« sur chacun des deux intervalles séparément »."
            )
        ) as tracker:
            self.play(FadeIn(piege_a))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_a))

        piege_b = warning_box(
            Text(
                _wrap(
                    "Piège (b) — irrationnelle : √u n'est pas dérivable là "
                    "où u s'annule (demi-tangente verticale, pas un point "
                    "anguleux).",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        piege_b.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège b : pour une fonction irrationnelle, racine de u "
                "n'est pas dérivable là où u s'annule — on obtient une "
                "demi-tangente verticale, pas un point anguleux ordinaire."
            )
        ) as tracker:
            self.play(FadeIn(piege_b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_b))

        piege_c = warning_box(
            Text(
                _wrap(
                    "Piège (c) — parité : vérifier d'abord que Df est "
                    "symétrique par rapport à 0, AVANT de calculer f(-x). "
                    "Sinon, f est ni paire ni impaire, point final.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        piege_c.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège c : avant même de se demander si une fonction est "
                "paire ou impaire, il faut vérifier que son domaine est "
                "symétrique par rapport à zéro. Si ce n'est pas le cas, "
                "elle n'est ni paire ni impaire, un point c'est tout."
            )
        ) as tracker:
            self.play(FadeIn(piege_c))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_c))

        piege_d = warning_box(
            Text(
                _wrap(
                    "Piège (d) — position par rapport à une asymptote : "
                    "étudier le signe de f(x) - (ax+b) sur TOUT le domaine "
                    "avec un tableau de signes, jamais seulement « au "
                    "voisinage de l'infini ».",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        piege_d.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège d : pour la position de la courbe par rapport à une "
                "asymptote, il faut étudier le signe de f de x moins a x "
                "plus b sur tout le domaine, avec un vrai tableau de "
                "signes, jamais seulement « au voisinage de l'infini »."
            )
        ) as tracker:
            self.play(FadeIn(piege_d))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_d))

        # --- À retenir (synthèse finale) ----------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Toute étude de fonction suit les mêmes 8 étapes de "
                    "rédaction, quelle que soit la famille (polynôme, "
                    "homographique, rationnelle, irrationnelle, "
                    "trigonométrique). Les méthodes de contrôle rapide "
                    "(quotient f(x)/x, test de symétrie, racines évidentes) "
                    "sécurisent chaque étape.",
                    width=58,
                ),
                font_size=21,
            ),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir pour clore ce chapitre : toute étude de "
                "fonction suit la même trame de rédaction, quelle que soit "
                "la famille étudiée — polynôme, homographique, "
                "rationnelle, irrationnelle ou trigonométrique. Les "
                "méthodes de contrôle rapide vues aujourd'hui — le "
                "quotient f de x sur x, le test de symétrie, la recherche "
                "de racines évidentes — permettent de sécuriser chaque "
                "étape de cette démarche."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège final : la synthèse elle-même ------------------------------
        piege_final = warning_box(
            Text(
                _wrap(
                    "Dernier conseil : ne jamais apprendre les exemples "
                    "par cœur — apprendre la MÉTHODE, applicable à toute "
                    "nouvelle fonction rencontrée le jour de l'examen.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege_final.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Un dernier conseil, le plus important de tous : ne jamais "
                "apprendre les exemples traités par cœur, mais bien "
                "apprendre la méthode elle-même — c'est elle, et elle "
                "seule, qui sera applicable à toute nouvelle fonction "
                "rencontrée le jour de l'examen."
            )
        ) as tracker:
            self.play(FadeIn(piege_final))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege_final))
