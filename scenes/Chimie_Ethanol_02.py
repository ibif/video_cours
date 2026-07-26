"""
scenes/Chimie_Ethanol_02.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 02.

§ 2.1 Obtention de l'éthanol — la fermentation alcoolique. Définition
(glucose → éthanol + CO₂ sous l'action des levures/enzymes, en l'absence
de dioxygène), équation C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂, rôle des levures
(Saccharomyces cerevisiae, zymase catalyseur biologique), conditions
(25-35°C, anaérobie, effervescence de CO₂), limite ≈16° (destruction des
levures). Exemples contextualisés (vin de palme/bangui, tchapalo).
Distillation pour concentrer (koutoukou) : schéma du montage (différence
Téb éthanol 78,5°C / eau 100°C), construit avec primitives Manim de base.
Source : 1ereC/Chimie.pdf, chapitre 7, pages 68-69.
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
    RED,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Line,
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


def _bullets(items, font_size=22, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_distillation():
    """Schéma simplifié d'un montage de distillation, construit uniquement
    avec des primitives Manim de base (Circle, Line, Rectangle, Arrow,
    MathTex/Text, VGroup) — aucune bibliothèque externe."""

    # Ballon de chauffage (vin) : cercle + petit col
    ballon = Circle(radius=0.55, color=WHITE, stroke_width=3)
    ballon.move_to([-4.2, -1.0, 0])
    col_ballon = Rectangle(width=0.28, height=0.5, color=WHITE, stroke_width=3)
    col_ballon.next_to(ballon, UP, buff=0)
    label_vin = Text("vin (éthanol + eau)", font_size=15, color=WHITE)
    label_vin.move_to(ballon.get_center())

    # Chauffe-ballon (source de chaleur)
    chauffage = Rectangle(width=1.3, height=0.25, color=ORANGE, fill_color=ORANGE, fill_opacity=1, stroke_width=0)
    chauffage.next_to(ballon, DOWN, buff=0.05)
    label_chauffage = Text("chauffage doux", font_size=14, color=ORANGE)
    label_chauffage.next_to(chauffage, DOWN, buff=0.1)

    # Thermomètre sur le col (petit segment collé au col, étiquette à gauche
    # pour ne pas empiéter sur le tube horizontal ni sur son étiquette)
    thermo = Line(col_ballon.get_top(), col_ballon.get_top() + UP * 0.35, color=RED, stroke_width=3)
    label_thermo = MathTex(r"78{,}5°C", font_size=18, color=RED)
    label_thermo.next_to(thermo, LEFT, buff=0.12)

    # Tube coudé vers le réfrigérant (part du sommet du col, au-dessus du
    # thermomètre, pour éviter tout croisement de traits)
    tube_horizontal = Line(col_ballon.get_top() + UP * 0.55, col_ballon.get_top() + UP * 0.55 + RIGHT * 1.6, color=WHITE, stroke_width=3)

    # Réfrigérant (double tube incliné avec circulation d'eau)
    refrig_ext = Rectangle(width=2.0, height=0.55, color=BLUE, stroke_width=3)
    refrig_ext.move_to(tube_horizontal.get_end() + RIGHT * 1.0)
    tube_interne = Line(refrig_ext.get_left(), refrig_ext.get_right(), color=WHITE, stroke_width=2)
    label_refrig = Text("réfrigérant", font_size=14, color=BLUE)
    label_refrig.next_to(refrig_ext, UP, buff=0.12)

    fleche_eau_entree = Arrow(
        refrig_ext.get_corner([1, -1, 0]) + [0.3, -0.5, 0],
        refrig_ext.get_corner([1, -1, 0]),
        color=BLUE, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.35,
    )
    label_eau_entree = Text("entrée d'eau froide", font_size=12, color=BLUE)
    label_eau_entree.next_to(fleche_eau_entree, DOWN, buff=0.05)

    fleche_eau_sortie = Arrow(
        refrig_ext.get_corner([-1, 1, 0]),
        refrig_ext.get_corner([-1, 1, 0]) + [-0.3, 0.5, 0],
        color=BLUE, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.35,
    )
    label_eau_sortie = Text("sortie d'eau tiède", font_size=12, color=BLUE)
    label_eau_sortie.next_to(fleche_eau_sortie, UP, buff=0.05)

    fleche_vapeur = Arrow(
        col_ballon.get_top() + UP * 0.55 + RIGHT * 0.1,
        refrig_ext.get_left(),
        color=YELLOW, stroke_width=2, buff=0.05, max_tip_length_to_length_ratio=0.25,
    )
    label_vapeur = Text("vapeurs d'éthanol", font_size=12, color=YELLOW)
    label_vapeur.next_to(fleche_vapeur, UP, buff=0.05)

    # Ballon de collecte (distillat)
    tube_sortie = Line(refrig_ext.get_right(), refrig_ext.get_right() + [0.5, -0.6, 0], color=WHITE, stroke_width=3)
    collecteur = Circle(radius=0.42, color=YELLOW, stroke_width=3)
    collecteur.move_to(tube_sortie.get_end() + DOWN * 0.4)
    label_distillat = Text("distillat riche\nen éthanol", font_size=13, color=YELLOW, line_spacing=0.8)
    label_distillat.move_to(collecteur.get_center() + DOWN * 0.95)

    schema = VGroup(
        chauffage, label_chauffage,
        ballon, col_ballon, label_vin,
        thermo, label_thermo,
        tube_horizontal,
        refrig_ext, tube_interne, label_refrig,
        fleche_eau_entree, label_eau_entree,
        fleche_eau_sortie, label_eau_sortie,
        fleche_vapeur, label_vapeur,
        tube_sortie, collecteur, label_distillat,
    )
    return schema


class FermentationAlcoolique(NotionScene):
    def construct(self):
        titre = scene_title("7.2 Obtention de l'éthanol — la fermentation alcoolique")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : deux voies d'obtention, focus sur la fermentation --------
        intro = Text(
            _wrap(
                "L'éthanol peut être obtenu de deux façons : une voie "
                "biologique, ancienne et renouvelable — la fermentation "
                "des sucres — et une voie industrielle, issue de la "
                "pétrochimie. Étudions d'abord la fermentation.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'éthanol peut être obtenu de deux façons : une voie "
                "biologique, ancienne et renouvelable, la fermentation des "
                "sucres, et une voie industrielle, issue de la "
                "pétrochimie, que nous verrons dans la scène suivante. "
                "Étudions d'abord la fermentation alcoolique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition + équation + rôle des levures -----------
        def_ferm = definition_box(
            Text(
                _wrap(
                    "La fermentation alcoolique est la transformation du "
                    "glucose (un sucre) en éthanol, avec dégagement de "
                    "dioxyde de carbone, sous l'action d'enzymes sécrétées "
                    "par des levures, en l'absence de dioxygène.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        def_ferm.next_to(titre, DOWN, buff=0.4)

        equation = MathTex(r"C_6H_{12}O_6 \longrightarrow 2\,C_2H_5OH + 2\,CO_2", font_size=30, color=WHITE)
        equation.next_to(def_ferm, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La fermentation alcoolique est la transformation du "
                "glucose, un sucre, en éthanol, avec dégagement de dioxyde "
                "de carbone, sous l'action d'enzymes sécrétées par des "
                "levures, des micro-organismes vivants, en l'absence "
                "totale de dioxygène. L'équation-bilan s'écrit : C-6, "
                "H-12, O-6 donne deux C-2, H-5, O-H, plus deux C-O-2."
            )
        ) as tracker:
            self.play(FadeIn(def_ferm))
            self.play(Write(equation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ferm), FadeOut(equation))

        entete_conditions = Text("Rôle des levures et conditions de la fermentation", font_size=22, color=YELLOW, weight="BOLD")
        entete_conditions.next_to(titre, DOWN, buff=0.35)

        conditions = _bullets(
            [
                "Les levures (par exemple Saccharomyces cerevisiae) "
                "produisent des enzymes, dont la zymase, qui jouent le "
                "rôle de catalyseurs biologiques : elles accélèrent la "
                "réaction sans être consommées.",
                "La fermentation se déroule en milieu anaérobie (sans "
                "air) et à température modérée, environ 25 à 35°C.",
                "Le dégagement de CO₂ produit une effervescence (des "
                "bulles) visible dans le jus.",
                "La fermentation s'arrête d'elle-même vers 16° d'alcool : "
                "au-delà, l'alcool formé détruit les levures.",
            ],
            font_size=20,
            width=54,
        )
        conditions.next_to(entete_conditions, DOWN, buff=0.35)
        _fit(VGroup(entete_conditions, conditions), entete_conditions.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Les levures, par exemple l'espèce Saccharomyces "
                "cerevisiae, produisent des enzymes, dont la zymase, qui "
                "jouent le rôle de catalyseurs biologiques : elles "
                "accélèrent la réaction sans être consommées. La "
                "fermentation se déroule en milieu anaérobie, c'est-à-dire "
                "sans air, et à température modérée, environ vingt-cinq à "
                "trente-cinq degrés. Le dégagement de dioxyde de carbone "
                "produit une effervescence visible, des bulles, dans le "
                "jus. Enfin, la fermentation s'arrête d'elle-même lorsque "
                "le degré en alcool atteint environ seize degrés : "
                "au-delà, l'alcool formé détruit les levures elles-mêmes."
            )
        ) as tracker:
            self.play(FadeIn(entete_conditions))
            self.play(FadeIn(conditions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_conditions), FadeOut(conditions))

        # --- Exemple traité : exemples contextualisés ivoiriens -----------------
        entete_exemples = Text("Exemples contextualisés", font_size=22, color=YELLOW, weight="BOLD")
        entete_exemples.next_to(titre, DOWN, buff=0.35)

        exemples = _bullets(
            [
                "Le vin de palme, ou bangui, obtenu par fermentation de "
                "la sève sucrée du palmier.",
                "Le tchapalo, bière traditionnelle de sorgho ou de maïs "
                "fermentés.",
                "Les vins de raisin et les bières industrielles, obtenus "
                "par le même principe biologique.",
            ],
            font_size=21,
            width=54,
        )
        exemples.next_to(entete_exemples, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Ce mécanisme se retrouve dans plusieurs boissons "
                "traditionnelles ivoiriennes. Le vin de palme, ou bangui, "
                "est obtenu par fermentation de la sève sucrée du "
                "palmier. Le tchapalo est une bière traditionnelle de "
                "sorgho ou de maïs fermentés. Le même principe biologique "
                "est à l'œuvre dans les vins de raisin et les bières "
                "industrielles."
            )
        ) as tracker:
            self.play(FadeIn(entete_exemples))
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_exemples), FadeOut(exemples))

        # --- À retenir : la distillation pour concentrer -------------------------
        entete_dist = Text("Concentrer l'alcool : la distillation", font_size=22, color=YELLOW, weight="BOLD")
        entete_dist.next_to(titre, DOWN, buff=0.35)

        texte_dist = Text(
            _wrap(
                "Pour dépasser 16°, il faut distiller le produit fermenté : "
                "l'éthanol bout à 78,5°C, l'eau à 100°C. C'est ainsi que "
                "l'on obtient les eaux-de-vie, comme le koutoukou.",
                width=54,
            ),
            font_size=19,
            color=WHITE,
        )
        texte_dist.next_to(entete_dist, DOWN, buff=0.25)

        schema = _schema_distillation()
        schema.scale(0.95)
        schema.next_to(texte_dist, DOWN, buff=0.35)
        groupe_dist = VGroup(entete_dist, texte_dist, schema)
        _fit(groupe_dist, entete_dist.get_top()[1] + 0.1)
        groupe_dist.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Pour obtenir des boissons plus concentrées en alcool, au "
                "delà de seize degrés, il faut distiller le produit "
                "fermenté. La distillation repose sur la différence des "
                "températures d'ébullition : l'éthanol bout à soixante-dix "
                "huit virgule cinq degrés, l'eau à cent degrés. En "
                "chauffant doucement le vin, les vapeurs, plus riches en "
                "éthanol, s'échappent en premier, remontent dans le tube, "
                "puis sont refroidies et condensées dans le réfrigérant, "
                "où circule de l'eau froide en sens inverse de la vapeur. "
                "Le distillat recueilli est beaucoup plus riche en alcool. "
                "C'est ainsi que l'on obtient les eaux-de-vie, par exemple "
                "le koutoukou, obtenu par distillation du vin de palme."
            )
        ) as tracker:
            self.play(FadeIn(entete_dist))
            self.play(FadeIn(texte_dist))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_dist))

        # --- Piège à éviter : fermentation ≠ réaction en présence d'air --------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre la fermentation alcoolique avec une "
                    "combustion ou une simple dissolution de sucre : c'est "
                    "une transformation chimique précise, catalysée par "
                    "des enzymes, qui n'a lieu qu'en l'absence de "
                    "dioxygène (milieu anaérobie).",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre la fermentation alcoolique "
                "avec une combustion, ou avec une simple dissolution de "
                "sucre dans l'eau : c'est une transformation chimique "
                "précise, catalysée par des enzymes, qui ne se produit "
                "qu'en l'absence de dioxygène, en milieu anaérobie."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
