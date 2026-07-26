"""
scenes/SVT_AbsorptionNutriments_05.py — Chapitre 13 (1ereD, SVT), scène 05.

§ 13.2.2-13.2.3 La villosité intestinale : structure détaillée (épithélium
à une couche d'entérocytes, microvillosités / bordure en brosse,
capillaires sanguins, vaisseau chylifère central), vocabulaire, piège
« villosités vs microvillosités » et méthode « relier structure à fonction ».
Source : 1ereD/SVT.pdf, pages 171-172.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    BLUE,
    GREEN,
    FadeIn,
    FadeOut,
    Line,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class StructureVillositeIntestinale(NotionScene):
    def construct(self):
        titre = scene_title("13.2.2 — La villosité intestinale")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : la villosité, un organe d'échange miniature -----------
        intro = Text(
            _wrap(
                "Observons de plus près une villosité intestinale : "
                "chaque villosité est une petite structure autonome, "
                "parfaitement organisée pour capter les nutriments.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Observons de plus près une villosité intestinale. Chaque "
                "villosité est une petite structure autonome, parfaitement "
                "organisée pour capter les nutriments."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : schéma légendé de la villosité ------
        contour = Polygon(
            LEFT * 1.1 + DOWN * 1.6,
            LEFT * 1.4 + UP * 1.3,
            LEFT * 0.5 + UP * 1.9,
            RIGHT * 0.5 + UP * 1.9,
            RIGHT * 1.4 + UP * 1.3,
            RIGHT * 1.1 + DOWN * 1.6,
            color=WHITE,
            stroke_width=3,
        )
        epithelium_label = Text("épithélium (1 couche d'entérocytes)", font_size=15, color=WHITE)
        epithelium_label.next_to(contour, LEFT, buff=0.3).shift(UP * 0.8)

        microv = VGroup(
            *[Line(UP * 0.02, UP * 0.14, color=RED, stroke_width=2).shift(RIGHT * 0.13 * k) for k in range(-3, 4)]
        )
        microv.move_to(contour.get_top() + UP * 0.05)
        microv_label = Text("microvillosités\n(bordure en brosse)", font_size=14, color=RED, line_spacing=0.8)
        microv_label.next_to(microv, UP, buff=0.15)

        capillaire = Line(LEFT * 0.7 + DOWN * 1.3, LEFT * 0.7 + UP * 1.0, color=RED, stroke_width=6)
        capillaire2 = Line(RIGHT * 0.7 + DOWN * 1.3, RIGHT * 0.7 + UP * 1.0, color=RED, stroke_width=6)
        capillaire_label = Text("capillaires sanguins", font_size=14, color=RED)
        capillaire_label.next_to(contour, RIGHT, buff=0.3).shift(DOWN * 0.2)

        chylifere = Line(DOWN * 1.4, UP * 1.1, color=BLUE, stroke_width=8)
        chylifere_label = Text("vaisseau chylifère\n(central)", font_size=14, color=BLUE, line_spacing=0.8)
        chylifere_label.next_to(contour, RIGHT, buff=0.3).shift(UP * 1.0)

        schema = VGroup(
            contour, epithelium_label, microv, microv_label,
            capillaire, capillaire2, capillaire_label, chylifere, chylifere_label,
        )
        schema.scale(0.95)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'épithélium qui tapisse la villosité est constitué d'une "
                "seule couche de cellules, les entérocytes, séparés du "
                "chyme par rien d'autre que leur propre membrane. Cette "
                "minceur extrême raccourcit le trajet des nutriments. Les "
                "entérocytes portent sur leur face externe les "
                "microvillosités de la bordure en brosse, véritable "
                "surface de captation. À l'intérieur de la villosité se "
                "trouve un réseau dense de capillaires sanguins, qui "
                "arrivent jusqu'au contact immédiat des entérocytes. Au "
                "centre se trouve un vaisseau chylifère, ou lactéal, un "
                "petit vaisseau lymphatique à l'extrémité fermée, dans "
                "lequel pénètrent les produits de la digestion des "
                "lipides."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Barrière mince et vascularisation intense -----------------------
        barriere = Text(
            _wrap(
                "Entre le chyme et le sang, un nutriment ne traverse que "
                "la membrane d'un entérocyte, son cytoplasme, puis la "
                "paroi d'un capillaire — quelques micromètres au total. "
                "L'intestin grêle est l'un des organes les plus "
                "vascularisés du corps : le sang emporte sans cesse les "
                "nutriments absorbés, ce qui entretient la différence de "
                "concentration favorable à l'absorption.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        barriere.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deux autres caractères rendent l'absorption très "
                "efficace. D'abord, la barrière à franchir est extrêmement "
                "mince : entre le chyme et le sang, le nutriment ne "
                "traverse que la membrane d'un entérocyte, son "
                "cytoplasme, puis la paroi d'un capillaire, soit quelques "
                "micromètres au total. Ensuite, l'intestin grêle est l'un "
                "des organes les plus vascularisés du corps : un sang "
                "abondant circule en permanence dans les villosités. Ce "
                "flux sanguin emporte sans cesse les nutriments absorbés, "
                "ce qui maintient une différence de concentration entre la "
                "lumière intestinale et le sang, différence qui favorise "
                "la poursuite de l'absorption."
            )
        ) as tracker:
            self.play(FadeIn(barriere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(barriere))

        # --- Exemple traité : méthode « relier structure à fonction » --------
        methode = method_box(
            Text(
                _wrap(
                    "1. Décrire le caractère structural (chiffre, forme, "
                    "disposition). 2. Dégager la conséquence fonctionnelle "
                    "immédiate (surface augmentée, trajet raccourci...). "
                    "3. Conclure en reliant le caractère à la fonction. "
                    "Exemple : « La paroi porte des millions de villosités "
                    "hautes d'1 mm (1). Elles multiplient par dix la "
                    "surface de contact avec le chyme (2). La quasi-"
                    "totalité des nutriments peut donc être absorbée "
                    "pendant le transit (3). »",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour expliquer l'adaptation d'un organe à sa fonction, "
                "procédons toujours en trois temps. Un : décrire le "
                "caractère structural, un chiffre, une forme, une "
                "disposition. Deux : dégager la conséquence fonctionnelle "
                "immédiate, surface augmentée, trajet raccourci, "
                "renouvellement permanent du sang. Trois : conclure en "
                "reliant explicitement ce caractère à la fonction. Par "
                "exemple : la paroi interne de l'intestin grêle porte des "
                "millions de villosités hautes d'environ un millimètre — "
                "c'est la description. Elles multiplient par dix la "
                "surface de contact avec le chyme — c'est la conséquence. "
                "La quasi-totalité des nutriments peut donc être absorbée "
                "pendant le transit intestinal — c'est la conclusion."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- À retenir : vocabulaire -------------------------------------------
        vocabulaire = _bullets(
            [
                "Chyme : contenu semi-liquide du tube digestif après digestion gastrique et intestinale.",
                "Entérocyte : cellule absorbante de l'épithélium intestinal, porteuse de microvillosités.",
                "Vaisseau chylifère : vaisseau lymphatique central de la villosité, recueille les lipides digérés.",
                "Chyle : lymphe intestinale riche en lipides après un repas, d'aspect laiteux.",
            ],
            font_size=19,
            width=56,
        )
        entete_vocab = Text("Vocabulaire à retenir", font_size=26, color=YELLOW, weight="BOLD")
        entete_vocab.next_to(titre, DOWN, buff=0.5)
        vocabulaire.next_to(entete_vocab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatre mots de vocabulaire à retenir. Le chyme est le "
                "contenu semi-liquide du tube digestif après la digestion "
                "gastrique et intestinale. L'entérocyte est la cellule "
                "absorbante de l'épithélium intestinal, porteuse de "
                "microvillosités. Le vaisseau chylifère est le vaisseau "
                "lymphatique situé au centre de chaque villosité ; il "
                "recueille les produits de la digestion des lipides. Le "
                "chyle est la lymphe intestinale riche en lipides après un "
                "repas, d'aspect laiteux."
            )
        ) as tracker:
            self.play(FadeIn(entete_vocab))
            self.play(FadeIn(vocabulaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_vocab), FadeOut(vocabulaire))

        # --- Piège à éviter : villosités vs microvillosités --------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre ces deux échelles. Les villosités "
                    "sont des replis de la paroi de l'intestin, visibles à "
                    "la loupe binoculaire ; il y en a des millions et "
                    "chacune contient des vaisseaux. Les microvillosités "
                    "sont des replis de la membrane d'une seule cellule "
                    "(l'entérocyte), invisibles au microscope optique. "
                    "Écrire « les microvillosités contiennent un vaisseau "
                    "chylifère » est une erreur grave.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention, ne pas confondre ces deux échelles. Les "
                "villosités sont des replis de la paroi de l'intestin, "
                "visibles à la loupe binoculaire ; il y en a des millions "
                "et chacune contient des vaisseaux. Les microvillosités "
                "sont des replis de la membrane d'une seule cellule, "
                "l'entérocyte, invisibles au microscope optique : on ne "
                "les observe qu'au microscope électronique. Dans une "
                "copie, écrire que les microvillosités contiennent un "
                "vaisseau chylifère est une erreur grave."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
