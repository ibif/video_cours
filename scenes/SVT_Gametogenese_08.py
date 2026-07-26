"""
scenes/SVT_Gametogenese_08.py — Chapitre 3 (1ereD, SVT), scène 08.

§ 3.6 Comparaison des deux gamétogenèses et contrôle hormonal — tableau
comparatif, propriété FSH/LH, remarque du rétrocontrôle, méthode d'analyse
d'un document de gamétogénèse, application directe (élevage, AMP).
Source : 1ereD/SVT.pdf, pages 43-45.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ComparaisonEtControleHormonal(NotionScene):
    def construct(self):
        titre = scene_title("3.6 — Comparaison et contrôle hormonal")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : tableau comparatif -------------------------------------
        entete_tab = Text("3.6.1 — Tableau comparatif", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        sperma_col = VGroup(
            Text("Spermatogenèse", font_size=20, color=BLUE, weight="BOLD"),
            Text("Lieu : tubes séminifères", font_size=15, color=WHITE),
            Text("Gamète : spermatozoïde", font_size=15, color=WHITE),
            Text("Continue, dès la puberté", font_size=15, color=WHITE),
            Text("Cycle : ~70 jours", font_size=15, color=WHITE),
            Text("Divisions égales", font_size=15, color=WHITE),
            Text("4 gamètes / spermatocyte I", font_size=15, color=WHITE),
            Text("Des millions/jour", font_size=15, color=WHITE),
            Text("60 µm, mobile (flagelle)", font_size=15, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)

        ovo_col = VGroup(
            Text("Ovogenèse", font_size=20, color=ORANGE, weight="BOLD"),
            Text("Lieu : follicules de l'ovaire", font_size=15, color=WHITE),
            Text("Gamète : ovule", font_size=15, color=WHITE),
            Text("Cyclique, débute avant la naissance", font_size=15, color=WHITE),
            Text("Cycle : 13 à 50 ans (blocages)", font_size=15, color=WHITE),
            Text("Divisions inégales (glob. polaires)", font_size=15, color=WHITE),
            Text("1 ovule / ovocyte I", font_size=15, color=WHITE),
            Text("1 ovocyte / cycle", font_size=15, color=WHITE),
            Text("120 µm, immobile, réserves", font_size=15, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)

        tableau = VGroup(sperma_col, ovo_col).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        tableau.scale(0.95)

        with self.voiceover(
            text=(
                "Comparons les deux gamétogenèses. La spermatogenèse a "
                "lieu dans les tubes séminifères des testicules, produit le "
                "spermatozoïde, est continue dès la puberté, avec un cycle "
                "d'environ soixante-dix jours, des divisions égales, quatre "
                "gamètes par spermatocyte premier, des millions par jour, "
                "et un gamète de soixante micromètres, mobile grâce à son "
                "flagelle. L'ovogenèse a lieu dans les follicules de "
                "l'ovaire, produit l'ovule, est cyclique et débute avant la "
                "naissance, avec un déroulement échelonné de treize à "
                "cinquante ans et des blocages, des divisions inégales avec "
                "globules polaires, un seul ovule par ovocyte premier, un "
                "seul ovocyte libéré par cycle, et un gamète de cent vingt "
                "micromètres, immobile et riche en réserves. Les deux "
                "processus partagent néanmoins le même plan d'ensemble : "
                "multiplication, accroissement, maturation par méiose, "
                "différenciation, et produisent des gamètes haploïdes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(sperma_col))
            self.play(FadeIn(ovo_col))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Raisonnement : le contrôle hormonal --------------------------------
        entete_hormones = Text("3.6.2 — Le contrôle hormonal", font_size=24, color=YELLOW, weight="BOLD")
        entete_hormones.next_to(titre, DOWN, buff=0.45)

        hypothalamus = Text("Hypothalamus", font_size=20, color=WHITE, weight="BOLD")
        hypophyse = Text("Hypophyse", font_size=20, color=WHITE, weight="BOLD")
        gonades = Text("Gonades\n(testicules / ovaires)", font_size=18, color=WHITE, weight="BOLD")
        chaine = VGroup(hypothalamus, hypophyse, gonades).arrange(RIGHT, buff=1.3)
        chaine.next_to(entete_hormones, DOWN, buff=0.6)

        fleche1 = Arrow(hypothalamus.get_right(), hypophyse.get_left(), buff=0.1, color=WHITE)
        fleche2 = Arrow(hypophyse.get_right(), gonades.get_left(), buff=0.1, color=WHITE)
        label_fleche2 = Text("FSH, LH", font_size=16, color=YELLOW)
        label_fleche2.next_to(fleche2, UP, buff=0.1)

        schema_axe = VGroup(chaine, fleche1, fleche2, label_fleche2)

        with self.voiceover(
            text=(
                "La gamétogénèse est commandée par des hormones sécrétées "
                "par le cerveau : l'hypothalamus stimule l'hypophyse, "
                "glande située à la base du crâne, qui libère alors deux "
                "hormones dites gonadotrophines, car elles agissent sur "
                "les gonades, la FSH et la LH."
            )
        ) as tracker:
            self.play(FadeIn(entete_hormones))
            self.play(FadeIn(chaine))
            self.play(FadeIn(fleche1), FadeIn(fleche2), FadeIn(label_fleche2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_hormones), FadeOut(schema_axe))

        # --- Propriété : rôles de FSH et LH --------------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "FSH (folliculo-stimulante) : chez l'homme, stimule "
                    "les cellules de Sertoli (spermatogenèse) ; chez la "
                    "femme, provoque la croissance des follicules "
                    "(folliculogenèse). LH (lutéinisante) : chez l'homme, "
                    "stimule les cellules de Leydig (testostérone) ; chez "
                    "la femme, un pic de LH en milieu de cycle déclenche "
                    "l'ovulation.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        propriete.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Précisons le rôle de chaque hormone. La FSH, hormone "
                "folliculo-stimulante : chez l'homme, elle stimule les "
                "cellules de Sertoli, donc le déroulement de la "
                "spermatogenèse ; chez la femme, elle provoque la "
                "croissance des follicules ovariens, la folliculogenèse. "
                "La LH, hormone lutéinisante : chez l'homme, elle stimule "
                "les cellules de Leydig, qui sécrètent la testostérone, "
                "indispensable à la maturation des spermatozoïdes ; chez la "
                "femme, un pic de LH en milieu de cycle déclenche "
                "l'ovulation."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Remarque : rétrocontrôle hormonal -----------------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "En retour, les hormones des gonades (testostérone "
                    "chez l'homme, œstrogènes et progestérone chez la "
                    "femme) freinent l'hypophyse : un rétrocontrôle en "
                    "boucle fermée qui stabilise la production. Ce "
                    "mécanisme explique aussi l'action des contraceptifs "
                    "hormonaux, qui bloquent l'ovulation en trompant ce "
                    "rétrocontrôle.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        remarque.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "En retour, les hormones produites par les gonades, la "
                "testostérone chez l'homme, les œstrogènes et la "
                "progestérone chez la femme, freinent l'hypophyse : c'est "
                "un contrôle en boucle fermée, le rétrocontrôle, qui "
                "maintient la production à un niveau stable. Ce mécanisme "
                "explique aussi l'action des contraceptifs hormonaux, qui "
                "bloquent l'ovulation en trompant ce rétrocontrôle."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Exemple / méthode traité : analyser un document -----------------------
        methode = method_box(
            Text(
                _wrap(
                    "Face à un document de gamétogénèse : 1) Repère la "
                    "gonade (tubes séminifères ou follicules). 2) Classe "
                    "les cellules de la périphérie vers la lumière. 3) "
                    "Attribue les formules chromosomiques (2n avant "
                    "méiose I, n après ; 2 chromatides avant méiose II, 1 "
                    "après). 4) Compte le rendement (1→4 ou 1→1). 5) "
                    "Conclus sur le double rôle de la méiose : réduction "
                    "et brassage.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = methode.get_top()[1] - _bas_visible
        if methode.height > _hauteur_dispo:
            methode.scale(_hauteur_dispo / methode.height, about_point=methode.get_top())

        with self.voiceover(
            text=(
                "Voici une méthode en cinq étapes pour analyser un document "
                "de gamétogénèse. Un : repère la gonade, tubes séminifères "
                "du testicule ou follicules de l'ovaire. Deux : classe les "
                "cellules de la périphérie vers la lumière, dans le "
                "testicule, spermatogonies, spermatocytes, spermatides, "
                "spermatozoïdes. Trois : attribue les formules "
                "chromosomiques, deux n avant la méiose un, n après, "
                "chromosomes à deux chromatides avant la méiose deux, à une "
                "chromatide après. Quatre : compte le rendement, un "
                "spermatocyte premier donne quatre spermatozoïdes, un "
                "ovocyte premier donne un ovule. Cinq : conclus en "
                "rappelant le double rôle de la méiose, réduction du nombre "
                "de chromosomes et brassage du patrimoine héréditaire."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- À retenir : application directe -----------------------------------
        application = _bullets(
            [
                "Élevage : les stations d'insémination artificielle "
                "conservent la semence de taureaux reproducteurs — un "
                "seul éjaculat peut féconder des centaines de vaches.",
                "Médecine : les centres d'AMP d'Abidjan aident les "
                "couples infertiles ; le spermogramme évalue la "
                "spermatogenèse, la FIV réunit les gamètes en laboratoire.",
            ],
            font_size=21,
            width=52,
        )
        entete_appli = Text("Application directe en Côte d'Ivoire", font_size=23, color=YELLOW, weight="BOLD")
        entete_appli.next_to(titre, DOWN, buff=0.45)
        application.next_to(entete_appli, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'étude de la gamétogénèse a des applications directes en "
                "Côte d'Ivoire. En élevage, les stations d'insémination "
                "artificielle, par exemple pour l'amélioration des races "
                "bovines laitières, prélèvent et conservent la semence de "
                "taureaux reproducteurs, dont un seul éjaculat, riche de "
                "milliards de spermatozoïdes, peut féconder des centaines "
                "de vaches. En médecine, les centres d'assistance médicale "
                "à la procréation d'Abidjan aident les couples confrontés à "
                "l'infertilité : l'analyse du sperme, le spermogramme, "
                "évalue la qualité de la spermatogenèse, et la fécondation "
                "in vitro réunit en laboratoire les gamètes des deux "
                "partenaires."
            )
        ) as tracker:
            self.play(FadeIn(entete_appli))
            self.play(FadeIn(application))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_appli), FadeOut(application))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas FSH et LH : la FSH fait grandir/mûrir "
                    "les cellules germinales (Sertoli, follicules), la LH "
                    "déclenche/entretient une sécrétion hormonale "
                    "(testostérone via Leydig) ou l'ovulation. Et le "
                    "rétrocontrôle est un frein (hormones des gonades → "
                    "hypophyse), pas un simple aller simple.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre FSH et LH : la FSH fait "
                "grandir et mûrir les cellules germinales, cellules de "
                "Sertoli ou follicules, tandis que la LH déclenche ou "
                "entretient une sécrétion hormonale, la testostérone via "
                "les cellules de Leydig, ou déclenche l'ovulation. Et "
                "n'oublie pas que le rétrocontrôle est un frein, des "
                "hormones des gonades vers l'hypophyse, et non un simple "
                "aller simple de l'hypophyse vers les gonades."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
