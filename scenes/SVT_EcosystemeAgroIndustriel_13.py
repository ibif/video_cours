"""
scenes/SVT_EcosystemeAgroIndustriel_13.py — Chapitre 11 (1ereC, SVT), scène 13.

§ 6 L'équilibre dynamique des écosystèmes : définition (fluctuations
autour de valeurs moyennes), mécanismes de régulation (proies/prédateurs,
rétroactions, compétition, facteurs climatiques, exemple du parc de la
Comoé), la succession écologique (définition, climax, exemples de la
friche de Bouaké et après feu de brousse), la résilience (définition, lien
avec la biodiversité), puis piège « l'équilibre dynamique a des
limites ». Source : 1ereC/SVT.pdf, pages 129-130.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

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


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class EquilibreDynamiqueEtSuccession(NotionScene):
    def construct(self):
        titre = scene_title("6 — L'équilibre dynamique des écosystèmes")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : définition de l'équilibre dynamique -----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un écosystème est en équilibre dynamique lorsque les "
                    "effectifs de ses populations et les flux de matière "
                    "et d'énergie restent globalement stables au cours du "
                    "temps, malgré des fluctuations permanentes, grâce à "
                    "des mécanismes de régulation internes.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Dans un écosystème naturel non perturbé, les effectifs "
                "des populations ne sont pas constants : ils fluctuent "
                "autour de valeurs moyennes. On parle d'équilibre "
                "dynamique. Un écosystème est en équilibre dynamique "
                "lorsque les effectifs de ses populations et les flux de "
                "matière et d'énergie restent globalement stables au "
                "cours du temps, malgré des fluctuations permanentes, "
                "grâce à des mécanismes de régulation internes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les mécanismes de régulation -------------------------
        regul_titre = Text("Les mécanismes de régulation", font_size=23, color=YELLOW, weight="BOLD")
        regul_titre.next_to(titre, DOWN, buff=0.4)
        regulation = _bullets(
            [
                "Régulation proies/prédateurs : trop d'herbivores → prédateurs prolifèrent → herbivores diminuent → prédateurs diminuent (rétroactions).",
                "Compétition entre espèces pour la nourriture, l'espace ou la lumière.",
                "Facteurs climatiques : sécheresses, feux de brousse, inondations.",
            ],
            font_size=19,
            width=58,
        )
        regulation.next_to(regul_titre, DOWN, buff=0.35)
        groupe_regul = VGroup(regul_titre, regulation)
        _fit(groupe_regul, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Plusieurs mécanismes assurent cette régulation. D'abord, "
                "la régulation des populations de proies par les "
                "prédateurs, et inversement : si les herbivores "
                "deviennent trop nombreux, la nourriture se raréfie et les "
                "prédateurs prolifèrent ; l'effectif des herbivores "
                "diminue, puis celui des prédateurs, et le cycle reprend. "
                "Ces rétroactions maintiennent l'équilibre. Ensuite, la "
                "compétition entre espèces pour la nourriture, l'espace ou "
                "la lumière. Enfin, les facteurs climatiques : "
                "sécheresses, feux de brousse, inondations."
            )
        ) as tracker:
            self.play(FadeIn(regul_titre))
            self.play(FadeIn(regulation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regul_titre), FadeOut(regulation))

        exemple = property_box(
            Text(
                _wrap(
                    "Exemple : dans le parc national de la Comoé, si les "
                    "herbivores se multiplient après de bonnes pluies, les "
                    "lions et les hyènes disposent de plus de proies ; "
                    "leur effectif augmente, ce qui freine ensuite la "
                    "croissance des herbivores.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un exemple concret : dans le parc national de la Comoé, "
                "si les herbivores se multiplient après de bonnes pluies, "
                "les lions et les hyènes disposent de plus de proies ; "
                "leur effectif augmente à son tour, ce qui freine ensuite "
                "la croissance des herbivores. L'équilibre se rétablit "
                "naturellement."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Exemple traité : la succession écologique ---------------------------
        succession_def = definition_box(
            Text(
                _wrap(
                    "La succession écologique est l'évolution naturelle et "
                    "orientée d'un écosystème au cours du temps, depuis un "
                    "milieu nu ou perturbé jusqu'à un état d'équilibre "
                    "relativement stable appelé climax.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        succession_def.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Autre manifestation du dynamisme des écosystèmes : la "
                "succession écologique, c'est-à-dire l'évolution naturelle "
                "et orientée d'un écosystème au cours du temps, depuis un "
                "milieu nu ou perturbé jusqu'à un état d'équilibre "
                "relativement stable, appelé climax."
            )
        ) as tracker:
            self.play(FadeIn(succession_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(succession_def))

        succession_ex = _bullets(
            [
                "Une friche abandonnée près de Bouaké : d'abord des herbes (stade pionnier), puis des arbustes, puis des arbres — savane arborée ou forêt secondaire en quelques décennies.",
                "Après un feu de brousse : la strate herbacée repousse dès les premières pluies.",
            ],
            font_size=20,
            width=58,
        )
        succession_ex.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deux exemples ivoiriens : une friche abandonnée dans la "
                "région de Bouaké est d'abord colonisée par des herbes, "
                "c'est le stade pionnier, puis par des arbustes, puis par "
                "des arbres. La savane arborée ou la forêt secondaire se "
                "reconstitue ainsi en quelques décennies. Autre exemple : "
                "après un feu de brousse, la strate herbacée repousse dès "
                "les premières pluies."
            )
        ) as tracker:
            self.play(FadeIn(succession_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(succession_ex))

        # --- À retenir : la résilience --------------------------------------------
        resilience = definition_box(
            Text(
                _wrap(
                    "La résilience d'un écosystème est sa capacité à "
                    "retrouver son équilibre après une perturbation. Un "
                    "écosystème est d'autant plus résilient que sa "
                    "biodiversité est grande (réseau trophique complexe, "
                    "redondance des rôles).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        resilience.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons enfin la notion de résilience : la résilience "
                "d'un écosystème est sa capacité à retrouver son équilibre "
                "après une perturbation. Un écosystème est d'autant plus "
                "résilient que sa biodiversité est grande, avec un réseau "
                "trophique complexe et une redondance des rôles — nous "
                "avions déjà rencontré cette idée avec les réseaux "
                "alimentaires."
            )
        ) as tracker:
            self.play(FadeIn(resilience))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resilience))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "L'équilibre dynamique a des limites : au-delà d'un "
                    "certain seuil de perturbation (déforestation massive, "
                    "pollution, surexploitation), l'écosystème ne peut "
                    "plus se régénérer et bascule vers un autre état "
                    "(désertification, eutrophisation d'un étang).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter : l'équilibre dynamique a des limites. "
                "Au-delà d'un certain seuil de perturbation, déforestation "
                "massive, pollution, surexploitation, l'écosystème ne peut "
                "plus se régénérer et bascule vers un autre état, comme la "
                "désertification ou l'eutrophisation d'un étang. La "
                "résilience n'est pas infinie."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
