"""
scenes/SVT_MouvementsPlaques_02.py — Chapitre 7 (1ereD, SVT), scène 02.

§ 7.1.1-7.1.2 Rappel de la structure interne de la Terre (croûte, manteau,
noyau) et découpage mécanique lithosphère / asthénosphère : définitions,
tableau des enveloppes, propriété du glissement, remarque sur les ondes
sismiques, attention à ne pas confondre croûte et lithosphère.
Source : 1ereD/SVT.pdf, pages 91-92.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
    GRAY_C,
    GRAY_E,
    GOLD,
    RED_E,
    BLUE_E,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.5, row_gap=0.28):
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


def _coupe_terre():
    """Schéma simplifié en coupe : croûte, manteau, noyau externe, graine."""
    croute = Circle(radius=1.9, fill_color=GOLD, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    manteau = Circle(radius=1.75, fill_color=ORANGE, fill_opacity=1, stroke_width=0)
    noyau_ext = Circle(radius=0.95, fill_color=RED_E, fill_opacity=1, stroke_width=0)
    graine = Circle(radius=0.45, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
    return VGroup(croute, manteau, noyau_ext, graine)


class StructureLithosphereAsthenosphere(NotionScene):
    def construct(self):
        titre = scene_title("7.1 — Structure du globe et lithosphère")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : rappel des 3 enveloppes -------------------------------
        definition_enveloppes = definition_box(
            Text(
                _wrap(
                    "La croûte : enveloppe superficielle très mince, 5-10 km "
                    "sous les océans (basaltes), 30-70 km sous les continents "
                    "(granites). Le manteau : de la base de la croûte à 2900 "
                    "km, roches denses riches en fer/magnésium (péridotites). "
                    "Le noyau : de 2900 à 6370 km, riche en fer et nickel ; "
                    "noyau externe liquide et noyau interne solide (la "
                    "« graine »).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        definition_enveloppes.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Rappelons d'abord la structure interne de la Terre, "
                "distinguée par la composition chimique des roches. La "
                "croûte est l'enveloppe superficielle, très mince : cinq à "
                "dix kilomètres sous les océans, faite de basaltes, et "
                "trente à soixante-dix kilomètres sous les continents, faite "
                "de granites. Le manteau s'étend de la base de la croûte "
                "jusqu'à deux mille neuf cents kilomètres de profondeur, des "
                "roches denses riches en fer et en magnésium appelées "
                "péridotites. Le noyau, enfin, va de deux mille neuf cents à "
                "six mille trois cent soixante-dix kilomètres, riche en fer "
                "et en nickel : un noyau externe liquide et un noyau "
                "interne solide, surnommé la graine."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_enveloppes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_enveloppes))

        # --- Animation du raisonnement : coupe de la Terre + remarque ondes -
        coupe = _coupe_terre()
        coupe.next_to(titre, DOWN, buff=0.6).shift(LEFT * 3.2)

        label_croute = Text("Croûte", font_size=18, color=WHITE)
        label_croute.next_to(coupe, RIGHT, buff=1.6).shift(UP * 1.4)
        fleche_croute = Line(coupe.get_top() + RIGHT * 0.1, label_croute.get_left(), color=WHITE, stroke_width=1.5)

        label_manteau = Text("Manteau", font_size=18, color=WHITE)
        label_manteau.next_to(coupe, RIGHT, buff=1.6).shift(UP * 0.55)
        fleche_manteau = Line(
            coupe.get_center() + UP * 1.3, label_manteau.get_left(), color=WHITE, stroke_width=1.5
        )

        label_noyau_ext = Text("Noyau externe (liquide)", font_size=18, color=WHITE)
        label_noyau_ext.next_to(coupe, RIGHT, buff=1.6).shift(DOWN * 0.3)
        fleche_noyau_ext = Line(
            coupe.get_center() + UP * 0.6, label_noyau_ext.get_left(), color=WHITE, stroke_width=1.5
        )

        label_graine = Text("Noyau interne (solide)", font_size=18, color=WHITE)
        label_graine.next_to(coupe, RIGHT, buff=1.6).shift(DOWN * 1.1)
        fleche_graine = Line(coupe.get_center(), label_graine.get_left(), color=WHITE, stroke_width=1.5)

        schema = VGroup(
            coupe,
            label_croute, fleche_croute,
            label_manteau, fleche_manteau,
            label_noyau_ext, fleche_noyau_ext,
            label_graine, fleche_graine,
        )

        with self.voiceover(
            text=(
                "Voici une coupe très simplifiée du globe : au centre, la "
                "graine solide ; autour, le noyau externe liquide ; puis "
                "l'épais manteau ; et tout en surface, la fine pellicule de "
                "la croûte."
            )
        ) as tracker:
            self.play(FadeIn(coupe))
            self.play(
                FadeIn(label_croute), FadeIn(fleche_croute),
                FadeIn(label_manteau), FadeIn(fleche_manteau),
            )
            self.play(
                FadeIn(label_noyau_ext), FadeIn(fleche_noyau_ext),
                FadeIn(label_graine), FadeIn(fleche_graine),
            )
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        remarque_ondes = warning_box(
            Text(
                _wrap(
                    "Comment connaît-on l'intérieur de la Terre ? Aucun "
                    "forage n'a dépassé environ 12 km : on n'a jamais atteint "
                    "le manteau directement. Les connaissances viennent de "
                    "l'étude des ondes sismiques, dont la vitesse et la "
                    "trajectoire changent à certaines profondeurs "
                    "(discontinuités révélant les limites entre les "
                    "enveloppes).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        remarque_ondes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment connaît-on l'intérieur de la Terre, alors qu'aucun "
                "forage n'a jamais dépassé environ douze kilomètres ? On "
                "n'a jamais atteint directement le manteau. Ces "
                "connaissances viennent en réalité de l'étude des ondes "
                "sismiques, dont la vitesse et la trajectoire changent "
                "brusquement à certaines profondeurs : ce sont ces "
                "discontinuités qui révèlent les limites entre croûte, "
                "manteau et noyau."
            )
        ) as tracker:
            self.play(FadeIn(remarque_ondes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_ondes))

        # --- Exemple traité : tableau des enveloppes -------------------------
        entete_tab = Text("Tableau des enveloppes du globe", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        header = [
            Text("Enveloppe", font_size=18, color=YELLOW, weight="BOLD"),
            Text("Profondeur", font_size=18, color=YELLOW, weight="BOLD"),
            Text("Composition", font_size=18, color=YELLOW, weight="BOLD"),
            Text("État", font_size=18, color=YELLOW, weight="BOLD"),
        ]
        rows = [
            ("Croûte", "0-5/10 km (océans)\n0-30/70 km (continents)", "basaltes / granites", "solide"),
            ("Manteau", "jusqu'à 2900 km", "péridotites", "solide déformable"),
            ("Noyau externe", "2900-5100 km", "fer / nickel", "liquide"),
            ("Noyau interne", "5100-6370 km", "fer / nickel", "solide"),
        ]
        cell_matrix = [header]
        for nom, prof, comp, etat in rows:
            cell_matrix.append([
                Text(nom, font_size=17, color=WHITE),
                Text(prof, font_size=15, color=WHITE),
                Text(comp, font_size=17, color=WHITE),
                Text(etat, font_size=17, color=WHITE),
            ])
        tableau = _grid_table(cell_matrix, col_gap=0.45, row_gap=0.22)
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        tableau.scale(0.82)

        with self.voiceover(
            text=(
                "Résumons dans un tableau. La croûte : de zéro à cinq ou dix "
                "kilomètres sous les océans, de zéro à trente ou soixante-dix "
                "kilomètres sous les continents, basaltes ou granites, "
                "solide. Le manteau : jusqu'à deux mille neuf cents "
                "kilomètres, péridotites, solide mais déformable. Le noyau "
                "externe : de deux mille neuf cents à cinq mille cent "
                "kilomètres, fer et nickel, liquide. Le noyau interne : de "
                "cinq mille cent à six mille trois cent soixante-dix "
                "kilomètres, fer et nickel, solide."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : lithosphère / asthénosphère ------------------------
        definition_litho = definition_box(
            Text(
                _wrap(
                    "La lithosphère (grec lithos, « pierre ») est l'enveloppe "
                    "externe rigide de la Terre. Elle comprend la croûte et la "
                    "partie supérieure du manteau, le manteau lithosphérique. "
                    "Épaisseur moyenne : ~100 km sous les océans, 150-200 km "
                    "sous les vieux continents.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition_litho.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour comprendre les mouvements des plaques, il faut "
                "découper le globe autrement : non plus selon la "
                "composition chimique, mais selon le comportement mécanique "
                "des roches, rigide ou ductile. La lithosphère, du grec "
                "lithos, la pierre, est l'enveloppe externe rigide de la "
                "Terre. Elle comprend la croûte et la partie supérieure du "
                "manteau, appelée manteau lithosphérique. Son épaisseur "
                "moyenne est d'environ cent kilomètres sous les océans, et "
                "de cent cinquante à deux cents kilomètres sous les vieux "
                "continents."
            )
        ) as tracker:
            self.play(FadeIn(definition_litho))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_litho))

        definition_asth = definition_box(
            Text(
                _wrap(
                    "L'asthénosphère (grec asthenès, « faible ») est la "
                    "partie du manteau sous la lithosphère, entre 100 et 350 "
                    "km de profondeur environ. Roches à plus de 1300°C, "
                    "ductiles, se déformant lentement sans se rompre (comme "
                    "du mastic), avec une faible part partiellement fondue.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition_asth.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Juste en dessous se trouve l'asthénosphère, du grec "
                "asthenès, faible. C'est la partie du manteau située sous la "
                "lithosphère, entre environ cent et trois cent cinquante "
                "kilomètres de profondeur. Ses roches, à plus de treize "
                "cents degrés, sont ductiles : elles se déforment lentement "
                "sans se rompre, un peu comme du mastic, avec une faible "
                "part partiellement fondue."
            )
        ) as tracker:
            self.play(FadeIn(definition_asth))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_asth))

        # Schéma : lithosphère rigide posée sur l'asthénosphère ductile
        bloc_litho = Rectangle(width=8.0, height=0.9, fill_color=GRAY_C, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
        bloc_asth = Rectangle(width=8.0, height=1.3, fill_color=RED_E, fill_opacity=0.55, stroke_color=WHITE, stroke_width=1)
        bloc_manteau_inf = Rectangle(width=8.0, height=0.6, fill_color=ORANGE, fill_opacity=0.8, stroke_width=0)
        empilement = VGroup(bloc_litho, bloc_asth, bloc_manteau_inf).arrange(DOWN, buff=0)
        empilement.next_to(titre, DOWN, buff=0.55)

        label_litho = Text("Lithosphère (rigide)", font_size=20, color=WHITE)
        label_litho.next_to(bloc_litho, LEFT, buff=0.3)
        label_asth = Text("Asthénosphère (ductile)", font_size=20, color=WHITE)
        label_asth.next_to(bloc_asth, LEFT, buff=0.3)
        label_manteau_inf = Text("Manteau plus profond", font_size=18, color=WHITE)
        label_manteau_inf.next_to(bloc_manteau_inf, LEFT, buff=0.3)

        fleche_glisse = Line(LEFT * 2.2, RIGHT * 2.2, color=YELLOW, stroke_width=4)
        fleche_glisse.next_to(bloc_litho, UP, buff=0.15)
        label_glisse = Text("glissement de la plaque", font_size=16, color=YELLOW)
        label_glisse.next_to(fleche_glisse, UP, buff=0.1)

        schema_glissement = VGroup(
            empilement, label_litho, label_asth, label_manteau_inf, fleche_glisse, label_glisse
        )

        propriete_glissement = property_box(
            Text(
                _wrap(
                    "La lithosphère, rigide, repose sur l'asthénosphère, "
                    "ductile : elle peut glisser à sa surface. Ce glissement "
                    "est la condition mécanique des mouvements des plaques.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )

        with self.voiceover(
            text=(
                "Voici le point mécanique essentiel : la lithosphère, "
                "rigide, repose sur l'asthénosphère, ductile, et peut donc "
                "glisser lentement à sa surface. Ce glissement est la "
                "condition mécanique de tous les mouvements des plaques que "
                "nous allons étudier dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(empilement), FadeIn(label_litho), FadeIn(label_asth), FadeIn(label_manteau_inf))
            self.play(FadeIn(fleche_glisse), FadeIn(label_glisse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_glissement))
        propriete_glissement.next_to(titre, DOWN, buff=0.5)
        self.play(FadeIn(propriete_glissement))
        self.wait(1)
        self.play(FadeOut(propriete_glissement))

        # --- Piège à éviter : croûte ≠ lithosphère --------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Erreur fréquente : « les plaques sont des morceaux de "
                    "croûte ». Faux : une plaque comprend la croûte plus le "
                    "manteau supérieur rigide, ~100 km au total. La croûte "
                    "seule ne fait que 5-10 km sous les océans. Formule : "
                    "lithosphère = croûte + manteau supérieur rigide.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à une erreur très fréquente : croire que les "
                "plaques sont de simples morceaux de croûte. C'est faux : "
                "une plaque comprend la croûte, plus le manteau supérieur "
                "rigide, soit environ cent kilomètres au total, alors que "
                "la croûte seule ne fait que cinq à dix kilomètres sous les "
                "océans. Retenez la formule : lithosphère égale croûte plus "
                "manteau supérieur rigide."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
