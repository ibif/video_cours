"""
scenes/SVT_ExpressionGenetique_13.py — Chapitre 5 (1ereC, SVT), scène 13.

Méthodes et astuces : les 5 méthodes (brin complémentaire, ARNm à partir
du brin transcrit, traduire un ARNm, identifier un type de mutation,
calculs Chargaff/liaisons hydrogène) + les 4 pièges à éviter, puis
L'ESSENTIEL DU CHAPITRE (clôture). Source : 1ereC/SVT.pdf, pages 53-56.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class MethodesEtEssentielDuChapitre(NotionScene):
    def construct(self):
        titre = scene_title("Méthodes, astuces et l'essentiel du chapitre")
        titre.scale(0.55)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Pour conclure ce long chapitre, rassemblons les cinq "
                "méthodes de calcul et les quatre pièges à éviter, avant de "
                "résumer l'essentiel à retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Méthode 1 et 2 : brin complémentaire / ARNm ----------------------------
        methode_12 = method_box(
            VGroup(
                Text("1. Trouver le brin complémentaire d'ADN", font_size=19, color=YELLOW, weight="BOLD"),
                Text(
                    _wrap(
                        "Remplacer chaque base par sa complémentaire "
                        "(A↔T, G↔C), puis inverser les extrémités 5' et 3'.",
                        width=54,
                    ),
                    font_size=18,
                ),
                MathTex(r"5'\text{-ATGC-}3' \;\longrightarrow\; 3'\text{-TACG-}5'", font_size=22, color=WHITE),
                Text("2. Écrire l'ARNm à partir du brin transcrit", font_size=19, color=YELLOW, weight="BOLD"),
                Text(
                    _wrap(
                        "Complémentarité avec U à la place de T, en "
                        "inversant le sens. Si l'énoncé donne le brin non "
                        "transcrit, l'ARNm lui est identique, sauf T→U.",
                        width=54,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        methode_12.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode un : trouver le brin complémentaire d'ADN. On "
                "recopie la séquence en remplaçant chaque base par sa "
                "complémentaire, A avec T, G avec C, sans oublier d'inverser "
                "les extrémités cinq prime et trois prime. Par exemple, "
                "cinq prime, A T G C, trois prime, donne trois prime, T A C "
                "G, cinq prime. Méthode deux : écrire l'ARNm à partir du "
                "brin transcrit. Le brin transcrit sert de matrice : on "
                "applique la complémentarité avec U à la place de T, et on "
                "inverse le sens. Si l'énoncé donne plutôt le brin non "
                "transcrit, l'ARNm lui est identique, sauf que T devient U."
            )
        ) as tracker:
            self.play(FadeIn(methode_12))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_12))

        # --- Méthode 3 et 4 : traduire / identifier une mutation --------------------
        methode_34 = method_box(
            VGroup(
                Text("3. Traduire un ARNm", font_size=19, color=YELLOW, weight="BOLD"),
                Text(
                    _wrap(
                        "1) Vérifier le sens 5'→3'. 2) Repérer AUG et "
                        "découper en triplets. 3) Traduire avec la table. "
                        "4) S'arrêter au premier codon stop (non traduit).",
                        width=54,
                    ),
                    font_size=18,
                ),
                Text("4. Identifier le type d'une mutation", font_size=19, color=YELLOW, weight="BOLD"),
                Text(
                    _wrap(
                        "Aligner séquence normale et mutée, codon par "
                        "codon : même longueur → substitution (vérifier "
                        "silencieuse/faux-sens/non-sens) ; plus longue → "
                        "insertion ; plus courte → délétion (décalage du "
                        "cadre en aval).",
                        width=54,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        methode_34.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode trois : traduire un ARNm. D'abord, vérifier le "
                "sens cinq prime vers trois prime. Ensuite, repérer le "
                "codon d'initiation AUG et découper en triplets à partir de "
                "lui. Puis traduire chaque codon avec la table. Enfin, "
                "s'arrêter au premier codon stop, qui n'est pas traduit. "
                "Méthode quatre : identifier le type d'une mutation. On "
                "aligne la séquence normale et la séquence mutée, codon par "
                "codon. Même longueur, une seule base changée : c'est une "
                "substitution, à vérifier ensuite si elle est silencieuse, "
                "faux-sens ou non-sens. Séquence plus longue : une "
                "insertion. Séquence plus courte : une délétion. Dans ces "
                "deux derniers cas, le décalage du cadre modifie tous les "
                "codons en aval."
            )
        ) as tracker:
            self.play(FadeIn(methode_34))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_34))

        # --- Méthode 5 : calculs Chargaff et liaisons hydrogène ----------------------
        formule = MathTex(
            r"N_{H} = 2 \times N_{A-T} \;+\; 3 \times N_{G-C}",
            font_size=30,
            color=YELLOW,
        )
        methode_5 = method_box(
            VGroup(
                Text("5. Calculs Chargaff et liaisons hydrogène", font_size=19, color=YELLOW, weight="BOLD"),
                Text(
                    _wrap(
                        "ADN double brin : %A=%T et %G=%C (somme = 100%). "
                        "Nombre de liaisons hydrogène d'un fragment :",
                        width=54,
                    ),
                    font_size=18,
                ),
                formule,
                Text("(compter les paires A-T, les paires G-C, puis additionner)", font_size=16, color=WHITE),
            ).arrange(DOWN, buff=0.25),
            box_width=11.8,
        )
        methode_5.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode cinq : les calculs sur les bases, dits calculs de "
                "Chargaff, et sur les liaisons hydrogène. Dans un ADN "
                "double brin, le pourcentage d'adénine égale celui de "
                "thymine, le pourcentage de guanine égale celui de "
                "cytosine, et la somme des quatre pourcentages vaut cent "
                "pour cent. Pour le nombre de liaisons hydrogène d'un "
                "fragment, on compte le nombre de paires A-T, qu'on "
                "multiplie par deux, on compte le nombre de paires G-C, "
                "qu'on multiplie par trois, puis on additionne les deux "
                "résultats."
            )
        ) as tracker:
            self.play(FadeIn(methode_5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_5))

        # --- Les 4 pièges à éviter -----------------------------------------------------
        entete_pieges = Text("Les 4 pièges à éviter", font_size=24, color=YELLOW, weight="BOLD")
        entete_pieges.next_to(titre, DOWN, buff=0.45)
        pieges = _bullets(
            [
                "Piège 1 : ne pas confondre T (ADN) et U (ARN) — un ARNm "
                "ne contient jamais de T.",
                "Piège 2 : ne jamais traduire directement l'ADN — on "
                "traduit l'ARNm, codon par codon, dans le sens 5'→3'.",
                "Piège 3 : le codon stop compte pour la longueur de l'ARNm, "
                "mais pas pour le nombre d'acides aminés de la protéine "
                "(protéine de 4 a.a. = 5 codons : 4 + 1 stop).",
                "Piège 4 : le brin non transcrit n'est jamais lu par l'ARN "
                "polymérase — c'est le brin transcrit (matrice) qui est lu.",
            ],
            font_size=18,
            width=56,
        )
        pieges.next_to(entete_pieges, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici les quatre pièges à éviter absolument. Piège un : ne "
                "pas confondre T, la thymine de l'ADN, et U, l'uracile de "
                "l'ARN — un ARNm ne contient jamais de T. Piège deux : ne "
                "jamais traduire directement l'ADN, on traduit toujours "
                "l'ARNm, codon par codon, dans le sens cinq prime vers "
                "trois prime — traduire l'ADN, ou traduire dans le mauvais "
                "sens, est l'erreur la plus fréquente aux devoirs. Piège "
                "trois : le codon stop compte pour la longueur de l'ARNm, "
                "mais pas pour le nombre d'acides aminés de la protéine — "
                "une protéine de quatre acides aminés correspond à cinq "
                "codons, quatre codons plus un stop. Piège quatre : le brin "
                "non transcrit n'est jamais lu par l'ARN polymérase, c'est "
                "toujours le brin transcrit, la matrice, qui est lu."
            )
        ) as tracker:
            self.play(FadeIn(entete_pieges))
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pieges), FadeOut(pieges))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) --------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "ADN = double hélice antiparallèle de nucléotides "
                    "(sucre + phosphate + base A/T/G/C) ; A-T (2 liaisons "
                    "H), G-C (3 liaisons H) ; %A=%T, %G=%C.",
                    "Dogme central : ADN → (transcription, noyau) → ARNm "
                    "→ (traduction, cytoplasme) → protéine. Sens unique.",
                    "Transcription : ARN polymérase lit le brin transcrit "
                    "3'→5', synthétise l'ARNm 5'→3' (U remplace T).",
                    "Code génétique : 64 codons (triplets), dégénéré, AUG "
                    "= initiation, UAA/UAG/UGA = stop, quasi universel.",
                    "Traduction : ribosome + ARNt (anticodon) + acides "
                    "aminés ; initiation → élongation → terminaison.",
                    "Mutations : substitution (silencieuse/faux-sens/"
                    "non-sens) vs insertion/délétion (décalage du cadre, "
                    "plus graves). Exemple : drépanocytose (GAG→GUG, "
                    "Glu→Val).",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)

        # Garde-fou : si le contenu déborde la hauteur visible, on réduit
        # l'échelle globale de la boîte pour qu'elle tienne à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel de ce long chapitre. L'ADN est une "
                "double hélice antiparallèle de nucléotides, chacun formé "
                "d'un sucre, d'un phosphate et d'une base A, T, G ou C ; A "
                "s'apparie avec T par deux liaisons hydrogène, G avec C par "
                "trois liaisons hydrogène, et le pourcentage d'A égale "
                "celui de T, celui de G égale celui de C. Le dogme central "
                "relie l'ADN à la protéine en un seul sens : transcription "
                "dans le noyau pour obtenir l'ARN messager, puis traduction "
                "dans le cytoplasme pour obtenir la protéine. Pendant la "
                "transcription, l'ARN polymérase lit le brin transcrit dans "
                "le sens trois prime vers cinq prime, et synthétise l'ARNm "
                "dans le sens cinq prime vers trois prime, en remplaçant T "
                "par U. Le code génétique compte soixante-quatre codons, "
                "des triplets, un code dégénéré, avec AUG pour "
                "l'initiation et trois codons stop. La traduction associe "
                "le ribosome, les ARN de transfert et leurs anticodons, et "
                "les acides aminés, en trois étapes : initiation, "
                "élongation, terminaison. Enfin, les mutations peuvent être "
                "des substitutions, silencieuses, faux-sens ou non-sens, ou "
                "des insertions et délétions, plus graves car elles "
                "décalent tout le cadre de lecture — comme l'illustre "
                "l'exemple de la drépanocytose, où le codon GAG devient GUG "
                "et l'acide glutamique devient une valine."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
