"""
scenes/Maths_LimitesContinuite_12.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 12 (clôture du chapitre).

Théorème des valeurs intermédiaires (admis) avec figure, corollaire
d'existence de solution (f(a)×f(b)<0) et corollaire avec unicité (stricte
monotonie). Exemples résolus 17 (x³+x-3=0 dans ]1;2[, encadrement à 10⁻¹
près) et 18 (cos x = x, solution unique dans [0;π/2]). Trois méthodes
(conduite d'un calcul de limite, étudier la continuité d'une fonction par
morceaux, montrer qu'une équation admet une solution) et cinq pièges à
éviter. Essentiel à retenir du chapitre.
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, theorem_box, warning_box


def _bissection(f, a, b, iterations=60):
    for _ in range(iterations):
        m = (a + b) / 2
        if (f(a) - 0) * (f(m) - 0) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2


class TheoremeValeursIntermediaires(NotionScene):
    def construct(self):
        titre = scene_title("Théorème des valeurs intermédiaires")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : TVI (admis) -------------------------------------------------
        theo_tvi = theorem_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Si } f \text{ est continue sur } [a\,;b],\\
                \text{alors pour tout réel } k \text{ compris entre } f(a) \text{ et } f(b),\\
                \text{il existe (au moins) un réel } c\in[a\,;b] \text{ tel que } f(c)=k.
                \end{array}
                """,
                font_size=25,
            ),
            box_width=11.0,
        )
        theo_tvi.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Théorème des valeurs intermédiaires, admis : si f est "
                "continue sur l'intervalle fermé a, b, alors pour tout réel "
                "k compris entre f de a et f de b, il existe au moins un "
                "réel c dans a, b tel que f de c égale k. Autrement dit, la "
                "courbe d'une fonction continue prend toutes les valeurs "
                "intermédiaires entre f de a et f de b."
            )
        ) as tracker:
            self.play(FadeIn(theo_tvi))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_tvi))

        # --- Figure illustrant le TVI ---------------------------------------------
        func = lambda x: 0.2 * x**2 - 0.3 * x + 0.5
        a_val, b_val, k_val = 0.5, 4.5, 2.0
        c_val = _bissection(lambda x: func(x) - k_val, a_val, b_val)

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 4, 1],
            x_length=6.5,
            y_length=3.5,
            axis_config={"color": WHITE, "font_size": 18},
        )
        courbe = axes.plot(func, x_range=[a_val, b_val], color=YELLOW)
        ligne_k = DashedLine(axes.c2p(0, k_val), axes.c2p(c_val, k_val), color="#288073")
        ligne_c = DashedLine(axes.c2p(c_val, 0), axes.c2p(c_val, k_val), color="#288073")
        pt_c = Dot(axes.c2p(c_val, k_val), color="#288073", radius=0.07)
        pt_a = Dot(axes.c2p(a_val, func(a_val)), color=WHITE, radius=0.06)
        pt_b = Dot(axes.c2p(b_val, func(b_val)), color=WHITE, radius=0.06)
        labels = VGroup(
            MathTex("a", font_size=20).next_to(axes.c2p(a_val, 0), DOWN, buff=0.1),
            MathTex("b", font_size=20).next_to(axes.c2p(b_val, 0), DOWN, buff=0.1),
            MathTex("c", font_size=20, color="#288073").next_to(axes.c2p(c_val, 0), DOWN, buff=0.1),
            MathTex("k", font_size=20, color="#288073").next_to(axes.c2p(0, k_val), LEFT, buff=0.1),
        )
        figure = VGroup(axes, courbe, ligne_k, ligne_c, pt_c, pt_a, pt_b, labels)
        figure.scale(0.85)
        figure.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Visuellement : la courbe de f, continue sur a, b, relie le "
                "point de hauteur f de a au point de hauteur f de b sans "
                "aucun saut. Pour toute hauteur k intermédiaire entre les "
                "deux, la courbe croise nécessairement la droite "
                "horizontale y égale k, en au moins un point d'abscisse c."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- Corollaires -----------------------------------------------------
        coro1 = theorem_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Si } f \text{ continue sur } [a\,;b] \text{ et } f(a)\times f(b) < 0,\\
                \text{alors l'équation } f(x)=0 \text{ admet au moins une solution dans } ]a\,;b[.
                \end{array}
                """,
                font_size=24,
            ),
            box_width=11.0,
        )
        coro1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premier corollaire, cas particulier avec k égale zéro : si "
                "f est continue sur a, b et que f de a fois f de b est "
                "strictement négatif — c'est-à-dire que f de a et f de b "
                "sont de signes contraires — alors l'équation f de x égale "
                "zéro admet au moins une solution dans l'intervalle ouvert "
                "a, b."
            )
        ) as tracker:
            self.play(FadeIn(coro1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coro1))

        coro2 = theorem_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Si, en plus, } f \text{ est strictement monotone sur } [a\,;b],\\
                \text{alors cette solution est UNIQUE dans } ]a\,;b[.
                \end{array}
                """,
                font_size=25,
            ),
            box_width=10.5,
        )
        coro2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deuxième corollaire, avec unicité : si, en plus d'être "
                "continue, f est strictement monotone sur a, b — "
                "strictement croissante ou strictement décroissante — "
                "alors cette solution est unique dans l'intervalle ouvert "
                "a, b."
            )
        ) as tracker:
            self.play(FadeIn(coro2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coro2))

        # --- Exemple 17 : x³+x-3=0 dans ]1;2[ --------------------------------------
        ex17_titre = Text(
            "Exemple 17 — x³+x-3=0 admet une unique solution dans ]1;2[ :",
            font_size=19,
            color=YELLOW,
            weight="BOLD",
        )
        ex17_titre.next_to(titre, DOWN, buff=0.35)
        ex17_calc = MathTex(
            r"""
            \begin{array}{l}
            g(x)=x^3+x-3 \text{ est un polynôme : continue et strictement croissante sur } \mathbb{R}\\
            g(1) = 1+1-3=-1 <0, \qquad g(2)=8+2-3=7>0 \ \Longrightarrow\ g(1)\times g(2)<0\\
            \Longrightarrow\ \exists!\, c\in\, ]1\,;2[ \ /\ g(c)=0\\[6pt]
            g(1.2)\approx -0.07 <0,\ g(1.3)\approx 0.50>0
            \ \Longrightarrow\ c\in\, ]1.2\,;1.3[ \ \text{(à } 10^{-1} \text{ près)}
            \end{array}
            """,
            font_size=20,
        )
        ex17_calc.next_to(ex17_titre, DOWN, buff=0.3)
        ex17_box = example_box(ex17_calc, box_width=11.8)
        ex17_box.next_to(ex17_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : montrons que x cube plus x moins trois égale "
                "zéro admet une unique solution dans l'intervalle un, deux. "
                "Posons g de x égale x cube plus x moins trois, un "
                "polynôme, donc continu et strictement croissant sur ℝ. On "
                "calcule g de un, qui vaut moins un, et g de deux, qui vaut "
                "sept : leur produit est négatif, donc il existe une unique "
                "solution c dans l'intervalle ouvert un, deux. En "
                "resserrant l'encadrement, on trouve c entre un virgule "
                "deux et un virgule trois, à dix puissance moins un près."
            )
        ) as tracker:
            self.play(FadeIn(ex17_titre))
            self.play(FadeIn(ex17_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex17_titre), FadeOut(ex17_box))

        # --- Exemple 18 : cos x = x, solution unique dans [0;π/2] -----------------
        ex18_titre = Text(
            "Exemple 18 — cos x = x admet une unique solution dans [0;π/2] :",
            font_size=18,
            color=YELLOW,
            weight="BOLD",
        )
        ex18_titre.next_to(titre, DOWN, buff=0.35)
        ex18_calc = MathTex(
            r"""
            \begin{array}{l}
            h(x)=\cos x - x \text{ : continue et strictement décroissante sur } \left[0\,;\dfrac{\pi}{2}\right]\\
            h(0)=\cos 0 - 0 = 1>0, \qquad h\!\left(\dfrac{\pi}{2}\right) = 0-\dfrac{\pi}{2}<0
            \ \Longrightarrow\ h(0)\times h\!\left(\dfrac{\pi}{2}\right)<0\\
            \Longrightarrow\ \exists!\, c\in\left]0\,;\dfrac{\pi}{2}\right[ \ /\ h(c)=0
            \ \text{c'est-à-dire } \cos c = c
            \end{array}
            """,
            font_size=21,
        )
        ex18_calc.next_to(ex18_titre, DOWN, buff=0.3)
        ex18_box = example_box(ex18_calc, box_width=11.5)
        ex18_box.next_to(ex18_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Deuxième exemple : l'équation cosinus de x égale x admet "
                "une unique solution dans zéro, pi sur deux. On pose h de x "
                "égale cosinus de x moins x, continue et strictement "
                "décroissante sur cet intervalle. h de zéro vaut un, "
                "positif ; h de pi sur deux vaut moins pi sur deux, "
                "négatif : leur produit est négatif, donc il existe une "
                "unique solution c telle que cosinus de c égale c."
            )
        ) as tracker:
            self.play(FadeIn(ex18_titre))
            self.play(FadeIn(ex18_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex18_titre), FadeOut(ex18_box))

        # --- Trois méthodes ---------------------------------------------------
        methode1 = method_box(
            Text(
                "Calculer une limite : repérer la F.I. éventuelle (0/0, ∞/∞, "
                "0×∞, ∞-∞), puis choisir factorisation, expression "
                "conjuguée, taux d'accroissement ou encadrement.",
                font_size=21,
            ),
            box_width=11.5,
        )
        methode1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Récapitulons trois méthodes de rédaction. D'abord, pour "
                "calculer une limite : repérer s'il y a une forme "
                "indéterminée, puis choisir l'outil adapté — factorisation "
                "par le terme dominant, expression conjuguée, taux "
                "d'accroissement, ou encadrement pour les gendarmes."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            Text(
                "Étudier la continuité d'une fonction par morceaux en x0 : "
                "calculer f(x0), la limite à gauche et la limite à droite "
                "en x0, puis comparer les trois valeurs.",
                font_size=21,
            ),
            box_width=11.5,
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ensuite, pour étudier la continuité d'une fonction définie "
                "par morceaux en un point x zéro : on calcule f de x zéro, "
                "la limite à gauche, et la limite à droite, puis on compare "
                "les trois valeurs obtenues."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            Text(
                "Montrer qu'une équation f(x)=0 admet une solution : vérifier "
                "que f est continue sur [a;b], calculer f(a) et f(b), et "
                "vérifier que f(a)×f(b)<0 (ajouter la stricte monotonie "
                "pour l'unicité).",
                font_size=21,
            ),
            box_width=11.8,
        )
        methode3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Enfin, pour montrer qu'une équation f de x égale zéro "
                "admet une solution : vérifier que f est continue sur a, "
                "b, calculer f de a et f de b, puis vérifier que leur "
                "produit est strictement négatif — et ajouter la stricte "
                "monotonie si l'on veut conclure à l'unicité."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Cinq pièges à éviter -----------------------------------------------
        pieges_titre = Text("Cinq pièges classiques à éviter :", font_size=25, color=YELLOW, weight="BOLD")
        pieges_titre.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour terminer, cinq pièges classiques à éviter absolument "
                "sur ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(pieges_titre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges_titre))

        piege1 = warning_box(
            Text("1/0 n'est PAS une forme indéterminée : c'est +∞, -∞, ou pas de limite (selon le signe).", font_size=21),
            box_width=11.5,
        )
        piege1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier piège : un sur zéro n'est pas une forme "
                "indéterminée. Selon le signe du dénominateur qui s'annule, "
                "on conclut directement à plus l'infini, moins l'infini, ou "
                "à l'absence de limite."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            Text("Face à une F.I., ne jamais conclure « la limite n'existe pas » : "
                 "il faut transformer l'écriture pour statuer.", font_size=21),
            box_width=11.5,
        )
        piege2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième piège : face à une forme indéterminée, ne jamais "
                "conclure hâtivement que la limite n'existe pas — il faut "
                "transformer l'expression avant de pouvoir se prononcer."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            Text("sin(x)/x → 1 en 0 n'est vrai qu'en RADIANS, jamais en degrés.", font_size=22),
            box_width=10.5,
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège : la limite de sinus de x sur x qui vaut "
                "un en zéro n'est valable qu'en radians — jamais avec un "
                "angle exprimé en degrés."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            Text("Prolongement par continuité : exige une limite FINIE. "
                 "Une limite infinie interdit tout prolongement.", font_size=22),
            box_width=10.5,
        )
        piege4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatrième piège : le prolongement par continuité exige une "
                "limite finie. Si la limite est infinie, aucun "
                "prolongement continu n'est possible."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        piege5 = warning_box(
            Text("TVI : exige la continuité de f sur l'intervalle FERMÉ [a;b] tout entier, "
                 "pas seulement aux extrémités.", font_size=21),
            box_width=11.5,
        )
        piege5.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cinquième et dernier piège : le théorème des valeurs "
                "intermédiaires exige la continuité de f sur l'intervalle "
                "fermé a, b tout entier — pas seulement en a et en b."
            )
        ) as tracker:
            self.play(FadeIn(piege5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege5))

        # --- Essentiel à retenir du chapitre --------------------------------------
        essentiel = essentiel_box(
            MathTex(
                r"""
                \begin{array}{l}
                \bullet\ \text{Limite finie en } \pm\infty \Rightarrow \text{asymptote horizontale ;}
                \text{ limite infinie en } x_0 \Rightarrow \text{asymptote verticale.}\\
                \bullet\ \text{4 F.I. : } (+\infty)-\infty,\ 0\times\infty,\ \infty/\infty,\ 0/0\ ;
                \text{ méthodes : factorisation, conjuguée, taux d'accroissement.}\\
                \bullet\ \lim_{x\to 0}\dfrac{\sin x}{x}=1,\ \lim_{x\to 0}\dfrac{\tan x}{x}=1,\
                \lim_{x\to 0}\dfrac{1-\cos x}{x^2}=\dfrac{1}{2}\\
                \bullet\ f \text{ continue en } x_0 :\ x_0\in D_f,\ \lim f \text{ finie en } x_0,\
                \lim_{x\to x_0} f(x) = f(x_0)\\
                \bullet\ \text{Prolongement possible si limite finie ; TVI si } f \text{ continue sur } [a\,;b]
                \end{array}
                """,
                font_size=19,
            ),
            box_width=12.3,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de ce chapitre : une limite finie en "
                "plus ou moins l'infini donne une asymptote horizontale, "
                "une limite infinie en un point donne une asymptote "
                "verticale. Il existe quatre formes indéterminées, que l'on "
                "lève par factorisation, expression conjuguée, ou taux "
                "d'accroissement. Les trois limites trigonométriques de "
                "référence sont à connaître par cœur. Une fonction est "
                "continue en x zéro si elle y est définie, y admet une "
                "limite finie, et que cette limite vaut f de x zéro. Enfin, "
                "le prolongement par continuité exige une limite finie, et "
                "le théorème des valeurs intermédiaires exige la continuité "
                "sur tout l'intervalle fermé."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
