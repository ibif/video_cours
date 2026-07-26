"""
scenes/Chimie_ComposesOxygenes_07.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 07.

§ Les esters : groupe ester -COO-, formule générale R-COO-R', CₙH₂ₙO₂
(isomères de fonction des acides), nomenclature en 2 termes, odeurs
fruitées et usages, ouverture vers l'estérification (sans détailler).
Source : 1ereC/Chimie.pdf, chapitre 6, page 61.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class Esters(NotionScene):
    def construct(self):
        titre = scene_title("Les esters")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : le groupe ester ------------------------------------------------
        def_ester = definition_box(
            VGroup(
                Text("Le groupe ester dérive du groupe carboxyle par", font_size=23),
                Text("remplacement du H par un groupe alkyle R' :", font_size=23),
                MathTex(r"-COO- \qquad R-COO-R'", font_size=30, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25),
        )
        def_ester.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les esters possèdent le groupe ester, moins C-O-O-moins, "
                "qui dérive du groupe carboxyle par remplacement de "
                "l'hydrogène acide par un groupe alkyle R prime. Un ester "
                "s'écrit donc R-C-O-O-R prime."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_ester))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ester))

        # --- Raisonnement : formule brute + nomenclature -----------------------------
        formule = property_box(
            Text(
                _wrap(
                    "Formule brute générale : CₙH₂ₙO₂ — identique à celle "
                    "des acides carboxyliques. Les esters sont donc des "
                    "isomères de fonction des acides carboxyliques.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        formule.next_to(titre, DOWN, buff=0.4)
        _fit(formule, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "La formule brute générale d'un ester, C indice n, H "
                "indice deux n, O-2, est rigoureusement identique à celle "
                "des acides carboxyliques. Esters et acides carboxyliques "
                "sont donc des isomères de fonction : même formule brute, "
                "fonctions chimiques différentes."
            )
        ) as tracker:
            self.play(FadeIn(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule))

        methode = method_box(
            Text(
                _wrap(
                    "Nomenclature en deux mots : « <acide>-oate de "
                    "<alkyle>-yle ». Le premier terme vient de l'acide "
                    "R-COOH (suffixe -oate), le second du groupe R' "
                    "(suffixe -yle).",
                    width=48,
                ),
                font_size=22,
            ),
        )
        methode.next_to(titre, DOWN, buff=0.4)
        _fit(methode, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Le nom d'un ester s'écrit en deux termes : le nom de "
                "l'acide dont il dérive, avec le suffixe -oate, suivi de "
                "« de », puis le nom du groupe alkyle R prime, avec le "
                "suffixe -yle."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : tableau d'exemples --------------------------------------
        tab_titre = Text("Exemples", font_size=24, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.35)

        tab = VGroup(
            VGroup(MathTex(r"CH_3-COO-CH_2CH_3", font_size=25), Text("éthanoate d'éthyle", font_size=21)).arrange(RIGHT, buff=0.6),
            VGroup(MathTex(r"CH_3COO-CH_3", font_size=25), Text("éthanoate de méthyle", font_size=21)).arrange(RIGHT, buff=0.6),
            VGroup(MathTex(r"HCOO-CH_2CH_3", font_size=25), Text("méthanoate d'éthyle", font_size=21)).arrange(RIGHT, buff=0.6),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        tab.next_to(tab_titre, DOWN, buff=0.4)

        groupe_tab = VGroup(tab_titre, tab)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Par exemple, C-H-3, C-O-O, C-H-2, C-H-3 se nomme "
                "éthanoate d'éthyle. C-H-3, C-O-O, C-H-3 se nomme "
                "éthanoate de méthyle. H-C-O-O, C-H-2, C-H-3 se nomme "
                "méthanoate d'éthyle."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- À retenir : odeurs fruitées et usages --------------------------------------
        usages = property_box(
            Text(
                _wrap(
                    "Les esters ont souvent des odeurs fruitées agréables "
                    "(banane, ananas, framboise) : ils sont donc largement "
                    "utilisés en parfumerie, dans les arômes alimentaires "
                    "et dans la fabrication des savons (savonnerie).",
                    width=48,
                ),
                font_size=22,
            ),
        )
        usages.next_to(titre, DOWN, buff=0.4)
        _fit(usages, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Les esters ont souvent des odeurs fruitées très "
                "agréables : banane, ananas, framboise. C'est pourquoi ils "
                "sont largement utilisés en parfumerie, dans les arômes "
                "alimentaires, et interviennent aussi dans la fabrication "
                "des savons, en savonnerie."
            )
        ) as tracker:
            self.play(FadeIn(usages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(usages))

        # --- Piège / ouverture : l'estérification (sans détailler) ---------------------
        ouverture = warning_box(
            VGroup(
                Text(
                    "On obtient un ester par estérification, réaction",
                    font_size=21,
                ),
                Text(
                    "d'un acide carboxylique sur un alcool — RÉVERSIBLE :",
                    font_size=21,
                ),
                MathTex(
                    r"R-COOH + R'-OH \; \rightleftharpoons \; R-COO-R' + H_2O",
                    font_size=25,
                    color="#1A1A1A",
                ),
                Text(
                    "(étudiée en détail dans un chapitre ultérieur)",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=12.0,
        )
        ouverture.next_to(titre, DOWN, buff=0.4)
        _fit(ouverture, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Une ouverture pour finir : un ester s'obtient par une "
                "réaction appelée estérification, entre un acide "
                "carboxylique et un alcool. C'est une réaction "
                "réversible, comme le montre la double flèche : "
                "R-C-O-O-H plus R prime-O-H est en équilibre avec "
                "R-C-O-O-R prime plus H-2-O. Nous étudierons cette "
                "réaction en détail dans un chapitre ultérieur."
            )
        ) as tracker:
            self.play(FadeIn(ouverture))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ouverture), FadeOut(titre))
