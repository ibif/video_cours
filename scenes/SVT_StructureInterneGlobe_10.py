"""
scenes/SVT_StructureInterneGlobe_10.py — Chapitre 7 (1ereC, SVT), scène 10.

§ IV.1 Les enveloppes du globe (découpage chimique) : la croûte
(définition, tableau comparatif croûte continentale / croûte océanique :
épaisseur, roche dominante, densité, composition SIAL/SIMA, âge, exemple
africain — socle ouest-africain). Source : 1ereC/SVT.pdf, pages 74-75.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(rows, font_size=17, header_color=YELLOW, body_color=WHITE, col_alignments=None, buff=(0.4, 0.2)):
    ncols = len(rows[0])
    cells = []
    for i, row in enumerate(rows):
        for c in row:
            cells.append(
                Text(
                    c,
                    font_size=font_size,
                    color=header_color if i == 0 else body_color,
                    weight="BOLD" if i == 0 else "NORMAL",
                )
            )
    grid = VGroup(*cells)
    align = col_alignments or ("l" * ncols)
    grid.arrange_in_grid(rows=len(rows), cols=ncols, buff=buff, col_alignments=align)
    return grid


def _garde_fou(mobject):
    bas_visible = -config.frame_height / 2 + 0.3
    hauteur_dispo = mobject.get_top()[1] - bas_visible
    if mobject.height > hauteur_dispo > 0:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())


class LaCrouteTerrestre(NotionScene):
    def construct(self):
        titre = scene_title("IV.1 — La croûte terrestre")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : les 3 discontinuités délimitent des enveloppes ---------
        intro = Text(
            _wrap(
                "Moho, Gutenberg et Lehmann délimitent, du centre vers la "
                "surface : le noyau, le manteau et la croûte. C'est un "
                "découpage fondé sur la composition chimique. Commençons "
                "par l'enveloppe la plus superficielle : la croûte.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Les trois discontinuités majeures, Moho, Gutenberg et "
                "Lehmann, délimitent, du centre vers la surface, le noyau, "
                "le manteau et la croûte. C'est un découpage fondé sur la "
                "composition chimique des matériaux. Commençons par "
                "l'enveloppe la plus superficielle : la croûte."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définition de la croûte -------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La croûte est l'enveloppe superficielle, mince et "
                    "rigide du globe, comprise entre la surface et le Moho. "
                    "Elle représente moins de 1 % du volume terrestre. Il "
                    "existe deux types de croûte : continentale et "
                    "océanique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La croûte est l'enveloppe superficielle, mince et rigide du "
                "globe, comprise entre la surface et le Moho. Elle "
                "représente moins de un pour cent du volume terrestre. Il "
                "existe deux types de croûte, aux propriétés très "
                "différentes : la croûte continentale et la croûte "
                "océanique."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : tableau comparatif -------------------
        entete_tab = Text("Croûte continentale vs croûte océanique", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        tableau = _tableau(
            [
                ["Caractère", "Continentale", "Océanique"],
                ["Épaisseur", "30-70 km (35-40 km)", "5-12 km (~7 km)"],
                ["Roche dominante", "Granite (clair)", "Basalte, gabbro (sombre)"],
                ["Densité", "~2,7", "~3,0 à 3,3"],
                ["Composition", "SIAL (Si+Al)", "SIMA (Si+Mg)"],
                ["Âge", "jusqu'à 4 Ga", "< 200 Ma, toujours jeune"],
                ["Exemple africain", "Socle ouest-africain (CI, Ghana)", "Plancher Atlantique/Indien"],
            ],
            font_size=15,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.3)
        bloc_tab = VGroup(entete_tab, tableau)
        _garde_fou(bloc_tab)

        with self.voiceover(
            text=(
                "Voici le tableau comparatif. En épaisseur, la croûte "
                "continentale mesure trente à soixante-dix kilomètres, "
                "contre seulement cinq à douze kilomètres pour l'océanique. "
                "En roche dominante, la continentale est du granite, clair "
                "; l'océanique est du basalte et du gabbro, sombres. En "
                "densité, deux virgule sept contre trois à trois virgule "
                "trois. En composition simplifiée, on parle de SIAL, riche "
                "en silice et aluminium, pour la continentale, et de SIMA, "
                "riche en silice et magnésium, pour l'océanique. En âge, la "
                "continentale peut atteindre quatre milliards d'années, "
                "alors que l'océanique reste toujours jeune, moins de deux "
                "cents millions d'années, sans cesse renouvelée. Exemple "
                "africain : le socle granitique du bouclier ouest-africain, "
                "en Côte d'Ivoire, au Ghana, au Burkina Faso, pour la "
                "continentale ; le plancher des océans Atlantique et Indien "
                "pour l'océanique."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : le socle ouest-africain --------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Le socle granitique du bouclier ouest-africain (Côte "
                    "d'Ivoire, Ghana, Burkina Faso) affleure par endroits, "
                    "sans sédiments récents dessus. Que peut-on en déduire "
                    "sur l'âge et la densité de cette croûte ?",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : le socle granitique du bouclier "
                "ouest-africain, en Côte d'Ivoire, au Ghana, au Burkina "
                "Faso, affleure par endroits, sans sédiments récents "
                "dessus. Que peut-on en déduire sur l'âge et la densité de "
                "cette croûte ?"
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        resolution = Text(
            _wrap(
                "Résolution : un socle granitique affleurant est une croûte "
                "continentale (densité ~2,7), parmi les plus anciennes du "
                "globe, formée il y a plusieurs milliards d'années puis "
                "stable depuis, sans être recouverte ni détruite.",
                width=52,
            ),
            font_size=20,
            color=YELLOW,
        )
        resolution.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résolution : un socle granitique affleurant est bien une "
                "croûte continentale, de densité environ deux virgule sept, "
                "et compte parmi les plus anciennes du globe, formée il y a "
                "plusieurs milliards d'années puis restée stable depuis, "
                "sans être recouverte ni détruite — contrairement à la "
                "croûte océanique, sans cesse recyclée."
            )
        ) as tracker:
            self.play(FadeIn(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(resolution))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Croûte = enveloppe superficielle entre surface et Moho, < 1 % du volume.",
                "Continentale : épaisse (30-70 km), granite, SIAL, ancienne.",
                "Océanique : mince (5-12 km), basalte/gabbro, SIMA, toujours jeune.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : la croûte est l'enveloppe superficielle "
                "comprise entre la surface et le Moho, moins de un pour "
                "cent du volume terrestre. La croûte continentale est "
                "épaisse, granitique, de type SIAL, et ancienne. La croûte "
                "océanique est mince, basaltique, de type SIMA, et toujours "
                "jeune."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre « épaisse » et « dense » : la croûte "
                    "continentale est plus ÉPAISSE que l'océanique, mais "
                    "MOINS DENSE (2,7 contre 3,0-3,3). C'est justement parce "
                    "qu'elle est moins dense qu'elle « flotte » plus haut, "
                    "ce qui explique en partie son épaisseur visible.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : ne confondez pas épaisse et "
                "dense. La croûte continentale est plus épaisse que "
                "l'océanique, mais elle est moins dense, deux virgule sept "
                "contre trois à trois virgule trois. C'est justement parce "
                "qu'elle est moins dense qu'elle flotte plus haut sur le "
                "manteau, comme nous le reverrons avec l'isostasie."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
