"""
scenes/SVT_Photosynthese_15.py — Chapitre 10 (1ereC, SVT), scène 15.

§ 10.7 Rôle de la photosynthèse : source de toute matière organique
(producteurs primaires, chaînes alimentaires ivoiriennes, énergies
fossiles) + équilibre gazeux de la planète (effet de serre, forêts/
phytoplancton = pompes à carbone, méthode point clé équilibre
photosynthèse/respiration, déforestation) + applications pratiques
(agriculture sous serre, dates de semis, reboisement/mangroves) +
méthodes et astuces (3 méthodes, 3 pièges, astuce mnémotechnique) puis
L'ESSENTIEL DU CHAPITRE (clôture).
Source : 1ereC/SVT.pdf, pages 114-118.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class RoleDeLaPhotosyntheseEtEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("10.7 — Rôle de la photosynthèse et essentiel du chapitre")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : source de toute matière organique -----------------------
        source = Text(
            _wrap(
                "Les végétaux chlorophylliens transforment chaque année "
                "des milliards de tonnes de CO2 en matière organique : "
                "ce sont les producteurs primaires. Toute chaîne "
                "alimentaire commence par un végétal chlorophyllien : "
                "l'attiéké, le riz, l'igname, le cacao ou le café "
                "ivoiriens ne sont que de la matière organique fabriquée "
                "par photosynthèse. Les énergies fossiles (charbon, "
                "pétrole) sont elles-mêmes issues d'organismes "
                "photosynthétiques anciens.",
                width=56,
            ),
            font_size=20,
            color=WHITE,
        )
        source.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, mesurons l'importance de la "
                "photosynthèse. Les végétaux chlorophylliens "
                "transforment chaque année des milliards de tonnes de "
                "CO2 en matière organique : ce sont les producteurs "
                "primaires. Les consommateurs et les décomposeurs se "
                "nourrissent, directement ou indirectement, de cette "
                "matière organique. Toute chaîne alimentaire commence "
                "donc par un végétal chlorophyllien : l'attiéké, le riz, "
                "l'igname, le cacao ou le café ivoiriens ne sont que de "
                "la matière organique fabriquée par photosynthèse. Même "
                "les énergies fossiles, charbon et pétrole, sont issues "
                "d'organismes photosynthétiques anciens."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(source))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(source))

        # --- Animation du raisonnement : équilibre gazeux de la planète ------
        equilibre_texte = Text(
            _wrap(
                "La photosynthèse absorbe du CO2 et rejette de l'O2 : "
                "elle régule la composition de l'atmosphère et limite "
                "l'effet de serre. Les grandes forêts (parc national de "
                "Taï) et le phytoplancton des océans sont de véritables "
                "« pompes à carbone » — le phytoplancton fournit à lui "
                "seul environ la moitié de l'O2 planétaire.",
                width=56,
            ),
            font_size=19,
            color=WHITE,
        )
        equilibre_texte.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La photosynthèse joue aussi un rôle majeur dans "
                "l'équilibre gazeux de la planète : elle absorbe du CO2 "
                "et rejette de l'O2, indispensable à la respiration de "
                "la quasi-totalité des êtres vivants, tout en limitant "
                "l'augmentation de l'effet de serre. Les grandes forêts, "
                "comme le parc national de Taï en Côte d'Ivoire, ou la "
                "forêt amazonienne, ainsi que le phytoplancton des "
                "océans, sont de véritables pompes à carbone. Le "
                "phytoplancton marin fournit à lui seul environ la "
                "moitié de l'oxygène planétaire."
            )
        ) as tracker:
            self.play(FadeIn(equilibre_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equilibre_texte))

        methode_equilibre = method_box(
            Text(
                _wrap(
                    "Point clé : à l'échelle de la planète, la "
                    "photosynthèse consomme du CO2 et produit de l'O2 ; "
                    "la respiration (et la combustion) consomment de "
                    "l'O2 et produisent du CO2. Ces deux processus, "
                    "globalement inverses, maintiennent l'équilibre "
                    "gazeux de l'atmosphère. La déforestation et les "
                    "combustions fossiles rompent cet équilibre.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=12.2,
        )
        methode_equilibre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenez ce point clé : à l'échelle de la planète, la "
                "photosynthèse consomme du CO2 et produit de l'O2 ; la "
                "respiration, et la combustion, consomment de l'O2 et "
                "produisent du CO2. Ces deux grands processus, "
                "globalement inverses, maintiennent l'équilibre gazeux "
                "de l'atmosphère. La déforestation et les combustions "
                "d'énergies fossiles rompent cet équilibre : le CO2 "
                "s'accumule, c'est l'effet de serre."
            )
        ) as tracker:
            self.play(FadeIn(methode_equilibre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_equilibre))

        # --- Exemple traité : applications pratiques ----------------------------
        applications = _bullets(
            [
                "Agriculture sous serre : enrichissement en CO2, "
                "éclairage d'appoint, contrôle de la température "
                "(tomates, piments à Bingerville ou Azaguié).",
                "Choix des dates de semis et densités de plantation "
                "pour optimiser l'interception de la lumière (maïs, "
                "riz pluvial).",
                "Lutte contre le réchauffement : reboisement, "
                "protection des mangroves, car la photosynthèse stocke "
                "le carbone dans la biomasse.",
            ],
            font_size=19,
            width=54,
        )
        applications.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Ces connaissances ont des applications pratiques bien "
                "concrètes. En agriculture sous serre : enrichissement "
                "en CO2, éclairage d'appoint, contrôle de la "
                "température, pour maximiser les rendements de tomates "
                "ou de piments, à Bingerville ou à Azaguié. Le choix des "
                "dates de semis et des densités de plantation, pour "
                "optimiser l'interception de la lumière, sur le maïs ou "
                "le riz pluvial. Et la lutte contre le réchauffement "
                "climatique, par le reboisement et la protection des "
                "mangroves, car la photosynthèse stocke le carbone dans "
                "la biomasse."
            )
        ) as tracker:
            self.play(FadeIn(applications))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(applications))

        # --- À retenir : méthodes et astuces --------------------------------------
        methodes = method_box(
            _bullets(
                [
                    "Méthode 1 : écrire/équilibrer l'équation (réactifs, "
                    "produits, conditions au-dessus de la flèche, puis "
                    "C, H, O dans cet ordre).",
                    "Méthode 2 : analyser une expérience avec témoin (4 "
                    "questions : variable ? témoin/expérimental ? "
                    "résultats ? conclusion sur la variable ?).",
                    "Méthode 3 : exploiter une courbe (axes/unités, "
                    "point de compensation, plateau de saturation, "
                    "facteur limitant par zone).",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.4,
        )
        methodes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résumons les trois méthodes à maîtriser pour l'examen. "
                "Méthode un : écrire et équilibrer l'équation bilan, en "
                "plaçant les réactifs, les produits, les conditions "
                "au-dessus de la flèche, puis en équilibrant dans "
                "l'ordre carbone, hydrogène, oxygène. Méthode deux : "
                "analyser une expérience avec témoin, en répondant "
                "toujours à quatre questions : quelle est la variable, "
                "quel est le témoin, quels sont les résultats, quelle "
                "conclusion en tirer. Méthode trois : exploiter une "
                "courbe de photosynthèse, en identifiant les axes, le "
                "point de compensation, le plateau de saturation, et le "
                "facteur limitant dans chaque zone."
            )
        ) as tracker:
            self.play(FadeIn(methodes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methodes))

        # --- Piège à éviter : les trois pièges classiques du chapitre --------
        pieges = warning_box(
            _bullets(
                [
                    "Piège 1 : l'O2 dégagé ne vient PAS du CO2, mais de "
                    "la photolyse de l'eau.",
                    "Piège 2 : « phase sombre » ne veut pas dire « la "
                    "nuit » — elle se déroule le jour, avec la phase "
                    "claire.",
                    "Piège 3 : la chlorophylle n'est ni un réactif ni "
                    "un produit (au-dessus de la flèche uniquement) ; "
                    "la plante respire jour ET nuit.",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.4,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Et rappelons les trois pièges les plus fréquents. "
                "Piège un : l'O2 dégagé ne vient jamais du CO2, mais "
                "toujours de la photolyse de l'eau. Piège deux : « phase "
                "sombre » ne signifie pas « phase de la nuit » — elle se "
                "déroule le jour, en même temps que la phase claire, "
                "dont elle dépend. Piège trois : la chlorophylle n'est "
                "ni un réactif ni un produit de l'équation bilan, elle "
                "apparaît seulement au-dessus de la flèche ; et la "
                "plante respire jour et nuit, alors qu'elle ne "
                "photosynthétise qu'à la lumière. Astuce mnémotechnique "
                "pour l'ordre d'équilibrage : « Charivari Hilarant "
                "Orgiaque », pour Carbone, puis Hydrogène, puis Oxygène."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges))

        # --- L'ESSENTIEL DU CHAPITRE (clôture) ------------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Photosynthèse : 6CO2+6H2O -(lumière,chlorophylle)-> "
                    "C6H12O6+6O2, dans les chloroplastes des cellules "
                    "chlorophylliennes.",
                    "Phase claire (thylakoïdes) : photolyse de l'eau -> "
                    "O2 + ATP + NADPH,H+ (l'O2 vient de l'EAU, pas du "
                    "CO2).",
                    "Phase sombre (stroma, cycle de Calvin) : la "
                    "Rubisco fixe le CO2 sur le RuBP -> PGA -> PGAL -> "
                    "glucose (6 tours = 1 glucose).",
                    "Mise en évidence : dégagement d'O2 (élodée "
                    "éclairée) et test à l'eau iodée (amidon), toujours "
                    "avec un lot témoin.",
                    "Facteurs limitants : lumière et CO2 (point de "
                    "compensation -> saturation), température (courbe "
                    "en cloche, optimum 25-30°C), eau, sels minéraux.",
                    "Rôle : seule source de matière organique du monde "
                    "vivant (producteurs primaires) et régulation de "
                    "l'équilibre gazeux (CO2/O2) de la planète.",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si le contenu dépasse la hauteur visible du cadre, on
        # réduit l'échelle globale de la boîte pour qu'elle tienne à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.25
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. La photosynthèse "
                "s'écrit : six CO2 plus six eau, avec lumière et "
                "chlorophylle, donnent un glucose plus six O2, dans les "
                "chloroplastes des cellules chlorophylliennes. La phase "
                "claire, dans les thylakoïdes, réalise la photolyse de "
                "l'eau et produit O2, ATP et NADPH,H plus — retenez bien "
                "que l'oxygène vient de l'eau, jamais du CO2. La phase "
                "sombre, dans le stroma, c'est le cycle de Calvin : la "
                "Rubisco fixe le CO2 sur le RuBP, ce qui donne du PGA, "
                "puis du PGAL, puis du glucose, au terme de six tours de "
                "cycle. La mise en évidence expérimentale repose sur le "
                "dégagement d'O2 par une élodée éclairée et le test à "
                "l'eau iodée sur l'amidon, toujours avec un lot témoin. "
                "Les facteurs limitants sont la lumière et le CO2, avec "
                "un point de compensation puis un point de saturation, "
                "la température, avec une courbe en cloche et un "
                "optimum vers vingt-cinq à trente degrés, ainsi que "
                "l'eau et les sels minéraux. Enfin, la photosynthèse est "
                "la seule source de matière organique du monde vivant, "
                "et elle régule l'équilibre gazeux, CO2 et O2, de toute "
                "la planète."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
