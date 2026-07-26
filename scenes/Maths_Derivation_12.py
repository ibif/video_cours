"""
scenes/Maths_Derivation_12.py — Chapitre 9 (1ereC, Maths), scène 12.

Dérivées successives f'', f''', f⁽ⁿ⁾, exemple résolu 15, interprétation
cinématique (vitesse, accélération), exemple résolu 16 (moto-taxi), 4
method_box (méthodes), 4 warning_box (pièges), essentiel_box récapitulatif
final du chapitre.
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DeriveesSuccessivesEtSynthese(NotionScene):
    def construct(self):
        titre = scene_title("Dérivées successives — synthèse")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------------
        enonce = Text(
            _wrap(
                "La fonction dérivée f' est elle-même une fonction : peut-on "
                "la dériver à son tour ? Et à quoi cela correspond-il "
                "physiquement, par exemple pour un mobile en mouvement ?",
                width=56,
            ),
            font_size=23,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous terminons ce chapitre avec les dérivées successives. "
                "La fonction dérivée f prime est elle-même une fonction : "
                "rien n'empêche, si elle est dérivable, de la dériver à "
                "nouveau. Et nous verrons que cette idée a une "
                "interprétation physique très concrète, pour un mobile en "
                "mouvement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Définition dérivées successives ------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Si f' est dérivable, sa dérivée est notée f'' (dérivée seconde).", font_size=21),
                Text("Si f'' est dérivable, sa dérivée est f''' (dérivée troisième).", font_size=21),
                MathTex(
                    r"\text{En général : } f^{(n)} = \left(f^{(n-1)}\right)'"
                    r"\quad \text{dérivée n-ième de } f",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Si f prime est elle-même dérivable, sa dérivée est notée f "
                "seconde, ou dérivée seconde de f. Si f seconde est encore "
                "dérivable, sa dérivée est f tierce. Plus généralement, on "
                "note f exposant n, entre parenthèses, la dérivée n-ième de "
                "f, obtenue en dérivant n fois de suite."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple résolu 15 ---------------------------------------------------------
        exemple15 = example_box(
            VGroup(
                Text("Exemple 15 — f(x) = x⁴, dérivées successives jusqu'à f⁽⁴⁾ :", font_size=20),
                MathTex(
                    r"f(x)=x^4 \quad f'(x)=4x^3 \quad f''(x)=12x^2"
                    r"\quad f'''(x)=24x \quad f^{(4)}(x)=24",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        exemple15.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple quinze : soit f de x égale x puissance quatre. On "
                "dérive successivement : f prime de x égale quatre x au "
                "cube, f seconde de x égale douze x carré, f tierce de x "
                "égale vingt-quatre x, et enfin f quatrième de x égale la "
                "constante vingt-quatre."
            )
        ) as tracker:
            self.play(FadeIn(exemple15))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple15))

        # --- Interprétation cinématique -----------------------------------------------
        cinematique = definition_box(
            VGroup(
                Text(
                    "Si x(t) est la position d'un mobile à l'instant t :",
                    font_size=21,
                ),
                MathTex(r"v(t) = x'(t) \quad \text{(vitesse)}", font_size=27),
                MathTex(r"a(t) = v'(t) = x''(t) \quad \text{(accélération)}", font_size=27),
            ).arrange(DOWN, buff=0.28),
            box_width=8.6,
        )
        cinematique.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici l'interprétation cinématique, très utilisée en "
                "physique : si x de t représente la position d'un mobile à "
                "l'instant t, alors la dérivée première, x prime de t, est "
                "la vitesse instantanée v de t, et la dérivée seconde, x "
                "seconde de t, est l'accélération a de t."
            )
        ) as tracker:
            self.play(FadeIn(cinematique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cinematique))

        # --- Exemple résolu 16 : moto-taxi ---------------------------------------------
        enonce16 = Text(
            "Exemple 16 — moto-taxi : x(t) = 2t³ - 9t² + 12t (t en s, x en m)",
            font_size=21,
            color=YELLOW,
        )
        enonce16.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple seize : un moto-taxi se déplace selon la loi x de "
                "t égale deux t au cube, moins neuf t carré, plus douze t, "
                "où t est en secondes et x en mètres. Calculons sa vitesse "
                "et son accélération à l'instant t égale deux secondes."
            )
        ) as tracker:
            self.play(FadeIn(enonce16))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce16))

        calcul16 = example_box(
            VGroup(
                MathTex(r"v(t) = x'(t) = 6t^2-18t+12 \qquad a(t) = v'(t) = 12t-18", font_size=24),
                MathTex(
                    r"v(2) = 6\times4-18\times2+12 = 24-36+12 = 0 \text{ m/s}",
                    font_size=25,
                ),
                MathTex(
                    r"a(2) = 12\times2-18 = 6 \text{ m/s}^2",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.4,
        )
        calcul16.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On calcule d'abord la vitesse, v de t égale x prime de t, "
                "égale six t carré moins dix-huit t plus douze, puis "
                "l'accélération, a de t égale v prime de t, égale douze t "
                "moins dix-huit. À t égale deux secondes, la vitesse vaut "
                "six fois quatre, moins dix-huit fois deux, plus douze, "
                "c'est-à-dire zéro mètre par seconde : le moto-taxi est "
                "momentanément à l'arrêt. Son accélération à cet instant "
                "vaut douze fois deux, moins dix-huit, soit six mètres par "
                "seconde au carré : il est en train de réaccélérer."
            )
        ) as tracker:
            self.play(FadeIn(calcul16))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul16))

        # --- Méthodes (4 method_box) ----------------------------------------------------
        methode1 = method_box(
            Text(
                _wrap(
                    "Calculer un nombre dérivé par la définition : former "
                    "le taux d'accroissement [f(a+h)-f(a)]/h, le "
                    "simplifier (factoriser h, conjuguée si besoin), puis "
                    "faire tendre h vers 0.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=10.4,
        )
        methode1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Récapitulons les méthodes essentielles du chapitre. "
                "Première méthode : pour calculer un nombre dérivé par la "
                "définition, on forme le taux d'accroissement f de a plus "
                "h moins f de a, sur h, on le simplifie, en factorisant h "
                "ou en utilisant la quantité conjuguée si nécessaire, puis "
                "on fait tendre h vers zéro."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            Text(
                _wrap(
                    "Établir l'équation d'une tangente en a : calculer "
                    "f(a), calculer f'(a), puis appliquer directement "
                    "y = f'(a)(x-a) + f(a).",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=9.6,
        )
        methode2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième méthode : pour établir l'équation d'une tangente "
                "en a, on calcule f de a, on calcule f prime de a, puis on "
                "applique directement la formule y égale f prime de a, "
                "fois x moins a, plus f de a."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            Text(
                _wrap(
                    "Étudier les variations de f : calculer f', factoriser "
                    "ou étudier son signe, dresser le tableau de signe "
                    "puis le tableau de variation en s'appuyant sur le "
                    "théorème fondamental.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=10.6,
        )
        methode3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième méthode : pour étudier les variations d'une "
                "fonction f, on calcule f prime, on la factorise ou on "
                "étudie directement son signe, on dresse le tableau de "
                "signe, puis le tableau de variation, en s'appuyant sur le "
                "théorème fondamental vu dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        methode4 = method_box(
            Text(
                _wrap(
                    "Résoudre un problème d'optimisation : exprimer la "
                    "quantité à optimiser en fonction d'une seule "
                    "variable, dériver, étudier le signe de f' pour "
                    "trouver l'extremum recherché.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=10.6,
        )
        methode4.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quatrième méthode : pour résoudre un problème "
                "d'optimisation, on exprime la quantité à optimiser en "
                "fonction d'une seule variable, on dérive cette expression, "
                "puis on étudie le signe de la dérivée pour repérer "
                "l'extremum recherché — exactement la démarche des "
                "extremums locaux vue dans la scène précédente."
            )
        ) as tracker:
            self.play(FadeIn(methode4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode4))

        # --- Pièges à éviter (4 warning_box) ---------------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 : toujours vérifier le domaine de "
                    "dérivabilité AVANT tout calcul (ex : 1/x en 0, √u si "
                    "u ≤ 0) — une formule appliquée hors domaine est "
                    "fausse.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=10.6,
        )
        piege1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Premier piège classique : il faut toujours vérifier le "
                "domaine de dérivabilité avant tout calcul, par exemple un "
                "sur x en zéro, ou racine de u lorsque u n'est pas "
                "strictement positive. Appliquer une formule hors de son "
                "domaine de validité conduit à un résultat faux."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            MathTex(
                r"\text{Piège 2 : } (uv)' \neq u'v' \quad "
                r"\left(\dfrac{u}{v}\right)' \neq \dfrac{u'}{v'} \quad "
                r"(u^n)' \neq n\,u^{n-1}",
                font_size=25,
            ),
            box_width=10.4,
        )
        piege2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième piège, très fréquent : la dérivée d'un produit "
                "n'est jamais le produit des dérivées, la dérivée d'un "
                "quotient n'est jamais le quotient des dérivées, et il ne "
                "faut jamais oublier le facteur u prime dans la dérivée de "
                "u puissance n. Ce sont des erreurs classiques à bannir."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            Text(
                _wrap(
                    "Piège 3 : f'(c) = 0 seul ne suffit jamais à conclure "
                    "à un extremum local (voir x³ en 0) — il faut "
                    "vérifier le changement de signe de f' autour de c.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=10.4,
        )
        piege3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième piège : une dérivée nulle en un point, sans "
                "changement de signe autour de ce point, ne suffit jamais à "
                "conclure à un extremum local — souvenez-vous de x au cube "
                "en zéro."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            Text(
                _wrap(
                    "Piège 4 : ne jamais écrire qu'une fonction est "
                    "décroissante « sur la réunion » de deux intervalles "
                    "disjoints — le sens de variation s'énonce séparément "
                    "sur chaque intervalle.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=10.4,
        )
        piege4.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quatrième et dernier piège : il ne faut jamais affirmer "
                "qu'une fonction est décroissante sur la réunion de deux "
                "intervalles disjoints. Le sens de variation doit toujours "
                "être énoncé séparément sur chaque intervalle du domaine."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- L'essentiel à retenir (récapitulatif du chapitre) --------------------------
        essentiel = essentiel_box(
            Text(
                _wrap(
                    "Le nombre dérivé f'(a), limite du taux "
                    "d'accroissement, donne la pente de la tangente en a. "
                    "Les formules de dérivation permettent de dériver "
                    "toute fonction usuelle. Le signe de f' pilote le "
                    "sens de variation, et un changement de signe de f' "
                    "donne un extremum local. Les dérivées successives "
                    "prolongent cette étude, avec une lecture cinématique "
                    "en physique (vitesse, accélération).",
                    width=58,
                ),
                font_size=21,
            )
        )
        essentiel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre : le nombre dérivé f prime de a, "
                "limite du taux d'accroissement, donne la pente de la "
                "tangente à la courbe au point a. Les formules de "
                "dérivation permettent de dériver toute combinaison de "
                "fonctions usuelles sans repasser par la définition. Le "
                "signe de la dérivée pilote entièrement le sens de "
                "variation de la fonction, et un changement de signe de la "
                "dérivée signale un extremum local. Enfin, les dérivées "
                "successives prolongent naturellement cette étude, avec "
                "une lecture cinématique très concrète en physique : "
                "vitesse et accélération d'un mobile."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
