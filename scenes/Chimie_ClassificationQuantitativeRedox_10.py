"""
scenes/Chimie_ClassificationQuantitativeRedox_10.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 10 (dernière scène du chapitre).

§ 10. Méthodes, pièges à éviter, tableau récapitulatif et essentiel.
Trois `method_box` : (1) prévoir le sens et l'ampleur d'une réaction
d'oxydoréduction en 4 étapes, (2) calculer la f.é.m. d'une pile, (3)
déterminer expérimentalement un potentiel standard inconnu. Tableau
récapitulatif des potentiels standard usuels (F₂/F⁻, MnO₄⁻/Mn²⁺, Cl₂/Cl⁻,
Cr₂O₇²⁻/Cr³⁺, Ag⁺/Ag, Fe³⁺/Fe²⁺, Cu²⁺/Cu, H₃O⁺/H₂, Fe²⁺/Fe, Zn²⁺/Zn,
Al³⁺/Al, Mg²⁺/Mg). Quatre `warning_box` (pièges classiques : ne jamais
multiplier E° par un coefficient stœchiométrique ; inverser oxydant et
réducteur dans le sens de la flèche ; oublier le signe de E° dans
E = E°(cathode) - E°(anode) ; confondre spontanéité et rapidité).
Conclusion par un `essentiel_box` récapitulatif du chapitre.
Source : 1ereC/Chimie.pdf, chapitre 11, pages 111-112.
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
    Line,
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


def _bullets(items, font_size=18, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


TABLEAU_E0 = [
    (r"F_2/F^{-}", "+2,87 V"),
    (r"MnO_4^{-}/Mn^{2+}", "+1,51 V"),
    (r"Cl_2/Cl^{-}", "+1,36 V"),
    (r"Cr_2O_7^{2-}/Cr^{3+}", "+1,33 V"),
    (r"Ag^{+}/Ag", "+0,80 V"),
    (r"Fe^{3+}/Fe^{2+}", "+0,77 V"),
    (r"Cu^{2+}/Cu", "+0,34 V"),
    (r"H_3O^{+}/H_2", "0,00 V"),
    (r"Fe^{2+}/Fe", "-0,44 V"),
    (r"Zn^{2+}/Zn", "-0,76 V"),
    (r"Al^{3+}/Al", "-1,66 V"),
    (r"Mg^{2+}/Mg", "-2,37 V"),
]


def _tableau_e0():
    """Tableau récapitulatif des E° usuels, deux colonnes (couple / E°),
    construit avec MathTex/Text/Line (aucune bibliothèque externe)."""
    colonne_couples = VGroup(*[MathTex(couple, font_size=20, color=WHITE) for couple, _ in TABLEAU_E0])
    colonne_couples.arrange(DOWN, buff=0.16, aligned_edge=LEFT)

    colonne_valeurs = VGroup(*[Text(valeur, font_size=19, color=YELLOW) for _, valeur in TABLEAU_E0])
    colonne_valeurs.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
    colonne_valeurs.next_to(colonne_couples, RIGHT, buff=1.0)

    # Aligner chaque valeur avec la ligne de son couple correspondant.
    for couple_mobj, valeur_mobj in zip(colonne_couples, colonne_valeurs):
        valeur_mobj.align_to(couple_mobj, UP)

    tableau = VGroup(colonne_couples, colonne_valeurs)
    separateur = Line(
        tableau.get_top() + UP * 0.15, tableau.get_bottom() + DOWN * 0.15, color=WHITE, stroke_width=1,
    )
    separateur.move_to([colonne_valeurs.get_left()[0] - 0.35, tableau.get_center()[1], 0])

    return VGroup(colonne_couples, colonne_valeurs, separateur)


class MethodesPiegesTableauEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("11.10 Méthodes, pièges et essentiel du chapitre")
        titre.scale(0.48)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Pour clore ce chapitre, rassemblons trois méthodes "
                "pratiques, quatre pièges classiques à éviter, un "
                "tableau récapitulatif des potentiels standard usuels, "
                "et l'essentiel à retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Méthode 1 : prévoir une réaction en 4 étapes ------------------------------
        methode1 = method_box(
            VGroup(
                Text("Prévoir le sens et l'ampleur d'une réaction", font_size=19, weight="BOLD"),
                Text("1. Identifier les deux couples Ox₁/Red₁ et Ox₂/Red₂ en présence.", font_size=16),
                Text("2. Relever leurs potentiels standard E°₁ et E°₂ dans une table.", font_size=16),
                Text("3. Calculer ΔE° = E°(couple du plus fort oxydant) - E°(autre couple).", font_size=16),
                Text("4. Conclure : sens spontané (Ox du + fort + Red de l'autre), puis "
                     "ampleur via ΔE° > 0,3 V (totale) ou < 0,3 V (équilibre).", font_size=16),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
            box_width=12.6,
        )
        methode1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Première méthode : prévoir le sens et l'ampleur d'une "
                "réaction d'oxydoréduction, en quatre étapes. Un : "
                "identifier les deux couples oxydant sur réducteur en "
                "présence. Deux : relever leurs potentiels standard dans "
                "une table. Trois : calculer delta E rond, potentiel "
                "standard du couple au plus fort oxydant moins celui de "
                "l'autre couple. Quatre : conclure sur le sens spontané, "
                "puis sur l'ampleur de la réaction grâce à la règle des "
                "zéro virgule trois volt."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : calculer la f.é.m. d'une pile ---------------------------------
        methode2 = method_box(
            VGroup(
                Text("Calculer la f.é.m. d'une pile", font_size=19, weight="BOLD"),
                Text("1. Identifier la cathode (pôle +, oxydant le plus fort, réduction).", font_size=16),
                Text("2. Identifier l'anode (pôle -, réducteur le plus fort, oxydation).", font_size=16),
                MathTex(r"3.\ E = E^{\circ}(\text{cathode}) - E^{\circ}(\text{anode})", font_size=22, color="#1A1A1A"),
                Text("4. Vérifier que E > 0 (sinon, cathode et anode ont été inversées).", font_size=16),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.6,
        )
        methode2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deuxième méthode : calculer la force électromotrice "
                "d'une pile. Un : identifier la cathode, le pôle positif, "
                "portée par l'oxydant le plus fort, siège de la "
                "réduction. Deux : identifier l'anode, le pôle négatif, "
                "portée par le réducteur le plus fort, siège de "
                "l'oxydation. Trois : appliquer E égale E rond de la "
                "cathode, moins E rond de l'anode. Quatre : vérifier que "
                "E est bien positif ; si ce n'est pas le cas, cathode et "
                "anode ont été inversées."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Méthode 3 : déterminer expérimentalement un E° inconnu --------------------
        methode3 = method_box(
            VGroup(
                Text("Déterminer expérimentalement un E° inconnu", font_size=19, weight="BOLD"),
                Text("1. Réaliser une pile [ENH | électrode standard du couple étudié].", font_size=16),
                Text("2. Mesurer la tension E à vide au voltmètre (intensité nulle).", font_size=16),
                Text("3. Repérer la polarité (ENH au pôle + ou au pôle -).", font_size=16),
                Text("4. En déduire E° : positif si l'ENH est au pôle -, négatif sinon.", font_size=16),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=12.6,
        )
        methode3.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Troisième méthode : déterminer expérimentalement le "
                "potentiel standard d'un couple inconnu. Un : réaliser "
                "la pile formée par l'électrode normale à hydrogène et "
                "l'électrode standard du couple étudié. Deux : mesurer "
                "la tension à vide au voltmètre. Trois : repérer quelle "
                "électrode constitue le pôle positif. Quatre : en "
                "déduire le potentiel standard, positif si l'électrode "
                "normale à hydrogène est au pôle négatif, négatif dans "
                "le cas contraire."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Tableau récapitulatif des E° usuels ----------------------------------------
        entete_tableau = Text("Tableau récapitulatif des potentiels standard usuels", font_size=20, color=YELLOW, weight="BOLD")
        entete_tableau.next_to(titre, DOWN, buff=0.3)

        tableau = _tableau_e0()
        tableau.scale(0.82)
        tableau.next_to(entete_tableau, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici, pour finir, un tableau récapitulatif des "
                "potentiels standard usuels, à connaître ou à savoir "
                "retrouver dans une table : du fluor sur ion fluorure, "
                "le plus élevé, jusqu'au magnésium, très négatif, en "
                "passant par l'ion permanganate, le dichlore, l'ion "
                "dichromate, l'argent, le fer trois plus sur fer deux "
                "plus, le cuivre, la référence ion oxonium sur "
                "dihydrogène, le fer deux plus sur fer, le zinc et "
                "l'aluminium."
            )
        ) as tracker:
            self.play(FadeIn(entete_tableau))
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tableau), FadeOut(tableau))

        # --- Pièges à éviter (4) ----------------------------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Ne JAMAIS multiplier E° par un coefficient "
                    "stœchiométrique : E° est une propriété intensive du "
                    "couple, indépendante des coefficients de l'équation "
                    "(contrairement à ΔG° ou à la quantité d'électrons "
                    "échangés).",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Premier piège : ne jamais multiplier un potentiel "
                "standard par un coefficient stœchiométrique. Même si "
                "l'équation-bilan comporte un facteur deux devant un "
                "couple, comme deux ions argent, le potentiel standard "
                "reste zéro virgule quatre-vingt volt : c'est une "
                "propriété intensive du couple, indépendante des "
                "coefficients de l'équation."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            Text(
                _wrap(
                    "Ne pas inverser oxydant et réducteur dans le sens de "
                    "la réaction : l'oxydant du couple le plus fort réagit "
                    "avec le RÉDUCTEUR de l'autre couple, jamais avec son "
                    "oxydant.",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième piège : ne pas inverser oxydant et réducteur "
                "dans le sens de la réaction. C'est l'oxydant du couple "
                "au potentiel standard le plus élevé qui réagit avec le "
                "réducteur de l'autre couple, jamais avec son oxydant : "
                "un oxydant ne réagit pas avec un autre oxydant."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            VGroup(
                Text(
                    "Ne pas oublier le signe de E° dans la formule :",
                    font_size=19,
                ),
                MathTex(r"E = E^{\circ}(\text{cathode}) - E^{\circ}(\text{anode})", font_size=24, color="#1A1A1A"),
                Text(
                    "un potentiel standard négatif se soustrait avec son signe "
                    "(soustraire un négatif = additionner sa valeur absolue).",
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=12.2,
        )
        piege3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième piège : ne pas oublier le signe de E rond "
                "dans la formule E égale E rond de la cathode, moins E "
                "rond de l'anode. Un potentiel standard négatif se "
                "soustrait avec son signe : soustraire un nombre négatif "
                "revient à additionner sa valeur absolue, comme nous "
                "l'avons vu pour la pile Daniell."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre spontanéité (ΔE° > 0, "
                    "thermodynamique) et rapidité (cinétique) : une "
                    "réaction thermodynamiquement favorable peut être "
                    "cinétiquement très lente (ex. l'aluminium passivé).",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege4.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quatrième et dernier piège, déjà rencontré : ne pas "
                "confondre spontanéité, une question thermodynamique "
                "liée au signe de delta E rond, et rapidité, une "
                "question purement cinétique. Une réaction "
                "thermodynamiquement très favorable peut rester "
                "extrêmement lente, comme l'oxydation de l'aluminium "
                "protégé par sa couche d'oxyde."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- Essentiel à retenir --------------------------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text(
                    "Le potentiel standard E°(Ox/Red) mesure, par rapport à "
                    "l'ENH (E°=0,00 V, convention), la force d'un couple "
                    "oxydant/réducteur dans les conditions standard.",
                    font_size=18,
                ),
                Text(
                    "Plus E° est élevé, plus l'oxydant est fort ; plus E° est "
                    "faible, plus le réducteur est fort.",
                    font_size=18,
                ),
                Text(
                    "Si E°₁ > E°₂ : réaction spontanée Ox₁+Red₂→Red₁+Ox₂ ; "
                    "ΔE°>0,3 V = quasi totale, sinon = équilibre.",
                    font_size=18,
                ),
                Text(
                    "Pour une pile : E = E°(cathode) - E°(anode). "
                    "Spontanéité (ΔE°) ≠ rapidité (cinétique).",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de ce chapitre. Le potentiel "
                "standard E rond de Ox sur Red mesure, par rapport à "
                "l'électrode normale à hydrogène fixée par convention à "
                "zéro, la force d'un couple oxydant sur réducteur dans "
                "les conditions standard. Plus E rond est élevé, plus "
                "l'oxydant est fort ; plus E rond est faible, plus le "
                "réducteur est fort. Si E rond un est supérieur à E rond "
                "deux, la réaction de l'oxydant un avec le réducteur deux "
                "est spontanée, quasi totale si l'écart dépasse zéro "
                "virgule trois volt, sinon limitée à un équilibre. Pour "
                "une pile, la force électromotrice vaut E rond de la "
                "cathode moins E rond de l'anode. Et n'oublions jamais "
                "que spontanéité et rapidité sont deux choses "
                "différentes."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
