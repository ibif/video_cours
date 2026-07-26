"""
scenes/SVT_EcosystemeAgroIndustriel_14.py — Chapitre 11 (1ereC, SVT), scène 14.

§ 7.1-7.2 L'agrosystème : définition (écosystème créé par l'homme,
exemples ivoiriens cacao/café/palmier à huile/hévéa/ananas/banane/
vivriers) et les 3 caractéristiques (biocénose simplifiée/monoculture ;
système très ouvert avec tableau des intrants ; productivité élevée mais
coûteuse et non autorégulée). Source : 1ereC/SVT.pdf, pages 130-131.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
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


class LAgrosystemeEtSesCaracteristiques(NotionScene):
    def construct(self):
        titre = scene_title("7 — L'écosystème agro-industriel (l'agrosystème)")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition + exemples ivoiriens ----------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un agrosystème (ou écosystème agro-industriel) est un "
                    "écosystème créé et entretenu par l'homme pour "
                    "produire des denrées agricoles : champ, plantation, "
                    "verger, rizière, étang de pisciculture, ferme "
                    "d'élevage.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Après avoir étudié les écosystèmes naturels, tournons "
                "nous vers un autre type d'écosystème : celui que l'homme "
                "façonne pour produire sa nourriture. Un agrosystème, ou "
                "écosystème agro-industriel, est un écosystème créé et "
                "entretenu par l'homme pour produire des denrées "
                "agricoles : champ, plantation, verger, rizière, étang de "
                "pisciculture, ferme d'élevage."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        exemples_titre = Text("Les grands agrosystèmes ivoiriens", font_size=23, color=YELLOW, weight="BOLD")
        exemples_titre.next_to(titre, DOWN, buff=0.45)
        exemples = _bullets(
            [
                "Cultures de rente : cacao (1er producteur mondial), café, palmier à huile, hévéa (caoutchouc), ananas, banane.",
                "Cultures vivrières : riz, maïs, manioc, igname.",
            ],
            font_size=21,
            width=56,
        )
        exemples.next_to(exemples_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "En Côte d'Ivoire, les grands agrosystèmes sont les "
                "plantations de cacao, premier producteur mondial, de "
                "café, de palmier à huile, d'hévéa pour le caoutchouc, "
                "d'ananas et de banane, ainsi que les champs vivriers de "
                "riz, de maïs, de manioc et d'igname."
            )
        ) as tracker:
            self.play(FadeIn(exemples_titre))
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples_titre), FadeOut(exemples))

        # --- Raisonnement : caractéristique 1, biocénose simplifiée --------------
        carac1 = property_box(
            Text(
                _wrap(
                    "a) Biocénose simplifiée. L'homme sélectionne une ou "
                    "quelques espèces utiles (monoculture du cacao ou du "
                    "palmier) et élimine les autres (désherbage, "
                    "pesticides). La biodiversité est faible, le réseau "
                    "trophique pauvre : l'agrosystème est donc "
                    "naturellement instable et vulnérable (pullulation de "
                    "ravageurs, maladies).",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=11.8,
        )
        carac1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comparé à l'écosystème naturel, l'agrosystème présente "
                "trois traits fondamentaux. D'abord, une biocénose "
                "simplifiée : l'homme sélectionne une ou quelques espèces "
                "utiles, c'est la monoculture du cacao ou du palmier, et "
                "élimine les autres par le désherbage et les pesticides. "
                "La biodiversité est faible, le réseau trophique pauvre : "
                "l'agrosystème est donc naturellement instable et "
                "vulnérable, exposé à la pullulation de ravageurs et aux "
                "maladies."
            )
        ) as tracker:
            self.play(FadeIn(carac1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(carac1))

        # --- Exemple traité : système ouvert, tableau des intrants ---------------
        intrants_titre = Text("b) Un système très ouvert : les intrants", font_size=21, color=YELLOW, weight="BOLD")
        intrants_titre.next_to(titre, DOWN, buff=0.4)
        intrants = _bullets(
            [
                "Engrais minéraux (NPK, urée, potasse) : restituer les éléments exportés.",
                "Engrais organiques (compost, fumier, engrais verts) : améliorer la fertilité du sol.",
                "Produits phytosanitaires (herbicides, insecticides, fongicides) : protéger les cultures.",
                "Eau (irrigation goutte-à-goutte, aspersion).",
                "Énergie fossile et mécanisation (tracteurs, pompes, séchoirs) : travail, transport, transformation.",
                "Semences sélectionnées : rendement et qualité.",
            ],
            font_size=16,
            width=64,
        )
        intrants.next_to(intrants_titre, DOWN, buff=0.3)
        groupe_intrants = VGroup(intrants_titre, intrants)
        _fit(groupe_intrants, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Ensuite, un système très ouvert : exportations et "
                "intrants. À chaque récolte, l'homme exporte de la "
                "biomasse, cabosses de cacao, régimes de palme, grains de "
                "café, et donc les éléments minéraux qu'elle contient. "
                "Contrairement à l'écosystème naturel, le recyclage ne se "
                "fait pas sur place : le sol s'épuise. Pour maintenir la "
                "production, l'homme doit apporter des intrants : des "
                "engrais minéraux pour restituer les éléments exportés ; "
                "des engrais organiques pour améliorer la fertilité du "
                "sol ; des produits phytosanitaires pour protéger les "
                "cultures ; de l'eau d'irrigation ; de l'énergie fossile "
                "et de la mécanisation ; et des semences sélectionnées."
            )
        ) as tracker:
            self.play(FadeIn(intrants_titre))
            self.play(FadeIn(intrants))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intrants_titre), FadeOut(intrants))

        # --- À retenir : caractéristique 3, productivité coûteuse ----------------
        carac3 = property_box(
            Text(
                _wrap(
                    "c) Une productivité primaire élevée mais coûteuse. "
                    "Grâce aux intrants, l'agrosystème atteint une "
                    "productivité par hectare souvent supérieure à celle "
                    "de l'écosystème naturel. Mais elle est obtenue au "
                    "prix d'une dépense d'énergie fossile et d'une "
                    "dépendance permanente : l'agrosystème ne peut pas "
                    "s'autoréguler ; sans l'intervention de l'homme, il "
                    "retourne à la friche.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=11.8,
        )
        carac3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Enfin, une productivité primaire élevée, mais coûteuse. "
                "Grâce aux intrants, l'agrosystème atteint une "
                "productivité par hectare souvent supérieure à celle de "
                "l'écosystème naturel. Mais cette productivité est "
                "obtenue au prix d'une dépense d'énergie fossile et d'une "
                "dépendance permanente : l'agrosystème ne peut pas "
                "s'autoréguler. Sans l'intervention constante de l'homme, "
                "il retourne rapidement à la friche."
            )
        ) as tracker:
            self.play(FadeIn(carac3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(carac3))
