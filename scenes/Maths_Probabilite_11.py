"""
scenes/Maths_Probabilite_11.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 11 (dernière).

§ Jeux de hasard, jeux équitables, méthodes et pièges à éviter
(synthèse) : gain algébrique G = somme reçue − mise, jeu équitable
(E(G)=0), favorable (E(G)>0), défavorable (E(G)<0). Exemple résolu
complet : mise 1000F, urne de 5 boules (2×« 3000F », 1×« 1000F »,
2×« 0F »), E(G)=400 ⟹ jeu favorable au joueur. Synthèse méthodes
(4 method_box) et pièges à éviter (4 warning_box). essentiel_box
récapitulatif final du chapitre.
Source : 1ereC/Maths.pdf, pages 152-153.
"""

import textwrap

from manim import DOWN, RIGHT, UP, WHITE, YELLOW, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _urne_gains() -> VGroup:
    etiquettes = ["3000F", "3000F", "1000F", "0F", "0F"]
    boules = VGroup()
    for texte in etiquettes:
        jeton = Dot(radius=0.35, color="#DE7C1F" if texte != "0F" else WHITE)
        label = Text(texte, font_size=14, color=WHITE if texte != "0F" else "#1A1A1A")
        label.move_to(jeton.get_center())
        boules.add(VGroup(jeton, label))
    boules.arrange(RIGHT, buff=0.35)
    return boules


