"""
scenes/SVT_RoleGonadesMammiferes_04.py — Chapitre 1 (1ereC, SVT), scène 04.

Le rôle des gonades : mise en évidence expérimentale du double rôle
exocrine (production de gamètes) et endocrine (sécrétion d'hormones
sexuelles) — castration, greffe, dosages hormonaux.
Source : 1ereC/SVT.pdf, page 8.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Cross,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _animal_icon(color=WHITE):
    corps = Circle(radius=0.35, color=color, stroke_width=3)
    tete = Circle(radius=0.18, color=color, stroke_width=3)
    tete.next_to(corps, UP, buff=-0.05)
    return VGroup(corps, tete)


class RoleDesGonadesMiseEnEvidence(NotionScene):
    def construct(self):
        titre = scene_title("1.4 — Le rôle des gonades")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : comment prouver le double rôle ? ------------------------
        enonce = Text(
            _wrap(
                "Comment prouver que la gonade a bien deux rôles ? Le rôle "
                "des gonades a été établi historiquement par des "
                "expériences de castration et de greffe, complétées "
                "aujourd'hui par des dosages hormonaux.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Comment prouver que la gonade a bien deux rôles ? Le rôle "
                "des gonades a été établi historiquement par des "
                "expériences de castration et de greffe, complétées "
                "aujourd'hui par des dosages hormonaux, qui mesurent la "
                "quantité d'hormones présentes dans le sang."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : les trois groupes expérimentaux -----
        temoin = _animal_icon(color=WHITE)
        temoin_lbl = Text("témoin", font_size=16, color=WHITE).next_to(temoin, DOWN, buff=0.15)
        temoin_obs = Text("gamètes + caractères\nsexuels normaux", font_size=13, color="#288073").next_to(
            temoin_lbl, DOWN, buff=0.15
        )
        groupe_temoin = VGroup(temoin, temoin_lbl, temoin_obs)

        castre = _animal_icon(color=WHITE)
        croix = Cross(stroke_color="#B42E41", stroke_width=4).scale(0.35).move_to(castre.get_center() + DOWN * 0.6)
        castre_lbl = Text("castré (gonades\nretirées)", font_size=16, color=WHITE).next_to(castre, DOWN, buff=0.55)
        castre_obs = Text(
            "arrêt des gamètes +\nrégression des caractères", font_size=13, color="#B42E41"
        ).next_to(castre_lbl, DOWN, buff=0.15)
        groupe_castre = VGroup(castre, croix, castre_lbl, castre_obs)

        greffe = _animal_icon(color=WHITE)
        petit_rond = Circle(radius=0.1, color="#DE7C1F", fill_opacity=0.9).move_to(greffe.get_center() + DOWN * 0.5)
        greffe_lbl = Text("castré + greffe\n(ou extrait)", font_size=16, color=WHITE).next_to(greffe, DOWN, buff=0.55)
        greffe_obs = Text(
            "caractères restaurés\n(gamètes si voies intactes)", font_size=13, color="#288073"
        ).next_to(greffe_lbl, DOWN, buff=0.15)
        groupe_greffe = VGroup(greffe, petit_rond, greffe_lbl, greffe_obs)

        groupes = VGroup(groupe_temoin, groupe_castre, groupe_greffe).arrange(RIGHT, buff=1.1)
        groupes.next_to(titre, DOWN, buff=0.8)

        fleche1 = Line(groupe_temoin.get_right(), groupe_castre.get_left(), color=WHITE)
        fleche2 = Line(groupe_castre.get_right(), groupe_greffe.get_left(), color=WHITE)

        with self.voiceover(
            text=(
                "Comparons trois groupes d'animaux. Le groupe témoin, non "
                "modifié, produit normalement ses gamètes et présente des "
                "caractères sexuels normaux. Chez un animal castré, c'est-à-"
                "dire dont on a retiré les gonades, la production de "
                "gamètes s'arrête et les caractères sexuels secondaires "
                "régressent. Mais chez un animal castré à qui l'on greffe "
                "une gonade, ou à qui l'on injecte un extrait gonadique, les "
                "caractères sexuels sont restaurés."
            )
        ) as tracker:
            self.play(FadeIn(groupe_temoin))
            self.play(FadeIn(fleche1), FadeIn(groupe_castre))
            self.play(FadeIn(fleche2), FadeIn(groupe_greffe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupes), FadeOut(fleche1), FadeOut(fleche2))

        # --- Exemple traité : le cas de l'injection d'extrait -----------------
        exemple = Text(
            _wrap(
                "Exemple : chez un rat mâle castré, le pelage et le "
                "comportement se féminisent et la spermatogenèse cesse. Une "
                "simple injection d'extrait testiculaire (sans reconnexion "
                "des voies génitales) restaure les caractères sexuels "
                "secondaires — mais PAS la production de spermatozoïdes.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        exemple.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Prenons un exemple précis : chez un rat mâle castré, le "
                "pelage et le comportement se féminisent, et la "
                "spermatogenèse, c'est-à-dire la fabrication des "
                "spermatozoïdes, s'arrête complètement. Or, une simple "
                "injection d'extrait testiculaire, sans aucune reconnexion "
                "des voies génitales, restaure les caractères sexuels "
                "secondaires, mais ne restaure PAS la production de "
                "spermatozoïdes, puisque les voies restent sectionnées."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : le double rôle démontré --------------------------------
        conclusion = property_box(
            Text(
                _wrap(
                    "Cette expérience prouve le double rôle de la gonade : "
                    "un rôle EXOCRINE (production de gamètes, transportés "
                    "par les voies génitales) ET un rôle ENDOCRINE "
                    "(sécrétion d'hormones sexuelles, transportées par le "
                    "sang). L'extrait, seul, ne peut agir que par voie "
                    "sanguine : il ne prouve donc QUE le rôle endocrine.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        conclusion.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Cette expérience prouve donc le double rôle de la gonade : "
                "un rôle exocrine, la production de gamètes transportés par "
                "les voies génitales, et un rôle endocrine, la sécrétion "
                "d'hormones sexuelles transportées par le sang. L'extrait, "
                "utilisé seul, ne peut agir que par voie sanguine : il ne "
                "prouve donc que le rôle endocrine, jamais le rôle exocrine."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas le produit qui emprunte les VOIES "
                    "GÉNITALES (les gamètes = rôle exocrine) avec celui qui "
                    "emprunte le SANG (les hormones = rôle endocrine). Une "
                    "greffe qui reconnecte les voies restaure les deux "
                    "rôles ; un extrait injecté ne restaure QUE l'endocrine.",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à bien distinguer les deux voies : les gamètes "
                "empruntent les voies génitales, c'est le rôle exocrine ; "
                "les hormones empruntent le sang, c'est le rôle endocrine. "
                "Une greffe qui reconnecte les voies génitales restaure les "
                "deux rôles à la fois, alors qu'un simple extrait injecté ne "
                "restaure que le rôle endocrine."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
