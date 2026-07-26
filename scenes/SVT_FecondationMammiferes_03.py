"""
scenes/SVT_FecondationMammiferes_03.py — Chapitre 4 (1ereC, SVT), scène 03.

§ 3.1 La capacitation (définition, modifications physiologiques, preuve
expérimentale = base de la FIVETE) + § 3.2 la réaction acrosomique
(définition, libération des enzymes de l'acrosome).
Source : 1ereC/SVT.pdf, pages 36-37.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _spermatozoide(with_coating: bool):
    """Petit schéma d'un spermatozoïde : tête + flagelle, avec ou sans
    "manteau" de substances protectrices provenant du liquide séminal."""
    tete = Circle(radius=0.2, color=WHITE, fill_color=WHITE, fill_opacity=0.6, stroke_width=2)
    flagelle = Line(tete.get_right(), tete.get_right() + RIGHT * 1.1, color=WHITE, stroke_width=2)
    groupe = VGroup(tete, flagelle)
    if with_coating:
        manteau = Circle(radius=0.32, color="#66CCFF", stroke_width=2, stroke_opacity=0.9)
        manteau.move_to(tete.get_center())
        groupe.add_to_back(manteau)
    return groupe


class CapacitationReactionAcrosomique(NotionScene):
    def construct(self):
        titre = scene_title("4.3 — Capacitation et réaction acrosomique")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition de la capacitation ------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La capacitation est l'ensemble des modifications "
                    "physiologiques que subissent les spermatozoïdes au "
                    "cours de leur trajet dans les voies génitales "
                    "féminines, et qui leur donnent le pouvoir fécondant.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les spermatozoïdes fraîchement éjaculés ne sont pas "
                "encore capables de féconder : ils doivent d'abord subir "
                "la capacitation. Retenons la définition : la capacitation "
                "est l'ensemble des modifications physiologiques que "
                "subissent les spermatozoïdes au cours de leur trajet dans "
                "les voies génitales féminines, et qui leur donnent le "
                "pouvoir fécondant."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : avant / après capacitation --------------
        avant = _spermatozoide(with_coating=True)
        apres = _spermatozoide(with_coating=False)
        chaine = VGroup(avant, apres).arrange(RIGHT, buff=2.3)
        chaine.next_to(titre, DOWN, buff=0.9)

        label_avant = Text(
            "Fraîchement éjaculé :\nsubstances protectrices du\nliquide séminal, non fécondant",
            font_size=15,
            color=WHITE,
        )
        label_avant.next_to(avant, DOWN, buff=0.3)
        label_apres = Text(
            "Après capacitation :\nmembrane perméable,\nmouvements vigoureux, fécondant",
            font_size=15,
            color=WHITE,
        )
        label_apres.next_to(apres, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Fraîchement éjaculés, les spermatozoïdes sont recouverts "
                "de substances protectrices provenant du liquide séminal, "
                "représentées ici en bleu clair : ils sont incapables de "
                "féconder. Dans l'utérus puis la trompe, ces substances "
                "sont progressivement éliminées, la membrane du "
                "spermatozoïde devient perméable, et ses mouvements "
                "deviennent plus vigoureux. La capacitation dure quelques "
                "heures."
            )
        ) as tracker:
            self.play(FadeIn(avant), FadeIn(label_avant))
            self.wait(1)
            self.play(FadeIn(apres), FadeIn(label_apres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(chaine), FadeOut(label_avant), FadeOut(label_apres))

        # --- Exemple traité : la preuve expérimentale -----------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Des spermatozoïdes prélevés dans l'épididyme ou dans "
                    "l'éjaculat, déposés sur un ovule in vitro SANS séjour "
                    "préalable, ne fécondent pas l'ovule. Après séjour "
                    "dans les voies génitales féminines (ou un milieu de "
                    "culture approprié), ils deviennent fécondants. Cette "
                    "découverte est à la base de la FIVETE.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la preuve expérimentale de la capacitation : des "
                "spermatozoïdes prélevés directement dans l'épididyme ou "
                "dans l'éjaculat, et déposés sur un ovule in vitro, sans "
                "séjour préalable, ne fécondent pas l'ovule. En revanche, "
                "après un séjour dans les voies génitales féminines, ou "
                "dans un milieu de culture approprié, ils deviennent "
                "fécondants. Cette découverte est à la base de la "
                "FIVETE : on sait désormais reproduire la capacitation en "
                "laboratoire."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : définition de la réaction acrosomique -------------------
        definition2 = definition_box(
            Text(
                _wrap(
                    "La réaction acrosomique est la libération des "
                    "enzymes contenues dans l'acrosome (vésicule à "
                    "l'extrémité de la tête du spermatozoïde), au contact "
                    "des enveloppes de l'ovule. Au contact de la couronne "
                    "radiée et de la zone pellucide, la membrane de "
                    "l'acrosome éclate et libère des enzymes digestives "
                    "(dont l'hyaluronidase) qui creusent un passage.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.4,
        )
        definition2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fois capacité, le spermatozoïde peut déclencher la "
                "réaction acrosomique : la libération des enzymes "
                "contenues dans l'acrosome, une vésicule située à "
                "l'extrémité de sa tête, au contact des enveloppes de "
                "l'ovule. La membrane de l'acrosome éclate et libère des "
                "enzymes digestives, dont l'hyaluronidase, qui dissolvent "
                "localement les enveloppes de l'ovule et creusent un "
                "passage pour le spermatozoïde."
            )
        ) as tracker:
            self.play(FadeIn(definition2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition2))

        # --- Piège à éviter : ne pas confondre les deux étapes -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas capacitation et réaction "
                    "acrosomique : la capacitation modifie le "
                    "spermatozoïde LUI-MÊME pendant son trajet (avant la "
                    "rencontre avec l'ovule) ; la réaction acrosomique "
                    "libère des enzymes AU CONTACT des enveloppes de "
                    "l'ovule. La capacitation est un préalable "
                    "indispensable à la réaction acrosomique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre les deux étapes : la "
                "capacitation modifie le spermatozoïde lui-même pendant "
                "son trajet, avant la rencontre avec l'ovule, alors que la "
                "réaction acrosomique libère des enzymes au contact "
                "direct des enveloppes de l'ovule. La capacitation est un "
                "préalable indispensable : sans elle, la réaction "
                "acrosomique ne peut pas avoir lieu."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
