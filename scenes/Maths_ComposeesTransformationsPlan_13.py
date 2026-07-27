"""
scenes/Maths_ComposeesTransformationsPlan_13.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 13 (synthèse finale).

§ Applications : construction (analyse-synthèse, exemple résolu 11) et
lieux géométriques (exemple résolu 12), tableau de choix de transformation,
5 méthodes de synthèse, 5 pièges classiques, tableau récapitulatif final,
essentiel à retenir.
Source : 1ereC/Maths.pdf, chapitre 8, pages 104 (et synthèse du chapitre).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


def _cell(text_str: str, font_size: int = 18, bold: bool = False):
    return Text(text_str, font_size=font_size, weight="BOLD" if bold else "NORMAL", color=WHITE)


class ApplicationsConstructionLieuxGeometriques(NotionScene):
    def construct(self):
        titre = scene_title("Constructions, lieux géométriques — synthèse")
        titre.scale(0.4)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : méthode analyse-synthèse -----------------------------------
        methode1 = method_box(
            VGroup(
                Text("Méthode : analyse-synthèse", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Analyse : supposer le problème résolu, traduire les "
                        "contraintes par une transformation, en déduire une "
                        "construction possible."
                    ),
                    font_size=21,
                ),
                Text(
                    _wrap(
                        "Synthèse : exécuter effectivement la construction "
                        "trouvée, puis vérifier qu'elle répond au problème "
                        "(discuter le nombre de solutions)."
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.22)
        )
        methode1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par les applications les plus "
                "utiles des composées : les problèmes de construction et "
                "les lieux géométriques. La méthode de référence pour "
                "toute construction est l'analyse-synthèse. En analyse, on "
                "suppose le problème résolu, et l'on traduit les "
                "contraintes de l'énoncé à l'aide d'une transformation "
                "bien choisie, ce qui suggère une construction. En "
                "synthèse, on exécute réellement cette construction, puis "
                "on vérifie qu'elle convient, en discutant, le cas "
                "échéant, du nombre de solutions."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Exemple résolu 11 : construction --------------------------------
        enonce11 = Text(
            _wrap(
                "Cercle (𝒞) de centre O, rayon r, point A extérieur au cercle. "
                "Construire une droite passant par A, recoupant (𝒞) en deux "
                "points M et N tels que N soit le milieu de [AM]."
            ),
            font_size=21,
        )
        enonce11.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu 11. Soit un cercle, de centre O et de "
                "rayon r, et un point A extérieur à ce cercle. On veut "
                "construire une droite passant par A, qui recoupe le "
                "cercle en deux points M et N, tels que N soit le milieu "
                "du segment A M."
            )
        ) as tracker:
            self.play(FadeIn(enonce11))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce11))

        analyse11 = VGroup(
            Text("Analyse", font_size=23, weight="BOLD"),
            MathTex(r"N \text{ milieu de } [AM] \iff \overrightarrow{AM}=2\overrightarrow{AN} \iff M = h_{(A,2)}(N)", font_size=22),
            Text(
                _wrap("N décrit (𝒞), donc M décrit (𝒞') = image de (𝒞) par h(A,2) : centre O'=h(A,2)(O), rayon 2r."),
                font_size=20,
            ),
            MathTex(r"\text{Or } M\in(\mathcal{C}) \implies M \in (\mathcal{C})\cap(\mathcal{C}')", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.2)
        analyse11.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Analysons. Dire que N est le milieu de A M revient à dire "
                "que le vecteur A-M est le double du vecteur A-N, "
                "c'est-à-dire que M est l'image de N par l'homothétie de "
                "centre A et de rapport 2. Comme N décrit le cercle "
                "initial, M décrit le cercle image de ce cercle par cette "
                "homothétie : un cercle de centre O prime, image de O, et "
                "de rayon 2 r. Or M doit aussi appartenir au cercle "
                "initial : M est donc à l'intersection des deux cercles."
            )
        ) as tracker:
            self.play(FadeIn(analyse11))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(analyse11))

        synthese11 = VGroup(
            Text("Synthèse & construction", font_size=23, weight="BOLD"),
            Text(_wrap("1) Construire (𝒞') = image de (𝒞) par h(A,2). 2) Placer M à l'intersection de (𝒞) et (𝒞'). 3) N = milieu de [AM]. La droite (AM) convient."), font_size=20),
            Text(_wrap("Discussion : le nombre de solutions (0, 1 ou 2) dépend de la position relative de (𝒞) et (𝒞'), donc de la distance AO."), font_size=20),
        ).arrange(DOWN, buff=0.22)
        synthese11.next_to(titre, DOWN, buff=0.35)

        o_pt = LEFT * 1.5
        a_pt = RIGHT * 2.5
        cercle_c = Circle(radius=1.3, color="#1E5FA8").move_to(o_pt)
        o_prime = a_pt + 2 * (o_pt - a_pt)
        cercle_c2 = Circle(radius=2.6, color="#74458C").move_to(o_prime)
        pt_o = _dot_label(o_pt, "O", dot_color="#288073", label_dir=DOWN)
        pt_a = _dot_label(a_pt, "A", label_dir=DOWN)
        figure11 = VGroup(cercle_c, cercle_c2, pt_o, pt_a)
        figure11.scale(0.55)
        figure11.next_to(synthese11, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "La construction se déroule donc en trois temps : on "
                "construit le cercle image par l'homothétie de centre A et "
                "de rapport 2, on place M à l'intersection des deux "
                "cercles, puis N comme milieu de A M. Le nombre de "
                "solutions, zéro, une ou deux, dépend de la position "
                "relative des deux cercles, donc de la distance entre A et "
                "O."
            )
        ) as tracker:
            self.play(FadeIn(synthese11))
            self.play(Create(figure11))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(synthese11), FadeOut(figure11))

        # --- Méthode : lieu géométrique -----------------------------------------
        methode2 = method_box(
            Text(
                _wrap(
                    "Méthode — lieu géométrique : identifier la transformation "
                    "qui relie le point variable au point cherché ; le lieu "
                    "cherché est alors l'image, par cette transformation, du "
                    "lieu décrit par le point variable."
                ),
                font_size=21,
            )
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour un lieu géométrique, la méthode est similaire : on "
                "identifie la transformation qui relie le point variable "
                "au point dont on cherche le lieu. Le lieu cherché est "
                "alors simplement l'image, par cette transformation, du "
                "lieu déjà connu du point variable."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Exemple résolu 12 : lieu géométrique -------------------------------
        enonce12 = Text(
            _wrap(
                "A, B fixes. M décrit le cercle de diamètre [AB] (triangle AMB "
                "rectangle en M, théorème de Thalès). G = centre de gravité de "
                "AMB. Quel est le lieu de G ?"
            ),
            font_size=21,
        )
        enonce12.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu 12. A et B sont fixes, et M décrit le "
                "cercle de diamètre A B — d'après le théorème de Thalès, "
                "cela équivaut à dire que le triangle A M B est rectangle "
                "en M. Soit G le centre de gravité de ce triangle. Quel "
                "est le lieu décrit par G ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce12))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce12))

        calc12 = VGroup(
            MathTex(r"G = \dfrac{A+M+B}{3} = \dfrac{A+B}{2} + \dfrac{1}{3}\left(M - \dfrac{A+B}{2}\right)", font_size=22),
            MathTex(r"\implies G = h_{(K,\,1/3)}(M), \quad K = \text{milieu}[AB]", font_size=25, color=YELLOW),
            Text(_wrap("M décrit le cercle de centre K, rayon AB/2 ⟹ G décrit le cercle de centre K, rayon AB/6."), font_size=20),
        ).arrange(DOWN, buff=0.25)
        calc12.next_to(titre, DOWN, buff=0.4)

        k_pt = LEFT * 0.5
        cercle_grand = Circle(radius=1.8, color="#1E5FA8").move_to(k_pt)
        cercle_petit = Circle(radius=0.6, color="#DE7C1F").move_to(k_pt)
        pt_k = _dot_label(k_pt, "K", dot_color="#288073", label_dir=DOWN)
        figure12 = VGroup(cercle_grand, cercle_petit, pt_k)
        figure12.scale(0.6)
        figure12.next_to(calc12, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Le centre de gravité G s'écrit A plus M plus B, le tout "
                "divisé par 3, ce qui se réarrange en K plus un tiers de M "
                "moins K, où K est le milieu de A B. Autrement dit, G est "
                "l'image de M par l'homothétie de centre K et de rapport "
                "un tiers. Comme M décrit le cercle de centre K et de "
                "rayon A B sur 2, G décrit son image par cette homothétie "
                ": un cercle concentrique, de rayon trois fois plus petit, "
                "A B sur 6."
            )
        ) as tracker:
            self.play(FadeIn(calc12))
            self.play(Create(figure12))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc12), FadeOut(figure12))

        # --- Tableau : choisir la bonne transformation ---------------------------
        headers = [_cell("Configuration", bold=True), _cell("Transformation", bold=True)]
        rows = [
            ("Vecteur constant MM'⃗", "Translation"),
            ("Point milieu fixe", "Symétrie centrale"),
            ("Médiatrice fixe", "Symétrie axiale"),
            ("Angle et distance au centre fixes", "Rotation"),
            ("Alignement, rapport constant", "Homothétie"),
        ]
        cells = list(headers)
        for a, b in rows:
            cells.append(_cell(a, font_size=17))
            cells.append(_cell(b, font_size=17))
        tableau_choix = VGroup(*cells).arrange_in_grid(rows=6, cols=2, buff=(0.5, 0.18), col_alignments="lc")
        tableau_choix.scale(0.85)
        tableau_choix.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour choisir rapidement la bonne transformation face à une "
                "configuration donnée, voici un tableau-guide. Un vecteur "
                "constant entre un point et son image évoque une "
                "translation. Un point milieu fixe évoque une symétrie "
                "centrale. Une médiatrice fixe évoque une symétrie axiale. "
                "Un angle et une distance au centre conservés évoquent une "
                "rotation. Et un alignement avec un rapport de distance "
                "constant évoque une homothétie."
            )
        ) as tracker:
            self.play(FadeIn(tableau_choix))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_choix))

        # --- 5 méthodes de synthèse -----------------------------------------
        methodes_titre = Text("Cinq méthodes de synthèse", font_size=26, weight="BOLD")
        methodes_titre.next_to(titre, DOWN, buff=0.35)
        with self.voiceover(text="Récapitulons cinq méthodes de synthèse indispensables pour ce chapitre.") as tracker:
            self.play(FadeIn(methodes_titre))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(methodes_titre))

        m1 = method_box(
            Text(_wrap("1) Nature d'une composée : 3 outils — parité déplacement/antidéplacement, calcul analytique (x',y'), théorème adapté au cas (mêmes/centres distincts, axes //ou sécants...)."), font_size=20)
        )
        m1.next_to(titre, DOWN, buff=0.4)
        with self.voiceover(
            text=(
                "Un : pour déterminer la nature d'une composée, trois "
                "outils se combinent : la règle de parité déplacement "
                "antidéplacement, le calcul analytique direct de x prime "
                "et y prime, et le théorème adapté à la configuration "
                "précise rencontrée."
            )
        ) as tracker:
            self.play(FadeIn(m1))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(m1))

        m2 = method_box(
            Text(_wrap("2) Éléments caractéristiques géométriquement : chercher les points invariants, calculer l'image de 2 points, mesurer angles et rapports de distances."), font_size=20)
        )
        m2.next_to(titre, DOWN, buff=0.4)
        with self.voiceover(
            text=(
                "Deux : pour trouver les éléments caractéristiques par la "
                "géométrie, on cherche les points invariants, on calcule "
                "l'image de deux points bien choisis, et l'on mesure les "
                "angles et les rapports de distances obtenus."
            )
        ) as tracker:
            self.play(FadeIn(m2))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(m2))

        m3 = method_box(
            Text(_wrap("3) Reconnaître une expression analytique : x'=x+a,y'=y+b (translation) ; x'=2a−x,y'=y (sym. axiale/centrale) ; x'−a=k(x−a) (homothétie) ; termes en cos/sin (rotation)."), font_size=19)
        )
        m3.next_to(titre, DOWN, buff=0.4)
        with self.voiceover(
            text=(
                "Trois : pour reconnaître une expression analytique, on "
                "repère sa forme — x prime égale x plus a signale une "
                "translation, une formule du type 2a moins x signale une "
                "symétrie, une forme proportionnelle à x moins a signale "
                "une homothétie, et la présence de cosinus et sinus "
                "signale une rotation."
            )
        ) as tracker:
            self.play(FadeIn(m3))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(m3))

        m4 = method_box(
            Text(_wrap("4) Problème de construction en 3 temps : analyse (traduire par une transformation), construction (exécuter), synthèse (vérifier, discuter le nombre de solutions)."), font_size=20)
        )
        m4.next_to(titre, DOWN, buff=0.4)
        with self.voiceover(
            text=(
                "Quatre : tout problème de construction se traite en trois "
                "temps — l'analyse, qui traduit les contraintes par une "
                "transformation, la construction elle-même, puis la "
                "synthèse, qui vérifie et discute le nombre de solutions."
            )
        ) as tracker:
            self.play(FadeIn(m4))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(m4))

        m5 = method_box(
            Text(_wrap("5) Lieu géométrique : relier le point cherché au point variable par une transformation, puis appliquer cette transformation au lieu connu du point variable."), font_size=20)
        )
        m5.next_to(titre, DOWN, buff=0.4)
        with self.voiceover(
            text=(
                "Cinq : pour un lieu géométrique, on relie le point "
                "cherché au point variable par une transformation "
                "explicite, puis on applique cette transformation au lieu "
                "déjà connu du point variable."
            )
        ) as tracker:
            self.play(FadeIn(m5))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(m5))

        # --- 5 pièges à éviter ------------------------------------------------
        pieges_titre = Text("Cinq pièges classiques", font_size=26, weight="BOLD")
        pieges_titre.next_to(titre, DOWN, buff=0.35)
        with self.voiceover(text="Passons en revue cinq pièges classiques de ce chapitre.") as tracker:
            self.play(FadeIn(pieges_titre))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(pieges_titre))

        p1 = warning_box(MathTex(r"1)\ \ g\circ f \text{ applique } f \text{ en premier, jamais } g", font_size=24))
        p1.next_to(titre, DOWN, buff=0.45)
        with self.voiceover(text="Un : g∘f applique toujours f en premier, jamais g — c'est le piège le plus fréquent du chapitre.") as tracker:
            self.play(FadeIn(p1))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(p1))

        p2 = warning_box(
            Text(_wrap("2) L'angle de sΔ'∘sΔ est le double de l'angle ORIENTÉ du premier axe vers le second, pas l'angle géométrique non orienté."), font_size=21)
        )
        p2.next_to(titre, DOWN, buff=0.45)
        with self.voiceover(text="Deux : l'angle de la composée de deux symétries axiales est le double de l'angle orienté du premier axe vers le second, jamais l'angle géométrique non orienté.") as tracker:
            self.play(FadeIn(p2))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(p2))

        p3 = warning_box(
            Text(_wrap("3) Homothéties de centres distincts avec k'k=1 : le résultat est une TRANSLATION, pas une homothétie — chercher un centre serait vain."), font_size=21)
        )
        p3.next_to(titre, DOWN, buff=0.45)
        with self.voiceover(text="Trois : pour deux homothéties de centres distincts dont le produit des rapports vaut 1, le résultat est une translation, pas une homothétie — chercher un centre serait vain.") as tracker:
            self.play(FadeIn(p3))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(p3))

        p4 = warning_box(
            Text(_wrap("4) Le centre d'une composée d'homothéties de centres distincts n'est en général NI O NI O' : il doit être calculé."), font_size=21)
        )
        p4.next_to(titre, DOWN, buff=0.45)
        with self.voiceover(text="Quatre : le centre d'une composée d'homothéties de centres distincts n'est en général ni l'un ni l'autre des deux centres de départ.") as tracker:
            self.play(FadeIn(p4))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(p4))

        p5 = warning_box(
            Text(_wrap("5) Démontrer une translation exige un vecteur MM'⃗ CONSTANT — conserver les distances prouve seulement une isométrie, pas une translation."), font_size=21)
        )
        p5.next_to(titre, DOWN, buff=0.45)
        with self.voiceover(text="Cinq : pour démontrer qu'une transformation est une translation, il faut établir qu'un vecteur MM' est constant — la seule conservation des distances ne prouve qu'une isométrie, pas une translation.") as tracker:
            self.play(FadeIn(p5))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(p5))

        # --- Tableau récapitulatif final -----------------------------------------
        headers_f = [_cell("Composée", bold=True), _cell("Résultat", bold=True)]
        rows_f = [
            ("t_v∘t_u", "translation (u+v)"),
            ("sO'∘sO", "translation (2OO')"),
            ("sΔ'∘sΔ (// )", "translation"),
            ("sΔ'∘sΔ (sécants)", "rotation (angle double)"),
            ("r∘r (même centre)", "rotation (somme angles)"),
            ("r'∘r (somme≠0)", "rotation"),
            ("r'∘r (somme≡0)", "translation"),
            ("h'∘h (même centre)", "homothétie (k'k)"),
            ("h'∘h (centres≠, k'k≠1)", "homothétie"),
            ("h'∘h (centres≠, k'k=1)", "translation"),
            ("t∘h", "homothétie (rapport k)"),
        ]
        cells_f = list(headers_f)
        for a, b in rows_f:
            cells_f.append(_cell(a, font_size=15))
            cells_f.append(_cell(b, font_size=15))
        tableau_final = VGroup(*cells_f).arrange_in_grid(rows=12, cols=2, buff=(0.45, 0.12), col_alignments="lc")
        tableau_final.scale(0.72)
        tableau_final.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici, pour finir, le tableau récapitulatif de toutes les "
                "composées étudiées dans ce chapitre : de la simple somme "
                "de vecteurs pour deux translations, jusqu'aux cas les "
                "plus riches d'homothéties de centres distincts."
            )
        ) as tracker:
            self.play(FadeIn(tableau_final))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_final))

        # --- Essentiel à retenir -------------------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel à retenir", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "g∘f applique f en premier. Isométries : la parité "
                        "déplacement/antidéplacement prédit la nature du résultat."
                    ),
                    font_size=20,
                ),
                Text(
                    _wrap(
                        "2 translations → translation. 2 symétries centrales ou "
                        "axiales // → translation. 2 symétries axiales sécantes → "
                        "rotation d'angle double."
                    ),
                    font_size=20,
                ),
                Text(
                    _wrap(
                        "Homothéties de même centre → homothétie (rapport produit). "
                        "Centres distincts : homothétie si k'k≠1 (centre à calculer), "
                        "translation si k'k=1."
                    ),
                    font_size=20,
                ),
                Text(_wrap("Toute construction : analyse (transformation) → synthèse (vérification, discussion)."), font_size=20),
            ).arrange(DOWN, buff=0.2)
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre : g∘f applique toujours f en "
                "premier, et la règle de parité entre déplacements et "
                "antidéplacements permet d'anticiper la nature de toute "
                "composée. Deux translations donnent une translation ; "
                "deux symétries centrales, ou deux symétries axiales "
                "d'axes parallèles, donnent une translation ; deux "
                "symétries axiales d'axes sécants donnent une rotation "
                "d'angle double. Pour les homothéties de même centre, le "
                "rapport se multiplie ; pour des centres distincts, on "
                "obtient une homothétie si le produit des rapports diffère "
                "de 1, avec un centre à calculer, et une translation "
                "sinon. Enfin, pour toute construction, la méthode "
                "analyse-synthèse, appuyée sur ces théorèmes, reste "
                "l'outil de référence."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
