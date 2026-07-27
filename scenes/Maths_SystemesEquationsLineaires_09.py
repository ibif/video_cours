"""
scenes/Maths_SystemesEquationsLineaires_09.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 09.

§ Mise en système d'un problème concret : méthode en 4 étapes (choix des
inconnues, mise en équations, résolution, vérification/conclusion).
Exemple résolu 9 complet (marché d'Adjamé : tomates/oignons/piment,
système 3×3, solution 2 kg / 7 kg / 1 kg).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, exercise_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MiseEnSystemeProblemesConcrets(NotionScene):
    def construct(self):
        titre = scene_title("Mise en système d'un problème concret")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Un problème concret ne se présente jamais directement "
                "sous forme d'équations : c'est à nous de traduire "
                "l'énoncé en un système, de le résoudre, puis d'interpréter "
                "le résultat dans le contexte de départ.",
                width=58,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un problème concret ne se présente jamais directement "
                "sous forme d'équations toutes prêtes : c'est à nous de "
                "traduire l'énoncé en un système, de le résoudre, puis "
                "d'interpréter le résultat dans le contexte de départ. "
                "Voyons la méthode sur un exemple complet."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : méthode en 4 étapes ------------------------------------
        methode = VGroup(
            Text("1. Choisir les inconnues et les nommer clairement.", font_size=23),
            Text("2. Traduire chaque phrase de l'énoncé par une équation.", font_size=23),
            Text("3. Résoudre le système obtenu (substitution, combinaison,", font_size=23),
            Text("    pivot de Gauss ou Cramer).", font_size=23),
            Text("4. Vérifier la solution, puis conclure DANS LE CONTEXTE.", font_size=23),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        methode_box = method_box(methode, box_width=12.0)
        methode_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici la méthode en quatre étapes. Première étape : "
                "choisir les inconnues et les nommer clairement, avec leur "
                "unité. Deuxième étape : traduire chaque phrase de "
                "l'énoncé par une équation. Troisième étape : résoudre le "
                "système obtenu, avec la méthode la plus adaptée. "
                "Quatrième étape : vérifier la solution dans l'énoncé "
                "d'origine, puis conclure en revenant au contexte concret, "
                "pas seulement à un triplet de nombres."
            )
        ) as tracker:
            self.play(FadeIn(methode_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_box))

        # --- Exemple traité 9 : énoncé -----------------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Au marché d'Adjamé, Awa achète des tomates, des "
                    "oignons et du piment, pour 10 kg au total, et dépense "
                    "4100 francs CFA (tomate : 500 F/kg, oignon : 300 F/kg, "
                    "piment : 1000 F/kg). Elle achète aussi 1 kg d'oignons "
                    "de plus que le triple du poids de tomates. Quelle "
                    "quantité de chaque produit a-t-elle achetée ?",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici l'énoncé. Au marché d'Adjamé, Awa achète des "
                "tomates, des oignons et du piment, pour dix kilogrammes au "
                "total, et dépense quatre mille cent francs C-F-A : la "
                "tomate coûte cinq cents francs le kilo, l'oignon trois "
                "cents francs le kilo, et le piment mille francs le kilo. "
                "Elle achète aussi un kilogramme d'oignons de plus que le "
                "triple du poids de tomates. Quelle quantité de chaque "
                "produit a-t-elle achetée ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Étapes 1 et 2 : inconnues + mise en équations -----------------------
        etape1 = MathTex(
            r"x = \text{kg de tomates}, \quad y = \text{kg d'oignons}, \quad z = \text{kg de piment}",
            font_size=23,
        )
        etape2 = MathTex(
            r"""
            \begin{cases}
            x+y+z=10 & \text{(poids total)} \\
            500x+300y+1000z=4100 & \text{(d\'epense totale)} \\
            y=3x+1 & \text{(relation oignons/tomates)}
            \end{cases}
            """,
            font_size=23,
        )
        etapes_12 = VGroup(etape1, etape2).arrange(DOWN, buff=0.35)
        etapes_12.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Étape un : on choisit x pour le poids de tomates, y pour "
                "celui d'oignons, z pour celui de piment, tous en "
                "kilogrammes. Étape deux : on traduit chaque phrase. Le "
                "poids total donne x plus y plus z égale dix. La dépense "
                "totale donne cinq cents x plus trois cents y plus mille z "
                "égale quatre mille cent. Et la relation entre oignons et "
                "tomates donne y égale trois x plus un."
            )
        ) as tracker:
            self.play(FadeIn(etapes_12))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes_12))

        # --- Étape 3 : résolution -----------------------------------------------------
        resol1 = MathTex(
            r"y=3x+1 \ \text{dans } x+y+z=10 \;\Rightarrow\; 4x+z=9 \;\Rightarrow\; z=9-4x",
            font_size=22,
        )
        resol2 = MathTex(
            r"500x+300(3x+1)+1000(9-4x)=4100", font_size=22,
        )
        resol3 = MathTex(
            r"500x+900x+300+9000-4000x=4100 \;\Rightarrow\; -2600x=-5200",
            font_size=21,
        )
        resol4 = MathTex(r"x=2 \;\Rightarrow\; y=3\times2+1=7 \;\Rightarrow\; z=9-4\times2=1", font_size=23, color=YELLOW)
        resol = VGroup(resol1, resol2, resol3, resol4).arrange(DOWN, buff=0.3)
        resol_box = corrige_box(resol, box_width=12.2)
        resol_box.scale(0.85)
        resol_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Étape trois, résolution par substitution. On remplace y "
                "par trois x plus un dans la première équation : quatre x "
                "plus z égale neuf, donc z égale neuf moins quatre x. On "
                "reporte y et z dans l'équation de la dépense : cinq cents "
                "x plus trois cents fois, trois x plus un, plus mille fois, "
                "neuf moins quatre x, égale quatre mille cent. En "
                "développant, on obtient moins deux mille six cents x égale "
                "moins cinq mille deux cents, donc x égale deux. On en "
                "déduit y égale trois fois deux plus un, soit sept, et z "
                "égale neuf moins quatre fois deux, soit un."
            )
        ) as tracker:
            self.play(FadeIn(resol_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resol_box))

        # --- Étape 4 : vérification et conclusion ------------------------------------
        verif = MathTex(
            r"2+7+1=10 \ \checkmark \qquad 500{\times}2+300{\times}7+1000{\times}1=4100 \ \checkmark"
            r"\qquad 7=3{\times}2+1 \ \checkmark",
            font_size=20,
        )
        conclusion = Text(
            "Awa a acheté 2 kg de tomates, 7 kg d'oignons et 1 kg de piment.",
            font_size=24,
        )
        etape4 = VGroup(verif, conclusion).arrange(DOWN, buff=0.35)
        etape4_box = corrige_box(etape4, box_width=12.2)
        etape4_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Étape quatre, vérification puis conclusion. Deux plus sept "
                "plus un égale bien dix. Cinq cents fois deux, plus trois "
                "cents fois sept, plus mille fois un, égale bien quatre "
                "mille cent. Et sept égale bien trois fois deux plus un. "
                "Les trois équations sont vérifiées. On conclut, dans le "
                "contexte du problème : Awa a acheté deux kilogrammes de "
                "tomates, sept kilogrammes d'oignons et un kilogramme de "
                "piment."
            )
        ) as tracker:
            self.play(FadeIn(etape4_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape4_box))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                "Ne JAMAIS conclure par un triplet de nombres seul (2 ; 7 ; 1) :\n"
                "revenir toujours au contexte (unités, ce que chaque inconnue\n"
                "représente) et rejeter une solution physiquement absurde\n"
                "(quantité négative, par exemple), même mathématiquement correcte.",
                font_size=21,
            ),
            box_width=12.3,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : ne jamais conclure un problème concret par "
                "un simple triplet de nombres. Il faut toujours revenir au "
                "contexte, préciser les unités et ce que chaque inconnue "
                "représente, et rejeter toute solution physiquement "
                "absurde, comme une quantité négative, même si elle est "
                "mathématiquement correcte."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
