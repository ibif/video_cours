"""
scenes/Chimie_ComposesOxygenes_01.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 01.

§ Introduction (mise en situation : vin de palme, koutoukou, vinaigre) +
Les alcools : groupe -OH, carbone fonctionnel, formule générale R-OH,
formule brute CₙH₂ₙ₊₂O (n≥1), M=14n+18. Piège : les éthers-oxydes R-O-R'
sont des isomères de fonction des alcools.
Source : 1ereC/Chimie.pdf, chapitre 6, pages 54-56.
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
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class IntroductionEtDefinitionAlcools(NotionScene):
    def construct(self):
        titre = scene_title("6. Quelques composés oxygénés")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation -----------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Le vin de palme, le koutoukou, le vinaigre de ménage : ces "
                "produits familiers contiennent tous, en plus du carbone et "
                "de l'hydrogène, un atome d'oxygène dans leur molécule. "
                "Quels sont ces composés organiques oxygénés, et comment "
                "les reconnaître ?",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le vin de palme, le koutoukou, le vinaigre de ménage : ces "
                "produits familiers de Côte d'Ivoire contiennent tous, en "
                "plus du carbone et de l'hydrogène, un atome d'oxygène dans "
                "leur molécule. Quels sont ces composés organiques "
                "oxygénés, et comment les reconnaître ? C'est l'objet de ce "
                "chapitre : les alcools, les phénols, les aldéhydes, les "
                "cétones, les acides carboxyliques et les esters."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : le groupe -OH et le carbone fonctionnel ------------
        def_alcool = definition_box(
            Text(
                _wrap(
                    "Un alcool est un composé organique caractérisé par un "
                    "groupe hydroxyle -OH fixé sur un atome de carbone "
                    "tétragonal (à quatre liaisons simples). Ce carbone est "
                    "appelé carbone fonctionnel.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        def_alcool.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Commençons par les alcools. Un alcool est un composé "
                "organique caractérisé par un groupe hydroxyle, -O-H, fixé "
                "sur un atome de carbone tétragonal, c'est-à-dire un "
                "carbone qui ne porte que des liaisons simples. Ce carbone "
                "particulier est appelé le carbone fonctionnel : c'est lui "
                "qui porte le groupe caractéristique de la fonction."
            )
        ) as tracker:
            self.play(FadeIn(def_alcool))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_alcool))

        # --- Exemple traité : formule générale et formule brute -----------------
        entete_formule = Text("Formule générale et formule brute", font_size=24, color=YELLOW, weight="BOLD")
        entete_formule.next_to(titre, DOWN, buff=0.4)

        formule_gen = MathTex(r"R-OH", font_size=34, color=WHITE)
        formule_gen.next_to(entete_formule, DOWN, buff=0.45)

        formule_brute = MathTex(r"C_nH_{2n+2}O \quad (n \geq 1)", font_size=32, color=WHITE)
        formule_brute.next_to(formule_gen, DOWN, buff=0.4)

        masse_molaire = MathTex(r"M = 14n + 18", font_size=30, color=WHITE)
        masse_molaire.next_to(formule_brute, DOWN, buff=0.4)

        groupe_formule = VGroup(entete_formule, formule_gen, formule_brute, masse_molaire)

        with self.voiceover(
            text=(
                "On note un alcool R-O-H, où R représente un groupe alkyle, "
                "c'est-à-dire le reste de la chaîne carbonée. Sa formule "
                "brute générale est C indice n, H indice deux n plus deux, "
                "O, avec n supérieur ou égal à un — c'est la même carcasse "
                "que celle d'un alcane, avec un atome d'oxygène en plus. Sa "
                "masse molaire vaut donc quatorze n plus dix-huit "
                "grammes par mole. Par exemple, pour n égal deux, "
                "l'éthanol C-2 H-6 O a une masse molaire de quarante-six "
                "grammes par mole."
            )
        ) as tracker:
            self.play(FadeIn(entete_formule))
            self.play(Write(formule_gen))
            self.play(Write(formule_brute))
            self.play(Write(masse_molaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_formule))

        # --- À retenir : propriété récapitulative --------------------------------
        propriete = property_box(
            VGroup(
                Text(
                    _wrap(
                        "Tout alcool CₙH₂ₙ₊₂O dérive d'un alcane CₙH₂ₙ₊₂ "
                        "par remplacement d'un atome d'hydrogène par un "
                        "groupe -OH.",
                        width=46,
                    ),
                    font_size=23,
                ),
                Text("Exemples : CH₄O (n=1) ; C₂H₆O (n=2) ; C₅H₁₂O (n=5).", font_size=21),
            ).arrange(DOWN, buff=0.3),
        )
        propriete.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons ceci : tout alcool, de formule C indice n, H "
                "indice deux n plus deux, O, dérive d'un alcane de formule "
                "C indice n, H indice deux n plus deux, par remplacement "
                "d'un seul atome d'hydrogène par un groupe hydroxyle. Ainsi, "
                "pour n égal un, CH-4-O, le méthanol ; pour n égal deux, "
                "C-2 H-6 O, l'éthanol ; pour n égal cinq, C-5 H-12 O."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : les éthers-oxydes ----------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas alcool et éther-oxyde : un éther-oxyde "
                    "R-O-R' a exactement la même formule brute CₙH₂ₙ₊₂O "
                    "qu'un alcool, mais l'atome d'oxygène y est entre deux "
                    "carbones, pas lié à un hydrogène. Alcools et "
                    "éthers-oxydes sont des isomères de fonction.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Attention à un piège classique : ne confondez pas un "
                "alcool avec un éther-oxyde. Un éther-oxyde, noté R-O-R "
                "prime, possède exactement la même formule brute, C indice "
                "n, H indice deux n plus deux, O, qu'un alcool — mais son "
                "atome d'oxygène est placé entre deux atomes de carbone, et "
                "non lié à un hydrogène. Alcools et éthers-oxydes sont donc "
                "des isomères de fonction : même formule brute, fonctions "
                "chimiques différentes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
