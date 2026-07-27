"""
scenes/Maths_VecteursEspace_11.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 11 (synthèse finale du chapitre).

§ Méthodes et astuces : démontrer un alignement, une coplanarité, qu'un
triplet est une base, calculer des coordonnées dans un repère naturel d'un
solide, construire la section d'un solide par un plan. Tableau
récapitulatif plan → espace. Quatre pièges à éviter (droites non sécantes
pas forcément parallèles ; w=xu+yv sans u,v non colinéaires ; distance
euclidienne hors repère orthonormé ; vecteurs colinéaires vs points
alignés). Essentiel à retenir final.
Source : 1ereC/Maths.pdf, pages 189-199.
"""

from manim import (
    DOWN,
    LEFT,
    UP,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, property_box, scene_title, warning_box


class SyntheseMethodesEtPieges(NotionScene):
    def construct(self):
        titre = scene_title("Méthodes, astuces et pièges à éviter — synthèse")
        titre.scale(0.48)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : tableau récapitulatif plan → espace ---------------------------
        lignes = VGroup(
            Text("Colinéarité de vecteurs : inchangée (même définition qu'en géométrie plane)", font_size=18),
            Text("Repère : (O;i,j) devient (O;i,j,k) — ajout de la cote z", font_size=18),
            Text("Coordonnées de AB : (xB−xA;yB−yA) devient (xB−xA;yB−yA;zB−zA)", font_size=18),
            Text("Décomposition sur une base : 2 vecteurs (i,j) deviennent 3 vecteurs (i,j,k)", font_size=18),
            Text("Coplanarité : notion NOUVELLE, propre à l'espace (tout est coplanaire dans le plan)", font_size=18),
            Text("Milieu : formule identique, avec simplement une composante z en plus", font_size=18),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        tableau = property_box(lignes)
        tableau.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, récapitulons ce qui change, et "
                "ce qui ne change pas, entre le plan et l'espace. La "
                "colinéarité de deux vecteurs reste identique. Le repère "
                "gagne un troisième vecteur, et donc une troisième "
                "coordonnée, la cote z. Les coordonnées d'un vecteur A-B "
                "gagnent elles aussi une composante z. La décomposition "
                "d'un vecteur se fait désormais sur trois vecteurs de base "
                "au lieu de deux. La coplanarité, en revanche, est une "
                "notion entièrement nouvelle, puisque dans le plan tout est "
                "automatiquement coplanaire. Et la formule du milieu reste "
                "la même, avec simplement une composante supplémentaire."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Raisonnement / à retenir : les 5 méthodes du chapitre ------------------
        methodes_txt = [
            r"\text{Démontrer } A,B,C \ \text{alignés} \ : \ \overrightarrow{AB}, \overrightarrow{AC} \ \text{colinéaires (ou coordonnées proportionnelles)}",
            r"\text{Démontrer } A,B,C,D \ \text{coplanaires} \ : \ \text{écrire } \overrightarrow{AD}=x\overrightarrow{AB}+y\overrightarrow{AC}, \ \text{résoudre sur 2 coord., vérifier la 3e}",
            r"\text{Démontrer qu'un triplet } (u,v,w) \ \text{est une base} \ : \ \text{vérifier qu'ils ne sont PAS coplanaires}",
            r"\text{Coordonnées dans un repère naturel} \ : \ \text{cube} \to (A;\overrightarrow{AB},\overrightarrow{AD},\overrightarrow{AE}), \ \text{tétraèdre} \to (A;\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD})",
            r"\text{Construire une section} \ : \ \text{joindre 2 points d'une même face, prolonger par parallélisme, refermer le polygone}",
        ]
        for i, txt in enumerate(methodes_txt, start=1):
            meth = method_box(MathTex(txt, font_size=18))
            meth.next_to(titre, DOWN, buff=0.4)
            with self.voiceover(text=f"Méthode {i}. " + self._methode_narration(i)) as tracker:
                self.play(FadeIn(meth))
                self.wait(tracker.get_remaining_duration())
            self.play(FadeOut(meth))

        # --- Pièges à éviter : les 4 pièges du chapitre ------------------------------
        piege1 = warning_box(
            Text(
                "Piège 1 : deux droites non sécantes ne sont PAS forcément parallèles —\n"
                "elles peuvent être GAUCHES (non coplanaires), voir scène 7.",
                font_size=20,
            ),
        )
        piege1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Premier piège, le plus fréquent : deux droites qui ne se "
                "coupent pas ne sont pas forcément parallèles dans "
                "l'espace, elles peuvent être gauches."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            VGroup(
                Text("Piège 2 : n'écrivez JAMAIS w = xu+yv sans avoir vérifié", font_size=20),
                MathTex(r"\text{que } u,v \ \text{sont NON colinéaires — sinon la décomposition n'est pas valide.}", font_size=19),
            ).arrange(DOWN, buff=0.18),
        )
        piege2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Deuxième piège : n'écrivez jamais qu'un vecteur w s'écrit x "
                "fois u plus y fois v sans avoir d'abord vérifié que u et v "
                "ne sont pas colinéaires — sinon cette décomposition n'a "
                "aucun sens, ou n'est plus unique."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            VGroup(
                Text(
                    "Piège 3 : la formule de distance euclidienne √((xB−xA)²+…) exige un\n"
                    "repère ORTHONORMÉ — pas valable dans le repère naturel (A;AB,AD,AE)\n"
                    "d'un cube (utiliser Pythagore dans les faces, pas les coordonnées brutes).",
                    font_size=18,
                ),
            ),
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège : la formule de distance avec la racine "
                "carrée de la somme des carrés des différences de "
                "coordonnées exige un repère orthonormé. Dans le repère "
                "naturel d'un cube, A, A-B, A-D, A-E, ce repère n'est pas "
                "orthonormé au sens strict des distances : il faut "
                "utiliser le théorème de Pythagore directement dans les "
                "faces, jamais appliquer cette formule aux coordonnées "
                "brutes."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            VGroup(
                Text("Piège 4 : ne confondez pas « vecteurs colinéaires » et « points alignés ».", font_size=20),
                MathTex(
                    r"u \parallel v \ (\text{droites parallèles}) \quad \neq \quad A,B,C \ \text{alignés} \ (\text{nécessite le POINT COMMUN } A \ \text{entre} \ \overrightarrow{AB}, \overrightarrow{AC})",
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.18),
        )
        piege4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatrième et dernier piège : ne confondez pas vecteurs "
                "colinéaires, qui donnent des droites parallèles, et points "
                "alignés, qui exigent que les deux vecteurs partagent un "
                "point commun, comme A-B et A-C, tous deux issus de A."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- L'essentiel à retenir ----------------------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("Vecteurs de l'espace — l'essentiel", font_size=22, weight="BOLD"),
                MathTex(r"\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC} \ \text{(Chasles, inchangée)} \quad ; \quad (i,j,k) \ \text{base} \iff \text{non coplanaires}", font_size=17),
                MathTex(r"w \ \text{coplanaire à} \ u,v \ (\text{non colin.}) \iff w=xu+yv \iff \exists (\alpha,\beta,\gamma)\neq 0, \ \alpha u+\beta v+\gamma w=\vec 0", font_size=15),
                MathTex(r"\overrightarrow{IA}+\overrightarrow{IB}=\vec 0 \ (\text{milieu}) \quad ; \quad \overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC}+\overrightarrow{GD}=\vec 0 \ (\text{centre de gravité, } \overrightarrow{AG}=\tfrac34\overrightarrow{AA'})", font_size=15),
            ).arrange(DOWN, buff=0.2),
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour conclure définitivement ce chapitre, l'essentiel à "
                "retenir. La relation de Chasles reste inchangée. Une base "
                "de l'espace est un triplet non coplanaire. Un vecteur w "
                "est coplanaire à deux vecteurs non colinéaires u et v si, "
                "et seulement si, il s'écrit comme leur combinaison "
                "linéaire, ou, de façon équivalente, s'il existe trois "
                "coefficients non tous nuls annulant leur somme pondérée. "
                "Enfin, le milieu et le centre de gravité se caractérisent "
                "tous deux par une somme de vecteurs nulle, le second étant "
                "la généralisation directe du premier à quatre points, avec "
                "G situé aux trois quarts de chaque médiane. Ces outils "
                "vectoriels, valables sans coordonnées, sont la base de "
                "toute la géométrie de l'espace au programme."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))

    @staticmethod
    def _methode_narration(i: int) -> str:
        textes = {
            1: (
                "Pour démontrer que trois points sont alignés, on montre "
                "que deux vecteurs partageant un point commun, comme A-B et "
                "A-C, sont colinéaires — ou que leurs coordonnées sont "
                "proportionnelles."
            ),
            2: (
                "Pour démontrer que quatre points sont coplanaires, on "
                "écrit un vecteur comme combinaison linéaire des deux "
                "autres : on résout le système sur deux coordonnées, puis "
                "on vérifie que la troisième coïncide bien."
            ),
            3: (
                "Pour démontrer qu'un triplet de vecteurs forme une base, "
                "il suffit de vérifier qu'ils ne sont pas coplanaires — "
                "géométriquement, ou en montrant qu'aucune combinaison "
                "linéaire non triviale ne les annule."
            ),
            4: (
                "Pour calculer des coordonnées dans le repère naturel d'un "
                "solide, on choisit un sommet comme origine et les trois "
                "arêtes qui en partent comme base : le point A et les "
                "vecteurs A-B, A-D, A-E pour un cube, A et A-B, A-C, A-D "
                "pour un tétraèdre."
            ),
            5: (
                "Pour construire la section d'un solide par un plan, on "
                "relie deux points du plan de coupe situés dans une même "
                "face, on prolonge grâce au parallélisme des faces "
                "opposées, et on recommence jusqu'à refermer le polygone "
                "obtenu."
            ),
        }
        return textes[i]
