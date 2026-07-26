"""
scenes/SVT_ExpressionGenetique_07.py — Chapitre 5 (1ereC, SVT), scène 07.

IV.A-B. Le code génétique : le problème posé (4 lettres → 20 acides
aminés → triplets, 4³=64), définition du codon, et la table complète du
code génétique (64 codons), affichée progressivement en 4 sous-tableaux
(un par 1re base U/C/A/G) pour rester lisible à l'écran.
Source : 1ereC/SVT.pdf, pages 48-49.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, ORIGIN, Rectangle, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


# --- Données complètes du code génétique (64 codons) --------------------------
CODE_GENETIQUE = {
    "U": {
        "U": [("UUU", "Phé"), ("UUC", "Phé"), ("UUA", "Leu"), ("UUG", "Leu")],
        "C": [("UCU", "Ser"), ("UCC", "Ser"), ("UCA", "Ser"), ("UCG", "Ser")],
        "A": [("UAU", "Tyr"), ("UAC", "Tyr"), ("UAA", "Stop"), ("UAG", "Stop")],
        "G": [("UGU", "Cys"), ("UGC", "Cys"), ("UGA", "Stop"), ("UGG", "Trp")],
    },
    "C": {
        "U": [("CUU", "Leu"), ("CUC", "Leu"), ("CUA", "Leu"), ("CUG", "Leu")],
        "C": [("CCU", "Pro"), ("CCC", "Pro"), ("CCA", "Pro"), ("CCG", "Pro")],
        "A": [("CAU", "His"), ("CAC", "His"), ("CAA", "Gln"), ("CAG", "Gln")],
        "G": [("CGU", "Arg"), ("CGC", "Arg"), ("CGA", "Arg"), ("CGG", "Arg")],
    },
    "A": {
        "U": [("AUU", "Ile"), ("AUC", "Ile"), ("AUA", "Ile"), ("AUG", "Met*")],
        "C": [("ACU", "Thr"), ("ACC", "Thr"), ("ACA", "Thr"), ("ACG", "Thr")],
        "A": [("AAU", "Asn"), ("AAC", "Asn"), ("AAA", "Lys"), ("AAG", "Lys")],
        "G": [("AGU", "Ser"), ("AGC", "Ser"), ("AGA", "Arg"), ("AGG", "Arg")],
    },
    "G": {
        "U": [("GUU", "Val"), ("GUC", "Val"), ("GUA", "Val"), ("GUG", "Val")],
        "C": [("GCU", "Ala"), ("GCC", "Ala"), ("GCA", "Ala"), ("GCG", "Ala")],
        "A": [("GAU", "Asp"), ("GAC", "Asp"), ("GAA", "Glu"), ("GAG", "Glu")],
        "G": [("GGU", "Gly"), ("GGC", "Gly"), ("GGA", "Gly"), ("GGG", "Gly")],
    },
}
ORDRE_BASES = "UCAG"


def _header_cell(text, w, h, fill="#2A2A2A"):
    rect = Rectangle(width=w, height=h, fill_color=fill, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1)
    txt = Text(text, font_size=14, color=YELLOW, weight="BOLD")
    if txt.width > w - 0.1:
        txt.scale((w - 0.1) / txt.width)
    txt.move_to(rect.get_center())
    return VGroup(rect, txt)


def _codon_cell(codon, aa, w, h):
    is_stop = aa == "Stop"
    is_start = aa == "Met*"
    if is_stop:
        fill = "#B42E41"
    elif is_start or aa == "Trp":
        fill = "#267540"
    else:
        fill = "#1E5FA8"
    rect = Rectangle(width=w, height=h, fill_color=fill, fill_opacity=0.35, stroke_color=WHITE, stroke_width=1)
    codon_txt = Text(codon, font_size=15, color=WHITE, weight="BOLD")
    aa_affiche = "Stop" if is_stop else ("Met (init)" if is_start else aa)
    aa_txt = Text(aa_affiche, font_size=12, color=YELLOW if (is_stop or is_start) else WHITE)
    contenu = VGroup(codon_txt, aa_txt).arrange(DOWN, buff=0.03)
    if contenu.width > w - 0.1:
        contenu.scale((w - 0.1) / contenu.width)
    contenu.move_to(rect.get_center())
    return VGroup(rect, contenu)


def _build_subtable(premiere_base):
    """Sous-tableau 5x5 : coin = 1re base, ligne d'en-tête = 3e base,
    colonne d'en-tête = 2e base, 16 cellules codon/acide aminé."""
    w, h = 1.65, 0.85
    grid = VGroup()

    corner = _header_cell(f"1re base\n= {premiere_base}", w, h, fill="#111111")
    corner.move_to([0, 0, 0])
    grid.add(corner)

    for j, b3 in enumerate(ORDRE_BASES):
        cell = _header_cell(f"3e base\n{b3}", w, h)
        cell.move_to([(j + 1) * w, 0, 0])
        grid.add(cell)

    for i, b2 in enumerate(ORDRE_BASES):
        rh = _header_cell(f"2e base\n{b2}", w, h)
        rh.move_to([0, -(i + 1) * h, 0])
        grid.add(rh)
        for j, b3 in enumerate(ORDRE_BASES):
            codon, aa = CODE_GENETIQUE[premiere_base][b2][j]
            cell = _codon_cell(codon, aa, w, h)
            cell.move_to([(j + 1) * w, -(i + 1) * h, 0])
            grid.add(cell)

    grid.move_to(ORIGIN)
    return grid


