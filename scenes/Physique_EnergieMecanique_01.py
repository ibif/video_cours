"""
scenes/Physique_EnergieMecanique_01.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 01.

Rappels essentiels des quatre chapitres précédents (travail/puissance,
énergie cinétique, énergie potentielle) avant d'aborder l'énergie
mécanique : Ec=½mv² (translation), Ec=½J_Δω² (rotation), Epp=mgz,
ΔEpp=-W(poids), Epe=½kx², théorème de l'énergie cinétique ΔEc=ΣW(F⃗ext).
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class RappelsEssentiels(NotionScene):
    def construct(self):
        titre = scene_title("Rappels essentiels")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : transition depuis les chapitres précédents ------------------
        intro = Text(
            _wrap(
                "Nous avons étudié séparément le travail, la puissance, "
                "l'énergie cinétique et l'énergie potentielle. Avant "
                "d'introduire l'énergie mécanique, faisons un bref rappel "
                "de ces notions.",
                width=54,
            ),
            font_size=24,
        )
        intro.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Au cours des quatre derniers chapitres, nous avons étudié "
                "séparément le travail et la puissance d'une force, "
                "l'énergie cinétique, puis l'énergie potentielle. Avant "
                "d'introduire la notion nouvelle de cette leçon, l'énergie "
                "mécanique, faisons un bref rappel de ces notions "
                "essentielles."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : rappel des formules, une à une -------------------------
        ec_trans = definition_box(
            VGroup(
                Text("Énergie cinétique de translation", font_size=22, weight="BOLD"),
                MathTex(r"E_c = \dfrac{1}{2} m v^2", font_size=30),
            ).arrange(DOWN, buff=0.2),
            box_width=9.0,
        )
        ec_trans.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Premier rappel : l'énergie cinétique de translation d'un "
                "solide de masse m et de vitesse v vaut E c égale un demi m "
                "v carré."
            )
        ) as tracker:
            self.play(FadeIn(ec_trans))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ec_trans))

        ec_rot = definition_box(
            VGroup(
                Text("Énergie cinétique de rotation", font_size=22, weight="BOLD"),
                MathTex(r"E_c = \dfrac{1}{2} J_{\Delta}\, \omega^2", font_size=30),
            ).arrange(DOWN, buff=0.2),
            box_width=9.0,
        )
        ec_rot.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Pour un solide en rotation autour d'un axe delta, "
                "l'énergie cinétique vaut un demi J indice delta oméga "
                "carré, où J delta est le moment d'inertie par rapport à "
                "l'axe, et oméga la vitesse angulaire."
            )
        ) as tracker:
            self.play(FadeIn(ec_rot))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ec_rot))

        epp = definition_box(
            VGroup(
                Text("Énergie potentielle de pesanteur", font_size=22, weight="BOLD"),
                MathTex(r"E_{pp} = mgz", font_size=30),
                MathTex(r"\Delta E_{pp} = -W(\vec{P})", font_size=27),
            ).arrange(DOWN, buff=0.2),
            box_width=9.6,
        )
        epp.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'énergie potentielle de pesanteur vaut E p p égale m g z, "
                "avec z l'altitude par rapport à une référence choisie. Sa "
                "variation est liée au travail du poids par la relation "
                "delta E p p égale moins le travail du poids."
            )
        ) as tracker:
            self.play(FadeIn(epp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(epp))

        epe = definition_box(
            VGroup(
                Text("Énergie potentielle élastique", font_size=22, weight="BOLD"),
                MathTex(r"E_{pe} = \dfrac{1}{2} k x^2", font_size=30),
            ).arrange(DOWN, buff=0.2),
            box_width=9.0,
        )
        epe.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'énergie potentielle élastique emmagasinée dans un "
                "ressort de raideur k, déformé de x, vaut E p e égale un "
                "demi k x carré, toujours positive ou nulle."
            )
        ) as tracker:
            self.play(FadeIn(epe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(epe))

        theoreme = theorem_box(
            VGroup(
                Text("Théorème de l'énergie cinétique", font_size=22, weight="BOLD"),
                MathTex(r"\Delta E_c = E_c(B) - E_c(A) = \sum W_{AB}(\vec{F}_{ext})", font_size=27),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Enfin, le théorème de l'énergie cinétique : la variation "
                "d'énergie cinétique d'un système entre deux instants est "
                "égale à la somme des travaux de toutes les forces "
                "extérieures qui s'exercent sur lui. C'est cet outil que "
                "nous allons mobiliser dans quelques instants pour faire "
                "émerger la notion d'énergie mécanique."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- À retenir : tableau récapitulatif --------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("Formules à connaître par cœur", font_size=23, weight="BOLD"),
                MathTex(r"E_c = \tfrac{1}{2}mv^2 \quad ; \quad E_c = \tfrac{1}{2}J_\Delta \omega^2", font_size=25),
                MathTex(r"E_{pp} = mgz \quad ; \quad E_{pe} = \tfrac{1}{2}kx^2", font_size=25),
                MathTex(r"\Delta E_c = \sum W_{ext}(\vec{F})", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons ces cinq relations : l'énergie cinétique de "
                "translation, un demi m v carré ; l'énergie cinétique de "
                "rotation, un demi J delta oméga carré ; l'énergie "
                "potentielle de pesanteur, m g z ; l'énergie potentielle "
                "élastique, un demi k x carré ; et le théorème de l'énergie "
                "cinétique. Ce sont les briques de tout ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter ---------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas ces trois énergies : Ec dépend de la "
                    "vitesse, Epp de l'altitude, Epe de la déformation d'un "
                    "ressort. N'oubliez jamais le facteur ½ dans Ec et Epe.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique à éviter dès maintenant : ne confondez pas "
                "ces trois énergies. L'énergie cinétique dépend de la "
                "vitesse, l'énergie potentielle de pesanteur de l'altitude, "
                "l'énergie potentielle élastique de la déformation d'un "
                "ressort. Et surtout, n'oubliez jamais le facteur un demi "
                "dans les expressions de Ec et de Epe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
