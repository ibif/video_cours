"""
scenes/SVT_FecondationMammiferes_09.py — Chapitre 4 (1ereC, SVT), scène 09.

§ 7. La maîtrise de la fécondation : la contraception (tableau des
méthodes, principe scientifique de chacune) + l'IVG (définition, risques) +
la FIVETE (définition, les 5 étapes, contexte Abidjan). Traité de façon
factuelle et scientifique, fidèle au registre du PDF officiel.
Source : 1ereC/SVT.pdf, pages 42-43.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _numbered(items, font_size=21, color="#1A1A1A", width=50):
    lines = VGroup(
        *[Text(f"{i+1}. {_wrap(it, width=width)}", font_size=font_size, color=color) for i, it in enumerate(items)]
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


class MaitriseDeLaFecondation(NotionScene):
    def construct(self):
        titre = scene_title("4.7 — La maîtrise de la fécondation")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : définition de la contraception -------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La contraception est l'ensemble des méthodes "
                    "utilisées pour empêcher la fécondation ou la "
                    "nidation lors d'un rapport sexuel, afin d'éviter une "
                    "grossesse non désirée.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comprendre la fécondation, c'est aussi comprendre "
                "comment on peut la maîtriser scientifiquement. "
                "Commençons par la contraception : l'ensemble des "
                "méthodes utilisées pour empêcher la fécondation ou la "
                "nidation lors d'un rapport sexuel, afin d'éviter une "
                "grossesse non désirée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : tableau des méthodes de contraception ------------------
        entete_tab = Text("Les méthodes de contraception", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        rows = [
            ("Méthode", "Exemple", "Principe scientifique"),
            ("Mécanique", "Préservatif", "Empêche la rencontre des\ngamètes ; protège aussi des IST"),
            ("Chirurgicale", "Ligature, vasectomie", "Bloque le trajet des\ngamètes (définitive)"),
            ("Hormonale", "Pilule", "Bloque l'ovulation (inhibe\nFSH/LH) ; épaissit la glaire"),
            ("Intra-utérine", "Stérilet (DIU)", "Empêche la nidation /\nimmobilise les spermatozoïdes"),
            ("Chimique", "Spermicides", "Détruit les spermatozoïdes\ndans le vagin"),
            ("Naturelle", "Températures, abstinence", "Évite la fenêtre de\nfécondité (peu fiable)"),
            ("D'urgence", "Pilule du lendemain", "Retarde l'ovulation / empêche\nla nidation (exceptionnelle)"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=14, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.4, row_gap=0.15)
        tableau.next_to(entete_tab, DOWN, buff=0.3)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = tableau.get_top()[1] - _bas_visible
        if tableau.height > _hauteur_dispo:
            tableau.scale(_hauteur_dispo / tableau.height, about_point=tableau.get_top())

        with self.voiceover(
            text=(
                "Voici un tableau des principales méthodes. La méthode "
                "mécanique, comme le préservatif, empêche la rencontre "
                "des gamètes et protège aussi des infections sexuellement "
                "transmissibles. La méthode chirurgicale, ligature des "
                "trompes ou vasectomie, bloque le trajet des gamètes, de "
                "façon définitive. La méthode hormonale, la pilule, "
                "bloque l'ovulation en inhibant la sécrétion de FSH et de "
                "LH, et épaissit aussi la glaire cervicale. Le stérilet, "
                "méthode intra-utérine, empêche la nidation ou immobilise "
                "les spermatozoïdes. Les spermicides détruisent les "
                "spermatozoïdes dans le vagin. Les méthodes naturelles "
                "évitent les rapports pendant la fenêtre de fécondité, "
                "mais restent peu fiables. Enfin, la pilule du lendemain, "
                "méthode d'urgence exceptionnelle, retarde l'ovulation ou "
                "empêche la nidation si elle est prise très tôt."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : la FIVETE, les 5 étapes -------------------------------
        entete_fivete = Text("Exemple : la FIVETE, en 5 étapes", font_size=23, color=YELLOW, weight="BOLD")
        entete_fivete.next_to(titre, DOWN, buff=0.4)

        fivete = example_box(
            _numbered(
                [
                    "Stimulation ovarienne : hormones pour la maturation "
                    "de plusieurs follicules.",
                    "Prélèvement des ovocytes + recueil des "
                    "spermatozoïdes.",
                    "Fécondation in vitro : mise en contact des gamètes en "
                    "culture (capacitation en laboratoire).",
                    "Culture de l'embryon jusqu'à quelques cellules ou "
                    "blastocyste.",
                    "Transfert de l'embryon dans l'utérus, où il peut se "
                    "nider.",
                ],
                font_size=19,
                width=48,
            ),
            box_width=12.6,
        )
        fivete.next_to(entete_fivete, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Prenons un exemple concret de maîtrise scientifique de "
                "la fécondation : la FIVETE, fécondation in vitro et "
                "transfert d'embryon, une technique d'assistance médicale "
                "à la procréation. Elle réalise la fécondation hors du "
                "corps de la femme, en laboratoire, puis replace "
                "l'embryon dans l'utérus, en cinq grandes étapes : "
                "stimulation ovarienne, prélèvement des ovocytes et "
                "recueil des spermatozoïdes, fécondation in vitro, "
                "culture de l'embryon, puis transfert dans l'utérus de la "
                "femme."
            )
        ) as tracker:
            self.play(FadeIn(entete_fivete))
            self.play(FadeIn(fivete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_fivete), FadeOut(fivete))

        methode_fivete = method_box(
            Text(
                _wrap(
                    "La FIVETE permet à des couples stériles (trompes "
                    "bouchées, faible nombre de spermatozoïdes...) "
                    "d'avoir un enfant. Le premier « bébé-éprouvette », "
                    "Louise Brown, est né en 1978. Des centres d'AMP "
                    "existent désormais en Afrique, notamment à Abidjan.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        methode_fivete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé à retenir : la FIVETE permet à des couples "
                "stériles, par exemple à cause de trompes bouchées ou "
                "d'un faible nombre de spermatozoïdes, d'avoir un enfant. "
                "Le premier « bébé-éprouvette », Louise Brown, est né en "
                "mille neuf cent soixante-dix-huit. Des centres "
                "d'assistance médicale à la procréation existent "
                "désormais en Afrique, notamment à Abidjan."
            )
        ) as tracker:
            self.play(FadeIn(methode_fivete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_fivete))

        # --- À retenir : l'IVG, définition et réalité scientifique -----------------
        ivg = definition_box(
            Text(
                _wrap(
                    "L'IVG (interruption volontaire de grossesse) est "
                    "l'arrêt provoqué d'une grossesse avant le terme "
                    "naturel, le plus souvent par méthode médicamenteuse "
                    "ou chirurgicale, d'autant plus risquée qu'elle est "
                    "tardive ou pratiquée dans de mauvaises conditions.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        ivg.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À bien distinguer de la contraception : l'IVG, ou "
                "interruption volontaire de grossesse, est l'arrêt "
                "provoqué d'une grossesse avant le terme naturel. Sur le "
                "plan scientifique, elle met fin au développement de "
                "l'embryon ou du fœtus, le plus souvent par méthode "
                "médicamenteuse ou chirurgicale, d'autant plus risquée "
                "qu'elle est tardive ou pratiquée dans de mauvaises "
                "conditions."
            )
        ) as tracker:
            self.play(FadeIn(ivg))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ivg))

        comportement = warning_box(
            Text(
                _wrap(
                    "Les IVG clandestines, hors des structures de santé, "
                    "sont une cause importante de décès et de stérilité "
                    "chez les jeunes femmes en Afrique. Le meilleur "
                    "comportement reste la prévention : information, "
                    "éducation à la vie affective et sexuelle, et "
                    "contraception adaptée. En cas de grossesse non "
                    "désirée, se confier à un adulte de confiance et "
                    "consulter un centre de santé.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.6,
        )
        comportement.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un point de comportement responsable, essentiel : les "
                "IVG clandestines, pratiquées hors des structures de "
                "santé, sont une cause importante de décès et de "
                "stérilité chez les jeunes femmes en Afrique. Le meilleur "
                "comportement reste donc la prévention, par "
                "l'information, l'éducation à la vie affective et "
                "sexuelle, et une contraception adaptée. En cas de "
                "grossesse non désirée, il faut se confier rapidement à "
                "un adulte de confiance et consulter un centre de santé, "
                "plutôt que de recourir à des pratiques dangereuses."
            )
        ) as tracker:
            self.play(FadeIn(comportement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(comportement))

        # --- Piège à éviter : contraception ≠ IVG -----------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas contraception et IVG : la "
                    "contraception empêche la fécondation ou la nidation, "
                    "AVANT qu'une grossesse ne s'installe. L'IVG arrête "
                    "une grossesse DÉJÀ installée. Ce ne sont ni les "
                    "mêmes principes, ni les mêmes conséquences.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne jamais confondre contraception et IVG : "
                "la contraception empêche la fécondation ou la nidation, "
                "avant qu'une grossesse ne s'installe. L'IVG, elle, "
                "arrête une grossesse déjà installée. Ce ne sont ni les "
                "mêmes principes scientifiques, ni les mêmes "
                "conséquences."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
