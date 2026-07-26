"""
scenes/SVT_EchangesIonsSol_03.py — Chapitre 8 (1ereD, SVT), scène 03.

§ 8.1.3-8.1.4 Les échanges de cations et la CEC, le pH du sol : mécanisme
d'échange H+ / cations nutritifs (respiration racinaire), définition de la
capacité d'échange de cations (CEC), tableau des types de sol, exemple de
comparaison de deux sols, définition du pH du sol, remarque sur les sols
ivoiriens ferralitiques. Source : 1ereD/SVT.pdf, pages 104-106.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class EchangesCationsEtCEC(NotionScene):
    def construct(self):
        titre = scene_title("8.1 — Échanges de cations, CEC et pH du sol")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : la rétention est un dépôt réversible -----------------
        intro = Text(
            _wrap(
                "La rétention des cations par le complexe argilo-humique "
                "n'est pas une prison : c'est un dépôt réversible. Comment "
                "les cations retenus redeviennent-ils disponibles pour la "
                "plante ?",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons vu que le complexe argilo-humique retient les "
                "cations à sa surface. Mais cette rétention n'est pas une "
                "prison : c'est un dépôt réversible. Comment les cations "
                "retenus redeviennent-ils disponibles pour la plante ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : mécanisme de l'échange H+ / cations -----------
        equation = MathTex(
            r"CO_2 + H_2O \;\longrightarrow\; H^+ + HCO_3^-",
            font_size=34,
            color=YELLOW,
        )
        equation.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le mécanisme. La racine respire et rejette du "
                "dioxyde de carbone, qui se dissout dans l'eau du sol et "
                "se transforme : le CO2 plus H2O donne un ion H+ plus un "
                "ion bicarbonate, HCO3−."
            )
        ) as tracker:
            self.play(Write(equation))
            self.wait(tracker.get_remaining_duration())

        # Schéma de l'échange : micelle avec K+ remplacé par H+
        micelle = Circle(radius=0.9, color=ORANGE, fill_color=ORANGE, fill_opacity=0.35, stroke_width=3)
        micelle.next_to(equation, DOWN, buff=0.7)
        h_dot = Dot(micelle.get_left() + LEFT * 0.5, color=RED, radius=0.1)
        h_txt = Text("H+", font_size=20, color=RED).next_to(h_dot, LEFT, buff=0.1)
        fleche_entree = Arrow(h_dot.get_center() + LEFT * 0.6, micelle.get_left(), buff=0.05, color=RED, stroke_width=3)

        k_dot = Dot(micelle.get_right() + RIGHT * 0.3, color=GREEN, radius=0.1)
        k_txt = Text("K+", font_size=20, color=GREEN).next_to(k_dot, RIGHT, buff=0.1)
        fleche_sortie = Arrow(micelle.get_right(), k_dot.get_center() + RIGHT * 0.55, buff=0.05, color=GREEN, stroke_width=3)
        vers_racine = Text("→ vers la racine (absorbable)", font_size=17, color=GREEN)
        vers_racine.next_to(VGroup(k_dot, k_txt), RIGHT, buff=0.15)

        schema = VGroup(micelle, h_dot, h_txt, fleche_entree, k_dot, k_txt, fleche_sortie, vers_racine)
        schema.scale(0.9)
        schema.next_to(equation, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les ions H+ s'adsorbent alors sur le complexe argilo-"
                "humique, en prenant la place des cations nutritifs, "
                "potassium, calcium, magnésium ou ammonium, qui sont "
                "libérés. Ces cations passent dans la solution du sol, "
                "près des poils absorbants, et deviennent absorbables par "
                "la racine. Cet échange respecte la neutralité électrique "
                ": il faut deux ions H+ pour libérer un ion calcium deux "
                "plus, qui porte deux charges positives."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation), FadeOut(schema))

        # --- Définition CEC + tableau des types de sol ---------------------
        def_cec = definition_box(
            Text(
                _wrap(
                    "La capacité d'échange de cations (CEC) est la "
                    "quantité totale de cations qu'un sol peut retenir "
                    "sur son CAH, exprimée en milliéquivalents pour 100g "
                    "de sol (méq/100g). Elle est élevée si le sol est "
                    "riche en argile et surtout en humus.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_cec.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On mesure la capacité totale d'un sol à retenir des "
                "cations par un indicateur appelé capacité d'échange de "
                "cations, ou CEC : c'est la quantité totale de cations "
                "qu'un sol peut retenir sur son complexe argilo-humique, "
                "exprimée en milliéquivalents pour cent grammes de sol. "
                "Elle est d'autant plus élevée que le sol est riche en "
                "argile, et surtout en humus."
            )
        ) as tracker:
            self.play(FadeIn(def_cec))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_cec))

        tab_titre = Text("Types de sol et CEC (méq/100g)", font_size=26, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.5)

        col1 = VGroup(
            Text("Sol sableux", font_size=22, color=WHITE),
            Text("Sol limoneux", font_size=22, color=WHITE),
            Text("Sol argilo-humique riche", font_size=22, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        col2 = VGroup(
            Text("2 - 5 (faible)", font_size=22, color=RED),
            Text("10 - 15 (moyenne)", font_size=22, color=YELLOW),
            Text("20 - 30 (forte)", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        tableau = VGroup(col1, col2).arrange(RIGHT, buff=0.8, aligned_edge=UP)
        tableau.next_to(tab_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le tableau ci-dessous compare trois grands types de sol. "
                "Un sol sableux a une CEC faible, entre deux et cinq : il "
                "retient peu les cations. Un sol limoneux a une CEC "
                "moyenne, entre dix et quinze. Un sol argilo-humique riche "
                "a une CEC forte, entre vingt et trente : il conserve bien "
                "les éléments nutritifs."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- Exemple traité : comparer la fertilité de deux sols ----------
        exemple = example_box(
            Text(
                _wrap(
                    "Sol A : CEC = 4 méq/100g. Sol B : CEC = 24 méq/100g. "
                    "Lequel retient mieux un engrais potassique ? Le sol B "
                    "a une CEC 6 fois plus grande : les ions K+ de "
                    "l'engrais seront adsorbés et conservés par B, mais "
                    "lessivés dans A. B est plus fertile ; sur A, "
                    "fractionner les apports d'engrais et augmenter "
                    "l'humus.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Appliquons ceci. Un sol A a une CEC de quatre "
                "milliéquivalents pour cent grammes ; un sol B a une CEC "
                "de vingt-quatre. Lequel retient le mieux un engrais "
                "potassique ? La CEC mesure la quantité de cations "
                "retenue : le sol B a une capacité six fois plus grande "
                "que le sol A. Les ions potassium de l'engrais seront donc "
                "adsorbés et conservés par le sol B, alors qu'ils seront "
                "lessivés dans le sol A. Conclusion : le sol B est plus "
                "fertile ; sur le sol A, il faudra fractionner les apports "
                "d'engrais et ajouter de la matière organique, pour "
                "augmenter l'humus et donc la CEC."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- pH du sol -------------------------------------------------------
        def_ph = definition_box(
            Text(
                _wrap(
                    "Le pH mesure l'acidité de la solution du sol : "
                    "inférieur à 7, sol acide ; égal à 7, neutre ; "
                    "supérieur à 7, basique. Les grandes cultures "
                    "ivoiriennes (maïs, manioc, igname, cacao) donnent "
                    "les meilleurs rendements pour un pH entre 5,5 et 7.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_ph.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Autre facteur essentiel : le pH du sol, qui mesure "
                "l'acidité de la solution du sol. En dessous de sept, le "
                "sol est acide ; à sept, il est neutre ; au-dessus de "
                "sept, il est basique. Les grandes cultures ivoiriennes, "
                "maïs, manioc, igname, cacao, donnent leurs meilleurs "
                "rendements pour un pH compris entre cinq virgule cinq et "
                "sept. Dans un sol très acide, en dessous de cinq, le "
                "phosphore devient insoluble, le calcium, le magnésium et "
                "le potassium sont fortement lessivés, l'aluminium passe "
                "en solution et devient toxique pour les racines, et "
                "l'activité des micro-organismes utiles ralentit. Pour "
                "corriger cela, l'agriculteur pratique le chaulage : "
                "l'épandage de chaux ou de calcaire, qui relève le pH et "
                "apporte du calcium."
            )
        ) as tracker:
            self.play(FadeIn(def_ph))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ph))

        # --- Remarque : les sols ivoiriens ---------------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Une grande partie des sols de Côte d'Ivoire sont des "
                    "sols ferralitiques (climat chaud et humide), "
                    "naturellement acides et fragiles, avec un lessivage "
                    "intense et un humus qui se décompose vite : la "
                    "connaissance des échanges d'ions est indispensable à "
                    "la fertilisation raisonnée.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une remarque importante pour la Côte d'Ivoire : une "
                "grande partie de nos sols sont des sols ferralitiques, "
                "typiques du climat chaud et humide. Ils sont "
                "naturellement acides et fragiles, avec un lessivage "
                "intense et un humus qui se décompose vite. C'est "
                "pourquoi la connaissance des échanges d'ions au niveau du "
                "sol est indispensable à une fertilisation raisonnée."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(remarque))
