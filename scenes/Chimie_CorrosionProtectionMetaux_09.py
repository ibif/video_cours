"""
scenes/Chimie_CorrosionProtectionMetaux_09.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 09 (dernière du chapitre).

§ 9. Coût économique, enjeux et synthèse. Enjeux économiques (environ un
quart de la production mondiale d'acier perdue à la corrosion), enjeux
infrastructures (ponts, pipelines, carrosseries, navires), contexte
ivoirien (air marin lagune Ébrié, golfe de Guinée, ponts d'Abidjan, port
autonome). method_box × 3 (interpréter une expérience de corrosion,
établir l'équation-bilan d'une corrosion humide, choisir un procédé de
protection). warning_box × 4 (étain ne protège pas le fer même rayé,
c'est l'inverse du zinc ; rouille = Fe2O3, xH2O et non FeO/Fe3O4, non
protectrice ; n(Mg) = n(Fe) et non 2×n(Fe) ; rouiller ≠ brûler, voie
humide à froid vs voie sèche). essentiel_box récapitulatif final du
chapitre.
Source : synthèse du chapitre 15, 1ereC/Chimie.pdf, pages 144-152.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


class EnjeuxMethodesPiegesEssentielCorrosion(NotionScene):
    def construct(self):
        titre = scene_title("15.9 Enjeux, méthodes, pièges et essentiel")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : enjeux économiques et infrastructures -----------------------
        entete_enjeux = Text("Un enjeu économique considérable", font_size=22, color=YELLOW, weight="BOLD")
        entete_enjeux.next_to(titre, DOWN, buff=0.35)

        enjeux = _bullets(
            [
                "environ un quart de la production mondiale d'acier est perdue chaque année à la corrosion",
                "infrastructures menacées : ponts, pipelines, carrosseries, navires",
                "Côte d'Ivoire : air marin de la lagune Ébrié et du golfe de Guinée, ponts d'Abidjan, port autonome",
            ],
            font_size=19,
        )
        enjeux.next_to(entete_enjeux, DOWN, buff=0.3)
        groupe_enjeux = VGroup(entete_enjeux, enjeux)
        _fit(groupe_enjeux, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "La corrosion n'est pas qu'une curiosité de laboratoire : "
                "c'est un enjeu économique considérable. On estime "
                "qu'environ un quart de la production mondiale d'acier "
                "est perdue chaque année à cause de la corrosion. De "
                "nombreuses infrastructures sont menacées : ponts, "
                "pipelines, carrosseries de véhicules, navires. En Côte "
                "d'Ivoire, l'air marin de la lagune Ébrié et du golfe de "
                "Guinée rend cette menace particulièrement présente pour "
                "les ponts d'Abidjan et les installations du port "
                "autonome, qui nécessitent une protection renforcée et "
                "un entretien constant."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(groupe_enjeux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_enjeux))

        # --- Raisonnement / exemple traité : 3 method_box --------------------------
        methode1 = method_box(
            Text(
                _wrap(
                    "Méthode — Interpréter une expérience de corrosion : "
                    "identifier ce que chaque tube isole ou supprime "
                    "(eau ? air/O2 ?) ; comparer les observations deux à "
                    "deux ; conclure sur la ou les conditions "
                    "nécessaires.",
                    width=46,
                ),
                font_size=21,
            ),
        )
        methode1.next_to(titre, DOWN, buff=0.4)
        _fit(methode1, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Première méthode à maîtriser : interpréter une "
                "expérience de corrosion. Il faut identifier précisément "
                "ce que chaque tube témoin isole ou supprime — l'eau, ou "
                "le dioxygène de l'air — comparer les observations deux "
                "à deux, puis conclure sur la ou les conditions "
                "réellement nécessaires à la corrosion."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            Text(
                _wrap(
                    "Méthode — Établir l'équation-bilan d'une corrosion "
                    "humide : écrire la demi-équation d'oxydation du "
                    "métal à l'anode, la demi-équation de réduction du "
                    "dioxygène à la cathode, puis équilibrer les "
                    "électrons échangés pour obtenir le bilan global.",
                    width=46,
                ),
                font_size=20,
            ),
        )
        methode2.next_to(titre, DOWN, buff=0.4)
        _fit(methode2, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Deuxième méthode : établir l'équation-bilan d'une "
                "corrosion humide. On écrit la demi-équation d'oxydation "
                "du métal à l'anode, la demi-équation de réduction du "
                "dioxygène à la cathode, puis on équilibre soigneusement "
                "le nombre d'électrons échangés entre les deux "
                "demi-équations pour obtenir le bilan global, comme nous "
                "l'avons fait pour la rouille du fer."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            Text(
                _wrap(
                    "Méthode — Choisir un procédé de protection : "
                    "comparer la position du métal de revêtement par "
                    "rapport au fer dans la classification "
                    "électrochimique. Plus réducteur (Zn, Mg) → protection "
                    "cathodique, efficace même rayée. Moins réducteur "
                    "(Sn, Cu, Cr) → barrière seule, efficace si intacte.",
                    width=46,
                ),
                font_size=19,
            ),
        )
        methode3.next_to(titre, DOWN, buff=0.4)
        _fit(methode3, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Troisième méthode : choisir un procédé de protection "
                "adapté. Il suffit de comparer la position du métal de "
                "revêtement par rapport au fer dans la classification "
                "électrochimique. S'il est plus réducteur, comme le "
                "zinc ou le magnésium, on obtient une protection "
                "cathodique, efficace même rayée. S'il est moins "
                "réducteur, comme l'étain, le cuivre ou le chrome, on "
                "n'obtient qu'une barrière, efficace seulement tant "
                "qu'elle reste intacte."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Pièges à éviter : 4 warning_box -----------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 : l'étain (étamage) NE protège PAS le fer "
                    "une fois rayé — c'est l'exact inverse du zinc "
                    "(galvanisation), qui protège même rayé, car l'étain "
                    "est MOINS réducteur que le fer.",
                    width=46,
                ),
                font_size=20,
            ),
        )
        piege1.next_to(titre, DOWN, buff=0.4)
        _fit(piege1, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Premier piège à éviter : l'étain, dans l'étamage, ne "
                "protège pas le fer une fois rayé. C'est exactement "
                "l'inverse du zinc dans la galvanisation, qui lui "
                "protège même rayé, car l'étain est moins réducteur que "
                "le fer, alors que le zinc est plus réducteur."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            VGroup(
                Text(
                    "Piège 2 : la rouille est Fe2O3, xH2O — jamais FeO ni",
                    font_size=20,
                ),
                Text(
                    "Fe3O4 — et elle NE protège PAS le fer (poreuse, non adhérente).",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.15),
        )
        piege2.next_to(titre, DOWN, buff=0.4)
        _fit(piege2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Deuxième piège : la rouille est l'oxyde de fer trois "
                "hydraté, F-e-deux-O-trois, x H-deux-O — jamais F-e-O ni "
                "F-e-trois-O-quatre, qui sont d'autres oxydes de fer. Et "
                "surtout, elle ne protège absolument pas le fer, "
                "puisqu'elle est poreuse et non adhérente."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            MathTex(
                r"\text{Piège 3 : } n(Mg) = n(Fe) \quad (\text{et non } 2\times n(Fe))",
                font_size=25,
            ),
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège, dans les calculs d'anode sacrificielle : "
                "la quantité de matière de magnésium consommée est égale "
                "à celle du fer protégé, n de magnésium égale n de fer, "
                "et non le double, puisque magnésium et fer cèdent "
                "chacun exactement deux électrons par atome."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            Text(
                _wrap(
                    "Piège 4 : rouiller n'est pas brûler. La corrosion "
                    "est une oxydation lente par voie humide, à froid "
                    "(eau + O2) ; la combustion est une oxydation rapide "
                    "par voie sèche, avec flamme — deux phénomènes bien "
                    "distincts.",
                    width=46,
                ),
                font_size=20,
            ),
        )
        piege4.next_to(titre, DOWN, buff=0.4)
        _fit(piege4, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Quatrième et dernier piège : rouiller n'est pas brûler. "
                "La corrosion est une oxydation lente par voie humide, à "
                "froid, nécessitant de l'eau et du dioxygène ensemble ; "
                "la combustion, elle, est une oxydation rapide par voie "
                "sèche, avec flamme, comme le fer qui brûle dans le "
                "dioxygène pur. Ce sont deux phénomènes bien distincts, "
                "à ne surtout pas confondre."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- À retenir : essentiel_box récapitulatif final du chapitre ---------------
        essentiel = essentiel_box(
            Text(
                _wrap(
                    "La corrosion est l'oxydation lente d'un métal par "
                    "l'air humide (eau + O2 nécessaires simultanément). "
                    "Le fer forme une rouille Fe2O3, xH2O poreuse et non "
                    "protectrice, via des micropiles (anode : Fe → Fe2+ "
                    "+ 2e- ; cathode : O2 + 2H2O + 4e- → 4OH-). On s'en "
                    "protège par revêtements (efficaces si intacts) ou "
                    "par métallisation avec un métal plus réducteur "
                    "(Zn, Mg — protection cathodique, efficace même "
                    "rayée). Enjeu économique et infrastructurel majeur, "
                    "particulièrement sensible en Côte d'Ivoire du fait "
                    "de l'air marin.",
                    width=50,
                ),
                font_size=20,
            ),
        )
        essentiel.next_to(titre, DOWN, buff=0.4)
        _fit(essentiel, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de ce chapitre, et du programme de "
                "chimie de cette année. La corrosion est l'oxydation "
                "lente d'un métal par l'air humide, nécessitant à la "
                "fois de l'eau et du dioxygène. Le fer forme une "
                "rouille, oxyde de fer trois hydraté, poreuse et non "
                "protectrice, via des micropiles où le fer s'oxyde à "
                "l'anode tandis que le dioxygène se réduit à la "
                "cathode. On s'en protège par des revêtements, efficaces "
                "seulement s'ils restent intacts, ou par métallisation "
                "avec un métal plus réducteur, zinc ou magnésium, qui "
                "offre une protection cathodique efficace même rayée. "
                "C'est un enjeu économique et infrastructurel majeur, "
                "particulièrement sensible en Côte d'Ivoire du fait de "
                "l'air marin qui borde nos côtes et notre lagune."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
