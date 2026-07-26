"""
scenes/Chimie_ClassificationQualitativeRedox_03.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 03.

§ 2. Construction expérimentale d'une classification qualitative :
principe de la méthode (plonger un métal M₂ dans une solution d'ions
M₁ⁿ⁺, observer s'il y a réaction ou non). Exemple résolu 2 : trois
expériences (Zn/Cu²⁺ réagit, Cu/Ag⁺ réagit, Cu/Zn²⁺ ne réagit pas) →
classement Ag < Cu < Zn. Classement général des métaux usuels par pouvoir
réducteur décroissant : Mg > Zn > Fe > Ni > Sn > Pb > Cu > Ag > Au.
Source : 1ereC/Chimie.pdf, chapitre 10, pages 95-96.
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
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, property_box, scene_title, warning_box


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


class ConstructionClassificationQualitative(NotionScene):
    def construct(self):
        titre = scene_title("10.2 Construire une classification qualitative")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : principe de la méthode ---------------------------------
        intro = Text(
            _wrap(
                "Peut-on classer TOUS les métaux usuels selon leur pouvoir "
                "réducteur, et pas seulement comparer le fer et le cuivre ? "
                "Oui, en généralisant la méthode des deux scènes "
                "précédentes.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Peut-on classer tous les métaux usuels selon leur pouvoir "
                "réducteur, et pas seulement comparer le fer et le cuivre ? "
                "Oui, en généralisant la méthode utilisée dans les scènes "
                "précédentes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : méthode -------------------------------------------
        principe = method_box(
            VGroup(
                Text("Pour comparer deux métaux M₁ et M₂ :", font_size=22, weight="BOLD"),
                Text("1. Plonger une lame de M₂ dans une solution d'ions M₁ⁿ⁺.", font_size=20),
                Text("2. Observer : dépôt métallique et/ou décoloration = réaction.", font_size=20),
                Text("3. Si réaction, M₂ est le réducteur le plus fort.", font_size=20),
                Text("4. Répéter par paires pour classer plusieurs métaux.", font_size=20),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.6,
        )
        principe.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode : pour comparer deux métaux M-un et M-deux, on "
                "plonge une lame de M-deux dans une solution contenant les "
                "ions M-un. On observe : un dépôt métallique, ou une "
                "décoloration de la solution, signe qu'une réaction a eu "
                "lieu. Si une réaction se produit, M-deux est le réducteur "
                "le plus fort des deux. En répétant l'expérience par paires "
                "de métaux, on peut classer plusieurs métaux les uns par "
                "rapport aux autres."
            )
        ) as tracker:
            self.play(FadeIn(principe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(principe))

        # --- Exemple traité : trois expériences --------------------------------
        entete_ex = Text("Exemple résolu 2 — Classer argent, cuivre et zinc", font_size=21, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.35)

        lignes = VGroup(
            MathTex(r"\text{Zn dans } Cu^{2+} : \text{réaction} \Rightarrow Zn \text{ plus réducteur que } Cu", font_size=22, color=WHITE),
            MathTex(r"\text{Cu dans } Ag^{+} : \text{réaction} \Rightarrow Cu \text{ plus réducteur que } Ag", font_size=22, color=WHITE),
            MathTex(r"\text{Cu dans } Zn^{2+} : \text{pas de réaction} \Rightarrow Cu \text{ moins réducteur que } Zn", font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        lignes.next_to(entete_ex, DOWN, buff=0.4)
        _fit(VGroup(entete_ex, lignes), titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Réalisons trois expériences. Première expérience : du zinc "
                "plongé dans une solution d'ions cuivre deux réagit ; le "
                "zinc est donc plus réducteur que le cuivre. Deuxième "
                "expérience : du cuivre plongé dans une solution d'ions "
                "argent réagit ; le cuivre est donc plus réducteur que "
                "l'argent. Troisième expérience : du cuivre plongé dans une "
                "solution d'ions zinc deux ne réagit pas, ce qui confirme "
                "que le cuivre est moins réducteur que le zinc."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(lignes[0]))
            self.play(Write(lignes[1]))
            self.play(Write(lignes[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(lignes))

        # --- Résultat : classement Ag < Cu < Zn --------------------------------
        entete_res = Text("Classement déduit", font_size=22, color=YELLOW, weight="BOLD")
        entete_res.next_to(titre, DOWN, buff=0.35)

        classement3 = MathTex(
            r"\text{pouvoir réducteur croissant : } Ag < Cu < Zn",
            font_size=28, color=ORANGE,
        )
        classement3.next_to(entete_res, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En combinant les trois résultats, on obtient un classement "
                "unique : par pouvoir réducteur croissant, argent, puis "
                "cuivre, puis zinc. L'argent est le réducteur le plus "
                "faible des trois, le zinc le plus fort."
            )
        ) as tracker:
            self.play(FadeIn(entete_res))
            self.play(Write(classement3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_res), FadeOut(classement3))

        # --- À retenir : classement général des métaux usuels ------------------
        classement_general = property_box(
            VGroup(
                Text("Classement des métaux usuels par pouvoir réducteur décroissant :", font_size=20, weight="BOLD"),
                MathTex(
                    r"Mg > Zn > Fe > Ni > Sn > Pb > Cu > Ag > Au",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=12.6,
        )
        classement_general.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "En généralisant cette méthode à tous les métaux usuels, on "
                "obtient le classement suivant, par pouvoir réducteur "
                "décroissant : magnésium, zinc, fer, nickel, étain, plomb, "
                "cuivre, argent, or. Le magnésium est le réducteur le plus "
                "fort de cette liste, l'or le plus faible : c'est pour cela "
                "que l'or reste inaltérable."
            )
        ) as tracker:
            self.play(FadeIn(classement_general))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(classement_general))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Une seule expérience isolée ne suffit jamais à classer "
                    "plusieurs métaux : il faut comparer les métaux deux à "
                    "deux, puis assembler les résultats par transitivité "
                    "(si A < B et B < C, alors A < C).",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : une seule expérience "
                "isolée ne suffit jamais à classer plusieurs métaux. Il "
                "faut comparer les métaux deux à deux, puis assembler les "
                "résultats par transitivité : si A est plus réducteur que "
                "B, et B plus réducteur que C, alors A est plus réducteur "
                "que C."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
