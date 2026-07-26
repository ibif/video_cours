"""
scenes/Chimie_OxydoreductionSolutionAqueuse_10.py — Chapitre 9 « Réactions
d'oxydoréduction en solution aqueuse » (1ereC, Chimie), scène 10.

§ Méthodes (identifier oxydant/réducteur, retrouver le couple d'une
espèce, équilibrer en milieu acide, construire l'équation bilan), pièges à
éviter (électrons dans le bilan final, inverser Ox/Red, oublier H⁺,
confondre décoloration et disparition), et essentiel à retenir du
chapitre.
Source : 1ereC/Chimie.pdf, chapitre 9, page 93.
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
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class MethodesPiegesEtEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("9.10 Méthodes, pièges à éviter et essentiel")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : quatre méthodes à maîtriser -------------------------------------
        intro = Text(
            _wrap(
                "Terminons ce chapitre par une synthèse : les quatre "
                "méthodes clés, les quatre pièges les plus fréquents, "
                "puis l'essentiel à retenir.",
                width=52,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Terminons ce chapitre sur les réactions d'oxydoréduction "
                "en solution aqueuse par une synthèse méthodologique : les "
                "quatre méthodes clés à maîtriser, les quatre pièges les "
                "plus fréquents, et enfin l'essentiel à retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : les quatre méthodes ---------------------------------------
        methode1 = method_box(
            Text(
                _wrap(
                    "Méthode 1 — Identifier oxydant et réducteur : "
                    "repérer l'espèce qui GAGNE des électrons (oxydant, "
                    "qui se réduit) et celle qui en PERD (réducteur, qui "
                    "s'oxyde).",
                    width=46,
                ),
                font_size=21,
            ),
        )
        methode1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode un : pour identifier l'oxydant et le réducteur "
                "d'une réaction, il faut repérer l'espèce qui gagne des "
                "électrons — c'est l'oxydant, qui se réduit — et celle qui "
                "en perd — c'est le réducteur, qui s'oxyde."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            Text(
                _wrap(
                    "Méthode 2 — Retrouver le couple d'une espèce : "
                    "chercher sa forme oxydée OU réduite associée. Une "
                    "espèce peut appartenir à plusieurs couples "
                    "(ampholyte redox, ex : Fe²⁺).",
                    width=46,
                ),
                font_size=21,
            ),
        )
        methode2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode deux : pour retrouver le couple d'une espèce "
                "donnée, il faut chercher sa forme oxydée ou sa forme "
                "réduite associée. N'oubliez pas qu'une même espèce peut "
                "appartenir à plusieurs couples : c'est le cas des "
                "ampholytes redox, comme l'ion fer deux plus."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            VGroup(
                Text("Méthode 3 — Équilibrer en milieu acide, dans l'ordre :", font_size=21, weight="BOLD"),
                Text("éléments (hors O,H) → O avec H₂O → H avec H⁺ → charges avec e⁻.", font_size=19),
            ).arrange(DOWN, buff=0.3),
        )
        methode3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode trois : pour équilibrer une demi-équation en "
                "milieu acide sans erreur, respecter toujours le même "
                "ordre : les éléments autres que l'oxygène et l'hydrogène "
                "d'abord, puis l'oxygène avec des molécules d'eau, puis "
                "l'hydrogène avec des ions H plus, et enfin les charges "
                "avec des électrons."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        methode4 = method_box(
            VGroup(
                Text("Méthode 4 — Construire l'équation bilan :", font_size=21, weight="BOLD"),
                Text("demi-équations → PPCM des e⁻ → multiplier → additionner/simplifier → vérifier.", font_size=18),
            ).arrange(DOWN, buff=0.3),
        )
        methode4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode quatre : pour construire l'équation bilan d'une "
                "réaction entre deux couples, écrire les deux "
                "demi-équations, déterminer le plus petit commun multiple "
                "des nombres d'électrons échangés, multiplier chaque "
                "demi-équation en conséquence, additionner puis simplifier "
                "les électrons, et enfin vérifier la conservation des "
                "éléments et des charges."
            )
        ) as tracker:
            self.play(FadeIn(methode4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode4))

        # --- Exemple traité : les quatre pièges classiques ----------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 — Une équation bilan finale ne doit JAMAIS "
                    "contenir d'électron libre : s'il en reste, le PPCM "
                    "ou les coefficients sont faux.",
                    width=46,
                ),
                font_size=21,
            ),
        )
        piege1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège un : une équation bilan finale ne doit jamais "
                "contenir d'électron libre. S'il en reste après addition, "
                "c'est que le plus petit commun multiple, ou les "
                "coefficients multiplicateurs, ont été mal choisis."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            MathTex(
                r"\text{Toujours } Ox/Red,\ \text{jamais } Red/Ox \quad (\text{ex : } Cu^{2+}/Cu,\ \text{pas } Cu/Cu^{2+})",
                font_size=22, color="#1A1A1A",
            ),
        )
        piege2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège deux : ne jamais inverser l'ordre dans la notation "
                "d'un couple. On écrit toujours oxydant sur réducteur, "
                "jamais l'inverse — par exemple, cuivre deux plus sur "
                "cuivre, et non cuivre sur cuivre deux plus."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            Text(
                _wrap(
                    "Piège 3 — Ne pas oublier les ions H⁺ en milieu "
                    "acide : ils sont indispensables dès qu'un couple "
                    "contient de l'oxygène (MnO₄⁻, Cr₂O₇²⁻...).",
                    width=46,
                ),
                font_size=21,
            ),
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège trois : ne pas oublier les ions H plus en milieu "
                "acide. Ils sont indispensables dès qu'un couple contient "
                "de l'oxygène, comme le permanganate ou le dichromate — "
                "sans eux, l'équation reste déséquilibrée en hydrogène."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            Text(
                _wrap(
                    "Piège 4 — Ne pas confondre DÉCOLORATION (l'espèce "
                    "colorée se transforme en une espèce incolore, mais "
                    "existe toujours en solution) et DISPARITION totale "
                    "de la matière.",
                    width=46,
                ),
                font_size=21,
            ),
        )
        piege4.next_to(titre, DOWN, buff=0.4)
        _fit(piege4, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Piège quatre, et dernier : ne pas confondre décoloration "
                "et disparition. Quand une solution se décolore, l'espèce "
                "colorée s'est transformée en une nouvelle espèce, "
                "souvent incolore, mais qui existe toujours bel et bien en "
                "solution — la matière ne disparaît jamais, elle change "
                "seulement de forme chimique."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- À retenir : l'essentiel du chapitre --------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text(
                    _wrap(
                        "Une réaction d'oxydoréduction transfère des "
                        "électrons d'un réducteur vers un oxydant, entre "
                        "deux couples Ox/Red distincts.",
                        width=48,
                    ),
                    font_size=20,
                ),
                MathTex(r"Ox_1 + Red_2 \rightarrow Red_1 + Ox_2", font_size=24, color="#1A1A1A"),
                Text(
                    "Demi-équation en milieu acide : éléments → O (H₂O) → H (H⁺) → charges (e⁻).",
                    font_size=18,
                ),
                Text(
                    "Équation bilan : PPCM des électrons, puis addition et simplification.",
                    font_size=18,
                ),
                Text(
                    "L'oxydant le plus fort réagit avec le réducteur le plus fort.",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)
        _fit(essentiel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de ce chapitre. Une réaction "
                "d'oxydoréduction transfère des électrons d'un réducteur "
                "vers un oxydant, entre deux couples oxydant sur réducteur "
                "distincts : Ox indice un, plus Red indice deux, donne Red "
                "indice un, plus Ox indice deux. Pour équilibrer une "
                "demi-équation en milieu acide, on procède dans l'ordre : "
                "les éléments, puis l'oxygène avec l'eau, puis l'hydrogène "
                "avec les ions H plus, puis les charges avec les "
                "électrons. Pour construire l'équation bilan, on cherche "
                "le plus petit commun multiple des électrons échangés, "
                "puis on additionne et on simplifie. Et enfin, "
                "expérimentalement, c'est toujours l'oxydant le plus fort "
                "qui réagit avec le réducteur le plus fort."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
