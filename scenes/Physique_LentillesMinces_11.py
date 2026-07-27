"""
scenes/Physique_LentillesMinces_11.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 11.

§ Applications : la loupe (convergente, petite distance focale, objet
entre F et O, image virtuelle droite agrandie, observation sans
accommodation si l'objet est au foyer) ; l'appareil photographique
(objectif convergent, image réelle renversée sur le capteur, mise au
point) ; l'œil réduit (cristallin = lentille convergente de vergence
variable, rétine = écran fixe à 15 mm, accommodation, punctum remotum /
punctum proximum).
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 5).
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
    Arrow,
    Create,
    DashedLine,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _lens_symbol(convergente: bool = True, height: float = 2.2, color=WHITE) -> VGroup:
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


class ApplicationsLoupeAppareilPhotoOeil(NotionScene):
    def construct(self):
        titre = scene_title("Applications : loupe, appareil photo, œil réduit")
        titre.scale(0.38)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : la loupe ---------------------------------------------------------
        loupe_def = definition_box(
            VGroup(
                Text("La loupe", font_size=22, weight="BOLD"),
                Text("Lentille convergente de petite distance focale.", font_size=19),
                Text("L'objet est placé entre F et O : l'image virtuelle,", font_size=19),
                Text("droite et agrandie, est observée à travers la loupe.", font_size=19),
                Text("Si l'objet est exactement en F, l'image est à l'infini :", font_size=19),
                Text("observation SANS ACCOMMODATION (œil au repos).", font_size=19, color=YELLOW),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=11.6,
        )
        loupe_def.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La loupe est une lentille convergente de petite distance "
                "focale. On place l'objet entre F et O : on a vu que "
                "l'image obtenue est alors virtuelle, droite et agrandie, "
                "et c'est cette image que l'œil observe à travers la "
                "loupe. Si l'objet est placé exactement au foyer F, "
                "l'image se forme à l'infini, ce qui permet une "
                "observation sans accommodation, l'œil restant au repos."
            )
        ) as tracker:
            self.play(FadeIn(loupe_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loupe_def))

        # --- Raisonnement : schéma de la loupe ------------------------------------------
        f = 1.3
        axe = Line(LEFT * 4.0, RIGHT * 4.0, color=WHITE, stroke_width=1.5)
        lentille = _lens_symbol(True, height=2.4)
        O = Dot(ORIGIN, color=WHITE, radius=0.05)
        F = Dot(LEFT * f, color=YELLOW, radius=0.05)
        label_F = MathTex("F", font_size=20, color=YELLOW).next_to(F, DOWN, buff=0.08)

        A = LEFT * 0.8
        B = LEFT * 0.8 + UP * 0.4
        objet = Arrow(A, B, buff=0, color=WHITE, stroke_width=2.5)
        label_objet = Text("objet (entre F et O)", font_size=15).next_to(objet, DOWN, buff=0.6)

        # rayon par O, non dévié, prolongé
        r2 = Line(B, B + (ORIGIN - B) * 3.2, color=GREEN, stroke_width=2.2)
        # rayon // axe -> J -> vers F' virtuel via prolongement arrière
        J = UP * 0.4
        Fp = RIGHT * f
        dir_JFp = Fp - J
        r1b = Line(J, Fp + dir_JFp * 1.8, color=BLUE, stroke_width=2.2)
        r1a = Line(B, J, color=BLUE, stroke_width=2.2)
        prol1 = DashedLine(J, J + dir_JFp * (-1.6), color=BLUE, stroke_width=1.4)

        pente_r1 = dir_JFp[1] / dir_JFp[0]
        pente_r2 = (0 - B[1]) / (0 - B[0])
        x_bp = 0.4 / (pente_r2 - pente_r1)
        y_bp = pente_r2 * x_bp
        Bp = RIGHT * x_bp + UP * y_bp
        prol2 = DashedLine(ORIGIN, Bp, color=GREEN, stroke_width=1.4)
        image = Arrow(RIGHT * x_bp, Bp, buff=0, color=YELLOW, stroke_width=2.5)
        label_image = Text("image virtuelle, droite, agrandie", font_size=15, color=YELLOW)

        groupe = VGroup(axe, lentille, O, F, label_F, objet, r2, r1a, r1b, prol1, prol2, image)
        groupe.move_to(ORIGIN).next_to(titre, DOWN, buff=0.55)
        label_objet.next_to(groupe, DOWN, buff=0.25).shift(LEFT * 1.5)
        label_image.next_to(label_objet, RIGHT, buff=1.0)

        with self.voiceover(
            text=(
                "Traçons le schéma : l'objet est placé entre F et le "
                "centre optique O. Le rayon issu du sommet de l'objet et "
                "passant par O n'est pas dévié. Le rayon parallèle à "
                "l'axe émerge en direction de F prime. Les deux rayons "
                "émergents divergent : ce sont leurs prolongements en "
                "pointillés qui se croisent, donnant l'image virtuelle, "
                "droite et agrandie, observée par l'œil placé derrière la "
                "loupe."
            )
        ) as tracker:
            self.play(Create(axe), Create(lentille))
            self.play(FadeIn(O), FadeIn(F), Write(label_F))
            self.play(Create(objet), Write(label_objet))
            self.play(Create(r2))
            self.play(Create(r1a), Create(r1b))
            self.play(Create(prol1), Create(prol2))
            self.play(Create(image), Write(label_image))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(label_objet), FadeOut(label_image))

        # --- Raisonnement : appareil photographique -------------------------------------
        appareil_def = definition_box(
            VGroup(
                Text("L'appareil photographique", font_size=21, weight="BOLD"),
                Text("Objectif = lentille convergente. Le capteur (écran)", font_size=18),
                Text("reçoit l'image RÉELLE et RENVERSÉE de la scène.", font_size=18),
                Text("Pour un objet à l'infini, l'image se forme dans le", font_size=18),
                Text("plan focal image : on règle la distance objectif-", font_size=18),
                Text("capteur pour d'autres distances (mise au point).", font_size=18),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=11.6,
        )
        appareil_def.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'appareil photographique utilise un objectif, qui est "
                "une lentille convergente. Le capteur, qui joue le rôle "
                "d'écran, reçoit l'image réelle et renversée de la scène "
                "photographiée. Pour un objet à l'infini, cette image se "
                "forme exactement dans le plan focal image. Pour "
                "photographier des objets plus proches, on doit régler la "
                "distance entre l'objectif et le capteur : c'est la mise "
                "au point."
            )
        ) as tracker:
            self.play(FadeIn(appareil_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(appareil_def))

        # --- Raisonnement : œil réduit --------------------------------------------------
        oeil_def = definition_box(
            VGroup(
                Text("L'œil réduit (modèle simplifié)", font_size=21, weight="BOLD"),
                Text("Cristallin = lentille convergente de vergence", font_size=18),
                Text("VARIABLE. Rétine = écran fixe, à 15 mm du cristallin.", font_size=18),
                Text("Accommodation : le cristallin ajuste sa vergence", font_size=18),
                Text("pour toujours former l'image nette sur la rétine.", font_size=18),
                Text("Punctum remotum (PR) : point le plus éloigné vu net.", font_size=18),
                Text("Punctum proximum (PP) : point le plus proche vu net.", font_size=18),
            ).arrange(DOWN, buff=0.13, aligned_edge=LEFT),
            box_width=11.6,
        )
        oeil_def.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le modèle de l'œil réduit assimile le cristallin à une "
                "lentille convergente dont la vergence est variable, et "
                "la rétine à un écran fixe, situé à environ 15 millimètres "
                "du cristallin. L'accommodation est le mécanisme par "
                "lequel le cristallin ajuste sa vergence pour que l'image "
                "reste toujours nette sur la rétine, quelle que soit la "
                "distance de l'objet observé. Le punctum remotum est le "
                "point le plus éloigné vu net sans accommodation ; le "
                "punctum proximum est le point le plus proche vu net, "
                "avec une accommodation maximale."
            )
        ) as tracker:
            self.play(FadeIn(oeil_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(oeil_def))

        # --- Exemple ---------------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un œil regarde un objet au punctum proximum, à 25 cm.", font_size=19),
                Text("La rétine étant à 15 mm du cristallin (OA' = +15 mm),", font_size=19),
                MathTex(
                    r"C = \dfrac{1}{\overline{OA'}} - \dfrac{1}{\overline{OA}} = \dfrac{1}{0{,}015} - \dfrac{1}{-0{,}25} \approx 70\ \delta",
                    font_size=20,
                    color=YELLOW,
                ),
                Text("(le cristallin doit fortement accommoder)", font_size=17),
            ).arrange(DOWN, buff=0.16),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : un œil regarde un objet situé à son punctum "
                "proximum, à 25 centimètres. La rétine étant à 15 "
                "millimètres du cristallin, la formule de Descartes donne "
                "une vergence nécessaire d'environ 70 dioptries : le "
                "cristallin doit alors fortement accommoder pour former "
                "une image nette."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                Text("Loupe : objet entre F et O → image virtuelle agrandie.", font_size=18),
                Text("Appareil photo : image réelle renversée sur le capteur.", font_size=18),
                Text("Œil réduit : vergence variable, rétine fixe, on", font_size=18),
                Text("accommode entre PP et PR.", font_size=18),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : pour la loupe, un objet entre F "
                "et O donne une image virtuelle agrandie. Pour l'appareil "
                "photo, l'image réelle et renversée se forme sur le "
                "capteur. Pour l'œil réduit, c'est la vergence du "
                "cristallin qui varie, la rétine restant fixe : on "
                "accommode entre le punctum proximum et le punctum "
                "remotum."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Dans l'œil réel, c'est le cristallin qui change de", font_size=18),
                Text("   vergence (la rétine ne bouge pas) — à l'inverse de", font_size=18),
                Text("   l'appareil photo, où c'est la distance capteur-", font_size=18),
                Text("   objectif qui varie (la vergence de l'objectif est", font_size=18),
                Text("   fixe).", font_size=18),
                Text("• « Sans accommodation » = objet au PR (souvent", font_size=18),
                Text("   assimilé à l'infini pour un œil normal), pas au PP.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.11),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à ne pas commettre : dans l'œil réel, c'est le "
                "cristallin qui change de vergence, la rétine ne bouge "
                "pas — c'est l'inverse de l'appareil photo, où c'est la "
                "distance entre le capteur et l'objectif qui varie, la "
                "vergence de l'objectif restant fixe. Et l'observation "
                "sans accommodation correspond à un objet placé au "
                "punctum remotum, souvent assimilé à l'infini pour un œil "
                "normal, et non au punctum proximum."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
