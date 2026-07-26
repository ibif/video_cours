"""
scenes/Chimie_Ethanol_10.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 10 (clôture du chapitre).

§ 7. Usages de l'éthanol et dangers de l'alcoolisme. Usages (boissons,
bioéthanol carburant E10/E85, désinfectant à 70°, solvant, matière
première industrielle). Dangers santé (cirrhose, cancers, maladies
cardiovasculaires) et sociaux. Sécurité routière (ralentissement réflexes,
alcoolémie max, élimination lente 0,15 g/L/h, OSER Côte d'Ivoire).
Méthodes et astuces (équilibrer combustion d'un alcool, calculs de degré
alcoolique). 3 pièges à éviter (densité vs masse volumique ; degré = %
volume ; fermentation limitée à 16°). Essentiel du chapitre.
Source : 1ereC/Chimie.pdf, chapitre 7, pages 73-75.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class UsagesDangersEssentielEthanol(NotionScene):
    def construct(self):
        titre = scene_title("7.7 Usages, dangers de l'alcoolisme et essentiel du chapitre")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : les usages de l'éthanol --------------------------------------
        entete_usages = Text("Usages de l'éthanol", font_size=23, color=YELLOW, weight="BOLD")
        entete_usages.next_to(titre, DOWN, buff=0.35)

        usages = _bullets(
            [
                "Boissons alcoolisées : vins, bières, liqueurs "
                "(fermentation puis, parfois, distillation).",
                "Carburant : le bioéthanol (canne à sucre, maïs, manioc) "
                "est mélangé à l'essence (E10 : 10% ; E85 : jusqu'à 85%).",
                "Désinfectant : l'alcool à 70° détruit les microbes en "
                "dénaturant leurs protéines.",
                "Solvant : parfums, teintures, médicaments, vernis, "
                "encres.",
                "Matière première industrielle : fabrication de l'acide "
                "éthanoïque, des esters, etc.",
            ],
            font_size=18,
            width=58,
        )
        usages.next_to(entete_usages, DOWN, buff=0.3)
        _fit(VGroup(entete_usages, usages), entete_usages.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par les usages de l'éthanol et les "
                "dangers de l'alcoolisme. L'éthanol sert d'abord aux "
                "boissons alcoolisées, vins, bières, liqueurs. C'est "
                "aussi un carburant : le bioéthanol, produit à partir de "
                "la canne à sucre, du maïs ou du manioc, est mélangé à "
                "l'essence, dans les carburants E-10, à dix pour cent "
                "d'éthanol, ou E-85, jusqu'à quatre-vingt-cinq pour "
                "cent. C'est également un désinfectant : l'alcool à "
                "soixante-dix degrés détruit les microbes en dénaturant "
                "leurs protéines. Enfin, c'est un excellent solvant, pour "
                "les parfums, teintures, médicaments et vernis, et une "
                "matière première pour l'industrie chimique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_usages))
            self.play(FadeIn(usages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_usages), FadeOut(usages))

        # --- Raisonnement : dangers de l'alcoolisme + sécurité routière ---------
        entete_dangers = Text("Les dangers de l'alcoolisme", font_size=22, color=RED, weight="BOLD")
        entete_dangers.next_to(titre, DOWN, buff=0.35)

        dangers = _bullets(
            [
                "Santé : cirrhose du foie, cancers (bouche, gorge, "
                "œsophage, foie), maladies cardiovasculaires, troubles "
                "du système nerveux.",
                "Vie sociale : violences familiales, pauvreté, échec "
                "scolaire, perte d'emploi.",
                "Sécurité routière : l'alcool ralentit les réflexes, "
                "allonge le temps de réaction et réduit le champ visuel ; "
                "l'organisme n'élimine l'alcool que très lentement, "
                "environ 0,15 g/L par heure.",
            ],
            font_size=18,
            width=58,
        )
        dangers.next_to(entete_dangers, DOWN, buff=0.3)
        _fit(VGroup(entete_dangers, dangers), entete_dangers.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "L'alcoolisme est une maladie aux conséquences graves. "
                "Sur la santé : cirrhose du foie, cancers de la bouche, "
                "de la gorge, de l'œsophage ou du foie, maladies "
                "cardiovasculaires, troubles du système nerveux. Sur la "
                "vie sociale : violences familiales, pauvreté, échec "
                "scolaire, perte d'emploi. Enfin, sur la sécurité "
                "routière : l'alcool, même à faible dose, ralentit les "
                "réflexes, allonge le temps de réaction et réduit le "
                "champ visuel. L'organisme n'élimine l'alcool que très "
                "lentement, environ zéro virgule quinze gramme par litre "
                "et par heure : ni le café, ni la douche, ni l'exercice "
                "physique n'accélèrent cette élimination. En Côte "
                "d'Ivoire, l'OSER, l'Office de Sécurité Routière, rappelle "
                "régulièrement : « Boire ou conduire, il faut choisir »."
            )
        ) as tracker:
            self.play(FadeIn(entete_dangers))
            self.play(FadeIn(dangers))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_dangers), FadeOut(dangers))

        # --- Exemple traité : les deux méthodes-clés du chapitre -----------------
        methode1 = method_box(
            VGroup(
                Text("Équilibrer la combustion d'un alcool CₙH₂ₙ₊₂O", font_size=18, weight="BOLD"),
                Text("1. Carbone : n CO₂  2. Hydrogène : (n+1) H₂O  3. Oxygène (en dernier) : 3n/2 O₂", font_size=16),
                MathTex(r"\text{Éthanol }(n{=}2): C_2H_5OH+3\,O_2 \rightarrow 2\,CO_2+3\,H_2O", font_size=19, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.6,
        )
        methode1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Rappelons les deux méthodes-clés du chapitre. Première "
                "méthode : équilibrer la combustion d'un alcool de "
                "formule C indice n, H indice deux n plus deux, O. On "
                "équilibre d'abord le carbone, avec n C-O-2, puis "
                "l'hydrogène, avec n plus un H-2-O, et enfin l'oxygène en "
                "dernier, avec trois n sur deux O-2. Pour l'éthanol, n "
                "égale deux, cela donne directement trois O-2."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            VGroup(
                Text("Calculs de degré alcoolique", font_size=18, weight="BOLD"),
                Text("1. Convertir tous les volumes dans la même unité (mL ou cL).", font_size=16),
                MathTex(r"2.\ V_{\text{éthanol}} = \dfrac{d\times V_{\text{boisson}}}{100}\ ;\ \ 3.\ m = 0{,}789\times V_{\text{éthanol}}", font_size=18, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.6,
        )
        methode2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Seconde méthode : les calculs de degré alcoolique. On "
                "convertit d'abord tous les volumes dans la même unité, "
                "millilitre ou centilitre. On applique ensuite V éthanol "
                "égale d fois V boisson, sur cent, puis, si la masse est "
                "demandée, m égale zéro virgule sept-cent-quatre-vingt-"
                "neuf fois V éthanol."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Pièges à éviter : les trois pièges classiques du chapitre ----------
        entete_pieges = Text("Trois pièges classiques à éviter", font_size=21, color=YELLOW, weight="BOLD")
        entete_pieges.next_to(titre, DOWN, buff=0.35)

        pieges = warning_box(
            _bullets(
                [
                    "Densité d = 0,789 (nombre SANS unité) ≠ masse "
                    "volumique ρ = 789 g/L (AVEC une unité) : une erreur "
                    "d'unité fausse tout le calcul.",
                    "Le degré alcoolique est un pourcentage en VOLUME, "
                    "pas en masse : un vin à 12° contient 12 mL, et non "
                    "12 g, d'éthanol pur pour 100 mL de vin.",
                    "La fermentation seule ne peut pas dépasser environ "
                    "16° (les levures sont détruites par l'alcool) : pour "
                    "des boissons plus fortes, il faut une distillation.",
                ],
                font_size=17,
                width=58,
            ),
            box_width=12.8,
        )
        pieges.next_to(entete_pieges, DOWN, buff=0.3)
        _fit(VGroup(entete_pieges, pieges), entete_pieges.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici les trois pièges classiques du chapitre. Un : ne "
                "pas confondre la densité, zéro virgule sept-cent-quatre-"
                "vingt-neuf, un nombre sans unité, avec la masse "
                "volumique, sept-cent-quatre-vingt-neuf grammes par "
                "litre, qui elle a une unité : une erreur d'unité fausse "
                "tout le calcul. Deux : le degré alcoolique est un "
                "pourcentage en volume, et non en masse : un vin à douze "
                "degrés contient douze millilitres, et non douze "
                "grammes, d'éthanol pur pour cent millilitres de vin. "
                "Trois : la fermentation seule ne peut pas dépasser "
                "environ seize degrés, car les levures sont détruites par "
                "l'alcool qu'elles produisent ; pour obtenir des boissons "
                "plus fortes, il faut une distillation."
            )
        ) as tracker:
            self.play(FadeIn(entete_pieges))
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pieges), FadeOut(pieges))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) -------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Éthanol : C₂H₆O, soit CH₃-CH₂-OH, alcool primaire, "
                    "M = 46 g/mol.",
                    "Deux voies d'obtention : fermentation des sucres "
                    "(≤16°, puis distillation) ou hydratation industrielle "
                    "de l'éthylène (H₂SO₄, ~300°C).",
                    "Miscible à l'eau (liaisons hydrogène), Téb = 78,5°C, "
                    "d = 0,789 (sans unité).",
                    "Combustion : oxydation totale, très exothermique. "
                    "Oxydation ménagée (Cu ou KMnO₄) : éthanol → éthanal "
                    "→ acide éthanoïque.",
                    "Degré alcoolique d = Véthanol/Vboisson × 100 ; tests "
                    "de reconnaissance (KMnO₄, DNPH, Schiff, papier pH).",
                    "Usages multiples (boissons, carburant, désinfectant, "
                    "solvant) mais alcoolisme dangereux pour la santé, la "
                    "vie sociale et la sécurité routière.",
                ],
                font_size=17,
                width=58,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)
        _fit(essentiel, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. L'éthanol a pour formule "
                "C-2, H-6, O, soit C-H-3 tiret C-H-2 tiret O-H, c'est un "
                "alcool primaire de masse molaire quarante-six grammes "
                "par mole. On l'obtient par deux voies : la fermentation "
                "des sucres, limitée à environ seize degrés puis "
                "éventuellement distillée, ou l'hydratation industrielle "
                "de l'éthylène, avec l'acide sulfurique comme catalyseur "
                "vers trois cents degrés. Il est miscible à l'eau grâce "
                "aux liaisons hydrogène, bout à soixante-dix-huit virgule "
                "cinq degrés, et sa densité vaut zéro virgule sept-cent-"
                "quatre-vingt-neuf, sans unité. Sa combustion est une "
                "oxydation totale, très exothermique ; son oxydation "
                "ménagée, par le cuivre ou le permanganate, donne "
                "successivement l'éthanal puis l'acide éthanoïque. Le "
                "degré alcoolique d'une boisson se calcule avec d égale V "
                "éthanol sur V boisson fois cent, et plusieurs tests "
                "permettent de reconnaître les alcools et leurs produits "
                "d'oxydation. Enfin, si l'éthanol a de nombreux usages, "
                "boissons, carburant, désinfectant, solvant, "
                "l'alcoolisme reste dangereux pour la santé, la vie "
                "sociale et la sécurité routière."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
