"""
scenes/SVT_Monohybridisme_03.py — Chapitre 4 (1ereD, SVT), scène 03.

§ 4.2 Génotype, phénotype, homozygotie et hétérozygotie (4.2.1-4.2.3) :
définitions génotype/phénotype, homozygote/hétérozygote, vocabulaire
P/F1/F2, dominance/récessivité appliquées au maïs, exemple du génotype au
phénotype (4 plants), attention phénotype dominant cache le génotype.
Source : 1ereD/SVT.pdf, pages 49-51.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class GenotypePhenotypeDominance(NotionScene):
    def construct(self):
        titre = scene_title("4.2 — Génotype, phénotype, dominance")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : génotype et phénotype -------------------------------------
        definition_geno = definition_box(
            Text(
                _wrap(
                    "Le génotype d'un individu est l'ensemble des allèles "
                    "qu'il possède pour le(s) gène(s) étudié(s). Il n'est "
                    "pas visible directement : on l'écrit avec des lettres "
                    "(ex. V/V, V/v, v/v).",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition_geno.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le génotype d'un individu est l'ensemble des allèles qu'il "
                "possède pour le ou les gènes étudiés. Il n'est pas visible "
                "directement : on l'écrit avec des lettres, par exemple V "
                "sur V, V sur v, ou v sur v."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_geno))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_geno))

        definition_pheno = definition_box(
            Text(
                _wrap(
                    "Le phénotype d'un individu est l'ensemble des "
                    "caractères observables résultant de l'expression de "
                    "son génotype. On l'écrit entre crochets : [V] "
                    "= grains violets, [v] = grains blancs.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition_pheno.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le phénotype d'un individu est l'ensemble des caractères "
                "observables qui résultent de l'expression de son génotype. "
                "On l'écrit entre crochets. Pour le maïs : crochet V "
                "signifie grains violets, crochet v signifie grains blancs. "
                "À retenir : le phénotype est ce que l'on voit, le génotype "
                "est ce qui est écrit dans les chromosomes."
            )
        ) as tracker:
            self.play(FadeIn(definition_pheno))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_pheno))

        # --- Animation du raisonnement : homozygote/hétérozygote, P/F1/F2 ------
        definition_homo = definition_box(
            Text(
                _wrap(
                    "Homozygote : deux allèles identiques (V/V ou v/v) — "
                    "dit aussi de lignée pure. Hétérozygote : deux allèles "
                    "différents (V/v) — dit aussi hybride.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition_homo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un individu est homozygote pour un gène lorsqu'il possède "
                "deux allèles identiques de ce gène, V sur V ou v sur v. On "
                "dit aussi qu'il est de lignée pure : croisé avec un "
                "individu identique à lui-même, il donne toujours des "
                "descendants identiques. Un individu est hétérozygote "
                "lorsqu'il possède deux allèles différents, V sur v. On dit "
                "aussi que c'est un hybride."
            )
        ) as tracker:
            self.play(FadeIn(definition_homo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_homo))

        vocab_titre = Text("Le langage des croisements", font_size=27, color=YELLOW, weight="BOLD")
        vocab_titre.next_to(titre, DOWN, buff=0.5)

        vocab = _bullets(
            [
                "Monohybridisme : transmission d'un seul caractère.",
                "P : génération parentale (les deux individus croisés "
                "au départ).",
                "F1 : première génération filiale (descendants de P).",
                "F2 : deuxième génération filiale (F1 x F1).",
                "Le symbole « x » se lit « croisé avec ».",
            ],
            font_size=22,
            width=54,
        )
        vocab.next_to(vocab_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le vocabulaire des croisements. Monohybridisme : "
                "étude de la transmission d'un seul caractère. P : "
                "génération parentale, les deux individus croisés au "
                "départ. F1 : première génération filiale, les descendants "
                "directs des parents P. F2 : deuxième génération filiale, "
                "obtenue en croisant les individus de la F1 entre eux. Le "
                "symbole « x », placé entre deux génotypes, signifie « "
                "croisé avec »."
            )
        ) as tracker:
            self.play(FadeIn(vocab_titre))
            self.play(FadeIn(vocab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vocab_titre), FadeOut(vocab))

        definition_dom = definition_box(
            Text(
                _wrap(
                    "Un allèle dominant s'exprime même en un seul "
                    "exemplaire (hétérozygote) — noté en majuscule. Un "
                    "allèle récessif ne s'exprime qu'en deux exemplaires "
                    "(homozygote) — noté en minuscule.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition_dom.next_to(titre, DOWN, buff=0.5)

        bilan_dom = MathTex(
            r"V/V \to [V] \qquad V/v \to [V] \qquad v/v \to [v]",
            font_size=28,
            color=YELLOW,
        )
        bilan_dom.next_to(definition_dom, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un allèle est dominant lorsqu'il s'exprime dans le "
                "phénotype même lorsqu'il n'est présent qu'en un seul "
                "exemplaire, chez l'hétérozygote. On le note par une "
                "majuscule. Un allèle est récessif lorsqu'il ne s'exprime "
                "que lorsqu'il est présent en deux exemplaires, chez "
                "l'homozygote. On le note par une minuscule. Chez le maïs : "
                "l'allèle V est dominant, un plant V sur V a des grains "
                "violets, exactement comme un plant V sur v. L'allèle v est "
                "récessif : seul un plant v sur v a des grains blancs."
            )
        ) as tracker:
            self.play(FadeIn(definition_dom))
            self.play(Write(bilan_dom))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_dom), FadeOut(bilan_dom))

        # --- Exemple traité : du génotype au phénotype (4 plants) --------------
        exemple = example_box(
            Text(
                _wrap(
                    "4 plants de maïs à Yamoussoukro : plant 1 V/V, plant "
                    "2 V/v, plant 3 v/v, plant 4 V/V. Résultat : plants "
                    "1, 2 et 4 -> [V] violets (l'allèle dominant "
                    "s'exprime) ; plant 3 -> [v] blanc (v en double "
                    "exemplaire). 3 génotypes -> 2 phénotypes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans un champ de la région de Yamoussoukro, on prélève "
                "quatre plants de maïs dont l'analyse donne les génotypes "
                "suivants : plant un, V sur V ; plant deux, V sur v ; plant "
                "trois, v sur v ; plant quatre, V sur V. Quels phénotypes "
                "observe-t-on ? Le plant un possède deux allèles V : "
                "phénotype violet. Le plant deux possède un allèle V "
                "dominant et un allèle v récessif : seul le dominant "
                "s'exprime, phénotype violet. Le plant trois ne possède "
                "aucun allèle V : l'allèle v s'exprime, phénotype blanc. Le "
                "plant quatre est comme le plant un : phénotype violet. "
                "Conclusion : les plants un, deux et quatre présentent des "
                "grains violets ; seul le plant trois présente des grains "
                "blancs. On remarque que trois génotypes différents ne "
                "donnent que deux phénotypes différents."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)

        retenir = _bullets(
            [
                "Génotype = allèles possédés (écrit avec des lettres).",
                "Phénotype = ce qu'on observe (écrit entre crochets).",
                "Homozygote = lignée pure ; hétérozygote = hybride.",
                "Allèle dominant = s'exprime même en un exemplaire ; "
                "allèle récessif = s'exprime en deux exemplaires.",
            ],
            font_size=22,
            width=54,
        )
        retenir.next_to(entete_retenir, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de cette section. Le génotype, ce "
                "sont les allèles possédés, écrit avec des lettres. Le "
                "phénotype, c'est ce qu'on observe, écrit entre crochets. "
                "Homozygote signifie lignée pure ; hétérozygote signifie "
                "hybride. Un allèle dominant s'exprime même en un seul "
                "exemplaire ; un allèle récessif ne s'exprime qu'en deux "
                "exemplaires."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter : le phénotype dominant cache le génotype ----------
        piege = warning_box(
            Text(
                _wrap(
                    "Un phénotype récessif révèle le génotype à coup sûr "
                    "(v/v). Mais un phénotype dominant NE permet PAS de "
                    "trancher : l'individu peut être V/V ou V/v. Écrire "
                    "« violet donc V/V » est faux dans deux cas sur trois "
                    "en F2 ! Il faut un croisement-test pour trancher "
                    "(§ 4.5).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.3,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention : un individu de phénotype récessif est "
                "forcément homozygote v sur v, sans exception. En revanche, "
                "un individu de phénotype dominant peut être soit V sur V, "
                "soit V sur v : son apparence ne permet pas de trancher. "
                "Beaucoup d'élèves écrivent « grains violets, donc génotype "
                "V sur V » : c'est impossible à savoir au seul regard du "
                "phénotype — dans une F2, c'est même faux deux fois sur "
                "trois ! Pour connaître le génotype d'un individu de "
                "phénotype dominant, il faudra réaliser un croisement-test, "
                "que nous verrons au paragraphe quatre point cinq."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
