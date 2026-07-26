"""
scenes/SVT_ActivitesInternesGlobe_07.py — Chapitre 6 (1ereD, SVT), scène 07.

§ 6.3.3 Lithosphère et asthénosphère (découpage mécanique) + § 6.4.1 De la
dérive des continents (Wegener, Pangée, arguments, exemple du Mesosaurus)
à l'expansion océanique (Harry Hess).
Source : 1ereD/SVT.pdf, pages 80-81.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Rectangle,
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


class LithosphereEtDeriveDesContinents(NotionScene):
    def construct(self):
        titre = scene_title("6.3.3 / 6.4.1 — Lithosphère et dérive des continents")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : un second découpage, mécanique cette fois -------------
        intro = Text(
            _wrap(
                "Le découpage croûte-manteau-noyau repose sur la "
                "composition chimique. Un second découpage se fonde sur le "
                "comportement mécanique (rigidité) : lithosphère et "
                "asthénosphère.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le découpage en croûte, manteau et noyau repose sur la "
                "composition chimique des roches. Il existe un second "
                "découpage, fondé cette fois sur le comportement mécanique, "
                "la rigidité : c'est la distinction entre lithosphère et "
                "asthénosphère."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        definition = definition_box(
            Text(
                _wrap(
                    "La lithosphère : enveloppe externe rigide, réunit "
                    "croûte et partie supérieure du manteau, jusqu'à ~100 "
                    "km. C'est elle qui se rompt lors des séismes. "
                    "L'asthénosphère : partie du manteau sous la "
                    "lithosphère, roches très chaudes partiellement "
                    "fondues, se déforment plastiquement comme du mastic.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La lithosphère est l'enveloppe externe rigide : elle "
                "réunit la croûte et la partie supérieure du manteau, "
                "jusqu'à environ cent kilomètres de profondeur. C'est elle "
                "qui se rompt lors des séismes. L'asthénosphère est la "
                "partie du manteau située sous la lithosphère : des roches "
                "très chaudes, partiellement fondues à quelques pour cent, "
                "qui se déforment plastiquement, comme du mastic."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma lithosphère / asthénosphère --
        litho = Rectangle(width=6.0, height=0.7, color=WHITE, fill_color="#288073", fill_opacity=0.9)
        astheno = Rectangle(width=6.0, height=1.6, color=WHITE, fill_color="#A42A5A", fill_opacity=0.5)
        astheno.next_to(litho, DOWN, buff=0)
        manteau_profond = Rectangle(width=6.0, height=0.8, color=WHITE, fill_color="#8B5A2B", fill_opacity=0.9)
        manteau_profond.next_to(astheno, DOWN, buff=0)
        pile = VGroup(litho, astheno, manteau_profond)
        pile.move_to(DOWN * 0.3)

        label_litho = Text("Lithosphère rigide (~100 km)\ncroûte + manteau supérieur", font_size=17, color=WHITE)
        label_litho.next_to(litho, UP, buff=0.2)
        label_astheno = Text("Asthénosphère plastique\n(la lithosphère « glisse » dessus)", font_size=16, color=WHITE)
        label_astheno.move_to(astheno.get_center())
        label_manteau_profond = Text("Manteau plus profond", font_size=15, color=WHITE)
        label_manteau_profond.move_to(manteau_profond.get_center())

        schema = VGroup(pile, label_litho, label_astheno, label_manteau_profond)
        schema.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sur ce schéma, la fine bande rigide du haut est la "
                "lithosphère : croûte et manteau supérieur soudés, sur "
                "environ cent kilomètres. En dessous, la bande rose est "
                "l'asthénosphère, plastique comme du mastic : la "
                "lithosphère peut y flotter et y glisser lentement, comme "
                "un radeau sur une pâte molle. Plus bas encore, le manteau "
                "redevient plus rigide sous l'effet de la pression."
            )
        ) as tracker:
            self.play(FadeIn(litho), FadeIn(label_litho))
            self.play(FadeIn(astheno), FadeIn(label_astheno))
            self.play(FadeIn(manteau_profond), FadeIn(label_manteau_profond))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Suite du raisonnement : Wegener et la Pangée --------------------
        wegener = Text(
            _wrap(
                "En 1912, Alfred Wegener publie l'hypothèse : les continents "
                "se déplacent, autrefois réunis en un supercontinent, la "
                "Pangée.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        wegener.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "En mille neuf cent douze, le météorologue allemand Alfred "
                "Wegener publie une hypothèse audacieuse : les continents se "
                "déplacent, et ils étaient autrefois réunis en un seul "
                "supercontinent, qu'il baptise la Pangée."
            )
        ) as tracker:
            self.play(FadeIn(wegener))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(wegener))

        entete_arg = Text("Les arguments de Wegener", font_size=26, color=YELLOW, weight="BOLD")
        entete_arg.next_to(titre, DOWN, buff=0.5)
        arguments = _bullets(
            [
                "Morphologique : les côtes d'Amérique du Sud et d'Afrique s'emboîtent.",
                "Paléontologique : mêmes fossiles (Mesosaurus) de part et d'autre de l'Atlantique sud.",
                "Paléoclimatique : traces de glaciers identiques en Afrique du Sud, en Inde, en Australie.",
                "Géologique : chaînes de montagnes et roches identiques se prolongent d'un continent à l'autre.",
            ],
            width=50,
        )
        arguments.next_to(entete_arg, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatre arguments soutiennent cette hypothèse. Argument "
                "morphologique : les côtes de l'Amérique du Sud et de "
                "l'Afrique s'emboîtent presque parfaitement. Argument "
                "paléontologique : on retrouve les mêmes fossiles, comme le "
                "Mesosaurus, de part et d'autre de l'Atlantique sud. "
                "Argument paléoclimatique : des traces de glaciers "
                "identiques en Afrique du Sud, en Inde et en Australie. "
                "Argument géologique : des chaînes de montagnes et des "
                "roches identiques se prolongent d'un continent à l'autre."
            )
        ) as tracker:
            self.play(FadeIn(entete_arg))
            self.play(FadeIn(arguments))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_arg), FadeOut(arguments))

        # --- Exemple traité : le témoignage du Mesosaurus ---------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Le Mesosaurus, reptile d'eau douce, fossiles datés "
                    "~280 Ma trouvés uniquement en Amérique du Sud est et "
                    "Afrique sud-ouest. Il ne pouvait pas traverser 4000 km "
                    "d'océan salé. Que conclure ?",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : le témoignage du Mesosaurus. Ce reptile "
                "d'eau douce, dont les fossiles datent d'environ deux cent "
                "quatre-vingts millions d'années, n'a été trouvé qu'en deux "
                "endroits : l'est de l'Amérique du Sud et le sud-ouest de "
                "l'Afrique. Il ne pouvait absolument pas traverser quatre "
                "mille kilomètres d'océan salé. Que peut-on en conclure ?"
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        # petit schéma : deux blocs qui s'emboîtent, avec fossiles communs
        bloc_sa = VGroup(
            Rectangle(width=1.3, height=1.0, color=WHITE, fill_color="#288073", fill_opacity=0.9),
            Text("Amérique\ndu Sud", font_size=14, color=WHITE),
        )
        bloc_sa[1].move_to(bloc_sa[0].get_center())
        fossile_sa = Dot(bloc_sa[0].get_right() + LEFT * 0.15, color=YELLOW)

        bloc_af = VGroup(
            Rectangle(width=1.3, height=1.0, color=WHITE, fill_color="#DE7C1F", fill_opacity=0.9),
            Text("Afrique", font_size=14, color=WHITE),
        )
        bloc_af[1].move_to(bloc_af[0].get_center())
        fossile_af = Dot(bloc_af[0].get_left() + RIGHT * 0.15, color=YELLOW)

        paire = VGroup(bloc_sa, fossile_sa, bloc_af, fossile_af).arrange(RIGHT, buff=0.05)
        paire.next_to(exemple, DOWN, buff=0.4)

        conclusion_ex = Text(
            "Conclusion : les deux continents étaient réunis, puis séparés par la dérive.",
            font_size=19,
            color=YELLOW,
        )
        conclusion_ex.next_to(paire, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Conclusion : les deux continents étaient réunis à "
                "l'époque du Mesosaurus ; la dérive les a ensuite séparés, "
                "emportant chacun sa moitié de la population de reptiles "
                "fossilisés."
            )
        ) as tracker:
            self.play(FadeIn(paire))
            self.play(FadeIn(conclusion_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(paire), FadeOut(conclusion_ex))

        # --- À retenir : de Wegener à l'expansion océanique (Hess) -----------
        hess = Text(
            _wrap(
                "À retenir : la théorie de Wegener est rejetée car il ne "
                "propose aucun mécanisme. Dans les années 1960, on découvre "
                "que les dorsales fabriquent en permanence de la nouvelle "
                "croûte océanique (tapis roulant) : c'est la théorie de "
                "l'expansion océanique de Harry Hess, avec deux preuves : "
                "l'âge des roches augmente en s'éloignant de l'axe, et les "
                "aimantations fossiles dessinent des bandes symétriques.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        hess.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "À retenir : la théorie de Wegener est d'abord rejetée par "
                "la communauté scientifique, car il ne propose aucun "
                "mécanisme capable de déplacer des continents entiers. Il "
                "faut attendre les années mille neuf cent soixante pour "
                "découvrir que les dorsales fabriquent en permanence de la "
                "nouvelle croûte océanique : le magma basaltique remonte, "
                "se solidifie, et est poussé de part et d'autre, comme un "
                "tapis roulant. Deux preuves confirment ce mécanisme : "
                "l'âge des roches augmente à mesure qu'on s'éloigne de "
                "l'axe de la dorsale, et les aimantations fossiles dessinent "
                "des bandes symétriques de part et d'autre. C'est la "
                "théorie de l'expansion océanique, proposée par Harry Hess."
            )
        ) as tracker:
            self.play(FadeIn(hess))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(hess))

        # --- Piège à éviter : lithosphère n'est pas synonyme de croûte -------
        piege = warning_box(
            Text(
                _wrap(
                    "La lithosphère contient la croûte plus la partie "
                    "rigide du manteau supérieur — ce n'est pas un synonyme "
                    "de croûte. Épaisseur totale : ~100 km sous les océans, "
                    "parfois plus sous les vieux continents.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention, piège fréquent : ne dites jamais que "
                "lithosphère est synonyme de croûte. La lithosphère "
                "contient la croûte, plus la partie rigide du manteau "
                "supérieur ; son épaisseur totale avoisine cent kilomètres "
                "sous les océans, parfois davantage sous les vieux "
                "continents."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
