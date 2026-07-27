"""
scenes/Physique_TravailPuissanceTranslation_04.py — Chapitre 1 « Travail et
puissance dans le cas d'un mouvement de translation » (1ereC, Physique),
scène 04.

§ Travail d'une force de frottement sur un déplacement rectiligne
W = -f×AB (toujours résistant, α=180°), remarque : contrairement au poids,
le travail des frottements DÉPEND du chemin suivi (W = -f×ℓ, ℓ = longueur
totale du trajet). Exemple résolu 3 : dalle de 50 kg traînée sur 20 m avec
f=80 N, puis sur un trajet allongé à 30 m.
Source : 1ereC/Physique.pdf, chapitre 1, pages 4-12.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    YELLOW,
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
from shapes.boxes import (
    corrige_box,
    definition_box,
    essentiel_box,
    exercise_box,
    scene_title,
    warning_box,
)


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


FROTTEMENT_COLOR = "#B42E41"
DEPLACEMENT_COLOR = "#288073"


class TravailForceFrottement(NotionScene):
    def construct(self):
        titre = scene_title("Travail d'une force de frottement")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------------
        sol = Line(LEFT * 4, RIGHT * 4, color="#FFFFFF")
        dalle = Rectangle(width=1.2, height=0.6, color="#FFFFFF", fill_color="#7A7A7A", fill_opacity=0.9)
        dalle.next_to(sol, UP, buff=0).shift(LEFT * 1.5)
        deplacement = Vector(RIGHT * 2.2, color=DEPLACEMENT_COLOR)
        deplacement.next_to(dalle, UP, buff=0.3)
        frottement = Vector(LEFT * 1.3, color=FROTTEMENT_COLOR)
        frottement.move_to(dalle.get_center() + DOWN * 0.15)
        label_f = MathTex(r"\vec{f}", font_size=26, color=FROTTEMENT_COLOR).next_to(frottement, LEFT, buff=0.15)
        label_dep = MathTex(r"\overrightarrow{AB}", font_size=24, color=DEPLACEMENT_COLOR).next_to(
            deplacement, UP, buff=0.1
        )

        figure = VGroup(sol, dalle, deplacement, frottement, label_f, label_dep)
        figure.move_to(ORIGIN).shift(DOWN * 0.3)

        mise_en_situation = Text(
            _wrap(
                "Quand on traîne un objet sur un sol rugueux, le frottement "
                "s'oppose toujours au mouvement : c'est une force "
                "systématiquement résistante.",
                width=54,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Quand on traîne un objet sur un sol rugueux, la force de "
                "frottement s'oppose toujours au mouvement : c'est une "
                "force systématiquement résistante, dirigée en permanence à "
                "l'opposé du déplacement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(figure))

        # --- Raisonnement : expression du travail -----------------------------------
        definition = definition_box(
            VGroup(
                Text("Travail d'une force de frottement", font_size=23, weight="BOLD"),
                MathTex(r"\alpha = 180° \ \Longrightarrow\ \cos(\alpha) = -1", font_size=25),
                MathTex(r"W_{AB}(\vec{f}) = -f \times AB \ \ (\text{toujours} < 0)", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La force de frottement f vecteur est exactement opposée "
                "au déplacement, donc l'angle alpha vaut cent-quatre-vingts "
                "degrés, et son cosinus vaut moins un. Le travail des "
                "frottements sur un déplacement rectiligne vaut donc moins "
                "f fois A-B : il est toujours négatif, toujours résistant."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        remarque = warning_box(
            VGroup(
                Text(
                    "Contrairement au poids, le travail des frottements",
                    font_size=22,
                ),
                Text("DÉPEND du chemin suivi :", font_size=22),
                MathTex(
                    r"W(\vec{f}) = -f \times \ell, \quad \ell = \text{longueur totale du trajet}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.0,
        )
        remarque.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Remarque essentielle : contrairement au poids, le travail "
                "des frottements dépend du chemin suivi. Ce n'est plus la "
                "distance directe entre A et B qui compte, mais la longueur "
                "totale réellement parcourue, notée ℓ : plus le trajet est "
                "long ou détourné, plus le travail résistant des "
                "frottements est important, même si le point d'arrivée est "
                "le même."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Exemple traité 3 : dalle ---------------------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Une dalle de béton de 50 kg est traînée sur un trajet "
                    "rectiligne de 20 m, avec une force de frottement "
                    "constante f = 80 N. Calculer le travail du frottement. "
                    "Que devient-il si le trajet est allongé à 30 m ?",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. Une dalle de béton de cinquante "
                "kilogrammes est traînée sur un trajet rectiligne de vingt "
                "mètres, avec une force de frottement constante de "
                "quatre-vingts newtons. Calculons le travail du frottement, "
                "puis ce qu'il devient si le trajet est allongé à trente "
                "mètres."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc = corrige_box(
            VGroup(
                MathTex(r"\ell = 20\ m \ :\quad W(\vec{f}) = -80\times20 = -1600\ J", font_size=25),
                MathTex(r"\ell = 30\ m \ :\quad W(\vec{f}) = -80\times30 = -2400\ J", font_size=25),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )
        calc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Sur le trajet de vingt mètres, le travail du frottement "
                "vaut moins quatre-vingts fois vingt, soit moins mille six "
                "cents joules. Si le trajet est allongé à trente mètres, "
                "sans changer ni l'objet ni le sol, le travail devient moins "
                "quatre-vingts fois trente, soit moins deux mille quatre "
                "cents joules : plus le trajet est long, plus l'énergie "
                "perdue par frottement est grande."
            )
        ) as tracker:
            self.play(FadeIn(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                MathTex(r"W(\vec{f}) = -f \times \ell", font_size=28),
                Text(
                    _wrap(
                        "Toujours résistant. Dépend de la longueur totale "
                        "du trajet ℓ, pas seulement des positions A et B.",
                        width=48,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : le travail d'une force de frottement vaut "
                "toujours moins f fois ℓ. Il est systématiquement "
                "résistant, et il dépend de la longueur totale du trajet "
                "parcouru, pas seulement des positions de départ et "
                "d'arrivée."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas appliquer W=-f×AB avec AB la distance directe "
                    "sur un trajet non rectiligne : utiliser la longueur ℓ "
                    "réellement parcourue. Ne jamais confondre le "
                    "frottement f avec la réaction normale N "
                    "(perpendiculaire, travail nul).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. D'abord, sur un trajet qui n'est pas "
                "rectiligne, ne jamais utiliser la distance directe A-B : il "
                "faut la longueur ℓ réellement parcourue. Ensuite, ne "
                "jamais confondre la force de frottement f avec la "
                "réaction normale N du support, qui elle est perpendiculaire "
                "au déplacement et dont le travail est nul."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
