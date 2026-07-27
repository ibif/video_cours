"""
scenes/Physique_EnergieCinetique_02.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 02.

§ Énergie cinétique de rotation : cas d'un point matériel en rotation
(Ec=½mr²ω²), définition du moment d'inertie J_Δ=Σm_i r_i², définition de
l'énergie cinétique de rotation Ec=½J_Δω², cas d'un solide qui roule sans
glisser (Ec=½mv²+½J_Δω², v=Rω). Exemple résolu : tige en rotation.
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, § 2).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EnergieCinetiqueRotationMomentInertie(NotionScene):
    def construct(self):
        titre = scene_title("Énergie cinétique de rotation, moment d'inertie")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : point matériel en rotation autour d'un axe fixe -----------
        centre = LEFT * 3.2 + DOWN * 0.3
        axe_pt = Dot(centre, color=WHITE, radius=0.06)
        rayon = 1.6
        m_pt = centre + RIGHT * rayon
        bille = Dot(m_pt, color=YELLOW, radius=0.13)
        rayon_ligne = Line(centre, m_pt, color=WHITE, stroke_width=2)
        trajectoire = Circle(radius=rayon, color=WHITE, stroke_width=1.5).move_to(centre)
        omega_arc = Arc(radius=rayon + 0.35, start_angle=0, angle=PI / 3, arc_center=centre, color="#288073")
        r_label = MathTex("r", font_size=24).next_to(rayon_ligne.get_center(), UP, buff=0.1)
        omega_label = MathTex(r"\omega", font_size=26, color="#288073").next_to(omega_arc, RIGHT, buff=0.1)
        schema = VGroup(trajectoire, axe_pt, rayon_ligne, bille, omega_arc, r_label, omega_label)
        schema.move_to(LEFT * 3.0)

        mise_en_situation = Text(
            _wrap(
                "Un point matériel de masse m tourne à distance r d'un axe "
                "fixe Δ, avec une vitesse angulaire ω. Sa vitesse linéaire "
                "vaut v = rω. Quelle est son énergie cinétique ?",
                width=42,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Considérons maintenant un point matériel de masse m qui "
                "tourne à une distance r d'un axe fixe delta, avec une "
                "vitesse angulaire oméga. Sa vitesse linéaire vaut v égale "
                "r oméga. Quelle est son énergie cinétique ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(mise_en_situation))

        # --- Raisonnement : Ec = 1/2 m r^2 omega^2 --------------------------------
        raisonnement = VGroup(
            MathTex(r"E_c = \dfrac{1}{2} m v^2 \quad \text{avec} \quad v = r\omega", font_size=28),
            MathTex(r"\Longrightarrow\ E_c = \dfrac{1}{2} m r^2 \omega^2", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        raisonnement.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En reprenant l'énergie cinétique de translation, un demi "
                "m v carré, et en remplaçant v par r oméga, on obtient "
                "l'énergie cinétique de ce point matériel en rotation : un "
                "demi m r carré oméga carré."
            )
        ) as tracker:
            self.play(Write(raisonnement[0]))
            self.play(Write(raisonnement[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(raisonnement))

        # --- Définition : moment d'inertie ----------------------------------------
        def_moment = definition_box(
            VGroup(
                Text("Moment d'inertie d'un solide par rapport à un axe Δ", font_size=23, weight="BOLD"),
                MathTex(r"J_\Delta = \sum_i m_i r_i^2", font_size=32),
                Text("m_i : masse de chaque élément, r_i : sa distance à Δ (en kg·m²)", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        def_moment.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour un solide entier, on décompose sa masse en petits "
                "éléments m indice i, situés chacun à une distance r "
                "indice i de l'axe delta, et on définit le moment "
                "d'inertie J delta comme la somme de chaque masse "
                "élémentaire multipliée par le carré de sa distance à "
                "l'axe. Il s'exprime en kilogrammes mètre carré."
            )
        ) as tracker:
            self.play(FadeIn(def_moment))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_moment))

        # --- Définition : énergie cinétique de rotation ---------------------------
        def_ec_rot = definition_box(
            VGroup(
                Text("Énergie cinétique de rotation autour d'un axe Δ", font_size=23, weight="BOLD"),
                MathTex(r"E_c = \dfrac{1}{2} J_\Delta \, \omega^2", font_size=34),
                Text("J_Δ en kg·m², ω en rad/s, Ec en joules", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        def_ec_rot.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'énergie cinétique de rotation d'un solide tournant "
                "autour de l'axe delta à la vitesse angulaire oméga vaut "
                "alors un demi J delta oméga carré, avec J delta en "
                "kilogrammes mètre carré, oméga en radians par seconde, et "
                "l'énergie cinétique en joules."
            )
        ) as tracker:
            self.play(FadeIn(def_ec_rot))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ec_rot))

        # --- Cas d'un solide qui roule sans glisser -------------------------------
        roule = VGroup(
            Text("Solide qui roule sans glisser (v = Rω) :", font_size=23, weight="BOLD"),
            MathTex(r"E_c = \underbrace{\dfrac{1}{2} m v^2}_{\text{translation}} + \underbrace{\dfrac{1}{2} J_\Delta \, \omega^2}_{\text{rotation}}", font_size=29),
        ).arrange(DOWN, buff=0.3)
        roue_centre = RIGHT * 3.0 + DOWN * 0.5
        roue = Circle(radius=0.9, color=WHITE, stroke_width=2).move_to(roue_centre)
        roue_rayon = Line(roue_centre, roue_centre + UP * 0.9, color="#288073", stroke_width=2)
        sol_ligne = Line(roue_centre + DOWN * 0.9 + LEFT * 1.4, roue_centre + DOWN * 0.9 + RIGHT * 1.4, color=WHITE)
        v_label = MathTex("v", font_size=24, color=YELLOW).next_to(roue, UP, buff=0.55)
        omega_label2 = MathTex(r"\omega", font_size=24, color="#288073").next_to(roue_rayon.get_center(), LEFT, buff=0.1)
        roue_schema = VGroup(sol_ligne, roue, roue_rayon, v_label, omega_label2)
        roue_schema.next_to(titre, DOWN, buff=0.5).shift(RIGHT * 1.5)
        roule.next_to(titre, DOWN, buff=0.45).shift(LEFT * 2.6)

        with self.voiceover(
            text=(
                "Cas particulier très important : un solide qui roule sans "
                "glisser, comme une roue, possède à la fois un mouvement "
                "de translation de son centre et un mouvement de rotation "
                "autour de son axe, avec la relation v égale R oméga entre "
                "sa vitesse linéaire et sa vitesse angulaire, R étant le "
                "rayon. Son énergie cinétique totale est alors la somme de "
                "l'énergie cinétique de translation, un demi m v carré, et "
                "de l'énergie cinétique de rotation, un demi J delta "
                "oméga carré."
            )
        ) as tracker:
            self.play(Write(roule[0]))
            self.play(Create(roue_schema))
            self.play(Write(roule[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(roule), FadeOut(roue_schema))

        # --- Exemple résolu : tige en rotation -------------------------------------
        exemple = example_box(
            VGroup(
                Text("Tige de longueur ℓ = 2 m, masse M = 200 g, tournant à N = 3 tr/s", font_size=20),
                Text("autour de son axe central perpendiculaire (J_Δ = Mℓ²/12) :", font_size=20),
                MathTex(r"J_\Delta = \dfrac{0{,}2\times 2^2}{12} \approx 6{,}67\times 10^{-2}\ \text{kg·m}^2", font_size=23),
                MathTex(r"\omega = 2\pi N \approx 18{,}85\ \text{rad/s}", font_size=23),
                MathTex(r"E_c = \dfrac{1}{2} J_\Delta \omega^2 \approx 11{,}84\ \text{J}", font_size=25, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : une tige de longueur deux mètres et de "
                "masse deux cents grammes tourne à trois tours par seconde "
                "autour de son axe central perpendiculaire, pour lequel J "
                "delta égale M ℓ carré sur douze. On calcule d'abord J "
                "delta : environ six virgule six sept fois dix puissance "
                "moins deux kilogramme mètre carré. La vitesse angulaire "
                "oméga égale deux pi N, soit environ dix-huit virgule "
                "quatre-vingt-cinq radians par seconde. L'énergie "
                "cinétique de rotation vaut alors environ onze virgule "
                "quatre-vingt-quatre joules."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"J_\Delta = \sum_i m_i r_i^2 \qquad E_c^{rot} = \dfrac{1}{2} J_\Delta \omega^2", font_size=25),
                MathTex(r"\text{Roulement sans glissement (}v=R\omega\text{)} : \ E_c = \dfrac{1}{2}mv^2 + \dfrac{1}{2}J_\Delta\omega^2", font_size=22),
            ).arrange(DOWN, buff=0.25),
            box_width=12.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le moment d'inertie J delta somme "
                "les masses élémentaires pondérées par le carré de leur "
                "distance à l'axe, l'énergie cinétique de rotation vaut un "
                "demi J delta oméga carré, et pour un solide qui roule "
                "sans glisser, avec v égale R oméga, l'énergie cinétique "
                "totale additionne translation et rotation."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
