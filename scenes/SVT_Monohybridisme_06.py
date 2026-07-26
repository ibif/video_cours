"""
scenes/SVT_Monohybridisme_06.py — Chapitre 4 (1ereD, SVT), scène 06.

§ 4.5 Le croisement-test (test-cross) : définition et rôle du testeur, les
deux cas possibles, méthode d'exploitation en 3 étapes, exemple du bélier
de Korhogo, attention : le testeur est toujours homozygote récessif.
Source : 1ereD/SVT.pdf, pages 55-57.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class CroisementTest(NotionScene):
    def construct(self):
        titre = scene_title("4.5 — Le croisement-test (test-cross)")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : définition du croisement-test -----------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un croisement-test (ou test-cross) est le croisement "
                    "d'un individu de phénotype dominant dont on cherche "
                    "le génotype avec un individu de phénotype récessif "
                    "(nécessairement homozygote v/v), appelé le testeur.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un individu de phénotype dominant peut être V sur V ou V "
                "sur v : son apparence ne suffit pas à trancher. Le "
                "croisement-test, ou test-cross, résout ce problème : c'est "
                "le croisement d'un individu de phénotype dominant dont on "
                "cherche le génotype avec un individu de phénotype "
                "récessif, nécessairement homozygote v sur v. Cet individu "
                "v sur v est appelé le testeur : il ne fournit que des "
                "gamètes v, qui ne masquent rien — chaque descendant révèle "
                "donc l'allèle apporté par le parent testé."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : les 2 cas + méthode --------------------
        cas1 = MathTex(
            r"\text{Cas 1 : } V/V \;\times\; v/v \;\longrightarrow\; 100\%\,V/v \;\; ([V])",
            font_size=26,
            color=WHITE,
        )
        cas2 = MathTex(
            r"\text{Cas 2 : } V/v \;\times\; v/v \;\longrightarrow\; \tfrac{1}{2}\,V/v\,([V]) \;+\; \tfrac{1}{2}\,v/v\,([v])",
            font_size=26,
            color=WHITE,
        )
        cas = VGroup(cas1, cas2).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        cas.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Deux cas, et deux cas seulement, sont possibles. Cas un : "
                "le parent testé est homozygote V sur V. Il ne produit que "
                "des gamètes V. Tous les zygotes sont V sur v : la "
                "descendance est uniforme, cent pour cent de phénotype "
                "dominant. Cas deux : le parent testé est hétérozygote V "
                "sur v. Il produit un demi de gamètes V et un demi de "
                "gamètes v. La descendance compte un demi de V sur v, "
                "phénotype dominant, et un demi de v sur v, phénotype "
                "récessif : c'est une descendance hétérogène en deux "
                "parties égales."
            )
        ) as tracker:
            self.play(Write(cas1))
            self.play(Write(cas2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas))

        methode = method_box(
            Text(
                _wrap(
                    "1. Repérer le croisement d'un dominant avec un "
                    "récessif.\n"
                    "2. Regarder la descendance obtenue (effectif assez "
                    "grand).\n"
                    "3. Conclure : descendance uniforme (100% dominants) "
                    "-> parent testé V/V ; descendance 1/2-1/2 -> parent "
                    "testé V/v. (Un seul descendant récessif suffit à "
                    "prouver V/v.)",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la méthode pour exploiter un croisement-test. Étape "
                "un : repérer dans l'énoncé le croisement d'un individu de "
                "phénotype dominant avec un individu de phénotype récessif. "
                "Étape deux : regarder la descendance obtenue, sur un "
                "effectif assez grand. Étape trois : conclure. Une "
                "descendance uniforme, cent pour cent de dominants, "
                "signifie que le parent testé est homozygote V sur V ; une "
                "descendance en deux parties égales, un demi et un demi, "
                "signifie que le parent testé est hétérozygote V sur v. "
                "Raisonnement inverse possible : si l'on trouve un seul "
                "descendant de phénotype récessif, le parent testé a "
                "forcément fourni un allèle v, donc il est hétérozygote."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : le bélier de Korhogo -------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Bélier à laine rousse [R] (R dominant/r récessif) x "
                    "brebis blanches r/r : 24 agneaux nés, 24 roux, 0 "
                    "blanc. Si le bélier était R/r, on attendrait ~12 "
                    "agneaux blancs sur 24. Aucun agneau blanc -> le "
                    "bélier n'a fourni que des gamètes R -> génotype R/R "
                    "(lignée pure).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.3,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un éleveur de moutons Djallonké, près de Korhogo, possède "
                "un bélier à laine rousse qu'il veut utiliser comme "
                "reproducteur. Chez cette race, la laine rousse, allèle R "
                "dominant, domine la laine blanche, allèle r récessif. Pour "
                "savoir si le bélier est de lignée pure, l'éleveur le "
                "croise avec plusieurs brebis à laine blanche. Sur "
                "vingt-quatre agneaux nés, vingt-quatre ont la laine "
                "rousse. Quel est le génotype du bélier ? Le bélier est de "
                "phénotype dominant, roux : son génotype est soit R sur R, "
                "soit R sur r. Les brebis, de phénotype récessif, sont r "
                "sur r : c'est bien un croisement-test. Si le bélier était "
                "hétérozygote R sur r, on attendrait environ un demi "
                "d'agneaux blancs, soit environ douze sur vingt-quatre. Or "
                "aucun agneau blanc n'est né : les vingt-quatre agneaux "
                "sont roux. Chacun a reçu un allèle r de sa mère ; il est "
                "donc R sur r, et n'a pu recevoir du père qu'un allèle R. "
                "Le bélier n'a fourni que des gamètes R : il est très "
                "probablement homozygote R sur R, de lignée pure."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)

        retenir = _bullets(
            [
                "Le croisement-test révèle le génotype caché d'un "
                "individu de phénotype dominant.",
                "Descendance 100% dominante -> testé homozygote V/V.",
                "Descendance 1/2 dominante - 1/2 récessive -> testé "
                "hétérozygote V/v.",
            ],
            font_size=23,
            width=54,
        )
        retenir.next_to(entete_retenir, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Le croisement-test révèle le "
                "génotype caché d'un individu de phénotype dominant. Une "
                "descendance à cent pour cent dominante signifie que "
                "l'individu testé est homozygote V sur V. Une descendance "
                "moitié dominante, moitié récessive, signifie qu'il est "
                "hétérozygote V sur v."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter : le testeur est toujours homozygote récessif ------
        piege = warning_box(
            Text(
                _wrap(
                    "Le croisement-test n'a de sens qu'avec un testeur "
                    "doublement récessif (r/r). Croiser avec un R/R ne "
                    "prouverait rien, tous les descendants seraient "
                    "dominants dans les 2 cas. Et un seul agneau ne prouve "
                    "rien : plus l'effectif est grand, plus la conclusion "
                    "est sûre.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.3,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention : le croisement-test n'a de sens qu'avec un "
                "partenaire doublement récessif, r sur r. Si l'on croisait "
                "l'individu testé avec un R sur R, tous les descendants "
                "seraient dominants dans les deux cas, et l'on ne pourrait "
                "rien conclure. Autre précision : l'effectif compte — un "
                "seul agneau ne prouve rien ; plus la descendance est "
                "nombreuse, plus la conclusion est sûre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
