"""
scenes/SVT_Photosynthese_12.py — Chapitre 10 (1ereC, SVT), scène 12.

§ 10.5.2-10.5.3 Mise en évidence expérimentale (2/2) : le test à l'eau
iodée (méthode technique en 5 étapes : dégarnir/décolorer/rincer/arroser)
+ tableau des 4 expériences classiques avec témoins (lumière, chlorophylle,
CO2, O2 dégagé) + Exemple résolu 1 (calcul du débit horaire de dégagement
gazeux, identification du gaz, rôle du témoin).
Source : 1ereC/SVT.pdf, pages 111-112.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, definition_box, exercise_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _cell(text: str, x: float, y: float, font_size=11, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


class TestEauIodeeEtExperiencesClassiques(NotionScene):
    def construct(self):
        titre = scene_title("10.5.2-10.5.3 — Mise en évidence expérimentale (2/2)")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi le test à l'eau iodée révèle la photosynthèse -
        intro = definition_box(
            Text(
                _wrap(
                    "Le glucose produit est rapidement transformé en "
                    "amidon de réserve, stocké dans les chloroplastes. "
                    "Or l'eau iodée (jaune-orangé) devient bleue-"
                    "violacée à noire en présence d'amidon : c'est un "
                    "révélateur commode de la photosynthèse.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        intro.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Après le dégagement d'oxygène, une seconde méthode "
                "classique révèle la photosynthèse : le test à l'eau "
                "iodée. Le glucose produit est en effet rapidement "
                "transformé en amidon de réserve, stocké dans les "
                "chloroplastes. Or l'eau iodée, jaune-orangé, devient "
                "bleue-violacée à noire en présence d'amidon : c'est un "
                "révélateur commode de la photosynthèse."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : méthode en 5 étapes -------------------
        methode = method_box(
            _bullets(
                [
                    "1. Dégarnir la plante : 48h à l'obscurité pour "
                    "épuiser les réserves d'amidon.",
                    "2. Réaliser l'expérience (éclairage, masquage...).",
                    "3. Détacher la feuille et la plonger dans l'eau "
                    "bouillante (1 min) pour tuer les cellules.",
                    "4. Décolorer la feuille dans l'alcool bouillant "
                    "(bain-marie) pour éliminer la chlorophylle.",
                    "5. Rincer, étaler et arroser d'eau iodée : les "
                    "zones avec amidon deviennent bleu-noir.",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.4,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la technique du test à l'eau iodée sur une "
                "feuille, en cinq étapes. Un : dégarnir la plante, en la "
                "plaçant quarante-huit heures à l'obscurité, pour "
                "épuiser ses réserves d'amidon. Deux : réaliser "
                "l'expérience proprement dite, éclairage, masquage. "
                "Trois : détacher la feuille et la plonger une minute "
                "dans l'eau bouillante, pour tuer les cellules et rompre "
                "les membranes. Quatre : décolorer la feuille dans "
                "l'alcool bouillant, au bain-marie, pour éliminer la "
                "chlorophylle qui masquerait la coloration. Cinq : "
                "rincer, étaler la feuille et l'arroser d'eau iodée : "
                "les zones contenant de l'amidon deviennent bleu-noir."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : tableau des 4 expériences classiques -----------
        entete_tab = Text("Quatre expériences classiques avec témoins", font_size=19, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.3)

        x_fact, x_exp, x_tem, x_res, x_conc = -6.9, -4.6, -1.9, 0.9, 3.9
        headers = ["Facteur", "Lot expérimental", "Lot témoin", "Résultat", "Conclusion"]
        row_y0 = entete_tab.get_bottom()[1] - 0.4
        row_h = 1.15

        header_row = VGroup(
            *[
                _cell(h, x, row_y0, font_size=13, color=YELLOW, bold=True)
                for h, x in zip(headers, [x_fact, x_exp, x_tem, x_res, x_conc])
            ]
        )

        rows_data = [
            (
                "Lumière",
                "Feuille partiellement\nmasquée (cache opaque),\nplante éclairée",
                "Même feuille, zone\nnon masquée",
                "Éclairée : bleu-noir ;\nmasquée : jaune-orangé",
                "Lumière nécessaire\nà l'amidon",
            ),
            (
                "Chloro-\nphylle",
                "Feuille panachée\n(zones vertes/blanches)\néclairée",
                "(comparaison interne\ndes zones)",
                "Vertes : bleu-noir ;\nblanches : jaune-orangé",
                "Chlorophylle\nnécessaire",
            ),
            (
                "CO2",
                "Plante sous cloche avec\npotasse (absorbe CO2),\néclairée",
                "Plante identique sous\ncloche sans potasse,\néclairée",
                "Sans CO2 : jaune-orangé ;\ntémoin : bleu-noir",
                "CO2 nécessaire\nà l'amidon",
            ),
            (
                "O2\ndégagé",
                "Élodée éclairée",
                "Élodée à\nl'obscurité",
                "Gaz ravive une braise\nuniquement si éclairée",
                "Photosynthèse dégage\nO2 à la lumière",
            ),
        ]

        data_rows = VGroup()
        for i, (fact, exp, tem, res, conc) in enumerate(rows_data):
            y = row_y0 - (i + 1) * row_h
            data_rows.add(
                VGroup(
                    _cell(fact, x_fact, y, font_size=12, color=YELLOW),
                    _cell(exp, x_exp, y, font_size=10.5),
                    _cell(tem, x_tem, y, font_size=10.5),
                    _cell(res, x_res, y, font_size=10.5),
                    _cell(conc, x_conc, y, font_size=10.5, color="#8FCB9A"),
                )
            )

        tableau = VGroup(header_row, data_rows)
        # Garde-fou d'auto-scale : tableau dense, on réduit si nécessaire.
        bas_visible = -config.frame_height / 2 + 0.2
        hauteur_dispo = row_y0 - bas_visible + 0.2
        if tableau.height > hauteur_dispo:
            tableau.scale(hauteur_dispo / tableau.height, about_point=[0, row_y0, 0])
        largeur_dispo = config.frame_width - 0.4
        if tableau.width > largeur_dispo:
            tableau.scale(largeur_dispo / tableau.width, about_point=[0, row_y0, 0])

        with self.voiceover(
            text=(
                "Voici les quatre expériences classiques, toutes bâties "
                "sur le même principe de témoin. Pour la lumière : une "
                "feuille partiellement masquée par un cache opaque, "
                "comparée à sa propre zone non masquée — la zone "
                "éclairée devient bleu-noir, la zone masquée reste "
                "jaune-orangé. Pour la chlorophylle : une feuille "
                "panachée, avec des zones vertes et des zones blanches — "
                "seules les zones vertes deviennent bleu-noir. Pour le "
                "CO2 : une plante sous cloche avec de la potasse, qui "
                "absorbe le CO2, comparée à une plante témoin sous "
                "cloche sans potasse — sans CO2, la feuille reste "
                "jaune-orangé. Et pour le dioxygène dégagé : une élodée "
                "éclairée, comparée à une élodée à l'obscurité — seul le "
                "gaz du lot éclairé ravive une braise."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(header_row))
            for row in data_rows:
                self.play(FadeIn(row), run_time=0.4)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : Exemple résolu 1 (débit horaire) -----------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Exemple résolu : une élodée éclairée dégage, en 40 "
                    "min, un volume de gaz de 4 mL. Le même dispositif à "
                    "l'obscurité ne dégage rien. 1. Débit horaire de "
                    "dégagement ? 2. Comment identifier ce gaz ? 3. Rôle "
                    "du dispositif à l'obscurité ?",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        enonce.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple résolu. Une élodée éclairée dégage, en "
                "quarante minutes, un volume de gaz de quatre "
                "millilitres, recueilli dans le tube gradué. Le même "
                "dispositif à l'obscurité ne dégage rien. Première "
                "question : quel est le débit horaire de dégagement "
                "gazeux ? Deuxième question : comment identifier ce gaz "
                "? Troisième question : quel est le rôle du dispositif à "
                "l'obscurité ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        correction = corrige_box(
            _bullets(
                [
                    "Débit : 4 mL / 40 min = 0,1 mL/min, soit "
                    "0,1×60 = 6 mL/h.",
                    "Identification : on approche une braise (baguette "
                    "incandescente) de l'orifice ; si elle se ravive, "
                    "le gaz est du dioxygène.",
                    "Rôle du témoin : il montre que sans lumière, aucun "
                    "gaz n'est dégagé ; le dégagement d'O2 est donc dû "
                    "à la lumière, et non à un autre facteur "
                    "(température, agitation...).",
                ],
                font_size=18,
                width=52,
            ),
            box_width=12.2,
        )
        correction.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Corrigeons. Premièrement, le débit : quatre "
                "millilitres pour quarante minutes, soit zéro virgule "
                "un millilitre par minute, ou encore six millilitres par "
                "heure. Deuxièmement, l'identification : on approche une "
                "braise, une fine baguette de bois incandescente, de "
                "l'orifice ; si elle se ravive, le gaz est du dioxygène. "
                "Troisièmement, le rôle du témoin : le dispositif à "
                "l'obscurité est le témoin ; il montre que sans lumière, "
                "aucun gaz n'est dégagé, donc que le dégagement d'O2 est "
                "bien dû à la lumière, et non à un autre facteur comme "
                "la température ou l'agitation."
            )
        ) as tracker:
            self.play(FadeIn(correction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(correction))

        # --- Piège à éviter : oublier de dégarnir la plante ---------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : oublier de dégarnir la plante (48h "
                    "à l'obscurité) avant l'expérience. Sans cette "
                    "étape, l'amidon déjà présent AVANT l'expérience "
                    "fausserait le résultat : on ne pourrait plus "
                    "savoir si l'amidon détecté vient de la "
                    "photosynthèse étudiée ou d'une réserve antérieure.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : oublier de dégarnir la "
                "plante, c'est-à-dire de la placer quarante-huit heures "
                "à l'obscurité avant l'expérience. Sans cette étape, "
                "l'amidon déjà présent avant l'expérience fausserait "
                "totalement le résultat : on ne pourrait plus savoir si "
                "l'amidon détecté vient de la photosynthèse étudiée ou "
                "d'une réserve antérieure."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
