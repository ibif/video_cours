# PROGRAMME.md — Découpage du programme en chapitres/scènes

Ce fichier découpe chaque matière/série en chapitres, d'après le sommaire
officiel du PDF source correspondant (`<Serie>/<Matiere>.pdf`). Chaque
chapitre y reçoit un identifiant de code (`NomChapitre`) utilisé pour le
nommage des scènes (`Matiere_NomChapitre_NN.py`, voir CLAUDE.md) et pour le
tag de déclenchement du rendu HD (`chapitre__<Serie>__<Matiere>__<NomChapitre>`).

Statut par chapitre : `à faire` / `en cours` / `fait`.

---

## 1ereD — SVT (`1ereD/SVT.pdf`, 178 pages, 13 chapitres)

| # | Titre officiel | NomChapitre | Sous-sections | Statut |
|---|---|---|---|---|
| 1 | Les fonctions des gonades | `FonctionsGonades` | 1.1 Les gonades, organes reproducteurs · 1.2 Mise en évidence expérimentale des deux fonctions des gonades · 1.3 La fonction exocrine : la production des gamètes (gamétogenèse) · 1.4 La fonction endocrine : les hormones sexuelles · 1.5 Synthèse : deux fonctions liées tout au long de la vie | fait |
| 2 | La division méiotique | `DivisionMeiotique` | 2.1 Les chromosomes et la formule chromosomique d'une espèce · 2.2 Le déroulement de la méiose · 2.3 La méiose, source de la diversité génétique · 2.4 Méiose, fécondation et cycle de vie ; comparaison avec la mitose | fait |
| 3 | La gamétogénèse | `Gametogenese` | 3.1 Rappels : reproduction sexuée, gamètes et chromosomes · 3.2 Les gonades, sièges de la gamétogénèse · 3.3 La méiose, mécanisme central de la gamétogénèse · 3.4 La spermatogenèse : formation des spermatozoïdes · 3.5 L'ovogenèse : formation de l'ovule · 3.6 Comparaison des deux gamétogenèses et contrôle hormonal | fait |
| 4 | La transmission d'un caractère héréditaire : le monohybridisme | `Monohybridisme` | 4.1 Les notions de base : caractère héréditaire, gène et allèles · 4.2 Génotype, phénotype, homozygotie et hétérozygotie · 4.3 L'expérience de Mendel : le croisement monohybride · 4.4 Interprétation chromosomique : l'échiquier de croisement · 4.5 Le croisement-test (test-cross) · 4.6 Cas particuliers : codominance, allèles létaux, application à l'Homme | fait |
| 5 | La synthèse des protéines | `SyntheseProteines` | 5.1 Du gène à la protéine : une relation fondamentale · 5.2 Le code génétique : le dictionnaire de la cellule · 5.3 La transcription : recopier le message dans le noyau · 5.4 La traduction : fabriquer la protéine dans le cytoplasme · 5.5 Les mutations : quand l'information génétique change | fait |
| 6 | Les activités internes du globe terrestre | `ActivitesInternesGlobe` | 6.1 Le volcanisme : l'activité interne visible du globe · 6.2 Les séismes : les vibrations de l'écorce terrestre · 6.3 Ce que les séismes révèlent : la structure interne du globe · 6.4 La tectonique des plaques : l'explication globale des activités internes | fait |
| 7 | Les mouvements des plaques lithosphériques | `MouvementsPlaques` | 7.1 La lithosphère : une enveloppe rigide découpée en plaques · 7.2 Les preuves des mouvements : l'expansion océanique · 7.3 Les trois types de mouvements aux limites de plaques · 7.4 Les manifestations des mouvements des plaques · 7.5 Le moteur des mouvements des plaques | fait |
| 8 | Les échanges d'ions au niveau du sol | `EchangesIonsSol` | 8.1 Le sol, source d'éléments minéraux pour la plante · 8.2 Les besoins minéraux de la plante · 8.3 L'absorption des ions minéraux par la racine · 8.4 Applications agricoles : fumure et conservation de la fertilité | fait |
| 9 | L'évolution des sols tropicaux | `EvolutionSolsTropicaux` | 9.1 Le sol : une couche superficielle vivante · 9.2 Le profil d'un sol : la succession des horizons · 9.3 La formation du sol : l'altération de la roche mère · 9.4 Les facteurs d'évolution des sols tropicaux · 9.5 Les processus d'évolution des sols en milieu tropical · 9.6 Les principaux types de sols tropicaux · 9.7 La dégradation et la conservation des sols tropicaux | fait |
| 10 | Le réflexe inné | `ReflexeInne` | 10.1 Mise en évidence du réflexe · 10.2 Quelques exemples de réflexes innés · 10.3 Le circuit nerveux du réflexe : l'arc réflexe · 10.4 Étude détaillée de deux réflexes types · 10.5 Le cerveau et les réflexes ; intérêt des réflexes | en cours |
| 11 | La production de la matière | `ProductionMatiere` | 11.1 Les échanges gazeux entre le végétal vert et l'atmosphère · 11.2 Les conditions nécessaires à la production de matière · 11.3 Les organes et les structures cellulaires de la production de matière · 11.4 Le bilan de l'assimilation chlorophyllienne · 11.5 L'importance de la production de matière | en cours |
| 12 | La digestion des aliments | `DigestionAliments` | 12.1 Aliments, nutriments et digestion · 12.2 Le système digestif : le tube digestif et les glandes annexes · 12.3 Les transformations mécaniques des aliments · 12.4 La digestion chimique : les sucs digestifs et leurs enzymes · 12.5 Étude expérimentale de l'action des enzymes digestives · 12.6 Le devenir des nutriments : l'absorption intestinale · 12.7 Hygiène du système digestif | en cours |
| 13 | L'absorption des nutriments | `AbsorptionNutriments` | 13.1 Le siège de l'absorption des nutriments · 13.2 L'intestin grêle, une surface d'échange immense · 13.3 Les mécanismes de l'absorption · 13.4 Le devenir immédiat des nutriments absorbés | en cours |

Convention de nommage des scènes pour cette matière :
`SVT_<NomChapitre>_NN.py` (ex : `SVT_FonctionsGonades_01.py`).
Tag de rendu HD par chapitre : `chapitre__1ereD__SVT__<NomChapitre>`.

Le découpage précis en scènes (une scène par notion, jamais fourre-tout —
voir CLAUDE.md) est affiné au moment d'écrire chaque chapitre, à partir de
la lecture intégrale de ses pages dans le PDF.

---

## Autres matières/séries — à découper

Sommaire à extraire depuis le PDF source correspondant avant d'écrire la
moindre scène (voir CLAUDE.md, section "Pipeline de travail").

- `1ereC/Maths.pdf` (211 pages)
- `1ereC/Physique.pdf` (141 pages)
- `1ereC/Chimie.pdf` (153 pages)
- `1ereC/SVT.pdf` (134 pages)
- `1ereD/Maths.pdf` (196 pages)
- `1ereD/Physique-Chimie.pdf` (293 pages)
