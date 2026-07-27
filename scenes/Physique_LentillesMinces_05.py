"""
scenes/Physique_LentillesMinces_05.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 05.

§ Objet réel / virtuel, image réelle / virtuelle. Les trois rayons
particuliers permettant de construire une image (rayon // à l'axe → passe
par F' ; rayon passant par O → non dévié ; rayon passant par F → émerge //
à l'axe). Méthode : deux rayons suffisent, le troisième vérifie.
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 3).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREEN,
    RED,
    Arrow,
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
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _lens_symbol(convergente: bool = True, height: float = 2.8, color=WHITE) -> VGroup:
    half = height / 2
    if convergente:
        haut = Arrow(ORIGIN, UP * half, buff=0, stroke_width=4, color=color)
        bas = Arrow(ORIGIN, DOWN * half, buff=0, stroke_width=4, color=color)
        return VGroup(haut, bas)
    inner = half * 0.5
    axe = Line(UP * inner, DOWN * inner, color=color, stroke_width=4)
    haut = Arrow(UP * half, UP * inner, buff=0, stroke_width=4, color=color)
    bas = Arrow(DOWN * half, DOWN * inner, buff=0, stroke_width=4, color=color)
    return VGroup(axe, haut, bas)


class ObjetImageTroisRayons(NotionScene):
    def construct(self):
        titre = scene_title("Objets, images et les trois rayons particuliers")
        titre.scale(0.4)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : objet/image réels ou virtuels --------------------------------
        definitions = definition_box(
            VGroup(
                Text("Objet réel", font_size=21, weight="BOLD"),
                Text("Point d'où partent réellement des rayons lumineux", font_size=18),
                Text("(avant la lentille, dans le sens de la lumière).", font_size=18),
                Text("Objet virtuel", font_size=21, weight="BOLD"),
                Text("Point vers lequel convergeraient des rayons si la", font_size=18),
                Text("lentille ne les interceptait pas.", font_size=18),
                Text("Image réelle / virtuelle", font_size=21, weight="BOLD"),
                Text("Réelle si les rayons émergents se croisent vraiment ;", font_size=18),
                Text("virtuelle si seuls leurs prolongements se croisent.", font_size=18),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=11.6,
        )
        definitions.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un objet est dit réel lorsque des rayons lumineux "
                "partent réellement de lui, avant la lentille. Il est dit "
                "virtuel lorsque des rayons convergeraient vers lui si la "
                "lentille ne les interceptait pas d'abord. De même, une "
                "image est réelle si les rayons émergents se croisent "
                "vraiment après la lentille, et virtuelle si seuls leurs "
                "prolongements en arrière se croisent."
            )
        ) as tracker:
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Raisonnement : les trois rayons particuliers --------------------------
        # NB : F choisi relativement proche de O (par rapport à l'objet) pour que
        # le rayon (3), passant par F, entre dans la lentille à une hauteur qui
        # reste visuellement à l'intérieur du symbole dessiné.
        axe = Line(LEFT * 4.4, RIGHT * 4.4, color=WHITE, stroke_width=1.5)
        lentille = _lens_symbol(True, height=3.2)
        O = Dot(ORIGIN, color=WHITE, radius=0.05)
        label_O = MathTex("O", font_size=22).next_to(O, DOWN, buff=0.1)
        F = Dot(LEFT * 1.7, color=YELLOW, radius=0.05)
        label_F = MathTex("F", font_size=22, color=YELLOW).next_to(F, DOWN, buff=0.1)
        Fp = Dot(RIGHT * 1.7, color=YELLOW, radius=0.05)
        label_Fp = MathTex("F'", font_size=22, color=YELLOW).next_to(Fp, DOWN, buff=0.1)

        A = Dot(LEFT * 3.4, color=WHITE, radius=0.04)
        B = Dot(LEFT * 3.4 + UP * 1.3, color=WHITE, radius=0.05)
        objet = Arrow(A.get_center(), B.get_center(), buff=0, color=WHITE, stroke_width=3)
        label_AB = Text("B", font_size=20).next_to(B, UP, buff=0.08)

        # Rayon 1 : // axe → passe par F'
        r1a = Line(B.get_center(), UP * 1.3, color=BLUE, stroke_width=3)
        r1b = Line(UP * 1.3, Fp.get_center() + (Fp.get_center() - UP * 1.3) * 1.3, color=BLUE, stroke_width=3)
        label_r1 = Text("(1) // axe → passe par F'", font_size=16, color=BLUE)

        # Rayon 2 : passe par O → non dévié
        direction_o = (ORIGIN - B.get_center())
        r2 = Line(B.get_center(), B.get_center() + direction_o * 2.6, color=GREEN, stroke_width=3)
        label_r2 = Text("(2) passe par O → non dévié", font_size=16, color=GREEN)

        # Rayon 3 : passe par F → émerge // axe
        # segment objet → F, puis à la lentille (même pente), calcul du point d'entrée
        pente_r3 = (0 - B.get_center()[1]) / (F.get_center()[0] - B.get_center()[0])
        y_entree = B.get_center()[1] + pente_r3 * (0 - B.get_center()[0])
        pt_lentille_r3 = UP * y_entree
        r3a = Line(B.get_center(), pt_lentille_r3, color=RED, stroke_width=3)
        r3b = Line(pt_lentille_r3, pt_lentille_r3 + RIGHT * 4.2, color=RED, stroke_width=3)
        label_r3 = Text("(3) passe par F → émerge // axe", font_size=16, color=RED)

        legendes = VGroup(label_r1, label_r2, label_r3).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        # Tous les éléments géométriques (y compris les rayons) sont regroupés
        # AVANT le repositionnement, pour que le déplacement s'applique à
        # l'ensemble de façon cohérente (les rayons ont été calculés en
        # coordonnées absolues à partir de B/F/Fp/O).
        groupe = VGroup(
            axe, lentille, O, label_O, F, label_F, Fp, label_Fp, objet, label_AB,
            r1a, r1b, r2, r3a, r3b,
        )
        groupe.move_to(ORIGIN).next_to(titre, DOWN, buff=0.55)
        legendes.next_to(groupe, DOWN, buff=0.3).align_to(groupe, LEFT)

        with self.voiceover(
            text=(
                "Pour construire l'image d'un point objet B, on utilise "
                "trois rayons particuliers, faciles à tracer. Premier "
                "rayon : parallèle à l'axe, il émerge en passant par le "
                "foyer image F prime. Deuxième rayon : il passe par le "
                "centre optique O, il n'est pas dévié. Troisième rayon : "
                "il passe par le foyer objet F avant la lentille, et "
                "émerge parallèle à l'axe."
            )
        ) as tracker:
            self.play(Create(axe), Create(lentille))
            self.play(FadeIn(O), Write(label_O), FadeIn(F), Write(label_F), FadeIn(Fp), Write(label_Fp))
            self.play(Create(objet), Write(label_AB))
            self.play(Create(r1a), Create(r1b), Write(label_r1))
            self.play(Create(r2), Write(label_r2))
            self.play(Create(r3a), Create(r3b), Write(label_r3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(legendes))

        # --- Méthode ------------------------------------------------------------------
        methode = method_box(
            VGroup(
                Text("Construire une image", font_size=22, weight="BOLD"),
                Text("Deux des trois rayons particuliers suffisent pour", font_size=19),
                Text("localiser l'image B' (leur intersection, réelle ou", font_size=19),
                Text("prolongée).", font_size=19),
                Text("Le troisième rayon sert seulement à VÉRIFIER : il", font_size=19),
                Text("doit passer par le même point B'.", font_size=19),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=11.6,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode : deux des trois rayons particuliers suffisent "
                "pour localiser l'image B prime, à leur intersection, "
                "qu'elle soit réelle ou obtenue par prolongement en "
                "pointillés. Le troisième rayon sert uniquement à "
                "vérifier la construction : il doit lui aussi passer par "
                "ce même point B prime."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple --------------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Avec seulement les rayons (1) et (2), tracés depuis B,", font_size=19),
                Text("leur point de croisement après la lentille donne", font_size=19),
                Text("directement B'. Le rayon (3) confirme le résultat", font_size=19),
                Text("s'il passe par ce même point.", font_size=19),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Par exemple, en ne traçant que les rayons un et deux "
                "depuis le point B, leur point de croisement après la "
                "lentille donne directement l'image B prime. Le rayon "
                "trois confirme le résultat s'il passe, lui aussi, par ce "
                "même point."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                Text("(1) // axe → sort par F'.", font_size=18),
                Text("(2) passe par O → non dévié.", font_size=18),
                Text("(3) passe par F → sort // axe.", font_size=18),
                Text("Deux rayons suffisent, le 3e vérifie.", font_size=18),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=10.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le rayon parallèle à l'axe sort "
                "par F prime. Le rayon qui passe par O n'est pas dévié. "
                "Le rayon qui passe par F sort parallèle à l'axe. Deux "
                "rayons suffisent pour construire l'image, le troisième "
                "sert à vérifier."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Ne pas confondre les rôles de F et F' : le rayon", font_size=19),
                Text("   // à l'axe sort par F' (pas par F), et le rayon", font_size=19),
                Text("   qui sort // à l'axe est celui qui passait par F", font_size=19),
                Text("   (pas par F').", font_size=19),
                Text("• On construit l'image de B (hors axe), pas de A :", font_size=19),
                Text("   l'image de A reste sur l'axe, par définition.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège classique : ne pas confondre les rôles de F et F "
                "prime. Le rayon parallèle à l'axe sort par F prime, pas "
                "par F. Et le rayon qui sort parallèle à l'axe est celui "
                "qui passait par F, pas par F prime. Autre point à "
                "retenir : on construit l'image du point B, situé hors de "
                "l'axe, car l'image du point A, sur l'axe, reste toujours "
                "sur l'axe par définition."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
