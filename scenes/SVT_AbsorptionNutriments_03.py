"""
scenes/SVT_AbsorptionNutriments_03.py — Chapitre 13 (1ereD, SVT), scène 03.

§ 13.1.3 L'absorption le long du tube digestif : tableau bouche / estomac /
intestin grêle / côlon, propriété « intestin grêle organe principal », et
piège « ne pas confondre digestion et absorption ».
Source : 1ereD/SVT.pdf, page 169.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, GREEN, ORANGE, RED, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class RepartitionAbsorption(NotionScene):
    def construct(self):
        titre = scene_title("13.1.3 — Qui absorbe quoi, le long du tube digestif ?")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : l'absorption n'est pas uniforme ------------------------
        intro = Text(
            _wrap(
                "Nous savons maintenant que l'intestin grêle absorbe le "
                "glucose. Mais l'absorption a-t-elle lieu partout le long "
                "du tube digestif, ou seulement à certains endroits ?",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous savons maintenant que l'intestin grêle absorbe le "
                "glucose. Mais l'absorption a-t-elle lieu partout le long "
                "du tube digestif, ou seulement à certains endroits ? Des "
                "dosages réalisés à différents niveaux du tube digestif "
                "montrent que l'absorption ne se répartit pas "
                "uniformément."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : tableau organe par organe -----------
        tab_titre = Text("Organe, substances absorbées, importance", font_size=22, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.5)

        col_organe = VGroup(
            Text("Bouche", font_size=21, color=WHITE, weight="BOLD"),
            Text("Estomac", font_size=21, color=WHITE, weight="BOLD"),
            Text("Intestin grêle", font_size=21, color=WHITE, weight="BOLD"),
            Text("Côlon", font_size=21, color=WHITE, weight="BOLD"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42)

        col_substances = VGroup(
            Text("quasi rien", font_size=18, color=WHITE),
            Text("un peu d'eau, alcool, sels", font_size=18, color=WHITE),
            Text("quasi-totalité des nutriments, eau, sels", font_size=18, color=WHITE),
            Text("eau résiduelle, sels, vitamines", font_size=18, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42)

        col_importance = VGroup(
            Text("négligeable", font_size=19, color=RED, weight="BOLD"),
            Text("faible", font_size=19, color=ORANGE, weight="BOLD"),
            Text("très grande", font_size=19, color=GREEN, weight="BOLD"),
            Text("moyenne", font_size=19, color=YELLOW, weight="BOLD"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42)

        tableau = VGroup(col_organe, col_substances, col_importance).arrange(RIGHT, buff=0.5, aligned_edge=UP)
        tableau.scale(0.92)
        tableau.next_to(tab_titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Dans la bouche, l'absorption est quasi nulle : seuls "
                "quelques médicaments passent sous la langue. Dans "
                "l'estomac, elle reste faible : un peu d'eau, l'alcool, "
                "quelques sels. Dans l'intestin grêle, l'absorption "
                "concerne la quasi-totalité des nutriments, ainsi que "
                "l'essentiel de l'eau et des sels minéraux : son "
                "importance est très grande. Dans le côlon enfin, "
                "l'absorption est moyenne : de l'eau résiduelle, des sels "
                "minéraux, et certaines vitamines produites par la flore "
                "intestinale."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- Exemple traité : lecture du tableau -------------------------------
        lecture = Text(
            _wrap(
                "En comparant les quatre lignes du tableau, un seul organe "
                "se détache très nettement : l'intestin grêle concentre "
                "presque toute l'activité d'absorption du tube digestif.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        lecture.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "En comparant les quatre lignes du tableau, un seul organe "
                "se détache très nettement : l'intestin grêle concentre "
                "presque toute l'activité d'absorption du tube digestif."
            )
        ) as tracker:
            self.play(FadeIn(lecture))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(lecture))

        # --- À retenir : propriété ------------------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "La quasi-totalité des nutriments (glucose, acides "
                    "aminés, acides gras, glycérol, vitamines) ainsi que "
                    "l'essentiel de l'eau et des sels minéraux sont "
                    "absorbés au niveau de l'intestin grêle. L'estomac a "
                    "surtout un rôle de brassage et de digestion ; le "
                    "côlon achève l'absorption de l'eau et concentre les "
                    "résidus non digérés pour former les fèces.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons cette propriété : la quasi-totalité des "
                "nutriments — glucose, acides aminés, acides gras, "
                "glycérol, vitamines — ainsi que l'essentiel de l'eau et "
                "des sels minéraux sont absorbés au niveau de l'intestin "
                "grêle. L'estomac a surtout un rôle de brassage et de "
                "digestion ; le côlon achève l'absorption de l'eau et "
                "concentre les résidus non digérés pour former les fèces."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : digestion vs absorption --------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre digestion et absorption. La "
                    "digestion transforme les aliments en nutriments dans "
                    "la lumière du tube digestif : c'est une découpe "
                    "chimique et mécanique. L'absorption fait ensuite "
                    "passer ces nutriments à travers la paroi, vers le "
                    "sang ou la lymphe. Ce sont deux phénomènes distincts, "
                    "qui n'ont pas lieu au même niveau : la digestion "
                    "commence dès la bouche, alors que l'absorption des "
                    "nutriments est presque entièrement intestinale.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre digestion et absorption. La "
                "digestion transforme les aliments en nutriments dans la "
                "lumière du tube digestif : c'est une découpe chimique et "
                "mécanique. L'absorption fait ensuite passer ces "
                "nutriments à travers la paroi, vers le sang ou la "
                "lymphe. La digestion prépare l'absorption, mais ce sont "
                "deux phénomènes distincts, qui n'ont pas lieu au même "
                "niveau : la digestion commence dès la bouche, alors que "
                "l'absorption des nutriments est presque entièrement "
                "intestinale."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
