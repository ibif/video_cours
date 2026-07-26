"""
scenes/SVT_ReflexeInne_09.py — Chapitre 10 (1ereD, SVT), scène 09.

§ 10.4.2-10.4.3 : le réflexe de retrait en détail — trajet complet (6
étapes), réflexe polysynaptique, exemple « le pied sur une épine » (analyse
complète avec la méthode du §10.3.1), tableau de comparaison des deux
réflexes, méthode pour compter les synapses sur un schéma.
Source : 1ereD/SVT.pdf, pages 140-141.
"""

import textwrap

from manim import (
    DOWN,
    GREEN_D,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


def _numbered(items, font_size=19, color=WHITE, width=58):
    lines = VGroup(
        *[Text(f"{i+1}. {_wrap(it, width=width)}", font_size=font_size, color=color) for i, it in enumerate(items)]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.45, row_gap=0.18):
    n_rows = len(cell_matrix)
    n_cols = len(cell_matrix[0])
    col_widths = [max(cell_matrix[r][c].width for r in range(n_rows)) for c in range(n_cols)]

    col_x = []
    x = 0.0
    for c in range(n_cols):
        col_x.append(x)
        x += col_widths[c] + col_gap

    table = VGroup()
    y = 0.0
    for r in range(n_rows):
        row_height = max(cell_matrix[r][c].height for c in range(n_cols))
        for c in range(n_cols):
            cell = cell_matrix[r][c]
            cell.move_to([col_x[c] + cell.width / 2, y - row_height / 2, 0])
            table.add(cell)
        y -= row_height + row_gap
    return table


def _schema_polysynaptique():
    """Neurone sensitif → interneurone → motoneurone (2 synapses)."""
    n_sens = Line(LEFT * 3.0, LEFT * 1.0, color="#1E90FF", stroke_width=5)
    label_sens = Text("sensitif", font_size=14, color="#1E90FF").next_to(n_sens, UP, buff=0.12)

    syn1 = Dot(point=[-0.5, 0, 0], radius=0.09, color=YELLOW)

    n_inter = Line(LEFT * 0.2, RIGHT * 0.2, color=ORANGE, stroke_width=5)
    label_inter = Text("interneurone", font_size=13, color=ORANGE).next_to(n_inter, UP, buff=0.12)

    syn2 = Dot(point=[0.7, 0, 0], radius=0.09, color=YELLOW)

    n_mot = Line(RIGHT * 1.2, RIGHT * 3.2, color=GREEN_D, stroke_width=5)
    label_mot = Text("moteur", font_size=14, color=GREEN_D).next_to(n_mot, UP, buff=0.12)

    label_syn = Text("2 synapses (ou plus)", font_size=14, color=YELLOW, weight="BOLD")
    label_syn.next_to(VGroup(n_sens, n_inter, n_mot), DOWN, buff=0.3)

    return VGroup(n_sens, label_sens, syn1, n_inter, label_inter, syn2, n_mot, label_mot, label_syn)


class LeReflexeDeRetrait(NotionScene):
    def construct(self):
        titre = scene_title("10.4.2 — Le réflexe de retrait, un réflexe polysynaptique")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : les six étapes du trajet -------------------------------
        intro = Text(
            _wrap(
                "Décrivons maintenant le trajet de l'influx lors du "
                "retrait de la main.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(text="Décrivons maintenant le trajet de l'influx lors du retrait de la main.") as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : le trajet en six étapes ------------------
        trajet = _numbered(
            [
                "la stimulation douloureuse (piqûre, brûlure) excite les récepteurs cutanés de la main ;",
                "l'influx sensitif remonte par le nerf du membre et entre dans la moelle par la racine dorsale ;",
                "dans la substance grise, l'influx passe par un ou plusieurs interneurones : plusieurs synapses (réflexe polysynaptique) ;",
                "les motoneurones des fléchisseurs sont excités, ceux des extenseurs sont inhibés (inhibition réciproque) ;",
                "l'influx moteur gagne les fléchisseurs par la racine ventrale et le nerf du membre ;",
                "les fléchisseurs se contractent : le membre se replie et s'éloigne de l'agression.",
            ],
            font_size=17,
            width=62,
        )
        trajet.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un : la stimulation douloureuse, piqûre ou brûlure, excite "
                "les récepteurs cutanés de la main. Deux : l'influx "
                "sensitif remonte par la fibre sensitive du nerf du membre "
                "et entre dans la moelle par la racine dorsale. Trois : "
                "dans la substance grise, l'influx est transmis à un ou "
                "plusieurs interneurones, qui le distribuent ensuite ; il y "
                "a donc plusieurs synapses, le réflexe est dit "
                "polysynaptique. Quatre : les motoneurones des muscles "
                "fléchisseurs sont excités, tandis que ceux des muscles "
                "extenseurs sont inhibés, c'est encore l'inhibition "
                "réciproque. Cinq : l'influx moteur gagne les fléchisseurs "
                "par la racine ventrale et le nerf du membre. Six : les "
                "fléchisseurs se contractent, le membre se replie et "
                "s'éloigne de l'agression. Le temps de latence est un peu "
                "plus long que pour le réflexe rotulien : chaque synapse "
                "supplémentaire ajoute un petit retard."
            )
        ) as tracker:
            self.play(FadeIn(trajet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(trajet))

        schema = _schema_polysynaptique()
        schema.next_to(titre, DOWN, buff=0.9)

        with self.voiceover(
            text=(
                "Sur un schéma, le circuit du réflexe de retrait montre "
                "bien un neurone sensitif, un interneurone intercalé, puis "
                "un motoneurone : deux synapses au minimum, parfois plus."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : le pied sur une épine (méthode complète) -------------
        exemple = example_box(
            _bullets(
                [
                    "Yao pique la plante de son pied sur une épine ; sa jambe se replie aussitôt.",
                    "Stimulation et récepteur : la piqûre excite les récepteurs de douleur de la peau du pied.",
                    "Réponse et effecteur : la jambe fléchit ; effecteurs = muscles fléchisseurs de la jambe.",
                    "Voie sensitive : les fibres sensitives du nerf sciatique.",
                    "Centre nerveux : la moelle épinière, au niveau lombaire, avec interneurones.",
                    "Voie motrice : les fibres motrices du nerf sciatique portent l'ordre aux fléchisseurs.",
                ],
                font_size=16,
                width=62,
            ),
            box_width=12.6,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : le pied sur une épine. En marchant pieds nus "
                "dans la cour, Yao pique la plante de son pied sur une "
                "épine ; sa jambe se replie aussitôt. Analysons avec la "
                "méthode du paragraphe 10.3.1. Stimulation et récepteur : "
                "la piqûre excite les récepteurs de douleur de la peau de "
                "la plante du pied. Réponse et effecteur : la jambe "
                "fléchit ; les effecteurs sont les muscles fléchisseurs de "
                "la jambe. Voie sensitive : les fibres sensitives du nerf "
                "sciatique conduisent l'influx vers la moelle épinière. "
                "Centre nerveux : la moelle épinière, au niveau lombaire, "
                "où des interneurones relient neurones sensitifs et "
                "motoneurones. Voie motrice : les fibres motrices du nerf "
                "sciatique portent l'ordre aux fléchisseurs. La chaîne "
                "complète s'écrit : récepteurs cutanés, fibre sensitive, "
                "moelle épinière, fibre motrice, muscles fléchisseurs. "
                "C'est un réflexe de retrait, polysynaptique, inné, dont le "
                "rôle est de protéger le pied."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : tableau de comparaison des deux réflexes -----------------
        entete_tab = Text("Comparaison des deux réflexes", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        def cell(txt, size=15, color=WHITE, bold=False):
            return Text(txt, font_size=size, color=color, weight="BOLD" if bold else "NORMAL")

        headers = [cell("Critère", bold=True, color=YELLOW), cell("Rotulien", bold=True, color=YELLOW), cell("Retrait", bold=True, color=YELLOW)]
        rows = [
            ["Stimulus", "étirement du muscle", "douleur de la peau"],
            ["Récepteur", "fuseau neuromusc.", "récepteurs cutanés"],
            ["Synapses", "une seule (mono)", "plusieurs (poly)"],
            ["Effecteur", "muscle étiré", "muscles fléchisseurs"],
            ["Latence", "très courte", "un peu plus longue"],
            ["Rôle", "tonus, posture", "protection"],
        ]
        matrix = [headers] + [[cell(v) for v in row] for row in rows]
        tableau = _grid_table(matrix)
        tableau.scale(0.85)
        tableau.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Comparons les deux réflexes. Le stimulus est l'étirement "
                "du muscle pour le rotulien, une stimulation douloureuse de "
                "la peau pour le retrait. Le récepteur est le fuseau "
                "neuromusculaire, ou des récepteurs cutanés. Le nombre de "
                "synapses est d'une seule pour le rotulien, monosynaptique, "
                "contre plusieurs pour le retrait, polysynaptique. "
                "L'effecteur est le muscle étiré lui-même, ou les muscles "
                "fléchisseurs. La latence est très courte pour le rotulien, "
                "un peu plus longue pour le retrait. Et le rôle est le "
                "tonus et la posture pour l'un, la protection de "
                "l'organisme pour l'autre."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Méthode : compter les synapses sur un schéma --------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Pour déterminer si un réflexe est mono- ou "
                    "polysynaptique, repérer sur le schéma de la moelle les "
                    "zones de contact entre neurones (petits élargissements "
                    "en forme de bouton). Un seul contact direct neurone "
                    "sensitif → motoneurone : monosynaptique. Un passage "
                    "par un interneurone intermédiaire : polysynaptique.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode pour compter les synapses sur un schéma. Pour "
                "déterminer si un réflexe est mono- ou polysynaptique, "
                "repérer sur le schéma de la moelle les zones de contact "
                "entre neurones, ces petits élargissements en forme de "
                "bouton. S'il n'y a qu'un contact direct entre le neurone "
                "sensitif et le motoneurone, le réflexe est monosynaptique. "
                "Si l'influx doit passer par un interneurone intermédiaire, "
                "il est polysynaptique."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le temps de latence un peu plus long du réflexe de "
                    "retrait n'est pas dû à une plus grande distance "
                    "parcourue par l'influx, mais au nombre de synapses "
                    "traversées : chaque synapse ajoute environ 1 ms de "
                    "retard, quelle que soit la longueur des fibres.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : le temps de latence un peu plus long du "
                "réflexe de retrait n'est pas dû à une plus grande distance "
                "parcourue par l'influx, mais au nombre de synapses "
                "traversées ; chaque synapse ajoute environ une "
                "milliseconde de retard, quelle que soit la longueur des "
                "fibres."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
