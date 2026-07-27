"""
scenes/Maths_StatistiqueUneVariable_05.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 05.

§ Mode, classe modale et médiane : définition mode (série discrète) /
classe modale (série regroupée, effectif ou densité maximal). Exemples :
mode = 12 dans l'exemple des notes (scène 02), classe modale [70;75[,
mode = 72,5 kg dans l'exemple des sacs de cacao (scène 03). Définition
médiane (partage la population en deux effectifs égaux). Cas série
discrète (N impair / N pair). Cas série en classes (définition CIAM :
nombre égal à N/2 de part et d'autre).
Source : 1ereC/Maths.pdf, chapitre 17, pages 204-205.
"""

import textwrap

from manim import DOWN, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ModeClasseModaleMediane(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Mode, classe modale et médiane")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Nous ouvrons maintenant la troisième partie du "
                "chapitre : les CARACTÉRISTIQUES DE POSITION, qui "
                "résument une série par une seule valeur typique. "
                "Commençons par le mode et la médiane.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous ouvrons maintenant la troisième partie du "
                "chapitre : les caractéristiques de position, qui "
                "résument toute une série statistique par une seule "
                "valeur typique. Commençons par les deux plus simples à "
                "définir : le mode, et la médiane."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : mode / classe modale -------------------------------
        def_mode = definition_box(
            VGroup(
                Text("Mode et classe modale", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "Série DISCRÈTE : le MODE est la modalité "
                        "d'effectif MAXIMAL.",
                        width=46,
                    ),
                    font_size=20,
                ),
                Text(
                    _wrap(
                        "Série en CLASSES : la CLASSE MODALE est la "
                        "classe d'effectif (ou de densité) MAXIMAL. Son "
                        "mode est le CENTRE de cette classe.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_mode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour une série discrète, le mode est simplement la "
                "modalité dont l'effectif est maximal. Pour une série "
                "regroupée en classes, on parle de classe modale : "
                "c'est la classe dont l'effectif, ou la densité si les "
                "amplitudes diffèrent, est maximal. Le mode est alors le "
                "centre de cette classe modale."
            )
        ) as tracker:
            self.play(FadeIn(def_mode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_mode))

        exemples_mode = example_box(
            VGroup(
                Text("Reprise des deux exemples", font_size=21, weight="BOLD"),
                MathTex(r"\text{Notes (série discrète)} : \ n_{12}=12 \ \text{maximal} \Rightarrow \text{mode} = 12", font_size=21),
                MathTex(r"\text{Cacao (série en classes)} : \ \text{classe modale} = [70\,;75[, \ \text{mode} = 72{,}5\text{ kg}", font_size=21),
            ).arrange(DOWN, buff=0.25),
        )
        exemples_mode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons nos deux exemples. Dans la série des notes, "
                "l'effectif maximal, 12 élèves, est atteint pour la note "
                "12 : le mode vaut donc 12. Dans la série des sacs de "
                "cacao, la classe la plus peuplée, avec 24 sacs, est la "
                "classe 70 à 75 kilogrammes : c'est la classe modale, et "
                "le mode associé est son centre, 72,5 kilogrammes."
            )
        ) as tracker:
            self.play(FadeIn(exemples_mode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples_mode))

        # --- Raisonnement : médiane, définition générale ------------------------
        def_mediane = definition_box(
            VGroup(
                Text("Médiane", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "La médiane M est une valeur qui PARTAGE la "
                        "population en deux groupes de MÊME EFFECTIF : "
                        "autant d'individus en dessous qu'au-dessus.",
                        width=46,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_mediane.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La médiane, notée M, est une valeur qui partage la "
                "population en deux groupes de même effectif : autant "
                "d'individus ont une modalité inférieure à M que "
                "d'individus ont une modalité supérieure à M."
            )
        ) as tracker:
            self.play(FadeIn(def_mediane))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_mediane))

        cas_discret = definition_box(
            VGroup(
                Text("Médiane — série discrète (valeurs triées)", font_size=20, weight="BOLD"),
                MathTex(r"N \text{ IMPAIR} : \ M = x_{\frac{N+1}{2}} \ (\text{valeur du RANG central})", font_size=21),
                MathTex(r"N \text{ PAIR} : \ M = \dfrac{x_{\frac{N}{2}} + x_{\frac{N}{2}+1}}{2} \ (\text{moyenne des 2 rangs centraux})", font_size=20),
            ).arrange(DOWN, buff=0.22),
        )
        cas_discret.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour une série discrète, on trie d'abord toutes les "
                "valeurs par ordre croissant. Si N est impair, la "
                "médiane est la valeur du rang central, N plus 1 sur 2. "
                "Si N est pair, il n'y a pas un mais deux rangs "
                "centraux, N sur 2 et N sur 2 plus 1 : la médiane est "
                "alors leur moyenne."
            )
        ) as tracker:
            self.play(FadeIn(cas_discret))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_discret))

        # --- Exemple traité : médiane de la série des notes (N=40, pair) -------
        enonce = Text(
            _wrap(
                "Reprenons l'exemple des notes : N=40 est pair. Les "
                "rangs centraux sont donc 20 et 21.",
                width=52,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons l'exemple des notes de la scène 2, où N vaut "
                "40, un nombre pair. Les rangs centraux sont donc 20 et "
                "21."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul_mediane = MathTex(
            r"\text{ECC}(11)=14 < 20 \text{ et } 21 \le \text{ECC}(12)=26 \ \Rightarrow \ x_{20}=x_{21}=12 \ \Rightarrow \ M = 12",
            font_size=22,
            color=YELLOW,
        )
        calcul_mediane.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'effectif cumulé croissant vaut 14 à la note 11, et "
                "26 à la note 12. Les rangs 20 et 21 tombent donc tous "
                "les deux dans le groupe de note 12 : la médiane vaut "
                "12, exactement comme le mode dans cet exemple — une "
                "coïncidence qui n'est pas systématique."
            )
        ) as tracker:
            self.play(Write(calcul_mediane))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_mediane))

        # --- Cas série en classes (définition CIAM) ------------------------------
        cas_classes = definition_box(
            VGroup(
                Text("Médiane — série en classes (définition CIAM)", font_size=19, weight="BOLD"),
                Text(
                    _wrap(
                        "La médiane est le nombre M tel qu'il y a N/2 "
                        "individus dans [min ; M] et N/2 individus dans "
                        "[M ; max]. On la calcule par INTERPOLATION "
                        "LINÉAIRE (scène suivante).",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        cas_classes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour une série regroupée en classes, la médiane se "
                "définit, selon la convention du CIAM, comme le nombre "
                "M tel qu'il y ait N sur 2 individus entre le minimum et "
                "M, et N sur 2 individus entre M et le maximum. Comme M "
                "n'est en général pas une borne de classe, on la calcule "
                "par interpolation linéaire — ce sera l'objet de la "
                "prochaine scène."
            )
        ) as tracker:
            self.play(FadeIn(cas_classes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_classes))

        # --- À retenir --------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "Mode = valeur/classe la plus fréquente. "
                        "Médiane = valeur qui partage la population en "
                        "deux effectifs égaux. Deux notions distinctes, "
                        "parfois égales par coïncidence.",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons bien la différence : le mode est la valeur ou "
                "la classe la plus fréquente, tandis que la médiane est "
                "la valeur qui partage la population en deux effectifs "
                "égaux. Deux notions bien distinctes, même si elles "
                "coïncident parfois, comme dans notre exemple des notes."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Toujours TRIER avant de chercher la médiane", font_size=18, weight="BOLD"),
                Text(
                    _wrap(
                        "Pour une série discrète, chercher le rang "
                        "central dans les données BRUTES (non triées) "
                        "donne un résultat faux. Trier — ou utiliser "
                        "l'ECC comme ci-dessus — est indispensable.",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège fréquent chez les élèves pressés : chercher le "
                "rang central directement dans les données brutes, non "
                "triées, ce qui donne systématiquement un résultat "
                "faux. Trier la série — ou, comme nous venons de le "
                "faire, s'appuyer directement sur l'effectif cumulé "
                "croissant — est une étape indispensable avant tout "
                "calcul de médiane ou de quartile."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
