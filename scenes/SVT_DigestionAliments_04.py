"""
scenes/SVT_DigestionAliments_04.py — Chapitre 12 (1ereD, SVT), scène 04.

§ 12.2.2 Les glandes digestives et les sucs digestifs : définition de
« suc digestif » et « enzyme », les 5 glandes, tableau récapitulatif
(volume, pH, enzymes), exemple « la bile est-elle riche en enzymes ? »,
piège des trois erreurs classiques.
Source : 1ereD/SVT.pdf, pages 157-158.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _cell(text: str, x: float, y: float, font_size=15, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


class GlandesDigestivesEtSucsDigestifs(NotionScene):
    def construct(self):
        titre = scene_title("12.2.2 — Glandes et sucs digestifs")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : définition suc digestif / enzyme -----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un suc digestif est un liquide sécrété par une glande "
                    "digestive ; il contient de l'eau, des sels et le plus "
                    "souvent des enzymes. Une enzyme digestive est une "
                    "protéine qui accélère (catalyse) le découpage d'une "
                    "substance précise, son substrat : l'enzyme est "
                    "spécifique de ce substrat.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un suc digestif est un liquide sécrété par une glande "
                "digestive ; il contient de l'eau, des sels et, le plus "
                "souvent, des enzymes. Une enzyme digestive est une "
                "protéine qui accélère — on dit qu'elle catalyse — le "
                "découpage d'une substance précise, appelée son substrat : "
                "l'enzyme est spécifique de ce substrat."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : les 5 glandes digestives -----------
        entete = Text("Les cinq glandes digestives", font_size=25, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.45)

        glandes = _bullets(
            [
                "Glandes salivaires (parotides, sous-maxillaires, sublinguales) → salive.",
                "Glandes gastriques (paroi de l'estomac) → suc gastrique.",
                "Foie (plus grosse glande du corps) → bile, stockée dans la vésicule biliaire.",
                "Pancréas → suc pancréatique, déversé dans le duodénum.",
                "Glandes intestinales (paroi de l'intestin grêle) → suc intestinal.",
            ],
            font_size=21,
            width=54,
        )
        glandes.next_to(entete, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les principales glandes digestives sont : les glandes "
                "salivaires, trois paires — parotides, sous-maxillaires et "
                "sublinguales — qui produisent la salive ; les glandes "
                "gastriques, logées dans la paroi de l'estomac, qui "
                "produisent le suc gastrique ; le foie, la plus grosse "
                "glande de l'organisme, qui produit la bile, stockée et "
                "concentrée dans la vésicule biliaire avant d'être "
                "déversée dans le duodénum ; le pancréas, qui produit le "
                "suc pancréatique, déversé lui aussi dans le duodénum ; et "
                "les glandes intestinales, disséminées dans la paroi de "
                "l'intestin grêle, qui produisent le suc intestinal."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(glandes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(glandes))

        # --- Tableau récapitulatif -------------------------------------------
        entete_tab = Text("Tableau récapitulatif des sucs digestifs", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.to_edge(UP).shift(DOWN * 1.0)

        x_glande, x_suc, x_ph, x_enz = -6.6, -3.7, -1.5, -0.2
        rows_data = [
            ("Glande", "Suc / volume", "pH", "Enzymes"),
            ("Salivaires", "salive, 1-1,5 L/j", "≈7", "amylase salivaire"),
            ("Gastriques", "suc gastrique, 2-3 L/j", "1,5-2", "pepsine, lipase gastr."),
            ("Foie", "bile, 0,5-1 L/j", "≈7,5", "aucune enzyme"),
            ("Pancréas", "suc pancr., 1-1,5 L/j", "≈8", "amylase, trypsine, lipase"),
            ("Intestinales", "suc intest., ≈2 L/j", "≈7,5", "peptidases, maltase,\nsaccharase, lactase,\nentérokinase"),
        ]
        row_ys = [2.9, 2.0, 1.1, 0.2, -0.7, -1.9]

        table_rows = VGroup()
        for i, (glande, suc, ph, enz) in enumerate(rows_data):
            bold = i == 0
            color = YELLOW if bold else WHITE
            fs = 17 if bold else 15
            row = VGroup(
                _cell(glande, x_glande, row_ys[i], font_size=fs, color=color, bold=bold),
                _cell(suc, x_suc, row_ys[i], font_size=fs, color=color, bold=bold),
                _cell(ph, x_ph, row_ys[i], font_size=fs, color=color, bold=bold),
                _cell(enz, x_enz, row_ys[i], font_size=fs, color=color, bold=bold),
            )
            table_rows.add(row)

        with self.voiceover(
            text=(
                "Voici le tableau récapitulatif. Les glandes salivaires "
                "sécrètent un litre à un litre et demi de salive par "
                "jour, de pH voisin de sept, avec l'amylase salivaire. "
                "Les glandes gastriques sécrètent deux à trois litres de "
                "suc gastrique, très acide, pH un virgule cinq à deux, "
                "avec pepsine et lipase gastrique. Le foie sécrète zéro "
                "virgule cinq à un litre de bile, pH voisin de sept "
                "virgule cinq, sans aucune enzyme. Le pancréas sécrète un "
                "à un litre et demi de suc pancréatique, pH voisin de "
                "huit, avec amylase, trypsine et lipase. Les glandes "
                "intestinales sécrètent environ deux litres de suc "
                "intestinal, pH voisin de sept virgule cinq, avec "
                "peptidases, maltase, saccharase, lactase et entérokinase."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            for row in table_rows:
                self.play(FadeIn(row), run_time=0.5)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table_rows))

        # --- Exemple traité : la bile est-elle riche en enzymes ? ------------
        exemple = example_box(
            Text(
                _wrap(
                    "Question : la bile est-elle un suc digestif riche en "
                    "enzymes ? Réponse : non. Produite par le foie et "
                    "stockée dans la vésicule biliaire, la bile ne "
                    "contient aucune enzyme. Son rôle est physique : ses "
                    "sels biliaires émulsionnent les graisses, divisant "
                    "les grosses gouttes d'huile en gouttelettes "
                    "microscopiques, ce qui facilite l'action de la "
                    "lipase.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : la bile est-elle un suc digestif riche en "
                "enzymes ? La réponse est non. La bile, produite par le "
                "foie et stockée dans la vésicule biliaire, ne contient "
                "aucune enzyme. Son rôle est physique : ses sels biliaires "
                "émulsionnent les graisses, c'est-à-dire qu'ils divisent "
                "les grosses gouttes d'huile en gouttelettes "
                "microscopiques. La surface de contact entre les graisses "
                "et la lipase devient alors beaucoup plus grande, ce qui "
                "facilite la digestion chimique des lipides."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Piège : trois erreurs classiques ---------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Trois erreurs classiques : (1) attribuer la "
                    "fabrication de la bile à la vésicule biliaire — elle "
                    "ne fait que la stocker, c'est le foie qui la "
                    "produit. (2) croire que le pancréas ne fait que "
                    "réguler le sucre sanguin — il a aussi un rôle "
                    "digestif (suc pancréatique). (3) oublier les glandes "
                    "gastriques et intestinales, disséminées dans la "
                    "paroi du tube.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Trois erreurs classiques à éviter. Première erreur : "
                "attribuer la fabrication de la bile à la vésicule "
                "biliaire — la vésicule ne fait que stocker la bile "
                "produite par le foie. Deuxième erreur : croire que le "
                "pancréas ne sert qu'à réguler le taux de sucre dans le "
                "sang — il a une double fonction, digestive et hormonale. "
                "Troisième erreur : oublier les glandes gastriques et "
                "intestinales — toutes les glandes digestives ne sont pas "
                "de gros organes séparés du tube."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
