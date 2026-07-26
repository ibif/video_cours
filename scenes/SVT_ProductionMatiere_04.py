"""
scenes/SVT_ProductionMatiere_04.py — Chapitre 11 (1ereD, SVT), scène 04.

§ 11.2.2 La lumière est indispensable (expérience de la feuille
partiellement masquée) et § 11.2.3 la chlorophylle est indispensable
(expérience de la feuille panachée) — deux expériences entièrement
résolues.
Source : 1ereD/SVT.pdf, pages 147-148.
"""

import textwrap

from manim import (
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Ellipse,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_anchor):
    """Réduit l'échelle de `mobject` si sa hauteur dépasse le cadre
    visible OU si sa largeur dépasse la largeur du cadre (cas fréquent
    d'un groupe boîte + schéma placés côte à côte)."""
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_anchor - bas_visible
    largeur_dispo = config.frame_width - 0.5
    echelle = 1.0
    if mobject.height > hauteur_dispo:
        echelle = min(echelle, hauteur_dispo / mobject.height)
    if mobject.width > largeur_dispo:
        echelle = min(echelle, largeur_dispo / mobject.width)
    if echelle < 1.0:
        mobject.scale(echelle, about_point=mobject.get_top())
    return mobject


def _feuille_masquee(apres=False):
    """Feuille ovale : moitié cachée (aluminium) / moitié éclairée.
    Après le test : moitié éclairée bleu-noir, moitié masquée jaune-brun."""
    feuille = Ellipse(width=2.4, height=1.5, color=WHITE, stroke_width=2, fill_opacity=0)

    if not apres:
        gauche = Rectangle(width=1.2, height=1.5, fill_color=GREEN, fill_opacity=0.7, stroke_width=0)
        droite = Rectangle(width=1.2, height=1.5, fill_color=GRAY, fill_opacity=0.85, stroke_width=0)
        gauche.move_to(feuille.get_center() + LEFT * 0.6)
        droite.move_to(feuille.get_center() + RIGHT * 0.6)
        groupe = VGroup(feuille, gauche, droite)
        label = Text("cache opaque\n(aluminium)", font_size=14, color=WHITE)
        label.next_to(groupe, DOWN, buff=0.15)
        return VGroup(groupe, label)
    else:
        gauche = Rectangle(width=1.2, height=1.5, fill_color="#0D1B4C", fill_opacity=0.9, stroke_width=0)
        droite = Rectangle(width=1.2, height=1.5, fill_color=YELLOW, fill_opacity=0.55, stroke_width=0)
        gauche.move_to(feuille.get_center() + LEFT * 0.6)
        droite.move_to(feuille.get_center() + RIGHT * 0.6)
        groupe = VGroup(feuille, gauche, droite)
        label = Text("éclairée : bleu-noir | masquée : jaune-brun", font_size=13, color=WHITE)
        label.next_to(groupe, DOWN, buff=0.15)
        return VGroup(groupe, label)


def _feuille_panachee(apres=False):
    """Feuille avec centre vert (chlorophylle) et bords blancs."""
    feuille = Ellipse(width=2.6, height=1.6, color=WHITE, stroke_width=2, fill_opacity=0.12, fill_color=WHITE)
    couleur_centre = "#0D1B4C" if apres else GREEN
    centre = Ellipse(width=1.3, height=0.9, fill_color=couleur_centre, fill_opacity=0.85, stroke_width=0)
    centre.move_to(feuille.get_center())
    if apres:
        feuille.set_fill(YELLOW, opacity=0.4)
    label = Text(
        "test : centre bleu-noir, bords jaune-brun" if apres else "centre vert / bords blancs",
        font_size=13,
        color=WHITE,
    )
    groupe = VGroup(feuille, centre)
    label.next_to(groupe, DOWN, buff=0.15)
    return VGroup(groupe, label)


