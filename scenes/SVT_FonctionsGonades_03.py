"""
scenes/SVT_FonctionsGonades_03.py — Chapitre 1 (1ereD, SVT), scène 03.

§ 1.2 Mise en évidence expérimentale des deux fonctions des gonades :
castration, greffe/injection d'extraits, ligature des voies génitales,
propriété des deux fonctions, exemple des taureaux, méthode d'exploitation
d'un protocole, piège vasectomie ≠ castration, application chapon/bœuf.
Source : 1ereD/SVT.pdf, pages 7-9.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class MiseEnEvidenceDesDeuxFonctions(NotionScene):
    def construct(self):
        titre = scene_title("1.2 — Mise en évidence expérimentale")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : la démarche expérimentale ---------------------------
        demarche = Text(
            _wrap(
                "Comment découvrir le rôle d'un organe qu'on ne peut pas "
                "ouvrir chez l'être humain ? Une démarche expérimentale en "
                "trois temps : 1) retirer l'organe et observer les "
                "troubles ; 2) restituer l'organe ou ses extraits et "
                "observer la guérison ; 3) couper ses canaux pour "
                "distinguer ce qui sort par les canaux de ce qui passe "
                "dans le sang.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        demarche.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment un scientifique découvre-t-il le rôle d'un organe "
                "qu'il ne peut pas ouvrir chez l'être humain ? Il applique une "
                "démarche expérimentale classique en trois temps : retirer "
                "l'organe et observer les troubles ; restituer l'organe ou "
                "ses extraits et observer la guérison ; puis couper ses "
                "canaux d'évacuation pour distinguer ce qui sort par les "
                "canaux de ce qui passe dans le sang."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(demarche))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demarche))

        # --- Raisonnement 1 : la castration --------------------------------
        entete1 = Text("1.2.1 — La castration", font_size=27, color=YELLOW, weight="BOLD")
        entete1.next_to(titre, DOWN, buff=0.5)

        castration = _bullets(
            [
                "Chez le coq castré : crête et barbillons pâlissent et "
                "retombent, chant rare, comportement sexuel disparu, "
                "sperme sans spermatozoïdes.",
                "Chez le rat castré : glandes annexes atrophiées, "
                "testostérone effondrée.",
                "Chez la rate ovariectomisée : utérus atrophié, cycles "
                "ovariens arrêtés.",
            ],
            width=50,
        )
        castration.next_to(entete1, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier temps : la castration, ablation chirurgicale des "
                "gonades. Chez le coq castré, la crête et les barbillons "
                "pâlissent et retombent, le chant devient rare, le "
                "comportement sexuel disparaît, et l'examen du sperme montre "
                "l'absence totale de spermatozoïdes. Chez le rat mâle castré, "
                "les glandes annexes s'atrophient et le taux de testostérone "
                "s'effondre. Chez la rate dont on retire les ovaires, "
                "l'utérus s'atrophie et les cycles ovariens s'arrêtent."
            )
        ) as tracker:
            self.play(FadeIn(entete1))
            self.play(FadeIn(castration))
            self.wait(tracker.get_remaining_duration())

        conclusion1 = Text(
            _wrap(
                "1er enseignement : les gonades entretiennent à distance "
                "les caractères sexuels et sont indispensables à la "
                "production des gamètes.",
                width=52,
            ),
            font_size=24,
            color=YELLOW,
        )
        conclusion1.next_to(castration, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier enseignement : les gonades entretiennent à distance "
                "les caractères sexuels, les glandes annexes et les "
                "comportements, et elles sont indispensables à la production "
                "des gamètes."
            )
        ) as tracker:
            self.play(FadeIn(conclusion1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete1), FadeOut(castration), FadeOut(conclusion1))

        # --- Raisonnement 2 : greffes et injections d'extraits ------------
        entete2 = Text("1.2.2 — Greffes et injections d'extraits", font_size=27, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.5)

        greffe = _bullets(
            [
                "Berthold (1849) : greffe d'un testicule dans l'abdomen "
                "d'un coq castré -> la crête et le comportement "
                "réapparaissent.",
                "Même résultat avec un simple extrait testiculaire "
                "broyé, injecté n'importe où dans le corps.",
                "Aucun canal ni nerf reconnecté -> une seule route "
                "possible : le sang.",
            ],
            width=50,
        )
        greffe.next_to(entete2, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième temps : dès 1849, le physiologiste allemand "
                "Berthold greffa un testicule dans l'abdomen d'un coq castré "
                "; la crête redevint rouge et dressée, le chant et le "
                "comportement sexuel réapparurent. Plus remarquable encore, "
                "l'injection d'un simple extrait testiculaire broyé produit "
                "les mêmes effets. Or, si un extrait broyé, déposé n'importe "
                "où dans le corps, suffit à restaurer les caractères sexuels, "
                "et que la greffe agit sans qu'aucun canal ni nerf ne soit "
                "reconnecté, cette substance ne peut emprunter qu'une seule "
                "route : le sang."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(greffe))
            self.wait(tracker.get_remaining_duration())

        conclusion2 = Text(
            _wrap(
                "Conclusion : le testicule libère dans le sang une ou "
                "plusieurs hormones. Les mêmes expériences chez la femelle "
                "(ovaire) mènent à la même conclusion.",
                width=52,
            ),
            font_size=24,
            color=YELLOW,
        )
        conclusion2.next_to(greffe, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On conclut donc que le testicule libère dans le sang une ou "
                "plusieurs hormones. Les mêmes expériences réalisées chez la "
                "femelle, greffe d'ovaire et injection d'extraits ovariens, "
                "conduisent à la même conclusion pour l'ovaire."
            )
        ) as tracker:
            self.play(FadeIn(conclusion2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete2), FadeOut(greffe), FadeOut(conclusion2))

        # --- Raisonnement 3 : la ligature des voies génitales --------------
        entete3 = Text("1.2.3 — La ligature des voies génitales", font_size=27, color=YELLOW, weight="BOLD")
        entete3.next_to(titre, DOWN, buff=0.5)

        ligature = _bullets(
            [
                "Canaux déférents ligaturés, testicules intacts.",
                "Sperme éjaculé sans spermatozoïdes (azoospermie).",
                "Testostérone sanguine normale, caractères et "
                "comportement sexuels maintenus.",
                "À long terme : tubes séminifères dégénèrent, cellules "
                "interstitielles restent intactes.",
            ],
            width=50,
        )
        ligature.next_to(entete3, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième temps : ligaturons les canaux déférents d'un rat "
                "mâle, sans toucher aux testicules. Le sperme éjaculé ne "
                "contient plus aucun spermatozoïde, on parle d'azoospermie. "
                "Mais, et c'est le point capital, le taux sanguin de "
                "testostérone reste normal, les caractères sexuels sont "
                "maintenus et le comportement sexuel persiste. À long terme, "
                "les tubes séminifères dégénèrent, tandis que les cellules "
                "interstitielles restent intactes."
            )
        ) as tracker:
            self.play(FadeIn(entete3))
            self.play(FadeIn(ligature))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete3), FadeOut(ligature))

        # --- Propriété : les deux fonctions des gonades --------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Toute gonade exerce une double fonction : une "
                    "fonction exocrine (génitale), production de gamètes "
                    "libérés par les voies génitales ; et une fonction "
                    "endocrine, production d'hormones sexuelles libérées "
                    "directement dans le sang.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        propriete.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Cette expérience dissocie nettement deux productions : celle "
                "qui emprunte les canaux, les gamètes, et celle qui passe "
                "dans le sang, les hormones, indépendante des canaux. Toute "
                "gonade exerce donc une double fonction : une fonction "
                "exocrine, ou fonction génitale, qui produit des gamètes "
                "libérés par les voies génitales ; et une fonction endocrine, "
                "qui produit des hormones sexuelles libérées directement dans "
                "le sang."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple traité : les taureaux de Yamoussoukro -----------------
        exemple = example_box(
            Text(
                _wrap(
                    "Trois lots de taureaux : Témoin (spermatozoïdes "
                    "présents, testostérone normale, vigueur) ; Castration "
                    "(spermatozoïdes absents, testostérone effondrée, "
                    "docilité) ; Canaux ligaturés (spermatozoïdes absents "
                    "dans l'éjaculat, testostérone normale, vigueur "
                    "conservée). La comparaison Témoin-Castration montre "
                    "que la castration supprime gamètes ET hormone ; la "
                    "comparaison Témoin-Ligature montre que la ligature "
                    "supprime seulement la sortie des gamètes.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un éleveur de Yamoussoukro soumet des taureaux à trois "
                "protocoles. Lot témoin : spermatozoïdes présents, "
                "testostérone normale, vigueur et rut. Lot castré : "
                "spermatozoïdes absents, testostérone effondrée, docilité et "
                "engraissement. Lot aux canaux déférents ligaturés : "
                "spermatozoïdes absents dans l'éjaculat, mais testostérone "
                "normale, vigueur et rut conservés. La comparaison "
                "témoin-castration montre que la castration supprime à la "
                "fois les gamètes et l'hormone ; la comparaison "
                "témoin-ligature montre que la ligature supprime seulement "
                "l'arrivée des gamètes."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        methode = method_box(
            Text(
                _wrap(
                    "Étape 1 : identifier le facteur modifié (organe "
                    "retiré, greffé, canal ligaturé). Étape 2 : comparer "
                    "témoin et lot expérimental, résultats chiffrés à "
                    "l'appui. Étape 3 : formuler une observation précise. "
                    "Étape 4 : conclure en reliant l'observation à la "
                    "fonction de l'organe, sans dépasser ce que permettent "
                    "les résultats.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour exploiter un protocole expérimental, une méthode en "
                "quatre étapes. Étape un : identifier le facteur modifié par "
                "l'expérimentateur. Étape deux : comparer le lot témoin et le "
                "lot expérimental, en citant les résultats chiffrés. Étape "
                "trois : formuler une observation précise. Étape quatre : "
                "conclure en reliant l'observation à la fonction de l'organe, "
                "sans jamais dépasser ce que les résultats permettent "
                "d'affirmer."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- À retenir : application chapon / bœuf --------------------------
        application = Text(
            _wrap(
                "Application : l'éleveur ivoirien qui castre un coq "
                "(chapon) ou un jeune taureau (bœuf) supprime la source de "
                "testostérone. Privé de cette hormone, l'animal est plus "
                "calme, dépense moins d'énergie en parades et en combats, "
                "et transforme davantage de nourriture en chair.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        application.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Cette connaissance explique une pratique d'élevage très "
                "répandue en Afrique de l'Ouest : l'éleveur ivoirien qui "
                "castre un coq pour en faire un chapon, ou un jeune taureau "
                "pour en faire un bœuf, supprime la source de testostérone. "
                "Privé de cette hormone, l'animal devient plus calme, dépense "
                "moins d'énergie en parades et en combats, et transforme une "
                "plus grande part de sa nourriture en chair."
            )
        ) as tracker:
            self.play(FadeIn(application))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(application))

        # --- Piège à éviter : vasectomie ≠ castration -----------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Erreur fréquente : écrire que la ligature des canaux "
                    "déférents (vasectomie) « supprime les hormones » ou "
                    "« rend impuissant ». C'est faux : la fonction "
                    "endocrine, indépendante des canaux, est conservée ; "
                    "seule la sortie des gamètes est bloquée. Aucune "
                    "hormone ne circule dans un canal déférent ou une "
                    "trompe : toute hormone passe par le sang.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Erreur très fréquente au baccalauréat : écrire que la "
                "ligature des canaux déférents, la vasectomie, supprime les "
                "hormones ou rend impuissant. C'est faux : la fonction "
                "endocrine, qui ne dépend pas des canaux, est conservée ; "
                "seule la sortie des gamètes est bloquée. Retenez aussi "
                "qu'aucune hormone ne circule dans les canaux déférents ni "
                "dans les trompes : toute hormone est libérée dans le sang."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
