"""
scenes/SVT_SyntheseProteines_08.py — Chapitre 5 (1ereD, SVT), scène 08.

§ 5.5.3 La drépanocytose (retour à la question d'Awa : GAG -> GTG,
Glu -> Val, conséquences en cascade, transmission autosomique récessive,
avantage sélectif face au paludisme), attention aux deux idées fausses,
tableau récapitulatif transcription/traduction, et L'ESSENTIEL DU
CHAPITRE en clôture. Source : 1ereD/SVT.pdf, pages 74-76.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    MAROON,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, warning_box

BASE_COLORS = {"A": GREEN, "U": RED, "G": BLUE, "C": ORANGE, "T": MAROON}


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _codon(codon: str, font_size: int = 32) -> VGroup:
    lettres = VGroup(
        *[Text(base, font_size=font_size, color=BASE_COLORS.get(base, WHITE), weight="BOLD") for base in codon]
    )
    lettres.arrange(RIGHT, buff=0.05)
    return lettres


class LaDrepanocytose(NotionScene):
    def construct(self):
        titre = scene_title("5.5.3 — La drépanocytose")
        titre.scale(0.8)
        titre.to_edge(UP)

        # --- Énoncé : retour à la question d'Awa, comparaison des codons ----
        intro = Text(
            _wrap(
                "Revenons à la question d'Awa. La bêta-globine, chaîne de "
                "l'hémoglobine, comporte 146 acides aminés.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Revenons à la question d'Awa. L'hémoglobine est formée "
                "notamment d'une chaîne appelée bêta-globine, qui comporte "
                "cent quarante-six acides aminés."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        entete_comp = Text("6e codon de l'ARNm de la bêta-globine", font_size=23, color=YELLOW, weight="BOLD")
        entete_comp.next_to(titre, DOWN, buff=0.5)

        ligne_sain = VGroup(
            Text("Individu sain :", font_size=22, color=WHITE),
            _codon("GAG"), Text("→ Glu (acide glutamique)", font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.3)
        ligne_malade = VGroup(
            Text("Drépanocytaire :", font_size=22, color=WHITE),
            _codon("GUG"), Text("→ Val (valine)", font_size=22, color=RED),
        ).arrange(RIGHT, buff=0.3)
        comparaison = VGroup(ligne_sain, ligne_malade).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        comparaison.next_to(entete_comp, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Chez un individu sain, le brin non transcrit porte le "
                "triplet G A G en sixième position : l'ARNm contient le "
                "codon G A G, qui code l'acide glutamique. Chez un "
                "individu atteint de drépanocytose, une seule base a "
                "changé : le triplet est devenu G T G sur l'ADN ; l'ARNm "
                "contient alors G U G, qui code la valine. Ce minuscule "
                "changement, un seul acide aminé sur cent quarante-six, a "
                "des conséquences en cascade."
            )
        ) as tracker:
            self.play(FadeIn(entete_comp))
            self.play(FadeIn(ligne_sain))
            self.play(FadeIn(ligne_malade))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_comp), FadeOut(comparaison))

        # --- Raisonnement : conséquences en cascade + transmission ----------
        entete_cascade = Text("Conséquences en cascade", font_size=25, color=YELLOW, weight="BOLD")
        entete_cascade.next_to(titre, DOWN, buff=0.5)

        cascade = _bullets(
            [
                "Val remplace Glu -> l'hémoglobine devient moins soluble.",
                "En cas de manque de dioxygène (effort, infection) : les "
                "molécules d'hémoglobine s'assemblent en longues fibres.",
                "Ces fibres déforment les globules rouges en faucille.",
                "Ces globules se détruisent vite (anémie) et bouchent les "
                "petits vaisseaux (crises douloureuses).",
            ],
            font_size=21,
            width=54,
        )
        cascade.next_to(entete_cascade, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La valine rend l'hémoglobine moins soluble ; lorsque le "
                "dioxygène manque, à l'effort ou lors d'une infection, les "
                "molécules d'hémoglobine s'assemblent en longues fibres qui "
                "déforment les globules rouges en faucille. Ces globules "
                "se détruisent rapidement, d'où l'anémie, et bouchent les "
                "petits vaisseaux, d'où les crises douloureuses que "
                "connaît Koffi."
            )
        ) as tracker:
            self.play(FadeIn(entete_cascade))
            self.play(FadeIn(cascade))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_cascade), FadeOut(cascade))

        transmission = Text(
            _wrap(
                "Transmission autosomique récessive : un enfant n'est "
                "malade que s'il reçoit l'allèle muté de ses deux "
                "parents. Les parents, porteurs d'un seul allèle muté "
                "(hétérozygotes), ne sont pas malades : c'est le cas des "
                "parents d'Awa.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        transmission.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La maladie se transmet selon le mode autosomique "
                "récessif : un enfant n'est malade que s'il reçoit l'allèle "
                "muté de ses deux parents. Les parents, porteurs d'un seul "
                "allèle muté, sont dits hétérozygotes, et ne sont pas "
                "malades : c'est le cas des parents d'Awa."
            )
        ) as tracker:
            self.play(FadeIn(transmission))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(transmission))

        # --- Remarque : avantage sélectif face au paludisme ------------------
        remarque_palu = warning_box(
            Text(
                _wrap(
                    "Pourquoi cette maladie est-elle fréquente en Afrique "
                    "de l'Ouest ? Les hétérozygotes résistent mieux aux "
                    "formes graves du paludisme, très répandu en Côte "
                    "d'Ivoire : le parasite se développe mal dans leurs "
                    "globules rouges. Cet avantage a maintenu l'allèle "
                    "muté dans les régions où le paludisme sévit : c'est "
                    "un avantage sélectif du porteur sain.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        remarque_palu.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi cette maladie est-elle si fréquente en Afrique de "
                "l'Ouest ? Les personnes hétérozygotes, qui possèdent un "
                "allèle normal et un allèle muté, résistent mieux aux "
                "formes graves du paludisme, maladie très répandue en Côte "
                "d'Ivoire : le parasite se développe mal dans leurs "
                "globules rouges. Cet avantage explique que l'allèle muté "
                "ait été conservé par l'évolution dans les régions où le "
                "paludisme sévit, malgré la gravité de la drépanocytose "
                "chez les personnes malades. C'est un exemple célèbre "
                "d'avantage sélectif du porteur sain."
            )
        ) as tracker:
            self.play(FadeIn(remarque_palu))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_palu))

        # --- Piège à éviter : deux idées fausses ------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Deux idées fausses à combattre. 1) « Une mutation est "
                    "toujours grave » : faux, grâce à la dégénérescence du "
                    "code, certaines substitutions sont silencieuses, "
                    "sans conséquence, voire favorables. 2) « Toute "
                    "mutation se transmet aux enfants » : faux, seules "
                    "les mutations des cellules reproductrices sont "
                    "héréditaires.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux idées fausses sont à combattre. Première idée fausse "
                ": une mutation est toujours grave. C'est faux : grâce à la "
                "dégénérescence du code, certaines substitutions ne "
                "changent pas l'acide aminé, ce sont des mutations "
                "silencieuses, sans conséquence ; d'autres mutations sont "
                "même favorables. Deuxième idée fausse : toute mutation se "
                "transmet aux enfants. C'est faux également : seules les "
                "mutations des cellules reproductrices sont héréditaires."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : tableau récapitulatif transcription/traduction ------
        entete_tab = Text("Récapitulatif : transcription / traduction", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        col_critere = VGroup(
            Text("Critère", font_size=19, color=YELLOW, weight="BOLD"),
            Text("Lieu", font_size=18, color=WHITE),
            Text("Départ", font_size=18, color=WHITE),
            Text("Acteur principal", font_size=18, color=WHITE),
            Text("Produit", font_size=18, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        col_transcription = VGroup(
            Text("Transcription", font_size=19, color=YELLOW, weight="BOLD"),
            Text("noyau", font_size=18, color=WHITE),
            Text(_wrap("ADN (brin transcrit)", width=20), font_size=18, color=WHITE),
            Text("ARN polymérase", font_size=18, color=WHITE),
            Text("ARNm", font_size=18, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        col_traduction = VGroup(
            Text("Traduction", font_size=19, color=YELLOW, weight="BOLD"),
            Text(_wrap("cytoplasme (ribosomes)", width=20), font_size=18, color=WHITE),
            Text("ARNm", font_size=18, color=WHITE),
            Text(_wrap("ribosome, ARNt", width=20), font_size=18, color=WHITE),
            Text(_wrap("protéine", width=20), font_size=18, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        tableau = VGroup(col_critere, col_transcription, col_traduction).arrange(RIGHT, buff=0.6, aligned_edge=UP)
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        tableau.scale(0.88)

        with self.voiceover(
            text=(
                "Récapitulons les deux grandes étapes dans un tableau. La "
                "transcription a lieu dans le noyau, part de l'ADN, du "
                "brin transcrit du gène, grâce à l'ARN polymérase, et "
                "produit l'ARNm. La traduction a lieu dans le cytoplasme, "
                "sur les ribosomes, part de l'ARNm, grâce au ribosome et "
                "aux ARNt, et produit la protéine."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) ---------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Une protéine est une chaîne ordonnée d'acides aminés "
                    "(20 sortes) ; sa séquence détermine sa fonction.",
                    "Un gène est un fragment d'ADN qui commande une chaîne "
                    "polypeptidique : « un gène, une chaîne "
                    "polypeptidique ».",
                    "Dogme central : l'ADN est transcrit en ARNm, puis "
                    "l'ARNm est traduit en protéine.",
                    "Le code génétique associe à chaque codon (3 "
                    "nucléotides) un acide aminé ; il est universel, "
                    "dégénéré, sans ponctuation, sans chevauchement ; AUG "
                    "= initiation, UAA/UAG/UGA = STOP.",
                    "Transcription (noyau) : ARN polymérase, ARNm "
                    "complémentaire du brin transcrit (A-U, T-A, G-C, "
                    "C-G).",
                    "Traduction (ribosomes) : initiation à AUG, "
                    "élongation par les ARNt, terminaison au codon STOP.",
                    "L'anticodon de l'ARNt est complémentaire du codon de "
                    "l'ARNm : il garantit le bon acide aminé.",
                    "Mutation = substitution, délétion ou insertion ; "
                    "silencieuse, faux-sens, non-sens, ou décalage du "
                    "cadre de lecture.",
                    "Drépanocytose : GAG devient GTG, Glu remplacé par "
                    "Val dans la bêta-globine -> globules déformés.",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si le contenu (9 points) dépasse la hauteur visible du
        # cadre malgré le petit corps de police, on réduit l'échelle globale
        # de la boîte pour qu'elle tienne entièrement à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. Une protéine est une "
                "chaîne ordonnée d'acides aminés, vingt sortes possibles ; "
                "sa séquence détermine sa fonction. Un gène est un "
                "fragment d'ADN qui commande une chaîne polypeptidique : un "
                "gène, une chaîne polypeptidique. L'information circule "
                "selon le dogme central : l'ADN est transcrit en ARNm, puis "
                "l'ARNm est traduit en protéine. Le code génétique fait "
                "correspondre à chaque codon, trois nucléotides de l'ARNm, "
                "un acide aminé ; il est universel, dégénéré, sans "
                "ponctuation et sans chevauchement ; A U G est le codon "
                "d'initiation, U A A, U A G et U G A sont les codons STOP. "
                "La transcription a lieu dans le noyau : l'ARN polymérase "
                "synthétise un ARNm complémentaire du brin transcrit. La "
                "traduction a lieu sur les ribosomes : initiation au codon "
                "A U G, élongation par enchaînement des acides aminés "
                "apportés par les ARNt, terminaison au codon STOP. "
                "L'anticodon de l'ARNt est complémentaire du codon de "
                "l'ARNm et garantit l'apport du bon acide aminé. Une "
                "mutation est une modification de la séquence de l'ADN : "
                "substitution, délétion ou insertion ; elle peut être "
                "silencieuse, faux-sens, non-sens, ou provoquer un "
                "décalage du cadre de lecture. Enfin, la drépanocytose "
                "illustre la chaîne complète : une substitution, G A G "
                "devient G T G, change un acide aminé de la bêta-globine, "
                "l'acide glutamique remplacé par la valine, ce qui déforme "
                "les globules rouges et provoque la maladie. Pour tout "
                "exercice, suis la chaîne : ADN vers ARNm par "
                "complémentarité, puis ARNm vers protéine grâce au "
                "tableau du code, puis raisonne sur les conséquences."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
