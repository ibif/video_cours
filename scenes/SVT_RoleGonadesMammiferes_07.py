"""
scenes/SVT_RoleGonadesMammiferes_07.py — Chapitre 1 (1ereC, SVT), scène 07.

Tableau de synthèse comparatif testicule/ovaire + caractères sexuels
primaires et secondaires. Source : 1ereC/SVT.pdf, page 11.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Line, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=44):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class SyntheseComparativeCaracteresSexuels(NotionScene):
    def construct(self):
        titre = scene_title("1.7 — Synthèse testicule / ovaire")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : présentation du tableau comparatif -----------------------
        enonce = Text(
            _wrap(
                "Après avoir étudié séparément le testicule et l'ovaire, "
                "comparons maintenant les deux gonades critère par "
                "critère.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Après avoir étudié séparément la structure du testicule et "
                "celle de l'ovaire, comparons maintenant les deux gonades, "
                "critère par critère, dans un tableau de synthèse."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : construction du tableau ----------------
        criteres = ["Gamète produit", "Cellules nourricières", "Cellules endocrines", "Hormone principale", "Production"]
        testicule_vals = ["Spermatozoïde", "Cellules de Sertoli", "Cellules de Leydig", "Testostérone", "Continue (dès la puberté)"]
        ovaire_vals = ["Ovule (ovocyte II)", "Cellules folliculeuses", "Thèque interne, corps jaune", "Œstrogènes, progestérone", "Cyclique (jusqu'à la ménopause)"]

        col_critere = VGroup(*[Text(c, font_size=18, color=YELLOW) for c in criteres]).arrange(
            DOWN, aligned_edge=LEFT, buff=0.35
        )
        col_testicule = VGroup(
            *[Text(_wrap(v, width=22), font_size=16, color=WHITE) for v in testicule_vals]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        col_ovaire = VGroup(
            *[Text(_wrap(v, width=22), font_size=16, color=WHITE) for v in ovaire_vals]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)

        entete_t = Text("TESTICULE", font_size=20, color="#1E5FA8", weight="BOLD")
        entete_o = Text("OVAIRE", font_size=20, color="#A42A5A", weight="BOLD")

        col_critere.next_to(titre, DOWN, buff=0.9).to_edge(LEFT, buff=1.0)
        entete_t.next_to(col_critere, RIGHT, buff=0.9)
        entete_o.next_to(entete_t, RIGHT, buff=1.1)

        col_testicule.next_to(entete_t, DOWN, buff=0.3).align_to(entete_t, LEFT)
        col_ovaire.next_to(entete_o, DOWN, buff=0.3).align_to(entete_o, LEFT)

        for i in range(len(criteres)):
            col_testicule[i].align_to(col_critere[i], UP)
            col_ovaire[i].align_to(col_critere[i], UP)

        ligne_sep = Line(
            entete_t.get_left() + UP * 0.35 + LEFT * 0.3,
            entete_o.get_right() + UP * 0.35 + RIGHT * 0.3,
            color=WHITE,
        )

        tableau = VGroup(col_critere, entete_t, entete_o, col_testicule, col_ovaire, ligne_sep)

        with self.voiceover(
            text=(
                "Pour le gamète produit : le testicule produit un "
                "spermatozoïde, l'ovaire un ovule, aussi appelé ovocyte "
                "second. Pour les cellules nourricières : ce sont les "
                "cellules de Sertoli chez l'homme, les cellules "
                "folliculeuses chez la femme. Pour les cellules endocrines : "
                "les cellules de Leydig chez l'homme, la thèque interne et "
                "le corps jaune chez la femme. Pour l'hormone principale : "
                "la testostérone chez l'homme, les œstrogènes et la "
                "progestérone chez la femme."
            )
        ) as tracker:
            self.play(FadeIn(col_critere))
            self.play(FadeIn(entete_t), FadeIn(entete_o), FadeIn(ligne_sep))
            self.play(FadeIn(col_testicule[0]), FadeIn(col_ovaire[0]))
            self.play(FadeIn(col_testicule[1]), FadeIn(col_ovaire[1]))
            self.play(FadeIn(col_testicule[2]), FadeIn(col_ovaire[2]))
            self.play(FadeIn(col_testicule[3]), FadeIn(col_ovaire[3]))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Enfin, pour le rythme de production : le testicule produit "
                "des spermatozoïdes en continu, dès la puberté et tout au "
                "long de la vie, alors que l'ovaire ne libère qu'un ovocyte "
                "environ par cycle, de façon cyclique, jusqu'à la "
                "ménopause."
            )
        ) as tracker:
            self.play(FadeIn(col_testicule[4]), FadeIn(col_ovaire[4]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Exemple traité : classement des caractères sexuels -----------------
        exemple = example_box(
            Text(
                _wrap(
                    "Classons : barbe, trompes de Fallope, seins "
                    "développés, vagin, voix grave, testicules. Présents "
                    "dès la naissance -> PRIMAIRES : trompes, vagin, "
                    "testicules. Apparus à la puberté -> SECONDAIRES : "
                    "barbe, seins, voix grave.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Appliquons cela : classons la barbe, les trompes de "
                "Fallope, les seins développés, le vagin, la voix grave et "
                "les testicules. Les caractères sexuels primaires sont les "
                "organes reproducteurs eux-mêmes, présents dès la "
                "naissance : les trompes, le vagin, les testicules. Les "
                "caractères sexuels secondaires sont les caractères "
                "morphologiques qui apparaissent à la puberté : la barbe, "
                "les seins développés, la voix grave."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : définitions primaires / secondaires ---------------------
        retenir = property_box(
            Text(
                _wrap(
                    "Caractères sexuels PRIMAIRES : les organes "
                    "reproducteurs eux-mêmes (gonades, voies génitales), "
                    "présents dès la naissance, déterminés génétiquement. "
                    "Caractères sexuels SECONDAIRES : caractères "
                    "morphologiques apparaissant à la puberté sous "
                    "l'influence des hormones sexuelles.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons les deux définitions. Les caractères sexuels "
                "primaires sont les organes reproducteurs eux-mêmes, les "
                "gonades et les voies génitales, présents dès la naissance "
                "et déterminés génétiquement. Les caractères sexuels "
                "secondaires sont les caractères morphologiques qui "
                "apparaissent à la puberté, sous l'influence des hormones "
                "sexuelles."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter : production continue vs cyclique -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Erreur fréquente : croire que la production de "
                    "gamètes est continue chez les DEUX sexes. En réalité, "
                    "seul le testicule produit en continu ; l'ovaire "
                    "libère environ un seul ovocyte par cycle, et cette "
                    "production cyclique s'arrête définitivement à la "
                    "ménopause.",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à une erreur fréquente : croire que la "
                "production de gamètes est continue chez les deux sexes. En "
                "réalité, seul le testicule produit en continu ; l'ovaire "
                "ne libère qu'environ un seul ovocyte par cycle, et cette "
                "production cyclique s'arrête définitivement à la "
                "ménopause."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
