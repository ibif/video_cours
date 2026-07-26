"""
scenes/SVT_FecondationMammiferes_08.py — Chapitre 4 (1ereC, SVT), scène 08.

§ 5.2 La nidation (définition, fixation dans l'endomètre J6-7, rôle du
trophoblaste/placenta, HCG et tests de grossesse) + § 6. Les jumeaux (vrais
jumeaux monozygotes vs faux jumeaux dizygotes, tableau comparatif).
Source : 1ereC/SVT.pdf, pages 41-42.
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
    Circle,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
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


class NidationEtJumeaux(NotionScene):
    def construct(self):
        titre = scene_title("4.5.2 — Nidation et jumeaux")
        titre.scale(0.65)
        titre.to_edge(UP)

        # === PARTIE 1 : LA NIDATION ================================================

        # --- Énoncé : définition de la nidation ------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La nidation (ou implantation) est la fixation du "
                    "blastocyste dans la muqueuse utérine (l'endomètre), "
                    "environ 6 à 7 jours après la fécondation.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Arrivé dans l'utérus au stade blastocyste, l'œuf va "
                "maintenant se fixer : c'est la nidation. Retenons la "
                "définition : la nidation, ou implantation, est la "
                "fixation du blastocyste dans la muqueuse utérine, "
                "l'endomètre, environ six à sept jours après la "
                "fécondation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma de la nidation ---------------------
        endometre = Rectangle(width=6.0, height=0.9, color="#B42E41", fill_color="#B42E41", fill_opacity=0.35, stroke_width=2)
        endometre.next_to(titre, DOWN, buff=1.6)
        label_endometre = Text("Endomètre (muqueuse utérine)", font_size=15, color=WHITE)
        label_endometre.next_to(endometre, DOWN, buff=0.25)

        blastocele = Circle(radius=0.55, color="#288073", stroke_width=2)
        trophoblaste = Circle(radius=0.62, color="#DE7C1F", stroke_width=3)
        bouton = Circle(radius=0.18, color="#1E5FA8", fill_color="#1E5FA8", fill_opacity=0.8, stroke_width=1)
        bouton.move_to(blastocele.get_center() + LEFT * 0.25)
        blastocyste = VGroup(trophoblaste, blastocele, bouton)
        blastocyste.next_to(endometre, UP, buff=0.35)

        label_bc = Text("Blastocyste : trophoblaste (orange),\nblastocèle, bouton embryonnaire (bleu)", font_size=14, color=WHITE)
        label_bc.next_to(blastocyste, UP, buff=0.25)

        with self.voiceover(
            text=(
                "Voici le blastocyste au-dessus de l'endomètre : le "
                "trophoblaste, en orange, entoure la cavité, le "
                "blastocèle, et le bouton embryonnaire, en bleu. "
                "L'endomètre est alors épais et richement vascularisé, "
                "grâce à l'action de la progestérone sécrétée par le "
                "corps jaune."
            )
        ) as tracker:
            self.play(FadeIn(endometre), FadeIn(label_endometre))
            self.play(FadeIn(blastocyste), FadeIn(label_bc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_bc))

        label_implant = Text("Nidation : le trophoblaste s'enfonce dans l'endomètre", font_size=15, color=YELLOW)
        label_implant.next_to(endometre, UP, buff=2.2)

        with self.voiceover(
            text=(
                "L'œuf perd sa zone pellucide et s'enfonce dans "
                "l'endomètre. Le trophoblaste se développe et formera le "
                "placenta, organe d'échange entre la mère et l'embryon ; "
                "le bouton embryonnaire, lui, donnera l'embryon "
                "proprement dit."
            )
        ) as tracker:
            self.play(blastocyste.animate.shift(DOWN * 0.6), FadeIn(label_implant))
            self.wait(tracker.get_remaining_duration())

        fleche_hcg = Arrow(blastocyste.get_right(), blastocyste.get_right() + RIGHT * 1.6, color=YELLOW, buff=0.1)
        label_hcg = Text("HCG → entretient le\ncorps jaune → détectée\npar les tests de grossesse", font_size=13, color=YELLOW)
        label_hcg.next_to(fleche_hcg, RIGHT, buff=0.15)

        with self.voiceover(
            text=(
                "Dès la nidation, le trophoblaste sécrète une hormone, la "
                "HCG, ou gonadotrophine chorionique, qui entretient le "
                "corps jaune. C'est précisément cette hormone qui est "
                "détectée par les tests de grossesse."
            )
        ) as tracker:
            self.play(FadeIn(fleche_hcg), FadeIn(label_hcg))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(endometre), FadeOut(label_endometre), FadeOut(blastocyste),
            FadeOut(label_implant), FadeOut(fleche_hcg), FadeOut(label_hcg),
        )

        # --- Exemple traité : que se passe-t-il sans nidation ? --------------------
        methode = method_box(
            Text(
                _wrap(
                    "Si la nidation réussit, la grossesse débute. En "
                    "l'absence de fécondation ou de nidation, le corps "
                    "jaune régresse, la chute des hormones provoque les "
                    "règles (menstrues), et l'endomètre est évacué.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ce point clé : si la nidation réussit, la "
                "grossesse débute réellement. En l'absence de fécondation "
                "ou de nidation, en revanche, le corps jaune régresse, la "
                "chute des hormones provoque les règles, et l'endomètre "
                "est évacué : c'est le début d'un nouveau cycle."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # === PARTIE 2 : LES JUMEAUX =================================================

        titre2 = Text("Les jumeaux : vrais ou faux ?", font_size=28, color=YELLOW, weight="BOLD")
        titre2.next_to(titre, DOWN, buff=0.5)

        vrais = Text(
            _wrap(
                "Vrais jumeaux (monozygotes) : fécondation d'UN SEUL "
                "ovule par UN SEUL spermatozoïde, puis séparation de "
                "l'œuf (ou du bouton embryonnaire) en deux parties qui "
                "évoluent chacune en un embryon complet.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        vrais.next_to(titre2, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une grossesse aboutit parfois à la naissance de deux "
                "enfants : des jumeaux. Il faut distinguer deux "
                "situations bien différentes. Les vrais jumeaux, ou "
                "jumeaux monozygotes, proviennent de la fécondation d'un "
                "seul ovule par un seul spermatozoïde, suivie de la "
                "séparation de l'œuf, ou du bouton embryonnaire, en deux "
                "parties qui évoluent chacune en un embryon complet."
            )
        ) as tracker:
            self.play(FadeIn(titre2))
            self.play(FadeIn(vrais))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vrais))

        faux = Text(
            _wrap(
                "Faux jumeaux (dizygotes) : libération de DEUX ovules "
                "lors du même cycle (double ovulation), fécondés chacun "
                "par un spermatozoïde différent.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        faux.next_to(titre2, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les faux jumeaux, ou jumeaux dizygotes, proviennent au "
                "contraire de la libération de deux ovules lors du même "
                "cycle, une double ovulation, fécondés chacun par un "
                "spermatozoïde différent : ce sont deux fécondations "
                "distinctes, simplement simultanées."
            )
        ) as tracker:
            self.play(FadeIn(faux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(faux), FadeOut(titre2))

        # --- À retenir : tableau comparatif -----------------------------------------
        entete_tab = Text("Tableau comparatif", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        rows = [
            ("Critère", "Vrais jumeaux", "Faux jumeaux"),
            ("Ovules fécondés", "1", "2"),
            ("Patrimoine génétique", "Identique", "Différent"),
            ("Sexe", "Toujours identique", "Identique ou différent"),
            ("Ressemblance", "Très forte", "Comme frères/sœurs"),
            ("Placenta", "Souvent unique", "Deux placentas"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=16, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.4, row_gap=0.22)
        tableau.next_to(entete_tab, DOWN, buff=0.35)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = tableau.get_top()[1] - _bas_visible
        if tableau.height > _hauteur_dispo:
            tableau.scale(_hauteur_dispo / tableau.height, about_point=tableau.get_top())

        with self.voiceover(
            text=(
                "Résumons dans un tableau comparatif. Nombre d'ovules "
                "fécondés : un pour les vrais jumeaux, deux pour les faux "
                "jumeaux. Patrimoine génétique : identique pour les "
                "vrais, différent pour les faux. Sexe : toujours "
                "identique pour les vrais, identique ou différent pour "
                "les faux. Ressemblance : très forte pour les vrais, "
                "comparable à des frères et sœurs ordinaires pour les "
                "faux. Placenta : souvent unique pour les vrais, deux "
                "placentas distincts pour les faux."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège à éviter : sexes différents = jamais vrais jumeaux --------------
        piege = warning_box(
            Text(
                _wrap(
                    "Deux jumeaux de sexes différents ne peuvent JAMAIS "
                    "être de vrais jumeaux : ayant le même patrimoine "
                    "génétique, les vrais jumeaux sont obligatoirement du "
                    "même sexe. Autre piège : ne confondez pas nidation "
                    "(dans l'utérus) et fécondation (dans la trompe).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ce piège classique : deux jumeaux de sexes "
                "différents ne peuvent jamais être de vrais jumeaux, "
                "puisque, ayant le même patrimoine génétique, les vrais "
                "jumeaux sont obligatoirement du même sexe. Et n'oubliez "
                "pas non plus de distinguer la nidation, qui a lieu dans "
                "l'utérus, de la fécondation, qui a lieu dans la trompe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
