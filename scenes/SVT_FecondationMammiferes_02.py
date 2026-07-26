"""
scenes/SVT_FecondationMammiferes_02.py — Chapitre 4 (1ereC, SVT), scène 02.

§ 2. Le trajet des gamètes : montée des spermatozoïdes (col de l'utérus ->
cavité utérine -> trompe, tableau des 3 étapes, vitesse, survie 24-72h) +
trajet de l'ovule (ovulation, pavillon, fécondabilité 12-24h) + méthode
"fenêtre de fécondité". Source : 1ereC/SVT.pdf, pages 35-36.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.5, row_gap=0.26):
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


class TrajetDesGametes(NotionScene):
    def construct(self):
        titre = scene_title("4.2 — Le trajet des gamètes")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : le dépôt du sperme -----------------------------------------
        depot = Text(
            _wrap(
                "Lors du rapport sexuel, à l'éjaculation, environ 3 à 5 mL "
                "de sperme sont déposés au fond du vagin, au voisinage du "
                "col de l'utérus. Ce sperme contient 200 à 500 millions de "
                "spermatozoïdes.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        depot.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Lors du rapport sexuel, à l'éjaculation, environ trois à "
                "cinq millilitres de sperme sont déposés au fond du vagin, "
                "au voisinage du col de l'utérus. Ce sperme contient deux "
                "cents à cinq cents millions de spermatozoïdes. Suivons "
                "maintenant leur trajet, puis celui de l'ovule, jusqu'à "
                "leur rencontre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(depot))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(depot))

        # --- Raisonnement : tableau des 3 étapes de la montée --------------------
        entete_tab = Text("La montée des spermatozoïdes", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        rows = [
            ("Étape", "Milieu traversé", "Mécanisme"),
            ("1", "Col de l'utérus", "Glaire cervicale fluide (période\nd'ovulation) laisse passer"),
            ("2", "Cavité utérine", "Flagelle + contractions\nde l'utérus"),
            ("3", "Trompe de Fallope", "Vers le tiers externe, à la\nrencontre de l'ovule"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=17, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.45, row_gap=0.24)
        tableau.next_to(entete_tab, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La montée des spermatozoïdes s'effectue en trois étapes. "
                "Étape un : le col de l'utérus, où la glaire cervicale, "
                "fluide en période d'ovulation, laisse passer les "
                "spermatozoïdes. Étape deux : la cavité utérine, franchie "
                "grâce au déplacement actif du flagelle et aux "
                "contractions de l'utérus. Étape trois : la trompe de "
                "Fallope, où les spermatozoïdes progressent vers le tiers "
                "externe, à la rencontre de l'ovule."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        vitesse = _bullets(
            [
                "Vitesse propre du spermatozoïde : faible, 2 à 3 mm/min ; "
                "aidée par les contractions utérines/tubaires et les cils "
                "de la trompe.",
                "Pouvoir fécondant conservé 24 à 72 heures environ dans "
                "les voies génitales féminines.",
            ],
            font_size=22,
            width=52,
        )
        vitesse.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Quelques chiffres à retenir : la vitesse propre du "
                "spermatozoïde est faible, deux à trois millimètres par "
                "minute ; les contractions de l'utérus et des trompes, "
                "ainsi que les cils de la trompe, l'aident dans son "
                "déplacement. Les spermatozoïdes conservent leur pouvoir "
                "fécondant pendant vingt-quatre à soixante-douze heures "
                "environ dans les voies génitales féminines."
            )
        ) as tracker:
            self.play(FadeIn(vitesse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vitesse))

        # --- Trajet de l'ovule -----------------------------------------------
        ovule_txt = _bullets(
            [
                "Ovulation (~14e jour d'un cycle de 28 jours) : le "
                "follicule de Graaf éclate et libère l'ovocyte II, entouré "
                "de la zone pellucide, de la couronne radiée et du "
                "cumulus oophorus.",
                "Le pavillon de la trompe, mobile et cilié, capture "
                "l'ovule à la surface de l'ovaire et l'aspire dans la "
                "trompe.",
                "L'ovule, immobile par lui-même, progresse lentement vers "
                "l'utérus grâce aux cils et aux contractions de la "
                "trompe.",
                "Durée de fécondabilité de l'ovule : courte, 12 à 24 "
                "heures après l'ovulation.",
            ],
            font_size=21,
            width=52,
        )
        ovule_titre = Text("Le trajet de l'ovule", font_size=25, color=YELLOW, weight="BOLD")
        ovule_titre.next_to(titre, DOWN, buff=0.45)
        ovule_txt.next_to(ovule_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Du côté féminin : au moment de l'ovulation, vers le "
                "quatorzième jour d'un cycle de vingt-huit jours, le "
                "follicule de Graaf éclate et libère l'ovocyte deux, "
                "entouré de la zone pellucide, de la couronne radiée et du "
                "cumulus oophorus. Le pavillon de la trompe, doué de "
                "mouvements et tapissé de cils vibratiles, capture l'ovule "
                "à la surface de l'ovaire et l'aspire dans la trompe. "
                "L'ovule, immobile par lui-même, progresse ensuite "
                "lentement vers l'utérus grâce aux cils et aux "
                "contractions de la trompe. Sa durée de fécondabilité est "
                "courte : douze à vingt-quatre heures après l'ovulation."
            )
        ) as tracker:
            self.play(FadeIn(ovule_titre))
            self.play(FadeIn(ovule_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ovule_titre), FadeOut(ovule_txt))

        # --- Exemple traité : une sélection sévère --------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Sur les 200 à 500 millions de spermatozoïdes "
                    "éjaculés, seuls quelques centaines parviennent au "
                    "voisinage de l'ovule, et un seul le féconde. Cette "
                    "sélection sévère élimine les spermatozoïdes anormaux "
                    "ou peu mobiles au fil du trajet.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un exemple chiffré illustre la sévérité du trajet : sur "
                "les deux cents à cinq cents millions de spermatozoïdes "
                "éjaculés, seuls quelques centaines parviennent au "
                "voisinage de l'ovule, et un seul le féconde. Cette "
                "sélection sévère élimine, tout au long du trajet, les "
                "spermatozoïdes anormaux ou peu mobiles."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : la fenêtre de fécondité ---------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "La fécondation n'est possible que si le rapport "
                    "sexuel a lieu dans les 3 jours précédant l'ovulation "
                    "ou dans les 24 heures qui la suivent. C'est la base "
                    "scientifique des méthodes naturelles d'espacement des "
                    "naissances.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ce point clé, la fenêtre de fécondité : la "
                "fécondation n'est possible que si le rapport sexuel a "
                "lieu dans les trois jours précédant l'ovulation, grâce à "
                "la survie des spermatozoïdes, ou dans les vingt-quatre "
                "heures qui la suivent, pendant la fécondabilité de "
                "l'ovule. C'est la base scientifique des méthodes "
                "naturelles d'espacement des naissances."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : ne pas confondre les deux durées -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas les deux durées : la survie du "
                    "spermatozoïde dans les voies génitales (24 à 72 "
                    "heures) et la fécondabilité de l'ovule après "
                    "l'ovulation (12 à 24 heures seulement, beaucoup plus "
                    "courte).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre deux durées qui se "
                "ressemblent : la survie du spermatozoïde dans les voies "
                "génitales féminines, vingt-quatre à soixante-douze "
                "heures, et la fécondabilité de l'ovule après "
                "l'ovulation, seulement douze à vingt-quatre heures, donc "
                "beaucoup plus courte."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
