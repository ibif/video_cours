"""
scenes/Chimie_OxydoreductionSolutionAqueuse_06.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 06.

§ Autres exemples résolus d'équations bilan : exemple résolu 4 (dichromate
+ iodure, coloration orange→verte+brun), exemple résolu 5 (diiode +
thiosulfate, dosage iodométrique), exemple résolu 6 (fer III + cuivre
métal, gravure de circuits imprimés).
Source : 1ereC/Chimie.pdf, chapitre 9, pages 90-91.
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
from shapes.boxes import example_box, scene_title, warning_box


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


class AutresExemplesEquationBilan(NotionScene):
    def construct(self):
        titre = scene_title("9.6 Autres exemples résolus d'équations bilan")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : trois nouvelles réactions à équilibrer ------------------------
        intro = _bullets(
            [
                "Exemple résolu 4 : dichromate + ions iodure ;",
                "Exemple résolu 5 : diiode + thiosulfate (dosage iodométrique) ;",
                "Exemple résolu 6 : fer III + cuivre métal (gravure des circuits imprimés).",
            ],
            width=52,
        )
        intro.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Consolidons la méthode avec trois nouveaux exemples "
                "résolus, appliqués à des réactions très classiques : la "
                "réaction du dichromate avec les ions iodure, celle du "
                "diiode avec le thiosulfate, base du dosage iodométrique, "
                "et enfin celle du fer trois plus avec le cuivre métal, "
                "utilisée pour la gravure des circuits imprimés."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement / Exemple 4 : dichromate + iodure --------------------------
        entete4 = Text("Exemple résolu 4 — dichromate + ions iodure", font_size=21, color=YELLOW, weight="BOLD")
        entete4.next_to(titre, DOWN, buff=0.35)

        demi4a = MathTex(r"Cr_2O_7^{2-} + 14\,H^+ + 6\,e^- \rightarrow 2\,Cr^{3+} + 7\,H_2O", font_size=21, color=WHITE)
        demi4b = MathTex(r"2\,I^- \rightarrow I_2 + 2\,e^- \quad (\times 3)", font_size=21, color=WHITE)
        bilan4 = MathTex(
            r"Cr_2O_7^{2-} + 14\,H^+ + 6\,I^- \longrightarrow 2\,Cr^{3+} + 7\,H_2O + 3\,I_2",
            font_size=22, color=YELLOW,
        )
        observation4 = Text(
            "Observation : la couleur vire de l'orange (Cr₂O₇²⁻) au vert (Cr³⁺), avec apparition de diiode brun.",
            font_size=17, color=WHITE,
        )

        groupe4 = VGroup(entete4, demi4a, demi4b, bilan4, observation4).arrange(DOWN, buff=0.28)
        groupe4.next_to(titre, DOWN, buff=0.3)
        _fit(groupe4, titre.get_bottom()[1] - 0.3)
        groupe4.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple résolu quatre : le dichromate échange six "
                "électrons, l'iodure deux électrons pour former du diiode. "
                "Le plus petit commun multiple de six et deux est six : on "
                "multiplie la seconde demi-équation par trois. En "
                "additionnant et en simplifiant les électrons, on obtient "
                "l'équation bilan : ion dichromate, plus quatorze ions H "
                "plus, plus six ions iodure, donne deux ions chrome trois "
                "plus, plus sept molécules d'eau, plus trois molécules de "
                "diiode. On observe alors la coloration orange du "
                "dichromate virer au vert du chrome trois plus, avec "
                "apparition du diiode, de couleur brune."
            )
        ) as tracker:
            self.play(FadeIn(entete4))
            self.play(Write(demi4a))
            self.play(Write(demi4b))
            self.play(Write(bilan4))
            self.play(FadeIn(observation4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe4))

        # --- Exemple 5 : diiode + thiosulfate (dosage iodométrique) -----------------
        entete5 = Text("Exemple résolu 5 — diiode + thiosulfate", font_size=21, color=YELLOW, weight="BOLD")
        entete5.next_to(titre, DOWN, buff=0.35)

        demi5a = MathTex(r"I_2 + 2\,e^- \rightarrow 2\,I^-", font_size=23, color=WHITE)
        demi5b = MathTex(r"2\,S_2O_3^{2-} \rightarrow S_4O_6^{2-} + 2\,e^-", font_size=23, color=WHITE)
        bilan5 = MathTex(r"I_2 + 2\,S_2O_3^{2-} \longrightarrow 2\,I^- + S_4O_6^{2-}", font_size=25, color=YELLOW)
        observation5 = Text(
            "Aucun H⁺ requis ici. Observation : décoloration du brun de I₂ (dosage iodométrique).",
            font_size=18, color=WHITE,
        )

        groupe5 = VGroup(entete5, demi5a, demi5b, bilan5, observation5).arrange(DOWN, buff=0.3)
        groupe5.next_to(titre, DOWN, buff=0.35)
        _fit(groupe5, titre.get_bottom()[1] - 0.35)
        groupe5.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu cinq : le diiode et l'ion thiosulfate "
                "échangent chacun deux électrons. Le plus petit commun "
                "multiple est directement deux : il suffit d'additionner "
                "les deux demi-équations telles quelles. On obtient : "
                "diiode, plus deux ions thiosulfate, donne deux ions "
                "iodure, plus un ion tétrathionate. Remarquez qu'aucun ion "
                "H plus n'est nécessaire ici, car aucun de ces deux couples "
                "ne contient d'oxygène. Cette réaction, appelée dosage "
                "iodométrique, se traduit par la décoloration du brun du "
                "diiode."
            )
        ) as tracker:
            self.play(FadeIn(entete5))
            self.play(Write(demi5a))
            self.play(Write(demi5b))
            self.play(Write(bilan5))
            self.play(FadeIn(observation5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe5))

        # --- Exemple 6 : fer III + cuivre métal (gravure circuits imprimés) --------
        entete6 = Text("Exemple résolu 6 — fer III + cuivre métal", font_size=21, color=YELLOW, weight="BOLD")
        entete6.next_to(titre, DOWN, buff=0.35)

        demi6a = MathTex(r"Fe^{3+} + e^- \rightarrow Fe^{2+} \quad (\times 2)", font_size=23, color=WHITE)
        demi6b = MathTex(r"Cu \rightarrow Cu^{2+} + 2\,e^-", font_size=23, color=WHITE)
        bilan6 = MathTex(r"2\,Fe^{3+} + Cu \longrightarrow 2\,Fe^{2+} + Cu^{2+}", font_size=26, color=YELLOW)
        observation6 = Text(
            "Application : le perchlorure de fer (Fe³⁺) grave le cuivre des circuits imprimés.",
            font_size=18, color=WHITE,
        )

        groupe6 = VGroup(entete6, demi6a, demi6b, bilan6, observation6).arrange(DOWN, buff=0.3)
        groupe6.next_to(titre, DOWN, buff=0.35)
        _fit(groupe6, titre.get_bottom()[1] - 0.35)
        groupe6.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu six, une application industrielle : le fer "
                "trois plus échange un électron, le cuivre métal en échange "
                "deux. On multiplie donc la demi-équation du fer par deux. "
                "En additionnant, on obtient : deux ions fer trois plus, "
                "plus du cuivre métal, donnent deux ions fer deux plus, "
                "plus un ion cuivre deux plus. C'est exactement la réaction "
                "utilisée pour graver les circuits imprimés en électronique "
                ": une solution de chlorure de fer trois dissout "
                "progressivement le cuivre non protégé par le vernis "
                "isolant."
            )
        ) as tracker:
            self.play(FadeIn(entete6))
            self.play(Write(demi6a))
            self.play(Write(demi6b))
            self.play(Write(bilan6))
            self.play(FadeIn(observation6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe6))

        # --- À retenir : les trois équations bilan ------------------------------------
        recap = example_box(
            VGroup(
                MathTex(r"Cr_2O_7^{2-} + 14\,H^+ + 6\,I^- \rightarrow 2\,Cr^{3+} + 7\,H_2O + 3\,I_2", font_size=17, color="#1A1A1A"),
                MathTex(r"I_2 + 2\,S_2O_3^{2-} \rightarrow 2\,I^- + S_4O_6^{2-}", font_size=18, color="#1A1A1A"),
                MathTex(r"2\,Fe^{3+} + Cu \rightarrow 2\,Fe^{2+} + Cu^{2+}", font_size=18, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=12.8,
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons ces trois équations bilan : elles illustrent que "
                "la méthode générale s'applique aussi bien en milieu acide "
                "qu'en milieu neutre, dès lors que les demi-équations de "
                "départ sont correctement équilibrées."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : toutes les réactions n'ont pas besoin de H⁺ ----------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : n'ajoutez des ions H⁺ que si l'un des couples "
                    "contient de l'oxygène (comme MnO₄⁻ ou Cr₂O₇²⁻). Le "
                    "couple I₂/I⁻ et le couple S₄O₆²⁻/S₂O₃²⁻ n'en "
                    "contiennent pas : leur équation bilan ne fait "
                    "intervenir aucun ion H⁺.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : n'ajoutez des ions H plus "
                "que si l'un des couples contient de l'oxygène, comme le "
                "permanganate ou le dichromate. Le couple diiode sur "
                "iodure, et le couple tétrathionate sur thiosulfate, n'en "
                "contiennent pas : leur équation bilan ne fait intervenir "
                "aucun ion H plus."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
