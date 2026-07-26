"""
scenes/SVT_EcosystemeAgroIndustriel_11.py — Chapitre 11 (1ereC, SVT), scène 11.

§ 4.5 / 5.1 Le flux de matière : recyclage en boucle (matière minérale ->
organique via producteurs -> organique via consommateurs -> minérale via
décomposeurs, minéralisation), puis le cycle du carbone (réservoir
atmosphérique CO2, 4 étapes : fixation / transfert / restitution /
stockage-combustion), avec méthode sur la combustion des combustibles
fossiles et l'effet de serre. Source : 1ereC/SVT.pdf, pages 126-128.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, DashedLine, FadeIn, FadeOut, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _case(texte, couleur, largeur=2.6, hauteur=0.9, font_size=15):
    rect = Rectangle(width=largeur, height=hauteur, fill_color=couleur, fill_opacity=0.9, stroke_color=WHITE, stroke_width=2)
    label = Text(texte, font_size=font_size, color="#1A1A1A", weight="BOLD")
    label.move_to(rect)
    label.set(width=min(label.width, largeur - 0.2))
    return VGroup(rect, label)


class RecyclageMatiereEtCycleCarbone(NotionScene):
    def construct(self):
        titre = scene_title("4.5-5.1 — Recyclage de la matière et cycle du carbone")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : contraste matière / énergie -----------------------------
        intro = Text(
            _wrap(
                "Contrairement à l'énergie, qui circule à sens unique et "
                "se perd, la matière circule en boucle dans l'écosystème : "
                "elle est recyclée.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Contrairement à l'énergie, qui circule à sens unique et "
                "se perd progressivement, la matière circule en boucle "
                "dans l'écosystème : elle est recyclée en permanence."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : la boucle de recyclage de la matière --------------
        minerale1 = _case("Matière\nminérale", "#B0BEC5")
        organique_p = _case("Matière organique\n(producteurs)", "#66BB6A")
        organique_c = _case("Matière organique\n(consommateurs)", "#FFEE58")
        minerale2 = _case("Matière\nminérale", "#B0BEC5")

        boucle = VGroup(minerale1, organique_p, organique_c, minerale2).arrange(RIGHT, buff=0.9)
        boucle.next_to(titre, DOWN, buff=0.7)

        f1 = Arrow(minerale1.get_right(), organique_p.get_left(), buff=0.08, color=YELLOW, stroke_width=3)
        f2 = Arrow(organique_p.get_right(), organique_c.get_left(), buff=0.08, color=YELLOW, stroke_width=3)
        f3 = Arrow(organique_c.get_right(), minerale2.get_left(), buff=0.08, color=YELLOW, stroke_width=3)
        l1 = Text("producteurs", font_size=13, color=WHITE).next_to(f1, UP, buff=0.08)
        l2 = Text("consommateurs", font_size=13, color=WHITE).next_to(f2, UP, buff=0.08)
        l3 = Text("décomposeurs\n(minéralisation)", font_size=13, color=WHITE).next_to(f3, UP, buff=0.08)

        schema = VGroup(boucle, f1, f2, f3, l1, l2, l3)

        with self.voiceover(
            text=(
                "La matière minérale est transformée en matière organique "
                "par les producteurs, grâce à la photosynthèse. Cette "
                "matière organique passe des producteurs aux "
                "consommateurs le long des chaînes alimentaires. Enfin, "
                "les décomposeurs transforment les substances organiques "
                "des cadavres et des déchets en sels minéraux, nitrates, "
                "phosphates, réutilisables par les plantes : c'est la "
                "minéralisation. La boucle est bouclée. Ce recyclage "
                "s'organise, à l'échelle de la planète, en grands cycles "
                "biogéochimiques."
            )
        ) as tracker:
            self.play(FadeIn(boucle))
            self.play(FadeIn(f1), FadeIn(l1))
            self.play(FadeIn(f2), FadeIn(l2))
            self.play(FadeIn(f3), FadeIn(l3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : le cycle du carbone ------------------------------
        cycle_titre = Text("Le cycle du carbone", font_size=24, color=YELLOW, weight="BOLD")
        cycle_titre.next_to(titre, DOWN, buff=0.4)

        atmo = _case("CO₂\natmosphérique", "#90A4AE", largeur=2.6, hauteur=0.9)
        producteurs = _case("Producteurs\n(plantes)", "#66BB6A")
        consommateurs = _case("Consommateurs", "#FFEE58")
        decomposeurs = _case("Décomposeurs", "#8D6E63")
        fossiles = _case("Combustibles\nfossiles", "#424242", font_size=14)

        atmo.move_to(UP * 1.5)
        producteurs.move_to(LEFT * 3.6 + DOWN * 0.4)
        consommateurs.move_to(DOWN * 0.4)
        decomposeurs.move_to(RIGHT * 3.6 + DOWN * 0.4)
        fossiles.move_to(RIGHT * 3.6 + DOWN * 1.9)

        fixation = Arrow(atmo.get_left(), producteurs.get_top(), buff=0.1, color="#66BB6A", stroke_width=3)
        transfert = Arrow(producteurs.get_right(), consommateurs.get_left(), buff=0.1, color="#FFEE58", stroke_width=3)
        vers_decomp = Arrow(consommateurs.get_right(), decomposeurs.get_left(), buff=0.1, color="#8D6E63", stroke_width=3)
        restitution1 = DashedLine(producteurs.get_top(), atmo.get_bottom() + LEFT * 0.3, color="#EF5350", stroke_width=2)
        restitution2 = DashedLine(consommateurs.get_top(), atmo.get_bottom(), color="#EF5350", stroke_width=2)
        restitution3 = DashedLine(decomposeurs.get_top(), atmo.get_bottom() + RIGHT * 0.3, color="#EF5350", stroke_width=2)
        enfouissement = Arrow(decomposeurs.get_bottom(), fossiles.get_top(), buff=0.1, color="#616161", stroke_width=3)
        combustion = DashedLine(fossiles.get_right(), atmo.get_bottom() + RIGHT * 1.0, color="#EF5350", stroke_width=2.5)

        label_fixation = Text("fixation (photosynthèse)", font_size=13, color="#66BB6A")
        label_fixation.next_to(fixation, LEFT, buff=0.1).shift(UP * 0.3)
        label_combustion = Text("combustion (l'homme)", font_size=13, color="#EF5350")
        label_combustion.next_to(fossiles, RIGHT, buff=0.15)

        cycle = VGroup(
            atmo, producteurs, consommateurs, decomposeurs, fossiles,
            fixation, transfert, vers_decomp, restitution1, restitution2, restitution3,
            enfouissement, combustion, label_fixation, label_combustion,
        )
        cycle.scale(0.8)
        cycle.next_to(cycle_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le carbone est le constituant de base de toute matière "
                "organique. Son réservoir principal est l'atmosphère, où "
                "il existe sous forme de gaz carbonique. Première étape, "
                "la fixation : les producteurs absorbent le CO2 "
                "atmosphérique par la photosynthèse et le transforment en "
                "matière organique. Deuxième étape, le transfert : le "
                "carbone organique passe des producteurs aux "
                "consommateurs par les chaînes alimentaires. Troisième "
                "étape, la restitution : tous les êtres vivants rejettent "
                "du CO2 par la respiration, et les décomposeurs en "
                "rejettent aussi en minéralisant la matière morte. "
                "Quatrième étape, le stockage et la combustion : une "
                "partie de la matière organique morte s'enfouit et se "
                "transforme, sur des millions d'années, en combustibles "
                "fossiles, charbon, pétrole ; leur combustion par l'homme "
                "rejette massivement du CO2 dans l'atmosphère."
            )
        ) as tracker:
            self.play(FadeIn(cycle_titre))
            self.play(FadeIn(atmo))
            self.play(FadeIn(producteurs), FadeIn(fixation), FadeIn(label_fixation))
            self.play(FadeIn(consommateurs), FadeIn(transfert))
            self.play(FadeIn(decomposeurs), FadeIn(vers_decomp))
            self.play(FadeIn(restitution1), FadeIn(restitution2), FadeIn(restitution3))
            self.play(FadeIn(fossiles), FadeIn(enfouissement), FadeIn(combustion), FadeIn(label_combustion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cycle_titre), FadeOut(cycle))

        # --- À retenir : point clé ------------------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "En brûlant les combustibles fossiles et en détruisant "
                    "les forêts (qui stockent le carbone), l'homme "
                    "augmente la teneur de l'atmosphère en CO₂. Or le CO₂ "
                    "est un gaz à effet de serre : son accumulation "
                    "provoque le réchauffement climatique.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé à retenir : en brûlant les combustibles "
                "fossiles et en détruisant les forêts, qui stockent le "
                "carbone, l'homme augmente la teneur de l'atmosphère en "
                "CO2. Or le CO2 est un gaz à effet de serre : son "
                "accumulation provoque le réchauffement climatique."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
