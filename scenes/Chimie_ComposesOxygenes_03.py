"""
scenes/Chimie_ComposesOxygenes_03.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 03.

§ Nomenclature des alcools (règles UICPA, suffixe -ol) + exemple résolu 2
(2-méthylbutan-1-ol) + propriétés physiques (miscibilité, Téb élevée par
liaison hydrogène, toxicité du méthanol).
Source : 1ereC/Chimie.pdf, chapitre 6, pages 56-58.
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
from shapes.boxes import corrige_box, exercise_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class NomenclatureEtProprietesPhysiques(NotionScene):
    def construct(self):
        titre = scene_title("Nomenclature des alcools et propriétés physiques")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : la méthode de nomenclature ---------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Nommer un alcool : 1) repérer la chaîne principale, "
                    "celle qui contient le carbone fonctionnel ; "
                    "2) numéroter la chaîne de façon à donner au carbone "
                    "fonctionnel l'indice le plus petit possible ; "
                    "3) remplacer le « e » final du nom de l'alcane "
                    "correspondant par le suffixe « -ol », précédé de "
                    "l'indice de position du groupe -OH.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        methode.next_to(titre, DOWN, buff=0.4)
        _fit(methode, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pour nommer un alcool, on applique trois règles. Un, on "
                "repère la chaîne principale, celle qui contient le "
                "carbone fonctionnel. Deux, on numérote cette chaîne de "
                "façon à donner au carbone fonctionnel l'indice le plus "
                "petit possible — c'est prioritaire sur tout autre "
                "substituant. Trois, on remplace le e final du nom de "
                "l'alcane correspondant par le suffixe -ol, précédé de "
                "l'indice de position du groupe hydroxyle."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Raisonnement : tableau d'exemples ------------------------------------
        entete_tab = Text("Exemples", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        lignes = VGroup(
            VGroup(MathTex(r"CH_3-OH", font_size=26), Text("méthanol", font_size=22)).arrange(RIGHT, buff=0.8),
            VGroup(MathTex(r"CH_3-CH_2-OH", font_size=26), Text("éthanol", font_size=22)).arrange(RIGHT, buff=0.8),
            VGroup(MathTex(r"CH_3-CH_2-CH_2-OH", font_size=26), Text("propan-1-ol", font_size=22)).arrange(RIGHT, buff=0.8),
            VGroup(MathTex(r"CH_3-CH(OH)-CH_3", font_size=26), Text("propan-2-ol", font_size=22)).arrange(RIGHT, buff=0.8),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        lignes.next_to(entete_tab, DOWN, buff=0.4)

        groupe_tab = VGroup(entete_tab, lignes)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici quelques exemples. C-H-3-O-H se nomme méthanol. "
                "C-H-3, C-H-2, O-H se nomme éthanol. C-H-3, C-H-2, C-H-2, "
                "O-H se nomme propan-1-ol, le groupe hydroxyle étant sur le "
                "premier carbone. C-H-3, C-H parenthèse O-H fermée "
                "parenthèse, C-H-3 se nomme propan-2-ol, le groupe "
                "hydroxyle étant sur le carbone central."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(lignes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Exemple traité : exemple résolu 2 (2-méthylbutan-1-ol) --------------
        enonce = exercise_box(
            MathTex(r"CH_3-CH_2-CH(CH_3)-CH_2-OH", font_size=28, color="#1A1A1A"),
            box_width=10.0,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : nommons l'alcool de formule "
                "semi-développée C-H-3, C-H-2, C-H parenthèse C-H-3 fermée "
                "parenthèse, C-H-2, O-H."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        corrige = corrige_box(
            VGroup(
                Text(
                    "Chaîne principale de 4 C (butane), numérotée pour donner\n"
                    "au carbone fonctionnel l'indice le plus petit : 1.\n"
                    "Le méthyle est alors en position 2.",
                    font_size=21,
                ),
                Text("2-méthylbutan-1-ol", font_size=28, weight="BOLD"),
            ).arrange(DOWN, buff=0.35),
            box_width=10.5,
        )
        corrige.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La chaîne principale compte quatre atomes de carbone : "
                "c'est un dérivé du butane. On numérote de façon à donner "
                "au carbone fonctionnel, celui qui porte O-H, l'indice le "
                "plus petit, c'est-à-dire un, en partant de la droite. Le "
                "groupe méthyle se retrouve alors en position deux. Le nom "
                "est donc deux-méthylbutan-1-ol."
            )
        ) as tracker:
            self.play(FadeIn(corrige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige))

        # --- À retenir : propriétés physiques -------------------------------------
        proprietes = property_box(
            Text(
                _wrap(
                    "Les alcools à petite chaîne (méthanol, éthanol, "
                    "propanol) sont miscibles à l'eau en toutes "
                    "proportions, grâce aux liaisons hydrogène entre le "
                    "groupe -OH et l'eau. Leur température d'ébullition "
                    "est nettement plus élevée que celle de l'alcane "
                    "correspondant, pour la même raison.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        proprietes.next_to(titre, DOWN, buff=0.4)
        _fit(proprietes, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Passons aux propriétés physiques. Les alcools à petite "
                "chaîne, comme le méthanol, l'éthanol ou le propanol, sont "
                "miscibles à l'eau en toutes proportions, grâce aux "
                "liaisons hydrogène qui s'établissent entre leur groupe "
                "hydroxyle et les molécules d'eau. Pour cette même raison, "
                "leur température d'ébullition est nettement plus élevée "
                "que celle de l'alcane possédant le même nombre de "
                "carbones."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Piège à éviter : toxicité du méthanol --------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le méthanol est un poison violent : ingéré, même en "
                    "petite quantité, il provoque cécité et peut être "
                    "mortel. Ne jamais le confondre avec l'éthanol, présent "
                    "dans les boissons — un alcool frelaté au méthanol est "
                    "extrêmement dangereux.",
                    width=48,
                ),
                font_size=22,
                color=RED,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention, un point de sécurité essentiel : le méthanol "
                "est un poison violent. Ingéré, même en petite quantité, "
                "il provoque la cécité et peut être mortel. Il ne faut "
                "jamais le confondre avec l'éthanol, celui des boissons : "
                "un alcool frelaté au méthanol est extrêmement dangereux "
                "pour la santé."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
