"""
scenes/SVT_ActivitesInternesGlobe_09.py — Chapitre 6 (1ereD, SVT), scène 09.

§ 6.4.4 La tectonique des plaques explique la répartition des volcans et
des séismes (subduction, dorsales, points chauds, cas de la Côte
d'Ivoire) + méthode pour rédiger une explication de géologie au bac +
L'ESSENTIEL DU CHAPITRE en clôture.
Source : 1ereD/SVT.pdf, pages 82-83.
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
    Star,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class RepartitionExpliqueeEtEssentielDuChapitre(NotionScene):
    def construct(self):
        titre = scene_title("6.4.4 — La tectonique des plaques tout explique")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : subduction et dorsales ----------------------------------
        intro = Text(
            _wrap(
                "Les volcans de la ceinture de feu et les grands séismes "
                "(Japon, Chili, Indonésie) se situent aux zones de "
                "subduction : la plaque qui plonge chauffe, les roches "
                "hydratées fondent partiellement, magma visqueux → "
                "éruptions explosives ; rupture des roches le long du plan "
                "de subduction → séismes de profondeur croissante.",
                width=56,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Reprenons chaque situation. Les volcans de la ceinture de "
                "feu et les grands séismes du Japon, du Chili ou de "
                "l'Indonésie se situent aux zones de subduction : la plaque "
                "qui plonge se réchauffe, ses roches hydratées fondent "
                "partiellement, ce qui donne un magma visqueux, source "
                "d'éruptions explosives ; la rupture des roches le long du "
                "plan de subduction provoque des séismes de profondeur "
                "croissante."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : dorsales et points chauds ------------
        suite = Text(
            _wrap(
                "Les volcans effusifs d'Islande et du rift est-africain se "
                "situent sur des dorsales. Les volcans de points chauds "
                "(Hawaï, ligne du Cameroun) sont alimentés par des "
                "remontées profondes localisées loin de toute limite.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        suite.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Les volcans effusifs de l'Islande et du rift est-africain "
                "se situent, eux, sur des dorsales : c'est là que deux "
                "plaques s'écartent et laissent remonter un magma pauvre en "
                "silice. Quant aux volcans de points chauds, comme Hawaï ou "
                "la ligne du Cameroun, ils sont alimentés par des remontées "
                "profondes, localisées loin de toute limite de plaque."
            )
        ) as tracker:
            self.play(FadeIn(suite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(suite))

        # --- Exemple traité : le cas de la Côte d'Ivoire ----------------------
        exemple = example_box(
            Text(
                _wrap(
                    "La Côte d'Ivoire se trouve au centre de la plaque "
                    "africaine, loin de toute limite : lithosphère ancienne, "
                    "épaisse, stable → pas de volcan actif ni grand séisme.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Revenons à l'énigme du début du chapitre : pourquoi la "
                "Côte d'Ivoire ne connaît-elle ni volcan actif ni grand "
                "séisme ? Elle se trouve au centre de la plaque africaine, "
                "loin de toute limite : sa lithosphère est ancienne, "
                "épaisse et stable. Sans écartement, sans subduction, sans "
                "collision, il n'y a ni magma qui remonte, ni faille qui se "
                "rompt brutalement."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        # Mini carte : étoile Côte d'Ivoire au centre, loin de toute limite
        etoile_ci = Star(color=YELLOW, fill_color=YELLOW, fill_opacity=1.0).scale(0.18)
        etiquette_ci = Text("Côte d'Ivoire\n(centre de plaque, stable)", font_size=16, color=YELLOW)
        mini_carte = VGroup(etoile_ci, etiquette_ci).arrange(DOWN, buff=0.15)
        mini_carte.next_to(exemple, DOWN, buff=0.4)

        self.play(FadeIn(mini_carte))
        self.wait(1.0)

        self.play(FadeOut(exemple), FadeOut(mini_carte))

        # --- À retenir : méthode pour rédiger une explication de géologie -----
        methode = method_box(
            Text(
                _wrap(
                    "Étape 1 — Constat : décrire précisément ce qu'on "
                    "observe. Étape 2 — Mécanisme : dire dans quelle "
                    "situation de plaque on se trouve et décrire le "
                    "processus. Étape 3 — Conséquence : relier le "
                    "mécanisme aux manifestations et conclure.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir, la méthode pour rédiger une explication de "
                "géologie au baccalauréat, en trois étapes. Étape un, le "
                "constat : décrire précisément ce que l'on observe, un "
                "volcan, un séisme, un relief. Étape deux, le mécanisme : "
                "préciser dans quelle situation de plaque on se trouve, "
                "dorsale, subduction, collision ou faille, et décrire le "
                "processus en jeu. Étape trois, la conséquence : relier ce "
                "mécanisme aux manifestations observées, et conclure."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- L'ESSENTIEL DU CHAPITRE (clôture) ---------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Volcanisme = remontée des magmas ; produits gaz / "
                    "laves / projections. Effusive (fluide) → coulées ; "
                    "explosive (visqueux) → cendres et nuées ardentes.",
                    "Séisme = libération brutale d'énergie à une faille ; "
                    "foyer et épicentre.",
                    "Ondes P (rapides, solides+liquides), S (solides), L "
                    "(surface, destructrices) ; d = (vP×vS)/(vP-vS) × Δt.",
                    "Magnitude (Richter) = énergie ; intensité (MSK) = "
                    "effets locaux.",
                    "Globe : croûte, manteau (solide, jusqu'à 2900 km), "
                    "noyau (externe liquide, interne solide) — Moho, "
                    "Gutenberg, Lehmann.",
                    "Zone d'ombre des ondes S au-delà de 105° = preuve du "
                    "noyau externe liquide.",
                    "Lithosphère rigide (~100 km) sur asthénosphère "
                    "plastique ; plaques mues par la convection "
                    "mantellique.",
                    "Volcans, séismes, montagnes se concentrent aux limites "
                    "de plaques ; le centre des plaques, comme la Côte "
                    "d'Ivoire, est stable.",
                ],
                font_size=17,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        # Garde-fou : si le contenu (8 points) dépasse la hauteur visible du
        # cadre malgré le petit corps de police, on réduit l'échelle globale
        # de la boîte pour qu'elle tienne entièrement à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. Le volcanisme est la "
                "remontée des magmas jusqu'à la surface, avec des produits "
                "gazeux, liquides et solides ; l'éruption effusive, à magma "
                "fluide, donne des coulées, l'éruption explosive, à magma "
                "visqueux, donne cendres et nuées ardentes. Un séisme est "
                "la libération brutale d'énergie à une faille, avec un "
                "foyer et un épicentre. Les ondes P, rapides, traversent "
                "solides et liquides ; les ondes S, plus lentes, ne "
                "traversent que les solides ; les ondes L, de surface, sont "
                "les plus destructrices ; la distance épicentrale se "
                "calcule par d égale vP fois vS, divisé par vP moins vS, "
                "fois delta t. La magnitude, sur l'échelle de Richter, "
                "mesure l'énergie ; l'intensité, sur l'échelle MSK, mesure "
                "les effets locaux. Le globe est fait de la croûte, du "
                "manteau solide jusqu'à deux mille neuf cents kilomètres, "
                "et du noyau, externe liquide et interne solide, séparés "
                "par les discontinuités de Moho, Gutenberg et Lehmann. La "
                "zone d'ombre des ondes S au-delà de cent cinq degrés "
                "prouve que le noyau externe est liquide. La lithosphère "
                "rigide, sur une centaine de kilomètres, repose sur "
                "l'asthénosphère plastique ; les plaques qui la composent "
                "sont mises en mouvement par la convection mantellique. "
                "Enfin, volcans, séismes et chaînes de montagnes se "
                "concentrent aux limites de plaques, tandis que le centre "
                "des plaques, comme la Côte d'Ivoire, reste stable."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
