"""
scenes/Chimie_DosagesOxydoreduction_09.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 09.

§ Le dosage en retour et la rigueur expérimentale. Principe du dosage en
retour en 4 étapes (excès connu de R, réaction totale avec X, dosage de
l'excès restant, calcul par différence), schéma. Tableau de rigueur
expérimentale (pipette jaugée rincée, burette rincée, erlenmeyer rincé à
l'eau distillée seulement, dilution en fiole jaugée, versement goutte à
goutte, lecture du ménisque). Piège : ajouter de l'eau distillée dans
l'erlenmeyer ne fausse pas le résultat.
Source : 1ereC/Chimie.pdf, chapitre 12, pages 121-122.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
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


def _etape(numero, texte, largeur=3.4, hauteur=1.5):
    boite = Rectangle(width=largeur, height=hauteur, color=YELLOW, stroke_width=2)
    contenu = Text(f"{numero}) {texte}", font_size=14, color=WHITE, line_spacing=0.9)
    contenu.set(width=min(contenu.width, largeur - 0.3))
    contenu.move_to(boite.get_center())
    return VGroup(boite, contenu)


def _schema_dosage_retour():
    """Diagramme de flux en 4 étapes du dosage en retour, construit avec
    des primitives Manim de base (Rectangle, Arrow, Text, VGroup) —
    aucune bibliothèque externe."""
    e1 = _etape(1, "Ajouter un excès\nCONNU de réactif R\nà la solution\ncontenant X")
    e2 = _etape(2, "Réaction totale\nR + X → produits\n(X entièrement\nconsommé)")
    e3 = _etape(3, "Doser l'excès de R\nRESTANT par un\nautre titrant")
    e4 = _etape(4, "Calculer n(X) par\nDIFFÉRENCE :\nn(R init.) − n(R restant)")

    f1 = Arrow(LEFT, RIGHT, color=WHITE, stroke_width=2, max_tip_length_to_length_ratio=0.3)
    f2 = Arrow(LEFT, RIGHT, color=WHITE, stroke_width=2, max_tip_length_to_length_ratio=0.3)
    f3 = Arrow(LEFT, RIGHT, color=WHITE, stroke_width=2, max_tip_length_to_length_ratio=0.3)

    schema = VGroup(e1, f1, e2, f2, e3, f3, e4).arrange(RIGHT, buff=0.2)
    return schema


class DosageEnRetourEtRigueurExperimentale(NotionScene):
    def construct(self):
        titre = scene_title("12.9 Le dosage en retour et la rigueur expérimentale")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------------------
        intro = Text(
            _wrap(
                "Que faire lorsque l'espèce X à doser ne réagit pas "
                "assez rapidement, ou pas de façon suffisamment nette, "
                "avec un titrant direct ? On utilise le dosage en "
                "retour.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Que faire lorsque l'espèce X que l'on souhaite doser ne "
                "réagit pas assez rapidement, ou pas de façon "
                "suffisamment nette, avec un titrant direct ? On utilise "
                "alors une méthode indirecte astucieuse : le dosage en "
                "retour."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : principe en 4 étapes + schéma -----------------------------------
        entete_principe = Text("Le principe en 4 étapes", font_size=20, color=YELLOW, weight="BOLD")
        entete_principe.next_to(titre, DOWN, buff=0.35)

        schema = _schema_dosage_retour()
        schema.scale(0.85)
        schema.next_to(entete_principe, DOWN, buff=0.35)
        groupe_principe = VGroup(entete_principe, schema)
        _fit(groupe_principe, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Le principe se déroule en quatre étapes. Un : on ajoute "
                "à la solution contenant X un excès connu d'un réactif R. "
                "Deux : une réaction totale se produit entre R et X, qui "
                "consomme entièrement X. Trois : on dose ensuite l'excès "
                "de R qui n'a pas réagi, à l'aide d'un autre titrant. "
                "Quatre : on calcule enfin la quantité de X par "
                "différence, entre la quantité de R initialement "
                "introduite et la quantité de R restante mesurée par ce "
                "second dosage."
            )
        ) as tracker:
            self.play(FadeIn(entete_principe))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_principe))

        formule = MathTex(r"n(X) = n(R)_{\text{introduit}} - n(R)_{\text{restant, dosé}}", font_size=28, color=YELLOW)
        formule.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La relation clé du dosage en retour tient en une seule "
                "ligne : la quantité de X vaut la quantité de R "
                "introduite au départ, moins la quantité de R restante, "
                "mesurée par le second dosage."
            )
        ) as tracker:
            self.play(Write(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule))

        # --- Exemple traité : tableau de rigueur expérimentale ------------------------------
        entete_rigueur = Text("Rigueur expérimentale : le tableau à respecter", font_size=19, color=YELLOW, weight="BOLD")
        entete_rigueur.next_to(titre, DOWN, buff=0.35)

        rigueur = _bullets(
            [
                "Pipette jaugée : rincée avec la solution à prélever "
                "(pas d'eau distillée résiduelle).",
                "Burette : rincée avec la solution titrante avant "
                "remplissage.",
                "Erlenmeyer : rincé à l'EAU DISTILLÉE SEULEMENT (jamais "
                "avec la solution titrée !).",
                "Dilution éventuelle : toujours réalisée en fiole "
                "jaugée, précise.",
                "Versement : goutte à goutte à l'approche de "
                "l'équivalence.",
                "Lecture : le ménisque se lit à hauteur des yeux, au "
                "bas du ménisque.",
            ],
            font_size=17,
            width=54,
        )
        rigueur.next_to(entete_rigueur, DOWN, buff=0.3)
        groupe_rigueur = VGroup(entete_rigueur, rigueur)
        _fit(groupe_rigueur, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Que le dosage soit direct ou en retour, la rigueur "
                "expérimentale reste indispensable. La pipette jaugée est "
                "rincée avec la solution à prélever, pour éviter toute "
                "eau distillée résiduelle. La burette est rincée avec la "
                "solution titrante avant remplissage. L'erlenmeyer, lui, "
                "est rincé à l'eau distillée seulement, jamais avec la "
                "solution titrée. Une dilution éventuelle se réalise "
                "toujours en fiole jaugée, précise. Le versement se fait "
                "goutte à goutte à l'approche de l'équivalence, et la "
                "lecture du volume se fait à hauteur des yeux, au bas du "
                "ménisque."
            )
        ) as tracker:
            self.play(FadeIn(entete_rigueur))
            self.play(FadeIn(rigueur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_rigueur))

        # --- À retenir ------------------------------------------------------------------------
        retenir = definition_box(
            Text(
                _wrap(
                    "Dosage en retour = 2 réactions successives : R+X "
                    "(totale, en excès), puis dosage de l'excès de R. "
                    "n(X) = n(R) introduit − n(R) restant dosé.",
                    width=48,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le dosage en retour combine deux "
                "réactions successives, d'abord R réagissant totalement "
                "et en excès avec X, puis le dosage de cet excès de R "
                "restant. La quantité de X s'obtient toujours par "
                "différence."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ---------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ajouter de l'eau distillée dans l'erlenmeyer NE "
                    "FAUSSE PAS le résultat : cela dilue le mélange (les "
                    "concentrations changent) mais ne change AUCUNE "
                    "quantité de matière n, seule grandeur utilisée dans "
                    "les calculs. C'est même recommandé pour mieux voir "
                    "le virage de couleur.",
                    width=48,
                ),
                font_size=18,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un point mérite d'être clarifié, car il inquiète "
                "souvent les élèves : ajouter de l'eau distillée dans "
                "l'erlenmeyer ne fausse absolument pas le résultat. Cela "
                "dilue certes le mélange, et les concentrations "
                "changent, mais aucune quantité de matière n n'est "
                "modifiée, or c'est justement la seule grandeur utilisée "
                "dans nos calculs. C'est même une pratique recommandée, "
                "car elle permet de mieux voir le virage de couleur à "
                "l'équivalence."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
