"""
scenes/SVT_EvolutionSolsTropicaux_10.py — Chapitre 9 (1ereD, SVT), scène 10.

L'ESSENTIEL DU CHAPITRE — synthèse finale du chapitre « L'évolution des
sols tropicaux ». Source : 1ereD/SVT.pdf, page 130.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=18, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class EssentielEvolutionSolsTropicaux(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 9 — L'essentiel à retenir")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : on relit l'histoire de Konan et Ibrahim -----------------
        rappel = Text(
            _wrap(
                "Revenons à Konan et Ibrahim : leur sol a changé parce "
                "que le climat tropical, la roche mère, le relief, la "
                "végétation, le temps et leurs propres pratiques ont "
                "façonné, puis parfois dégradé, la terre de leurs champs. "
                "Résumons ce que nous avons appris.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        rappel.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Revenons à Konan et à Ibrahim : leur sol a changé parce "
                "que le climat tropical, la roche mère, le relief, la "
                "végétation, le temps, et leurs propres pratiques ont "
                "façonné, puis parfois dégradé, la terre de leurs champs. "
                "Résumons maintenant tout ce que nous avons appris dans ce "
                "chapitre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel))

        # --- Animation du raisonnement + à retenir : L'ESSENTIEL DU CHAPITRE --
        essentiel = essentiel_box(
            _bullets(
                [
                    "Le sol est la couche superficielle, meuble et vivante de l'écorce terrestre, issue de l'altération de la roche mère : ~45% minéraux, 25% eau, 25% air, 5% matière organique.",
                    "Le profil d'un sol évolué : horizons O (litière), A (humifère), parfois E, B (accumulation), C (roche altérée), R (roche saine).",
                    "L'altération transforme la roche sur place : physique (fragmentation), chimique (hydrolyse des silicates → argile), biologique (racines, termites).",
                    "Six facteurs d'évolution : climat, roche mère, relief, végétation, temps, activités humaines — le climat chaud et humide domine sous les tropiques.",
                    "Le lessivage entraîne les bases et la silice ; la ferralitisation concentre fer et aluminium (sols rouges, kaolinite) ; exposé, l'horizon B durcit en cuirasse latéritique.",
                    "L'hydromorphie (eau stagnante) donne des sols gris de bas-fond, propices au riz.",
                    "Types en Côte d'Ivoire : ferralitiques (Sud), ferrugineux tropicaux (Centre-Nord), hydromorphes (bas-fonds), vertisols (plaines du Nord), peu évolués (versants).",
                    "L'érosion hydrique est la 1ère cause de dégradation ; on la combat en couvrant le sol, en ralentissant l'eau et en restituant la matière.",
                ],
                font_size=16,
                width=58,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : 8 points denses, on vérifie que la boîte tient à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. Le sol est la couche "
                "superficielle, meuble et vivante de l'écorce terrestre, "
                "issue de la transformation de la roche mère : environ "
                "quarante-cinq pour cent d'éléments minéraux, vingt-cinq "
                "pour cent d'eau, vingt-cinq pour cent d'air, cinq pour "
                "cent de matière organique. Le profil d'un sol évolué "
                "comprend, de haut en bas, les horizons O, la litière, A, "
                "humifère et lessivé, parfois E, B, zone d'accumulation, C, "
                "la roche altérée, et R, la roche mère saine. Le sol naît "
                "de l'altération de la roche : physique, par "
                "fragmentation ; chimique, par dissolution, oxydation, et "
                "surtout hydrolyse des silicates, qui donne l'argile ; et "
                "biologique, par l'action des racines, des termites et des "
                "microorganismes. Six facteurs font évoluer les sols : "
                "climat, roche mère, relief, végétation, temps, activités "
                "humaines — et sous les tropiques, c'est le climat chaud et "
                "humide qui domine. Le lessivage entraîne vers le bas les "
                "bases et la silice ; la ferralitisation concentre les "
                "oxydes de fer et d'aluminium, donnant des sols rouges, "
                "acides, riches en kaolinite ; exposé en surface, l'horizon "
                "B durcit en une cuirasse latéritique. L'hydromorphie, due "
                "à une eau stagnante, donne des sols gris de bas-fond, "
                "propices au riz. Les principaux types de sols de Côte "
                "d'Ivoire sont : les sols ferralitiques du Sud forestier, "
                "les sols ferrugineux tropicaux des savanes du Centre-Nord, "
                "les sols hydromorphes des bas-fonds, les vertisols des "
                "plaines du Nord, et les sols peu évolués des versants. "
                "Enfin, l'érosion hydrique est la première cause de "
                "dégradation ; on la combat en couvrant le sol, en "
                "ralentissant l'eau grâce aux courbes de niveau, aux bandes "
                "enherbées et aux terrasses, et en restituant la matière "
                "grâce au compost, au fumier, aux légumineuses et au "
                "chaulage."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Piège à éviter / conclusion : phrase de clôture -------------------
        cloture = Text(
            _wrap(
                "Un sol se forme en des siècles et se détruit en quelques "
                "saisons : le conserver, c'est nourrir les générations "
                "futures.",
                width=52,
            ),
            font_size=28,
            color=YELLOW,
            weight="BOLD",
        )
        cloture.next_to(titre, DOWN, buff=1.2)

        with self.voiceover(
            text=(
                "Retenons cette phrase, qui résume tout le chapitre : un "
                "sol se forme en des siècles, et se détruit en quelques "
                "saisons seulement. Le conserver, c'est nourrir les "
                "générations futures."
            )
        ) as tracker:
            self.play(Write(cloture))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(cloture))
