"""
scenes/SVT_StructureInterneGlobe_14.py — Chapitre 7 (1ereC, SVT), scène 14.

§ Méthodes et astuces : méthode « lire un sismogramme » (Δt, formule
distance épicentrale, trilatération), méthode « exploiter un graphique
vitesse/profondeur », méthode « les 4 calculs types » + les 3 pièges + les
3 astuces mnémotechniques, puis L'ESSENTIEL DU CHAPITRE (clôture).
Source : 1ereC/SVT.pdf, pages 78-79.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _garde_fou(mobject):
    bas_visible = -config.frame_height / 2 + 0.3
    hauteur_dispo = mobject.get_top()[1] - bas_visible
    if mobject.height > hauteur_dispo > 0:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())


class MethodesAstucesEtEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("Méthodes, astuces et essentiel du chapitre")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : trois méthodes à maîtriser pour les calculs -------------
        intro = Text(
            _wrap(
                "Ce chapitre calculatoire repose sur quelques méthodes "
                "réutilisables. Passons-les en revue avant la synthèse "
                "finale.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ce chapitre calculatoire repose sur quelques méthodes "
                "réutilisables. Passons-les en revue avant la synthèse "
                "finale."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Méthode 1 : lire un sismogramme ------------------------------------
        methode_sismo = method_box(
            Text(
                _wrap(
                    "Lire un sismogramme : 1. Repérer la 1ère arrivée "
                    "(ondes P, les plus rapides). 2. Repérer la 2e arrivée "
                    "(ondes S). 3. Mesurer Δt=tS-tP. 4. Distance "
                    "épicentrale : d=Δt×vP×vS/(vP-vS). 5. Une seule station "
                    "= un cercle ; il faut 3 stations (trilatération) pour "
                    "localiser l'épicentre.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=11.9,
        )
        methode_sismo.next_to(titre, DOWN, buff=0.45)

        formule_d = MathTex(r"d = \Delta t \times \dfrac{v_P \times v_S}{v_P - v_S}", font_size=28, color=YELLOW)
        formule_d.next_to(methode_sismo, DOWN, buff=0.3)
        bloc_sismo = VGroup(methode_sismo, formule_d)
        _garde_fou(bloc_sismo)

        with self.voiceover(
            text=(
                "Première méthode : lire et exploiter un sismogramme. "
                "Étape un, repérer la première arrivée d'ondes, les ondes "
                "P, les plus rapides. Étape deux, repérer la seconde "
                "arrivée, les ondes S. Étape trois, mesurer l'écart de "
                "temps delta t entre les deux arrivées. Étape quatre, plus "
                "delta t est grand, plus la station est loin de "
                "l'épicentre : la distance épicentrale se calcule par d "
                "égale delta t fois vP fois vS, divisé par vP moins vS. "
                "Étape cinq, une seule station ne donne qu'un cercle de "
                "positions possibles : il faut trois stations pour "
                "localiser l'épicentre, par trilatération."
            )
        ) as tracker:
            self.play(FadeIn(methode_sismo))
            self.play(Write(formule_d))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_sismo), FadeOut(formule_d))

        # --- Méthode 2 : exploiter un graphique vitesse/profondeur ------------
        methode_graphique = method_box(
            Text(
                _wrap(
                    "Exploiter un graphique vitesse/profondeur : toute "
                    "rupture brutale de la courbe = une discontinuité "
                    "(relever sa profondeur, la nommer). Si vS=0 sur un "
                    "intervalle → milieu liquide (noyau externe). Si vP "
                    "augmente brutalement → milieu plus dense/solide (Moho, "
                    "Lehmann) ; si elle chute → milieu moins rigide "
                    "(Gutenberg).",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=11.9,
        )
        methode_graphique.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième méthode : exploiter un graphique vitesse des "
                "ondes en fonction de la profondeur. Toute rupture brutale "
                "de la courbe signale une discontinuité : il faut relever "
                "sa profondeur et la nommer. Si vS est nulle sur un "
                "intervalle, c'est un milieu liquide, le noyau externe. Si "
                "vP augmente brutalement, c'est un passage à un milieu plus "
                "dense ou plus solide, comme au Moho ou à Lehmann ; si elle "
                "chute, c'est un milieu moins rigide, comme à Gutenberg."
            )
        ) as tracker:
            self.play(FadeIn(methode_graphique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_graphique))

        # --- Méthode 3 : les 4 calculs types -------------------------------------
        methode_calculs = method_box(
            Text(
                "Les quatre calculs types du chapitre :",
                font_size=22,
            ),
            box_width=11.9,
        )
        methode_calculs.next_to(titre, DOWN, buff=0.45)

        formules4 = VGroup(
            MathTex(r"\text{Vitesse : } v = \dfrac{d}{t}", font_size=22, color=YELLOW),
            MathTex(r"\text{Densité : } \rho = \dfrac{M}{V},\ V = \dfrac{4}{3}\pi R^3", font_size=22, color=YELLOW),
            MathTex(r"\text{Pression : } P = \rho \times g \times h", font_size=22, color=YELLOW),
            MathTex(r"\text{Température : } T = T_0 + G \times z", font_size=22, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        formules4.next_to(methode_calculs, DOWN, buff=0.3)
        bloc_calculs = VGroup(methode_calculs, formules4)
        _garde_fou(bloc_calculs)

        with self.voiceover(
            text=(
                "Troisième méthode : les quatre calculs types de ce "
                "chapitre. La vitesse d'une onde, v égale d sur t, en "
                "convertissant le temps en secondes. La densité moyenne, "
                "rho égale M sur V, avec V égale quatre tiers pi R cube. La "
                "pression, P égale rho fois g fois h, la profondeur en "
                "mètres. Et la température, T égale T zéro plus G fois z. "
                "Vérifiez toujours l'homogénéité des unités avant de "
                "calculer."
            )
        ) as tracker:
            self.play(FadeIn(methode_calculs))
            self.play(Write(formules4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_calculs), FadeOut(formules4))

        # --- Exemple traité : application des 3 pièges et 3 astuces ----------
        pieges = warning_box(
            _bullets(
                [
                    "Ne pas confondre découpage chimique et découpage mécanique.",
                    "L'asthénosphère n'est pas un océan de magma (seulement 1-10 % fondue).",
                    "La graine est solide malgré 5000-6000°C, grâce à la pression.",
                ],
                font_size=18,
                width=48,
            ),
            box_width=11.9,
        )
        pieges.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois pièges à éviter absolument. Un : ne pas confondre le "
                "découpage chimique, croûte-manteau-noyau, avec le "
                "découpage mécanique, lithosphère-asthénosphère. Deux : "
                "l'asthénosphère n'est pas un océan de magma, c'est une "
                "roche solide contenant seulement un à dix pour cent de "
                "liquide — la preuve, les ondes S la traversent. Trois : la "
                "graine est solide malgré cinq mille à six mille degrés, "
                "grâce à la pression : ne jamais écrire que tout le noyau "
                "est liquide."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges))

        astuces = _bullets(
            [
                "Astuce 1 : P=Primaire/Pression, arrive en Premier, Passe partout. S=Secondaire/Shear, arrive en Second, S'arrête (Stop) dans les liquides.",
                "Astuce 2 : Moho, Gutenberg (Grand choc, S disparaissent), Lehmann (Liquide s'arrête). Profondeurs : 2 900 km et 5 150 km ; centre à 6 371 km.",
                "Astuce 3 : Continent=granite (clair), océan=basalte (noir), manteau=péridotite (verte), noyau=fer-nickel (sidérites).",
            ],
            font_size=17,
            width=52,
        )
        entete_astuces = Text("Trois astuces mnémotechniques", font_size=23, color=YELLOW, weight="BOLD")
        entete_astuces.next_to(titre, DOWN, buff=0.45)
        astuces.next_to(entete_astuces, DOWN, buff=0.35)
        bloc_astuces = VGroup(entete_astuces, astuces)
        _garde_fou(bloc_astuces)

        with self.voiceover(
            text=(
                "Et trois astuces mnémotechniques pour ne jamais se "
                "tromper. Astuce un, pour les ondes : P comme Primaire et "
                "Pression, elles arrivent en Premier et Passent partout, "
                "solides et liquides. S comme Secondaire et Shear, "
                "cisaillement en anglais, elles arrivent en Second et "
                "S'arrêtent, Stop, dans les liquides. Astuce deux, pour les "
                "discontinuités, presque par ordre alphabétique du haut "
                "vers le bas : Moho, puis Gutenberg, le grand choc où les S "
                "disparaissent, puis Lehmann, où le Liquide s'arrête et où "
                "la graine solide commence ; retenez les profondeurs, deux "
                "mille neuf cents et cinq mille cent cinquante kilomètres, "
                "et le centre à six mille trois cent soixante et onze "
                "kilomètres. Astuce trois, pour les roches témoins : "
                "continent égale granite, clair ; océan égale basalte, "
                "noir ; manteau égale péridotite, verte ; noyau égale "
                "fer-nickel, comme dans les sidérites."
            )
        ) as tracker:
            self.play(FadeIn(entete_astuces))
            self.play(FadeIn(astuces))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_astuces), FadeOut(astuces))

        # --- À retenir / clôture : L'ESSENTIEL DU CHAPITRE ---------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Indices directs (10-100 premiers km) + indices indirects (densité, "
                    "météorites, champ magnétique, chaleur, ondes sismiques).",
                    "Ondes P (longitudinales, solides+liquides, rapides) et ondes S "
                    "(transversales, solides seulement, plus lentes) ; vS=0 dans un liquide.",
                    "Trois discontinuités : Moho (5-70 km, croûte/manteau), "
                    "Gutenberg (2 900 km, manteau/noyau liquide), Lehmann (5 150 km, "
                    "noyau externe/interne solide).",
                    "Enveloppes chimiques : croûte, manteau (péridotites, 84 % du volume), "
                    "noyau (Fe-Ni).",
                    "Découpage mécanique distinct : lithosphère rigide (~100 km) vs "
                    "asthénosphère ductile — ne pas confondre avec le découpage chimique.",
                    "Densité, pression (P=ρgh) et température (T=T0+Gz) croissent avec la "
                    "profondeur ; la graine reste solide grâce à la pression malgré la "
                    "chaleur.",
                ],
                font_size=17,
                width=56,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)
        _garde_fou(essentiel)

        with self.voiceover(
            text=(
                "Voici l'essentiel de ce chapitre dense sur la structure "
                "interne du globe terrestre. Les indices directs ne "
                "renseignent que sur les dix à cent premiers kilomètres ; "
                "les indices indirects, densité moyenne, météorites, champ "
                "magnétique, chaleur interne et ondes sismiques, explorent "
                "tout le reste. Les ondes P, longitudinales, traversent "
                "solides et liquides et sont les plus rapides ; les ondes "
                "S, transversales, ne traversent que les solides et "
                "s'annulent dans un liquide. Trois discontinuités majeures "
                "structurent le globe : le Moho, entre cinq et soixante-dix "
                "kilomètres, sépare croûte et manteau ; Gutenberg, à deux "
                "mille neuf cents kilomètres, sépare le manteau du noyau "
                "liquide ; Lehmann, à cinq mille cent cinquante kilomètres, "
                "sépare le noyau externe liquide de la graine solide. Le "
                "découpage chimique donne croûte, manteau et noyau ; le "
                "découpage mécanique, bien distinct, donne une lithosphère "
                "rigide d'environ cent kilomètres et une asthénosphère "
                "ductile en dessous. Enfin, densité, pression et "
                "température croissent toutes avec la profondeur, et la "
                "graine reste solide malgré une chaleur extrême, grâce à la "
                "pression colossale qui y règne."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
