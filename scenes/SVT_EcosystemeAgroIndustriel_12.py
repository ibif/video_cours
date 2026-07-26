"""
scenes/SVT_EcosystemeAgroIndustriel_12.py — Chapitre 11 (1ereC, SVT), scène 12.

§ 5.2 Le cycle de l'azote (réservoir atmosphérique N2 inutilisable
directement, 6 étapes : fixation par bactéries Rhizobium en symbiose avec
les légumineuses / foudre / industrie, absorption sous forme NH4+/NO3-,
transfert, ammonification, nitrification, dénitrification), puis méthode
agronomique (rotation avec légumineuses niébé/arachide/haricot).
Source : 1ereC/SVT.pdf, pages 128-129.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, FadeIn, FadeOut, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LeCycleDeLAzote(NotionScene):
    def construct(self):
        titre = scene_title("5.2 — Le cycle de l'azote")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : réservoir atmosphérique inutilisable ---------------------
        intro = definition_box(
            Text(
                _wrap(
                    "L'azote entre dans la composition des protéines. Son "
                    "réservoir est l'atmosphère, qui contient environ 78 % "
                    "de diazote (N₂) — mais ce gaz est inutilisable "
                    "directement par la plupart des êtres vivants.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        intro.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'azote entre dans la composition des protéines. Son "
                "réservoir est l'atmosphère, qui contient environ "
                "soixante-dix-huit pour cent de diazote. Mais ce gaz est "
                "inutilisable directement par la plupart des êtres "
                "vivants : il faut d'abord le transformer."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : la fixation de l'azote (Rhizobium) ------------------
        fixation_titre = Text("Étape 1 — La fixation de l'azote", font_size=22, color=YELLOW, weight="BOLD")
        fixation_titre.next_to(titre, DOWN, buff=0.4)
        fixation = _bullets(
            [
                "Bactéries Rhizobium, en symbiose dans les nodosités des racines des légumineuses (haricot, niébé, arachide, soja).",
                "La foudre fixe aussi l'azote atmosphérique.",
                "Certaines industries fabriquent des engrais azotés.",
            ],
            font_size=20,
            width=54,
        )
        fixation.next_to(fixation_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Première étape, la fixation de l'azote atmosphérique : "
                "certaines bactéries transforment le diazote en composés "
                "azotés assimilables. Les plus connues sont les bactéries "
                "du genre Rhizobium, qui vivent en symbiose dans les "
                "nodosités des racines des légumineuses : haricot, niébé, "
                "arachide, soja, pois de terre. La foudre et certaines "
                "industries, engrais, fixent aussi l'azote."
            )
        ) as tracker:
            self.play(FadeIn(fixation_titre))
            self.play(FadeIn(fixation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(fixation_titre), FadeOut(fixation))

        # --- Exemple traité : schéma des 6 étapes du cycle ----------------------
        def _case(texte, couleur, largeur=2.5, hauteur=0.85, font_size=13):
            rect = Rectangle(width=largeur, height=hauteur, fill_color=couleur, fill_opacity=0.9, stroke_color=WHITE, stroke_width=2)
            label = Text(texte, font_size=font_size, color="#1A1A1A", weight="BOLD")
            label.move_to(rect)
            label.set(width=min(label.width, largeur - 0.15))
            return VGroup(rect, label)

        n2 = _case("N₂\natmosphérique", "#90A4AE")
        nh4 = _case("NH₄⁺\n(ammonium)", "#66BB6A")
        no3 = _case("NO₃⁻\n(nitrates)", "#42A5B5" if False else "#26A69A")
        plante = _case("Plante\n(protéines)", "#FFEE58")
        matiere_morte = _case("Matière\nazotée morte", "#8D6E63")

        rangee = VGroup(n2, nh4, no3, plante).arrange(RIGHT, buff=0.7)
        rangee.next_to(titre, DOWN, buff=0.7)
        matiere_morte.next_to(rangee, DOWN, buff=1.3).align_to(plante, RIGHT)

        f_fixation = Arrow(n2.get_right(), nh4.get_left(), buff=0.08, color="#66BB6A", stroke_width=3)
        f_nitrif = Arrow(nh4.get_right(), no3.get_left(), buff=0.08, color="#26A69A", stroke_width=3)
        f_absorption = Arrow(no3.get_right(), plante.get_left(), buff=0.08, color="#FFEE58", stroke_width=3)
        f_transfert = Arrow(plante.get_bottom(), matiere_morte.get_top(), buff=0.08, color="#8D6E63", stroke_width=3)
        f_ammonif = Arrow(matiere_morte.get_left(), nh4.get_bottom(), buff=0.1, color="#8D6E63", stroke_width=2.5)
        f_denitrif = Arrow(no3.get_top(), n2.get_top(), buff=0.1, color="#EF5350", stroke_width=2.5, path_arc=-2.2)

        label_fix = Text("fixation", font_size=12, color="#66BB6A").next_to(f_fixation, UP, buff=0.05)
        label_nitrif = Text("nitrification", font_size=12, color="#26A69A").next_to(f_nitrif, UP, buff=0.05)
        label_abs = Text("absorption", font_size=12, color="#FFEE58").next_to(f_absorption, UP, buff=0.05)
        label_transfert = Text("transfert", font_size=12, color="#8D6E63").next_to(f_transfert, RIGHT, buff=0.05)
        label_ammonif = Text("ammonification", font_size=12, color="#8D6E63").next_to(f_ammonif, DOWN, buff=0.05)
        label_denitrif = Text("dénitrification", font_size=12, color="#EF5350").next_to(f_denitrif, UP, buff=0.35)

        cycle = VGroup(
            rangee, matiere_morte,
            f_fixation, f_nitrif, f_absorption, f_transfert, f_ammonif, f_denitrif,
            label_fix, label_nitrif, label_abs, label_transfert, label_ammonif, label_denitrif,
        )
        cycle.scale(0.82)
        cycle.move_to(cycle.get_center())
        cycle.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le cycle complet en six étapes. Un : la fixation, "
                "que nous venons de voir. Deux : l'absorption — les "
                "plantes prélèvent dans le sol l'azote sous forme "
                "d'ammonium et surtout de nitrates, et fabriquent leurs "
                "protéines. Trois : le transfert — l'azote organique "
                "circule le long des chaînes alimentaires. Quatre : "
                "l'ammonification — à la mort des organismes, les "
                "décomposeurs transforment l'azote organique en ammonium. "
                "Cinq : la nitrification — des bactéries du sol oxydent "
                "l'ammonium en nitrites puis en nitrates, de nouveau "
                "assimilables. Six : la dénitrification — d'autres "
                "bactéries, en milieu pauvre en oxygène, retransforment "
                "les nitrates en diazote, qui retourne à l'atmosphère."
            )
        ) as tracker:
            self.play(FadeIn(n2))
            self.play(FadeIn(f_fixation), FadeIn(label_fix), FadeIn(nh4))
            self.play(FadeIn(f_nitrif), FadeIn(label_nitrif), FadeIn(no3))
            self.play(FadeIn(f_absorption), FadeIn(label_abs), FadeIn(plante))
            self.play(FadeIn(f_transfert), FadeIn(label_transfert), FadeIn(matiere_morte))
            self.play(FadeIn(f_ammonif), FadeIn(label_ammonif))
            self.play(FadeIn(f_denitrif), FadeIn(label_denitrif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cycle))

        # --- À retenir : point clé agronomique ------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Les légumineuses enrichissent le sol en azote grâce à "
                    "leurs bactéries symbiotiques. C'est pourquoi "
                    "l'agriculteur ivoirien a intérêt à associer ou à "
                    "alterner le niébé, l'arachide ou le haricot avec le "
                    "maïs ou le manioc : c'est le principe de la rotation "
                    "culturale et des engrais verts.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé agronomique à retenir : les légumineuses "
                "enrichissent le sol en azote grâce à leurs bactéries "
                "symbiotiques. C'est pourquoi l'agriculteur ivoirien a "
                "intérêt à associer, ou à alterner, le niébé, l'arachide "
                "ou le haricot avec le maïs ou le manioc : c'est le "
                "principe de la rotation culturale et des engrais verts, "
                "que nous détaillerons plus loin dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
