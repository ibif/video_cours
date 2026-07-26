"""
scenes/Chimie_CorrosionProtectionMetaux_08.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 08.

§ 8. La protection cathodique : anode sacrificielle. definition_box de la
protection cathodique (bloc de métal plus réducteur, Mg ou Zn),
demi-équations (anode : Mg → Mg2+ + 2e- ; cathode : O2 + 2H2O + 4e- →
4OH- sur le fer non attaqué). Applications (coques de navires/pirogues,
pipelines enterrés, chauffe-eau, ouvrages portuaires d'Abidjan), schéma du
pipeline protégé construit avec des primitives Manim de base. Exemple
résolu 3 : calcul de la masse de magnésium consommée pour protéger 16,8 g
de fer (≈ 7,3 g).
Source : 1ereC/Chimie.pdf, pages 150-151.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    ORANGE,
    FadeIn,
    FadeOut,
    Arrow,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


def _schema_pipeline():
    """Pipeline enterré protégé par une anode sacrificielle de magnésium
    reliée par un fil conducteur. Primitives Manim de base uniquement
    (Rectangle, Line, Arrow, MathTex, VGroup)."""
    sol = Rectangle(width=9.0, height=2.0, fill_color="#4a3524", fill_opacity=0.5, stroke_width=0)
    sol.to_edge(DOWN, buff=0.6)

    tuyau = Rectangle(width=7.5, height=0.55, fill_color="#595959", fill_opacity=1, stroke_color=WHITE, stroke_width=1.5)
    tuyau.move_to(sol.get_center() + UP * 0.3)
    label_tuyau = Text("pipeline (fer)", font_size=15, color=WHITE)
    label_tuyau.next_to(tuyau, UP, buff=0.15)

    anode = Rectangle(width=0.8, height=0.8, fill_color=ORANGE, fill_opacity=1, stroke_color=WHITE, stroke_width=1.5)
    anode.move_to(sol.get_center() + DOWN * 0.4 + LEFT * 2.5)
    label_anode = Text("Mg\n(anode\nsacrificielle)", font_size=13, color=WHITE, line_spacing=0.8)
    label_anode.next_to(anode, DOWN, buff=0.15)

    fil = Line(anode.get_top(), tuyau.get_left() + LEFT * 0.1, color=YELLOW, stroke_width=2.5)
    fil.shift(UP * 0.1)

    fleche_e = Arrow(
        anode.get_center() + UP * 0.5, tuyau.get_left() + UP * 0.1,
        color=YELLOW, stroke_width=2.5, buff=0.4, max_tip_length_to_length_ratio=0.2,
    )
    label_e = MathTex("e^{-}", font_size=18, color=YELLOW)
    label_e.next_to(fleche_e, UP, buff=0.08)

    schema = VGroup(sol, tuyau, label_tuyau, anode, label_anode, fleche_e, label_e)
    return schema


class ProtectionCathodiqueAnodeSacrificielle(NotionScene):
    def construct(self):
        titre = scene_title("15.8 La protection cathodique : anode sacrificielle")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : définition --------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La protection cathodique par anode sacrificielle "
                    "consiste à relier électriquement le fer à un bloc "
                    "d'un métal plus réducteur (magnésium ou zinc), qui "
                    "s'oxyde à la place du fer et le préserve.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La protection cathodique par anode sacrificielle "
                "consiste à relier électriquement l'objet en fer à un "
                "bloc d'un métal plus réducteur, du magnésium ou du "
                "zinc. Ce bloc s'oxyde volontairement à la place du fer, "
                "et le préserve totalement de la corrosion, tant qu'il "
                "n'est pas entièrement consommé."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : demi-équations ----------------------------------------
        entete_eq = Text("Les deux demi-équations", font_size=21, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.35)

        anode_eq = MathTex(
            r"\text{Anode (Mg) : } Mg \;\longrightarrow\; Mg^{2+} + 2e^{-}",
            font_size=27, color=ORANGE,
        )
        cathode_eq = MathTex(
            r"\text{Cathode (fer, non attaqué) : } O_2 + 2H_2O + 4e^{-} \;\longrightarrow\; 4OH^{-}",
            font_size=25, color="#288073",
        )
        equations = VGroup(anode_eq, cathode_eq).arrange(DOWN, buff=0.4)
        equations.next_to(entete_eq, DOWN, buff=0.4)
        groupe_eq = VGroup(entete_eq, equations)
        _fit(groupe_eq, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Le mécanisme reprend exactement celui de la micropile, "
                "mais à l'échelle d'un ouvrage entier. À l'anode, le "
                "magnésium s'oxyde : M-g donne M-g deux plus, plus deux "
                "électrons. Ces électrons circulent jusqu'au fer, qui "
                "devient la cathode : là, le dioxygène les capte en "
                "présence d'eau, sans que le fer lui-même ne soit "
                "attaqué."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(anode_eq))
            self.play(Write(cathode_eq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_eq))

        # --- Exemple traité : applications + schéma du pipeline --------------------
        entete_appli = Text("Applications concrètes", font_size=20, color=YELLOW, weight="BOLD")
        entete_appli.next_to(titre, DOWN, buff=0.3)

        applications = _bullets(
            [
                "coques de navires et pirogues",
                "pipelines enterrés",
                "chauffe-eau (cuve intérieure)",
                "ouvrages portuaires d'Abidjan (quais, jetées)",
            ],
            font_size=19,
        )
        applications.next_to(entete_appli, DOWN, buff=0.25)

        schema = _schema_pipeline()
        schema.scale(0.85)
        schema.next_to(applications, DOWN, buff=0.3)

        groupe_appli = VGroup(entete_appli, applications, schema)
        _fit(groupe_appli, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Cette méthode protège de nombreux ouvrages en fer ou en "
                "acier : les coques de navires et de pirogues, les "
                "pipelines enterrés, la cuve intérieure des chauffe-eau, "
                "ou encore les ouvrages portuaires d'Abidjan, quais et "
                "jetées, exposés en permanence à l'air marin. Sur un "
                "pipeline, un bloc de magnésium est relié par un fil "
                "conducteur au métal du tuyau, et s'oxyde à sa place."
            )
        ) as tracker:
            self.play(FadeIn(entete_appli))
            self.play(FadeIn(applications))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_appli))

        # --- À retenir : exemple résolu 3, calcul de masse -------------------------
        exemple = example_box(
            VGroup(
                Text(
                    "Quelle masse de magnésium est consommée pour protéger",
                    font_size=19, weight="BOLD",
                ),
                Text("16,8 g de fer ? (M(Fe)=56 ; M(Mg)=24,3 g/mol)", font_size=19, weight="BOLD"),
                MathTex(r"n(Fe) = \frac{m(Fe)}{M(Fe)} = \frac{16{,}8}{56} = 0{,}3\ mol", font_size=22),
                Text("Anode sacrificielle : n(Mg) = n(Fe) (pas de coefficient 2)", font_size=18, color=GREEN),
                MathTex(r"m(Mg) = n(Mg)\times M(Mg) = 0{,}3 \times 24{,}3 \approx 7{,}3\ g", font_size=22, color=ORANGE),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.35)
        _fit(exemple, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Exemple résolu : quelle masse de magnésium est "
                "consommée pour protéger seize virgule huit grammes de "
                "fer ? On calcule d'abord la quantité de matière de fer "
                "à protéger : n égale m sur M, soit seize virgule huit "
                "divisé par cinquante-six, ce qui donne zéro virgule "
                "trois mole. Pour une anode sacrificielle, chaque atome "
                "de magnésium cède exactement deux électrons, tout comme "
                "chaque atome de fer en aurait cédé deux s'il s'était "
                "oxydé : la quantité de matière de magnésium consommée "
                "est donc égale à celle du fer, sans coefficient deux. "
                "On obtient enfin la masse : zéro virgule trois fois "
                "vingt-quatre virgule trois, soit environ sept virgule "
                "trois grammes de magnésium."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas multiplier n(Mg) par 2 : Mg et Fe cèdent "
                    "chacun exactement 2 électrons par atome, donc n(Mg) "
                    "= n(Fe), et non 2×n(Fe).",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Piège fréquent à éviter dans ce type de calcul : ne pas "
                "multiplier n de magnésium par deux. Le magnésium et le "
                "fer cèdent chacun exactement deux électrons par atome, "
                "donc leurs quantités de matière sont directement "
                "égales, et non dans un rapport de deux."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
