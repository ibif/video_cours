"""
scenes/Chimie_Alcanes_13.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 13.

§ 7.5 Les dérivés halogénés : usages et limites (monochlorométhane,
dichlorométhane, trichlorométhane, tétrachlorométhane) + remarque
environnementale (CFC/fréons, protocole de Montréal) + § 8.1 le pouvoir
calorifique (définition, tableau méthane/propane/butane/essence) +
§ 8.2 usages des alcanes. Source : 1ereC/Chimie.pdf, pages 23-24.
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
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


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


class DerivesHalogenesPouvoirCalorifique(NotionScene):
    def construct(self):
        titre = scene_title("8. Dérivés halogénés, pouvoir calorifique, usages")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : les 4 dérivés chlorés du méthane et leurs usages ----------
        entete_usages = Text("Usages des dérivés chlorés du méthane", font_size=22, color=YELLOW, weight="BOLD")
        entete_usages.next_to(titre, DOWN, buff=0.4)

        usages = _bullets(
            [
                "CH₃Cl (monochlorométhane) : gaz très liquéfiable, agent "
                "de réfrigération.",
                "CH₂Cl₂ (dichlorométhane) : solvant (décaféination, "
                "décapage).",
                "CHCl₃ (trichlorométhane, chloroforme) : ancien "
                "anesthésique, solvant et intermédiaire de synthèse.",
                "CCl₄ (tétrachlorométhane) : excellent solvant, mais "
                "toxique et destructeur de la couche d'ozone : usage "
                "très réglementé.",
            ],
            font_size=20,
            width=56,
        )
        usages.next_to(entete_usages, DOWN, buff=0.35)
        _fit(usages, entete_usages.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Les quatre dérivés chlorés du méthane ont chacun leurs "
                "usages. Le monochlorométhane, gaz très liquéfiable, sert "
                "d'agent de réfrigération. Le dichlorométhane est utilisé "
                "comme solvant, par exemple pour la décaféination ou le "
                "décapage. Le trichlorométhane, ou chloroforme, autrefois "
                "utilisé comme anesthésique en médecine, sert aujourd'hui "
                "de solvant et d'intermédiaire de synthèse. Le "
                "tétrachlorométhane est un excellent solvant, mais il est "
                "toxique et destructeur de la couche d'ozone : son usage "
                "est très réglementé."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_usages))
            self.play(FadeIn(usages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_usages), FadeOut(usages))

        # --- Raisonnement : remarque environnementale (CFC, protocole Montréal) -
        remarque_env = warning_box(
            Text(
                _wrap(
                    "Certains dérivés halogénés contenant chlore et "
                    "fluor (les fréons, ou CFC) sont des gaz à effet de "
                    "serre qui détruisent la couche d'ozone. Leur "
                    "production est interdite par le protocole de "
                    "Montréal.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        remarque_env.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Remarque environnementale importante : certains dérivés "
                "halogénés contenant à la fois du chlore et du fluor, "
                "appelés fréons ou C-F-C, sont des gaz à effet de serre "
                "qui détruisent la couche d'ozone. Leur production est "
                "aujourd'hui interdite par le protocole de Montréal."
            )
        ) as tracker:
            self.play(FadeIn(remarque_env))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_env))

        # --- Exemple traité : le pouvoir calorifique -----------------------------
        definition_pc = definition_box(
            Text(
                _wrap(
                    "Le pouvoir calorifique (massique) d'un combustible "
                    "est l'énergie thermique dégagée par la combustion "
                    "complète de l'unité de masse de ce combustible "
                    "(en J·kg⁻¹, souvent kJ·kg⁻¹ ou MJ·kg⁻¹).",
                    width=48,
                ),
                font_size=22,
            ),
        )
        definition_pc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le pouvoir calorifique massique d'un combustible est "
                "l'énergie thermique dégagée par la combustion complète "
                "de l'unité de masse de ce combustible. Il s'exprime en "
                "joules par kilogramme, le plus souvent en kilojoules ou "
                "en mégajoules par kilogramme."
            )
        ) as tracker:
            self.play(FadeIn(definition_pc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_pc))

        entete_tab_pc = Text("Pouvoir calorifique de quelques combustibles", font_size=20, color=YELLOW, weight="BOLD")
        entete_tab_pc.next_to(titre, DOWN, buff=0.35)

        rows = [["méthane", "propane", "butane", "essence"], ["≈50", "≈46", "≈46", "≈44"]]
        table = Table(
            rows,
            row_labels=[Text("combustible", font_size=15), Text("PC (MJ/kg)", font_size=15)],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 18},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.3,
            h_buff=0.4,
        )
        table.get_entries().set_color(WHITE)
        table.get_row_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(entete_tab_pc, DOWN, buff=0.35)
        _fit(table, entete_tab_pc.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Voici le pouvoir calorifique de quelques combustibles "
                "usuels : environ cinquante mégajoules par kilogramme "
                "pour le méthane, quarante-six pour le propane et le "
                "butane, quarante-quatre pour l'essence. Les alcanes "
                "dégagent beaucoup de chaleur en brûlant : ce sont "
                "d'excellents combustibles."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab_pc))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab_pc), FadeOut(table))

        # --- À retenir : les usages des alcanes -----------------------------------
        entete_usages2 = Text("Les grands usages des alcanes", font_size=22, color=YELLOW, weight="BOLD")
        entete_usages2.next_to(titre, DOWN, buff=0.4)

        usages2 = _bullets(
            [
                "Combustibles : gaz naturel, butane et propane "
                "domestiques, essence, kérosène, gas-oil, pétrole lampant.",
                "Solvants : hexane, heptane (extraction d'huiles "
                "végétales, huile de palme).",
                "Matières premières : dérivés halogénés, plastiques "
                "(vapocraquage), engrais azotés.",
                "Paraffines et cires : bougies, pommades, emballages.",
            ],
            font_size=20,
            width=56,
        )
        usages2.next_to(entete_usages2, DOWN, buff=0.35)
        _fit(usages2, entete_usages2.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Résumons les grands usages des alcanes. Comme "
                "combustibles : le gaz naturel pour l'électricité, le "
                "butane et le propane domestiques, l'essence, le "
                "kérosène pour l'aviation, le gas-oil, obtenus par "
                "raffinage à la SIR à Abidjan, et le pétrole lampant pour "
                "l'éclairage. Comme solvants : l'hexane et l'heptane, "
                "pour l'extraction des huiles végétales, comme l'huile de "
                "palme. Comme matières premières : la fabrication des "
                "dérivés halogénés, des plastiques par vapocraquage, et "
                "des engrais azotés. Et enfin, les paraffines et les "
                "cires, pour les bougies, les pommades et les emballages."
            )
        ) as tracker:
            self.play(FadeIn(entete_usages2))
            self.play(FadeIn(usages2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_usages2), FadeOut(usages2))

        # --- Piège à éviter : usage domestique ≠ absence de danger --------------
        piege = warning_box(
            Text(
                _wrap(
                    "Un usage domestique courant (réfrigération, "
                    "solvants) ne signifie pas « sans danger » : le "
                    "tétrachlorométhane est toxique et les CFC détruisent "
                    "la couche d'ozone. Toujours vérifier la "
                    "réglementation avant d'utiliser un dérivé halogéné.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : un usage domestique courant ne signifie pas "
                "sans danger. Le tétrachlorométhane est toxique, et les "
                "C-F-C détruisent la couche d'ozone. Il faut toujours "
                "vérifier la réglementation avant d'utiliser un dérivé "
                "halogéné."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
