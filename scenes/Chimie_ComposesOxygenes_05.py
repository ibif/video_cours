"""
scenes/Chimie_ComposesOxygenes_05.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 05.

§ Le groupe carbonyle >C=O + les aldéhydes (R-CHO, CₙH₂ₙO, nomenclature
-al) + les cétones (R₁-CO-R₂, CₙH₂ₙO n≥3, isomères de fonction des
aldéhydes, nomenclature -one) + tableau de distinction aldéhyde/cétone.
Source : 1ereC/Chimie.pdf, chapitre 6, pages 59-60.
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
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class AldehydesEtCetones(NotionScene):
    def construct(self):
        titre = scene_title("Le groupe carbonyle : aldéhydes et cétones")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le groupe carbonyle -------------------------------------------
        def_carbonyle = definition_box(
            VGroup(
                Text(
                    "Le groupe carbonyle est un atome de carbone doublement",
                    font_size=23,
                ),
                Text("lié à un atome d'oxygène :", font_size=23),
                MathTex(r">C=O", font_size=32, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25),
        )
        def_carbonyle.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux nouvelles familles partagent un même groupe "
                "caractéristique : le groupe carbonyle, un atome de "
                "carbone doublement lié à un atome d'oxygène, C égale O. "
                "Selon ce qui entoure ce carbone, on obtient soit un "
                "aldéhyde, soit une cétone."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_carbonyle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_carbonyle))

        # --- Raisonnement : les aldéhydes -------------------------------------------
        def_aldehyde = definition_box(
            VGroup(
                Text(
                    "Un aldéhyde porte le groupe carbonyle à l'EXTRÉMITÉ de",
                    font_size=22,
                ),
                Text("la chaîne carbonée (un H sur le carbone fonctionnel) :", font_size=22),
                MathTex(r"R-CHO \qquad C_nH_{2n}O \;\; (n \geq 1)", font_size=27, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25),
        )
        def_aldehyde.next_to(titre, DOWN, buff=0.4)
        _fit(def_aldehyde, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Un aldéhyde porte le groupe carbonyle à l'extrémité de la "
                "chaîne carbonée : son carbone fonctionnel porte donc "
                "encore un atome d'hydrogène. On le note R-C-H-O. Sa "
                "formule brute générale est C indice n, H indice deux n, "
                "O, avec n supérieur ou égal à un."
            )
        ) as tracker:
            self.play(FadeIn(def_aldehyde))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_aldehyde))

        methode_al = method_box(
            Text(
                _wrap(
                    "Nomenclature des aldéhydes : le carbone fonctionnel "
                    "est TOUJOURS le carbone n°1 (extrémité de chaîne), "
                    "donc jamais d'indice de position. On remplace le « e » "
                    "final du nom de l'alcane par le suffixe « -al ».",
                    width=48,
                ),
                font_size=21,
            ),
        )
        methode_al.next_to(titre, DOWN, buff=0.4)
        _fit(methode_al, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pour nommer un aldéhyde, retenez que le carbone "
                "fonctionnel est toujours le carbone numéro un, puisqu'il "
                "est en bout de chaîne : on ne met donc jamais d'indice de "
                "position. On remplace simplement le e final du nom de "
                "l'alcane par le suffixe -al."
            )
        ) as tracker:
            self.play(FadeIn(methode_al))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_al))

        tab_al_titre = Text("Exemples d'aldéhydes", font_size=23, color=YELLOW, weight="BOLD")
        tab_al_titre.next_to(titre, DOWN, buff=0.35)

        tab_al = VGroup(
            VGroup(MathTex(r"H-CHO", font_size=26), Text("méthanal", font_size=21)).arrange(RIGHT, buff=0.8),
            VGroup(MathTex(r"CH_3-CHO", font_size=26), Text("éthanal", font_size=21)).arrange(RIGHT, buff=0.8),
            VGroup(MathTex(r"CH_3-CH_2-CHO", font_size=26), Text("propanal", font_size=21)).arrange(RIGHT, buff=0.8),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        tab_al.next_to(tab_al_titre, DOWN, buff=0.4)

        groupe_tab_al = VGroup(tab_al_titre, tab_al)
        _fit(groupe_tab_al, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici trois exemples. H-C-H-O se nomme méthanal. C-H-3, "
                "C-H-O se nomme éthanal. C-H-3, C-H-2, C-H-O se nomme "
                "propanal : jamais de un devant -al."
            )
        ) as tracker:
            self.play(FadeIn(tab_al_titre))
            self.play(FadeIn(tab_al))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab_al))

        # --- Exemple traité : les cétones -------------------------------------------
        def_cetone = definition_box(
            VGroup(
                Text(
                    "Une cétone porte le groupe carbonyle À L'INTÉRIEUR de",
                    font_size=22,
                ),
                Text("la chaîne (2 carbones voisins du carbone fonctionnel) :", font_size=22),
                MathTex(r"R_1-CO-R_2 \qquad C_nH_{2n}O \;\; (n \geq 3)", font_size=27, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25),
        )
        def_cetone.next_to(titre, DOWN, buff=0.4)
        _fit(def_cetone, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Une cétone, elle, porte le groupe carbonyle à l'intérieur "
                "de la chaîne carbonée : son carbone fonctionnel est relié "
                "à deux autres carbones, R-1 et R-2, jamais à un "
                "hydrogène. On la note R-1-C-O-R-2. Sa formule brute est "
                "identique à celle des aldéhydes, C indice n, H indice "
                "deux n, O, mais avec n supérieur ou égal à trois cette "
                "fois : il faut au moins trois carbones pour avoir de la "
                "place à l'intérieur de la chaîne. Aldéhydes et cétones "
                "sont donc des isomères de fonction."
            )
        ) as tracker:
            self.play(FadeIn(def_cetone))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_cetone))

        methode_one = method_box(
            Text(
                _wrap(
                    "Nomenclature des cétones : on numérote la chaîne pour "
                    "donner au carbone fonctionnel l'indice le plus petit, "
                    "puis on remplace le « e » final par le suffixe "
                    "« -one », précédé de cet indice de position.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        methode_one.next_to(titre, DOWN, buff=0.4)
        _fit(methode_one, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pour nommer une cétone, on numérote la chaîne de façon à "
                "donner au carbone fonctionnel l'indice le plus petit "
                "possible, puis on remplace le e final du nom de l'alcane "
                "par le suffixe -one, précédé cette fois de l'indice de "
                "position, car il peut y avoir une ambiguïté."
            )
        ) as tracker:
            self.play(FadeIn(methode_one))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_one))

        tab_one_titre = Text("Exemples de cétones", font_size=23, color=YELLOW, weight="BOLD")
        tab_one_titre.next_to(titre, DOWN, buff=0.35)

        tab_one = VGroup(
            VGroup(MathTex(r"CH_3-CO-CH_3", font_size=26), Text("propan-2-one", font_size=21)).arrange(RIGHT, buff=0.8),
            VGroup(MathTex(r"CH_3-CO-CH_2-CH_3", font_size=26), Text("butan-2-one", font_size=21)).arrange(RIGHT, buff=0.8),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        tab_one.next_to(tab_one_titre, DOWN, buff=0.4)

        groupe_tab_one = VGroup(tab_one_titre, tab_one)
        _fit(groupe_tab_one, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Par exemple, C-H-3, C-O, C-H-3 se nomme propan-2-one, "
                "aussi appelée acétone. Et C-H-3, C-O, C-H-2, C-H-3 se "
                "nomme butan-2-one."
            )
        ) as tracker:
            self.play(FadeIn(tab_one_titre))
            self.play(FadeIn(tab_one))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab_one))

        # --- À retenir + piège : distinguer aldéhyde et cétone ----------------------
        distinction = warning_box(
            VGroup(
                Text(
                    "Aldéhyde : carbonyle en bout de chaîne, avec un H\n"
                    "→ R-CHO. Suffixe -al, sans indice.",
                    font_size=21,
                ),
                Text(
                    "Cétone : carbonyle entre deux carbones, jamais de H\n"
                    "→ R₁-CO-R₂. Suffixe -one, AVEC indice.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.35, aligned_edge=LEFT),
            box_width=11.5,
        )
        distinction.next_to(titre, DOWN, buff=0.4)
        _fit(distinction, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons la différence essentielle. Dans un aldéhyde, le "
                "groupe carbonyle est en bout de chaîne et porte encore un "
                "atome d'hydrogène : on le nomme avec le suffixe -al, "
                "jamais d'indice. Dans une cétone, le groupe carbonyle est "
                "entre deux carbones et ne porte jamais d'hydrogène : on la "
                "nomme avec le suffixe -one, toujours accompagné d'un "
                "indice de position."
            )
        ) as tracker:
            self.play(FadeIn(distinction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(distinction), FadeOut(titre))
