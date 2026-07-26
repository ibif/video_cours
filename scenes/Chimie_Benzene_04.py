"""
scenes/Chimie_Benzene_04.py — Chapitre 4 (1ereC, Chimie), scène 04.

§ Délocalisation des électrons π — caractère aromatique : carbone
trigonal, liaisons σ du cycle, électron π non apparié perpendiculaire au
plan, recouvrement latéral formant un nuage électronique délocalisé
au-dessus et en-dessous du cycle (schéma vue de profil). definition_box
« caractère aromatique ». Explication des 3 faits expérimentaux du § 2.
Source : 1ereC/Chimie.pdf, chapitre 4, pages 37-38.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    ORIGIN,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Circle,
    Dot,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _vue_profil(center, width=6.4, color=WHITE, cloud_color=YELLOW):
    """Schéma « vue de profil » du cycle benzénique : plan du cycle (trait
    horizontal), orbitales p perpendiculaires au plan à chaque carbone
    (petits traits verticaux), et nuage π délocalisé au-dessus/en-dessous
    (deux cercles aplatis)."""
    plan = Line(LEFT * width / 2, RIGHT * width / 2, color=color, stroke_width=3)
    plan.move_to(center)

    n = 6
    carbones = VGroup()
    orbitales = VGroup()
    for i in range(n):
        x = -width / 2 + width * i / (n - 1)
        pos = center + RIGHT * x
        carbones.add(Dot(pos, radius=0.06, color=color))
        orbitales.add(Line(pos, pos + UP * 0.4, color=color, stroke_width=2))
        orbitales.add(Line(pos, pos + DOWN * 0.4, color=color, stroke_width=2))

    nuage_haut = Circle(radius=0.4, color=cloud_color, fill_color=cloud_color, fill_opacity=0.25, stroke_width=2)
    nuage_haut.stretch_to_fit_width(width + 0.5)
    nuage_haut.move_to(center + UP * 0.6)
    nuage_bas = nuage_haut.copy().move_to(center + DOWN * 0.6)

    return VGroup(plan, orbitales, carbones, nuage_haut, nuage_bas)


class DelocalisationCaractereAromatique(NotionScene):
    def construct(self):
        titre = scene_title("4. Délocalisation des électrons π")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le carbone trigonal et les liaisons σ ---------------------
        enonce = Text(
            _wrap(
                "Dans le cycle benzénique, chaque atome de carbone est "
                "trigonal : il forme 3 liaisons σ dans un même plan (2 "
                "vers ses carbones voisins, 1 vers un hydrogène). Il lui "
                "reste un 4ᵉ électron, dans une orbitale p perpendiculaire "
                "à ce plan.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)
        _fit(enonce, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Reprenons au niveau atomique. Dans le cycle benzénique, "
                "chaque atome de carbone est trigonal : il forme trois "
                "liaisons sigma situées dans un même plan, deux vers ses "
                "carbones voisins et une vers un atome d'hydrogène. Il "
                "lui reste alors un quatrième électron, logé dans une "
                "orbitale p, perpendiculaire à ce plan."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : vue de profil, le nuage π --------------
        entete = Text("Vue de profil du cycle : le nuage π délocalisé", font_size=23, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        schema = _vue_profil(ORIGIN)
        schema.next_to(entete, DOWN, buff=0.6)
        _fit(schema, entete.get_bottom()[1] - 0.6)

        legende = Text("nuage électronique π délocalisé au-dessus / en-dessous du plan", font_size=18, color=YELLOW)
        legende.next_to(schema, DOWN, buff=0.35)

        groupe_schema = VGroup(entete, schema, legende)

        with self.voiceover(
            text=(
                "Vue de profil, le cycle apparaît comme un plan portant, "
                "à chaque carbone, une orbitale p perpendiculaire, avec "
                "un lobe au-dessus et un lobe en-dessous. Ces six "
                "orbitales p se recouvrent latéralement les unes avec les "
                "autres, tout autour du cycle : les six électrons "
                "correspondants ne restent donc pas localisés entre deux "
                "carbones précis, mais forment un unique nuage "
                "électronique délocalisé, réparti au-dessus et "
                "en-dessous du plan de la molécule."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(schema))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : ce nuage explique les 3 faits du § 2 --------------
        entete2 = Text("Ce nuage explique les faits observés", font_size=24, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        explications = _bullets(
            [
                "Pas de décoloration de l'eau de brome : il n'y a pas de "
                "vraie double liaison localisée à \"additionner\"",
                "Réactions de substitution : le nuage délocalisé, très "
                "stable, résiste à l'addition et se conserve",
                "Molécule plane hexagonale régulière : imposée par les 6 "
                "carbones trigonaux et le recouvrement circulaire des "
                "orbitales p",
            ],
            font_size=21,
            width=54,
        )
        explications.next_to(entete2, DOWN, buff=0.35)
        groupe_expl = VGroup(entete2, explications)
        _fit(groupe_expl, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Ce nuage délocalisé explique enfin les trois faits "
                "observés précédemment. Le benzène ne décolore pas l'eau "
                "de brome, car il n'existe pas de double liaison "
                "localisée à additionner. Il privilégie les réactions de "
                "substitution, car ce nuage très stable résiste à "
                "l'addition et cherche à se conserver. Et la molécule est "
                "plane et hexagonale régulière, car cette géométrie est "
                "imposée par les six carbones trigonaux et par le "
                "recouvrement circulaire de leurs orbitales p."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(explications))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_expl))

        # --- À retenir : definition_box « caractère aromatique » ----------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le caractère aromatique est la propriété d'une "
                    "molécule cyclique plane possédant un système "
                    "d'électrons π délocalisés sur l'ensemble du cycle, "
                    "qui lui confère une stabilité particulière et "
                    "privilégie les réactions de substitution.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la définition du caractère aromatique : c'est "
                "la propriété d'une molécule cyclique plane possédant un "
                "système d'électrons pi délocalisés sur l'ensemble du "
                "cycle, ce qui lui confère une stabilité particulière et "
                "privilégie les réactions de substitution plutôt que "
                "d'addition. Attention à ne pas confondre délocalisation "
                "et simple alternance de doubles liaisons : c'est bien le "
                "recouvrement continu des orbitales p qui est en jeu, pas "
                "une succession de liaisons doubles indépendantes."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition), FadeOut(titre))
