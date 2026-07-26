"""
scenes/Chimie_OxydoreductionSolutionAqueuse_03.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 03.

§ Les demi-équations électroniques : définition (Ox + n e⁻ ⇌ Red comme
traduction formelle d'un couple), exemples simples sans oxygène (Fe³⁺/Fe²⁺,
Cu²⁺/Cu, I₂/I⁻, S₄O₆²⁻/S₂O₃²⁻). Piège : équilibrer d'abord les atomes,
ensuite seulement les charges avec les électrons.
Source : 1ereC/Chimie.pdf, chapitre 9, page 88.
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
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class LesDemiEquationsElectroniques(NotionScene):
    def construct(self):
        titre = scene_title("9.3 Les demi-équations électroniques")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition -----------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une demi-équation électronique est l'écriture "
                    "formelle qui traduit l'échange d'électrons au sein "
                    "d'un couple oxydant/réducteur : elle relie la forme "
                    "oxydée à sa forme réduite.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une demi-équation électronique est l'écriture formelle "
                "qui traduit l'échange d'électrons au sein d'un couple "
                "oxydant sur réducteur : elle relie la forme oxydée à sa "
                "forme réduite, avec le nombre exact d'électrons échangés."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : équilibrer un couple simple, pas à pas -----------------
        entete_methode = Text("Pour un couple sans oxygène : équilibrer atomes, puis charges", font_size=20, color=YELLOW, weight="BOLD")
        entete_methode.next_to(titre, DOWN, buff=0.4)

        etape_i2_brut = MathTex(r"I_2 \;+\; e^- \;\longrightarrow\; I^-\quad\text{(atomes déséquilibrés !)}", font_size=24, color=WHITE)
        etape_i2_brut.next_to(entete_methode, DOWN, buff=0.4)

        etape_i2_ok = MathTex(r"I_2 + 2\,e^- \longrightarrow 2\,I^-", font_size=30, color=YELLOW)
        etape_i2_ok.next_to(etape_i2_brut, DOWN, buff=0.4)

        groupe_methode = VGroup(entete_methode, etape_i2_brut, etape_i2_ok)

        with self.voiceover(
            text=(
                "Prenons le couple diiode sur ion iodure. Si l'on écrit "
                "I-deux plus un électron donne I moins, les atomes d'iode "
                "sont déséquilibrés : deux à gauche, un seul à droite. Il "
                "faut d'abord équilibrer les atomes en plaçant un "
                "coefficient deux devant l'ion iodure, puis seulement "
                "ensuite ajuster les charges avec les électrons : I-deux, "
                "plus deux électrons, donne deux I moins. Les charges sont "
                "alors bien égales des deux côtés : moins deux d'un côté, "
                "moins deux de l'autre."
            )
        ) as tracker:
            self.play(FadeIn(entete_methode))
            self.play(Write(etape_i2_brut))
            self.play(Write(etape_i2_ok))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_methode))

        # --- Exemple traité : trois autres demi-équations simples -------------------
        entete_exemples = Text("Autres exemples sans oxygène", font_size=22, color=YELLOW, weight="BOLD")
        entete_exemples.next_to(titre, DOWN, buff=0.35)

        demi_fe = MathTex(r"Fe^{3+} + e^- \longrightarrow Fe^{2+}", font_size=28, color=WHITE)
        demi_cu = MathTex(r"Cu^{2+} + 2\,e^- \longrightarrow Cu", font_size=28, color=WHITE)
        demi_s = MathTex(r"S_4O_6^{2-} + 2\,e^- \longrightarrow 2\,S_2O_3^{2-}", font_size=28, color=WHITE)

        exemples = VGroup(demi_fe, demi_cu, demi_s).arrange(DOWN, buff=0.4)
        exemples.next_to(entete_exemples, DOWN, buff=0.4)

        groupe_exemples = VGroup(entete_exemples, exemples)

        with self.voiceover(
            text=(
                "Voici trois autres demi-équations de couples sans "
                "oxygène, déjà équilibrées en atomes et en charges. Pour "
                "fer trois plus sur fer deux plus : fer trois plus, plus un "
                "électron, donne fer deux plus. Pour cuivre deux plus sur "
                "cuivre : cuivre deux plus, plus deux électrons, donne "
                "cuivre. Et pour le couple tétrathionate sur thiosulfate : "
                "S-quatre-O-six deux moins, plus deux électrons, donne deux "
                "fois S-deux-O-trois deux moins — remarquez le coefficient "
                "deux, nécessaire pour équilibrer les quatre atomes de "
                "soufre."
            )
        ) as tracker:
            self.play(FadeIn(entete_exemples))
            self.play(Write(demi_fe))
            self.play(Write(demi_cu))
            self.play(Write(demi_s))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_exemples))

        # --- À retenir : la forme générale -------------------------------------------
        recap = definition_box(
            MathTex(r"Ox + n\,e^- \rightleftharpoons Red", font_size=32, color="#1A1A1A"),
        )
        recap.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la forme générale d'une demi-équation "
                "électronique : Ox, plus n électrons, en équilibre avec "
                "Red. C'est cette écriture que nous allons maintenant "
                "apprendre à construire de façon systématique, y compris "
                "pour des couples contenant de l'oxygène."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : l'ordre des étapes ------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : toujours équilibrer d'abord les ATOMES (avec "
                    "de simples coefficients), et seulement ENSUITE les "
                    "CHARGES avec les électrons. Ajouter des électrons "
                    "avant d'avoir équilibré les atomes conduit "
                    "systématiquement à une demi-équation fausse.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)
        _fit(piege, titre.get_bottom()[1] - 0.5)

        with self.voiceover(
            text=(
                "Attention à l'ordre des étapes : il faut toujours "
                "équilibrer d'abord les atomes, avec de simples "
                "coefficients, et seulement ensuite les charges, avec les "
                "électrons. Ajouter des électrons avant d'avoir équilibré "
                "les atomes conduit systématiquement à une demi-équation "
                "fausse."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
