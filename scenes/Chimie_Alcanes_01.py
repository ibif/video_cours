"""
scenes/Chimie_Alcanes_01.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 01.

§ Mise en situation (visite SIR), rappels sur la liaison covalente et la
valence, définitions hydrocarbure / alcane, propriété (formule générale
CₙH₂ₙ₊₂ et sa justification), objectifs du chapitre.
Source : 1ereC/Chimie.pdf, pages 14-15.
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
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
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


class IntroductionAlcanes(NotionScene):
    def construct(self):
        titre = scene_title("2. Hydrocarbures saturés — les alcanes")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation (visite à la SIR) ----------------------
        mise_en_situation = Text(
            _wrap(
                "Lors d'une visite à la Société Ivoirienne de Raffinage "
                "(SIR), des élèves découvrent que le pétrole lampant, le "
                "gaz de cuisine, l'essence, le gas-oil et le kérosène "
                "contiennent tous des alcanes. Comment sont-ils "
                "structurés ? Comment les nommer ? Quel est leur intérêt "
                "dans la vie quotidienne ?",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Lors d'une visite à la Société Ivoirienne de Raffinage, la "
                "SIR, des élèves de première C découvrent que le pétrole "
                "lampant, le gaz de cuisine, l'essence sans plomb, le "
                "gas-oil et le kérosène contiennent tous des alcanes. De "
                "retour en classe, ils cherchent à répondre à trois "
                "questions : quelle est la structure des alcanes ? Comment "
                "les nommer correctement ? Et quel est leur intérêt dans la "
                "vie quotidienne ? Ce chapitre répond à ces trois "
                "questions."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : rappels liaison covalente et valence ---------------
        rappel_covalence = definition_box(
            Text(
                _wrap(
                    "Une liaison covalente s'établit entre deux atomes par "
                    "la mise en commun de deux électrons célibataires, "
                    "formant un doublet d'électrons appelé doublet liant.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        rappel_covalence.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avant de commencer, rappelons deux notions vues au collège. "
                "Une liaison covalente s'établit entre deux atomes par la "
                "mise en commun de deux de leurs électrons célibataires, de "
                "manière à former un doublet d'électrons appelé doublet "
                "liant, ou doublet de liaison."
            )
        ) as tracker:
            self.play(FadeIn(rappel_covalence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel_covalence))

        rappel_valence = definition_box(
            Text(
                _wrap(
                    "La valence d'un atome est le nombre de liaisons de "
                    "covalence qu'il peut établir avec d'autres atomes. Le "
                    "carbone (Z=6) est tétravalent : il forme toujours "
                    "quatre liaisons. L'hydrogène est monovalent : il n'en "
                    "forme qu'une seule.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        rappel_valence.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La valence d'un atome est le nombre de liaisons de "
                "covalence qu'il peut établir avec d'autres atomes. L'atome "
                "de carbone, de numéro atomique six, possède quatre "
                "électrons sur sa couche externe : il est tétravalent, il "
                "établit toujours quatre liaisons covalentes. L'atome "
                "d'hydrogène, lui, est monovalent : il n'établit qu'une "
                "seule liaison covalente."
            )
        ) as tracker:
            self.play(FadeIn(rappel_valence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel_valence))

        # --- Exemple traité : définitions + formule générale justifiée ---------
        def_hydrocarbure = definition_box(
            Text(
                _wrap(
                    "Un hydrocarbure est un composé organique formé "
                    "uniquement d'atomes de carbone et d'hydrogène.",
                    width=48,
                ),
                font_size=26,
            ),
        )
        def_hydrocarbure.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un hydrocarbure est un composé organique formé uniquement "
                "d'atomes de carbone et d'hydrogène."
            )
        ) as tracker:
            self.play(FadeIn(def_hydrocarbure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_hydrocarbure))

        def_alcane = definition_box(
            Text(
                _wrap(
                    "Un alcane est un hydrocarbure saturé dont tous les "
                    "atomes de carbone ont une structure tétraédrique et "
                    "sont reliés par des liaisons covalentes simples C–C. "
                    "La molécule est « saturée » : chaque carbone a épuisé "
                    "ses quatre valences, il ne peut plus fixer d'autres "
                    "atomes.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        def_alcane.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un alcane est un hydrocarbure saturé dont tous les atomes "
                "de carbone ont une structure tétraédrique et sont reliés "
                "par des liaisons covalentes simples carbone-carbone. La "
                "molécule est dite « saturée » parce que chaque atome de "
                "carbone a épuisé ses quatre valences : il ne peut plus "
                "fixer, c'est-à-dire additionner, d'autres atomes."
            )
        ) as tracker:
            self.play(FadeIn(def_alcane))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_alcane))

        entete_formule = Text("Justification de la formule générale CₙH₂ₙ₊₂", font_size=23, color=YELLOW, weight="BOLD")
        entete_formule.next_to(titre, DOWN, buff=0.4)

        schema_chaine = MathTex(
            r"\underbrace{CH_3}_{3\,H} - \underbrace{CH_2 - \cdots - CH_2}_{(n-2)\times 2\,H} - \underbrace{CH_3}_{3\,H}",
            font_size=28,
            color=WHITE,
        )
        schema_chaine.next_to(entete_formule, DOWN, buff=0.45)

        calcul = MathTex(
            r"N(H) = \underbrace{2 \times 3}_{\text{extrémités}} + \underbrace{2(n-2)}_{\text{carbones internes}} = 2n+2",
            font_size=27,
            color=WHITE,
        )
        calcul.next_to(schema_chaine, DOWN, buff=0.5)

        groupe_formule = VGroup(entete_formule, schema_chaine, calcul)

        with self.voiceover(
            text=(
                "Justifions la formule générale des alcanes. Considérons "
                "une chaîne linéaire de n atomes de carbone. Les deux "
                "atomes de carbone situés aux extrémités portent chacun "
                "trois atomes d'hydrogène, des groupes C-H-3, soit deux "
                "fois trois, six atomes d'hydrogène. Chacun des n moins "
                "deux atomes de carbone intermédiaires porte deux atomes "
                "d'hydrogène, des groupes C-H-2, soit deux fois n moins "
                "deux atomes d'hydrogène. Au total : six plus deux n moins "
                "quatre, c'est-à-dire deux n plus deux atomes d'hydrogène. "
                "Une ramification ne change rien à ce résultat : "
                "remplacer un hydrogène par un groupe méthyle retire un H "
                "mais en ajoute trois, un gain net de deux H pour un "
                "carbone ajouté, exactement comme un allongement de "
                "chaîne."
            )
        ) as tracker:
            self.play(FadeIn(entete_formule))
            self.play(Write(schema_chaine))
            self.play(Write(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_formule))

        propriete = property_box(
            VGroup(
                MathTex(r"C_nH_{2n+2} \quad (n \geq 1)", font_size=34, color="#1A1A1A"),
                Text(
                    _wrap("Exemples : CH₄ (n=1) ; C₄H₁₀ (n=4) ; C₈H₁₈ (n=8).", width=44),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.35),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les alcanes non cycliques ont donc pour formule brute "
                "générale C indice n, H indice deux n plus deux, avec n "
                "supérieur ou égal à un. Par exemple, pour n égal un, on "
                "obtient C-H-4, le méthane ; pour n égal quatre, C-4, "
                "H-10, le butane ; pour n égal huit, C-8, H-18, l'octane."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- À retenir : les objectifs du chapitre ------------------------------
        entete_obj = Text("Objectifs du chapitre", font_size=26, color=YELLOW, weight="BOLD")
        entete_obj.next_to(titre, DOWN, buff=0.4)

        objectifs = _bullets(
            [
                "Donner la formule générale des alcanes et décrire la "
                "structure tétraédrique du carbone.",
                "Nommer un alcane (linéaire, ramifié, cyclique) et écrire "
                "sa formule semi-développée à partir de son nom (UICPA).",
                "Déterminer les isomères de chaîne d'une formule brute "
                "donnée.",
                "Interpréter l'état physique et le point d'ébullition des "
                "alcanes.",
                "Écrire et équilibrer les combustions complète et "
                "incomplète, les exploiter (formule brute, volume, "
                "pouvoir calorifique).",
                "Décrire la substitution radicalaire d'un halogène et "
                "citer des usages des alcanes.",
            ],
            font_size=19,
            width=58,
        )
        objectifs.next_to(entete_obj, DOWN, buff=0.35)
        _fit(objectifs, entete_obj.get_bottom()[1] - 0.35)

        groupe_obj = VGroup(entete_obj, objectifs)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, vous devez être capable de : "
                "donner la formule brute générale des alcanes et décrire "
                "la structure tétraédrique de l'atome de carbone ; nommer "
                "un alcane linéaire, ramifié ou cyclique, et écrire sa "
                "formule semi-développée à partir de son nom, en "
                "appliquant les règles de l'UICPA ; déterminer les "
                "isomères de chaîne d'une formule brute donnée ; "
                "interpréter l'état physique et le point d'ébullition des "
                "alcanes ; écrire et équilibrer les équations de "
                "combustion complète et incomplète, et les exploiter ; "
                "enfin, décrire la réaction de substitution radicalaire "
                "d'un halogène sur un alcane et citer des usages des "
                "alcanes et de leurs dérivés."
            )
        ) as tracker:
            self.play(FadeIn(entete_obj))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_obj))

        # --- Piège à éviter : hydrocarbure ≠ toujours alcane --------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas hydrocarbure et alcane : tout alcane "
                    "est un hydrocarbure, mais tout hydrocarbure n'est pas "
                    "un alcane. Un alcane n'a QUE des liaisons simples "
                    "C–C ; dès qu'une liaison double ou triple apparaît, "
                    "la molécule n'est plus saturée et n'est donc plus un "
                    "alcane.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre hydrocarbure et alcane : tout "
                "alcane est un hydrocarbure, mais tout hydrocarbure n'est "
                "pas un alcane. Un alcane n'a que des liaisons simples "
                "carbone-carbone ; dès qu'une liaison double ou triple "
                "apparaît, la molécule n'est plus saturée, et ce n'est donc "
                "plus un alcane."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
