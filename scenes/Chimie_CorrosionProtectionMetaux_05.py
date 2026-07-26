"""
scenes/Chimie_CorrosionProtectionMetaux_05.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 05.

§ 5. Mécanisme simplifié de la corrosion humide : les micropiles. Notion
de micropile de corrosion (goutte d'eau = électrolyte, zone anodique au
centre pauvre en O2, zone cathodique sur les bords riche en O2),
demi-équations (anode : Fe → Fe2+ + 2e- ; cathode : O2 + 2H2O + 4e- →
4OH-). Schéma de la micropile construit avec des primitives Manim de base.
Source : 1ereC/Chimie.pdf, chapitre 15, pages 147-148.
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
    BLUE,
    GREY_B,
    FadeIn,
    FadeOut,
    Arrow,
    Circle,
    Ellipse,
    MathTex,
    Rectangle,
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


def _schema_micropile():
    """Goutte d'eau sur une plaque de fer : zone anodique (centre, pauvre
    en O2) et zone cathodique (bords, riche en O2). Primitives de base
    uniquement (Ellipse, Circle, Rectangle, Arrow, MathTex, VGroup)."""
    plaque = Rectangle(width=6.5, height=0.5, fill_color=GREY_B, fill_opacity=1, stroke_width=1.5, stroke_color=WHITE)

    goutte = Ellipse(width=5.2, height=1.6, fill_color=BLUE, fill_opacity=0.35, stroke_color=BLUE, stroke_width=2)
    goutte.next_to(plaque, UP, buff=-0.15)

    zone_anodique = Circle(radius=0.55, fill_color=ORANGE, fill_opacity=0.6, stroke_width=0)
    zone_anodique.move_to(goutte.get_center() + DOWN * 0.15)
    label_anode = Text("anode\n(centre, pauvre en O2)", font_size=14, color=WHITE, line_spacing=0.8)
    label_anode.move_to(zone_anodique.get_center())

    zone_cathodique_g = Ellipse(width=1.5, height=1.3, fill_color="#288073", fill_opacity=0.6, stroke_width=0)
    zone_cathodique_g.move_to(goutte.get_left() + RIGHT * 0.55)
    zone_cathodique_d = Ellipse(width=1.5, height=1.3, fill_color="#288073", fill_opacity=0.6, stroke_width=0)
    zone_cathodique_d.move_to(goutte.get_right() + LEFT * 0.55)

    label_cathode_g = Text("cathode\n(bord, riche\nen O2)", font_size=13, color=WHITE, line_spacing=0.8)
    label_cathode_g.move_to(zone_cathodique_g.get_center())
    label_cathode_d = Text("cathode\n(bord, riche\nen O2)", font_size=13, color=WHITE, line_spacing=0.8)
    label_cathode_d.move_to(zone_cathodique_d.get_center())

    fleche_e = Arrow(
        zone_anodique.get_center() + UP * 0.1,
        zone_cathodique_d.get_center() + UP * 0.1,
        color=YELLOW, stroke_width=3, buff=0.35, max_tip_length_to_length_ratio=0.15,
    )
    label_e = MathTex("e^{-}", font_size=22, color=YELLOW)
    label_e.next_to(fleche_e, UP, buff=0.1)

    label_plaque = Text("plaque de fer", font_size=15, color=WHITE)
    label_plaque.next_to(plaque, DOWN, buff=0.2)

    schema = VGroup(
        plaque, goutte,
        zone_cathodique_g, zone_cathodique_d, zone_anodique,
        label_cathode_g, label_cathode_d, label_anode,
        fleche_e, label_e,
        label_plaque,
    )
    return schema


class MicropilesCorrosionHumide(NotionScene):
    def construct(self):
        titre = scene_title("15.5 Mécanisme de la corrosion humide : les micropiles")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : la goutte d'eau, un vrai petit circuit électrique --------
        enonce = Text(
            _wrap(
                "Comment expliquer précisément, à l'échelle microscopique, "
                "que le fer perde ses électrons sous une simple goutte "
                "d'eau ? La réponse : une goutte d'eau posée sur du fer "
                "se comporte comme une minuscule pile électrique.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment expliquer précisément, à l'échelle microscopique, "
                "que le fer perde ses électrons sous une simple goutte "
                "d'eau ? La réponse est surprenante : une goutte d'eau "
                "posée sur une surface de fer se comporte comme une "
                "minuscule pile électrique, qu'on appelle une micropile "
                "de corrosion."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : schéma de la micropile ------------------------------
        entete_schema = Text("La micropile de corrosion sur une goutte d'eau", font_size=20, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.3)

        schema = _schema_micropile()
        schema.next_to(entete_schema, DOWN, buff=0.35)
        groupe_schema = VGroup(entete_schema, schema)
        _fit(groupe_schema, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "La goutte d'eau joue le rôle d'électrolyte. Au centre de "
                "la goutte, le dioxygène dissous a du mal à arriver : "
                "cette zone, pauvre en dioxygène, devient la zone "
                "anodique. Sur les bords de la goutte, en contact direct "
                "avec l'air, le dioxygène est abondant : ces zones, "
                "riches en dioxygène, deviennent les zones cathodiques. "
                "Les électrons libérés au centre migrent, à travers le "
                "métal, vers les bords."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : les deux demi-équations ---------------------------
        entete_eq = Text("Les deux demi-équations électroniques", font_size=21, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.35)

        anode_eq = MathTex(
            r"\text{Anode (centre) : } Fe \;\longrightarrow\; Fe^{2+} + 2e^{-}",
            font_size=27, color=ORANGE,
        )
        cathode_eq = MathTex(
            r"\text{Cathode (bords) : } O_2 + 2H_2O + 4e^{-} \;\longrightarrow\; 4OH^{-}",
            font_size=27, color="#288073",
        )
        equations = VGroup(anode_eq, cathode_eq).arrange(DOWN, buff=0.4)
        equations.next_to(entete_eq, DOWN, buff=0.4)
        groupe_eq = VGroup(entete_eq, equations)
        _fit(groupe_eq, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Écrivons les deux demi-équations électroniques. À "
                "l'anode, au centre de la goutte, le fer s'oxyde : F-e "
                "donne F-e deux plus, plus deux électrons. À la cathode, "
                "sur les bords, le dioxygène capte ces électrons en "
                "présence d'eau, selon : O-deux, plus deux H-deux-O, plus "
                "quatre électrons, donne quatre ions hydroxyde O-H moins."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(anode_eq))
            self.play(Write(cathode_eq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_eq))

        # --- À retenir : ce qu'est une micropile de corrosion -------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une micropile de corrosion est un ensemble anode / "
                    "cathode qui se forme spontanément sur un même métal, "
                    "dès qu'une hétérogénéité (accès inégal au dioxygène, "
                    "impureté…) crée deux zones de réactivité différente.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.45)
        _fit(definition, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Retenons la définition générale : une micropile de "
                "corrosion est un ensemble anode-cathode qui se forme "
                "spontanément sur un même métal, dès qu'une "
                "hétérogénéité — ici un accès inégal au dioxygène, mais "
                "cela peut aussi être une impureté ou un défaut de "
                "surface — crée deux zones de réactivité différente."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas inverser les rôles : c'est la zone PAUVRE en "
                    "O2 (le centre, difficile d'accès) qui est l'anode où "
                    "le fer se dissout, et la zone RICHE en O2 (les bords) "
                    "qui est la cathode où le fer est préservé.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Attention à un piège classique : il ne faut pas inverser "
                "les rôles. C'est la zone pauvre en dioxygène, le centre, "
                "difficile d'accès pour l'air, qui devient l'anode où le "
                "fer se dissout réellement. La zone riche en dioxygène, "
                "sur les bords, devient la cathode, où le fer, lui, est "
                "préservé."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
