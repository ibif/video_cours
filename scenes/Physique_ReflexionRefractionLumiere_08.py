"""
scenes/Physique_ReflexionRefractionLumiere_08.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 08.

§ Autres applications de la réflexion totale : principe de la fontaine
lumineuse (jet d'eau, réflexions totales aux parois eau-air, λ≈48,8°),
autres applications (prismes à réflexion totale des jumelles/appareils
photo, catadioptres, mirage sur route chaude).
Source : 1ereC/Physique.pdf, pages 117-129.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREY,
    ORANGE,
    Create,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ApplicationsFontaineLumineuseDivers(NotionScene):
    def construct(self):
        titre = scene_title("Autres applications : fontaine lumineuse et divers")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : la fontaine lumineuse ------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Dans certains parcs, un jet d'eau semble « transporter » "
                "de la lumière colorée le long de sa courbe, sans que "
                "l'eau ne s'éclaire uniformément. Comment est-ce "
                "possible ?",
                width=48,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans certains parcs, un jet d'eau semble transporter de "
                "la lumière colorée le long de sa courbe, sans que l'eau "
                "ne s'éclaire uniformément. Comment est-ce possible ? "
                "C'est encore la réflexion totale qui est à l'œuvre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : principe de la fontaine lumineuse -------------------------
        xs = np.linspace(-3.2, 3.2, 60)
        pts = [np.array([x, -0.35 * (x ** 2) + 0.9, 0]) for x in xs]
        jet = VGroup(*[Line(pts[k], pts[k + 1], color=BLUE, stroke_width=6) for k in range(len(pts) - 1)])
        jet.move_to(DOWN * 0.5)

        # rayon lumineux injecté à la base, suivant la courbure par réflexions totales
        rayon_pts = pts[::7]
        rayon = VGroup(*[Line(rayon_pts[k], rayon_pts[k + 1], color=ORANGE, stroke_width=4) for k in range(len(rayon_pts) - 1)])
        rayon.move_to(jet.get_center())

        lampe = Text("lampe", font_size=16).next_to(jet, DOWN, buff=0.5).align_to(jet, LEFT)

        with self.voiceover(
            text=(
                "Le principe est le suivant : une lampe puissante est "
                "placée à la base du jet d'eau, et injecte de la lumière "
                "à l'intérieur même du jet. Cette lumière, en frappant "
                "la paroi eau-air du jet avec un angle d'incidence "
                "supérieur à l'angle limite, environ quarante-huit "
                "virgule huit degrés pour l'eau, subit une réflexion "
                "totale : elle reste confinée à l'intérieur de l'eau, et "
                "suit ainsi toute la courbure du jet jusqu'à ce que "
                "celui-ci retombe."
            )
        ) as tracker:
            self.play(Create(jet), Write(lampe))
            self.play(Create(rayon), run_time=2.0)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(jet), FadeOut(rayon), FadeOut(lampe))

        # --- Propriété : condition (rappel angle limite eau) ---------------------------
        condition = property_box(
            VGroup(
                Text("Fontaine lumineuse", font_size=21, weight="BOLD"),
                Text("Le jet d'eau joue le rôle d'un guide de lumière, comme", font_size=19),
                Text("une fibre optique (paroi eau-air à la place cœur-gaine).", font_size=19),
                MathTex(r"\lambda_{\text{eau}\to\text{air}} \approx 48{,}8^\circ", font_size=24, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
            box_width=11.0,
        )
        condition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le jet d'eau joue donc exactement le rôle d'une fibre "
                "optique, avec l'interface eau-air remplaçant l'interface "
                "cœur-gaine. L'angle limite de l'eau vers l'air, environ "
                "quarante-huit virgule huit degrés, est la valeur clé qui "
                "permet ce guidage."
            )
        ) as tracker:
            self.play(FadeIn(condition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(condition))

        # --- Autres applications : prisme à réflexion totale --------------------------
        prisme = Polygon(
            np.array([-0.9, -0.7, 0]), np.array([0.9, -0.7, 0]), np.array([0.0, 0.9, 0]),
            color=WHITE, stroke_width=2, fill_color=BLUE, fill_opacity=0.1,
        )
        prisme.move_to(LEFT * 3.0 + DOWN * 0.3)
        # Trajet simplifié : entrée horizontale -> réflexion totale sur l'hypoténuse -> sortie verticale.
        p_entree = prisme.get_left() + RIGHT * 0.05
        chemin1 = Line(prisme.get_center() + LEFT * 1.8, p_entree, color=YELLOW, stroke_width=3)
        chemin2 = Line(p_entree, np.array([0.0, -0.7, 0]) + (LEFT * 3.0 + DOWN * 0.3), color=YELLOW, stroke_width=3)
        chemin3 = Line(np.array([0.0, -0.7, 0]) + (LEFT * 3.0 + DOWN * 0.3), np.array([0.0, -0.7, 0]) + (LEFT * 3.0 + DOWN * 0.3) + DOWN * 1.4, color=YELLOW, stroke_width=3)
        prisme_schema = VGroup(prisme, chemin1, chemin2, chemin3)
        prisme_label = Text("prisme à réflexion totale (45°-45°-90°)", font_size=14).next_to(prisme_schema, DOWN, buff=0.3)

        catadioptre_txt = Text("catadioptres (réflecteurs de vélo)", font_size=17)
        mirage_txt = Text("mirage sur route très chaude", font_size=17)
        liste_autres = VGroup(catadioptre_txt, mirage_txt).arrange(DOWN, buff=0.3)
        liste_autres.next_to(prisme_schema, RIGHT, buff=1.0)

        with self.voiceover(
            text=(
                "D'autres applications utilisent aussi la réflexion "
                "totale. Dans les jumelles et certains appareils photo, "
                "des prismes à réflexion totale, taillés avec des angles "
                "de quarante-cinq, quarante-cinq et quatre-vingt-dix "
                "degrés, replient le trajet de la lumière sans utiliser "
                "de miroir argenté, avec très peu de pertes. Les "
                "catadioptres, ces réflecteurs rouges ou blancs des "
                "vélos, utilisent le même principe pour renvoyer la "
                "lumière des phares vers leur source. Enfin, le mirage "
                "observé au-dessus d'une route très chaude s'explique "
                "par une réflexion totale progressive de la lumière dans "
                "les couches d'air chaud proches du sol, d'indice "
                "légèrement différent de l'air plus frais au-dessus."
            )
        ) as tracker:
            self.play(Create(prisme_schema), Write(prisme_label))
            self.play(Write(liste_autres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prisme_schema), FadeOut(prisme_label), FadeOut(liste_autres))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Fontaine lumineuse : le jet d'eau guide la lumière comme", font_size=20),
                Text("une fibre optique, par réflexion totale eau-air.", font_size=20),
                Text("Autres applications : prismes (jumelles), catadioptres,", font_size=20),
                Text("mirages routiers.", font_size=20),
            ).arrange(DOWN, buff=0.18),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : dans une fontaine lumineuse, le "
                "jet d'eau guide la lumière comme une fibre optique, par "
                "réflexion totale à l'interface eau-air. La réflexion "
                "totale se retrouve aussi dans les prismes des jumelles, "
                "les catadioptres, et le mirage observé sur une route "
                "très chaude."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Dans TOUTES ces applications, le milieu de propagation", font_size=20),
                Text("   de la lumière doit être PLUS réfringent que le milieu", font_size=20),
                Text("   environnant — sinon aucune réflexion totale.", font_size=20),
                Text("• Le mirage n'est pas une illusion optique due à l'œil :", font_size=20),
                Text("   c'est un phénomène physique réel de réfraction/réflexion.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Piège à éviter : dans toutes ces applications, le milieu "
                "où se propage la lumière doit être plus réfringent que "
                "le milieu environnant, sinon aucune réflexion totale ne "
                "peut se produire. Et attention, le mirage n'est pas une "
                "illusion due à l'œil : c'est un phénomène physique réel "
                "de réfraction et de réflexion dans l'air chaud."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