class LumiereEtChlorophylleIndispensables(NotionScene):
    def construct(self):
        # --- Énoncé -------------------------------------------------------
        titre = scene_title("11.2.2-11.2.3 — Lumière et chlorophylle indispensables")
        titre.scale(0.48)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Deux expériences classiques permettent de prouver que la "
                "lumière, puis la chlorophylle, sont indispensables à la "
                "production de matière organique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Exemple traité : la feuille partiellement masquée ---------------
        exemple_lumiere = example_box(
            Text(
                _wrap(
                    "Un géranium à l'obscurité 48 h (réserves épuisées) "
                    "reçoit un cache opaque sur une partie d'une feuille, "
                    "puis quelques heures de lumière. Après décoloration "
                    "et test à l'eau iodée, seule la partie éclairée "
                    "devient bleu-noir.",
                    width=52,
                ),
                font_size=20,
            ),
            box_width=11.2,
        )
        exemple_lumiere.to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        avant = _feuille_masquee(apres=False)
        apres = _feuille_masquee(apres=True)
        schemas_lumiere = VGroup(avant, apres).arrange(DOWN, buff=0.35)
        schemas_lumiere.scale(0.85)
        schemas_lumiere.next_to(exemple_lumiere, RIGHT, buff=0.4)

        groupe_lumiere = VGroup(exemple_lumiere, schemas_lumiere)
        groupe_lumiere.move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)
        _fit(groupe_lumiere, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "On prend un géranium en pot, placé à l'obscurité pendant "
                "quarante-huit heures pour épuiser les réserves d'amidon "
                "de ses feuilles. On fixe sur une feuille, toujours "
                "attachée à la plante, un cache opaque en aluminium qui "
                "masque seulement une partie de la feuille. On expose la "
                "plante à la lumière pendant quelques heures, puis on "
                "prélève la feuille, on enlève le cache, et on réalise le "
                "test à l'eau iodée après décoloration. Résultat : la "
                "partie éclairée devient bleu-noir ; la partie masquée "
                "reste jaune-brun, couleur de l'eau iodée."
            )
        ) as tracker:
            self.play(FadeIn(exemple_lumiere))
            self.play(FadeIn(avant))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "L'amidon n'apparaît donc que dans la zone éclairée. La "
                "zone masquée, qui n'a pas reçu de lumière, n'a pas "
                "fabriqué d'amidon, alors que c'était la même feuille, "
                "avec la même chlorophylle et le même air : seule la "
                "lumière différait entre les deux zones. Conclusion : la "
                "lumière est indispensable à la production de matière "
                "organique par le végétal vert."
            )
        ) as tracker:
            self.play(FadeIn(apres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_lumiere))

        # --- Exemple traité : la feuille panachée -----------------------------
        exemple_chlorophylle = example_box(
            Text(
                _wrap(
                    "Une plante à feuilles panachées (vertes au centre, "
                    "blanches sur les bords) est mise 48 h à l'obscurité, "
                    "puis exposée à la lumière quelques heures. Après "
                    "décoloration et test, seules les zones qui étaient "
                    "vertes deviennent bleu-noir.",
                    width=52,
                ),
                font_size=20,
            ),
            box_width=11.2,
        )
        exemple_chlorophylle.to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        avant_2 = _feuille_panachee(apres=False)
        apres_2 = _feuille_panachee(apres=True)
        schemas_chloro = VGroup(avant_2, apres_2).arrange(DOWN, buff=0.35)
        schemas_chloro.scale(0.85)
        schemas_chloro.next_to(exemple_chlorophylle, RIGHT, buff=0.4)

        groupe_chloro = VGroup(exemple_chlorophylle, schemas_chloro)
        groupe_chloro.move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)
        _fit(groupe_chloro, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Certaines plantes cultivées, géranium panaché, coleus, "
                "portent des feuilles panachées : vertes au centre, "
                "blanches ou jaunes sur les bords, car la chlorophylle "
                "n'y est pas présente partout. On place la plante "
                "quarante-huit heures à l'obscurité, on repère avec "
                "précision le dessin des zones vertes et blanches d'une "
                "feuille, puis on l'expose à la lumière quelques heures, "
                "avant de réaliser le test à l'eau iodée après "
                "décoloration."
            )
        ) as tracker:
            self.play(FadeIn(exemple_chlorophylle))
            self.play(FadeIn(avant_2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Résultat : après le test, les zones qui étaient vertes "
                "deviennent bleu-noir ; les zones qui étaient blanches "
                "restent jaune-brun. Toute la feuille a pourtant reçu la "
                "même lumière et le même air ; seule la présence de "
                "chlorophylle différait entre les zones. Conclusion : la "
                "chlorophylle est indispensable à la production de "
                "matière organique. C'est le pigment vert qui capte "
                "l'énergie lumineuse."
            )
        ) as tracker:
            self.play(FadeIn(apres_2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(groupe_chloro))
