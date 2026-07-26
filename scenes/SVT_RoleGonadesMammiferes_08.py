"""
scenes/SVT_RoleGonadesMammiferes_08.py — Chapitre 1 (1ereC, SVT), scène 08.

Méthode d'analyse d'une expérience de castration/greffe, exercice
d'application, piège classique primaire/secondaire, puis L'ESSENTIEL DU
CHAPITRE en clôture. Source : 1ereC/SVT.pdf, page 11 (§ VI).
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, exercise_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class MethodeEtEssentielDuChapitre(NotionScene):
    def construct(self):
        titre = scene_title("1.8 — Méthode : castration et greffe")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : la méthode en trois étapes --------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Pour analyser une expérience de castration/greffe : "
                    "1) identifier ce qui est RETIRÉ (la gonade) et l'effet "
                    "observé ; 2) identifier ce qui est RÉINTRODUIT (greffe "
                    "ou extrait) et l'effet observé ; 3) conclure sur le "
                    "double rôle — un extrait SEUL (sans reconnexion des "
                    "voies) ne prouve QUE le rôle endocrine.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici la méthode à suivre pour analyser une expérience de "
                "castration et de greffe. Étape une : identifier ce qui est "
                "retiré, c'est-à-dire la gonade, et l'effet observé, la "
                "régression des caractères sexuels et l'arrêt de la "
                "production de gamètes. Étape deux : identifier ce qui est "
                "réintroduit, une greffe ou un simple extrait, et l'effet "
                "observé. Étape trois : conclure sur le double rôle de la "
                "gonade, exocrine et endocrine, en précisant qu'un extrait "
                "seul, sans reconnexion des voies génitales, ne peut prouver "
                "que le rôle endocrine, puisqu'il n'agit que par voie "
                "sanguine."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Animation du raisonnement : exercice d'application -----------------
        exercice = exercise_box(
            Text(
                _wrap(
                    "Un bélier est castré : sa toison s'affine, son "
                    "comportement de reproducteur disparaît, et il ne "
                    "produit plus de spermatozoïdes. On lui greffe alors un "
                    "testicule, SANS reconnecter les canaux déférents : son "
                    "comportement et sa toison redeviennent normaux, mais "
                    "il reste stérile. Que peut-on conclure ?",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        exercice.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Appliquons la méthode à un exercice. Un bélier est castré : "
                "sa toison s'affine, son comportement de reproducteur "
                "disparaît, et il ne produit plus de spermatozoïdes. On lui "
                "greffe alors un testicule, mais sans reconnecter les "
                "canaux déférents. Résultat : son comportement et sa "
                "toison redeviennent normaux, mais il reste stérile. Que "
                "peut-on conclure de cette expérience ?"
            )
        ) as tracker:
            self.play(FadeIn(exercice))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exercice))

        # --- Exemple traité : le corrigé pas à pas --------------------------------
        corrige = corrige_box(
            Text(
                _wrap(
                    "Étape 1 : la castration fait régresser toison + "
                    "comportement ET arrête les spermatozoïdes -> la gonade "
                    "a bien un double effet. Étape 2 : la greffe SANS "
                    "reconnexion des voies restaure toison + comportement "
                    "(donc l'endocrine), mais PAS la fertilité (les voies "
                    "restent coupées). Étape 3 : conclusion -> les "
                    "hormones (toison, comportement) passent par le sang "
                    "(endocrine) ; les spermatozoïdes ont besoin des voies "
                    "génitales intactes (exocrine).",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=12.6,
        )
        corrige.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le corrigé, étape par étape. Étape une : la "
                "castration fait régresser à la fois la toison et le "
                "comportement, et arrête la production de spermatozoïdes : "
                "la gonade a donc bien un double effet. Étape deux : la "
                "greffe, sans reconnexion des voies génitales, restaure la "
                "toison et le comportement, donc le rôle endocrine, mais ne "
                "restaure pas la fertilité, puisque les voies restent "
                "coupées. Étape trois, la conclusion : les hormones, "
                "responsables de la toison et du comportement, passent par "
                "le sang, c'est le rôle endocrine ; les spermatozoïdes, eux, "
                "ont besoin de voies génitales intactes pour être "
                "transportés, c'est le rôle exocrine."
            )
        ) as tracker:
            self.play(FadeIn(corrige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige))

        # --- Piège à éviter : primaire vs secondaire (piège classique) ----------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège classique : ne confonds jamais caractères "
                    "sexuels PRIMAIRES (les gonades et voies génitales "
                    "elles-mêmes) et SECONDAIRES (les caractères qui "
                    "apparaissent à la puberté). Un exercice demandant de "
                    "« citer un caractère sexuel secondaire » ne doit "
                    "JAMAIS mentionner un testicule ou un ovaire.",
                    width=56,
                ),
                font_size=20,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un piège classique à éviter : ne confonds jamais les "
                "caractères sexuels primaires, les gonades et les voies "
                "génitales elles-mêmes, avec les caractères sexuels "
                "secondaires, ceux qui apparaissent à la puberté. Un "
                "exercice qui demande de citer un caractère sexuel "
                "secondaire ne doit jamais te faire répondre testicule ou "
                "ovaire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) -----------------------
        titre_fin = scene_title("L'essentiel du chapitre 1")
        titre_fin.scale(0.65)
        titre_fin.to_edge(UP)
        self.play(FadeOut(titre), FadeIn(titre_fin))
        titre = titre_fin

        essentiel = essentiel_box(
            _bullets(
                [
                    "Gonade = organe reproducteur primaire : testicule "
                    "(mâle) / ovaire (femelle). Double rôle : exocrine "
                    "(gamètes) + endocrine (hormones).",
                    "Appareil mâle : testicules, épididymes, canaux "
                    "déférents, vésicules séminales, prostate, glandes de "
                    "Cowper, urètre, pénis, scrotum.",
                    "Appareil femelle : ovaires, trompes de Fallope "
                    "(fécondation), utérus (nidation), vagin, vulve.",
                    "Castration -> régression + arrêt des gamètes ; greffe "
                    "-> restauration. Extrait seul = preuve du rôle "
                    "endocrine uniquement.",
                    "Testicule : tubes séminifères (cellules germinales + "
                    "Sertoli nourricières) entourés de tissu interstitiel "
                    "(cellules de Leydig, testostérone).",
                    "Ovaire : follicules à stades croissants (primordial "
                    "-> De Graaf) -> ovulation -> corps jaune (endocrine "
                    "temporaire, progestérone).",
                    "Testicule = production continue ; ovaire = "
                    "production cyclique, arrêt à la ménopause.",
                    "Caractères primaires = organes génitaux (dès la "
                    "naissance) ; secondaires = traits de puberté (jamais "
                    "un testicule ou un ovaire).",
                ],
                font_size=16,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        # Garde-fou : si le contenu dépasse la hauteur visible du cadre, on
        # réduit l'échelle globale de la boîte pour qu'elle tienne entièrement
        # à l'écran (technique de SVT_DivisionMeiotique_08.py).
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. La gonade est l'organe "
                "reproducteur primaire, le testicule chez le mâle, l'ovaire "
                "chez la femelle, avec un double rôle, exocrine pour les "
                "gamètes et endocrine pour les hormones. L'appareil mâle "
                "comprend les testicules, les épididymes, les canaux "
                "déférents, les vésicules séminales, la prostate, les "
                "glandes de Cowper, l'urètre, le pénis et le scrotum. "
                "L'appareil femelle comprend les ovaires, les trompes de "
                "Fallope, lieu de la fécondation, l'utérus, lieu de la "
                "nidation, le vagin et la vulve. La castration entraîne une "
                "régression des caractères sexuels et l'arrêt de la "
                "production de gamètes ; une greffe restaure ces effets, "
                "mais un extrait injecté seul ne prouve que le rôle "
                "endocrine. Le testicule est formé de tubes séminifères, "
                "avec les cellules germinales et les cellules de Sertoli "
                "nourricières, entourés d'un tissu interstitiel contenant "
                "les cellules de Leydig, qui sécrètent la testostérone. "
                "L'ovaire contient des follicules à des stades croissants, "
                "du follicule primordial au follicule de De Graaf, "
                "jusqu'à l'ovulation, suivie de la formation du corps "
                "jaune, une structure endocrine temporaire qui sécrète la "
                "progestérone. La production est continue chez l'homme, "
                "cyclique chez la femme, jusqu'à la ménopause. Enfin, les "
                "caractères sexuels primaires sont les organes génitaux "
                "eux-mêmes, présents dès la naissance, tandis que les "
                "caractères sexuels secondaires sont les traits qui "
                "apparaissent à la puberté, et qui ne doivent jamais être "
                "confondus avec les gonades elles-mêmes."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
