"""
scenes/SVT_EvolutionSolsTropicaux_08.py — Chapitre 9 (1ereD, SVT), scène 08.

§ 9.6 Les principaux types de sols tropicaux — les 5 types, tableau
régions/cultures de Côte d'Ivoire, exemple pour associer sol, région et
culture. Source : 1ereD/SVT.pdf, pages 124-125.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LesTypesDeSolsTropicaux(NotionScene):
    def construct(self):
        titre = scene_title("9.6 — Les principaux types de sols tropicaux")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : les 5 types de sols --------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Sols ferralitiques : très évolués, profonds, "
                    "rouges/jaunes, acides, riches en kaolinite. Sols "
                    "ferrugineux tropicaux : évolués mais moins lessivés, "
                    "brun-rouge, souvent cuirassés. Sols hydromorphes : "
                    "engorgés, gris à bleuâtres. Vertisols : très "
                    "argileux, noirs à gris, gonflent puis se fendent. "
                    "Sols peu évolués : jeunes, minces, proches de leur "
                    "roche mère.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = definition.get_top()[1] - _bas_visible
        if definition.height > _hauteur_dispo:
            definition.scale(_hauteur_dispo / definition.height, about_point=definition.get_top())

        with self.voiceover(
            text=(
                "La Côte d'Ivoire présente cinq grands types de sols "
                "tropicaux. Les sols ferralitiques : très évolués, "
                "profonds, rouges ou jaunes, acides, fortement lessivés, "
                "riches en kaolinite et en oxydes de fer et d'aluminium ; "
                "ils dominent le Sud forestier, fertiles sous forêt, mais "
                "se dégradent vite une fois défrichés. Les sols "
                "ferrugineux tropicaux : évolués mais moins lessivés, "
                "brun-rouge à rougeâtres, fréquemment cuirassés, dans les "
                "savanes du Centre et du Nord. Les sols hydromorphes : "
                "engorgés, gris à bleuâtres, avec des taches de rouille, "
                "dans les bas-fonds et les vallées. Les vertisols : très "
                "argileux, noirs à gris, ils gonflent à l'humidité et se "
                "fendent en saison sèche, dans les plaines du Nord. Et les "
                "sols peu évolués : jeunes, minces, ressemblant encore à "
                "leur roche mère, sur les versants, les berges, les zones "
                "d'érosion ou de dépôt récentes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : tableau régions / cultures ----------
        entete_tableau = Text("Sols, régions et cultures de Côte d'Ivoire", font_size=22, color=YELLOW, weight="BOLD")
        entete_tableau.next_to(titre, DOWN, buff=0.4)

        entetes = VGroup(
            Text("Type de sol", font_size=18, color=YELLOW, weight="BOLD"),
            Text("Région", font_size=18, color=YELLOW, weight="BOLD"),
            Text("Cultures", font_size=18, color=YELLOW, weight="BOLD"),
        )

        lignes_donnees = [
            ("Ferralitique", "Soubré, San-Pédro, Aboisso", "Cacao, café, hévéa, palmier"),
            ("Ferrugineux tropical", "Bouaké, Korhogo, Ferké", "Coton, maïs, igname, anacarde"),
            ("Hydromorphe", "Bas-fonds de tout le pays", "Riz, maraîchage"),
            ("Vertisol", "Plaines du Nord", "Coton, céréales"),
            ("Peu évolué", "Versants, berges", "Friche, cultures difficiles"),
        ]

        col1 = VGroup(entetes[0], *[Text(l[0], font_size=17, color=WHITE) for l in lignes_donnees])
        col2 = VGroup(entetes[1], *[Text(l[1], font_size=17, color=WHITE) for l in lignes_donnees])
        col3 = VGroup(entetes[2], *[Text(l[2], font_size=17, color=WHITE) for l in lignes_donnees])

        col1.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        col2.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        col3.arrange(DOWN, aligned_edge=LEFT, buff=0.28)

        tableau = VGroup(col1, col2, col3).arrange(RIGHT, buff=0.6, aligned_edge=UP)
        tableau.next_to(entete_tableau, DOWN, buff=0.35)

        _hauteur_dispo2 = tableau.get_top()[1] - _bas_visible
        groupe_tab = VGroup(entete_tableau, tableau)
        if groupe_tab.height > _hauteur_dispo2 + 0.6:
            groupe_tab.scale(0.85, about_point=entete_tableau.get_top())

        with self.voiceover(
            text=(
                "Résumons dans un tableau. Le sol ferralitique se trouve "
                "autour de Soubré, San-Pédro, Aboisso, propice au cacao, au "
                "café, à l'hévéa et au palmier. Le sol ferrugineux "
                "tropical se trouve autour de Bouaké, Korhogo, "
                "Ferkéssédougou, propice au coton, au maïs, à l'igname et à "
                "l'anacarde. Le sol hydromorphe se trouve dans les "
                "bas-fonds de tout le pays, propice au riz et au "
                "maraîchage. Le vertisol se trouve dans les plaines du "
                "Nord, propice au coton et aux céréales. Et le sol peu "
                "évolué se trouve sur les versants et les berges, avec des "
                "cultures de pente difficiles."
            )
        ) as tracker:
            self.play(FadeIn(entete_tableau))
            self.play(FadeIn(col1))
            self.play(FadeIn(col2))
            self.play(FadeIn(col3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tableau), FadeOut(tableau))

        # --- Exemple traité : associer sol, région et culture -----------------
        exemple = example_box(
            Text(
                _wrap(
                    "Trois parcelles : 1. « sol rouge profond, sous "
                    "ancienne forêt, région de Soubré ». 2. « sol gris, eau "
                    "à 30 cm, bas-fond près de Gagnoa ». 3. « sol brun-rouge "
                    "avec dalle ferrugineuse affleurante, savane de "
                    "Korhogo ». Résolution : 1=ferralitique (cacao avec "
                    "ombrage) ; 2=hydromorphe (riz) ; 3=ferrugineux "
                    "tropical cuirassé (coton/anacarde hors zones "
                    "cuirassées).",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        _hauteur_dispo3 = exemple.get_top()[1] - _bas_visible
        if exemple.height > _hauteur_dispo3:
            exemple.scale(_hauteur_dispo3 / exemple.height, about_point=exemple.get_top())

        with self.voiceover(
            text=(
                "Exemple traité : associer sol, région et culture pour "
                "trois parcelles décrites. Parcelle un : sol rouge "
                "profond, sous une ancienne forêt, région de Soubré. "
                "Parcelle deux : sol gris, eau à trente centimètres de "
                "profondeur, bas-fond près de Gagnoa. Parcelle trois : sol "
                "brun-rouge avec une dalle ferrugineuse affleurante, "
                "savane de Korhogo. Résolution : la parcelle un est un sol "
                "ferralitique, adapté au cacao cultivé avec ombrage et "
                "couverture du sol. La parcelle deux est un sol "
                "hydromorphe, où le riz est parfaitement adapté. La "
                "parcelle trois est un sol ferrugineux tropical cuirassé, "
                "où l'on peut cultiver le coton ou l'anacarde, en dehors "
                "des zones cuirassées. La démarche à suivre est toujours la "
                "même : description, type, usage."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------
        retenir = _bullets(
            [
                "Ferralitique = rouge, acide, Sud forestier : cacao, café, hévéa.",
                "Ferrugineux tropical = brun-rouge, souvent cuirassé, Centre-Nord : coton, igname.",
                "Hydromorphe = gris engorgé, bas-fonds : riz. Vertisol = noir fendillé, plaines du Nord.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : le sol ferralitique, rouge et acide, domine le "
                "Sud forestier et porte cacao, café et hévéa. Le sol "
                "ferrugineux tropical, brun-rouge, souvent cuirassé, "
                "domine le Centre et le Nord, avec coton et igname. Le sol "
                "hydromorphe, gris et engorgé, occupe les bas-fonds et "
                "porte le riz. Le vertisol, noir et fendillé en saison "
                "sèche, occupe les plaines du Nord."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(entete_retenir), FadeOut(retenir))
