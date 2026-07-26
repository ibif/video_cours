"""
scenes/SVT_StructureInterneGlobe_11.py — Chapitre 7 (1ereC, SVT), scène 11.

§ IV.2-IV.4 Le manteau (Moho → 2900 km, 84 % du volume, péridotites,
preuves par xénolites) + le noyau (2900 km → centre, alliage Fe-Ni, noyau
externe liquide/effet dynamo, noyau interne/graine solide malgré 5000-6000°C
grâce à la pression) + tableau de synthèse des 5 enveloppes + coupe
schématique du globe (cercles concentriques). Source : 1ereC/SVT.pdf,
pages 75-76.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Circle, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(rows, font_size=15, header_color=YELLOW, body_color=WHITE, col_alignments=None, buff=(0.35, 0.18)):
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


class LeManteauEtLeNoyau(NotionScene):
    def construct(self):
        titre = scene_title("IV.2-IV.3 — Le manteau et le noyau")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : sous la croûte, deux enveloppes bien plus vastes -------
        intro = Text(
            _wrap(
                "Sous la croûte, qui ne fait que 1 % du volume terrestre, "
                "s'étendent deux enveloppes bien plus vastes : le manteau, "
                "puis le noyau, jusqu'au centre.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Sous la croûte, qui ne représente qu'un pour cent du "
                "volume terrestre, s'étendent deux enveloppes bien plus "
                "vastes : le manteau, puis le noyau, jusqu'au centre de la "
                "Terre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Le manteau ----------------------------------------------------------
        manteau_def = definition_box(
            Text(
                _wrap(
                    "Le manteau s'étend du Moho à 2 900 km de profondeur : "
                    "c'est l'enveloppe la plus volumineuse (~84 % du volume "
                    "de la Terre). Constitué de péridotites (olivine, "
                    "pyroxènes), plus denses (3,3 à 5,7) que les roches de "
                    "la croûte. Preuves directes : xénolites de péridotites "
                    "(kimberlites d'Afrique australe, Hoggar).",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=11.9,
        )
        manteau_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le manteau s'étend du Moho à deux mille neuf cents "
                "kilomètres de profondeur : c'est l'enveloppe la plus "
                "volumineuse de la Terre, environ quatre-vingt-quatre pour "
                "cent du volume total. Il est constitué de péridotites, des "
                "roches vertes formées d'olivine et de pyroxènes, plus "
                "denses, de trois virgule trois à cinq virgule sept, que "
                "les roches de la croûte. Les preuves directes en sont les "
                "xénolites de péridotites, remontés par les kimberlites "
                "d'Afrique australe ou les laves du Hoggar. Le manteau est "
                "globalement solide, les ondes S s'y propagent, mais il "
                "contient une zone partiellement fondue, l'asthénosphère, "
                "que nous étudierons plus loin."
            )
        ) as tracker:
            self.play(FadeIn(manteau_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(manteau_def))

        # --- Le noyau --------------------------------------------------------------
        noyau_def = definition_box(
            Text(
                _wrap(
                    "Le noyau s'étend de 2 900 km au centre (6 371 km) : "
                    "~16 % du volume mais près du tiers de la masse du "
                    "globe. Alliage de fer et de nickel (~90 % Fe, 10 % "
                    "Ni), densité 10 à 13. Noyau externe (2 900-5 150 km) : "
                    "liquide, effet dynamo. Noyau interne/graine "
                    "(5 150-6 371 km) : solide malgré 5 000-6 000°C, grâce "
                    "à la pression.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=11.9,
        )
        noyau_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le noyau s'étend de deux mille neuf cents kilomètres "
                "jusqu'au centre, à six mille trois cent soixante et onze "
                "kilomètres : environ seize pour cent du volume, mais près "
                "du tiers de la masse totale du globe, tant il est dense. "
                "Il est constitué d'un alliage de fer et de nickel, environ "
                "quatre-vingt-dix pour cent de fer, dix pour cent de "
                "nickel, de densité élevée, dix à treize. Le noyau externe, "
                "de deux mille neuf cents à cinq mille cent cinquante "
                "kilomètres, est liquide : ses mouvements engendrent le "
                "champ magnétique par effet dynamo. Le noyau interne, ou "
                "graine, de cinq mille cent cinquante kilomètres au centre, "
                "est solide, malgré une température de cinq mille à six "
                "mille degrés, car la pression colossale y élève le point "
                "de fusion du fer au-dessus de la température régnante."
            )
        ) as tracker:
            self.play(FadeIn(noyau_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(noyau_def))

        # --- Animation du raisonnement : coupe schématique du globe -----------
        centre_pt = Circle(radius=0.55, color="#F2C14E", fill_color="#F2C14E", fill_opacity=1.0)  # graine
        noyau_ext = Circle(radius=1.05, color="#E8A33D", fill_color="#E8A33D", fill_opacity=0.85)  # noyau externe
        manteau = Circle(radius=1.85, color="#B5651D", fill_color="#B5651D", fill_opacity=0.65)   # manteau
        croute = Circle(radius=2.05, color="#595959", fill_color="#8C8C8C", fill_opacity=0.9)      # croûte

        coupe = VGroup(croute, manteau, noyau_ext, centre_pt)
        coupe.move_to(LEFT * 2.6)

        label_croute = Text("Croûte", font_size=13, color=WHITE).next_to(coupe, RIGHT, buff=1.6).shift(UP * 1.6)
        label_manteau = Text("Manteau (84 % du volume)\npéridotites", font_size=13, color=WHITE).next_to(coupe, RIGHT, buff=1.6).shift(UP * 0.7)
        label_noyau_ext = Text("Noyau externe : liquide\nFe-Ni (effet dynamo)", font_size=13, color=WHITE).next_to(coupe, RIGHT, buff=1.6).shift(DOWN * 0.3)
        label_graine = Text("Graine : solide\nFe-Ni (~5000-6000°C)", font_size=13, color=WHITE).next_to(coupe, RIGHT, buff=1.6).shift(DOWN * 1.3)

        labels = VGroup(label_croute, label_manteau, label_noyau_ext, label_graine)

        with self.voiceover(
            text=(
                "Voici une coupe schématique du globe, en cercles "
                "concentriques. Tout à l'extérieur, la fine pellicule de la "
                "croûte. En dessous, le manteau, en brun, la plus "
                "volumineuse des enveloppes, fait de péridotites. Puis le "
                "noyau externe, en orange, liquide, siège de l'effet "
                "dynamo. Et enfin, tout au centre, la graine, en jaune "
                "doré, solide malgré une température comparable à celle de "
                "la surface du Soleil."
            )
        ) as tracker:
            self.play(FadeIn(croute))
            self.play(FadeIn(label_croute))
            self.play(FadeIn(manteau))
            self.play(FadeIn(label_manteau))
            self.play(FadeIn(noyau_ext))
            self.play(FadeIn(label_noyau_ext))
            self.play(FadeIn(centre_pt))
            self.play(FadeIn(label_graine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coupe), FadeOut(labels))

        # --- Exemple traité : tableau de synthèse des 5 enveloppes -----------
        entete_tab = Text("Tableau de synthèse des cinq enveloppes", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        tableau = _tableau(
            [
                ["Enveloppe", "Limites", "Matériaux", "État", "Densité"],
                ["Croûte continentale", "0-30/70 km", "Granite (SIAL)", "Solide", "2,7"],
                ["Croûte océanique", "0-5/12 km", "Basalte, gabbro (SIMA)", "Solide", "3,0-3,3"],
                ["Manteau", "Moho-2 900 km", "Péridotites", "Solide (asthéno. partiel)", "3,3-5,7"],
                ["Noyau externe", "2 900-5 150 km", "Alliage Fe-Ni", "Liquide", "10-12"],
                ["Noyau interne", "5 150-6 371 km", "Alliage Fe-Ni", "Solide", "13"],
            ],
            font_size=14,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.3)
        bloc_tab = VGroup(entete_tab, tableau)
        _garde_fou(bloc_tab)

        with self.voiceover(
            text=(
                "Voici le tableau de synthèse des cinq enveloppes du globe, "
                "de la surface au centre : croûte continentale, granitique, "
                "solide, densité deux virgule sept ; croûte océanique, "
                "basaltique, solide, densité trois à trois virgule trois ; "
                "manteau, péridotitique, globalement solide, densité "
                "croissante de trois virgule trois à cinq virgule sept ; "
                "noyau externe, alliage de fer et de nickel, liquide, "
                "densité dix à douze ; noyau interne, même alliage, solide, "
                "densité treize."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Manteau : Moho → 2 900 km, ~84 % du volume, péridotites.",
                "Noyau externe (liquide) : effet dynamo → champ magnétique.",
                "Noyau interne/graine (solide) : pression > effet de la température.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : le manteau s'étend du Moho à deux mille neuf "
                "cents kilomètres, fait de péridotites, environ "
                "quatre-vingt-quatre pour cent du volume terrestre. Le "
                "noyau externe, liquide, produit le champ magnétique par "
                "effet dynamo. Le noyau interne, la graine, reste solide "
                "car la pression y domine l'effet de la température."
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
                    "Le manteau n'est PAS liquide, malgré le magma des "
                    "volcans : il est globalement solide (les ondes S s'y "
                    "propagent). Seule une petite fraction, localement, est "
                    "partiellement fondue (asthénosphère) ou fond "
                    "ponctuellement pour alimenter un volcan.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : le manteau n'est pas liquide, "
                "malgré le magma des volcans. Il est globalement solide, "
                "les ondes S s'y propagent parfaitement. Seule une petite "
                "fraction, localement, est partiellement fondue, dans "
                "l'asthénosphère, ou fond ponctuellement pour alimenter un "
                "volcan."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
