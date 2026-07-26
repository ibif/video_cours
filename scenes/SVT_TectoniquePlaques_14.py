"""
scenes/SVT_TectoniquePlaques_14.py — Chapitre 8 (1ereC, SVT), scène 14
(clôture).

Exemple résolu 3 (exploiter un profil de foyers sismiques : profondeurs
croissantes 10→600 km, plan de Wadati-Benioff, sens de plongée) ; méthodes
et astuces (3 méthodes) ; les 5 pièges à éviter ; L'ESSENTIEL DU CHAPITRE.
Source : 1ereC/SVT.pdf, pages 93-95.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, Create, Dot, FadeIn, FadeOut, Line, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, exercise_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class SyntheseChapitreTectoniquePlaques(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse : les mouvements des plaques")
        titre.scale(0.62)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : exemple résolu 3, profil de foyers sismiques -------------
        enonce_ex3 = exercise_box(
            Text(
                _wrap(
                    "Exemple résolu 3 : sous une marge continentale, les "
                    "foyers des séismes sont à 10 km sous la fosse, puis 60, "
                    "150, 300, 450 puis 600 km, en s'enfonçant de 100, 250, "
                    "450, 700 puis 900 km horizontalement vers l'intérieur "
                    "des terres. Déterminer le sens de plongée de la plaque "
                    "et le type de frontière.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        enonce_ex3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par un dernier exemple résolu. "
                "Énoncé : sous une marge continentale, les foyers des "
                "séismes sont à dix kilomètres de profondeur sous la fosse, "
                "puis à soixante, cent cinquante, trois cents, "
                "quatre cent cinquante, puis six cents kilomètres de "
                "profondeur, en s'enfonçant de cent, deux cent cinquante, "
                "quatre cent cinquante, sept cents, puis neuf cents "
                "kilomètres horizontalement vers l'intérieur des terres. "
                "Déterminons le sens de plongée de la plaque et le type de "
                "frontière."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex3))

        # --- Animation du raisonnement : profil de foyers (plan de Wadati) -----
        axe_surface = Line([-5.0, 1.5, 0], [5.0, 1.5, 0], color=WHITE, stroke_width=2)
        label_surface = Text("surface", font_size=14, color=WHITE).next_to(axe_surface, UP, buff=0.1).align_to(axe_surface, LEFT)

        # Couples (distance horizontale en km, profondeur en km) de l'énoncé :
        # foyers à 10/60/150/300/450/600 km de profondeur, en s'enfonçant de
        # 100/250/450/700/900 km horizontalement — le dernier couple (600 km
        # de profondeur) prolonge la tendance du dernier segment mesuré.
        donnees = [(100, 10), (250, 60), (450, 150), (700, 300), (900, 450), (1050, 600)]

        # échelle graphique : x = distance horizontale / 130, y = -profondeur / 130
        points = [Dot(point=[-4.5 + d / 130.0, 1.5 - p / 130.0, 0], radius=0.06, color=YELLOW) for d, p in donnees]
        segments = VGroup(*[Line(points[i].get_center(), points[i + 1].get_center(), color=YELLOW, stroke_width=2) for i in range(len(points) - 1)])
        foyers_group = VGroup(*points)

        fosse_label = Text("fosse", font_size=14, color=WHITE).move_to([-4.5, 1.7, 0])
        interieur_label = Text("intérieur des terres →", font_size=14, color=WHITE).move_to([2.0, 1.7, 0])
        prof_label = Text("profondeur croissante ↓", font_size=14, color=YELLOW).move_to([-4.3, -1.6, 0])

        schema = VGroup(axe_surface, label_surface, foyers_group, segments, fosse_label, interieur_label, prof_label)
        schema.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Traçons ces foyers sur un profil : en abscisse, la "
                "distance horizontale depuis la fosse ; en ordonnée, la "
                "profondeur. On voit apparaître un alignement incliné, dont "
                "la profondeur croît régulièrement à mesure que l'on "
                "s'éloigne de la fosse vers l'intérieur des terres."
            )
        ) as tracker:
            self.play(Create(axe_surface), FadeIn(label_surface), FadeIn(fosse_label), FadeIn(interieur_label))
            self.play(FadeIn(foyers_group))
            self.play(FadeIn(segments), FadeIn(prof_label))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        correction_ex3 = corrige_box(
            Text(
                _wrap(
                    "Les foyers s'alignent selon un plan incliné dont la "
                    "profondeur croît de la fosse vers l'intérieur des "
                    "terres : c'est un plan de Wadati-Benioff, signature "
                    "d'une subduction. La plaque océanique plonge vers "
                    "l'intérieur des terres (vers l'Est si la fosse longe "
                    "la côte ouest du continent), sous la plaque "
                    "continentale.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        correction_ex3.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Correction : les foyers s'alignent selon un plan incliné "
                "dont la profondeur croît de la fosse vers l'intérieur des "
                "terres. C'est un plan de Wadati-Benioff, signature "
                "caractéristique d'une subduction. La plaque océanique "
                "plonge vers l'intérieur des terres, vers l'Est si la fosse "
                "longe la côte ouest du continent, sous la plaque "
                "continentale."
            )
        ) as tracker:
            self.play(FadeIn(correction_ex3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(correction_ex3))

        # --- Exemple traité : méthodes et astuces --------------------------------
        entete_methodes = Text("Méthodes et astuces", font_size=27, color=YELLOW, weight="BOLD")
        entete_methodes.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(text="Récapitulons trois méthodes utiles pour ce chapitre.") as tracker:
            self.play(FadeIn(entete_methodes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_methodes))

        m1 = method_box(
            Text(
                _wrap(
                    "Méthode 1 — Calculer une vitesse d'expansion ou de "
                    "dérive : 1. relever d et t. 2. v = d/t. 3. convertir "
                    "(1 km/Ma = 1 mm/an = 0,1 cm/an). 4. distinguer "
                    "demi-vitesse (un flanc) et vitesse totale (= 2 × "
                    "demi-vitesse).",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        m1.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Méthode un : calculer une vitesse d'expansion ou de "
                "dérive. Un, relever la distance d et l'âge t. Deux, "
                "calculer v égale d sur t. Trois, convertir les unités : un "
                "kilomètre par mégaannée égale un millimètre par an, égale "
                "zéro virgule un centimètre par an. Quatre, bien distinguer "
                "la demi-vitesse, celle d'un seul flanc de la dorsale, de "
                "la vitesse d'expansion totale, qui vaut deux fois la "
                "demi-vitesse."
            )
        ) as tracker:
            self.play(FadeIn(m1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m1))

        m2 = method_box(
            Text(
                _wrap(
                    "Méthode 2 — Exploiter un profil d'anomalies "
                    "magnétiques : repérer l'axe (bande la plus jeune, au "
                    "centre) ; vérifier la symétrie des bandes ; associer "
                    "chaque bande à son âge ; si l'on mesure la distance "
                    "entre deux bandes symétriques de même âge, diviser "
                    "par 2 avant de calculer la vitesse.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        m2.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Méthode deux : exploiter un profil d'anomalies "
                "magnétiques. Repérer l'axe, la bande la plus jeune, au "
                "centre ; vérifier la symétrie des bandes ; associer chaque "
                "bande à son âge ; et si l'on mesure la distance entre deux "
                "bandes symétriques du même âge, ne pas oublier de diviser "
                "cette distance par deux avant de calculer la vitesse."
            )
        ) as tracker:
            self.play(FadeIn(m2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m2))

        m3 = method_box(
            Text(
                _wrap(
                    "Méthode 3 — Démarche APC d'analyse de documents en "
                    "SVT : observer et décrire les faits → comparer → "
                    "dégager une régularité ou une anomalie → formuler une "
                    "interprétation → conclure en répondant au problème "
                    "posé. Toujours justifier chaque réponse par un élément "
                    "précis du document.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        m3.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Méthode trois : la démarche APC d'analyse de documents en "
                "SVT. Observer et décrire les faits, comparer, dégager une "
                "régularité ou une anomalie, formuler une interprétation, "
                "puis conclure en répondant au problème posé. Toujours "
                "justifier chaque réponse par un élément précis du "
                "document."
            )
        ) as tracker:
            self.play(FadeIn(m3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m3))

        # --- Pièges à éviter -------------------------------------------------------
        entete_pieges = Text("Les pièges à éviter", font_size=26, color=YELLOW, weight="BOLD")
        entete_pieges.next_to(titre, DOWN, buff=0.45)

        pieges = _bullets(
            [
                "Confondre dérive des continents (hypothèse de Wegener, "
                "sans mécanisme valable) et expansion océanique (mécanisme "
                "découvert dans les années 1960, qui explique la "
                "première).",
                "Croire que les limites de plaques suivent les côtes : "
                "elles passent au milieu des océans, le long des fosses, "
                "ou au sein des continents.",
                "Affirmer que tous les volcans se trouvent aux frontières "
                "de plaques : les points chauds (Hawaï, Cameroun) "
                "produisent un volcanisme intraplaque.",
                "Dans un calcul de vitesse, utiliser la distance totale "
                "entre deux bandes symétriques avec la demi-vitesse "
                "(oublier de diviser par 2).",
                "Attribuer la formation de l'Himalaya à une subduction : "
                "c'est une collision continent-continent, sans "
                "volcanisme.",
            ],
            font_size=18,
            width=54,
        )
        pieges.next_to(entete_pieges, DOWN, buff=0.3)

        piege_box = warning_box(pieges, box_width=12.6)
        piege_box.next_to(titre, DOWN, buff=0.5)

        _bas_visible_p = -config.frame_height / 2 + 0.3
        _hauteur_dispo_p = piege_box.get_top()[1] - _bas_visible_p
        if piege_box.height > _hauteur_dispo_p:
            piege_box.scale(_hauteur_dispo_p / piege_box.height, about_point=piege_box.get_top())
            piege_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Cinq pièges à éviter absolument. Un : confondre la dérive "
                "des continents, l'hypothèse de Wegener sans mécanisme "
                "valable, et l'expansion océanique, le mécanisme découvert "
                "dans les années mille neuf cent soixante, qui explique la "
                "première. Deux : croire que les limites de plaques "
                "suivent les côtes ; elles passent au milieu des océans, le "
                "long des fosses, ou au sein même des continents. Trois : "
                "affirmer que tous les volcans se trouvent aux frontières "
                "de plaques ; les points chauds, comme Hawaï ou la ligne "
                "volcanique du Cameroun, produisent un volcanisme "
                "intraplaque. Quatre : dans un calcul de vitesse, utiliser "
                "la distance totale entre deux bandes symétriques avec la "
                "demi-vitesse, en oubliant de diviser par deux. Cinq : "
                "attribuer la formation de l'Himalaya à une subduction ; "
                "c'est en réalité une collision continent-continent, sans "
                "aucun volcanisme."
            )
        ) as tracker:
            self.play(FadeIn(entete_pieges))
            self.wait(0.3)
            self.play(FadeOut(entete_pieges))
            self.play(FadeIn(piege_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_box))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) ------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Les plaques lithosphériques glissent sur "
                    "l'asthénosphère (pas de flottaison sur un océan de "
                    "magma).",
                    "Wegener (1912) : dérive des continents, arguments "
                    "géométriques, géologiques, paléontologiques, "
                    "paléoclimatiques — mais aucun mécanisme valable.",
                    "Hess (1962) puis Vine et Matthews (1963) : expansion "
                    "océanique confirmée par les anomalies magnétiques "
                    "symétriques et l'âge croissant des fonds océaniques.",
                    "Trois frontières : dorsale (divergence, accrétion), "
                    "subduction et collision (convergence), faille "
                    "transformante (coulissage).",
                    "Moteurs : convection mantellique, poussée des "
                    "dorsales, et surtout traction des plaques plongeantes "
                    "(slab pull).",
                    "Séismes et volcans dessinent les limites de plaques ; "
                    "la Côte d'Ivoire, au cœur de la plaque africaine, est "
                    "une zone stable.",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si le contenu dépasse la hauteur visible malgré le
        # petit corps de police, on réduit l'échelle globale de la boîte
        # (voir SVT_FonctionsGonades_09).
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. Les plaques lithosphériques "
                "glissent sur l'asthénosphère, elles ne flottent pas sur un "
                "océan de magma. Wegener, en dix-neuf cent douze, propose "
                "la dérive des continents, avec des arguments géométriques, "
                "géologiques, paléontologiques et paléoclimatiques, mais "
                "sans mécanisme valable. Hess, en dix-neuf cent "
                "soixante-deux, puis Vine et Matthews, en dix-neuf cent "
                "soixante-trois, confirment l'expansion océanique grâce aux "
                "anomalies magnétiques symétriques et à l'âge croissant des "
                "fonds océaniques. On distingue trois types de frontières : "
                "la dorsale, en divergence, avec accrétion ; la subduction "
                "et la collision, en convergence ; et la faille "
                "transformante, en coulissage. Les moteurs de ces "
                "mouvements sont la convection mantellique, la poussée des "
                "dorsales, et surtout la traction des plaques plongeantes. "
                "Enfin, séismes et volcans dessinent les limites de "
                "plaques : la Côte d'Ivoire, au cœur de la plaque "
                "africaine, reste une zone stable."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
