"""
scenes/Physique_EnergieMecanique_09.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 09.

Application : mouvement sur piste avec/sans frottements et transferts
d'énergie. Stratégie type (tronçon sans frottement : Em(entrée)=Em(sortie) ;
tronçon avec frottement : Em(sortie)-Em(entrée)=-fℓ). Exemple résolu 6
complet : piste avec 3 tronçons (AB sans frottement, BC rugueux, CD sans
frottement) → vB=5 m/s, vC=√17≈4,12 m/s, zD=0,85 m, vérification bilan
énergétique (2,0 J dissipés = fℓ). Transferts et chaînes énergétiques :
barrage hydroélectrique (Kossou, Buyo, Taabo), chocs et rebonds, freinage
véhicule. Rendement énergétique η=E_utile/E_fournie.
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
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
from shapes.boxes import (
    corrige_box,
    definition_box,
    essentiel_box,
    exercise_box,
    method_box,
    scene_title,
    warning_box,
)

FROTTEMENT_COLOR = "#B42E41"
LISSE_COLOR = "#288073"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _piste_trois_troncons():
    """Piste A-B (lisse, descend) - B-C (rugueux, horizontal) - C-D (lisse, remonte)."""
    a = UP * 1.4 + LEFT * 4.4
    b = DOWN * 0.6 + LEFT * 2.0
    c = DOWN * 0.6 + RIGHT * 0.6
    d = UP * 0.4 + RIGHT * 2.6
    ab = Line(a, b, color=LISSE_COLOR, stroke_width=5)
    bc = Line(b, c, color=FROTTEMENT_COLOR, stroke_width=5)
    cd = Line(c, d, color=LISSE_COLOR, stroke_width=5)
    label_a = MathTex("A", font_size=22).next_to(a, UP, buff=0.1)
    label_b = MathTex("B", font_size=22).next_to(b, DOWN, buff=0.15)
    label_c = MathTex("C", font_size=22).next_to(c, DOWN, buff=0.15)
    label_d = MathTex("D", font_size=22).next_to(d, UP, buff=0.1)
    bille = Dot(a, color=YELLOW, radius=0.12)
    return VGroup(ab, bc, cd, label_a, label_b, label_c, label_d, bille)


class ApplicationPisteTransferts(NotionScene):
    def construct(self):
        titre = scene_title("Application : piste et transferts d'énergie")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé : stratégie type sur un parcours à plusieurs tronçons ------------
        piste = _piste_trois_troncons().scale(0.85)
        piste.next_to(titre, DOWN, buff=0.55)

        legende = VGroup(
            Line(LEFT * 0.3, RIGHT * 0.3, color=LISSE_COLOR, stroke_width=5),
            Text("sans frottement", font_size=18),
        ).arrange(RIGHT, buff=0.15)
        legende2 = VGroup(
            Line(LEFT * 0.3, RIGHT * 0.3, color=FROTTEMENT_COLOR, stroke_width=5),
            Text("rugueux (frottements)", font_size=18),
        ).arrange(RIGHT, buff=0.15)
        legendes = VGroup(legende, legende2).arrange(RIGHT, buff=0.6)
        legendes.next_to(piste, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "De nombreux problèmes font intervenir une piste composée "
                "de plusieurs tronçons successifs, certains sans "
                "frottement, d'autres rugueux. Voyons la stratégie à "
                "adopter pour les traiter, tronçon par tronçon."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(piste), FadeIn(legendes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piste), FadeOut(legendes))

        # --- Raisonnement : méthode générale par tronçon ------------------------------
        methode = method_box(
            VGroup(
                Text("Stratégie tronçon par tronçon :", font_size=21, weight="BOLD"),
                MathTex(r"\text{Sans frottement : } E_m(\text{entrée}) = E_m(\text{sortie})", font_size=24),
                MathTex(r"\text{Avec frottement : } E_m(\text{sortie}) - E_m(\text{entrée}) = -f\ell", font_size=24),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sur chaque tronçon sans frottement, l'énergie mécanique à "
                "l'entrée est égale à l'énergie mécanique à la sortie. Sur "
                "chaque tronçon avec frottement, l'énergie mécanique à la "
                "sortie moins l'énergie mécanique à l'entrée vaut moins f "
                "fois ℓ, la longueur de ce tronçon uniquement. On traite "
                "ainsi le parcours morceau par morceau, en utilisant à "
                "chaque fois la vitesse de sortie d'un tronçon comme "
                "vitesse d'entrée du suivant."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple résolu 6 complet ---------------------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Une bille de masse m=500 g part de A sans vitesse "
                    "initiale, zA=1,25 m. AB (sans frottement) descend "
                    "jusqu'à zB=0. BC (rugueux, ℓ=2 m) est horizontal. CD "
                    "(sans frottement) remonte, sans vitesse finale en D. "
                    "f=1 N sur BC. Calculer vB, vC et zD (g=10 N/kg).",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=11.6,
        )
        enonce.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple résolu complet. Une bille de masse cinq cents "
                "grammes part du point A sans vitesse initiale, à une "
                "altitude de un mètre vingt-cinq. Le tronçon A-B, sans "
                "frottement, descend jusqu'à l'altitude zéro en B. Le "
                "tronçon B-C, rugueux et de longueur deux mètres, est "
                "horizontal, avec une force de frottement d'intensité un "
                "newton. Le tronçon C-D, sans frottement, remonte, et la "
                "bille s'arrête tout juste en D. Calculons la vitesse en "
                "B, la vitesse en C, et l'altitude de D."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc_ab = MathTex(
            r"AB\ (\text{sans frott.}) : \ v_B = \sqrt{2gz_A} = \sqrt{2\times10\times1{,}25} = 5\ \text{m/s}",
            font_size=23,
        )
        calc_bc = MathTex(
            r"BC\ (\text{frott.}) : \ \tfrac{1}{2}mv_C^2 - \tfrac{1}{2}mv_B^2 = -f\ell",
            font_size=23,
        )
        calc_bc2 = MathTex(
            r"v_C = \sqrt{v_B^2 - \dfrac{2f\ell}{m}} = \sqrt{25 - \dfrac{2\times1\times2}{0{,}5}} = \sqrt{17} \approx 4{,}12\ \text{m/s}",
            font_size=22,
        )
        calc_cd = MathTex(
            r"CD\ (\text{sans frott.}) : \ v_D = 0 \ \Longrightarrow\ z_D = \dfrac{v_C^2}{2g} = \dfrac{17}{20} = 0{,}85\ \text{m}",
            font_size=23,
            color=YELLOW,
        )
        calc = VGroup(calc_ab, calc_bc, calc_bc2, calc_cd).arrange(DOWN, buff=0.25)
        calc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Sur le tronçon A-B, sans frottement, la conservation de "
                "l'énergie mécanique donne v de B égale racine de deux g z "
                "de A, soit cinq mètres par seconde. Sur le tronçon B-C, "
                "rugueux et horizontal, la variation d'énergie cinétique "
                "égale moins f ℓ, ce qui donne v de C égale racine de v de "
                "B au carré moins deux f ℓ sur m, soit racine de dix-sept, "
                "environ quatre virgule douze mètres par seconde. Enfin, "
                "sur le tronçon C-D, sans frottement, la bille s'arrête "
                "tout juste en D : toute son énergie cinétique en C s'est "
                "transformée en énergie potentielle, ce qui donne z de D "
                "égale zéro virgule quatre-vingt-cinq mètre."
            )
        ) as tracker:
            self.play(Write(calc_ab))
            self.play(Write(calc_bc))
            self.play(Write(calc_bc2))
            self.play(Write(calc_cd))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        verif = corrige_box(
            VGroup(
                Text("Vérification du bilan énergétique global :", font_size=20),
                MathTex(r"E_m(A) - E_m(D) = mg(z_A - z_D) = 0{,}5\times10\times(1{,}25-0{,}85) = 2{,}0\ \text{J}", font_size=21),
                MathTex(r"f\ell = 1\times 2 = 2{,}0\ \text{J} \quad \text{(énergie dissipée sur BC)}", font_size=21),
            ).arrange(DOWN, buff=0.22),
            box_width=11.4,
        )
        verif.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Vérifions la cohérence globale du bilan énergétique : "
                "l'énergie dissipée par frottement sur le tronçon B-C, f "
                "fois ℓ, vaut deux joules — c'est exactement l'énergie "
                "mécanique perdue entre le départ et l'arrivée du "
                "parcours complet, ce qui confirme nos calculs."
            )
        ) as tracker:
            self.play(FadeIn(verif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(verif))

        # --- Transferts et chaînes énergétiques -----------------------------------------
        transferts = definition_box(
            VGroup(
                Text("Transferts et chaînes énergétiques", font_size=21, weight="BOLD"),
                Text("• Barrage hydroélectrique (Kossou, Buyo, Taabo) :", font_size=19),
                Text("   Ep de l'eau → Ec (turbine) → électricité", font_size=19),
                Text("• Choc, rebond : Em partiellement dissipée en chaleur/son", font_size=19),
                Text("• Freinage d'un véhicule : Ec → chaleur (disques de frein)", font_size=19),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.4,
        )
        transferts.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ces transformations d'énergie mécanique se retrouvent "
                "partout. Dans un barrage hydroélectrique, comme ceux de "
                "Kossou, Buyo ou Taabo, l'énergie potentielle de l'eau "
                "retenue se transforme en énergie cinétique en actionnant "
                "les turbines, puis en électricité. Lors d'un choc ou d'un "
                "rebond, une partie de l'énergie mécanique est dissipée en "
                "chaleur et en son. Lors du freinage d'un véhicule, "
                "l'énergie cinétique se transforme en chaleur au niveau "
                "des disques de frein."
            )
        ) as tracker:
            self.play(FadeIn(transferts))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(transferts))

        rendement = definition_box(
            VGroup(
                Text("Rendement énergétique", font_size=21, weight="BOLD"),
                MathTex(r"\eta = \dfrac{E_{utile}}{E_{fournie}} \quad (\eta < 1, \text{souvent en \%})", font_size=27),
            ).arrange(DOWN, buff=0.25),
            box_width=9.6,
        )
        rendement.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On caractérise l'efficacité de ces transferts par un "
                "rendement énergétique, noté êta, égal à l'énergie utile "
                "récupérée divisée par l'énergie fournie au départ. Ce "
                "rendement est toujours inférieur à un, et s'exprime "
                "souvent en pourcentage."
            )
        ) as tracker:
            self.play(FadeIn(rendement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rendement))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Sur une piste à plusieurs tronçons, traiter chaque "
                    "tronçon séparément (conservation ou perte -fℓ), puis "
                    "chaîner les vitesses. Rendement η=Eutile/Efournie<1.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : sur une piste à plusieurs "
                "tronçons, on traite chaque tronçon séparément, en "
                "appliquant la conservation ou la relation avec perte "
                "moins f ℓ, puis on chaîne les vitesses de sortie et "
                "d'entrée. Et tout transfert d'énergie réel a un rendement "
                "inférieur à un."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : ℓ dans -fℓ est la longueur du TRONÇON "
                    "concerné uniquement, pas la longueur totale du "
                    "parcours. N'appliquez le frottement que là où il "
                    "existe réellement.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent pour finir : la longueur ℓ utilisée dans "
                "moins f ℓ est la longueur du tronçon rugueux concerné "
                "uniquement, jamais la longueur totale du parcours. Il ne "
                "faut appliquer le frottement que là où il existe "
                "réellement, tronçon par tronçon."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
