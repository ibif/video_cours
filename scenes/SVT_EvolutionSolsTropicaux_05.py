"""
scenes/SVT_EvolutionSolsTropicaux_05.py — Chapitre 9 (1ereD, SVT), scène 05.

§ 9.4 Les facteurs d'évolution des sols tropicaux — définition, les 6
facteurs (climat, roche mère, relief, végétation, temps, homme), tableau,
exemple bas-fond de Gagnoa vs plateau (toposéquence), attention le climat
ne fait pas tout. Source : 1ereD/SVT.pdf, pages 120-121.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    RED,
    Arrow,
    FadeIn,
    FadeOut,
    Polygon,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LesFacteursEvolutionDesSols(NotionScene):
    def construct(self):
        titre = scene_title("9.4 — Les facteurs d'évolution des sols tropicaux")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : définition des facteurs ---------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Les facteurs d'évolution (ou de formation) d'un sol : "
                    "le climat, la roche mère, le relief, la végétation et "
                    "les êtres vivants, le temps, les activités humaines.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Les facteurs d'évolution, ou de formation, d'un sol sont "
                "au nombre de six : le climat, la roche mère, le relief, la "
                "végétation et les êtres vivants, le temps, et les "
                "activités humaines."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : les 6 facteurs détaillés ------------
        entete_facteurs = Text("Le rôle de chaque facteur", font_size=26, color=YELLOW, weight="BOLD")
        entete_facteurs.next_to(titre, DOWN, buff=0.4)

        facteurs = _bullets(
            [
                "Climat : domine sous les tropiques — chaleur accélère les réactions, pluies fournissent l'eau et lessivent.",
                "Roche mère : granite → sols sableux filtrants ; basalte → sols argileux riches ; calcaire → sols bruns structurés.",
                "Relief : plateau → lessivage ; pente → sol mince érodé ; bas-fond → sol engorgé.",
                "Végétation : forêt → litière abondante ; savane → moins de litière, feux de brousse.",
                "Temps : sol jeune ressemble à la roche mère ; sol vieux porte la marque d'un long lessivage.",
                "Activités humaines : défrichements/feux dégradent ; couverts végétaux/fumures conservent.",
            ],
            font_size=18,
            width=54,
        )
        facteurs.next_to(entete_facteurs, DOWN, buff=0.35)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = facteurs.get_top()[1] - _bas_visible
        if facteurs.height > _hauteur_dispo:
            facteurs.scale(_hauteur_dispo / facteurs.height, about_point=facteurs.get_top())

        with self.voiceover(
            text=(
                "Détaillons le rôle de chaque facteur. Le climat domine "
                "sous les tropiques : les températures élevées accélèrent "
                "les réactions chimiques et la vie microbienne, tandis que "
                "les pluies abondantes, entre mille deux cents et plus de "
                "deux mille millimètres par an dans le Sud ivoirien, "
                "fournissent l'eau de l'hydrolyse et lessivent le sol ; du "
                "Sud forestier humide vers le Nord soudanien plus sec, le "
                "lessivage diminue. La roche mère fournit le matériau "
                "initial : le granite donne des sols sableux et filtrants, "
                "le basalte des sols argileux sombres et riches, le "
                "calcaire des sols bruns bien structurés. Le relief "
                "commande le destin de l'eau : sur un plateau, l'eau "
                "s'infiltre et lessive tout le profil ; sur une pente, elle "
                "ruisselle et laisse un sol mince et tronqué ; dans un "
                "bas-fond, elle s'accumule et engorge le sol. La "
                "végétation et les êtres vivants apportent la matière "
                "organique : la forêt dense produit une litière abondante "
                "et un recyclage rapide, la savane moins de litière, et les "
                "feux de brousse en détruisent une partie chaque année. Le "
                "temps : un sol jeune ressemble encore à sa roche mère, un "
                "sol vieux, sur les vieux plateaux, porte la marque d'une "
                "longue histoire de lessivage. Enfin, les activités "
                "humaines accélèrent ou freinent l'évolution : "
                "défrichements, feux, cultures et surpâturage dégradent, "
                "tandis que couverts végétaux, fumures et terrasses "
                "conservent."
            )
        ) as tracker:
            self.play(FadeIn(entete_facteurs))
            self.play(FadeIn(facteurs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_facteurs), FadeOut(facteurs))

        # --- Exemple traité : toposéquence Gagnoa (plateau / bas-fond) -------
        entete_topo = Text("Toposéquence : plateau et bas-fond de Gagnoa", font_size=22, color=YELLOW, weight="BOLD")
        entete_topo.next_to(titre, DOWN, buff=0.4)

        # Coupe simplifiée du relief : plateau (gauche, haut), pente, bas-fond (droite, bas)
        relief = Polygon(
            [-3.4, 0.8, 0], [-1.0, 0.8, 0], [1.6, -0.9, 0], [3.4, -0.9, 0],
            [3.4, -1.6, 0], [-3.4, -1.6, 0],
            fill_color="#8A7A63", fill_opacity=1.0, stroke_color=WHITE, stroke_width=2,
        )
        fleche_plateau = Arrow(
            [-2.2, 0.8, 0], [-2.2, -1.0, 0], color=RED, stroke_width=3, buff=0
        )
        label_plateau = Text("Plateau\n(sol rouge, drainé)", font_size=16, color=RED)
        label_plateau.next_to(fleche_plateau, UP, buff=0.15)

        fleche_bas_fond = Arrow(
            [2.5, -0.9, 0], [2.5, -1.55, 0], color=BLUE, stroke_width=3, buff=0
        )
        label_bas_fond = Text("Bas-fond\n(eau stagnante, sol gris)", font_size=16, color=BLUE)
        label_bas_fond.next_to(fleche_bas_fond, DOWN, buff=0.15)

        schema_topo = VGroup(relief, fleche_plateau, label_plateau, fleche_bas_fond, label_bas_fond)
        schema_topo.next_to(entete_topo, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Prenons un exemple : pourquoi le bas-fond de Gagnoa ne "
                "ressemble-t-il pas au plateau voisin ? Sur le plateau, la "
                "pluie s'infiltre et traverse tout le profil : le sol est "
                "drainé, aéré, oxydé, de couleur rouge. Dans le bas-fond, "
                "l'eau stagne, l'air ne circule plus, le fer est réduit et "
                "donne des teintes grises à bleuâtres, avec des taches de "
                "rouille autour des racines : c'est un sol hydromorphe, peu "
                "propice aux cultures sèches, mais excellent pour le riz."
            )
        ) as tracker:
            self.play(FadeIn(entete_topo))
            self.play(FadeIn(relief))
            self.play(FadeIn(fleche_plateau), FadeIn(label_plateau))
            self.play(FadeIn(fleche_bas_fond), FadeIn(label_bas_fond))
            self.wait(tracker.get_remaining_duration())

        conclusion_topo = Text(
            "À climat et roche identiques, le relief seul a fabriqué un autre sol.",
            font_size=20,
            color=WHITE,
        )
        conclusion_topo.next_to(schema_topo, DOWN, buff=0.3)
        self.play(FadeIn(conclusion_topo))
        self.wait(1.5)

        self.play(FadeOut(entete_topo), FadeOut(schema_topo), FadeOut(conclusion_topo))

        # --- Piège à éviter : le climat ne fait pas tout ----------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le climat ne fait pas tout. « Sous un même climat, "
                    "tous les sols sont identiques » est faux ! La roche "
                    "mère, le relief, la végétation, le temps et l'homme "
                    "modulent l'évolution. Il faut citer au moins deux "
                    "facteurs et les illustrer.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : le climat ne fait pas tout. Affirmer que sous "
                "un même climat, tous les sols sont identiques, est faux. "
                "La roche mère, le relief, la végétation, le temps et "
                "l'homme modulent aussi l'évolution du sol. Dans une "
                "réponse d'examen, il faut donc citer au moins deux "
                "facteurs et les illustrer par un exemple concret."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
