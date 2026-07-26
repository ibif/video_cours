"""
scenes/SVT_MouvementsPlaques_06.py — Chapitre 7 (1ereD, SVT), scène 06.

§ 7.3.1-7.3.2 La divergence (accrétion océanique, rift continental,
exemple du rift est-africain) et la convergence (subduction, collision,
attention à bien choisir, exemple Andes vs Himalaya).
Source : 1ereD/SVT.pdf, pages 95-96.
"""

import textwrap

from manim import (
    BLUE_E,
    DOWN,
    GRAY_C,
    GRAY_D,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Polygon,
    Rectangle,
    Text,
    Triangle,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _schema_rift():
    """Continent étiré, failles, dépression centrale : rift continental."""
    socle = Rectangle(width=7.5, height=0.9, fill_color=ORANGE, fill_opacity=0.7, stroke_color=WHITE, stroke_width=1)
    fosse = Polygon(
        [-0.9, 0.45, 0], [0.9, 0.45, 0], [0.5, -0.1, 0], [-0.5, -0.1, 0],
        fill_color=RED, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1,
    )
    fosse.move_to(socle.get_top() + DOWN * 0.15)

    fleche_g = Arrow(start=[-0.5, 0.6, 0], end=[-2.0, 0.6, 0], color=WHITE, buff=0, stroke_width=3)
    fleche_d = Arrow(start=[0.5, 0.6, 0], end=[2.0, 0.6, 0], color=WHITE, buff=0, stroke_width=3)

    label = Text("rift : dépression + failles", font_size=15, color=WHITE)
    label.next_to(fosse, DOWN, buff=0.35)

    return VGroup(socle, fosse, fleche_g, fleche_d, label)


def _schema_subduction():
    """Plaque océanique plongeant sous une plaque continentale : fosse, volcan."""
    continent = Polygon(
        [-3.0, -0.4, 0], [0.5, -0.4, 0], [0.5, 0.6, 0], [-1.0, 1.1, 0], [-3.0, 0.6, 0],
        fill_color=ORANGE, fill_opacity=0.85, stroke_color=WHITE, stroke_width=1,
    )
    ocean_plaque = Polygon(
        [0.5, -0.4, 0], [3.2, -0.1, 0], [3.2, -0.9, 0], [0.5, -1.6, 0],
        fill_color=GRAY_D, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1,
    )
    fosse = Text("fosse", font_size=14, color=WHITE).move_to([0.7, -0.05, 0])

    volcan = Triangle(fill_color=RED, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1)
    volcan.set(width=0.6, height=0.6)
    volcan.move_to([-1.2, 1.25, 0])
    label_volcan = Text("volcan explosif", font_size=13, color=RED).next_to(volcan, UP, buff=0.08)

    fleche_plongee = Arrow(
        start=[0.7, -0.2, 0], end=[2.3, -1.4, 0], color=YELLOW, buff=0, stroke_width=4
    )
    label_plongee = Text("plongée (subduction)", font_size=13, color=YELLOW)
    label_plongee.next_to(fleche_plongee, RIGHT, buff=0.05).shift(DOWN * 0.15)

    points_seismes = VGroup(*[
        Rectangle(width=0.06, height=0.06, fill_color=WHITE, fill_opacity=1, stroke_width=0).move_to(pt)
        for pt in [[0.9, -0.3, 0], [1.3, -0.6, 0], [1.7, -0.95, 0], [2.1, -1.3, 0]]
    ])
    label_seismes = Text("séismes de + en + profonds", font_size=12, color=WHITE)
    label_seismes.next_to(points_seismes, DOWN, buff=0.15)

    return VGroup(
        continent, ocean_plaque, fosse, volcan, label_volcan,
        fleche_plongee, label_plongee, points_seismes, label_seismes,
    )


def _schema_collision():
    """Deux lithosphères continentales plissées : chaîne de montagnes sans volcan."""
    plaque_g = Polygon(
        [-3.2, -0.3, 0], [-0.3, -0.3, 0], [-0.6, 0.5, 0], [-3.2, 0.5, 0],
        fill_color=ORANGE, fill_opacity=0.85, stroke_color=WHITE, stroke_width=1,
    )
    plaque_d = Polygon(
        [3.2, -0.3, 0], [0.3, -0.3, 0], [0.6, 0.5, 0], [3.2, 0.5, 0],
        fill_color="#C98A3C", fill_opacity=0.85, stroke_color=WHITE, stroke_width=1,
    )
    chaine = Polygon(
        [-0.6, 0.5, 0], [-0.2, 1.6, 0], [0.15, 1.0, 0], [0.35, 1.7, 0], [0.6, 0.5, 0],
        fill_color=GRAY_C, fill_opacity=0.95, stroke_color=WHITE, stroke_width=1,
    )
    label_chaine = Text("chaîne de montagnes (plissée)", font_size=13, color=WHITE)
    label_chaine.next_to(chaine, UP, buff=0.15)

    fleche_g = Arrow(start=[-2.0, 0.75, 0], end=[-0.9, 0.75, 0], color=WHITE, buff=0, stroke_width=3)
    fleche_d = Arrow(start=[2.0, 0.75, 0], end=[0.9, 0.75, 0], color=WHITE, buff=0, stroke_width=3)

    label_pas_volcan = Text("pas de volcanisme", font_size=13, color=RED)
    label_pas_volcan.next_to(chaine, DOWN, buff=1.0)

    return VGroup(plaque_g, plaque_d, chaine, label_chaine, fleche_g, fleche_d, label_pas_volcan)


class DivergenceConvergence(NotionScene):
    def construct(self):
        titre = scene_title("7.3 — Divergence et convergence")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : divergence et accrétion océanique -----------------------
        definition_diverg = definition_box(
            Text(
                _wrap(
                    "Deux plaques divergent lorsqu'elles s'écartent. L'espace "
                    "créé est comblé par la remontée de matériau mantellique "
                    "chaud qui se solidifie : nouvelle lithosphère océanique. "
                    "Ce processus est l'accrétion océanique. En domaine "
                    "océanique, marquée par une dorsale ; en domaine "
                    "continental, par un rift.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        definition_diverg.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étudions maintenant les trois façons dont deux plaques "
                "voisines peuvent se comporter l'une par rapport à "
                "l'autre. D'abord, la divergence : deux plaques divergent "
                "lorsqu'elles s'écartent l'une de l'autre. L'espace ainsi "
                "créé est comblé par la remontée de matériau mantellique "
                "chaud, qui se solidifie en nouvelle lithosphère océanique. "
                "Ce processus s'appelle l'accrétion océanique. En domaine "
                "océanique, cette divergence est marquée par une dorsale ; "
                "en domaine continental, elle est marquée par un rift."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_diverg))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_diverg))

        definition_rift = definition_box(
            Text(
                _wrap(
                    "Un rift est une dépression allongée bordée de failles, "
                    "s'ouvrant dans un continent étiré et aminci. Il annonce, "
                    "si l'étirement se poursuit sur des dizaines de Ma, la "
                    "rupture du continent et la naissance d'un nouvel océan.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition_rift.next_to(titre, DOWN, buff=0.5)

        schema_rift = _schema_rift()
        schema_rift.next_to(definition_rift, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un rift est une dépression allongée bordée de failles, "
                "qui s'ouvre dans un continent étiré et aminci. Il annonce, "
                "si l'étirement se poursuit pendant des dizaines de "
                "millions d'années, la rupture complète du continent et la "
                "naissance d'un nouvel océan."
            )
        ) as tracker:
            self.play(FadeIn(definition_rift))
            self.play(FadeIn(schema_rift))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_rift), FadeOut(schema_rift))

        # --- Animation du raisonnement : exemple du rift est-africain ---------
        exemple_rift = example_box(
            Text(
                _wrap(
                    "Le rift est-africain s'étend de la mer Rouge au "
                    "Mozambique, plus de 4000 km. Les deux rives s'écartent "
                    "de quelques mm/an ; lacs Tanganyika et Nyasa occupent des "
                    "fossés effondrés ; volcans (Kilimandjaro, mont Kenya) "
                    "bordent la dépression. Comparable à l'étirement qui a "
                    "précédé l'ouverture de l'Atlantique il y a ~130 Ma. Si le "
                    "mouvement se poursuit, l'Afrique de l'Est se détachera : "
                    "un océan en gestation.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.0,
        )
        exemple_rift.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'Afrique nous offre un exemple grandeur nature : le rift "
                "est-africain, qui s'étend de la mer Rouge jusqu'au "
                "Mozambique, sur plus de quatre mille kilomètres. Ses deux "
                "rives s'écartent de quelques millimètres par an ; les lacs "
                "Tanganyika et Nyasa occupent des fossés effondrés ; des "
                "volcans, comme le Kilimandjaro et le mont Kenya, bordent "
                "la dépression. Cette situation est comparable à "
                "l'étirement qui a précédé l'ouverture de l'océan "
                "Atlantique, il y a environ cent trente millions d'années. "
                "Si ce mouvement se poursuit, l'Afrique de l'Est finira par "
                "se détacher du reste du continent : le rift est-africain "
                "est un véritable océan en gestation."
            )
        ) as tracker:
            self.play(FadeIn(exemple_rift))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_rift))

        # --- Convergence : subduction et collision ------------------------------
        definition_converg = definition_box(
            Text(
                _wrap(
                    "Deux plaques convergent lorsqu'elles se rapprochent. Le "
                    "destin dépend de la nature de la lithosphère : "
                    "subduction (lithosphère océanique dense plonge sous une "
                    "autre plaque et disparaît dans le manteau) ou collision "
                    "(deux lithosphères continentales, trop légères pour "
                    "plonger, se rencontrent et se déforment).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        definition_converg.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Passons maintenant à la convergence : deux plaques "
                "convergent lorsqu'elles se rapprochent l'une de l'autre. "
                "Mais leur destin dépend alors de la nature de la "
                "lithosphère en présence : c'est soit la subduction, quand "
                "une lithosphère océanique, dense, plonge sous une autre "
                "plaque et disparaît dans le manteau ; soit la collision, "
                "quand deux lithosphères continentales, trop légères pour "
                "plonger, se rencontrent et se déforment."
            )
        ) as tracker:
            self.play(FadeIn(definition_converg))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_converg))

        definition_subd = definition_box(
            Text(
                _wrap(
                    "Subduction : enfoncement d'une plaque océanique dans le "
                    "manteau sous une autre plaque. Manifestations : fosse "
                    "océanique (jusqu'à 10 000 m), séismes de profondeur "
                    "croissante vers le continent, volcanisme explosif "
                    "aligné parallèlement à la fosse (la plaque plongeante "
                    "chauffe, les roches hydratées fondent partiellement, le "
                    "magma remonte).",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=12.0,
        )
        definition_subd.next_to(titre, DOWN, buff=0.5)

        schema_subd = _schema_subduction()
        schema_subd.scale(0.9)
        schema_subd.next_to(definition_subd, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La subduction est l'enfoncement d'une plaque océanique "
                "dans le manteau, sous une autre plaque. Elle se manifeste "
                "par une fosse océanique, pouvant atteindre dix mille "
                "mètres de profondeur, par des séismes dont la profondeur "
                "augmente en s'éloignant de la fosse vers le continent, et "
                "par un volcanisme explosif, aligné parallèlement à la "
                "fosse : la plaque plongeante chauffe, ses roches "
                "hydratées fondent partiellement, et le magma produit "
                "remonte jusqu'en surface."
            )
        ) as tracker:
            self.play(FadeIn(definition_subd))
            self.play(FadeIn(schema_subd))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_subd), FadeOut(schema_subd))

        definition_collision = definition_box(
            Text(
                _wrap(
                    "Collision : rencontre de deux lithosphères continentales "
                    "après disparition complète de l'océan séparateur. Les "
                    "roches, trop légères pour plonger, se plissent et se "
                    "chevauchent : chaîne de montagnes. Pas de volcanisme, "
                    "mais forts séismes superficiels.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        definition_collision.next_to(titre, DOWN, buff=0.5)

        schema_coll = _schema_collision()
        schema_coll.next_to(definition_collision, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La collision, elle, résulte de la rencontre de deux "
                "lithosphères continentales, après la disparition complète "
                "de l'océan qui les séparait. Les roches continentales, "
                "trop légères pour plonger dans le manteau, se plissent et "
                "se chevauchent : c'est ainsi que naît une chaîne de "
                "montagnes. Pas de volcanisme dans ce cas, mais de forts "
                "séismes superficiels."
            )
        ) as tracker:
            self.play(FadeIn(definition_collision))
            self.play(FadeIn(schema_coll))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_collision), FadeOut(schema_coll))

        # --- Piège à éviter : subduction ou collision ? ------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Fosse océanique + volcans alignés + séismes profonds = "
                    "subduction ; haute chaîne de montagnes + absence de "
                    "volcans + séismes superficiels = collision. Écrire "
                    "« subduction » pour l'Himalaya est une erreur grave : "
                    "c'est une chaîne de collision.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à bien choisir entre les deux : fosse "
                "océanique, volcans alignés et séismes profonds signent "
                "une subduction ; haute chaîne de montagnes, absence de "
                "volcans et séismes superficiels signent une collision. "
                "Écrire « subduction » à propos de l'Himalaya est une "
                "erreur grave : c'est bien une chaîne de collision."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : exemple Andes vs Himalaya ------------------------------
        exemple_final = example_box(
            Text(
                _wrap(
                    "Andes : fosse du Pérou-Chili (>8000 m), volcans andins "
                    "alignés, séismes de + en + profonds vers l'est → la "
                    "plaque de Nazca subducte sous la plaque sud-américaine, "
                    "chaîne de subduction. Himalaya : ni fosse ni volcan au "
                    "nord de l'Inde, mais les plus hauts sommets (Everest, "
                    "8849 m) et séismes superficiels violents → plaque "
                    "indo-australienne en collision avec la plaque "
                    "eurasiatique depuis ~50 Ma, chaîne de collision.",
                    width=54,
                ),
                font_size=17,
            ),
            box_width=12.0,
        )
        exemple_final.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comparons deux convergences bien différentes. Les Andes : "
                "la fosse du Pérou-Chili dépasse huit mille mètres de "
                "profondeur, des volcans andins s'alignent le long de la "
                "chaîne, et les séismes deviennent de plus en plus profonds "
                "vers l'est. Conclusion : la plaque de Nazca subducte sous "
                "la plaque sud-américaine, c'est une chaîne de subduction. "
                "L'Himalaya, maintenant : ni fosse, ni volcan au nord de "
                "l'Inde, mais les plus hauts sommets du monde, dont "
                "l'Everest et ses huit mille huit cent quarante-neuf "
                "mètres, et de violents séismes superficiels. Conclusion : "
                "la plaque indo-australienne est en collision avec la "
                "plaque eurasiatique depuis environ cinquante millions "
                "d'années, c'est une chaîne de collision."
            )
        ) as tracker:
            self.play(FadeIn(exemple_final))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(exemple_final))
