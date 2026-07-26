"""
scenes/Maths_EquationsInequationsSecondDegre_10.py — Chapitre 1 (1ereC,
Maths), scène 10 (dernière scène du chapitre).

Problèmes de mise en équation (méthode en 4 étapes, deux exemples dont un
problème d'optimisation), remarque minimum/maximum, trois méthodes-clés du
chapitre à retenir, cinq pièges classiques, et la boîte « L'essentiel à
retenir » qui récapitule tout le chapitre.
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


class ProblemesMiseEnEquationEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("Problèmes de mise en équation — l'essentiel")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : méthode en 4 étapes -----------------------------------------
        methode = VGroup(
            Text("1. Choisir l'inconnue (et préciser son domaine).", font_size=24),
            Text("2. Traduire l'énoncé par une équation ou une inéquation.", font_size=24),
            Text("3. Résoudre l'équation ou l'inéquation obtenue.", font_size=24),
            Text("4. Contrôler : la solution a-t-elle un sens dans le problème ?", font_size=24),
        ).arrange(DOWN, buff=0.28)
        methode_box = method_box(methode, box_width=12.0)
        methode_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour résoudre un problème concret à l'aide d'une équation "
                "du second degré, on suit toujours la même méthode en "
                "quatre étapes. D'abord, choisir l'inconnue, en précisant "
                "son domaine de validité. Ensuite, traduire l'énoncé par "
                "une équation, ou une inéquation. Puis résoudre "
                "cette équation. Enfin, contrôler que chaque solution "
                "trouvée a bien un sens concret dans le problème posé — un "
                "âge ou une longueur, par exemple, ne peut pas être "
                "négatif."
            )
        ) as tracker:
            self.play(FadeIn(methode_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_box))

        # --- Exemple traité 18 : entiers consécutifs -------------------------------
        ex18_enonce = Text(
            "Trouver deux entiers naturels consécutifs dont le produit vaut 552.",
            font_size=24,
        )
        ex18_mise_eq = MathTex(r"n(n+1) = 552 \;\Longleftrightarrow\; n^2+n-552=0", font_size=28)
        ex18_calc = MathTex(r"\Delta = 1+2208=2209=47^2", font_size=27)
        ex18_racines = MathTex(
            r"n=\dfrac{-1-47}{2}=-24 \qquad n=\dfrac{-1+47}{2}=23",
            font_size=27,
        )
        ex18_concl = MathTex(
            r"n \ge 0 \;\Rightarrow\; n=23 \;\Rightarrow\; \text{les entiers sont } 23 \text{ et } 24",
            font_size=27,
        )
        ex18 = VGroup(ex18_enonce, ex18_mise_eq, ex18_calc, ex18_racines, ex18_concl).arrange(
            DOWN, buff=0.25
        )
        ex18_box = example_box(ex18, box_width=12.2)
        ex18_box.scale(0.9)
        ex18_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : trouver deux entiers naturels consécutifs dont "
                "le produit vaut cinq cent cinquante-deux. En notant n le "
                "plus petit, n fois n plus un égale cinq cent "
                "cinquante-deux, soit n carré plus n moins cinq cent "
                "cinquante-deux égale zéro. Le discriminant vaut deux mille "
                "deux cent neuf, le carré de quarante-sept. On trouve n "
                "égale moins vingt-quatre, rejetée car n doit être positif, "
                "et n égale vingt-trois. Les deux entiers cherchés sont "
                "donc vingt-trois et vingt-quatre."
            )
        ) as tracker:
            self.play(FadeIn(ex18_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex18_box))

        # --- Exemple traité 19 : optimisation ---------------------------------------
        ex19_enonce = Text(
            "ABCD carré de côté 2. M sur [AB], AM = x (0 < x < 2).\n"
            "AEFM et MGHB sont deux carrés. Minimiser la somme des aires.",
            font_size=22,
        )
        ex19_fonction = MathTex(r"S(x) = x^2 + (2-x)^2", font_size=30)
        ex19_dev = MathTex(
            r"S(x) = x^2+4-4x+x^2 = 2x^2-4x+4 = 2(x-1)^2+2",
            font_size=27,
        )
        ex19_concl = MathTex(
            r"S(x) \ge 2, \text{ minimum atteint en } x=1, \quad S(1)=2\text{ m}^2",
            font_size=27,
        )
        ex19 = VGroup(ex19_enonce, ex19_fonction, ex19_dev, ex19_concl).arrange(DOWN, buff=0.28)
        ex19_box = example_box(ex19, box_width=12.3)
        ex19_box.scale(0.88)
        ex19_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple d'optimisation : ABCD est un carré de côté deux "
                "mètres, M un point de côté A B tel que A M égale x, avec "
                "x compris entre zéro et deux. On construit deux carrés, A "
                "E F M et M G H B, de côtés respectifs x et deux moins x. "
                "La somme de leurs aires vaut S de x égale x carré plus "
                "deux moins x, le tout au carré. En développant et en "
                "utilisant la forme canonique, on obtient deux fois le "
                "carré de x moins un, plus deux : cette somme est minimale "
                "quand x égale un, et vaut alors deux mètres carrés."
            )
        ) as tracker:
            self.play(FadeIn(ex19_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex19_box))

        # --- Remarque : minimum / maximum -------------------------------------------
        remarque_minmax = MathTex(
            r"a>0 \;\Rightarrow\; \text{le trinôme admet un } \textbf{minimum}"
            r" \text{ (parabole vers le haut)} \\[4pt]"
            r"a<0 \;\Rightarrow\; \text{le trinôme admet un } \textbf{maximum}"
            r" \text{ (parabole vers le bas)}",
            font_size=26,
        )
        remarque_box = warning_box(remarque_minmax, box_width=12.0)
        remarque_box.scale(0.92)
        remarque_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Remarque importante : si a est strictement positif, la "
                "parabole est tournée vers le haut, et le trinôme admet un "
                "minimum, atteint au sommet. Si a est strictement négatif, "
                "la parabole est tournée vers le bas, et le trinôme admet "
                "un maximum."
            )
        ) as tracker:
            self.play(FadeIn(remarque_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_box))

        # --- Trois méthodes-clés à retenir -------------------------------------------
        methodes_cles = VGroup(
            Text("1. Toujours chercher un facteur commun ou une identité", font_size=23),
            Text("   remarquable avant de calculer Δ.", font_size=23),
            Text("2. Réflexe racine évidente (0, 1, −1, 2, −2 ;", font_size=23),
            Text("   a+b+c=0 ⟹ 1 racine) avant de foncer sur Δ.", font_size=23),
            Text("3. Utiliser le discriminant réduit Δ′ dès que b = 2b′.", font_size=23),
        ).arrange(DOWN, buff=0.22)
        methodes_box = method_box(methodes_cles, box_width=12.0)
        methodes_box.scale(0.92)
        methodes_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Trois méthodes-clés à garder en tête pour tout le "
                "chapitre. Un : toujours chercher un facteur commun ou une "
                "identité remarquable avant de calculer delta. Deux : "
                "avoir le réflexe de la racine évidente — zéro, un, moins "
                "un, deux, moins deux, ou la somme des coefficients nulle "
                "— avant de foncer sur le calcul de delta. Trois : "
                "utiliser le discriminant réduit delta prime dès que b "
                "s'écrit deux b prime, pour alléger les calculs."
            )
        ) as tracker:
            self.play(FadeIn(methodes_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methodes_box))

        # --- Cinq pièges classiques ---------------------------------------------------
        pieges = VGroup(
            Text("1. Le coefficient de x² peut s'annuler avec un paramètre :", font_size=21),
            Text("   toujours vérifier a ≠ 0.", font_size=21),
            Text("2. Signe du trinôme : ne pas confondre « à l'extérieur »", font_size=21),
            Text("   et « entre » les racines (dépend du signe de a).", font_size=21),
            Text("3. Élever au carré peut créer des solutions parasites :", font_size=21),
            Text("   toujours vérifier.", font_size=21),
            Text("4. Une inéquation se conclut par un intervalle, jamais", font_size=21),
            Text("   par une simple liste de valeurs.", font_size=21),
            Text("5. Équation bicarrée : ne pas oublier le cas X = 0.", font_size=21),
        ).arrange(DOWN, buff=0.16)
        pieges_box = warning_box(pieges, box_width=12.3)
        pieges_box.scale(0.92)
        pieges_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Cinq pièges à éviter absolument sur tout ce chapitre. "
                "Premier piège : le coefficient de x carré peut s'annuler "
                "pour une valeur particulière d'un paramètre — toujours "
                "vérifier que a est différent de zéro. Deuxième piège : ne "
                "pas confondre le signe du trinôme à l'extérieur des "
                "racines, et entre les racines, cela dépend du signe de a. "
                "Troisième piège : élever au carré dans une équation "
                "irrationnelle peut créer des solutions parasites — "
                "toujours vérifier. Quatrième piège : une inéquation se "
                "conclut par un intervalle, jamais par une simple liste de "
                "valeurs. Cinquième piège : dans une équation bicarrée, ne "
                "pas oublier le cas où X est égal à zéro."
            )
        ) as tracker:
            self.play(FadeIn(pieges_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges_box))

        # --- L'essentiel à retenir : récapitulatif du chapitre -----------------------
        essentiel = VGroup(
            MathTex(
                r"ax^2+bx+c = a\left[\left(x+\frac{b}{2a}\right)^2-\frac{\Delta}{4a^2}\right]"
                r"\qquad \Delta=b^2-4ac",
                font_size=25,
            ),
            MathTex(
                r"\Delta<0 : S=\varnothing \quad\;"
                r"\Delta=0 : x_0=-\frac{b}{2a} \quad\;"
                r"\Delta>0 : x_{1,2}=\frac{-b\pm\sqrt{\Delta}}{2a}",
                font_size=23,
            ),
            MathTex(
                r"\text{Signe du trinôme : signe de } a \text{ à l'extérieur des racines,"
                r" signe de } {-a} \text{ entre elles}",
                font_size=21,
            ),
            Text(
                "Méthode générale : choisir l'inconnue, calculer Δ (ou Δ′), "
                "résoudre, contrôler la cohérence de la solution.",
                font_size=21,
            ),
        ).arrange(DOWN, buff=0.28)
        essentiel_box_ = essentiel_box(essentiel, box_width=12.5)
        essentiel_box_.scale(0.85)
        essentiel_box_.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, l'essentiel à retenir. La "
                "forme canonique du trinôme, construite à partir du "
                "discriminant delta égal à b carré moins quatre a c. Les "
                "trois cas de résolution de l'équation selon le signe de "
                "delta : aucune solution, une racine double, ou deux "
                "racines distinctes. Le signe du trinôme, qui est celui de "
                "a à l'extérieur des racines, et l'opposé du signe de a "
                "entre elles. Et enfin, la méthode générale valable pour "
                "tout problème du second degré : choisir l'inconnue, "
                "calculer le discriminant, résoudre, puis toujours "
                "contrôler que la solution a un sens."
            )
        ) as tracker:
            self.play(FadeIn(essentiel_box_))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel_box_))