class LeCodeGenetique(NotionScene):
    def construct(self):
        titre = scene_title("IV — Le code génétique")
        titre.scale(0.6)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "L'ARN messager ne porte que quatre lettres, A, U, G et C, "
                "alors qu'il faut coder vingt acides aminés différents. "
                "Comment est-ce possible ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : le problème posé -------------------------------------------
        ligne1 = MathTex(r"1\ \text{base} \Rightarrow 4^1 = 4\ \text{combinaisons (insuffisant)}", font_size=26, color=WHITE)
        ligne2 = MathTex(r"2\ \text{bases} \Rightarrow 4^2 = 16\ \text{combinaisons (insuffisant)}", font_size=26, color=WHITE)
        ligne3 = MathTex(r"3\ \text{bases} \Rightarrow 4^3 = 64\ \text{combinaisons (largement suffisant)}", font_size=26, color=YELLOW)
        calcul = VGroup(ligne1, ligne2, ligne3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        calcul.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Si une seule base codait un acide aminé, on n'aurait que "
                "quatre possibilités : insuffisant. Si deux bases codaient "
                "un acide aminé, quatre fois quatre, soit seize "
                "combinaisons : encore insuffisant. Mais si trois bases "
                "codent un acide aminé, quatre fois quatre fois quatre, "
                "soit soixante-quatre combinaisons : c'est largement "
                "suffisant pour coder vingt acides aminés. L'information est "
                "donc lue par groupes de trois nucléotides, appelés codons."
            )
        ) as tracker:
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul))

        definition = definition_box(
            Text(
                _wrap(
                    "Un codon est une suite de trois nucléotides "
                    "consécutifs de l'ARNm qui correspond à un acide aminé "
                    "déterminé (ou à un signal de fin de traduction). La "
                    "lecture se fait sans chevauchement : chaque nucléotide "
                    "n'appartient qu'à un seul codon.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un codon est une suite de trois nucléotides consécutifs de "
                "l'ARNm, qui correspond à un acide aminé déterminé, ou à un "
                "signal de fin de traduction. La lecture se fait sans "
                "chevauchement : chaque nucléotide n'appartient qu'à un seul "
                "codon."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : la table complète, en 4 sous-tableaux ----------------
        entete_table = Text("La table du code génétique (64 codons)", font_size=24, color=YELLOW, weight="BOLD")
        entete_table.next_to(titre, DOWN, buff=0.4)

        methode_lecture = Text(
            "Lecture : 1re base = sous-tableau, 2e base = ligne, 3e base = colonne",
            font_size=17,
            color=WHITE,
        )
        methode_lecture.next_to(entete_table, DOWN, buff=0.2)

        narrations = {
            "U": (
                "Voici le premier sous-tableau, pour une première base U. "
                "En ligne, la deuxième base ; en colonne, la troisième base. "
                "Par exemple, U U U code la phénylalanine. Repérez aussi "
                "trois cases en rouge : U A A, U A G et U G A sont des "
                "codons stop, qui arrêtent la traduction. Et U G G, en vert, "
                "est le seul codon du tryptophane."
            ),
            "C": (
                "Deuxième sous-tableau, pour une première base C : que des "
                "acides aminés, aucun codon stop ici. C U U à C U G codent "
                "tous la leucine ; C C U à C C G codent tous la proline ; C "
                "A U et C A C codent l'histidine, C A A et C A G la "
                "glutamine ; et toute la ligne C G codent l'arginine."
            ),
            "A": (
                "Troisième sous-tableau, pour une première base A. Repérez "
                "la case en vert, A U G : c'est le codon d'initiation, qui "
                "code la méthionine et marque toujours le début de la "
                "traduction. Les autres cases codent l'isoleucine, la "
                "thréonine, l'asparagine, la lysine, ou encore la sérine et "
                "l'arginine pour la dernière ligne."
            ),
            "G": (
                "Quatrième et dernier sous-tableau, pour une première base "
                "G : là encore, que des acides aminés. La valine, "
                "l'alanine, l'acide aspartique, l'acide glutamique, et la "
                "glycine pour toute la dernière ligne. La table complète des "
                "soixante-quatre codons est maintenant sous vos yeux."
            ),
        }

        with self.voiceover(text="Pour rester lisible, la table est découpée en quatre parties, une par première base : U, C, A, puis G.") as tracker:
            self.play(FadeIn(entete_table), FadeIn(methode_lecture))
            self.wait(tracker.get_remaining_duration())

        bas_visible = -config.frame_height / 2 + 0.3
        haut_disponible = methode_lecture.get_bottom()[1] - 0.25

        sous_tableau_precedent = None
        for premiere_base in ORDRE_BASES:
            sous_tableau = _build_subtable(premiere_base)
            sous_tableau.next_to(methode_lecture, DOWN, buff=0.3)

            # Garde-fou d'auto-scale : si le sous-tableau déborde la zone
            # visible sous l'en-tête, on le réduit pour qu'il tienne à l'écran.
            hauteur_dispo = haut_disponible - bas_visible
            if sous_tableau.height > hauteur_dispo:
                sous_tableau.scale(hauteur_dispo / sous_tableau.height, about_point=sous_tableau.get_top())
            largeur_dispo = config.frame_width - 0.6
            if sous_tableau.width > largeur_dispo:
                sous_tableau.scale(largeur_dispo / sous_tableau.width)
                sous_tableau.next_to(methode_lecture, DOWN, buff=0.3)

            with self.voiceover(text=narrations[premiere_base]) as tracker:
                if sous_tableau_precedent is not None:
                    self.play(FadeOut(sous_tableau_precedent), FadeIn(sous_tableau))
                else:
                    self.play(FadeIn(sous_tableau))
                self.wait(tracker.get_remaining_duration())

            sous_tableau_precedent = sous_tableau

        self.play(FadeOut(sous_tableau_precedent), FadeOut(entete_table), FadeOut(methode_lecture))

        # --- À retenir --------------------------------------------------------------
        essentiel = definition_box(
            Text(
                _wrap(
                    "La table du code génétique associe à chacun des 64 "
                    "codons possibles un acide aminé (ou un signal stop). "
                    "Elle sera notre outil de référence pour traduire tout "
                    "ARNm dans les scènes suivantes.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la table du code génétique associe "
                "à chacun des soixante-quatre codons possibles un acide "
                "aminé, ou un signal stop. Ce sera notre outil de référence "
                "pour traduire n'importe quel ARNm dans les scènes "
                "suivantes."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
