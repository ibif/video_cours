"""
scenes/SVT_EvolutionSolsTropicaux_04.py — Chapitre 9 (1ereD, SVT), scène 04.

§ 9.3 La formation du sol : l'altération de la roche mère — définition de
l'altération, les 3 types (physique, chimique, biologique), équation de
l'hydrolyse de l'orthose en kaolinite, exemple du pays Baoulé (Bouaké),
méthode pour reconnaître le type d'altération, attention altération ≠
érosion. Source : 1ereD/SVT.pdf, pages 118-120.
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
    Line,
    MathTex,
    Polygon,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LaFormationDuSolAlteration(NotionScene):
    def construct(self):
        titre = scene_title("9.3 — La formation du sol : l'altération")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : définition de l'altération -----------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'altération est l'ensemble des processus qui "
                    "désagrègent et transforment la roche sur place (sans "
                    "transport). On distingue l'altération physique "
                    "(fragmentation sans changement de composition), "
                    "l'altération chimique (transformation des minéraux) "
                    "et l'altération biologique (action des êtres "
                    "vivants).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'altération est l'ensemble des processus qui désagrègent "
                "et transforment la roche sur place, sans aucun transport. "
                "On distingue trois types : l'altération physique, une "
                "fragmentation sans changement de composition ; "
                "l'altération chimique, qui transforme les minéraux ; et "
                "l'altération biologique, due à l'action des êtres "
                "vivants."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma de fissuration de roche -----
        entete_physique = Text("Altération physique", font_size=26, color=YELLOW, weight="BOLD")
        entete_physique.next_to(titre, DOWN, buff=0.45)

        bloc_roche = Polygon(
            [-1.4, -1.0, 0], [1.4, -1.0, 0], [1.4, 1.0, 0], [-1.4, 1.0, 0],
            fill_color="#8A7A63", fill_opacity=1.0, stroke_color=WHITE, stroke_width=2,
        )
        fissures = VGroup(
            Line([-0.5, 1.0, 0], [-0.2, -0.2, 0], color="#2B2B2B", stroke_width=3),
            Line([0.6, 1.0, 0], [0.1, -0.2, 0], color="#2B2B2B", stroke_width=3),
            Line([-0.2, -0.2, 0], [-1.4, -0.6, 0], color="#2B2B2B", stroke_width=3),
            Line([0.1, -0.2, 0], [1.4, -0.5, 0], color="#2B2B2B", stroke_width=3),
        )
        legende_physique = _bullets(
            [
                "Thermoclastie : dilatation le jour, contraction la nuit → fissures (fort dans le Nord).",
                "Action mécanique de l'eau : pluies, ruissellement, crues.",
                "Cryoclastie (le gel) : inexistante en Côte d'Ivoire.",
                "Décompression : la roche mise à nu se fissure en dalles.",
            ],
            font_size=19,
            width=48,
        )
        schema_physique = VGroup(bloc_roche, fissures)
        groupe_physique = VGroup(schema_physique, legende_physique).arrange(RIGHT, buff=0.7)
        groupe_physique.next_to(entete_physique, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'altération physique, ou mécanique, fragmente la roche "
                "sans modifier ses minéraux. Plusieurs agents : les "
                "variations de température, appelées thermoclastie, "
                "dilatent la roche le jour et la contractent la nuit, ce "
                "qui crée des fissures, un phénomène fort dans les savanes "
                "du Nord ivoirien ; l'action mécanique de l'eau, pluies, "
                "ruissellement, crues ; le gel, appelé cryoclastie, "
                "inexistant en Côte d'Ivoire ; et la décompression, quand "
                "une roche mise à nu se fissure en dalles. Cette "
                "fragmentation augmente la surface de contact entre l'eau "
                "et la roche, et prépare ainsi l'altération chimique."
            )
        ) as tracker:
            self.play(FadeIn(entete_physique))
            self.play(FadeIn(bloc_roche))
            self.play(FadeIn(fissures))
            self.play(FadeIn(legende_physique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_physique), FadeOut(groupe_physique))

        # --- Altération chimique + équation de l'hydrolyse --------------------
        entete_chimique = Text("Altération chimique", font_size=26, color=YELLOW, weight="BOLD")
        entete_chimique.next_to(titre, DOWN, buff=0.45)

        chimique_texte = _bullets(
            [
                "Dissolution : l'eau dissout sel gemme, gypse, calcaire+CO2.",
                "Oxydation : O2 transforme le fer ferreux Fe2+ en fer ferrique Fe3+ (rouille, rouge, jaune).",
                "Hydrolyse : eau acidulée par CO2 + minéraux silicatés — réaction reine sous climat tropical.",
            ],
            font_size=19,
            width=52,
        )
        chimique_texte.next_to(entete_chimique, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'altération chimique transforme les minéraux en "
                "minéraux nouveaux, par trois réactions. La dissolution : "
                "l'eau dissout le sel gemme, le gypse, ou le calcaire en "
                "présence de dioxyde de carbone. L'oxydation : le "
                "dioxygène transforme le fer ferreux, Fe deux plus, en fer "
                "ferrique, Fe trois plus, ce qui donne les couleurs "
                "rouille, rouges ou jaunes si caractéristiques des sols "
                "tropicaux. Et l'hydrolyse, où l'eau, souvent acidulée par "
                "le dioxyde de carbone, réagit avec les minéraux silicatés "
                "— c'est la réaction reine sous climat tropical chaud et "
                "humide."
            )
        ) as tracker:
            self.play(FadeIn(entete_chimique))
            self.play(FadeIn(chimique_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_chimique), FadeOut(chimique_texte))

        equation_titre = Text(
            "Exemple fondamental : hydrolyse de l'orthose", font_size=23, color=YELLOW, weight="BOLD"
        )
        equation_titre.next_to(titre, DOWN, buff=0.5)

        equation = MathTex(
            r"2\,KAlSi_3O_8 + 2H^+ + H_2O \;\rightarrow\; Al_2Si_2O_5(OH)_4 + 4\,SiO_2 + 2K^+",
            font_size=26,
            color=WHITE,
        )
        equation.next_to(equation_titre, DOWN, buff=0.4)

        legende_eq = Text(
            _wrap(
                "Orthose (feldspath du granite) + eau acidulée → kaolinite "
                "(argile) + silice + ions potassium solubles.",
                width=52,
            ),
            font_size=20,
            color=WHITE,
        )
        legende_eq.next_to(equation, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Prenons l'exemple fondamental de l'orthose, le feldspath "
                "potassique du granite. Son hydrolyse s'écrit : deux "
                "unités d'orthose, plus deux ions hydrogène, plus une "
                "molécule d'eau, donnent une unité de kaolinite, l'argile "
                "claire, plus quatre unités de silice, plus deux ions "
                "potassium solubles. Autrement dit : le feldspath du "
                "granite, attaqué par une eau acidulée, se transforme en "
                "argile kaolinite, en silice, et libère des ions potassium "
                "que les plantes ou l'eau emportent. La chaleur accélère "
                "cette réaction, et les pluies abondantes fournissent l'eau "
                "et entraînent les produits solubles."
            )
        ) as tracker:
            self.play(FadeIn(equation_titre))
            self.play(Write(equation))
            self.play(FadeIn(legende_eq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation_titre), FadeOut(equation), FadeOut(legende_eq))

        # --- Altération biologique --------------------------------------------
        biologique = definition_box(
            Text(
                _wrap(
                    "Altération biologique : les racines des grands arbres "
                    "(iroko, fromager) fendent les roches ; termites et "
                    "vers de terre brassent des tonnes de terre ; "
                    "microorganismes sécrètent des acides organiques ; la "
                    "respiration des racines et des microbes enrichit "
                    "l'air du sol en CO2, acidifie l'eau d'infiltration et "
                    "renforce l'hydrolyse.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        biologique.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'altération biologique enfin : les racines des grands "
                "arbres, comme l'iroko ou le fromager, fendent les roches ; "
                "les termites et les vers de terre brassent des tonnes de "
                "terre ; les microorganismes sécrètent des acides "
                "organiques ; et la respiration des racines et des microbes "
                "enrichit l'air du sol en dioxyde de carbone, ce qui "
                "acidifie l'eau d'infiltration et renforce l'hydrolyse."
            )
        ) as tracker:
            self.play(FadeIn(biologique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(biologique))

        # --- Exemple traité : pays Baoulé, région de Bouaké -------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Région de Bouaké, le granite affleure en grosses "
                    "boules. Étape 1 : les variations de température "
                    "fissurent le granite (altération physique). Étape 2 : "
                    "les pluies s'infiltrent, l'eau acidulée hydrolyse les "
                    "feldspaths en argile, le quartz résistant demeure en "
                    "sable (altération chimique). Étape 3 : racines, "
                    "termites, microorganismes mélangent et enrichissent "
                    "(altération biologique). Résultat : une arène "
                    "granitique, sol sableux facile à cultiver mais "
                    "fragile.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = exemple.get_top()[1] - _bas_visible
        if exemple.height > _hauteur_dispo:
            exemple.scale(_hauteur_dispo / exemple.height, about_point=exemple.get_top())

        with self.voiceover(
            text=(
                "Exemple traité, en pays Baoulé, région de Bouaké, où le "
                "granite affleure en grosses boules. Étape un : les "
                "variations de température fissurent le granite, c'est "
                "l'altération physique. Étape deux : les pluies "
                "s'infiltrent, l'eau acidulée hydrolyse les feldspaths en "
                "argile, tandis que le quartz, résistant, demeure en grains "
                "de sable, c'est l'altération chimique. Étape trois : les "
                "racines, les termites, les microorganismes mélangent et "
                "enrichissent le tout, c'est l'altération biologique. "
                "Résultat : une arène granitique, un sable grossier mêlé "
                "d'argile, surmontée d'un sol sableux, facile à cultiver "
                "mais fragile."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : méthode pour reconnaître le type d'altération ------
        methode = method_box(
            _bullets(
                [
                    "Roche cassée en morceaux, minéraux inchangés → altération physique.",
                    "Minéraux changés de nature (argiles, rouille, vides de dissolution) → altération chimique.",
                    "Galeries, racines, déjections, terriers → altération biologique.",
                    "Les trois agissent ensemble : identifier l'agent dominant.",
                ],
                font_size=20,
                width=50,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Méthode pour reconnaître le type d'altération à partir "
                "d'indices. Une roche cassée en morceaux, avec des minéraux "
                "inchangés, signale une altération physique. Des minéraux "
                "changés de nature, argiles nouvelles, couleurs de rouille, "
                "vides de dissolution, signalent une altération chimique. "
                "Des galeries, des racines, des déjections, des terriers "
                "signalent une altération biologique. En réalité, les trois "
                "agissent toujours ensemble : il s'agit d'identifier "
                "l'agent dominant."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : altération ≠ érosion ----------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Altération et érosion : deux mots, deux réalités. "
                    "L'altération transforme la roche sur place ; "
                    "l'érosion enlève et transporte les particules (eau, "
                    "vent, gravité). « La roche est érodée par "
                    "l'hydrolyse » est une erreur : l'hydrolyse altère, le "
                    "ruissellement érode.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, altération et érosion sont deux mots pour deux "
                "réalités différentes. L'altération transforme la roche "
                "sur place ; l'érosion enlève et transporte les particules, "
                "par l'eau, le vent ou la gravité. Dire que « la roche est "
                "érodée par l'hydrolyse » est donc une erreur : "
                "l'hydrolyse altère, le ruissellement érode."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
