"""
scenes/Maths_AnglesOrientesTrigonometrie_13.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 13 (dernière scène du chapitre).

§ Équations se ramenant aux types de base (produit nul, a cosx+b sinx=c,
second degré en cosx/sinx), inéquations trigonométriques simples (méthode
en 3 étapes, exemples résolus 12/13/14), synthèse des méthodes, pièges à
éviter, essentiel à retenir du chapitre.
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EquationsInequationsSyntheseChapitre(NotionScene):
    def construct(self):
        titre = scene_title("Équations, inéquations et synthèse")
        titre.scale(0.6)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Cette dernière scène du chapitre traite les équations "
                "qui se ramènent aux trois équations de base, les "
                "inéquations trigonométriques, puis termine par une "
                "synthèse des méthodes et des pièges à éviter."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : équations factorisables (rappel exemple 7) --------------
        factorisables = example_box(
            VGroup(
                Text("Rappel : sin5x + sinx = 0 ⟺ 2sin3x·cos2x = 0 (scène 10)", font_size=19),
                MathTex(
                    r"\sin 3x = 0 \iff 3x = k\pi \iff x = \dfrac{k\pi}{3},\ k \in \mathbb{Z}",
                    font_size=20,
                ),
                MathTex(
                    r"\cos 2x = 0 \iff 2x = \dfrac{\pi}{2}+k\pi \iff x = \dfrac{\pi}{4}+\dfrac{k\pi}{2},\ k \in \mathbb{Z}",
                    font_size=20,
                ),
                Text(
                    "Solutions : réunion des deux familles trouvées (une équation-produit donne toujours une union).",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        factorisables.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Premier type : les équations qui se factorisent en "
                "produit nul. Reprenons l'exemple de la scène "
                "précédente : sinus de cinq x plus sinus de x égale zéro "
                "équivaut à deux sinus de trois x cosinus de deux x égale "
                "zéro. On résout séparément chaque facteur : sinus de "
                "trois x égale zéro donne x égale k pi tiers ; cosinus de "
                "deux x égale zéro donne x égale pi quart plus k pi demi. "
                "L'ensemble des solutions est la réunion de ces deux "
                "familles : une équation-produit donne toujours une "
                "union, jamais une intersection."
            )
        ) as tracker:
            self.play(FadeIn(factorisables))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(factorisables))

        # --- Méthode : a cos x + b sin x = c ------------------------------------
        methode_acbs = method_box(
            VGroup(
                Text("Méthode : a cos x + b sin x = c", font_size=22, weight="BOLD"),
                MathTex(
                    r"a\cos x + b\sin x = R\cos(x-\varphi), \quad R = \sqrt{a^2+b^2}",
                    font_size=22,
                ),
                MathTex(r"\cos \varphi = \dfrac{a}{R}, \quad \sin \varphi = \dfrac{b}{R}", font_size=22),
                Text("On résout ensuite R cos(x-φ) = c, une équation de type cos u = c/R.", font_size=19),
            ).arrange(DOWN, buff=0.25),
            box_width=9.6,
        )
        methode_acbs.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deuxième type : les équations de la forme a cosinus x "
                "plus b sinus x égale c. La méthode consiste à introduire "
                "R égale racine carrée de a carré plus b carré, puis un "
                "angle phi tel que cosinus phi égale a sur R et sinus phi "
                "égale b sur R. On réécrit alors a cosinus x plus b sinus "
                "x sous la forme R cosinus de x moins phi, ce qui ramène "
                "l'équation à cosinus u égale c sur R, une équation de "
                "type de base."
            )
        ) as tracker:
            self.play(FadeIn(methode_acbs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_acbs))

        # --- Exemple résolu 11 ----------------------------------------------------
        ex11 = example_box(
            VGroup(
                Text("Résoudre √3 cosx + sinx = 1 dans ℝ.", font_size=20),
                MathTex(
                    r"R = \sqrt{3+1} = 2, \quad \cos\varphi = \dfrac{\sqrt{3}}{2},\ \sin\varphi = \dfrac{1}{2} \Rightarrow \varphi = \dfrac{\pi}{6}",
                    font_size=19,
                ),
                MathTex(
                    r"2\cos\!\left(x-\dfrac{\pi}{6}\right) = 1 \iff \cos\!\left(x-\dfrac{\pi}{6}\right) = \dfrac{1}{2} = \cos\dfrac{\pi}{3}",
                    font_size=19,
                ),
                MathTex(
                    r"\iff x = \dfrac{\pi}{2}+k2\pi \ \text{ou} \ x = -\dfrac{\pi}{6}+k2\pi,\ k \in \mathbb{Z}",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        ex11.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu onze. Résolvons racine de trois cosinus x "
                "plus sinus x égale un. Ici a égale racine de trois et b "
                "égale un, donc R égale racine de trois plus un, soit "
                "deux. On trouve cosinus phi égale racine de trois sur "
                "deux et sinus phi égale un demi, donc phi égale pi "
                "sixième. L'équation devient deux cosinus de x moins pi "
                "sixième égale un, soit cosinus de x moins pi sixième "
                "égale un demi, égale cosinus de pi tiers. On obtient x "
                "égale pi demi plus k deux pi, ou x égale moins pi "
                "sixième plus k deux pi."
            )
        ) as tracker:
            self.play(FadeIn(ex11))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex11))

        # --- Mention second degré --------------------------------------------------
        second_degre = Text(
            _wrap(
                "Autre type fréquent : une équation du second degré en "
                "cos x (ou sin x), par exemple 2cos²x − cosx − 1 = 0. On "
                "pose X = cos x, on résout l'équation du second degré en "
                "X (discriminant, racines), puis on revient à x en "
                "résolvant cos x = X₁ et cos x = X₂ — en écartant toute "
                "racine X hors de [-1 ; 1], impossible pour un cosinus.",
                width=56,
            ),
            font_size=21,
        )
        second_degre.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On rencontre aussi des équations du second degré en "
                "cosinus x, ou en sinus x, par exemple deux cosinus carré "
                "x moins cosinus x moins un égale zéro. On pose alors "
                "grand X égale cosinus x, on résout l'équation du second "
                "degré en grand X avec discriminant et racines, puis on "
                "revient à x en résolvant cosinus x égale chacune des "
                "racines trouvées, en écartant toute racine qui sortirait "
                "de l'intervalle moins un, un, impossible pour un "
                "cosinus."
            )
        ) as tracker:
            self.play(FadeIn(second_degre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(second_degre))

        # --- Méthode générale pour les inéquations -----------------------------
        methode_ineq = method_box(
            VGroup(
                Text("Méthode générale — inéquations trigonométriques simples", font_size=20, weight="BOLD"),
                Text("1) Résoudre l'équation associée pour trouver les valeurs-frontières.", font_size=19),
                Text("2) Placer ces valeurs-frontières sur le cercle trigonométrique.", font_size=19),
                Text("3) Lire graphiquement l'intervalle-solution sur le cercle, puis généraliser par périodicité.", font_size=19),
            ).arrange(DOWN, buff=0.25),
            box_width=10.6,
        )
        methode_ineq.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Passons aux inéquations trigonométriques simples. La "
                "méthode générale comporte trois étapes. Première étape : "
                "résoudre l'équation associée pour trouver les "
                "valeurs-frontières. Deuxième étape : placer ces "
                "valeurs-frontières sur le cercle trigonométrique. "
                "Troisième étape : lire graphiquement, sur le cercle, "
                "l'intervalle qui vérifie l'inégalité, puis généraliser "
                "le résultat par périodicité si l'on travaille sur ℝ tout "
                "entier."
            )
        ) as tracker:
            self.play(FadeIn(methode_ineq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_ineq))

        # --- Exemple résolu 12 -------------------------------------------------------
        ex12 = example_box(
            VGroup(
                Text("Résoudre sin x > 1/2, dans ]-π ; π] puis dans ℝ.", font_size=20),
                MathTex(
                    r"\sin x = \dfrac{1}{2} \iff x = \dfrac{\pi}{6} \ \text{ou} \ x = \dfrac{5\pi}{6} \ \text{ (dans } ]-\pi;\pi])",
                    font_size=19,
                ),
                MathTex(
                    r"\text{Dans } ]-\pi;\pi] : \quad S = \left]\dfrac{\pi}{6}\, ;\, \dfrac{5\pi}{6}\right[",
                    font_size=21,
                ),
                MathTex(
                    r"\text{Dans } \mathbb{R} : \quad S = \bigcup_{k\in\mathbb{Z}} \left]\dfrac{\pi}{6}+k2\pi\, ;\, \dfrac{5\pi}{6}+k2\pi\right[",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        ex12.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu douze. Résolvons sinus x strictement "
                "supérieur à un demi. L'équation associée sinus x égale "
                "un demi a pour solutions, dans l'intervalle ]-π ; π], x "
                "égale pi sixième et x égale cinq pi sixièmes. En "
                "observant le cercle, le sinus dépasse un demi entre ces "
                "deux points : l'ensemble solution, dans ]-π ; π], est "
                "l'intervalle ouvert pi sixième, cinq pi sixièmes. Dans ℝ "
                "tout entier, on généralise par périodicité deux pi : "
                "l'ensemble solution est la réunion, pour k entier "
                "relatif, des intervalles pi sixième plus k deux pi, cinq "
                "pi sixièmes plus k deux pi."
            )
        ) as tracker:
            self.play(FadeIn(ex12))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex12))

        # --- Exemple résolu 13 -------------------------------------------------------
        ex13 = example_box(
            VGroup(
                Text("Résoudre cos 2x ⩾ 1/2, dans ℝ.", font_size=21),
                MathTex(
                    r"\cos u = \dfrac{1}{2} \iff u = \pm\dfrac{\pi}{3} + k2\pi \ \Rightarrow \ \cos u \geqslant \dfrac{1}{2}"
                    r" \iff u \in \left[-\dfrac{\pi}{3};\dfrac{\pi}{3}\right] [2\pi]",
                    font_size=18,
                ),
                MathTex(
                    r"\text{Avec } u = 2x : \quad 2x \in \left[-\dfrac{\pi}{3}+k2\pi\, ;\, \dfrac{\pi}{3}+k2\pi\right]",
                    font_size=19,
                ),
                MathTex(
                    r"\iff x \in \left[-\dfrac{\pi}{6}+k\pi\, ;\, \dfrac{\pi}{6}+k\pi\right],\ k \in \mathbb{Z}",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        ex13.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu treize. Résolvons cosinus de deux x "
                "supérieur ou égal à un demi. En posant u égale deux x, "
                "le cosinus de u dépasse un demi lorsque u appartient à "
                "l'intervalle moins pi tiers, pi tiers, modulo deux pi. "
                "On revient à x en divisant tout par deux : attention, on "
                "divise aussi la période, qui devient pi au lieu de deux "
                "pi. On obtient x appartient à l'intervalle moins pi "
                "sixième plus k pi, pi sixième plus k pi, k entier "
                "relatif."
            )
        ) as tracker:
            self.play(FadeIn(ex13))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex13))

        # --- Exemple résolu 14 -------------------------------------------------------
        ex14 = example_box(
            VGroup(
                Text("Résoudre tan x < 1, dans ]-π/2 ; π/2[.", font_size=21),
                Text(
                    "tan x = 1 ⟺ x = π/4. La tangente est strictement croissante sur ]-π/2 ; π/2[.",
                    font_size=19,
                ),
                MathTex(r"S = \left]-\dfrac{\pi}{2}\, ;\, \dfrac{\pi}{4}\right[", font_size=24),
            ).arrange(DOWN, buff=0.3),
            box_width=9,
        )
        ex14.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu quatorze. Résolvons tangente x strictement "
                "inférieure à un, sur l'intervalle ]-π/2 ; π/2[. "
                "L'équation associée tangente x égale un donne x égale pi "
                "quart. Comme la tangente est strictement croissante sur "
                "cet intervalle, l'inégalité tangente x inférieure à un "
                "est vérifiée avant ce point : l'ensemble solution est "
                "l'intervalle ouvert moins pi demi, pi quart."
            )
        ) as tracker:
            self.play(FadeIn(ex14))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex14))

        # --- Synthèse des méthodes (6 method_box) -------------------------------
        titre_synthese = Text("Synthèse des méthodes", font_size=28, color="#A42A5A", weight="BOLD")
        titre_synthese.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Récapitulons, en six points, les méthodes essentielles de "
                "ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(titre_synthese))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre_synthese))

        syntheses = [
            ("cos x = a", r"x = \varphi + k2\pi \ \text{ou}\ x = -\varphi + k2\pi"),
            ("sin x = a", r"x = \varphi + k2\pi \ \text{ou}\ x = \pi - \varphi + k2\pi"),
            ("tan x = a", r"x = \varphi + k\pi"),
            ("a cos x + b sin x = c", r"R\cos(x-\varphi) = c,\ R=\sqrt{a^2+b^2}"),
            ("Produit nul A(x)·B(x) = 0", r"A(x)=0 \ \text{ou}\ B(x)=0 \ \text{(union)}"),
            ("Inéquation simple", r"\text{équation associée} \to \text{cercle} \to \text{lecture} \to \text{périodicité}"),
        ]
        for i, (nom, formule) in enumerate(syntheses, start=1):
            bloc = method_box(
                VGroup(
                    Text(f"{i}. {nom}", font_size=23, weight="BOLD"),
                    MathTex(formule, font_size=21),
                ).arrange(DOWN, buff=0.22),
                box_width=9,
            )
            bloc.next_to(titre, DOWN, buff=0.6)
            with self.voiceover(text=f"Méthode {i} : {nom}.") as tracker:
                self.play(FadeIn(bloc))
                self.wait(tracker.get_remaining_duration())
            self.play(FadeOut(bloc))

        # --- Pièges à éviter (7 warning_box) ------------------------------------
        titre_pieges = Text("Pièges à éviter", font_size=28, color="#595959", weight="BOLD")
        titre_pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text="Voici sept pièges classiques à éviter absolument dans ce chapitre."
        ) as tracker:
            self.play(FadeIn(titre_pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre_pieges))

        pieges = [
            "Oublier le « +k2π » (ou « +kπ » pour la tangente) et la précision « k∈ℤ » : une équation trigonométrique a une INFINITÉ de solutions.",
            "Oublier la deuxième famille de solutions pour cos x=a et sin x=a : il y en a toujours deux, sauf cas particuliers (1, -1, 0).",
            "Diviser l'angle (ex : 2x devient x) SANS diviser aussi la période (2π devient π) : erreur très fréquente.",
            "Oublier le domaine de définition de la tangente (x ≠ π/2+kπ) avant de manipuler une équation avec tan x.",
            "Confondre degrés et radians dans un calcul ou une conversion : toujours vérifier l'unité utilisée.",
            "Se tromper de signe dans les formules des angles associés (ex : cos(-x)=cos x mais cos(π-x)=-cos x).",
            "Oublier de vérifier que a appartient à [-1 ; 1] avant de résoudre cos x=a ou sin x=a (sinon : aucune solution).",
        ]
        for i, texte in enumerate(pieges, start=1):
            bloc = warning_box(
                Text(_wrap(f"{i}. {texte}", width=52), font_size=20),
                box_width=10,
            )
            bloc.next_to(titre, DOWN, buff=0.6)
            with self.voiceover(text=f"Piège numéro {i}. {texte}") as tracker:
                self.play(FadeIn(bloc))
                self.wait(tracker.get_remaining_duration())
            self.play(FadeOut(bloc))

        # --- Essentiel à retenir ----------------------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre", font_size=25, weight="BOLD"),
                Text(
                    _wrap(
                        "Le cercle trigonométrique et le radian fondent "
                        "toute la trigonométrie. cos²x+sin²x=1. Les "
                        "formules d'addition sont la clé de voûte : "
                        "duplication, linéarisation et transformations "
                        "produits/sommes s'en déduisent toutes. Les "
                        "équations cos x=a, sin x=a, tan x=a ont chacune "
                        "leur ensemble de solutions caractéristique, à "
                        "généraliser TOUJOURS avec « +k2π » ou « +kπ », "
                        "k∈ℤ. Les inéquations se résolvent par lecture sur "
                        "le cercle.",
                        width=54,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        essentiel.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, retenons l'essentiel. Le "
                "cercle trigonométrique et le radian fondent toute la "
                "trigonométrie. La relation cosinus carré x plus sinus "
                "carré x égale un est omniprésente. Les formules "
                "d'addition sont la clé de voûte du chapitre : la "
                "duplication, la linéarisation, et les transformations "
                "entre produits et sommes s'en déduisent toutes. Les "
                "équations cosinus x égale a, sinus x égale a, tangente x "
                "égale a ont chacune leur ensemble de solutions "
                "caractéristique, à généraliser toujours avec plus k deux "
                "pi ou plus k pi, k entier relatif. Enfin, les "
                "inéquations trigonométriques se résolvent par une simple "
                "lecture graphique sur le cercle trigonométrique."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
