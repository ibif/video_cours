"""
scenes/Physique_TravailPuissanceRotation_09.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 09 (synthèse finale du chapitre).

§ Synthèse : méthode calculer le moment d'une force en 4 étapes, méthode
appliquer le théorème des moments, méthode exploiter W = ℳΔθ et P = ℳω
(conversions radians/tr min). Pièges à éviter : bras de levier, unités,
signe des moments, couple (inutile de chercher l'axe).
Source : 1ereC/Physique.pdf, chapitre 2, pages 13-23 (synthèse).
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse : méthodes et pièges à éviter")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Récapitulons les méthodes essentielles de ce chapitre, et "
                "les erreurs les plus fréquentes à éviter.",
                width=54,
            ),
            font_size=24,
            color="#DE7C1F",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous arrivons à la fin de ce chapitre sur le travail et "
                "la puissance en rotation. Récapitulons les méthodes "
                "essentielles à maîtriser, ainsi que les pièges les plus "
                "fréquents."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : méthode 1, calculer un moment -------------------------
        methode1 = method_box(
            VGroup(
                Text("Méthode 1 — calculer le moment d'une force", font_size=21, weight="BOLD"),
                Text("1. Identifier l'axe Δ et le point d'application A.", font_size=18),
                Text("2. Tracer la droite d'action de la force.", font_size=18),
                Text("3. Calculer le bras de levier d = OA × sin(α).", font_size=18),
                Text("4. Affecter le signe selon le sens de rotation (tire-bouchon).", font_size=18),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=10.4,
        )
        methode1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Première méthode : calculer le moment d'une force, en "
                "quatre étapes. On identifie l'axe et le point "
                "d'application de la force. On trace la droite d'action de "
                "cette force. On calcule le bras de levier, d égale O A "
                "fois sinus alpha. Et enfin, on affecte le signe du "
                "moment selon le sens de rotation induit, grâce à la "
                "règle du tire-bouchon."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : théorème des moments + méthode 3 : W et P ----------------
        methode2 = method_box(
            VGroup(
                Text("Méthode 2 — appliquer le théorème des moments", font_size=20, weight="BOLD"),
                Text("Bilan des forces → sens positif → bras de levier → signes → ΣℳΔ = 0 → résoudre.", font_size=17),
                Text("Méthode 3 — exploiter W = ℳΔθ et P = ℳω", font_size=20, weight="BOLD"),
                Text("Toujours convertir : tours → radians (×2π), tr/min → rad/s (×2π/60).", font_size=17),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        methode2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deuxième méthode : pour appliquer le théorème des "
                "moments à l'équilibre, on fait le bilan des forces, on "
                "choisit un sens positif, on calcule les bras de levier, "
                "on affecte les signes, on écrit que la somme des moments "
                "est nulle, puis on résout. Troisième méthode : pour "
                "exploiter les formules W égale ℳ fois delta thêta et P "
                "égale ℳ fois oméga, il faut toujours convertir les "
                "angles — des tours vers les radians, en multipliant par "
                "deux pi — et les vitesses de rotation — des tours par "
                "minute vers les radians par seconde, en multipliant par "
                "deux pi sur soixante."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Exemple traité : synthèse rapide (mini-cas complet) -------------------
        exemple = example_box(
            VGroup(
                Text("Mini-cas de synthèse : manivelle F = 20 N, OA = 0,3 m, α = 90°, tourne à 2 tr/s :", font_size=17),
                MathTex(r"\mathcal{M}_\Delta(\vec{F}) = F\times OA = 20\times0{,}3 = 6\ \text{N}\cdot\text{m}", font_size=22),
                MathTex(r"\omega = 2\pi\times2 = 4\pi\ \text{rad/s} \ \Rightarrow\ P = \mathcal{M}_\Delta(\vec{F})\times\omega = 6\times4\pi \approx 75{,}4\ \text{W}", font_size=21),
            ).arrange(DOWN, buff=0.24),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un dernier cas de synthèse : une manivelle de trente "
                "centimètres, actionnée perpendiculairement par une force "
                "de vingt newtons, tournant à deux tours par seconde. Le "
                "moment vaut F fois O A, soit six newton-mètre. La "
                "vitesse angulaire vaut deux pi fois deux, soit quatre pi "
                "radians par seconde. La puissance développée vaut alors "
                "le moment fois oméga, soit six fois quatre pi, environ "
                "soixante-quinze virgule quatre watts."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : formules clés du chapitre ---------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("Formules clés du chapitre", font_size=22, weight="BOLD"),
                Text("ℳΔ(F⃗) = ±F×d,  d = OA×sin(α)", font_size=20),
                Text("Couple : ℳ_C = F×d (indépendant de l'axe)", font_size=20),
                Text("W = ℳΔ(F⃗)×Δθ,  P = ℳΔ(F⃗)×ω", font_size=20),
                Text("Équilibre : ΣℳΔ(F⃗ext) = 0", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=8.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir, pour tout le chapitre : le moment d'une force "
                "vaut plus ou moins F fois d, avec d égale O A fois sinus "
                "alpha. Le moment d'un couple, ℳ indice C égale F fois "
                "d, ne dépend jamais de la position de l'axe. Le travail "
                "vaut ℳ fois delta thêta, la puissance vaut ℳ fois "
                "oméga, et à l'équilibre, la somme des moments des forces "
                "extérieures est nulle."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter (récapitulatif) ----------------------------------------
        pieges = warning_box(
            VGroup(
                Text("Pièges à éviter", font_size=22, weight="BOLD"),
                Text("• Le bras de levier n'est pas OA, mais d = OA×sin(α)", font_size=18),
                Text("  (sauf si la force est perpendiculaire à OA).", font_size=18),
                Text("• Unités : moment en N·m (jamais en J), angle en", font_size=18),
                Text("  radians dans W = ℳΔθ, ω en rad/s dans P = ℳω.", font_size=18),
                Text("• Fixer le sens positif AVANT d'affecter les signes.", font_size=18),
                Text("• Pour un couple : inutile de chercher l'axe,", font_size=18),
                Text("  ℳ_C = F×d (d = distance entre les 2 droites d'action).", font_size=18),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=9.6,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour terminer, récapitulons les quatre pièges les plus "
                "fréquents de ce chapitre. Un : le bras de levier n'est "
                "pas O A, mais O A fois sinus alpha, sauf si la force est "
                "perpendiculaire à O A. Deux : attention aux unités — le "
                "moment se mesure en newton-mètre, jamais en joules, "
                "l'angle doit être en radians dans la formule du travail, "
                "et la vitesse angulaire en radians par seconde dans la "
                "formule de la puissance. Trois : toujours fixer le sens "
                "positif avant d'affecter les signes des moments. Et "
                "quatre : pour un couple de forces, inutile de chercher "
                "la position de l'axe, puisque son moment vaut simplement "
                "F fois d, où d est la distance entre les deux droites "
                "d'action."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
