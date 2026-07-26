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
| 10 | Le réflexe inné | `ReflexeInne` | 10.1 Mise en évidence du réflexe · 10.2 Quelques exemples de réflexes innés · 10.3 Le circuit nerveux du réflexe : l'arc réflexe · 10.4 Étude détaillée de deux réflexes types · 10.5 Le cerveau et les réflexes ; intérêt des réflexes | fait |
| 11 | La production de la matière | `ProductionMatiere` | 11.1 Les échanges gazeux entre le végétal vert et l'atmosphère · 11.2 Les conditions nécessaires à la production de matière · 11.3 Les organes et les structures cellulaires de la production de matière · 11.4 Le bilan de l'assimilation chlorophyllienne · 11.5 L'importance de la production de matière | fait |
| 12 | La digestion des aliments | `DigestionAliments` | 12.1 Aliments, nutriments et digestion · 12.2 Le système digestif : le tube digestif et les glandes annexes · 12.3 Les transformations mécaniques des aliments · 12.4 La digestion chimique : les sucs digestifs et leurs enzymes · 12.5 Étude expérimentale de l'action des enzymes digestives · 12.6 Le devenir des nutriments : l'absorption intestinale · 12.7 Hygiène du système digestif | fait |
| 13 | L'absorption des nutriments | `AbsorptionNutriments` | 13.1 Le siège de l'absorption des nutriments · 13.2 L'intestin grêle, une surface d'échange immense · 13.3 Les mécanismes de l'absorption · 13.4 Le devenir immédiat des nutriments absorbés | fait |

Convention de nommage des scènes pour cette matière :
`SVT_<NomChapitre>_NN.py` (ex : `SVT_FonctionsGonades_01.py`).
Tag de rendu HD par chapitre : `chapitre__1ereD__SVT__<NomChapitre>`.

Le découpage précis en scènes (une scène par notion, jamais fourre-tout —
voir CLAUDE.md) est affiné au moment d'écrire chaque chapitre, à partir de
la lecture intégrale de ses pages dans le PDF.

---

## 1ereC — SVT (`1ereC/SVT.pdf`, 134 pages, 11 chapitres)

