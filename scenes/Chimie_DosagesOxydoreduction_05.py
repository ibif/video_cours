"""
scenes/Chimie_DosagesOxydoreduction_05.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 05.

§ L'iodométrie : réactifs, dosage direct du diiode. Couples I2/I- (E°=0,54V)
et S4O6^2-/S2O3^2- (E°=0,09V), équation-bilan I2+2S2O3^2- → 2I-+S4O6^2-.
Observation des couleurs (brun → jaune pâle, ajout empois d'amidon → bleu-
violet → décoloration brutale à l'équivalence). Définition indicateur
coloré. Relation à l'équivalence n(I2)=n(S2O3^2-)/2. Exemple résolu 2 :
dosage du Lugol, C(I2)=2,0×10⁻² mol/L.
Source : 1ereC/Chimie.pdf, chapitre 12, pages 117-118.
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
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class IodometrieDirecte(NotionScene):
    def construct(self):
        titre = scene_title("12.5 L'iodométrie : dosage direct du diiode")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------------------
        intro = Text(
            _wrap(
                "Après la manganimétrie, découvrons une deuxième grande "
                "famille de dosages redox : l'iodométrie, qui repose sur "
                "le couple du diiode.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Après la manganimétrie, découvrons une deuxième grande "
                "famille de dosages d'oxydoréduction : l'iodométrie, qui "
                "repose sur le couple du diiode et sur son dosage par les "
                "ions thiosulfate."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : les deux couples --------------------------------------------
        entete_couples = Text("Les deux couples oxydant/réducteur en jeu", font_size=22, color=YELLOW, weight="BOLD")
        entete_couples.next_to(titre, DOWN, buff=0.35)

        couple1 = MathTex(r"I_2/I^- \quad (E^\circ = 0{,}54\ V)", font_size=28, color=WHITE)
        couple2 = MathTex(r"S_4O_6^{2-}/S_2O_3^{2-} \quad (E^\circ = 0{,}09\ V)", font_size=28, color=WHITE)
        note = Text(
            _wrap(
                "Le diiode I₂ (oxydant) oxyde totalement l'ion thiosulfate "
                "S₂O₃²⁻ (réducteur) en ion tétrathionate S₄O₆²⁻.",
                width=50,
            ),
            font_size=19,
            color=WHITE,
        )
        couples = VGroup(couple1, couple2, note).arrange(DOWN, buff=0.35)
        couples.next_to(entete_couples, DOWN, buff=0.35)
        groupe_couples = VGroup(entete_couples, couples)
        _fit(groupe_couples, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Deux couples oxydant-réducteur sont en jeu. D'une part, "
                "le couple diiode sur ion iodure, I-2 sur I moins, de "
                "potentiel standard zéro virgule cinquante-quatre volt. "
                "D'autre part, le couple ion tétrathionate sur ion "
                "thiosulfate, S-4-O-6 deux moins sur S-2-O-3 deux moins, "
                "de potentiel standard zéro virgule zéro neuf volt. Le "
                "diiode, oxydant, oxyde donc totalement l'ion thiosulfate, "
                "réducteur, en ion tétrathionate."
            )
        ) as tracker:
            self.play(FadeIn(entete_couples))
            self.play(Write(couple1))
            self.play(Write(couple2))
            self.play(FadeIn(note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_couples))

        equation = MathTex(
            r"I_2 + 2\,S_2O_3^{2-} \longrightarrow 2\,I^- + S_4O_6^{2-}",
            font_size=30, color=YELLOW,
        )
        equation.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'équation-bilan de ce dosage s'écrit : I-2, plus deux "
                "S-2-O-3 deux moins, donne deux I moins, plus S-4-O-6 "
                "deux moins. Retenons bien le coefficient deux devant le "
                "thiosulfate : il faut deux ions thiosulfate pour "
                "consommer une molécule de diiode."
            )
        ) as tracker:
            self.play(Write(equation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation))

        # --- Raisonnement : observation des couleurs + indicateur coloré ---------------
        entete_couleurs = Text("Observation des couleurs et indicateur", font_size=22, color=YELLOW, weight="BOLD")
        entete_couleurs.next_to(titre, DOWN, buff=0.35)

        obs = _bullets(
            [
                "Sans indicateur : la solution de diiode, brune, "
                "s'éclaircit progressivement vers un jaune pâle au fur "
                "et à mesure du versement de thiosulfate.",
                "Juste avant l'équivalence (jaune pâle), on ajoute "
                "l'empois d'amidon : la solution devient bleu-violet "
                "(complexe amidon-diiode), très sensible.",
                "À l'équivalence : décoloration BRUTALE et totale (le "
                "bleu-violet disparaît d'un coup).",
            ],
            font_size=19,
            width=54,
        )
        obs.next_to(entete_couleurs, DOWN, buff=0.3)
        groupe_obs = VGroup(entete_couleurs, obs)
        _fit(groupe_obs, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Observons les couleurs pendant ce dosage. Sans "
                "indicateur, la solution de diiode, brune, s'éclaircit "
                "progressivement vers un jaune pâle, au fur et à mesure "
                "du versement de thiosulfate. Juste avant l'équivalence, "
                "quand la teinte devient jaune pâle, on ajoute l'empois "
                "d'amidon : la solution devient alors bleu-violet, "
                "couleur du complexe formé entre l'amidon et le diiode "
                "restant, une coloration très sensible. À l'équivalence, "
                "la décoloration est brutale et totale : le bleu-violet "
                "disparaît d'un coup."
            )
        ) as tracker:
            self.play(FadeIn(entete_couleurs))
            self.play(FadeIn(obs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_obs))

        def_indicateur = definition_box(
            Text(
                _wrap(
                    "Un indicateur coloré est une espèce chimique dont la "
                    "couleur change nettement au voisinage de "
                    "l'équivalence, permettant de la repérer sans "
                    "ambiguïté (ex : empois d'amidon avec le diiode).",
                    width=48,
                ),
                font_size=21,
            ),
        )
        def_indicateur.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la définition générale : un indicateur coloré "
                "est une espèce chimique dont la couleur change "
                "nettement au voisinage de l'équivalence, ce qui permet "
                "de la repérer sans ambiguïté. L'empois d'amidon, avec le "
                "diiode, en est l'exemple emblématique."
            )
        ) as tracker:
            self.play(FadeIn(def_indicateur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_indicateur))

        # --- Relation à l'équivalence ----------------------------------------------------
        relation = MathTex(
            r"n(I_2) = \dfrac{n(S_2O_3^{2-})}{2}",
            font_size=32, color=YELLOW,
        )
        relation.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "D'après l'équation-bilan, à l'équivalence, la quantité "
                "de matière de diiode est égale à la moitié de la "
                "quantité de matière de thiosulfate versée : n de I-2 "
                "égale n de S-2-O-3 deux moins, sur deux."
            )
        ) as tracker:
            self.play(Write(relation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(relation))

        # --- Exemple résolu 2 : dosage du Lugol ------------------------------------------
        entete_ex = Text("Exemple résolu 2 — Dosage du Lugol", font_size=22, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.35)

        enonce_ex = Text(
            _wrap(
                "On dose 10,0 mL de Lugol (solution de diiode) par une "
                "solution de thiosulfate de sodium à 0,10 mol/L. "
                "L'équivalence est obtenue pour Veq = 4,0 mL. Calculer "
                "C(I₂).",
                width=50,
            ),
            font_size=18,
            color=WHITE,
        )

        calcul = example_box(
            VGroup(
                MathTex(r"n(S_2O_3^{2-}) = 0{,}10\times 4{,}0\times 10^{-3} = 4{,}0\times 10^{-4}\ \text{mol}", font_size=22, color="#1A1A1A"),
                MathTex(r"n(I_2) = \dfrac{4{,}0\times 10^{-4}}{2} = 2{,}0\times 10^{-4}\ \text{mol}", font_size=22, color="#1A1A1A"),
                MathTex(r"C(I_2) = \dfrac{2{,}0\times 10^{-4}}{10{,}0\times 10^{-3}} = 2{,}0\times 10^{-2}\ \text{mol/L}", font_size=23, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25),
            box_width=11.5,
        )

        bloc_ex = VGroup(enonce_ex, calcul).arrange(DOWN, buff=0.3)
        bloc_ex.next_to(entete_ex, DOWN, buff=0.3)
        groupe_ex = VGroup(entete_ex, bloc_ex)
        _fit(groupe_ex, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Traitons un exemple résolu : le dosage du Lugol, une "
                "solution de diiode utilisée en pharmacie. On dose dix "
                "millilitres de Lugol par une solution de thiosulfate de "
                "sodium à zéro virgule un mol par litre, l'équivalence "
                "étant obtenue pour un volume versé de quatre "
                "millilitres. On calcule d'abord la quantité de "
                "thiosulfate versée : zéro virgule un fois quatre fois "
                "dix puissance moins trois, soit quatre fois dix "
                "puissance moins quatre mole. On en déduit la quantité "
                "de diiode, moitié de cette valeur, soit deux fois dix "
                "puissance moins quatre mole. En divisant par le volume "
                "de Lugol, dix millilitres, on obtient la concentration "
                "en diiode : deux virgule zéro fois dix puissance moins "
                "deux mol par litre."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(enonce_ex))
            self.play(Write(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_ex))

        # --- Piège à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne jamais ajouter l'empois d'amidon trop tôt : en "
                    "présence de beaucoup de diiode, le complexe "
                    "bleu-violet formé se décompose mal et retarde la "
                    "décoloration nette. On l'ajoute seulement quand la "
                    "teinte devient jaune pâle, juste avant l'équivalence.",
                    width=48,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : il ne faut jamais "
                "ajouter l'empois d'amidon trop tôt dans le dosage. En "
                "présence de beaucoup de diiode, le complexe bleu-violet "
                "formé se décompose mal, ce qui retarde et rend flou le "
                "repérage de l'équivalence. On ajoute donc l'empois "
                "d'amidon seulement lorsque la teinte devient jaune pâle, "
                "juste avant l'équivalence attendue."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
