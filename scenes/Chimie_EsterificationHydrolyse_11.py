"""
scenes/Chimie_EsterificationHydrolyse_11.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 11 (dernière).

§ Usages des esters (arômes/parfums, solvants, polyesters/fibres textiles,
savons/détergents). method_box × 4 (écrire une estérification nommée,
exploiter un dosage pour le rendement, reconnaître si un système est à
l'équilibre, identifier acide/alcool parents d'un ester). warning_box × 3
pièges (lente ≠ limitée ; chauffer n'augmente pas le rendement ;
estérification/hydrolyse acide = flèche réversible mais saponification =
flèche simple). essentiel_box récapitulatif final.
Source : 1ereC/Chimie.pdf, chapitre 8, pages 83-84.
"""

import textwrap

from manim import (
    DOWN,
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
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class UsagesMethodesPiegesEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("11. Usages, méthodes, pièges et l'essentiel")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : usages des esters ------------------------------------------
        entete = Text("Les usages des esters", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        usages = Text(
            _wrap(
                "Arômes et parfums (agroalimentaire, cosmétique) · "
                "Solvants (vernis, peintures, colles) · Polyesters, "
                "fibres textiles (ex : PET) · Savons et détergents "
                "(via la saponification).",
                width=50,
            ),
            font_size=23,
            color=WHITE,
        )
        usages.next_to(entete, DOWN, buff=0.4)
        groupe = VGroup(entete, usages)
        _fit(groupe, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Terminons ce chapitre par un panorama des usages des "
                "esters, et une synthèse des méthodes et pièges à "
                "connaître. Les esters se retrouvent d'abord dans les "
                "arômes et les parfums, en agroalimentaire comme en "
                "cosmétique. On les utilise aussi comme solvants, pour "
                "les vernis, les peintures ou les colles. Certains "
                "esters, comme le PET, forment des polyesters utilisés "
                "dans les fibres textiles. Et enfin, via la "
                "saponification, ils sont à l'origine des savons et des "
                "détergents."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete))
            self.play(FadeIn(usages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Raisonnement : 4 méthodes -----------------------------------------------
        m1 = method_box(
            Text(
                _wrap(
                    "1) Écrire une estérification nommée : identifier "
                    "acide (suffixe -oate) et alcool (groupe -yle) à "
                    "partir du nom de l'ester, écrire les formules "
                    "semi-développées, puis l'équation avec ⇌.",
                    width=46,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )
        m1.next_to(titre, DOWN, buff=0.4)
        _fit(m1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Première méthode : pour écrire une estérification "
                "nommée, on identifie l'acide, à partir du suffixe "
                "-oate, et l'alcool, à partir du groupe en -yle, on "
                "écrit les formules semi-développées de chacun, puis "
                "l'équation complète avec sa double flèche."
            )
        ) as tracker:
            self.play(FadeIn(m1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m1))

        m2 = method_box(
            Text(
                _wrap(
                    "2) Exploiter un dosage pour le rendement : doser la "
                    "quantité d'acide restant à l'équilibre, en déduire "
                    "xe = n - n(acide restant), puis τ = xe / xmax.",
                    width=46,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )
        m2.next_to(titre, DOWN, buff=0.4)
        _fit(m2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : pour exploiter un dosage et calculer "
                "un rendement, on dose la quantité d'acide restant à "
                "l'équilibre, on en déduit l'avancement xe égal à n moins "
                "cette quantité restante, puis on calcule le taux "
                "d'avancement final, xe sur x-max."
            )
        ) as tracker:
            self.play(FadeIn(m2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m2))

        m3 = method_box(
            Text(
                _wrap(
                    "3) Reconnaître un système à l'équilibre : les "
                    "quantités de matière n'évoluent plus au cours du "
                    "temps (courbes horizontales), mais la réaction se "
                    "poursuit microscopiquement (équilibre DYNAMIQUE, "
                    "vitesse directe = vitesse inverse).",
                    width=46,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )
        m3.next_to(titre, DOWN, buff=0.4)
        _fit(m3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième méthode : pour reconnaître qu'un système est "
                "à l'équilibre, on observe que les quantités de matière "
                "n'évoluent plus au cours du temps, courbes horizontales "
                "sur un graphique. Mais attention, la réaction se "
                "poursuit toujours microscopiquement : c'est un "
                "équilibre dynamique, où la vitesse directe égale la "
                "vitesse inverse."
            )
        ) as tracker:
            self.play(FadeIn(m3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m3))

        m4 = method_box(
            Text(
                _wrap(
                    "4) Identifier acide/alcool parents d'un ester : "
                    "repérer le groupe -COO-, couper de part et d'autre ; "
                    "le côté C=O redevient l'acide R-COOH, le côté O-R' "
                    "redevient l'alcool R'-OH.",
                    width=46,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )
        m4.next_to(titre, DOWN, buff=0.4)
        _fit(m4, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Quatrième méthode : pour identifier l'acide et l'alcool "
                "parents d'un ester donné, on repère le groupe -C-O-O-, "
                "puis on coupe de part et d'autre. Le côté qui contient "
                "le carbone du carbonyle redevient l'acide R-C-O-O-H, et "
                "le côté qui contient le O-R' redevient l'alcool R'-O-H."
            )
        ) as tracker:
            self.play(FadeIn(m4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(m4))

        # --- Exemple traité : 3 pièges à éviter ---------------------------------------
        p1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 : LENTE ≠ LIMITÉE. Ce sont deux "
                    "caractéristiques indépendantes : la première est "
                    "cinétique (la vitesse), la seconde thermodynamique "
                    "(l'équilibre). On peut accélérer sans changer la "
                    "limite.",
                    width=46,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )
        p1.next_to(titre, DOWN, buff=0.4)
        _fit(p1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Passons maintenant à trois pièges classiques à éviter. "
                "Premier piège : lente n'est pas synonyme de limitée. Ce "
                "sont deux caractéristiques bien indépendantes : la "
                "première est d'ordre cinétique, elle concerne la "
                "vitesse ; la seconde est d'ordre thermodynamique, elle "
                "concerne l'équilibre. On peut accélérer une réaction "
                "sans jamais changer sa limite."
            )
        ) as tracker:
            self.play(FadeIn(p1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(p1))

        p2 = warning_box(
            Text(
                _wrap(
                    "Piège 2 : chauffer N'AUGMENTE PAS le rendement "
                    "(réaction athermique → facteur cinétique uniquement). "
                    "Seul un déplacement d'équilibre (excès de réactif, "
                    "retrait d'un produit) augmente réellement le "
                    "rendement.",
                    width=46,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )
        p2.next_to(titre, DOWN, buff=0.4)
        _fit(p2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deuxième piège : chauffer n'augmente jamais le "
                "rendement, puisque la réaction est athermique — le "
                "chauffage n'est qu'un facteur cinétique. Seul un "
                "véritable déplacement d'équilibre, par excès de réactif "
                "ou par retrait d'un produit formé, augmente réellement "
                "le rendement."
            )
        ) as tracker:
            self.play(FadeIn(p2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(p2))

        p3 = warning_box(
            Text(
                _wrap(
                    "Piège 3 : estérification et hydrolyse ACIDE = flèche "
                    "réversible ⇌ (équilibre). Mais SAPONIFICATION "
                    "(hydrolyse BASIQUE) = flèche simple → (réaction "
                    "TOTALE) : ne jamais confondre ces deux flèches.",
                    width=46,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )
        p3.next_to(titre, DOWN, buff=0.4)
        _fit(p3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième piège, et non des moindres : l'estérification "
                "et l'hydrolyse acide s'écrivent avec une flèche "
                "réversible, car c'est un équilibre. Mais la "
                "saponification, l'hydrolyse basique, s'écrit avec une "
                "flèche simple, car c'est une réaction totale. Il ne "
                "faut jamais confondre ces deux flèches."
            )
        ) as tracker:
            self.play(FadeIn(p3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(p3))

        # --- À retenir : essentiel_box récapitulatif final -----------------------------
        essentiel = essentiel_box(
            VGroup(
                Text(
                    _wrap(
                        "Acide + alcool ⇌ ester + eau (estérification / "
                        "hydrolyse) : réaction LENTE, ATHERMIQUE, LIMITÉE "
                        "(≈ 2/3 pour un alcool primaire).",
                        width=46,
                    ),
                    font_size=20,
                ),
                Text(
                    _wrap(
                        "H⁺ catalyse (vitesse), sans déplacer l'équilibre. "
                        "Excès d'un réactif ou retrait d'un produit "
                        "augmentent le rendement.",
                        width=46,
                    ),
                    font_size=20,
                ),
                Text(
                    _wrap(
                        "Saponification (hydrolyse basique) : réaction "
                        "TOTALE → savons, ions carboxylate amphiphiles.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=12.2,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)
        _fit(essentiel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, retenons l'essentiel. "
                "L'estérification et l'hydrolyse forment un même "
                "équilibre, acide plus alcool contre ester plus eau : "
                "une réaction lente, athermique, et limitée, avec une "
                "limite d'environ deux tiers pour un alcool primaire. "
                "Les ions H plus catalysent cette réaction, en accélérant "
                "sa vitesse, sans jamais déplacer l'équilibre. Pour "
                "augmenter le rendement, il faut soit mettre un réactif "
                "en excès, soit retirer un produit formé. Enfin, la "
                "saponification, hydrolyse basique de l'ester, est une "
                "réaction totale, à l'origine de la fabrication des "
                "savons, grâce aux ions carboxylate amphiphiles."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
