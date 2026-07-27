"""
scenes/Physique_TravailPuissanceRotation_08.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 08.

§ Applications : le treuil (rayon r, couple moteur T×r = mgr, travail
W = mgh, puissance P = mgv = Tv), le pédalier (moment maximal manivelle
horizontale, nul au point mort), machines simples (levier F×dF = R×dR,
poulie fixe, treuil à manivelle F×L = T×r), tableau récapitulatif
translation/rotation.
Source : 1ereC/Physique.pdf, chapitre 2, pages 13-23.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=24, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.06)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class ApplicationsTreuilPedalierMachines(NotionScene):
    def construct(self):
        titre = scene_title("Applications : treuil, pédalier, machines simples")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Treuil de puits, pédalier de vélo, levier : comment le "
                "travail et la puissance de rotation s'y appliquent-ils ?",
                width=54,
            ),
            font_size=23,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le treuil d'un puits, le pédalier d'un vélo, le levier "
                "d'un ouvrier : ce sont toutes des machines qui exploitent "
                "le moment d'une force. Voyons comment nos formules de "
                "travail et de puissance s'y appliquent concrètement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Le treuil --------------------------------------------------------------
        centre = LEFT * 3.4 + DOWN * 1.3
        tambour = Circle(radius=0.6, color="#595959", stroke_width=4).move_to(centre)
        corde = Line(centre + DOWN * 0.6, centre + DOWN * 2.2, color=WHITE, stroke_width=3)
        seau = Rectangle(width=0.5, height=0.4, color="#DE7C1F", fill_color="#DE7C1F", fill_opacity=1)
        seau.move_to(centre + DOWN * 2.4)
        manivelle = Line(centre, centre + RIGHT * 0.9, color="#1E5FA8", stroke_width=5)
        force_t = Vector(UP * 0.7, color="#1E5FA8").shift(centre + RIGHT * 0.9)
        r_lbl = MathTex("r", font_size=22).next_to(Line(centre, centre + DOWN * 0.6), LEFT, buff=0.1)
        schema_treuil = VGroup(tambour, corde, seau, manivelle, force_t, Dot(centre, color=YELLOW, radius=0.05), r_lbl)
        schema_treuil.scale(0.85)

        treuil_txt = property_box(
            VGroup(
                Text("Le treuil (rayon r) :", font_size=21, weight="BOLD"),
                MathTex(r"\text{couple moteur} = T \times r = m\,g\,r", font_size=23),
                MathTex(r"W = m\,g\,h \qquad P = m\,g\,v = T \times v", font_size=23),
            ).arrange(DOWN, buff=0.22),
            box_width=6.4,
        )
        treuil_txt.next_to(schema_treuil, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Le treuil enroule une corde sur un tambour de rayon r "
                "pour remonter une charge de masse m. Le couple moteur "
                "nécessaire vaut T fois r, égal à m g r à vitesse "
                "constante. Le travail fourni pour monter la charge d'une "
                "hauteur h vaut simplement m g h, et la puissance "
                "développée vaut m g v, c'est-à-dire T fois v — on "
                "retrouve ici le lien direct entre rotation du tambour et "
                "translation de la charge."
            )
        ) as tracker:
            self.play(Create(schema_treuil))
            self.play(FadeIn(treuil_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_treuil), FadeOut(treuil_txt))

        # --- Le pédalier --------------------------------------------------------------
        centre2 = LEFT * 3.4 + DOWN * 1.0
        pedalier = Circle(radius=0.9, color="#288073", stroke_width=4).move_to(centre2)
        manivelle_h = Line(centre2, centre2 + RIGHT * 0.9, color=WHITE, stroke_width=5)
        force_h = Vector(DOWN * 0.9, color="#DE7C1F").shift(centre2 + RIGHT * 0.9)
        schema_ped1 = VGroup(pedalier, manivelle_h, force_h, Dot(centre2, color=YELLOW, radius=0.05))
        schema_ped1.scale(0.75)

        pedalier_txt = property_box(
            VGroup(
                Text("Le pédalier :", font_size=21, weight="BOLD"),
                Text("manivelle horizontale : moment maximal (bras de levier = manivelle).", font_size=18),
                Text("manivelle verticale (« point mort ») : moment nul.", font_size=18),
            ).arrange(DOWN, buff=0.2),
            box_width=6.6,
        )
        pedalier_txt.next_to(schema_ped1, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Sur un pédalier de vélo, le moment de la force du "
                "cycliste dépend de la position de la manivelle. Lorsque "
                "la manivelle est horizontale et la force verticale, le "
                "moment est maximal, le bras de levier étant égal à la "
                "longueur de la manivelle. Mais lorsque la manivelle est "
                "verticale — c'est le fameux point mort — le bras de "
                "levier s'annule, et le moment aussi : le cycliste pousse "
                "sans faire tourner le pédalier."
            )
        ) as tracker:
            self.play(Create(schema_ped1))
            self.play(FadeIn(pedalier_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_ped1), FadeOut(pedalier_txt))

        # --- Machines simples : levier, poulie fixe, treuil à manivelle ---------
        machines = property_box(
            VGroup(
                Text("Machines simples", font_size=22, weight="BOLD"),
                MathTex(r"\text{Levier : } F \times d_F = R \times d_R \ \Rightarrow\ \text{gain en force si } d_F > d_R", font_size=22),
                Text("Poulie fixe : change la direction de la force, sans gain en intensité.", font_size=19),
                MathTex(r"\text{Treuil à manivelle : } F \times L = T \times r", font_size=22),
            ).arrange(DOWN, buff=0.24),
            box_width=10.8,
        )
        machines.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "D'autres machines simples exploitent le même principe. "
                "Le levier : F fois d indice F égale R fois d indice R, "
                "ce qui permet de multiplier la force si le bras d'action "
                "d indice F est plus grand que le bras de résistance d "
                "indice R. La poulie fixe, elle, ne fait que changer la "
                "direction de la force, sans en changer l'intensité. Et le "
                "treuil à manivelle vérifie F fois L égale T fois r, où L "
                "est la longueur de la manivelle et r le rayon du tambour "
                "— plus L est grand par rapport à r, plus l'effort à "
                "fournir est réduit."
            )
        ) as tracker:
            self.play(FadeIn(machines))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(machines))

        # --- Exemple traité : treuil à manivelle -------------------------------------
        exemple = example_box(
            VGroup(
                Text("Exemple — treuil à manivelle L = 40 cm, tambour r = 8 cm, charge m = 25 kg :", font_size=18),
                MathTex(r"T = m\,g = 25\times10 = 250\ \text{N}", font_size=23),
                MathTex(r"F = \dfrac{T\times r}{L} = \dfrac{250\times0{,}08}{0{,}40} = 50\ \text{N}", font_size=24),
            ).arrange(DOWN, buff=0.26),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : un treuil à manivelle de quarante centimètres "
                "de long, avec un tambour de huit centimètres de rayon, "
                "remonte une charge de vingt-cinq kilogrammes. La tension "
                "nécessaire dans la corde vaut T égale m g, soit deux "
                "cent cinquante newtons. La force à exercer sur la "
                "manivelle vaut F égale T fois r sur L, soit deux cent "
                "cinquante fois zéro virgule zéro huit, sur zéro virgule "
                "quarante, c'est-à-dire seulement cinquante newtons : la "
                "manivelle multiplie la force par cinq."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : tableau récapitulatif translation / rotation --------------
        tableau = VGroup(
            Text("Translation ⟷ Rotation", font_size=22, weight="BOLD"),
            Text("Déplacement : x ⟷ θ (rad)", font_size=19),
            Text("Vitesse : v ⟷ ω (rad/s)", font_size=19),
            Text("Cause du mouvement : F⃗ ⟷ ℳΔ(F⃗)", font_size=19),
            Text("Travail : W = F×d ⟷ W = ℳ×Δθ", font_size=19),
            Text("Puissance : P = F×v ⟷ P = ℳ×ω", font_size=19),
            Text("Équilibre : ΣF⃗ = 0⃗ ⟷ ΣℳΔ = 0", font_size=19),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        retenir = essentiel_box(tableau, box_width=9.0)
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : la rotation possède un vocabulaire tout à "
                "fait parallèle à celui de la translation. Le déplacement "
                "x devient l'angle thêta, la vitesse v devient la vitesse "
                "angulaire oméga, la force F devient le moment de la "
                "force, le travail F fois d devient ℳ fois delta thêta, "
                "la puissance F fois v devient ℳ fois oméga, et la "
                "condition d'équilibre somme des forces nulle devient "
                "somme des moments nulle."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : dans un treuil, ne pas confondre le rayon r "
                    "du tambour (charge) et la longueur L de la manivelle "
                    "(force appliquée) — ce sont deux bras de levier "
                    "différents."
                ),
                font_size=21,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : dans un treuil à manivelle, il ne faut "
                "surtout pas confondre le rayon r du tambour, qui sert "
                "pour la charge, et la longueur L de la manivelle, qui "
                "sert pour la force appliquée par l'utilisateur — ce sont "
                "deux bras de levier bien différents, et c'est leur "
                "rapport qui donne le gain en force de la machine."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
