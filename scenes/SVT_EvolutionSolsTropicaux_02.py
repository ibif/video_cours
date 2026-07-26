"""
scenes/SVT_EvolutionSolsTropicaux_02.py — Chapitre 9 (1ereD, SVT), scène 02.

§ 9.1 Le sol : une couche superficielle vivante — définition du sol,
remarque sol/roche, les 4 composantes avec proportions, exemple d'analyse
d'un échantillon de 400 cm³, attention aux deux confusions matière
organique/humus, et le sol comme bien précieux. Source : 1ereD/SVT.pdf,
page 116.
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
    PI,
    Sector,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box

MINERAUX_COLOR = "#C9A66B"
EAU_COLOR = "#3C8DBC"
AIR_COLOR = "#DCEFF7"
MO_COLOR = "#5B3A29"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LeSolCoucheSuperficielleVivante(NotionScene):
    def construct(self):
        titre = scene_title("9.1 — Le sol : une couche superficielle vivante")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition du sol --------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le sol est la couche superficielle, meuble et vivante "
                    "de l'écorce terrestre. Il résulte de la transformation "
                    "très lente de la roche sous-jacente (roche mère) sous "
                    "l'action combinée du climat, des êtres vivants, du "
                    "relief et du temps. « Meuble » = particules libres "
                    "(sable, poussières, miettes). « Vivant » = abrite "
                    "bactéries, champignons, vers de terre, termites, "
                    "fourmis.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le sol est la couche superficielle, meuble et vivante de "
                "l'écorce terrestre. Il résulte de la transformation très "
                "lente de la roche sous-jacente, appelée roche mère, sous "
                "l'action combinée du climat, des êtres vivants, du relief "
                "et du temps. Meuble signifie fait de particules libres, "
                "sable, poussières, miettes, et non d'un bloc continu. "
                "Vivant signifie qu'il abrite bactéries, champignons, vers "
                "de terre, termites et fourmis. En Côte d'Ivoire, les "
                "termites aèrent et brassent le sol en profondeur par leurs "
                "galeries."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        remarque = warning_box(
            Text(
                _wrap(
                    "Sol et roche : ne pas confondre. Une roche est un "
                    "matériau solide, cohérent, aux minéraux soudés. Le sol "
                    "est meuble, traversé par l'eau et l'air, habité par des "
                    "organismes, organisé en horizons. Le sable d'une plage "
                    "n'est pas un sol : ni structure, ni matière organique, "
                    "ni vie.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre sol et roche. Une roche est un "
                "matériau solide, cohérent, dont les minéraux sont soudés "
                "entre eux. Le sol, lui, est meuble, traversé par l'eau et "
                "l'air, habité par des organismes, et organisé en horizons. "
                "Le sable d'une plage n'est donc pas un sol : il n'a ni "
                "structure, ni matière organique, ni vie."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Animation du raisonnement : les 4 composantes (camembert) ------
        entete_compo = Text("Les composantes du sol", font_size=27, color=YELLOW, weight="BOLD")
        entete_compo.next_to(titre, DOWN, buff=0.45)

        # Diagramme circulaire simple : 4 secteurs proportionnels.
        proportions = [
            ("Minéraux", 0.45, MINERAUX_COLOR),
            ("Eau", 0.25, EAU_COLOR),
            ("Air", 0.25, AIR_COLOR),
            ("Mat. organique", 0.05, MO_COLOR),
        ]
        secteurs = VGroup()
        angle_courant = PI / 2
        for nom, part, couleur in proportions:
            angle = part * 2 * PI
            secteur = Sector(
                start_angle=angle_courant,
                angle=-angle,
                radius=1.6,
                fill_color=couleur,
                fill_opacity=1.0,
                stroke_color=WHITE,
                stroke_width=1.5,
            )
            secteurs.add(secteur)
            angle_courant -= angle

        legende = VGroup(
            *[
                Text(f"■ {nom} : ~{int(part * 100)}%", font_size=20, color=couleur)
                for nom, part, couleur in proportions
            ]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        schema = VGroup(secteurs, legende).arrange(RIGHT, buff=0.9)
        schema.next_to(entete_compo, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le sol se compose de quatre éléments. Les éléments "
                "minéraux : des particules issues de l'altération des "
                "roches, sables, limons, argiles, plus des éléments "
                "nutritifs dissous comme le calcium, le potassium, le "
                "magnésium, le phosphore, l'azote ; environ quarante-cinq "
                "pour cent du volume. La matière organique : les restes "
                "d'êtres vivants en décomposition, dont la partie stable et "
                "sombre forme l'humus ; environ cinq pour cent du volume. "
                "L'eau occupe une partie des vides et forme la solution du "
                "sol : environ vingt-cinq pour cent. L'air occupe les "
                "autres vides et fournit l'oxygène nécessaire à la "
                "respiration : environ vingt-cinq pour cent également. Ces "
                "proportions varient selon les sols et les saisons."
            )
        ) as tracker:
            self.play(FadeIn(entete_compo))
            self.play(FadeIn(secteurs))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_compo), FadeOut(schema))

        # --- Exemple traité : analyse d'un échantillon -----------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Cylindre de terre de Soubré, volume total 400 cm³ : "
                    "minéraux 180 cm³, eau 100 cm³, air 96 cm³, matière "
                    "organique 24 cm³. Étape 1 : vérifier le total : "
                    "180+100+96+24=400 ✓. Étape 2 : proportions : minéraux "
                    "180/400=0,45 (45%) ; eau 100/400=0,25 (25%) ; air "
                    "96/400=0,24 (24%) ; matière organique 24/400=0,06 (6%). "
                    "Étape 3 : composition proche de la moyenne, teneur en "
                    "matière organique (6%) légèrement supérieure — "
                    "parcelle protégée par un couvert végétal.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        # Garde-fou : boîte dense (5 lignes), on vérifie qu'elle tient.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = exemple.get_top()[1] - _bas_visible
        if exemple.height > _hauteur_dispo:
            exemple.scale(_hauteur_dispo / exemple.height, about_point=exemple.get_top())

        with self.voiceover(
            text=(
                "Exemple traité : on prélève un cylindre de terre à Soubré, "
                "de volume total quatre cents centimètres cubes. Il "
                "contient cent quatre-vingts centimètres cubes de "
                "minéraux, cent centimètres cubes d'eau, quatre-vingt-seize "
                "centimètres cubes d'air, et vingt-quatre centimètres cubes "
                "de matière organique. Étape un : on vérifie le total : cent "
                "quatre-vingts plus cent plus quatre-vingt-seize plus "
                "vingt-quatre égale bien quatre cents. Étape deux, on "
                "calcule les proportions : les minéraux représentent "
                "quarante-cinq pour cent, l'eau vingt-cinq pour cent, l'air "
                "vingt-quatre pour cent, et la matière organique six pour "
                "cent. Étape trois, conclusion : cette composition est "
                "proche de la moyenne, avec une teneur en matière organique "
                "légèrement supérieure, signe d'une parcelle protégée par "
                "un couvert végétal."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : un bien précieux ------------------------------------
        precieux = Text(
            _wrap(
                "Le sol est un écosystème vivant : microorganismes "
                "décomposent la matière organique, vers de terre et "
                "termites brassent et aèrent, racines puisent eau et sels "
                "minéraux. Pour la Côte d'Ivoire (cacao, café, hévéa, "
                "palmier, cultures vivrières), le sol est un capital "
                "irremplaçable : il faut une centaine à un millier d'années "
                "pour qu'un seul centimètre de sol se forme naturellement.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        precieux.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le sol est aussi un milieu vivant et un bien précieux : "
                "c'est un véritable écosystème, où les microorganismes "
                "décomposent la matière organique, où les vers de terre et "
                "les termites brassent et aèrent la terre, où les racines "
                "puisent l'eau et les sels minéraux. Pour la Côte d'Ivoire, "
                "avec le cacao, le café, l'hévéa, le palmier et les "
                "cultures vivrières, le sol est un capital irremplaçable : "
                "il faut une centaine à un millier d'années pour qu'un seul "
                "centimètre de sol se forme naturellement."
            )
        ) as tracker:
            self.play(FadeIn(precieux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(precieux))

        # --- Piège à éviter : deux confusions fréquentes ---------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Deux confusions fréquentes : la matière organique est "
                    "l'ensemble des restes d'êtres vivants ; l'humus n'en "
                    "est que la fraction déjà transformée, stable et "
                    "sombre. Les « éléments nutritifs » (azote, phosphore, "
                    "potassium...) ne sont pas une composante à part : ils "
                    "appartiennent aux éléments minéraux ou à la matière "
                    "organique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à deux confusions fréquentes. D'abord, la "
                "matière organique est l'ensemble des restes d'êtres "
                "vivants ; l'humus n'en est que la fraction déjà "
                "transformée, stable et sombre, ce n'est pas un synonyme. "
                "Ensuite, les éléments nutritifs, comme l'azote, le "
                "phosphore ou le potassium, ne forment pas une composante à "
                "part du sol : ils appartiennent soit aux éléments "
                "minéraux, soit à la matière organique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