class JeuxHasardSynthese(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Jeux de hasard et synthèse")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Pour clore ce chapitre : appliquons l'espérance "
                "mathématique à un jeu de hasard, pour savoir s'il est "
                "avantageux ou non de jouer.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour clore ce chapitre, appliquons l'espérance "
                "mathématique à un jeu de hasard, afin de déterminer s'il "
                "est avantageux ou non de jouer."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : gain algébrique + jeu équitable ------------------------
        def_gain = definition_box(
            VGroup(
                Text("Gain algébrique G", font_size=23, weight="BOLD"),
                MathTex(r"G = \text{somme reçue} - \text{mise}", font_size=26),
                Text(_wrap("G peut être négatif (le joueur perd) : c'est un gain ALGÉBRIQUE.", width=44), font_size=20),
            ).arrange(DOWN, buff=0.25),
        )
        def_gain.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans un jeu d'argent, le gain algébrique G d'un joueur "
                "est la somme qu'il reçoit, moins la mise qu'il a versée "
                "pour jouer. G peut parfaitement être négatif, lorsque le "
                "joueur perd : c'est bien pour cela qu'on parle de gain "
                "algébrique."
            )
        ) as tracker:
            self.play(FadeIn(def_gain))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_gain))

        def_equitable = definition_box(
            VGroup(
                Text("Jeu équitable, favorable, défavorable", font_size=22, weight="BOLD"),
                MathTex(r"E(G) = 0 \ : \ \text{jeu ÉQUITABLE}", font_size=23),
                MathTex(r"E(G) > 0 \ : \ \text{jeu FAVORABLE au joueur}", font_size=23),
                MathTex(r"E(G) < 0 \ : \ \text{jeu DÉFAVORABLE au joueur}", font_size=23),
            ).arrange(DOWN, buff=0.22),
        )
        def_equitable.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On classe alors le jeu selon le signe de l'espérance du "
                "gain. Si E de G vaut exactement 0, le jeu est dit "
                "équitable : sur le long terme, ni le joueur ni "
                "l'organisateur n'a l'avantage. Si E de G est strictement "
                "positive, le jeu est favorable au joueur. Et si E de G "
                "est strictement négative, le jeu lui est défavorable — "
                "ce qui est le cas, en pratique, de la quasi-totalité des "
                "jeux d'argent organisés."
            )
        ) as tracker:
            self.play(Write(def_equitable))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_equitable))

        # --- Exemple résolu complet ------------------------------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu : mise de 1000F pour tirer une boule "
                "dans une urne de 5 boules — 2 donnent 3000F, 1 donne "
                "1000F, 2 ne donnent rien.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)
        urne = _urne_gains()
        urne.next_to(enonce, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu complet. Un joueur mise 1000 francs pour "
                "tirer une boule dans une urne de 5 boules indiscernables "
                "au toucher : 2 boules font gagner 3000 francs, 1 boule "
                "fait gagner 1000 francs, et 2 boules ne rapportent rien."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.play(FadeIn(urne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce), FadeOut(urne))

        loi_G_titre = Text("Loi du gain algébrique G (après déduction de la mise)", font_size=19, weight="BOLD")
        loi_G = MathTex(
            r"g_i:\ 2000 \quad 0 \quad -1000 \qquad\qquad P(G=g_i):\ \tfrac{2}{5} \quad \tfrac{1}{5} \quad \tfrac{2}{5}",
            font_size=19,
        )
        bloc_loi = VGroup(loi_G_titre, loi_G).arrange(DOWN, buff=0.3)
        bloc_loi.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Établissons la loi du gain algébrique G, en n'oubliant "
                "jamais de retrancher la mise de 1000 francs à chaque "
                "somme reçue. Avec les 2 boules à 3000 francs : gain "
                "algébrique 2000 francs, probabilité 2 cinquièmes. Avec "
                "la boule à 1000 francs : gain algébrique 0, probabilité "
                "1 cinquième. Et avec les 2 boules à 0 franc : gain "
                "algébrique moins 1000 francs, probabilité 2 cinquièmes."
            )
        ) as tracker:
            self.play(Write(loi_G_titre))
            self.play(Write(loi_G))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_loi))

        calcul_E = MathTex(
            r"E(G) = \tfrac{2}{5}\times 2000 + \tfrac{1}{5}\times 0 + \tfrac{2}{5}\times(-1000)",
            font_size=23,
        )
        calcul_E2 = MathTex(r"= 800 + 0 - 400 = 400", font_size=25)
        conclusion = MathTex(r"E(G) = 400 > 0 \ \Rightarrow\ \text{jeu FAVORABLE au joueur}", font_size=26, color=YELLOW)
        bloc_calcul = VGroup(calcul_E, calcul_E2, conclusion).arrange(DOWN, buff=0.35)
        bloc_calcul.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'espérance de G vaut donc 2 cinquièmes fois 2000, plus "
                "1 cinquième fois 0, plus 2 cinquièmes fois moins 1000, "
                "soit 800 plus 0 moins 400, égale 400. Comme E de G est "
                "strictement positive, ce jeu est favorable au joueur : en "
                "moyenne, sur le long terme, il gagne 400 francs par "
                "partie."
            )
        ) as tracker:
            self.play(Write(calcul_E))
            self.play(Write(calcul_E2))
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_calcul))

        # --- Synthèse méthodes : 4 method_box --------------------------------------
        meth1 = method_box(
            VGroup(
                Text("Méthode 1 — Reconnaître l'équiprobabilité", font_size=19, weight="BOLD"),
                Text(_wrap("« équilibré », « non truqué », « indiscernables », « au hasard » → équiprobabilité.", width=46), font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        meth1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, synthétisons les méthodes et "
                "les pièges essentiels. Méthode 1 : repérer immédiatement "
                "les mots-clés qui signalent l'équiprobabilité — "
                "« équilibré », « non truqué », « indiscernables », "
                "« au hasard »."
            )
        ) as tracker:
            self.play(FadeIn(meth1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth1))

        meth2 = method_box(
            VGroup(
                Text("Méthode 2 — Bien choisir l'univers Ω", font_size=19, weight="BOLD"),
                Text(_wrap("Pour 2 dés, prendre les 36 COUPLES, jamais les 11 sommes (non équiprobables).", width=46), font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        meth2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode 2 : bien choisir l'univers équiprobable sur "
                "lequel travailler — pour deux dés, ce sont les 36 "
                "couples de résultats, jamais les 11 sommes possibles, qui "
                "ne sont pas équiprobables entre elles."
            )
        ) as tracker:
            self.play(FadeIn(meth2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth2))

        meth3 = method_box(
            VGroup(
                Text("Méthode 3 — « au moins un » → complémentaire", font_size=19, weight="BOLD"),
                Text(_wrap("Passer systématiquement par l'événement contraire, presque toujours plus rapide.", width=46), font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        meth3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode 3 : dès qu'un énoncé contient « au moins un », "
                "passer systématiquement par l'événement contraire, "
                "presque toujours beaucoup plus rapide à dénombrer."
            )
        ) as tracker:
            self.play(FadeIn(meth3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth3))

        meth4 = method_box(
            VGroup(
                Text("Méthode 4 — Construire une loi en 3 étapes", font_size=19, weight="BOLD"),
                Text(_wrap("1) Lister X(Ω). 2) Calculer chaque P(X=x_i). 3) Vérifier que la somme vaut 1.", width=46), font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        meth4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode 4, enfin : pour construire une loi de "
                "probabilité, procéder toujours en trois étapes — lister "
                "X de Ω, calculer chaque probabilité P de X égale x-i, "
                "puis vérifier obligatoirement que leur somme vaut 1."
            )
        ) as tracker:
            self.play(FadeIn(meth4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(meth4))

        # --- Pièges à éviter : 4 warning_box ----------------------------------------
        piege1 = warning_box(
            VGroup(
                Text("Piège 1 — Additionner sans retrancher l'intersection", font_size=18, weight="BOLD"),
                MathTex(r"A,B \text{ compatibles} \Rightarrow P(A\cup B) = P(A)+P(B)-P(A\cap B)", font_size=19),
            ).arrange(DOWN, buff=0.2),
        )
        piege1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège 1 : si A et B ne sont pas incompatibles, ne jamais "
                "se contenter d'additionner P de A et P de B — il faut "
                "impérativement retrancher P de A inter B, sous peine de "
                "compter deux fois les issues communes."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            VGroup(
                Text("Piège 2 — Confondre incompatibles et contraires", font_size=18, weight="BOLD"),
                Text(_wrap("Contraires ⟹ incompatibles, mais l'inverse est FAUX (voir scène 3).", width=46), font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        piege2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège 2 : ne pas confondre événements incompatibles et "
                "événements contraires. Être contraires entraîne "
                "toujours être incompatibles, mais la réciproque est "
                "fausse, comme nous l'avons vu."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            VGroup(
                Text("Piège 3 — Oublier de retrancher la mise", font_size=18, weight="BOLD"),
                Text(_wrap("Calculer l'espérance du gain NET (après mise), jamais celle du gain BRUT.", width=46), font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège 3 : dans un jeu de hasard, toujours calculer "
                "l'espérance du gain NET, c'est-à-dire après déduction de "
                "la mise, jamais celle du gain BRUT, la somme reçue seule "
                "— sinon la conclusion sur le caractère favorable ou "
                "défavorable du jeu est totalement faussée."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            VGroup(
                Text("Piège 4 — Arrondir trop tôt", font_size=18, weight="BOLD"),
                Text(_wrap("Garder les FRACTIONS EXACTES tout au long du calcul ; n'arrondir qu'au tout dernier résultat.", width=46), font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        piege4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège 4, enfin : ne jamais arrondir les probabilités "
                "trop tôt dans un calcul. Garder les fractions exactes "
                "tout au long du raisonnement, et n'arrondir, si "
                "nécessaire, qu'au tout dernier résultat, comme nous "
                "l'avons fait pour racine de 2 sur 2."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- L'essentiel à retenir : récapitulatif du chapitre -----------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre Probabilité", font_size=21, weight="BOLD"),
                MathTex(r"P(A) = \dfrac{\mathrm{Card}(A)}{\mathrm{Card}(\Omega)} \ \text{(équiprobabilité)} \qquad P(\overline{A}) = 1-P(A)", font_size=19),
                MathTex(r"P(A\cup B) = P(A)+P(B)-P(A\cap B)", font_size=19),
                MathTex(r"E(X) = \textstyle\sum_i p_i x_i \qquad V(X) = E(X^2)-[E(X)]^2 \qquad \sigma(X)=\sqrt{V(X)}", font_size=18),
                MathTex(r"\text{Jeu : } E(G)=0 \text{ équitable}, \ E(G)>0 \text{ favorable}, \ E(G)<0 \text{ défavorable}", font_size=18),
            ).arrange(DOWN, buff=0.22),
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, voici l'essentiel à retenir. "
                "En situation d'équiprobabilité, la probabilité d'un "
                "événement est le rapport des cardinaux, cas favorables "
                "sur cas possibles. La probabilité du contraire vaut 1 "
                "moins la probabilité de l'événement. La probabilité "
                "d'une réunion s'obtient en retranchant celle de "
                "l'intersection. L'espérance d'une variable aléatoire est "
                "la somme des p-i fois x-i ; sa variance s'obtient par la "
                "formule de König-Huygens, et son écart-type en est la "
                "racine carrée. Enfin, pour un jeu de hasard, le signe de "
                "l'espérance du gain algébrique indique s'il est "
                "équitable, favorable ou défavorable au joueur. Avec ces "
                "outils, vous êtes prêts à résoudre tous les problèmes de "
                "probabilité du programme."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
