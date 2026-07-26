"""
scenes/Chimie_OxydoreductionSolutionAqueuse_05.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 05.

§ Équation bilan d'une réaction d'oxydoréduction : principe
(Ox₁+Red₂→Red₁+Ox₂), méthode en 5 étapes (demi-équations, PPCM électrons,
addition, simplification, vérification). Exemple résolu 3 : permanganate +
fer II (dosage manganimétrique).
Source : 1ereC/Chimie.pdf, chapitre 9, page 90.
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
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class EquationBilanOxydoreduction(NotionScene):
    def construct(self):
        titre = scene_title("9.5 Équation bilan d'une réaction d'oxydoréduction")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : le principe -----------------------------------------------------
        principe = MathTex(r"Ox_1 + Red_2 \longrightarrow Red_1 + Ox_2", font_size=32, color=WHITE)
        principe.next_to(titre, DOWN, buff=0.55)

        texte_principe = Text(
            _wrap(
                "Une réaction d'oxydoréduction met en jeu DEUX couples : "
                "l'oxydant du premier couple réagit avec le réducteur du "
                "second, en échangeant directement leurs électrons.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        texte_principe.next_to(principe, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous savons désormais écrire la demi-équation d'un "
                "couple isolé. Mais une vraie réaction d'oxydoréduction met "
                "en jeu deux couples à la fois : l'oxydant du premier "
                "couple, Ox indice un, réagit avec le réducteur du second "
                "couple, Red indice deux, pour donner Red indice un et Ox "
                "indice deux. Les électrons cédés par l'un sont "
                "exactement ceux captés par l'autre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Write(principe))
            self.play(FadeIn(texte_principe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(principe), FadeOut(texte_principe))

        # --- Raisonnement : la méthode en 5 étapes -----------------------------------
        methode = property_box(
            VGroup(
                Text("1. Écrire les deux demi-équations électroniques.", font_size=20),
                Text("2. Déterminer le PPCM des nombres d'électrons échangés.", font_size=20),
                Text("3. Multiplier chaque demi-équation pour égaliser les électrons.", font_size=20),
                Text("4. Additionner les deux demi-équations, puis simplifier les e⁻.", font_size=20),
                Text("5. Vérifier la conservation des éléments et des charges.", font_size=20),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.5,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour construire l'équation bilan, on suit une méthode en "
                "cinq étapes. Un : écrire les deux demi-équations "
                "électroniques des couples en présence. Deux : déterminer "
                "le plus petit commun multiple des nombres d'électrons "
                "échangés par chaque couple. Trois : multiplier chaque "
                "demi-équation par le coefficient nécessaire pour égaliser "
                "ce nombre d'électrons. Quatre : additionner membre à "
                "membre les deux demi-équations, puis simplifier les "
                "électrons, qui doivent totalement disparaître. Cinq : "
                "vérifier que tous les éléments et toutes les charges sont "
                "bien conservés."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : dosage manganimétrique (MnO₄⁻ + Fe²⁺) -----------------
        entete_ex = Text("Exemple résolu 3 — dosage manganimétrique", font_size=22, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.35)

        demi1 = MathTex(r"MnO_4^- + 8\,H^+ + 5\,e^- \rightarrow Mn^{2+} + 4\,H_2O \quad (\times 1)", font_size=22, color=WHITE)
        demi2 = MathTex(r"Fe^{2+} \rightarrow Fe^{3+} + e^- \quad (\times 5)", font_size=22, color=WHITE)
        ppcm_txt = Text("PPCM(5, 1) = 5", font_size=18, color=YELLOW)

        demis = VGroup(demi1, demi2, ppcm_txt).arrange(DOWN, buff=0.3)
        demis.next_to(entete_ex, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Traitons un exemple classique, celui du dosage "
                "manganimétrique : le permanganate réagit avec les ions fer "
                "deux plus, en milieu acide. La demi-équation du "
                "permanganate échange cinq électrons, celle du fer en "
                "échange un seul. Le plus petit commun multiple de cinq et "
                "un est cinq : on garde donc la première demi-équation "
                "telle quelle, et on multiplie la seconde par cinq."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(demi1))
            self.play(Write(demi2))
            self.play(FadeIn(ppcm_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(demis))

        entete_somme = Text("Addition et simplification des électrons", font_size=22, color=YELLOW, weight="BOLD")
        entete_somme.next_to(titre, DOWN, buff=0.35)

        somme_brute = MathTex(
            r"MnO_4^- + 8\,H^+ + 5\,e^- + 5\,Fe^{2+} \rightarrow Mn^{2+} + 4\,H_2O + 5\,Fe^{3+} + 5\,e^-",
            font_size=19, color=WHITE,
        )
        somme_brute.next_to(entete_somme, DOWN, buff=0.4)

        equation_bilan = MathTex(
            r"MnO_4^- + 8\,H^+ + 5\,Fe^{2+} \longrightarrow Mn^{2+} + 4\,H_2O + 5\,Fe^{3+}",
            font_size=24, color=YELLOW,
        )
        equation_bilan.next_to(somme_brute, DOWN, buff=0.45)

        groupe_somme = VGroup(entete_somme, somme_brute, equation_bilan)

        with self.voiceover(
            text=(
                "On additionne alors membre à membre les deux "
                "demi-équations. Les cinq électrons apparaissent des deux "
                "côtés : ils se simplifient exactement. Il reste "
                "l'équation bilan : ion permanganate, plus huit ions H "
                "plus, plus cinq ions fer deux plus, donne ion manganèse "
                "deux plus, plus quatre molécules d'eau, plus cinq ions "
                "fer trois plus. Vérifions : dix-sept charges positives de "
                "chaque côté, et tous les éléments sont bien conservés. "
                "C'est la réaction utilisée lors du dosage manganimétrique "
                "des ions fer deux plus."
            )
        ) as tracker:
            self.play(FadeIn(entete_somme))
            self.play(Write(somme_brute))
            self.play(Write(equation_bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_somme))

        # --- À retenir : l'équation bilan finale -------------------------------------
        recap = example_box(
            MathTex(
                r"MnO_4^- + 8\,H^+ + 5\,Fe^{2+} \rightarrow Mn^{2+} + 4\,H_2O + 5\,Fe^{3+}",
                font_size=22, color="#1A1A1A",
            ),
            box_width=12.5,
        )
        recap.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons cette équation bilan : elle illustre parfaitement "
                "la méthode générale en cinq étapes que nous venons "
                "d'appliquer, et qui fonctionne pour n'importe quel couple "
                "de réactions d'oxydoréduction."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : oublier de vérifier la simplification totale ---------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : si, après addition, des électrons subsistent "
                    "encore d'un seul côté de l'équation, c'est que le "
                    "PPCM ou les coefficients multiplicateurs ont été mal "
                    "choisis. Une équation bilan correcte ne contient "
                    "JAMAIS d'électron libre.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)
        _fit(piege, titre.get_bottom()[1] - 0.5)

        with self.voiceover(
            text=(
                "Attention à un piège : si, après addition, des électrons "
                "subsistent encore d'un seul côté de l'équation, c'est que "
                "le plus petit commun multiple ou les coefficients "
                "multiplicateurs ont été mal choisis. Une équation bilan "
                "correcte ne contient jamais d'électron libre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
