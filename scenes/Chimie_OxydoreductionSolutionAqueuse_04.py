"""
scenes/Chimie_OxydoreductionSolutionAqueuse_04.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 04.

§ Méthode d'équilibrage d'une demi-équation en milieu acide (4 étapes :
éléments autres que O/H, puis O avec H₂O, puis H avec H⁺, puis charges avec
e⁻). Exemple résolu 1 : MnO₄⁻/Mn²⁺ en détail. Exemple résolu 2 :
Cr₂O₇²⁻/Cr³⁺. Piège : les électrons n'équilibrent jamais les éléments.
Source : 1ereC/Chimie.pdf, chapitre 9, pages 88-89.
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
from shapes.boxes import method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class MethodeEquilibrageMilieuAcide(NotionScene):
    def construct(self):
        titre = scene_title("9.4 Équilibrer une demi-équation en milieu acide")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : la méthode en 4 étapes -----------------------------------------
        methode = method_box(
            VGroup(
                Text("1. Équilibrer les éléments autres que O et H.", font_size=21),
                Text("2. Équilibrer l'oxygène O avec des molécules H₂O.", font_size=21),
                Text("3. Équilibrer l'hydrogène H avec des ions H⁺.", font_size=21),
                Text("4. Équilibrer les charges avec des électrons e⁻.", font_size=21),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour les couples contenant de l'oxygène, on équilibre une "
                "demi-équation en milieu acide en suivant toujours quatre "
                "étapes, dans cet ordre précis. Un : équilibrer les "
                "éléments autres que l'oxygène et l'hydrogène. Deux : "
                "équilibrer l'oxygène avec des molécules d'eau, H-deux-O. "
                "Trois : équilibrer l'hydrogène avec des ions H plus, "
                "puisque le milieu est acide. Quatre : équilibrer enfin les "
                "charges avec des électrons."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Raisonnement / Exemple traité 1 : MnO₄⁻/Mn²⁺, pas à pas ----------------
        entete_ex1 = Text("Exemple résolu 1 — couple MnO₄⁻ / Mn²⁺", font_size=22, color=YELLOW, weight="BOLD")
        entete_ex1.next_to(titre, DOWN, buff=0.35)

        e1_depart = MathTex(r"MnO_4^- \;\longrightarrow\; Mn^{2+}", font_size=26, color=WHITE)
        e1_mn = Text("Étape 1 (Mn) : déjà équilibré, 1 atome de chaque côté.", font_size=18, color=WHITE)
        e1_o = MathTex(r"MnO_4^- \longrightarrow Mn^{2+} + 4\,H_2O", font_size=26, color=WHITE)
        e1_o_txt = Text("Étape 2 (O) : 4 atomes d'oxygène → 4 H₂O.", font_size=18, color=WHITE)
        e1_h = MathTex(r"MnO_4^- + 8\,H^+ \longrightarrow Mn^{2+} + 4\,H_2O", font_size=26, color=WHITE)
        e1_h_txt = Text("Étape 3 (H) : 4 H₂O contiennent 8 H → 8 H⁺ à gauche.", font_size=18, color=WHITE)
        e1_final = MathTex(r"MnO_4^- + 8\,H^+ + 5\,e^- \longrightarrow Mn^{2+} + 4\,H_2O", font_size=27, color=YELLOW)
        e1_charge_txt = Text("Étape 4 (charges) : gauche (-1+8)=+7, droite +2 → 5 e⁻ à gauche.", font_size=18, color=WHITE)

        colonne1 = VGroup(
            entete_ex1,
            e1_depart, e1_mn,
            e1_o, e1_o_txt,
            e1_h, e1_h_txt,
            e1_final, e1_charge_txt,
        ).arrange(DOWN, buff=0.22)
        colonne1.next_to(titre, DOWN, buff=0.3)
        _fit(colonne1, titre.get_bottom()[1] - 0.3)
        colonne1.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Traitons en détail le couple ion permanganate sur "
                "manganèse deux plus. On part de M-n-O-quatre moins donne "
                "M-n deux plus. Étape un, le manganèse : déjà équilibré, un "
                "atome de chaque côté. Étape deux, l'oxygène : il y a "
                "quatre atomes d'oxygène à gauche, on ajoute donc quatre "
                "molécules d'eau à droite. Étape trois, l'hydrogène : ces "
                "quatre molécules d'eau contiennent huit atomes "
                "d'hydrogène, on ajoute donc huit ions H plus à gauche, "
                "puisque le milieu est acide. Étape quatre, les charges : à "
                "gauche, moins un plus huit égale plus sept ; à droite, "
                "plus deux. Il faut donc ajouter cinq électrons à gauche "
                "pour équilibrer : plus sept moins cinq égale plus deux. La "
                "demi-équation finale est équilibrée."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex1))
            self.play(Write(e1_depart), FadeIn(e1_mn))
            self.play(Write(e1_o), FadeIn(e1_o_txt))
            self.play(Write(e1_h), FadeIn(e1_h_txt))
            self.play(Write(e1_final), FadeIn(e1_charge_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(colonne1))

        # --- Exemple traité 2 : Cr₂O₇²⁻/Cr³⁺ -----------------------------------------
        entete_ex2 = Text("Exemple résolu 2 — couple Cr₂O₇²⁻ / Cr³⁺", font_size=22, color=YELLOW, weight="BOLD")
        entete_ex2.next_to(titre, DOWN, buff=0.35)

        e2_cr = MathTex(r"Cr_2O_7^{2-} \longrightarrow 2\,Cr^{3+}", font_size=26, color=WHITE)
        e2_cr_txt = Text("Étape 1 (Cr) : 2 atomes de chrome → coefficient 2 sur Cr³⁺.", font_size=18, color=WHITE)
        e2_o = MathTex(r"Cr_2O_7^{2-} \longrightarrow 2\,Cr^{3+} + 7\,H_2O", font_size=26, color=WHITE)
        e2_o_txt = Text("Étape 2 (O) : 7 atomes d'oxygène → 7 H₂O.", font_size=18, color=WHITE)
        e2_h = MathTex(r"Cr_2O_7^{2-} + 14\,H^+ \longrightarrow 2\,Cr^{3+} + 7\,H_2O", font_size=25, color=WHITE)
        e2_h_txt = Text("Étape 3 (H) : 7 H₂O contiennent 14 H → 14 H⁺.", font_size=18, color=WHITE)
        e2_final = MathTex(r"Cr_2O_7^{2-} + 14\,H^+ + 6\,e^- \longrightarrow 2\,Cr^{3+} + 7\,H_2O", font_size=25, color=YELLOW)
        e2_charge_txt = Text("Étape 4 (charges) : gauche (-2+14)=+12, droite +6 → 6 e⁻.", font_size=18, color=WHITE)

        colonne2 = VGroup(
            entete_ex2,
            e2_cr, e2_cr_txt,
            e2_o, e2_o_txt,
            e2_h, e2_h_txt,
            e2_final, e2_charge_txt,
        ).arrange(DOWN, buff=0.22)
        colonne2.next_to(titre, DOWN, buff=0.3)
        _fit(colonne2, titre.get_bottom()[1] - 0.3)
        colonne2.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Appliquons la même méthode au couple ion dichromate sur "
                "chrome trois plus. Étape un, le chrome : il y a deux "
                "atomes de chrome à gauche, on place donc un coefficient "
                "deux devant Cr trois plus. Étape deux, l'oxygène : sept "
                "atomes d'oxygène à gauche, donc sept molécules d'eau à "
                "droite. Étape trois, l'hydrogène : sept molécules d'eau "
                "contiennent quatorze atomes d'hydrogène, donc quatorze "
                "ions H plus à gauche. Étape quatre, les charges : à "
                "gauche, moins deux plus quatorze égale plus douze ; à "
                "droite, deux fois plus trois égale plus six. Il faut donc "
                "six électrons à gauche pour équilibrer."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex2))
            self.play(Write(e2_cr), FadeIn(e2_cr_txt))
            self.play(Write(e2_o), FadeIn(e2_o_txt))
            self.play(Write(e2_h), FadeIn(e2_h_txt))
            self.play(Write(e2_final), FadeIn(e2_charge_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(colonne2))

        # --- À retenir : les deux demi-équations obtenues ----------------------------
        recap = method_box(
            VGroup(
                MathTex(r"MnO_4^- + 8\,H^+ + 5\,e^- \rightarrow Mn^{2+} + 4\,H_2O", font_size=22, color="#1A1A1A"),
                MathTex(r"Cr_2O_7^{2-} + 14\,H^+ + 6\,e^- \rightarrow 2\,Cr^{3+} + 7\,H_2O", font_size=22, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=12.5,
        )
        recap.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons ces deux demi-équations désormais équilibrées : "
                "elles reviendront très souvent dans les exercices, car les "
                "ions permanganate et dichromate sont des oxydants très "
                "utilisés en milieu acide."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : les électrons n'équilibrent jamais les éléments -------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège fréquent : les électrons ne servent JAMAIS à "
                    "équilibrer un élément chimique (ni O, ni H, ni le "
                    "reste). Ils n'interviennent qu'à la toute dernière "
                    "étape, pour équilibrer les CHARGES, une fois tous les "
                    "atomes déjà équilibrés.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.45)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : les électrons ne servent "
                "jamais à équilibrer un élément chimique, ni l'oxygène, ni "
                "l'hydrogène, ni aucun autre. Ils n'interviennent qu'à la "
                "toute dernière étape, pour équilibrer les charges, une "
                "fois que tous les atomes sont déjà équilibrés."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
