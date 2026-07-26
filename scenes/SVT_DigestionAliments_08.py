"""
scenes/SVT_DigestionAliments_08.py — Chapitre 12 (1ereD, SVT), scène 08.

§ 12.5 Étude expérimentale de l'action des enzymes digestives : action de
la salive sur l'amidon (protocole A1/A2, eau iodée + Fehling), influence
de la température et du pH (salive bouillie/refroidie, pepsine + acidité
sur blanc d'œuf), méthode d'analyse en 4 étapes, rôle de la bile
(émulsion : eau+huile vs eau+huile+sels biliaires).
Source : 1ereD/SVT.pdf, pages 161-163.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tube(label: str, fill_color, w=1.0, h=1.6):
    body = Rectangle(width=w, height=h, color=WHITE, fill_color=fill_color, fill_opacity=0.85)
    txt = Text(label, font_size=16, color=WHITE)
    txt.next_to(body, DOWN, buff=0.15)
    return VGroup(body, txt)


class EtudeExperimentaleDesEnzymesDigestives(NotionScene):
    def construct(self):
        titre = scene_title("12.5 — Étude expérimentale des enzymes")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : le protocole A1 / A2 -----------------------------------
        protocole = Text(
            _wrap(
                "Protocole : deux tubes avec la même quantité d'eau "
                "d'amidon. Tube A1 : eau distillée ajoutée. Tube A2 : "
                "liquide salivaire ajouté. Les deux, 10 min au bain-marie "
                "à 37°C, puis testés à l'eau iodée et à la liqueur de "
                "Fehling.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        protocole.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On prépare deux tubes contenant la même quantité d'eau "
                "d'amidon. Au tube A1, on ajoute de l'eau distillée ; au "
                "tube A2, on ajoute du liquide salivaire recueilli après "
                "s'être rincé la bouche. Les deux tubes sont placés dix "
                "minutes dans un bain-marie à trente-sept degrés. On "
                "partage ensuite le contenu de chaque tube en deux "
                "portions : l'une testée à l'eau iodée, l'autre chauffée "
                "avec de la liqueur de Fehling."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(protocole))

        # --- Animation du raisonnement : résultats des tests -------------------
        entete_res = Text("Résultats", font_size=25, color=YELLOW, weight="BOLD")
        entete_res.next_to(titre, DOWN, buff=0.4)

        iode_titre = Text("Eau iodée", font_size=19, color=WHITE)
        a1_iode = _tube("A1 : bleu violet\n(amidon présent)", "#3A2E8C")
        a2_iode = _tube("A2 : jaune brun\n(amidon disparu)", "#B08A2E")
        iode_row = VGroup(a1_iode, a2_iode).arrange(RIGHT, buff=1.0)
        iode_group = VGroup(iode_titre, iode_row).arrange(DOWN, buff=0.3)

        fehling_titre = Text("Liqueur de Fehling", font_size=19, color=WHITE)
        a1_fehling = _tube("A1 : reste bleu\n(pas de sucre)", BLUE)
        a2_fehling = _tube("A2 : précipité\nrouge brique", ORANGE)
        fehling_row = VGroup(a1_fehling, a2_fehling).arrange(RIGHT, buff=1.0)
        fehling_group = VGroup(fehling_titre, fehling_row).arrange(DOWN, buff=0.3)

        resultats = VGroup(iode_group, fehling_group).arrange(RIGHT, buff=1.4)
        resultats.next_to(entete_res, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avec l'eau iodée, le contenu du tube A1 devient bleu "
                "violet : l'amidon est encore présent. Celui du tube A2 "
                "reste jaune brun : l'amidon a disparu. Avec la liqueur de "
                "Fehling chauffée, la portion issue de A1 reste bleue, "
                "pas de sucre réducteur, tandis que celle issue de A2 "
                "donne un précipité rouge brique, signe de la présence de "
                "maltose."
            )
        ) as tracker:
            self.play(FadeIn(entete_res))
            self.play(FadeIn(iode_group))
            self.play(FadeIn(fehling_group))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_res), FadeOut(resultats))

        # --- Exemple traité : interprétation ------------------------------------
        interpretation = example_box(
            Text(
                _wrap(
                    "Interprétation : la seule différence entre A1 et A2 "
                    "est la présence de salive. La salive a donc "
                    "transformé l'amidon en maltose, grâce à l'amylase "
                    "salivaire, puisque l'eau distillée seule ne produit "
                    "rien.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        interpretation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Interprétation : la seule différence entre A1 et A2 est "
                "la présence de salive. La salive a donc transformé "
                "l'amidon en maltose. Cette transformation est due à "
                "l'amylase salivaire, puisque l'eau distillée seule ne "
                "produit rien."
            )
        ) as tracker:
            self.play(FadeIn(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interpretation))

        # --- Influence de la température et du pH ---------------------------------
        entete_temp = Text("Influence de la température et du pH", font_size=23, color=YELLOW, weight="BOLD")
        entete_temp.next_to(titre, DOWN, buff=0.45)

        temp_bullets = _bullets(
            [
                "Salive bouillie puis refroidie : le test reste bleu violet — l'amylase est dénaturée (irréversible).",
                "Salive refroidie (glace) : digestion très lente — le froid ralentit sans détruire ; à 37°C, activité normale retrouvée.",
                "Blanc d'œuf + pepsine + HCl dilué à 37°C : le blanc se dissout. Sans acide : rien. Acide seul, sans pepsine : rien non plus.",
            ],
            font_size=19,
            width=56,
        )
        temp_bullets.next_to(entete_temp, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Des variantes du protocole renseignent sur les "
                "conditions d'action des enzymes. Si l'on remplace la "
                "salive fraîche par de la salive portée à ébullition puis "
                "refroidie, le test à l'eau iodée redevient bleu violet : "
                "l'amidon n'a pas été digéré, la chaleur a dénaturé "
                "l'amylase, de façon irréversible. Un tube amidon plus "
                "salive placé dans la glace montre une digestion très "
                "lente : le froid ralentit l'enzyme sans la détruire ; "
                "ramené à trente-sept degrés, le tube retrouve une "
                "activité normale. Enfin, des cubes de blanc d'œuf dur "
                "placés avec de la pepsine se dissolvent peu à peu à "
                "trente-sept degrés seulement en présence d'acide "
                "chlorhydrique dilué ; sans acide, rien ; et l'acide seul, "
                "sans pepsine, ne dissout rien non plus. La pepsine n'agit "
                "donc qu'en milieu acide."
            )
        ) as tracker:
            self.play(FadeIn(entete_temp))
            self.play(FadeIn(temp_bullets))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_temp), FadeOut(temp_bullets))

        # --- À retenir : méthode d'analyse en 4 étapes ----------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Étape 1 : repérer la variable étudiée (le seul "
                    "facteur qui change entre les tubes). Étape 2 : "
                    "identifier le tube témoin et le(s) tube(s) "
                    "expérimental(aux). Étape 3 : comparer les résultats, "
                    "test par test. Étape 4 : conclure uniquement à partir "
                    "de la différence observée.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode pour analyser une expérience de digestion. "
                "Étape un : repérer la variable étudiée, c'est-à-dire "
                "l'unique facteur qui change entre les tubes — présence "
                "de salive, température, pH. Étape deux : identifier le "
                "tube témoin, sans le facteur étudié, et le ou les tubes "
                "expérimentaux. Étape trois : comparer les résultats "
                "obtenus dans chaque tube, test par test. Étape quatre : "
                "conclure uniquement à partir de la différence observée : "
                "si seul le tube contenant la salive digère l'amidon, "
                "alors c'est la salive, et non une autre cause, qui est "
                "responsable."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Rôle de la bile : l'émulsion des graisses -----------------------------
        entete_bile = Text("Rôle de la bile : l'émulsion des graisses", font_size=22, color=YELLOW, weight="BOLD")
        entete_bile.next_to(titre, DOWN, buff=0.45)

        tube1 = _tube("Eau + huile\n→ 2 couches\n(émulsion se dépare)", "#7FA8D9", w=1.3, h=1.8)
        tube2 = _tube("Eau + huile +\nsels biliaires\n→ trouble, stable", "#D9C87F", w=1.3, h=1.8)
        tubes_bile = VGroup(tube1, tube2).arrange(RIGHT, buff=1.6)
        tubes_bile.next_to(entete_bile, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Dans un premier tube, on verse de l'eau et de l'huile ; "
                "dans un deuxième tube, de l'eau, de l'huile et des sels "
                "biliaires. Après agitation et dix minutes de repos, dans "
                "le premier tube l'huile remonte et forme une couche "
                "séparée : l'émulsion se dépare. Dans le deuxième tube, le "
                "mélange reste trouble et homogène : l'émulsion est "
                "stable. Conclusion : les sels biliaires maintiennent les "
                "graisses dispersées en gouttelettes microscopiques. Cette "
                "action est physique — la bile ne contient pas d'enzyme "
                "— mais elle est indispensable : elle prépare l'action "
                "chimique de la lipase, qui ne peut attaquer efficacement "
                "que des graisses finement divisées."
            )
        ) as tracker:
            self.play(FadeIn(entete_bile))
            self.play(FadeIn(tubes_bile))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_bile), FadeOut(tubes_bile))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne dis pas que « la bile digère les graisses » au "
                    "sens chimique : elle ne les découpe pas. Formulation "
                    "correcte : « la bile émulsionne les graisses, ce qui "
                    "facilite l'action des lipases ». La digestion "
                    "chimique des lipides est l'œuvre des lipases.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ne dis pas que la bile digère les graisses au sens "
                "chimique : elle ne les découpe pas. La formulation "
                "correcte est : la bile émulsionne les graisses, ce qui "
                "facilite l'action des lipases. La digestion chimique des "
                "lipides est l'œuvre des lipases."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
