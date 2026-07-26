"""
scenes/Chimie_DosagesOxydoreduction_04.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 04.

§ La manganimétrie : protocole et exemple résolu. Protocole en 6 étapes
(rinçage burette, pipette 20 mL de Fe²⁺, acidification H₂SO₄, versement
jusqu'à décoloration instantanée, ralentissement puis goutte à goutte,
arrêt à la 1ère goutte persistante). Piège du choix de l'acide (jamais HCl
ni HNO₃). Relation à l'équivalence Cred = 5×Cox×Voxeq/Vred. Exemple résolu
1 : calcul complet, Cred = 7,5×10⁻² mol/L.
Source : 1ereC/Chimie.pdf, chapitre 12, pages 116-117.
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
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _numbered(items, font_size=20, color=WHITE, width=52):
    lines = VGroup(
        *[
            Text(f"{i+1}) {_wrap(it, width=width)}", font_size=font_size, color=color)
            for i, it in enumerate(items)
        ]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ManganimetrieProtocoleEtExemple(NotionScene):
    def construct(self):
        titre = scene_title("12.4 La manganimétrie : protocole et exemple résolu")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------------
        intro = Text(
            _wrap(
                "Comment mettre en œuvre concrètement le dosage d'une "
                "solution de fer II par le permanganate de potassium ? "
                "Suivons le protocole complet, étape par étape.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment mettre en œuvre concrètement le dosage d'une "
                "solution de fer deux par le permanganate de potassium ? "
                "Suivons le protocole complet, étape par étape, avant de "
                "traiter un exemple chiffré."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : protocole en 6 étapes ---------------------------------
        entete_proto = Text("Protocole en 6 étapes", font_size=22, color=YELLOW, weight="BOLD")
        entete_proto.next_to(titre, DOWN, buff=0.35)

        protocole = _numbered(
            [
                "Rincer la burette avec la solution de permanganate, "
                "puis la remplir et ajuster le zéro.",
                "Prélever 20 mL de la solution de Fe²⁺ à la pipette "
                "jaugée, les verser dans l'erlenmeyer.",
                "Acidifier avec de l'acide sulfurique H₂SO₄ en excès "
                "(milieu acide indispensable).",
                "Verser le permanganate jusqu'à ce que la décoloration "
                "devienne instantanée (le violet ne persiste plus).",
                "Ralentir le versement, puis passer goutte à goutte.",
                "S'arrêter à la 1ère goutte qui rend la couleur "
                "ROSE PÂLE PERSISTANTE : on note Veq.",
            ],
            font_size=19,
            width=52,
        )
        protocole.next_to(entete_proto, DOWN, buff=0.3)
        groupe_proto = VGroup(entete_proto, protocole)
        _fit(groupe_proto, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Le protocole comporte six étapes. Un : on rince la "
                "burette avec la solution de permanganate, puis on la "
                "remplit et on ajuste le zéro. Deux : on prélève vingt "
                "millilitres de la solution de fer deux plus à la "
                "pipette jaugée, que l'on verse dans l'erlenmeyer. Trois "
                ": on acidifie avec de l'acide sulfurique en excès, le "
                "milieu acide étant indispensable. Quatre : on verse le "
                "permanganate jusqu'à ce que la décoloration devienne "
                "instantanée, le violet ne persistant plus. Cinq : on "
                "ralentit le versement, puis on passe goutte à goutte. "
                "Six : on s'arrête à la première goutte qui rend la "
                "couleur rose pâle persistante, et l'on note le volume "
                "versé, Veq."
            )
        ) as tracker:
            self.play(FadeIn(entete_proto))
            self.play(FadeIn(protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_proto))

        # --- Piège : choix de l'acide ---------------------------------------------------
        piege_acide = warning_box(
            Text(
                _wrap(
                    "Piège du choix de l'acide : n'utiliser JAMAIS l'acide "
                    "chlorhydrique HCl (Cl⁻ est oxydable par MnO₄⁻, "
                    "réaction parasite) ni l'acide nitrique HNO₃ (oxydant "
                    "lui-même). Utiliser l'acide sulfurique H₂SO₄, "
                    "chimiquement inerte ici.",
                    width=48,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        piege_acide.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège classique sur le choix de l'acide "
                "acidifiant : il ne faut jamais utiliser l'acide "
                "chlorhydrique, car l'ion chlorure est lui-même oxydable "
                "par le permanganate, ce qui créerait une réaction "
                "parasite. Il ne faut pas non plus utiliser l'acide "
                "nitrique, qui est lui-même un oxydant. On utilise "
                "toujours l'acide sulfurique, chimiquement inerte dans "
                "cette réaction."
            )
        ) as tracker:
            self.play(FadeIn(piege_acide))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_acide))

        # --- Raisonnement : relation à l'équivalence -----------------------------------
        entete_rel = Text("Relation à l'équivalence", font_size=22, color=YELLOW, weight="BOLD")
        entete_rel.next_to(titre, DOWN, buff=0.4)

        explication = Text(
            _wrap(
                "À l'équivalence : n(Fe²⁺) = 5 × n(MnO₄⁻ versé), car il "
                "faut 5 Fe²⁺ pour 1 MnO₄⁻ dans l'équation-bilan.",
                width=50,
            ),
            font_size=20,
            color=WHITE,
        )
        relation = MathTex(
            r"C_{red}\,V_{red} = 5\,C_{ox}\,V_{ox\,eq} \quad\Longrightarrow\quad C_{red} = \dfrac{5\,C_{ox}\,V_{ox\,eq}}{V_{red}}",
            font_size=28, color=YELLOW,
        )
        bloc_rel = VGroup(explication, relation).arrange(DOWN, buff=0.4)
        bloc_rel.next_to(entete_rel, DOWN, buff=0.35)
        groupe_rel = VGroup(entete_rel, bloc_rel)
        _fit(groupe_rel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Établissons la relation à l'équivalence. D'après "
                "l'équation-bilan, il faut cinq fer deux plus pour un "
                "permanganate : à l'équivalence, la quantité de matière "
                "de fer deux plus est donc égale à cinq fois la quantité "
                "de matière de permanganate versé. En notant Cred et Vred "
                "la concentration et le volume du fer deux plus, Cox et "
                "Voxeq la concentration du permanganate et le volume "
                "versé à l'équivalence, on obtient : Cred fois Vred égale "
                "cinq fois Cox fois Voxeq, soit Cred égale cinq Cox Voxeq "
                "sur Vred."
            )
        ) as tracker:
            self.play(FadeIn(entete_rel))
            self.play(FadeIn(explication))
            self.play(Write(relation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_rel))

        # --- Exemple résolu 1 -----------------------------------------------------------
        entete_ex = Text("Exemple résolu 1", font_size=22, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.35)

        enonce_ex = Text(
            _wrap(
                "On dose 20,0 mL d'une solution de Fe²⁺ par une solution "
                "de permanganate de potassium à 2,0×10⁻² mol/L. "
                "L'équivalence est obtenue pour Voxeq = 15,0 mL. "
                "Calculer Cred.",
                width=50,
            ),
            font_size=19,
            color=WHITE,
        )

        calcul = example_box(
            VGroup(
                MathTex(r"C_{red} = \dfrac{5\times C_{ox}\times V_{ox\,eq}}{V_{red}}", font_size=24, color="#1A1A1A"),
                MathTex(r"C_{red} = \dfrac{5\times 2{,}0\times 10^{-2}\times 15{,}0}{20{,}0}", font_size=24, color="#1A1A1A"),
                MathTex(r"C_{red} = 7{,}5\times 10^{-2}\ \text{mol/L}", font_size=26, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )

        bloc_ex = VGroup(enonce_ex, calcul).arrange(DOWN, buff=0.35)
        bloc_ex.next_to(entete_ex, DOWN, buff=0.3)
        groupe_ex = VGroup(entete_ex, bloc_ex)
        _fit(groupe_ex, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Traitons un exemple résolu. On dose vingt millilitres "
                "d'une solution de fer deux plus par une solution de "
                "permanganate de potassium à deux virgule zéro fois dix "
                "puissance moins deux mol par litre. L'équivalence est "
                "obtenue pour un volume versé de quinze millilitres. "
                "Calculons Cred : on applique la relation, Cred égale "
                "cinq fois deux virgule zéro fois dix puissance moins "
                "deux, fois quinze, le tout divisé par vingt, ce qui "
                "donne sept virgule cinq fois dix puissance moins deux "
                "mol par litre."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(enonce_ex))
            self.play(Write(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_ex))

        # --- À retenir --------------------------------------------------------------------
        retenir = method_box(
            Text(
                _wrap(
                    "Manganimétrie du fer : Cred = 5×Cox×Voxeq / Vred. "
                    "Protocole : acidifier au H₂SO₄, verser jusqu'à "
                    "décoloration instantanée, puis goutte à goutte "
                    "jusqu'à teinte rose pâle persistante.",
                    width=46,
                ),
                font_size=19,
            ),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : pour la manganimétrie du fer, la "
                "relation Cred égale cinq Cox Voxeq sur Vred permet de "
                "calculer la concentration inconnue. Sur le plan "
                "expérimental, on acidifie toujours au H-2-S-O-4, on "
                "verse jusqu'à décoloration instantanée, puis goutte à "
                "goutte jusqu'à l'apparition d'une teinte rose pâle "
                "persistante, qui marque l'équivalence."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