⚠️ **Piège de nommage à connaître** : `1ereC/SVT.pdf` et `1ereD/SVT.pdf`
partagent le même nom de `<Matiere>` (`SVT`). Or le pipeline
(`.github/scripts/detect_scenes.py`) résout les scènes d'un chapitre par le
motif `scenes/<Matiere>_<NomChapitre>_*.py`, **sans jamais tenir compte de
la `<Serie>`**. Si un chapitre de 1ereC portait le même `NomChapitre`
qu'un chapitre de 1ereD (ex : réutiliser `DivisionMeiotique` ou
`EchangesIonsSol` tels quels), les deux tags
`chapitre__1ereC__SVT__X` et `chapitre__1ereD__SVT__X` cibleraient
**les mêmes fichiers de scènes** — collision silencieuse. C'est pourquoi
tous les `NomChapitre` ci-dessous ont été choisis **explicitement
distincts** de ceux déjà utilisés en 1ereD/SVT (voir tableau plus haut),
même quand le thème se recoupe (méiose, gamétogénèse, synthèse des
protéines, échanges d'ions du sol, mouvements des plaques...). Toute
future écriture de chapitre SVT (1ereC ou 1ereD) doit vérifier l'ensemble
des deux tableaux de ce fichier avant de choisir un nouveau `NomChapitre`.

| # | Titre officiel | NomChapitre | Sous-sections | Statut |
|---|---|---|---|---|
| 1 | Le rôle et la structure des gonades des mammifères | `RoleGonadesMammiferes` | I. Introduction : le contexte de la reproduction · II. Les appareils reproducteurs · III. Le rôle des gonades · IV. Structure et ultrastructure des gonades · V. Tableau de synthèse comparatif · VI. Méthodes et astuces | fait |
| 2 | La division méiotique | `MeioseChromosomes` | I. Définition et intérêt de la méiose · II. Rappels sur les chromosomes · III. Le déroulement de la méiose (deux divisions successives) · IV. Le brassage génétique au cours de la méiose · V. Comparaison entre la méiose et la mitose · VI. Conséquences de la méiose · VII. Les anomalies de la méiose : l'exemple de la trisomie 21 | fait |
| 3 | La gamétogénèse chez les mammifères | `GametogeneseMammiferes` | I. Définition et cadre général de la gamétogénèse · II. La spermatogenèse : formation des spermatozoïdes · III. L'ovogenèse : formation des ovules · IV. Comparaison des deux processus (tableau de synthèse) · V. La structure des gamètes · VI. Les notions de fécondité | fait |
| 4 | La fécondation chez les mammifères | `FecondationMammiferes` | 1. Définition et lieu de la fécondation · 2. Le trajet des gamètes (spermatozoïdes, ovule) · 3. Les étapes de la fécondation (capacitation, réaction acrosomique, franchissement des enveloppes, blocage de la polyspermie, amphimixie) · 4. Les conséquences de la fécondation : diploïdie et détermination du sexe · 5. Les premières étapes du développement : segmentation et nidation · 6. Les jumeaux (vrais/faux) · 7. La maîtrise de la fécondation : contraception, IVG, FIVETE | fait |
| 5 | La synthèse des protéines | `ExpressionGenetique` | I. Rappels sur l'ADN, support de l'information génétique · II. Gène et protéine : le dogme central de la biologie moléculaire · III. La transcription : de l'ADN à l'ARN messager · IV. Le code génétique · V. La traduction : de l'ARNm à la protéine · VI. De la séquence nucléotidique à la séquence en acides aminés · VII. Les mutations et leurs conséquences : l'exemple de la drépanocytose | fait |
| 6 | La transmission d'un caractère héréditaire | `HerediteMendelienne` | I. Les notions de base de la génétique · II. Dominance, récessivité, homozygotie et hétérozygotie · III. Le monohybridisme : les croisements de Mendel sur le pois · IV. L'échiquier de croisement et les proportions théoriques · V. Le test-cross (croisement test) · VI. Exemples de transmission chez l'Homme et d'autres espèces · VII. Transmission autosomique et transmission liée au sexe · VIII. Les arbres généalogiques · IX. Applications : conseil génétique et sélection agricole | fait |
| 7 | La structure interne du globe terrestre | `StructureInterneGlobe` | I. Comment explorer l'intérieur de la Terre ? · II. Les ondes sismiques : nature, vitesses, réflexion et réfraction · III. Les discontinuités majeures : Moho, Gutenberg et Lehmann · IV. Les enveloppes du globe : croûte, manteau, noyau · V. Lithosphère et asthénosphère : un découpage mécanique · VI. Densité, pression et température internes | fait |
| 8 | Les mouvements des plaques lithosphériques | `TectoniquePlaques` | I. Le découpage de la lithosphère en plaques · II. Les arguments de la dérive des continents (Wegener, 1912) · III. Les arguments de l'expansion océanique · IV. Les trois types de frontières de plaques · V. Les moteurs des mouvements des plaques · VI. Conséquences : la répartition des séismes et des volcans | fait |
| 9 | Les échanges d'ions au niveau du sol | `EchangesCationiquesSol` | I. Rappels sur les ions et le sol · II. Les échanges cationiques : adsorption et désorption des ions · III. La capacité d'échange cationique (CEC) et la saturation du complexe · IV. Le pH du sol et la disponibilité des éléments nutritifs · V. Le lessivage et les pertes d'éléments fertilisants · VI. Les engrais, les amendements et le chaulage · VII. Application : les sols agricoles en Côte d'Ivoire | fait |
| 10 | La photosynthèse | `Photosynthese` | 1. Définition et équation bilan de la photosynthèse · 2. Le site de la photosynthèse : le chloroplaste et ses pigments · 3. La phase photochimique (phase claire) · 4. La phase biochimique (phase sombre) : le cycle de Calvin · 5. Mise en évidence expérimentale de la photosynthèse (dégagement d'O₂, test à l'eau iodée, témoins) · 6. Les facteurs influençant la photosynthèse (lumière, CO₂, température) · 7. Rôle de la photosynthèse dans la production de matière et l'équilibre du monde vivant | fait |
| 11 | L'écosystème naturel et l'écosystème agro-industriel | `EcosystemeAgroIndustriel` | 1. Définitions fondamentales : écosystème, biotope, biocénose, station · 2. Quelques écosystèmes naturels : la forêt, la savane, l'étang · 3. Les relations trophiques : chaînes et réseaux alimentaires · 4. Les flux de matière et d'énergie dans un écosystème · 5. Les cycles biogéochimiques : carbone et azote · 6. L'équilibre dynamique des écosystèmes · 7. L'écosystème agro-industriel (l'agrosystème) | fait |

Convention de nommage des scènes pour cette matière :
`SVT_<NomChapitre>_NN.py` (ex : `SVT_RoleGonadesMammiferes_01.py`).
Tag de rendu HD par chapitre : `chapitre__1ereC__SVT__<NomChapitre>`.

Le découpage précis en scènes (une scène par notion, jamais fourre-tout —
voir CLAUDE.md) est affiné au moment d'écrire chaque chapitre, à partir de
la lecture intégrale de ses pages dans le PDF.

Page 2 du PDF (`couleur.pdf` intégré) vérifiée : le code couleur des 9
catégories de contenu est identique à celui déjà mesuré et intégré dans
`constants.py`/`shapes/boxes.py` — pas de duplication de `constants.py`
nécessaire pour cette série.

---

## Autres matières/séries — à découper

Sommaire à extraire depuis le PDF source correspondant avant d'écrire la
moindre scène (voir CLAUDE.md, section "Pipeline de travail").

- `1ereC/Maths.pdf` (211 pages)
- `1ereC/Physique.pdf` (141 pages)
- `1ereC/Chimie.pdf` (153 pages)
- `1ereD/Maths.pdf` (196 pages)
- `1ereD/Physique-Chimie.pdf` (293 pages)
