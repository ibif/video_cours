"""
scenes/Chimie_Alcanes_04.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 04.

§ 3.2 Les groupes alkyles (définition, exemples méthyle / éthyle /
propyle / isopropyle) + § 3.3 règles de nomenclature UICPA pour les
alcanes ramifiés (les 5 règles). Source : 1ereC/Chimie.pdf, pages 17-18.
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
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class GroupesAlkylesEtNomenclatureUICPA(NotionScene):
    def construct(self):
        titre = scene_title("3. Groupes alkyles et nomenclature UICPA")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition du groupe alkyle -------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un groupe alkyle est un groupe d'atomes qui dérive "
                    "d'un alcane par perte d'un atome d'hydrogène. On le "
                    "nomme en remplaçant la terminaison « ane » de "
                    "l'alcane par la terminaison « yle ».",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour nommer les alcanes ramifiés, il nous faut d'abord "
                "connaître les groupes alkyles. Un groupe alkyle est un "
                "groupe d'atomes qui dérive d'un alcane par perte d'un "
                "atome d'hydrogène. On le nomme en remplaçant la "
                "terminaison ane de l'alcane par la terminaison yle."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les 4 groupes alkyles usuels ------------------------
        entete_alk = Text("Les groupes alkyles à connaître", font_size=24, color=YELLOW, weight="BOLD")
        entete_alk.next_to(titre, DOWN, buff=0.4)

        alkyles = VGroup(
            MathTex(r"\text{méthyle : } CH_3-", font_size=27, color=WHITE),
            MathTex(r"\text{éthyle : } CH_3-CH_2- \; (\text{ou } C_2H_5-)", font_size=27, color=WHITE),
            MathTex(r"\text{propyle : } CH_3-CH_2-CH_2-", font_size=27, color=WHITE),
            MathTex(r"\text{isopropyle : } CH_3-CH(CH_3)-", font_size=27, color=WHITE),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        alkyles.next_to(entete_alk, DOWN, buff=0.45)
        _fit(alkyles, entete_alk.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici les quatre groupes alkyles les plus courants. Le "
                "groupe méthyle, C-H-3, dérive du méthane. Le groupe "
                "éthyle, C-H-3, C-H-2, aussi noté C-2, H-5, dérive de "
                "l'éthane. Le groupe propyle, une chaîne de trois "
                "carbones, dérive du propane. Et le groupe isopropyle, "
                "où le point d'attache est sur le carbone central, dérive "
                "lui aussi du propane, mais autrement."
            )
        ) as tracker:
            self.play(FadeIn(entete_alk))
            self.play(Write(alkyles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_alk), FadeOut(alkyles))

        # --- Exemple traité : les 5 règles de nomenclature UICPA ----------------
        entete_regles = Text("Les 5 règles UICPA pour nommer un alcane ramifié", font_size=21, color=YELLOW, weight="BOLD")
        entete_regles.next_to(titre, DOWN, buff=0.35)

        regles = _bullets(
            [
                "1. Rechercher la chaîne la plus longue (chaîne "
                "principale) : son nombre de carbones donne le nom de "
                "l'alcane.",
                "2. Numéroter la chaîne pour donner aux substituants les "
                "indices de position les plus petits possibles.",
                "3. Citer les substituants par ordre alphabétique, chacun "
                "précédé de son indice suivi d'un tiret, puis le nom de "
                "la chaîne principale.",
                "4. Si des substituants sont identiques, les regrouper "
                "avec di, tri, tétra… et répéter l'indice de position à "
                "chaque fois.",
                "5. Virgules entre les chiffres, tirets entre chiffres et "
                "lettres.",
            ],
            font_size=19,
            width=58,
        )
        regles.next_to(entete_regles, DOWN, buff=0.35)
        _fit(regles, entete_regles.get_bottom()[1] - 0.35)

        groupe_regles = VGroup(entete_regles, regles)

        with self.voiceover(
            text=(
                "Voici les cinq règles de nomenclature de l'UICPA pour un "
                "alcane ramifié. Un : on recherche la chaîne la plus "
                "longue, appelée chaîne principale, dont le nombre "
                "d'atomes de carbone détermine le nom de l'alcane. Deux : "
                "on numérote cette chaîne de sorte que les indices de "
                "position des groupes alkyles soient les plus petits "
                "possibles. Trois : le nom de l'alcane est formé des noms "
                "des ramifications, chacune précédée de son indice suivi "
                "d'un tiret, citées par ordre alphabétique, puis du nom "
                "de la chaîne principale. Quatre : si plusieurs "
                "substituants sont identiques, on les regroupe à l'aide "
                "des préfixes di, tri, tétra, et on répète l'indice de "
                "position autant de fois que nécessaire. Cinq : les "
                "chiffres sont séparés entre eux par des virgules, et les "
                "chiffres des lettres par des tirets."
            )
        ) as tracker:
            self.play(FadeIn(entete_regles))
            self.play(FadeIn(regles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_regles))

        # --- À retenir : la propriété condensée ---------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Nom = [indice-substituant]... (ordre alphabétique) "
                    "+ nom de la chaîne principale la plus longue, "
                    "numérotée pour donner les plus petits indices.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En résumé, le nom d'un alcane ramifié s'écrit toujours "
                "ainsi : indice et nom de chaque substituant, cités par "
                "ordre alphabétique, suivis du nom de la chaîne "
                "principale, celle-ci étant numérotée pour donner les "
                "plus petits indices possibles aux substituants."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : virgules et tirets, ordre alphabétique -----------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre virgule et tiret : virgule ENTRE "
                    "deux chiffres (2,2-diméthyl...), tiret entre un "
                    "chiffre et une lettre (4-éthyl...). Les préfixes di, "
                    "tri, tétra ne comptent PAS pour l'ordre alphabétique "
                    "(triméthyl se classe à « m »).",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux pièges classiques à éviter. D'abord, ne confondez "
                "pas virgule et tiret : une virgule sépare deux chiffres, "
                "comme dans deux-virgule-deux-diméthyl ; un tiret sépare "
                "un chiffre d'une lettre, comme dans quatre-tiret-éthyl. "
                "Ensuite, les préfixes di, tri, tétra ne comptent pas "
                "pour l'ordre alphabétique : triméthyl se classe à la "
                "lettre m, comme méthyl, et non à la lettre t."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
