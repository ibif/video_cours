"""
scenes/SVT_HerediteMendelienne_13.py — Chapitre 6 (1ereC, SVT), scène 13.

§ VIII. Les arbres généalogiques : définition, conventions de
représentation (tableau des symboles), exemple commenté (arbre du
daltonisme sur 3 générations, lecture détaillée du « saut de
génération »), méthode d'analyse en 3 questions. Source : 1ereC/SVT.pdf,
pages 63-64.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLACK,
    Circle,
    Create,
    FadeIn,
    FadeOut,
    Line,
    Square,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _individu(kind="carre", atteint=False, side=0.5):
    """Symbole d'un individu : carré (homme) ou rond (femme), blanc si
    sain, plein (coloré) si atteint — conventions internationales."""
    couleur_remplissage = YELLOW if atteint else BLACK
    opacite = 1.0 if atteint else 0.0
    if kind == "carre":
        forme = Square(side_length=side, stroke_color=WHITE, stroke_width=3, fill_color=couleur_remplissage, fill_opacity=opacite)
    else:
        forme = Circle(radius=side / 2, stroke_color=WHITE, stroke_width=3, fill_color=couleur_remplissage, fill_opacity=opacite)
    return forme


class ArbresGenealogiques(NotionScene):
    def construct(self):
        titre = scene_title("6.13 — Les arbres généalogiques")
        titre.scale(0.72)
        titre.to_edge(UP)

        # --- Énoncé : la définition ------------------------------------------------
        def_arbre = definition_box(
            Text(
                _wrap(
                    "Un arbre généalogique est un schéma qui représente "
                    "les liens de parenté au sein d'une famille et la "
                    "répartition d'un caractère héréditaire sur plusieurs "
                    "générations.",
                    width=50,
                ),
                font_size=24,
            ),
            box_width=11.3,
        )
        def_arbre.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un arbre généalogique est un schéma qui représente les "
                "liens de parenté au sein d'une famille, et la "
                "répartition d'un caractère héréditaire sur plusieurs "
                "générations."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_arbre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_arbre))

        # --- Animation du raisonnement : les conventions de représentation --------
        entete_conv = Text("Conventions internationales de représentation", font_size=21, color=YELLOW, weight="BOLD")
        entete_conv.next_to(titre, DOWN, buff=0.45)

        def _ligne_convention(symbole, texte):
            t = Text(texte, font_size=19, color=WHITE)
            return VGroup(symbole, t).arrange(RIGHT, buff=0.4)

        homme_sain = _ligne_convention(_individu("carre", False), "Carré blanc : homme sain")
        homme_atteint = _ligne_convention(_individu("carre", True), "Carré plein : homme atteint")
        femme_saine = _ligne_convention(_individu("rond", False), "Rond blanc : femme saine")
        femme_atteinte = _ligne_convention(_individu("rond", True), "Rond plein : femme atteinte")

        col1 = VGroup(homme_sain, homme_atteint, femme_saine, femme_atteinte).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        trait_h = Line(LEFT * 0.4, RIGHT * 0.4, color=WHITE, stroke_width=3)
        trait_h_txt = _ligne_convention(trait_h, "Trait horizontal : union (couple)")
        trait_v = Line(UP * 0.3, DOWN * 0.3, color=WHITE, stroke_width=3)
        trait_v_txt = _ligne_convention(trait_v, "Trait vertical : descendance (filiation)")
        chiffres_txt = _ligne_convention(
            Text("I, II, III", font_size=19, color=WHITE), "Chiffres romains : générations successives"
        )

        col2 = VGroup(trait_h_txt, trait_v_txt, chiffres_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        conventions = VGroup(col1, col2).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        conventions.next_to(entete_conv, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un arbre généalogique suit des conventions "
                "internationales précises. Un carré blanc représente un "
                "homme sain ; un carré plein, coloré, représente un "
                "homme atteint. Un rond blanc représente une femme "
                "saine ; un rond plein représente une femme atteinte. Un "
                "trait horizontal entre deux individus indique une "
                "union, un couple ; un trait vertical indique une "
                "descendance, une filiation. Enfin, des chiffres romains, "
                "I, II, III, numérotent les générations successives."
            )
        ) as tracker:
            self.play(FadeIn(entete_conv))
            self.play(FadeIn(conventions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_conv), FadeOut(conventions))

        # --- Exemple traité : arbre du daltonisme sur 3 générations ---------------
        entete_ex = Text("Exemple : le daltonisme sur 3 générations", font_size=21, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.4)

        # Génération I
        i1 = _individu("carre", True).move_to([-1.3, 1.4, 0])
        i2 = _individu("rond", False).move_to([1.3, 1.4, 0])
        lab_i1 = Text("I-1", font_size=14, color=WHITE).next_to(i1, DOWN, buff=0.1)
        lab_i2 = Text("I-2", font_size=14, color=WHITE).next_to(i2, DOWN, buff=0.1)
        union_i = Line(i1.get_right(), i2.get_left(), color=WHITE, stroke_width=2)

        # Génération II
        ii1 = _individu("carre", False).move_to([-3.0, 0.0, 0])
        ii2 = _individu("rond", False).move_to([-1.0, 0.0, 0])
        ii3 = _individu("carre", False).move_to([1.3, 0.0, 0])
        lab_ii1 = Text("II-1", font_size=14, color=WHITE).next_to(ii1, DOWN, buff=0.1)
        lab_ii2 = Text("II-2", font_size=14, color=WHITE).next_to(ii2, DOWN, buff=0.1)
        lab_ii3 = Text("II-3", font_size=14, color=WHITE).next_to(ii3, DOWN, buff=0.1)
        union_ii = Line(ii1.get_right(), ii2.get_left(), color=WHITE, stroke_width=2)

        # Descente génération I -> II (via un bus horizontal au-dessus de II-2/II-3)
        milieu_i = (i1.get_center() + i2.get_center()) / 2
        bus_i_y = 0.75
        bus_i = Line([ii2.get_center()[0], bus_i_y, 0], [ii3.get_center()[0], bus_i_y, 0], color=WHITE, stroke_width=2)
        chute_i = Line(milieu_i, [milieu_i[0], bus_i_y, 0], color=WHITE, stroke_width=2)
        chute_ii2 = Line([ii2.get_center()[0], bus_i_y, 0], ii2.get_top(), color=WHITE, stroke_width=2)
        chute_ii3 = Line([ii3.get_center()[0], bus_i_y, 0], ii3.get_top(), color=WHITE, stroke_width=2)

        gen1 = VGroup(i1, i2, lab_i1, lab_i2, union_i)
        gen2 = VGroup(ii1, ii2, ii3, lab_ii1, lab_ii2, lab_ii3, union_ii)
        liens_i_ii = VGroup(bus_i, chute_i, chute_ii2, chute_ii3)

        rom_i = Text("I", font_size=20, color=YELLOW).move_to([-5.2, 1.4, 0])
        rom_ii = Text("II", font_size=20, color=YELLOW).move_to([-5.2, 0.0, 0])

        arbre_haut = VGroup(gen1, gen2, liens_i_ii, rom_i, rom_ii)
        arbre_haut.next_to(entete_ex, DOWN, buff=0.5).scale(0.85)

        with self.voiceover(
            text=(
                "Construisons l'arbre. En génération I, l'homme I-1 est "
                "daltonien, carré plein ; son épouse I-2 est saine, rond "
                "blanc. Leurs deux enfants apparaissent en génération II "
                ": II-2, une fille, et II-3, un fils. II-1 est l'époux de "
                "II-2, un homme sain qui rejoint la famille par mariage."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(rom_i), Create(i1), Create(i2), FadeIn(lab_i1), FadeIn(lab_i2), Create(union_i))
            self.play(Create(liens_i_ii))
            self.play(
                FadeIn(rom_ii),
                Create(ii1),
                Create(ii2),
                Create(ii3),
                FadeIn(lab_ii1),
                FadeIn(lab_ii2),
                FadeIn(lab_ii3),
                Create(union_ii),
            )
            self.wait(tracker.get_remaining_duration())

        # Génération III
        iii1 = _individu("carre", True, side=0.4).move_to([-2.4, -1.5, 0])
        iii2 = _individu("rond", False, side=0.4).move_to([-1.4, -1.5, 0])
        iii3 = _individu("carre", False, side=0.4).move_to([-0.4, -1.5, 0])
        lab_iii1 = Text("III-1", font_size=13, color=WHITE).next_to(iii1, DOWN, buff=0.1)
        lab_iii2 = Text("III-2", font_size=13, color=WHITE).next_to(iii2, DOWN, buff=0.1)
        lab_iii3 = Text("III-3", font_size=13, color=WHITE).next_to(iii3, DOWN, buff=0.1)

        milieu_ii = (ii1.get_center() + ii2.get_center()) / 2
        bus_ii_y = -0.75
        bus_ii = Line([iii1.get_center()[0], bus_ii_y, 0], [iii3.get_center()[0], bus_ii_y, 0], color=WHITE, stroke_width=2)
        chute_ii = Line(milieu_ii, [milieu_ii[0], bus_ii_y, 0], color=WHITE, stroke_width=2)
        chute_iii1 = Line([iii1.get_center()[0], bus_ii_y, 0], iii1.get_top(), color=WHITE, stroke_width=2)
        chute_iii2 = Line([iii2.get_center()[0], bus_ii_y, 0], iii2.get_top(), color=WHITE, stroke_width=2)
        chute_iii3 = Line([iii3.get_center()[0], bus_ii_y, 0], iii3.get_top(), color=WHITE, stroke_width=2)

        rom_iii = Text("III", font_size=20, color=YELLOW).move_to([-5.2, -1.5, 0])

        gen3 = VGroup(iii1, iii2, iii3, lab_iii1, lab_iii2, lab_iii3)
        liens_ii_iii = VGroup(bus_ii, chute_ii, chute_iii1, chute_iii2, chute_iii3)
        arbre_bas = VGroup(gen3, liens_ii_iii, rom_iii)
        arbre_bas.scale(0.85).next_to(arbre_haut, DOWN, buff=0.35).align_to(arbre_haut, LEFT).shift(RIGHT * 0.3)

        with self.voiceover(
            text=(
                "En génération III, le couple II-1 et II-2 a trois "
                "enfants : III-1, un garçon daltonien, carré plein, et "
                "ses frère et sœur, III-2 et III-3, tous deux sains. Le "
                "caractère daltonisme, absent chez II-1 et II-2 en "
                "apparence, ressort donc chez leur fils III-1."
            )
        ) as tracker:
            self.play(Create(liens_ii_iii))
            self.play(
                FadeIn(rom_iii),
                Create(iii1),
                Create(iii2),
                Create(iii3),
                FadeIn(lab_iii1),
                FadeIn(lab_iii2),
                FadeIn(lab_iii3),
            )
            self.wait(tracker.get_remaining_duration())

        lecture = Text(
            _wrap(
                "Le caractère « saute » une génération : il passe du "
                "grand-père (I-1) au petit-fils (III-1), via la mère "
                "conductrice II-2, non atteinte elle-même.",
                width=46,
            ),
            font_size=18,
            color=YELLOW,
        )
        lecture.next_to(arbre_bas, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Lisons cet arbre en détail. L'homme I-1 est daltonien, X "
                "d Y ; son épouse I-2 est saine et non conductrice, X D X "
                "D. Toutes leurs filles reçoivent X d du père et X D de "
                "la mère : elles sont donc saines conductrices, X D X d, "
                "comme II-2. Tous leurs fils reçoivent Y du père et X D "
                "de la mère : ils sont sains, X D Y, comme II-3. La "
                "conductrice II-2, unie à l'homme sain II-1, peut alors "
                "avoir des garçons daltoniens, la moitié de ses garçons "
                "en moyenne : c'est le cas de III-1. Le caractère semble "
                "donc sauter une génération : il passe du grand-père au "
                "petit-fils, par l'intermédiaire de la mère conductrice, "
                "qui n'est elle-même pas atteinte."
            )
        ) as tracker:
            self.play(FadeIn(lecture))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_ex),
            FadeOut(arbre_haut),
            FadeOut(arbre_bas),
            FadeOut(lecture),
        )

        # --- À retenir : méthode d'analyse en 3 questions --------------------------
        methode = method_box(
            Text(
                _wrap(
                    "1. Récessif ou dominant ? Deux parents sains avec un "
                    "enfant atteint → allèle récessif. Le caractère "
                    "apparaît à chaque génération → plutôt dominant.\n"
                    "2. Autosomique ou lié à X ? Presque uniquement des "
                    "garçons atteints, aucun père ne transmet à son fils "
                    "→ probablement lié à X récessif. Filles et garçons "
                    "atteints de façon égale → autosomique.\n"
                    "3. On vérifie en attribuant un génotype à chaque "
                    "individu : tous les cas doivent être compatibles.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.3,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour déterminer le mode de transmission d'un caractère à "
                "partir d'un arbre, on se pose trois questions "
                "successives. Un : le caractère est-il récessif ou "
                "dominant ? Si deux parents sains ont un enfant atteint, "
                "l'allèle est récessif, resté masqué chez des parents "
                "hétérozygotes. Si le caractère apparaît à chaque "
                "génération, il est plutôt dominant. Deux : le gène est-il "
                "autosomique ou lié à X ? Si les personnes atteintes sont "
                "presque uniquement des garçons, et qu'aucun père ne "
                "transmet le caractère à son fils, le gène est "
                "probablement lié à X et récessif. Si filles et garçons "
                "sont atteints de la même façon, le gène est autosomique. "
                "Trois : on vérifie l'hypothèse en attribuant un génotype "
                "à chaque individu de l'arbre ; tous les cas doivent être "
                "compatibles."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
