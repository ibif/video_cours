"""
scenes/Maths_GeometrieAnalytiquePlan_11.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 11 (synthèse finale).

§ Méthodes et astuces : déterminer une équation de droite (point + vecteur
directeur / deux points / point + vecteur normal), passer d'une forme
d'équation à une autre, étudier la position relative de deux droites,
reconnaître l'ensemble x²+y²+ux+vy+w=0, tangence droite-cercle (2
réflexes). Synthèse des pièges à éviter de tout le chapitre.
Source : 1ereC/Maths.pdf, chapitre 14, page 175.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MethodesAstucesSynthese(NotionScene):
    def construct(self):
        titre = scene_title("Géométrie analytique du plan — Méthodes et pièges")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : objectif de la synthèse -------------------------------------
        enonce = Text(
            _wrap(
                "Ce chapitre a introduit de nombreux outils : déterminant, "
                "équations de droite, distance, cercle, tangente. "
                "Rassemblons-les en une boîte à outils de méthodes prêtes "
                "à l'emploi, et une liste des pièges les plus fréquents.",
                width=54,
            ),
            font_size=24,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Ce chapitre de géométrie analytique a introduit beaucoup "
                "d'outils : le déterminant, les différentes équations de "
                "droite, la distance d'un point à une droite, l'équation "
                "d'un cercle, la tangente. Pour terminer, rassemblons tout "
                "cela en une boîte à outils de méthodes prêtes à l'emploi, "
                "puis passons en revue les pièges les plus fréquents du "
                "chapitre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Méthodes (raisonnement + exemple condensés en synthèse) --------------
        methode1 = method_box(
            VGroup(
                Text("Déterminer une équation de droite", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "• Point A + vecteur directeur u(α;β) : "
                        "β(x-xA)-α(y-yA)=0"
                        "\n• Deux points A, B : prendre u=AB⃗ et appliquer "
                        "la méthode précédente"
                        "\n• Point A + vecteur normal n(a;b) (orthonormé) : "
                        "a(x-xA)+b(y-yA)=0",
                        width=52,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.3,
        )
        methode1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première méthode : déterminer une équation de droite. "
                "Avec un point A et un vecteur directeur u, on applique "
                "directement la formule bêta, x moins x-A, moins alpha, y "
                "moins y-A, égale zéro. Avec deux points A et B, on prend "
                "simplement u égale le vecteur A-B et on se ramène au cas "
                "précédent. Et avec un point A et un vecteur normal n, en "
                "repère orthonormé, on écrit a, x moins x-A, plus b, y "
                "moins y-A, égale zéro."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            VGroup(
                Text("Passer d'une forme d'équation à une autre", font_size=22, weight="BOLD"),
                MathTex(
                    r"ax+by+c=0 \ \xrightarrow{b\neq0} \ y=-\dfrac{a}{b}x-\dfrac{c}{b}"
                    r"\qquad ax+by+c=0 \ \xrightarrow{\vec{u}(-b;a)} \ \text{paramétrique}",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.5,
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : passer d'une forme d'équation à une "
                "autre. De la forme cartésienne à la forme réduite, on "
                "isole y, si b est non nul. De la forme cartésienne à la "
                "forme paramétrique, on lit un vecteur directeur moins b, "
                "a, avec le moyen mnémotechnique, puis on écrit le système "
                "paramétrique à partir d'un point de la droite."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            VGroup(
                Text("Position relative de deux droites", font_size=22, weight="BOLD"),
                MathTex(
                    r"ab'-a'b=0 \Rightarrow \parallel \qquad "
                    r"aa'+bb'=0 \ (\text{orthonormé}) \Rightarrow \perp \qquad "
                    r"\text{sinon} \Rightarrow \text{sécantes}",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.5,
        )
        methode3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième méthode : étudier la position relative de deux "
                "droites. On calcule d'abord a b prime moins a prime b : "
                "s'il est nul, les droites sont parallèles. Sinon, en "
                "repère orthonormé, on peut tester a a prime plus b b "
                "prime : s'il est nul, les droites sont perpendiculaires. "
                "Dans tous les autres cas, les droites sont simplement "
                "sécantes, sans être perpendiculaires."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        methode4 = method_box(
            VGroup(
                Text("Reconnaître x²+y²+ux+vy+w=0", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "1. Compléter les carrés en x et en y. "
                        "2. Calculer R = (u²+v²)/4 - w. "
                        "3. Conclure : R>0 cercle, R=0 point, R<0 vide.",
                        width=50,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        methode4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatrième méthode : reconnaître l'ensemble x carré plus y "
                "carré plus u x plus v y plus w égale zéro. On complète "
                "systématiquement les carrés en x et en y, on calcule R, et "
                "on conclut selon son signe : cercle si R est strictement "
                "positif, point si R est nul, ensemble vide si R est "
                "strictement négatif."
            )
        ) as tracker:
            self.play(FadeIn(methode4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode4))

        methode5 = method_box(
            VGroup(
                Text("Tangence droite-cercle : deux réflexes", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "1. Comparer d(Ω,(D)) et r (méthode géométrique, la "
                        "plus rapide). "
                        "2. Si un point A du cercle est déjà connu : la "
                        "tangente en A est perpendiculaire à (ΩA), ou "
                        "s'obtient par dédoublement.",
                        width=52,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.3,
        )
        methode5.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cinquième et dernière méthode : les deux réflexes face à "
                "un problème de tangence droite-cercle. Premier réflexe, "
                "le plus rapide : comparer la distance du centre à la "
                "droite avec le rayon. Deuxième réflexe, si un point A du "
                "cercle est déjà connu : la tangente en A est "
                "perpendiculaire au rayon oméga-A, et son équation "
                "s'obtient directement par dédoublement."
            )
        ) as tracker:
            self.play(FadeIn(methode5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode5))

        # --- À retenir : l'essentiel du chapitre -----------------------------------
        essentiel = essentiel_box(
            VGroup(
                MathTex(r"\overrightarrow{AB}(x_B-x_A;y_B-y_A) \qquad \det(\vec{u},\vec{v})=xy'-x'y", font_size=22),
                MathTex(r"(D):ax+by+c=0 \ \Rightarrow\ \vec{u}(-b;a),\ \vec{n}(a;b)", font_size=22),
                MathTex(r"d(A,(D)) = \dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}} \qquad \mathcal{C}: (x-a)^2+(y-b)^2=r^2", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=11.5,
        )
        essentiel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de tout le chapitre : les "
                "coordonnées du vecteur A-B, le déterminant x y prime moins "
                "x prime y pour la colinéarité, le couple vecteur "
                "directeur moins b, a et vecteur normal a, b lus sur une "
                "équation de droite, la formule de distance d'un point à "
                "une droite, et l'équation d'un cercle par son centre et "
                "son rayon."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Pièges à éviter (synthèse de tout le chapitre) ------------------------
        pieges = warning_box(
            VGroup(
                Text("Pièges à éviter — synthèse", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "• Norme, distance, aire, perpendicularité exigent "
                        "un repère ORTHONORMÉ (colinéarité et parallélisme, "
                        "eux, marchent dans tout repère)."
                        "\n• Une droite verticale x=k n'a pas d'équation "
                        "réduite y=mx+p."
                        "\n• d(A,(D)) : ne pas oublier |·| au numérateur et "
                        "√ au dénominateur."
                        "\n• Vérifier qu'un point est bien SUR le cercle "
                        "avant d'écrire l'équation de la tangente en ce "
                        "point ; un point intérieur n'a aucune tangente qui "
                        "passe par lui.",
                        width=56,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour terminer, la synthèse des pièges à éviter dans ce "
                "chapitre. Premièrement, la norme, la distance, l'aire et "
                "la perpendicularité exigent toutes un repère orthonormé, "
                "alors que la colinéarité et le parallélisme fonctionnent "
                "dans n'importe quel repère. Deuxièmement, une droite "
                "verticale n'a pas d'équation réduite. Troisièmement, dans "
                "la formule de distance d'un point à une droite, n'oubliez "
                "jamais ni la valeur absolue au numérateur, ni la racine "
                "carrée au dénominateur. Et enfin, vérifiez toujours qu'un "
                "point est bien sur le cercle avant d'écrire l'équation de "
                "la tangente en ce point : un point intérieur au cercle "
                "n'a, par définition, aucune tangente qui passe par lui."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
