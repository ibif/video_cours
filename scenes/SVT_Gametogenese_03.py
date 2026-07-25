"""
scenes/SVT_Gametogenese_03.py — Chapitre 3 (1ereD, SVT), scène 03.

§ 3.2 Les gonades, sièges de la gamétogénèse : définition de la
gamétogénèse (spermatogenèse/ovogenèse), double fonction des gonades,
structure du testicule (spermatogonies, cellules de Sertoli, cellules de
Leydig), structure de l'ovaire (follicules, ovulation).
Source : 1ereD/SVT.pdf, pages 32-34.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Annulus,
    Arrow,
    Circle,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class GonadesSiegesDeLaGametogenese(NotionScene):
    def construct(self):
        titre = scene_title("3.2 — Les gonades, sièges de la gamétogénèse")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : définition de la gamétogénèse -------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La gamétogénèse est l'ensemble des phénomènes qui "
                    "aboutissent à la formation des gamètes. Elle se "
                    "déroule dans des organes appelés gonades : la "
                    "spermatogenèse (spermatozoïdes, testicules) et "
                    "l'ovogenèse (ovules, ovaires).",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La gamétogénèse est l'ensemble des phénomènes qui "
                "aboutissent à la formation des gamètes. Elle se déroule "
                "dans des organes appelés gonades. On distingue la "
                "spermatogenèse, formation des spermatozoïdes dans les "
                "testicules, les gonades mâles, et l'ovogenèse, formation "
                "des ovules dans les ovaires, les gonades femelles."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        remarque_double = warning_box(
            Text(
                _wrap(
                    "Les gonades ont une double fonction : produire les "
                    "gamètes (fonction reproductrice) et sécréter des "
                    "hormones sexuelles (fonction endocrine) — voir la "
                    "section 3.6.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.5,
        )
        remarque_double.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons dès maintenant que les gonades ont une double "
                "fonction : produire les gamètes, c'est la fonction "
                "reproductrice, et sécréter des hormones sexuelles, c'est "
                "la fonction endocrine, dont nous parlerons en détail à la "
                "section trois point six."
            )
        ) as tracker:
            self.play(FadeIn(remarque_double))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_double))

        # --- Raisonnement 1 : le testicule ----------------------------------
        entete_t = Text("3.2.2 — Le testicule", font_size=27, color=YELLOW, weight="BOLD")
        entete_t.next_to(titre, DOWN, buff=0.45)

        outer = Annulus(inner_radius=1.5, outer_radius=1.85, color=BLUE, fill_opacity=0.85)
        ring2 = Annulus(inner_radius=1.05, outer_radius=1.5, color=GREEN, fill_opacity=0.85)
        ring3 = Annulus(inner_radius=0.55, outer_radius=1.05, color=ORANGE, fill_opacity=0.85)
        center = Circle(radius=0.55, color=RED, fill_opacity=0.85)
        tube = VGroup(outer, ring2, ring3, center)
        tube.shift(LEFT * 3.4 + DOWN * 0.2)

        label_sperm = Text("Spermatogonies\n(diploïdes, paroi)", font_size=17, color=WHITE)
        label_sperm.next_to(tube, UP, buff=0.7).shift(LEFT * 0.2)
        arrow_sperm = Arrow(label_sperm.get_bottom(), outer.get_top(), buff=0.1, color=WHITE)

        label_sertoli = Text("Cellules de Sertoli\n(nourricières)", font_size=16, color=WHITE)
        label_sertoli.next_to(tube, RIGHT, buff=1.5).shift(UP * 1.0)
        arrow_sertoli = Arrow(label_sertoli.get_left(), ring2.get_right(), buff=0.1, color=WHITE)

        label_center = Text("Spermatozoïdes\n(lumière du tube)", font_size=16, color=WHITE)
        label_center.next_to(tube, RIGHT, buff=1.5).shift(DOWN * 1.0)
        arrow_center = Arrow(label_center.get_left(), center.get_right(), buff=0.1, color=WHITE)

        leydig_dots = VGroup(*[Dot(color=YELLOW) for _ in range(5)]).arrange(RIGHT, buff=0.15)
        leydig_dots.next_to(tube, DOWN, buff=0.55)
        label_leydig = Text("Cellules de Leydig\n(testostérone)", font_size=16, color=YELLOW)
        label_leydig.next_to(leydig_dots, DOWN, buff=0.15)

        schema_t = VGroup(
            tube, label_sperm, arrow_sperm, label_sertoli, arrow_sertoli,
            label_center, arrow_center, leydig_dots, label_leydig,
        )
        schema_t.next_to(entete_t, DOWN, buff=0.35).shift(LEFT * 0.2)

        with self.voiceover(
            text=(
                "Les deux testicules sont logés dans les bourses, à "
                "l'extérieur de l'abdomen, ce qui les maintient à une "
                "température inférieure d'environ deux degrés à celle du "
                "corps, condition nécessaire à la formation des "
                "spermatozoïdes. Chaque testicule contient environ deux "
                "cent cinquante compartiments renfermant de longs tubes "
                "repliés, les tubes séminifères, où se déroule la "
                "spermatogenèse. Dans la paroi d'un tube, de l'extérieur "
                "vers le centre, on observe les spermatogonies, cellules "
                "diploïdes contre la membrane basale, puis des cellules de "
                "plus en plus mûres qui migrent vers la lumière, jusqu'aux "
                "spermatozoïdes achevés, plantés dans les cellules de "
                "Sertoli, les cellules nourricières. Entre les tubes, les "
                "cellules de Leydig sécrètent la testostérone, l'hormone "
                "mâle."
            )
        ) as tracker:
            self.play(FadeIn(entete_t))
            self.play(FadeIn(tube))
            self.play(FadeIn(label_sperm), FadeIn(arrow_sperm))
            self.play(FadeIn(label_sertoli), FadeIn(arrow_sertoli))
            self.play(FadeIn(label_center), FadeIn(arrow_center))
            self.play(FadeIn(leydig_dots), FadeIn(label_leydig))
            self.wait(tracker.get_remaining_duration())

        remarque_epididyme = Text(
            _wrap(
                "Les spermatozoïdes sont ensuite stockés et achèvent leur "
                "maturation dans l'épididyme, avant d'être expulsés par "
                "les canaux déférents lors de l'éjaculation.",
                width=52,
            ),
            font_size=21,
            color=WHITE,
        )
        remarque_epididyme.next_to(entete_t, DOWN, buff=3.4)

        with self.voiceover(
            text=(
                "Les spermatozoïdes formés dans les tubes séminifères sont "
                "ensuite stockés et achèvent leur maturation fonctionnelle "
                "dans l'épididyme, un long canal accolé au testicule. Ils "
                "seront expulsés au moment de l'éjaculation par les voies "
                "génitales, les canaux déférents."
            )
        ) as tracker:
            self.play(FadeOut(schema_t))
            self.play(FadeIn(remarque_epididyme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_t), FadeOut(remarque_epididyme))

        # --- Raisonnement 2 : l'ovaire ---------------------------------------
        entete_o = Text("3.2.3 — L'ovaire", font_size=27, color=YELLOW, weight="BOLD")
        entete_o.next_to(titre, DOWN, buff=0.45)

        ovaire = Ellipse(width=3.0, height=2.2, color=BLUE, fill_opacity=0.6)
        ovaire.shift(LEFT * 3.2 + DOWN * 0.2)

        follicules_petits = VGroup(
            *[Circle(radius=0.18, color=GREEN, fill_opacity=0.8) for _ in range(4)]
        )
        positions = [LEFT * 0.9 + UP * 0.5, LEFT * 0.5 + DOWN * 0.6, RIGHT * 0.2 + UP * 0.2, RIGHT * 0.1 + DOWN * 0.7]
        for dot, pos in zip(follicules_petits, positions):
            dot.move_to(ovaire.get_center() + pos)

        follicule_mur = Circle(radius=0.45, color=ORANGE, fill_opacity=0.85)
        follicule_mur.move_to(ovaire.get_right() + LEFT * 0.35)
        ovocyte = Dot(color=RED, radius=0.09)
        ovocyte.move_to(follicule_mur.get_center())

        schema_o = VGroup(ovaire, follicules_petits, follicule_mur, ovocyte)

        label_follicules = Text("Follicules ovariens\n(chacun = 1 ovocyte)", font_size=16, color=GREEN)
        label_follicules.next_to(schema_o, UP, buff=0.7).shift(LEFT * 0.3)
        arrow_follicules = Arrow(label_follicules.get_bottom(), follicules_petits[0].get_top(), buff=0.1, color=WHITE)

        label_mur = Text("Follicule mûr\n(ovocyte prêt à ovuler)", font_size=16, color=ORANGE)
        label_mur.next_to(schema_o, RIGHT, buff=1.3).shift(UP * 0.3)
        arrow_mur = Arrow(label_mur.get_left(), follicule_mur.get_right(), buff=0.1, color=WHITE)

        schema_o_full = VGroup(schema_o, label_follicules, arrow_follicules, label_mur, arrow_mur)
        schema_o_full.next_to(entete_o, DOWN, buff=0.35).shift(LEFT * 0.2)

        with self.voiceover(
            text=(
                "Les deux ovaires, de la taille d'une grosse amande, sont "
                "situés dans la cavité abdominale, de part et d'autre de "
                "l'utérus. Chaque ovaire contient des milliers de petites "
                "vésicules, les follicules ovariens ; chaque follicule "
                "renferme une cellule de la lignée femelle, un ovocyte. Un "
                "follicule n'est pas une simple poche : il grandit avec "
                "l'ovocyte qu'il contient, le nourrit, le protège et "
                "produit des hormones, les œstrogènes. À chaque cycle "
                "menstruel, quelques follicules commencent à se "
                "développer, mais en général un seul arrive à terme et "
                "libère son ovocyte : c'est l'ovulation."
            )
        ) as tracker:
            self.play(FadeIn(entete_o))
            self.play(FadeIn(ovaire))
            self.play(FadeIn(follicules_petits), FadeIn(label_follicules), FadeIn(arrow_follicules))
            self.play(FadeIn(follicule_mur), FadeIn(ovocyte), FadeIn(label_mur), FadeIn(arrow_mur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_o_full))

        # --- À retenir : vocabulaire -----------------------------------------
        vocabulaire = _bullets(
            [
                "Follicule ovarien : ensemble formé par un ovocyte et les "
                "cellules qui l'entourent dans l'ovaire.",
                "Ovulation : libération de l'ovocyte par le follicule mûr, "
                "capté ensuite par le pavillon de la trompe utérine, où "
                "pourra avoir lieu la fécondation.",
            ],
            width=50,
        )
        entete_vocab = Text("Vocabulaire à retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_vocab.next_to(titre, DOWN, buff=0.5)
        vocabulaire.next_to(entete_vocab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux mots de vocabulaire à retenir. Le follicule ovarien "
                "est l'ensemble formé par un ovocyte et les cellules qui "
                "l'entourent dans l'ovaire. L'ovulation est la libération "
                "de l'ovocyte par le follicule mûr, à la surface de "
                "l'ovaire : l'ovocyte est alors capté par le pavillon de la "
                "trompe utérine, la trompe de Fallope, où pourra avoir lieu "
                "la fécondation."
            )
        ) as tracker:
            self.play(FadeOut(entete_o))
            self.play(FadeIn(entete_vocab))
            self.play(FadeIn(vocabulaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_vocab), FadeOut(vocabulaire))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas testicule et gonade en général : le "
                    "testicule est la gonade mâle, l'ovaire la gonade "
                    "femelle. Et n'oublie pas les cellules de soutien : "
                    "sans les cellules de Sertoli (nourricières) et sans le "
                    "follicule (nourricier, protecteur), les gamètes ne "
                    "peuvent pas achever leur formation.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre testicule et gonade en "
                "général : le testicule est la gonade mâle, l'ovaire la "
                "gonade femelle, chacun n'étant qu'un cas particulier. "
                "N'oublie pas non plus les cellules de soutien : sans les "
                "cellules de Sertoli, nourricières, dans le testicule, et "
                "sans le follicule, nourricier et protecteur, dans "
                "l'ovaire, les gamètes ne pourraient pas achever leur "
                "formation."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
