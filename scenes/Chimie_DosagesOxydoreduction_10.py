"""
scenes/Chimie_DosagesOxydoreduction_10.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 10 (dernière).

§ Méthodes, pièges à éviter et essentiel. method_box × 3 (résoudre un
exercice de dosage redox en 6 étapes, dosage avec dilution — remonter la
chaîne avec le facteur F, dosage en retour — deux bilans séparés).
warning_box × 3 pièges (le « 1 pour 1 » imaginaire, eau oxygénée réductrice
face à MnO4- pas oxydante, titre en volumes = équation de décomposition et
non celle du dosage). essentiel_box récapitulatif final du chapitre.
Source : 1ereC/Chimie.pdf, chapitre 12, pages 122-123.
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


class MethodesPiegesEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("12.10 Méthodes, pièges à éviter et l'essentiel")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------------------------
        intro = Text(
            _wrap(
                "Terminons ce chapitre par trois méthodes de résolution, "
                "trois pièges classiques à éviter, puis une synthèse "
                "complète à retenir.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons ce chapitre sur les dosages d'oxydoréduction "
                "par trois méthodes de résolution utiles, trois pièges "
                "classiques à éviter absolument, puis une synthèse "
                "complète de l'essentiel à retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : 3 méthodes ---------------------------------------------------------
        m1 = method_box(
            Text(
                _wrap(
                    "1) Résoudre un exercice de dosage redox en 6 étapes "
                    ": identifier les 2 couples et écrire les "
                    "demi-équations · en déduire l'équation-bilan · "
                    "repérer titrant/titré · repérer l'équivalence (Veq) "
                    "· écrire la relation stœchiométrique · calculer "
                    "l'inconnue.",
                    width=46,
                ),
                font_size=18,
            ),
            box_width=11.8,
        )
        m1.next_to(titre, DOWN, buff=0.4)
        _fit(m1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Première méthode : pour résoudre n'importe quel "
                "exercice de dosage redox, on suit toujours les mêmes six "
                "étapes. Un, identifier les deux couples oxydant-réducteur "
                "en présence et écrire leurs demi-équations. Deux, en "
                "déduire l'équation-bilan de la réaction de dosage. "
                "Trois, repérer clairement qui est le titrant et qui est "
                "le titré. Quatre, repérer le volume à l'équivalence, "
                "Veq, donné par l'énoncé ou l'expérience. Cinq, écrire la "
                "relation stœchiométrique adaptée. Six, enfin, calculer "
                "l'inconnue demandée."
            )
        ) as tracker:
            self.play(FadeIn(m1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m1))

        m2 = method_box(
            VGroup(
                Text(
                    _wrap(
                        "2) Dosage avec dilution : remonter la chaîne avec "
                        "le facteur de dilution F.",
                        width=46,
                    ),
                    font_size=18,
                ),
                MathTex(r"F = \dfrac{V_{\text{fille}}}{V_{\text{mère}}} \quad\Longrightarrow\quad C_{\text{mère}} = F\times C_{\text{fille}}", font_size=22, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25),
            box_width=11.8,
        )
        m2.next_to(titre, DOWN, buff=0.4)
        _fit(m2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : lorsque l'on a dilué la solution "
                "titrée avant de la doser, il faut remonter la chaîne "
                "avec le facteur de dilution F, égal au volume de la "
                "solution fille, divisé par le volume de la solution "
                "mère prélevé. La concentration de la solution mère, "
                "celle qui nous intéresse réellement, s'obtient alors en "
                "multipliant la concentration mesurée dans la solution "
                "fille par ce facteur F."
            )
        ) as tracker:
            self.play(FadeIn(m2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m2))

        m3 = method_box(
            Text(
                _wrap(
                    "3) Dosage en retour : traiter comme DEUX BILANS "
                    "séparés. Bilan 1 : réaction totale R + X (en excès de "
                    "R). Bilan 2 : dosage classique de l'excès de R "
                    "restant. Ne jamais mélanger les deux équations dans "
                    "un même calcul.",
                    width=46,
                ),
                font_size=18,
            ),
            box_width=11.8,
        )
        m3.next_to(titre, DOWN, buff=0.4)
        _fit(m3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième méthode : pour traiter un dosage en retour, il "
                "faut toujours le décomposer en deux bilans séparés. Le "
                "premier bilan concerne la réaction totale entre R, en "
                "excès, et X. Le second bilan concerne le dosage "
                "classique de l'excès de R restant. Il ne faut jamais "
                "mélanger les deux équations dans un même calcul : ce "
                "sont deux réactions chimiques bien distinctes."
            )
        ) as tracker:
            self.play(FadeIn(m3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m3))

        # --- Exemple traité : 3 pièges à éviter -------------------------------------------------
        p1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 : le « 1 pour 1 » imaginaire. Ne JAMAIS "
                    "supposer n(titrant)=n(titré) par réflexe : toujours "
                    "vérifier les coefficients stœchiométriques réels "
                    "(ex : MnO₄⁻/Fe²⁺ n'est pas 1:1 mais 1:5 !).",
                    width=46,
                ),
                font_size=18,
            ),
            box_width=11.8,
        )
        p1.next_to(titre, DOWN, buff=0.4)
        _fit(p1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Passons à trois pièges classiques. Premier piège : le "
                "« un pour un » imaginaire. Il ne faut jamais supposer, "
                "par réflexe, que la quantité de titrant égale la "
                "quantité de titré à l'équivalence : il faut toujours "
                "vérifier les coefficients stœchiométriques réels de "
                "l'équation-bilan. Le cas du permanganate et du fer deux "
                "plus en est l'exemple parfait : ce n'est pas un rapport "
                "un pour un, mais un pour cinq."
            )
        ) as tracker:
            self.play(FadeIn(p1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(p1))

        p2 = warning_box(
            Text(
                _wrap(
                    "Piège 2 : face au permanganate, l'eau oxygénée est "
                    "RÉDUCTRICE, pas oxydante. Le rôle de H₂O₂ (ampholyte "
                    "redox) dépend toujours de son partenaire de réaction "
                    "— ne jamais le fixer d'avance.",
                    width=46,
                ),
                font_size=18,
            ),
            box_width=11.8,
        )
        p2.next_to(titre, DOWN, buff=0.4)
        _fit(p2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deuxième piège : face au permanganate, l'eau oxygénée "
                "est réductrice, et non oxydante. Comme c'est un "
                "ampholyte redox, son rôle dépend toujours de son "
                "partenaire de réaction : il ne faut jamais le fixer "
                "d'avance sans regarder avec quel réactif elle réagit."
            )
        ) as tracker:
            self.play(FadeIn(p2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(p2))

        p3 = warning_box(
            Text(
                _wrap(
                    "Piège 3 : le titre en volumes T=11,2×C se calcule "
                    "avec l'équation de DÉCOMPOSITION (2H₂O₂→2H₂O+O₂), "
                    "PAS avec l'équation du dosage par le permanganate "
                    "(2MnO₄⁻+5H₂O₂+6H⁺→...) : ce sont deux réactions "
                    "différentes de H₂O₂.",
                    width=46,
                ),
                font_size=17,
            ),
            box_width=11.8,
        )
        p3.next_to(titre, DOWN, buff=0.4)
        _fit(p3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième piège, souvent source d'erreur : le titre en "
                "volumes de l'eau oxygénée se calcule à partir de "
                "l'équation de décomposition, deux H-2-O-2 donnant deux "
                "H-2-O plus O-2, et non à partir de l'équation du dosage "
                "par le permanganate. Ce sont deux réactions différentes "
                "de l'eau oxygénée, à ne surtout pas confondre dans les "
                "calculs."
            )
        ) as tracker:
            self.play(FadeIn(p3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(p3))

        # --- À retenir : essentiel_box récapitulatif final du chapitre -------------------------
        essentiel = essentiel_box(
            VGroup(
                Text(
                    _wrap(
                        "Dosage direct : solution titrante (burette) + "
                        "solution titrée (erlenmeyer), réaction TOTALE, "
                        "RAPIDE, UNIQUE. Équivalence : électrons cédés = "
                        "électrons captés.",
                        width=46,
                    ),
                    font_size=18,
                ),
                Text(
                    _wrap(
                        "Manganimétrie (MnO₄⁻) et iodométrie (I₂/S₂O₃²⁻, "
                        "directe ou indirecte via un excès d'iodure) : "
                        "deux grandes familles de dosages redox.",
                        width=46,
                    ),
                    font_size=18,
                ),
                MathTex(
                    r"\dfrac{n(Ox_1)}{a} = \dfrac{n(Red_2)}{b} \quad\text{ou}\quad \nu_{ox}C_{ox}V_{ox\,eq} = \nu_{red}C_{red}V_{red}",
                    font_size=20, color="#1A1A1A",
                ),
                Text(
                    "Dosage en retour = 2 bilans séparés, n(X) par différence.",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=12.4,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)
        _fit(essentiel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, retenons l'essentiel. Un "
                "dosage direct met en jeu une solution titrante, dans la "
                "burette, et une solution titrée, dans l'erlenmeyer, "
                "grâce à une réaction totale, rapide et unique ; "
                "l'équivalence correspond à l'égalité entre électrons "
                "cédés et électrons captés. La manganimétrie, utilisant "
                "le permanganate, et l'iodométrie, directe ou indirecte "
                "via un excès d'iodure, forment les deux grandes familles "
                "de dosages redox de ce chapitre. La relation générale à "
                "l'équivalence s'écrit soit sous forme stœchiométrique, n "
                "de Ox-1 sur a égale n de Red-2 sur b, soit sous forme "
                "électronique, nu-ox Cox Voxeq égale nu-red Cred Vred. "
                "Enfin, le dosage en retour se traite toujours comme deux "
                "bilans séparés, la quantité de X s'obtenant par "
                "différence."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
