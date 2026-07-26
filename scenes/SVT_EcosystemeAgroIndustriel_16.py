"""
scenes/SVT_EcosystemeAgroIndustriel_16.py — Chapitre 11 (1ereC, SVT), scène 16.

§ 9 Les impacts des activités humaines : déforestation (chiffres Côte
d'Ivoire, causes, conséquences, mesures), pollution (engrais/pesticides,
eutrophisation, pollution industrielle), érosion (mécanisme, lutte), puis
conclusion du chapitre (propriété de synthèse), méthodes et astuces (3
méthodes + 4 pièges), et enfin L'ESSENTIEL DU CHAPITRE (clôture du
programme 1ereC SVT). Source : 1ereC/SVT.pdf, pages 132-133.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, property_box, scene_title, warning_box


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


class ImpactsHumainsEtEssentielDuChapitre(NotionScene):
    def construct(self):
        titre = scene_title("9 — Impacts humains, conclusion & essentiel")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : la déforestation en Côte d'Ivoire ---------------------------
        defo_titre = Text("La déforestation en Côte d'Ivoire", font_size=23, color=YELLOW, weight="BOLD")
        defo_titre.next_to(titre, DOWN, buff=0.4)
        defo = _bullets(
            [
                "16 millions d'hectares de forêt dense en 1960 → moins de 3 millions aujourd'hui.",
                "Causes : cultures de rente (cacao, café, palmier), exploitation du bois, feux de brousse, urbanisation.",
                "Conséquences : perte de biodiversité, perturbation des cycles du carbone et de l'eau, érosion, désertification.",
                "Mesures : aires protégées (Taï, Comoé), reboisement, agroforesterie, lutte contre l'orpaillage clandestin.",
            ],
            font_size=17,
            width=62,
        )
        defo.next_to(defo_titre, DOWN, buff=0.3)
        groupe_defo = VGroup(defo_titre, defo)
        _fit(groupe_defo, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Terminons ce chapitre, et ce programme de première C, par "
                "les impacts des activités humaines sur les écosystèmes. "
                "D'abord, la déforestation : la Côte d'Ivoire a perdu "
                "l'essentiel de son couvert forestier, de l'ordre de "
                "seize millions d'hectares de forêt dense à "
                "l'indépendance, en mille neuf cent soixante, il en "
                "resterait aujourd'hui moins de trois millions. Les causes "
                "principales : l'extension des cultures de rente, cacao, "
                "café, palmier, l'exploitation du bois, les feux de "
                "brousse, l'urbanisation. Les conséquences : disparition "
                "de la biodiversité, perturbation du cycle du carbone et "
                "du cycle de l'eau, érosion, appauvrissement des sols puis "
                "désertification. Les mesures de préservation : les aires "
                "protégées, comme le parc national de Taï ou celui de la "
                "Comoé, le reboisement, l'agroforesterie, la lutte contre "
                "l'orpaillage clandestin, et la sensibilisation des "
                "populations."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(defo_titre))
            self.play(FadeIn(defo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(defo_titre), FadeOut(defo))

        # --- Raisonnement : pollution et érosion -----------------------------------
        pollution_titre = Text("Pollution et érosion", font_size=23, color=YELLOW, weight="BOLD")
        pollution_titre.next_to(titre, DOWN, buff=0.4)
        pollution = _bullets(
            [
                "Pollution : lessivage des engrais/pesticides vers les nappes ; eutrophisation des étangs (algues → asphyxie des poissons) ; pollution industrielle et urbaine.",
                "Érosion : sur sol dénudé, les pluies emportent la couche fertile ; combattue par la couverture végétale, les haies, les courbes de niveau.",
            ],
            font_size=18,
            width=60,
        )
        pollution.next_to(pollution_titre, DOWN, buff=0.3)
        groupe_pollution = VGroup(pollution_titre, pollution)
        _fit(groupe_pollution, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Ensuite, la pollution des sols et des eaux par les "
                "engrais et pesticides mal utilisés : lessivage des "
                "nitrates vers les nappes phréatiques, accumulation "
                "d'insecticides dans les chaînes alimentaires. "
                "L'eutrophisation des étangs est un cas fréquent : "
                "l'excès d'engrais entraîne une prolifération d'algues, "
                "dont la décomposition épuise l'oxygène de l'eau et "
                "asphyxie les poissons. Il faut y ajouter la pollution "
                "industrielle et urbaine. Enfin, l'érosion : sur les sols "
                "dénudés, par déforestation, cultures sur pentes ou feux "
                "tardifs, les pluies tropicales emportent la couche "
                "fertile. On la combat par la couverture végétale "
                "permanente, les haies, les courbes de niveau et la "
                "limitation des feux."
            )
        ) as tracker:
            self.play(FadeIn(pollution_titre))
            self.play(FadeIn(pollution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pollution_titre), FadeOut(pollution))

        # --- Exemple traité : conclusion du chapitre (propriété de synthèse) ------
        conclusion = property_box(
            Text(
                _wrap(
                    "L'écosystème naturel fonctionne en circuit presque "
                    "fermé, grâce au recyclage de la matière et à la "
                    "complexité de ses réseaux trophiques. L'agrosystème, "
                    "simplifié et ouvert, offre de hauts rendements mais "
                    "dépend d'intrants coûteux et fragilise les "
                    "équilibres naturels. Le défi de la Côte d'Ivoire — "
                    "premier producteur mondial de cacao — est de "
                    "concilier production agricole et préservation des "
                    "écosystèmes.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=11.8,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la conclusion de ce chapitre. L'écosystème naturel "
                "fonctionne en circuit presque fermé, grâce au recyclage "
                "de la matière et à la complexité de ses réseaux "
                "trophiques. L'agrosystème, simplifié et ouvert, offre de "
                "hauts rendements, mais dépend d'intrants coûteux et "
                "fragilise les équilibres naturels. Le défi de la Côte "
                "d'Ivoire, premier producteur mondial de cacao, est de "
                "concilier production agricole et préservation des "
                "écosystèmes : c'est tout l'enjeu de l'agriculture "
                "durable."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- À retenir : méthodes et pièges ---------------------------------------
        methodes = method_box(
            _bullets(
                [
                    "Construire une chaîne/réseau : repérer les producteurs, classer C1/C2/C3, orienter les flèches (proie → prédateur).",
                    "Calculer un rendement : r = (En/En-1) × 100, vérifier qu'il reste entre 5 et 20 %.",
                    "Exploiter un document : lire les unités, identifier ce qui est demandé, justifier par une notion du cours.",
                ],
                font_size=17,
                width=60,
            ),
            box_width=12.0,
        )
        methodes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant l'essentiel du chapitre, trois méthodes à "
                "maîtriser pour l'épreuve. Un : pour construire une chaîne "
                "ou un réseau alimentaire, repérer d'abord les "
                "producteurs, classer les autres organismes en "
                "consommateurs primaires, secondaires, tertiaires, et "
                "orienter les flèches de la proie vers le prédateur. Deux "
                ": pour calculer un rendement écologique, appliquer r "
                "égale En sur En moins un, fois cent, et vérifier que le "
                "résultat reste cohérent, entre cinq et vingt pour cent en "
                "général. Trois : pour exploiter un document, lire "
                "d'abord la légende et les unités, repérer ce qui est "
                "demandé, décrire, comparer, calculer ou interpréter, et "
                "toujours justifier par une notion du cours."
            )
        ) as tracker:
            self.play(FadeIn(methodes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methodes))

        pieges = warning_box(
            _bullets(
                [
                    "L'énergie ne se recycle JAMAIS : elle circule à sens unique, seule la matière se recycle.",
                    "Ne pas confondre pyramide des nombres/biomasses (parfois renversée) et pyramide des énergies (toujours régulière).",
                    "Les plantes ne « puisent » pas leur nourriture dans le sol : elles la fabriquent par photosynthèse (le sol ne fournit que l'eau et les sels minéraux).",
                    "Sens des flèches : de l'organisme mangé vers l'organisme mangeur.",
                ],
                font_size=17,
                width=60,
            ),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Et quatre pièges classiques à éviter. Un : n'écrivez "
                "jamais que l'énergie se recycle, c'est faux, elle circule "
                "à sens unique ; seule la matière se recycle grâce aux "
                "décomposeurs. Deux : ne confondez pas la pyramide des "
                "nombres ou des biomasses, parfois renversée, avec la "
                "pyramide des énergies, toujours régulière. Trois "
                ": n'écrivez pas que les plantes puisent leur nourriture "
                "dans le sol ; les plantes vertes fabriquent elles-mêmes "
                "leur matière organique par photosynthèse, elles ne "
                "prélèvent dans le sol que de l'eau et des sels minéraux. "
                "Quatre : attention au sens des flèches, qui vont toujours "
                "de l'organisme mangé vers l'organisme mangeur."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges))

        # --- L'ESSENTIEL DU CHAPITRE (clôture du programme 1ereC SVT) -------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Écosystème = biotope (facteurs physico-chimiques) + biocénose (populations en relation) + interactions (Tansley, 1935).",
                    "Chaîne alimentaire : P → C1 → C2 → C3… ; réseau alimentaire : chaînes interconnectées, gage de stabilité.",
                    "Loi de Lindeman : le flux d'énergie est unidirectionnel et décroissant (80-95 % perdu à chaque niveau) ; seule la matière est recyclée.",
                    "Rendement écologique r = (En/En-1) × 100 ; pyramide des énergies toujours régulière.",
                    "Cycles du carbone et de l'azote : recyclage global de la matière entre atmosphère, êtres vivants et décomposeurs.",
                    "Équilibre dynamique + résilience (liée à la biodiversité) ; agrosystème = biocénose simplifiée, système ouvert, forte productivité mais non autorégulé.",
                    "Défi ivoirien : concilier agriculture durable (rotation, agroforesterie, engrais verts) et préservation face à la déforestation, la pollution et l'érosion.",
                ],
                font_size=16,
                width=62,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)
        _fit(essentiel, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Voici l'essentiel de ce dernier chapitre, et de tout le "
                "programme de sciences de la vie et de la Terre de "
                "première C. Un écosystème, c'est un biotope, les facteurs "
                "physico-chimiques, plus une biocénose, les populations "
                "d'êtres vivants en relation, plus leurs interactions, "
                "selon la définition de Tansley en mille neuf cent "
                "trente-cinq. Une chaîne alimentaire relie producteurs et "
                "consommateurs successifs ; un réseau alimentaire, "
                "formé de chaînes interconnectées, est un gage de "
                "stabilité. La loi de Lindeman nous rappelle que le flux "
                "d'énergie est unidirectionnel et décroissant, avec "
                "quatre-vingts à quatre-vingt-quinze pour cent perdus à "
                "chaque niveau, alors que seule la matière est recyclée. "
                "Le rendement écologique se calcule par r égale En sur En "
                "moins un fois cent, et la pyramide des énergies est "
                "toujours régulière. Les cycles du carbone et de l'azote "
                "assurent le recyclage global de la matière entre "
                "l'atmosphère, les êtres vivants et les décomposeurs. "
                "L'écosystème naturel vit en équilibre dynamique, avec une "
                "résilience liée à sa biodiversité, tandis que "
                "l'agrosystème, à la biocénose simplifiée et au système "
                "ouvert, offre une forte productivité mais ne peut pas "
                "s'autoréguler. Le grand défi de la Côte d'Ivoire est de "
                "concilier une agriculture durable, rotation culturale, "
                "agroforesterie, engrais verts, avec la préservation des "
                "écosystèmes, face à la déforestation, à la pollution et à "
                "l'érosion. Ceci conclut le programme de première C : "
                "félicitations pour ce parcours."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
