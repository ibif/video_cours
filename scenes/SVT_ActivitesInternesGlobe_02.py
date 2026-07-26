"""
scenes/SVT_ActivitesInternesGlobe_02.py — Chapitre 6 (1ereD, SVT), scène 02.

§ 6.1.1-6.1.2 Le volcanisme : définition, vocabulaire (magma, lave,
chambre magmatique, cheminée, cône), produits d'une éruption selon leur
état, puis les deux grands types d'éruptions (effusive / explosive),
tableau comparatif et exemple du Nyiragongo (2021).
Source : 1ereD/SVT.pdf, page 77-78.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LeVolcanismeDefinitionEtTypesEruptions(NotionScene):
    def construct(self):
        titre = scene_title("6.1 — Le volcanisme : définition et types")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : du gradient géothermique au magma --------------------
        intro = Text(
            _wrap(
                "Le gradient géothermique est d'environ 3°C tous les 100 m "
                "près de la surface. À quelques dizaines de km de "
                "profondeur, certaines roches fondent partiellement : un "
                "magma se forme, plus léger que les roches solides, qui "
                "remonte lentement.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le gradient géothermique est d'environ trois degrés tous "
                "les cent mètres, près de la surface. À quelques dizaines de "
                "kilomètres de profondeur, certaines roches fondent "
                "partiellement : il se forme un magma, plus léger que les "
                "roches solides environnantes, qui remonte lentement. Quand "
                "il trouve un chemin jusqu'à l'air libre, c'est l'éruption "
                "volcanique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        definition = definition_box(
            Text(
                _wrap(
                    "Le volcanisme est l'ensemble des phénomènes liés à la "
                    "remontée des magmas depuis l'intérieur de la Terre et à "
                    "leur dégagement à la surface. Un volcan est un relief "
                    "construit par l'accumulation des produits d'un "
                    "volcanisme, autour d'une ouverture appelée cratère.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le volcanisme est l'ensemble des phénomènes liés à la "
                "remontée des magmas depuis l'intérieur de la Terre et à "
                "leur dégagement à la surface. Un volcan est un relief "
                "construit par l'accumulation des produits d'un volcanisme, "
                "autour d'une ouverture appelée cratère."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma d'un volcan et vocabulaire -
        base_left = LEFT * 1.9 + DOWN * 1.1
        base_right = RIGHT * 1.9 + DOWN * 1.1
        top_left = LEFT * 0.35 + UP * 1.7
        top_right = RIGHT * 0.35 + UP * 1.7
        cone = Polygon(base_left, top_left, top_right, base_right, color=WHITE, fill_color="#7A6A55", fill_opacity=0.9)

        cratere = Line(top_left, top_right, color=RED, stroke_width=6)
        chambre = Ellipse(width=1.6, height=0.9, color=RED, fill_color=RED, fill_opacity=0.85)
        chambre.move_to(DOWN * 2.4)
        cheminee = Line(chambre.get_top(), (top_left + top_right) / 2, color=ORANGE, stroke_width=8)

        volcan = VGroup(chambre, cheminee, cone, cratere)
        volcan.move_to(LEFT * 3.3 + DOWN * 0.2)

        label_cratere = Text("Cratère", font_size=20, color=WHITE)
        label_cratere.next_to(volcan, UP, buff=0.7).shift(LEFT * 0.9)
        arrow_cratere = Arrow(label_cratere.get_bottom(), cratere.get_center(), buff=0.1, color=WHITE)

        label_cone = Text("Cône volcanique\n(laves + projections)", font_size=17, color=WHITE)
        label_cone.next_to(volcan, RIGHT, buff=1.6).shift(UP * 1.2)
        arrow_cone = Arrow(label_cone.get_left(), cone.get_right(), buff=0.1, color=WHITE)

        label_cheminee = Text("Cheminée\n(conduit du magma)", font_size=17, color=ORANGE)
        label_cheminee.next_to(volcan, RIGHT, buff=1.6)
        arrow_cheminee = Arrow(label_cheminee.get_left(), cheminee.get_center(), buff=0.1, color=ORANGE)

        label_chambre = Text("Chambre magmatique\n(réservoir de magma)", font_size=17, color=RED)
        label_chambre.next_to(volcan, RIGHT, buff=1.6).shift(DOWN * 1.6)
        arrow_chambre = Arrow(label_chambre.get_left(), chambre.get_right(), buff=0.1, color=RED)

        schema = VGroup(
            volcan, label_cratere, arrow_cratere, label_cone, arrow_cone,
            label_cheminee, arrow_cheminee, label_chambre, arrow_chambre,
        )
        schema.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le magma, roche en fusion en profondeur chargée en gaz "
                "dissous, s'accumule dans un réservoir souterrain, la "
                "chambre magmatique. Il remonte par un conduit, la "
                "cheminée, qui relie la chambre magmatique au cratère, "
                "l'ouverture au sommet. L'ensemble des laves et projections "
                "accumulées forme le cône volcanique."
            )
        ) as tracker:
            self.play(FadeIn(volcan))
            self.play(FadeIn(label_cratere), FadeIn(arrow_cratere))
            self.play(FadeIn(label_cone), FadeIn(arrow_cone))
            self.play(FadeIn(label_cheminee), FadeIn(arrow_cheminee))
            self.play(FadeIn(label_chambre), FadeIn(arrow_chambre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        produits = _bullets(
            [
                "État gazeux : vapeur d'eau (majoritaire), CO₂, SO₂, H₂S — panache volcanique.",
                "État liquide : laves fluides ou visqueuses — coulées, lacs de lave, dômes.",
                "État solide : cendres fines, lapilli, bombes et blocs — projections, nuées ardentes.",
            ],
            width=52,
        )
        entete_produits = Text("Les produits d'une éruption", font_size=26, color=YELLOW, weight="BOLD")
        entete_produits.next_to(titre, DOWN, buff=0.5)
        produits.next_to(entete_produits, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une éruption libère des produits sous trois états. À l'état "
                "gazeux : vapeur d'eau majoritaire, dioxyde de carbone, "
                "dioxyde de soufre, sulfure d'hydrogène, qui forment le "
                "panache volcanique. À l'état liquide : des laves fluides ou "
                "visqueuses, qui forment coulées, lacs de lave ou dômes. À "
                "l'état solide : cendres fines, lapilli, bombes et blocs, "
                "projetés lors des explosions ou emportés dans des nuées "
                "ardentes."
            )
        ) as tracker:
            self.play(FadeIn(entete_produits))
            self.play(FadeIn(produits))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_produits), FadeOut(produits))

        # --- Suite du raisonnement : les deux grands types d'éruptions -----
        types_def = definition_box(
            Text(
                _wrap(
                    "Éruption effusive : magma très chaud (~1200°C), pauvre "
                    "en silice, fluide, laisse les gaz s'échapper facilement "
                    "— produit surtout des coulées de lave. Éruption "
                    "explosive : magma moins chaud (~800-900°C), riche en "
                    "silice, visqueux, emprisonne les gaz — la pression fait "
                    "éclater le magma.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        types_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux grands types d'éruptions dépendent de la nature du "
                "magma. L'éruption effusive : un magma très chaud, environ "
                "mille deux cents degrés, pauvre en silice, donc fluide, qui "
                "laisse les gaz s'échapper facilement et produit surtout des "
                "coulées de lave. L'éruption explosive : un magma moins "
                "chaud, environ huit cents à neuf cents degrés, riche en "
                "silice, donc visqueux, qui emprisonne les gaz ; la pression "
                "monte jusqu'à faire éclater le magma, projetant cendres, "
                "blocs et nuées ardentes, des nuages brûlants à plus de "
                "cent kilomètres par heure."
            )
        ) as tracker:
            self.play(FadeIn(types_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(types_def))

        # Tableau comparatif effusive / explosive
        effusive_titre = Text("Éruption effusive", font_size=23, color=YELLOW, weight="BOLD")
        effusive_lignes = _bullets(
            [
                "Magma fluide, pauvre en silice",
                "Coulées de lave dominantes",
                "Cône large et plat (bouclier)",
                "Ex : Nyiragongo, Erta Ale, Hawaï",
            ],
            font_size=18,
            width=32,
        )
        effusive = VGroup(effusive_titre, effusive_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        explosive_titre = Text("Éruption explosive", font_size=23, color=YELLOW, weight="BOLD")
        explosive_lignes = _bullets(
            [
                "Magma visqueux, riche en silice",
                "Cendres, bombes, nuées ardentes",
                "Cône raide et élevé (stratovolcan)",
                "Ex : montagne Pelée, Vésuve",
            ],
            font_size=18,
            width=32,
        )
        explosive = VGroup(explosive_titre, explosive_lignes).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        tableau = VGroup(effusive, explosive).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        tableau.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "En résumé : l'éruption effusive, à magma fluide pauvre en "
                "silice, produit surtout des coulées de lave et bâtit un "
                "cône large et plat, dit bouclier, comme le Nyiragongo, "
                "l'Erta Ale ou les volcans d'Hawaï. L'éruption explosive, à "
                "magma visqueux riche en silice, produit cendres, bombes et "
                "nuées ardentes, et bâtit un cône raide et élevé, dit "
                "stratovolcan, comme la montagne Pelée ou le Vésuve."
            )
        ) as tracker:
            self.play(FadeIn(effusive))
            self.play(FadeIn(explosive))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Exemple traité : identifier le type de l'éruption du Nyiragongo 2021 --
        exemple = example_box(
            Text(
                _wrap(
                    "Mai 2021 : le Nyiragongo entre en éruption. Une lave "
                    "noire très liquide jaillit de fissures et s'écoule "
                    "rapidement jusqu'aux faubourgs de Goma, sans grande "
                    "explosion ni panache de cendres. Quel type d'éruption ?",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : en mai deux mille vingt et un, le "
                "Nyiragongo entre en éruption. Une lave noire très liquide "
                "jaillit de fissures et s'écoule rapidement jusqu'aux "
                "faubourgs de Goma, sans grande explosion ni panache de "
                "cendres. Quel type d'éruption reconnaît-on ?"
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        resolution = Text(
            _wrap(
                "Résolution : lave fluide, écoulement en coulées, absence "
                "d'explosion → magma pauvre en silice, gaz séparés "
                "facilement → éruption effusive, cohérente avec le rift "
                "est-africain.",
                width=52,
            ),
            font_size=22,
            color=YELLOW,
        )
        resolution.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Résolution : une lave fluide, un écoulement en coulées, "
                "l'absence de grande explosion — cela signe un magma pauvre "
                "en silice, dont les gaz se séparent facilement. C'est donc "
                "une éruption effusive, cohérente avec la position du "
                "Nyiragongo sur le rift est-africain."
            )
        ) as tracker:
            self.play(FadeIn(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(resolution))

        # --- À retenir : le mont Cameroun, un volcan mixte ------------------
        remarque = Text(
            _wrap(
                "À retenir : le mont Cameroun a des éruptions généralement "
                "effusives, avec parfois des phases explosives modérées — "
                "on parle de volcan « mixte ». Il fait partie de la « ligne "
                "du Cameroun ».",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        remarque.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le mont Cameroun a des éruptions généralement "
                "effusives, avec parfois des phases explosives modérées ; on "
                "parle de volcan mixte. Il fait partie d'un ensemble appelé "
                "la ligne du Cameroun, que nous retrouverons plus loin dans "
                "ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Piège à éviter : ne pas confondre magma et lave ----------------
        piege = warning_box(
            Text(
                _wrap(
                    "Erreur fréquente : « la lave sort de la chambre "
                    "magmatique ». Non : c'est le magma qui remonte par la "
                    "cheminée ; il ne devient lave qu'une fois arrivé à la "
                    "surface. Phrase-bilan : le magma est en dessous, la "
                    "lave est au-dessus.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre magma et lave. Erreur "
                "fréquente : dire que la lave sort de la chambre "
                "magmatique. C'est faux : c'est le magma qui remonte par la "
                "cheminée ; il ne devient lave qu'une fois arrivé à la "
                "surface. Retenez la phrase-bilan : le magma est en "
                "dessous, la lave est au-dessus."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
