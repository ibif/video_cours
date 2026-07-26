"""
scenes/Chimie_ClassificationQualitativeRedox_06.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 06.

§ 3. La règle du gamma : énoncé (deux couples empilés selon la
classification, l'oxydant du couple du haut réagit avec le réducteur du
couple du bas, le schéma dessine la lettre grecque γ), schéma Cu²⁺/Cu et
Zn²⁺/Zn. Méthode en 3 étapes pour prévoir une réaction. Exemple résolu 3 :
fer + nitrate d'argent (réaction) ; cuivre + sulfate de fer II (pas de
réaction). Schéma construit uniquement avec des primitives Manim de base.
Source : 1ereC/Chimie.pdf, chapitre 10, pages 97-98.
"""

import textwrap

from manim import (
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
    Line,
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


def _schema_gamma():
    """Schéma de la règle du gamma pour les couples Cu²⁺/Cu (en haut,
    donc oxydant fort) et Zn²⁺/Zn (en bas, donc réducteur fort), construit
    uniquement avec des primitives Manim de base (Line, Arrow, MathTex,
    VGroup) — aucune bibliothèque externe."""

    ox_haut = MathTex(r"Cu^{2+}", font_size=30, color=WHITE)
    red_haut = MathTex(r"Cu", font_size=30, color=WHITE)
    ox_bas = MathTex(r"Zn^{2+}", font_size=30, color=WHITE)
    red_bas = MathTex(r"Zn", font_size=30, color=WHITE)

    ox_haut.move_to([-1.6, 1.0, 0])
    red_haut.move_to([1.6, 1.0, 0])
    ox_bas.move_to([-1.6, -1.0, 0])
    red_bas.move_to([1.6, -1.0, 0])

    ligne_haut = Line(ox_haut.get_right() + RIGHT * 0.15, red_haut.get_left() + LEFT * 0.15, color=WHITE, stroke_width=2)
    ligne_bas = Line(ox_bas.get_right() + RIGHT * 0.15, red_bas.get_left() + LEFT * 0.15, color=WHITE, stroke_width=2)

    label_haut = Text("Cu²⁺/Cu  (couple du haut : oxydant fort)", font_size=17, color=ORANGE)
    label_haut.next_to(VGroup(ox_haut, red_haut), UP, buff=0.35)
    label_bas = Text("Zn²⁺/Zn  (couple du bas : réducteur fort)", font_size=17, color="#288073")
    label_bas.next_to(VGroup(ox_bas, red_bas), DOWN, buff=0.35)

    # La diagonale du gamma : de l'oxydant fort (haut-gauche) vers le
    # réducteur fort (bas-droite) — sens du transfert d'électrons.
    diagonale = Arrow(
        ox_haut.get_bottom() + DOWN * 0.1,
        red_bas.get_top() + UP * 0.1,
        color=YELLOW, stroke_width=4, buff=0.05, max_tip_length_to_length_ratio=0.12,
    )
    label_diag = Text("sens de la réaction (γ)", font_size=16, color=YELLOW)
    label_diag.next_to(diagonale, RIGHT, buff=0.15)

    schema = VGroup(
        ox_haut, red_haut, ox_bas, red_bas,
        ligne_haut, ligne_bas, label_haut, label_bas,
        diagonale, label_diag,
    )
    return schema


class RegleDuGamma(NotionScene):
    def construct(self):
        titre = scene_title("10.3 La règle du gamma")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        intro = Text(
            _wrap(
                "La classification permet de prévoir, sans expérience "
                "préalable, si une réaction va se produire entre deux "
                "couples donnés. La méthode graphique qui permet cela "
                "s'appelle la règle du gamma.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La classification permet de prévoir, sans avoir besoin de "
                "faire l'expérience, si une réaction va se produire entre "
                "deux couples donnés. La méthode graphique qui permet cela "
                "s'appelle la règle du gamma, du nom de la lettre grecque "
                "que dessine le schéma."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : énoncé de la règle ------------------------------
        regle = method_box(
            VGroup(
                Text("Règle du gamma :", font_size=22, weight="BOLD"),
                Text(
                    "On empile les deux couples selon la classification",
                    font_size=20,
                ),
                Text(
                    "(oxydant fort en haut, réducteur fort en bas).",
                    font_size=20,
                ),
                Text(
                    "L'oxydant du couple du haut réagit avec le réducteur",
                    font_size=20,
                ),
                Text(
                    "du couple du bas : le trait qui les relie dessine un γ.",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.6,
        )
        regle.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la règle : on empile les deux couples selon leur "
                "position dans la classification, le couple contenant "
                "l'oxydant le plus fort en haut, celui contenant le "
                "réducteur le plus fort en bas. L'oxydant du couple du "
                "haut réagit alors avec le réducteur du couple du bas : le "
                "trait qui relie ces deux espèces, en diagonale, dessine la "
                "lettre grecque gamma."
            )
        ) as tracker:
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle))

        # --- Exemple traité : schéma Cu2+/Cu et Zn2+/Zn ---------------------
        entete_schema = Text("Exemple : les couples Cu²⁺/Cu et Zn²⁺/Zn", font_size=20, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.3)

        schema = _schema_gamma()
        schema.next_to(entete_schema, DOWN, buff=0.35)
        groupe_schema = VGroup(entete_schema, schema)
        _fit(groupe_schema, titre.get_bottom()[1] - 0.15)
        groupe_schema.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Prenons les couples cuivre deux plus sur cuivre et zinc "
                "deux plus sur zinc. Le zinc étant plus réducteur, son "
                "couple se place en dessous. On relie l'oxydant du couple "
                "du haut, les ions cuivre deux plus, au réducteur du couple "
                "du bas, le zinc métal : cette diagonale indique le sens de "
                "la réaction, ainsi que le sens du transfert des "
                "électrons, du zinc vers les ions cuivre deux plus."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(Write(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Méthode en 3 étapes --------------------------------------------
        methode = method_box(
            VGroup(
                Text("Pour prévoir une réaction entre deux couples :", font_size=21, weight="BOLD"),
                Text("1. Placer les deux couples dans la classification.", font_size=20),
                Text("2. Tracer le γ : oxydant du haut → réducteur du bas.", font_size=20),
                Text("3. Écrire l'équation bilan à partir de ce sens.", font_size=20),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.4,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En pratique, pour prévoir une réaction entre deux couples, "
                "on procède en trois étapes : d'abord, on place les deux "
                "couples dans la classification. Ensuite, on trace le "
                "gamma, de l'oxydant du couple du haut vers le réducteur du "
                "couple du bas. Enfin, on écrit l'équation bilan à partir "
                "de ce sens de réaction."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple résolu 3 : fer + nitrate d'argent / cuivre + sulfate de fer
        entete_ex = Text("Exemple résolu 3 — Deux cas à comparer", font_size=20, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.3)

        cas1 = VGroup(
            Text("Fer + nitrate d'argent : Ag⁺/Ag est au-dessus de Fe²⁺/Fe", font_size=19, color=WHITE),
            MathTex(r"Fe + 2Ag^{+} \longrightarrow Fe^{2+} + 2Ag \quad\text{(réaction)}", font_size=24, color=ORANGE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        cas2 = VGroup(
            Text("Cuivre + sulfate de fer II : Cu²⁺/Cu est au-dessus de Fe²⁺/Fe", font_size=19, color=WHITE),
            Text("le cuivre est moins réducteur que le fer : pas de γ possible", font_size=19, color=WHITE),
            MathTex(r"\text{aucune réaction}", font_size=24, color=YELLOW),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        contenu_ex = VGroup(cas1, cas2).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        contenu_ex.next_to(entete_ex, DOWN, buff=0.35)
        groupe_ex = VGroup(entete_ex, contenu_ex)
        _fit(groupe_ex, titre.get_bottom()[1] - 0.15)
        groupe_ex.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Comparons deux cas. Premier cas : on plonge du fer dans "
                "une solution de nitrate d'argent. Dans la classification, "
                "le couple argent sur argent est au-dessus du couple fer "
                "deux plus sur fer : le gamma relie les ions argent au fer, "
                "et la réaction a bien lieu, fer plus deux ions argent, "
                "donne fer deux plus, plus deux argent. Deuxième cas : on "
                "plonge du cuivre dans une solution de sulfate de fer deux. "
                "Le couple cuivre deux plus sur cuivre est cette fois "
                "au-dessus du couple du fer : le cuivre est moins réducteur "
                "que le fer, aucun gamma ne peut relier un oxydant du bas à "
                "un réducteur du haut : il n'y a donc aucune réaction."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(cas1))
            self.play(FadeIn(cas2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_ex))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le gamma ne se trace que dans un seul sens : de "
                    "l'oxydant du couple placé le plus HAUT vers le "
                    "réducteur du couple placé le plus BAS. Dans l'autre "
                    "sens, aucune réaction spontanée n'est prévue.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : le gamma ne se trace que "
                "dans un seul sens, de l'oxydant du couple placé le plus "
                "haut vers le réducteur du couple placé le plus bas. Dans "
                "l'autre sens, aucune réaction spontanée n'est prévue par "
                "la classification."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
