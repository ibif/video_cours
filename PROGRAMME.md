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

## 1ereC — Chimie (`1ereC/Chimie.pdf`, 153 pages, 15 chapitres)

Page 2 du PDF vérifiée : code couleur des 9 catégories de contenu identique
à celui déjà intégré dans `constants.py`/`shapes/boxes.py` (mêmes 8
catégories + « L'ESSENTIEL À RETENIR »). Pas de collision de nom de
matière à craindre : `1ereD` n'a pas de `Chimie.pdf` séparé (il a
`Physique-Chimie.pdf`, préfixe de scène différent `Physique-Chimie_...`).

| # | Titre officiel | NomChapitre | Sous-sections | Statut |
|---|---|---|---|---|
| 1 | Généralités sur les composés organiques | `GeneralitesComposesOrganiques` | 1. La chimie organique et les composés organiques · 2. Analyse élémentaire qualitative · 3. Analyse élémentaire quantitative · 4. Les différentes écritures d'une molécule organique · 5. Les chaînes carbonées · 6. L'isomérie · 7. Les principales fonctions organiques (aperçu) · 8. Bases de la nomenclature | fait |
| 2 | Hydrocarbures saturés — les alcanes | `Alcanes` | 1. Généralités : liaison covalente, valence et formule générale des alcanes · 2. Structure des alcanes · 3. Nomenclature des alcanes (règles UICPA) · 4. Les cyclanes (cycloalcanes) · 5. Isomérie de chaîne · 6. Propriétés physiques des alcanes · 7. Propriétés chimiques des alcanes : combustion et substitution · 8. Pouvoir calorifique et usages des alcanes | fait |
| 3 | Hydrocarbures insaturés — les alcènes et les alcynes | `AlcenesAlcynes` | 1. Structure et nomenclature des alcènes (molécule d'éthylène, formule générale, nomenclature, isomérie de position et stéréoisomérie Z/E) · 2. Structure et nomenclature des alcynes (acétylène, formule générale, nomenclature) · 3. Propriétés chimiques des alcènes/alcynes (combustion, additions, test à l'eau de brome) · 4. Réactions de polymérisation d'addition (monomère/polymère/motif/degré, polyéthylène/PVC/polystyrène, importance industrielle) | fait |
| 4 | Le benzène | `Benzene` | 1. Introduction et formule brute du benzène · 2. Structure de la molécule de benzène · 3. Propriétés physiques du benzène · 4. Propriétés chimiques : réactions de substitution électrophile · 5. Comparaison du benzène avec les alcènes · 6. Usages et toxicité du benzène | fait |
| 5 | Pétrole et gaz naturels | `PetroleGazNaturels` | 1. Origine du pétrole et des gaz naturels · 2. Composition du pétrole brut et des gaz naturels · 3. Le raffinage : distillation fractionnée et principales fractions · 4. Le craquage et le reformage — l'indice d'octane · 5. Importance économique : le pétrole en Côte d'Ivoire · 6. Les enjeux environnementaux | fait |
| 6 | Quelques composés oxygénés | `ComposesOxygenes` | 1. Les alcools : définition, classes, nomenclature, propriétés · 2. Les phénols (simple mention) · 3. Les aldéhydes et les cétones : le groupe carbonyle · 4. Les acides carboxyliques : le groupe carboxyle, acidité faible · 5. Les esters : groupe fonctionnel, odeurs fruitées · 6. L'oxydation ménagée des alcools · 7. Les tests de reconnaissance des composés oxygénés | fait |
| 7 | L'éthanol | `Ethanol` | 1. Généralités : formule et classe de l'éthanol · 2. Obtention de l'éthanol · 3. Propriétés physiques de l'éthanol · 4. Propriétés chimiques de l'éthanol · 5. Le degré alcoolique d'une boisson · 6. Tests de reconnaissance des alcools · 7. Usages de l'éthanol et dangers de l'alcoolisme | fait |
| 8 | Estérification et hydrolyse d'un ester | `EsterificationHydrolyse` | 1. Les esters : structure, nomenclature et occurrence · 2. La réaction d'estérification : équation générale · 3. Caractéristiques de l'estérification : lente, athermique, limitée · 4. Catalyse par les ions H⁺ ; rôle de l'acide sulfurique · 5. L'équilibre estérification-hydrolyse : limite de réaction et taux d'avancement · 6. Comment augmenter le rendement d'une estérification ? · 7. L'hydrolyse des esters · 8. Aperçu de la saponification : hydrolyse basique et savons · 9. Usages des esters : arômes, parfums, fibres | fait |
| 9 | Réactions d'oxydoréduction en solution aqueuse | `OxydoreductionSolutionAqueuse` | 1. Oxydation, réduction, oxydant, réducteur : définitions fondamentales · 2. Les couples oxydant/réducteur (couples redox) · 3. Les demi-équations électroniques · 4. Méthode d'équilibrage des demi-équations en milieu acide · 5. Équation bilan d'une réaction d'oxydoréduction · 6. Étude de quelques couples usuels · 7. Réaction entre deux couples : sens spontané (approche expérimentale) | fait |
| 10 | Classification qualitative des couples oxydant/réducteur | `ClassificationQualitativeRedox` | 1. Force des oxydants et des réducteurs : expériences, observations, interprétation, conclusion · 2. Construction expérimentale d'une classification qualitative (couples redox métalliques, action des acides sur les métaux, place du couple H₃O⁺/H₂) · 3. Règle du gamma : sens de la réaction spontanée, prévision des réactions possibles · 4. Applications : métallurgie, protection des métaux, récupération des métaux | fait |
| 11 | Classification quantitative des couples oxydant/réducteur | `ClassificationQuantitativeRedox` | 1. Rappels : de la classification qualitative à la nécessité d'un critère quantitatif · 2. La pile Daniell : point de départ expérimental · 3. L'électrode normale à hydrogène (ENH) : la référence des potentiels · 4. Le potentiel standard d'oxydoréduction E° et l'échelle des E° · 5. Signification des valeurs de E° : force des oxydants et des réducteurs · 6. Prévision quantitative des réactions d'oxydoréduction · 7. Comparaison avec la règle du gamma · 8. Tableau récapitulatif des potentiels standard usuels | fait |
| 12 | Couples oxydant/réducteur en solution aqueuse — dosages d'oxydoréduction | `DosagesOxydoreduction` | 1. Généralités sur les dosages d'oxydoréduction : but, principe du dosage direct, équivalence et son repérage · 2. La manganimétrie : dosage par le permanganate de potassium · 3. L'iodométrie : dosages mettant en jeu le diiode et l'ion thiosulfate · 4. Relation générale à l'équivalence : formulation stœchiométrique et électronique · 5. Applications : concentration, titre de l'eau oxygénée « en volumes », degré chlorométrique de l'eau de Javel, dosage en retour · 6. Rigueur expérimentale : verrerie, rinçage, goutte à goutte | fait |
| 13 | Oxydoréduction par voie sèche | `OxydoreductionVoieSeche` | 1. Généralisation de la notion d'oxydoréduction : les réactions par voie sèche · 2. Le nombre d'oxydation : définition et règles de calcul · 3. Variation du nombre d'oxydation au cours d'une réaction · 4. Exemples de réactions par voie sèche (combustion des métaux dans O₂, réduction des oxydes métalliques : aluminothermie, réduction de CuO par H₂ ou par le carbone) · 5. Applications métallurgiques : sidérurgie et obtention des métaux | fait |
| 14 | Électrolyse | `Electrolyse` | 1. Le phénomène d'électrolyse : expérience de découverte, définition, montage, sens des porteurs de charge, réactions aux électrodes · 2. Électrolyses à électrodes inertes (acide sulfurique, chlorure de sodium, sulfate de cuivre) · 3. Électrolyse à électrode soluble (anode attaquable) : cas de CuSO₄ avec anode de cuivre, raffinage du cuivre · 4. Aspect quantitatif de l'électrolyse : quantité d'électricité Q=I×t, lien avec la quantité de matière déposée · 5. Applications industrielles de l'électrolyse | fait |
| 15 | Corrosion et protection des métaux | `CorrosionProtectionMetaux` | 1. La corrosion : un phénomène d'oxydoréduction · 2. Conditions de la corrosion du fer : les expériences témoins · 3. Nature de la rouille · 4. Mécanisme simplifié de la corrosion humide · 5. Les moyens de protection des métaux · 6. Coût économique et enjeux pour les infrastructures | fait |

Convention de nommage des scènes pour cette matière :
`Chimie_<NomChapitre>_NN.py` (ex : `Chimie_GeneralitesComposesOrganiques_01.py`).
Tag de rendu HD par chapitre : `chapitre__1ereC__Chimie__<NomChapitre>`.

Le découpage précis en scènes (une scène par notion, jamais fourre-tout —
voir CLAUDE.md) est affiné au moment d'écrire chaque chapitre, à partir de
la lecture intégrale de ses pages dans le PDF.

---

## 1ereC — Maths (`1ereC/Maths.pdf`, 211 pages, 17 chapitres)

Page 2 du PDF vérifiée : code couleur des 9 catégories de contenu identique
à celui déjà intégré dans `constants.py`/`shapes/boxes.py` (DÉFINITION,
THÉORÈME, PROPRIÉTÉ, EXEMPLE, MÉTHODE, REMARQUE, EXERCICE, CORRIGÉ,
L'ESSENTIEL À RETENIR). Pas de collision de nom de matière à craindre avec
`1ereD/Maths.pdf` : les deux PDF partagent le même nom de matière
(`Maths`), donc les `NomChapitre` de cette série et de `1ereD` devront
rester distincts lors du découpage de `1ereD/Maths.pdf` (à faire plus
tard) pour éviter toute collision de motif de fichiers de scènes.

| # | Titre officiel | NomChapitre | Sous-sections | Statut |
|---|---|---|---|---|
| 1 | Équations et inéquations du second degré dans ℝ | `EquationsInequationsSecondDegre` | 1. Équations du second degré : forme canonique, discriminant, résolution, factorisation, somme et produit des racines · 2. Signe du trinôme et inéquations du second degré · 3. Équations et inéquations se ramenant au second degré : bicarrées, avec valeurs absolues, irrationnelles · 4. Problèmes de mise en équation | fait |
| 2 | Angles orientés et trigonométrie | `AnglesOrientesTrigonometrie` | 1. Cercle trigonométrique et radian · 2. Angle orienté de deux vecteurs · 3. Lignes trigonométriques · 4. Formules de trigonométrie · 5. Équations trigonométriques · 6. Inéquations trigonométriques simples | fait |
| 3 | Généralités sur les fonctions | `GeneralitesFonctions` | 1. Ensemble de définition — image d'un élément · 2. Parité : fonctions paires, fonctions impaires · 3. Périodicité · 4. Sens de variation · 5. Extremums — majorant, minorant · 6. Composition de fonctions · 7. Restriction et prolongement d'une fonction · 8. Bijection et fonction réciproque · 9. Fonctions associées et leurs courbes | fait |
| 4 | Barycentre | `Barycentre` | 1. Barycentre de deux points pondérés : existence et unicité, homogénéité, position, réduction de vecteurs, coordonnées · 2. Barycentre de trois points pondérés : isobarycentre, réduction, coordonnées, associativité (barycentres partiels) · 3. Applications : alignement, concours de droites, lignes de niveau et lieux géométriques, centre de gravité | fait |
| 5 | Limites et continuité | `LimitesContinuite` | 1. Notion de limite : en +∞/−∞, en un point, à gauche/à droite, limites des fonctions élémentaires · 2. Opérations sur les limites et formes indéterminées · 3. Limites et comparaison : théorème des gendarmes, limites trigonométriques de référence · 4. Continuité en un point, sur un intervalle, prolongement par continuité · 5. Théorème des valeurs intermédiaires | fait |
| 6 | Dénombrement | `Denombrement` | 1. Ensembles finis et cardinal : partition, principe additif, produit cartésien, principe multiplicatif · 2. Les p-listes (p-uplets) · 3. Arrangements et permutations : notation factorielle, anagrammes · 4. Combinaisons : coefficients binomiaux, triangle de Pascal, formule du binôme de Newton · 5. Modélisation des problèmes de dénombrement : les tirages | fait |
| 7 | Extension de la notion de limite | `ExtensionNotionLimite` | 1. Limite à gauche et limite à droite · 2. Limites de fonctions rationnelles et irrationnelles · 3. Asymptotes verticales et horizontales · 4. Asymptotes obliques · 5. Directions asymptotiques et branches infinies · 6. Position relative d'une courbe par rapport à son asymptote · 7. Application à l'étude de fonctions | fait |
| 8 | Composées de transformations du plan | `ComposeesTransformationsPlan` | 1. Rappels sur les transformations usuelles du plan · 2. Généralités sur la composée de deux transformations · 3. Composée de deux translations — de deux symétries centrales · 4. Composée de deux symétries axiales · 5. Composée de deux rotations · 6. Composée de deux homothéties · 7. Composée d'une homothétie et d'une translation · 8. Décomposition des transformations usuelles · 9. Applications : constructions et lieux géométriques | fait |
| 9 | Dérivation | `Derivation` | 1. Taux d'accroissement · 2. Nombre dérivé — dérivabilité en un point · 3. Tangente à une courbe et approximation affine · 4. Fonction dérivée — dérivées des fonctions usuelles · 5. Opérations sur les fonctions dérivables · 6. Dérivée de x↦f(ax+b) et de x↦√u(x) · 7. Signe de la dérivée et sens de variation · 8. Extremums locaux · 9. Dérivées successives | fait |
| 10 | Orthogonalité dans l'espace | `OrthogonaliteEspace` | 1. Droites orthogonales et droites perpendiculaires · 2. Droite et plan orthogonaux · 3. Projeté orthogonal — distance d'un point à un plan/à une droite · 4. Plans perpendiculaires · 5. Applications aux solides usuels | fait |
| 11 | Étude et représentation graphique d'une fonction | `EtudeGraphiqueFonctions` | 1. Le plan complet d'étude d'une fonction (les sept étapes) · 2. Étude des fonctions polynômes du 3e degré · 3. Étude des fonctions homographiques · 4. Fonctions rationnelles et asymptote oblique · 5. Étude des fonctions irrationnelles simples · 6. Étude des fonctions trigonométriques simples · 7. Intersections de courbes et lectures graphiques | fait |
| 12 | Probabilité | `Probabilite` | 1. Expériences aléatoires et événements : univers, opérations sur les événements · 2. Probabilité sur un ensemble fini : définition, propriétés, équiprobabilité, probabilités et dénombrement, arbres et tableaux à double entrée · 3. Variables aléatoires réelles : loi de probabilité, espérance, variance et écart-type, application aux jeux de hasard | fait |
| 13 | Systèmes d'équations linéaires dans ℝ² et ℝ³ | `SystemesEquationsLineaires` | 1. Systèmes de deux équations à deux inconnues : substitution, combinaison linéaire, déterminant et formules de Cramer, discussion, interprétation géométrique · 2. Déterminant d'ordre 3 : règle de Sarrus, propriétés · 3. Systèmes de trois équations à trois inconnues : substitution, pivot de Gauss, formules de Cramer, discussion, interprétation géométrique · 4. Mise en système de problèmes concrets | fait |
| 14 | Géométrie analytique du plan | `GeometrieAnalytiquePlan` | 1. Repère du plan et coordonnées de vecteurs · 2. Déterminant de deux vecteurs et colinéarité · 3. Équations de droites · 4. Distance d'un point à une droite · 5. Cercle : équations, intersections, tangentes | fait |
| 15 | Suites numériques | `SuitesNumeriques` | 1. Généralités sur les suites numériques · 2. Sens de variation — suites majorées, minorées, bornées · 3. Suites arithmétiques · 4. Suites géométriques · 5. Suites arithmético-géométriques · 6. Notions de limites de suites · 7. Résolution de problèmes contextualisés | fait |
| 16 | Vecteurs de l'espace | `VecteursEspace` | 1. Extension à l'espace de la notion de vecteur · 2. Vecteurs colinéaires et alignement · 3. Vecteurs coplanaires · 4. Bases et repères de l'espace · 5. Applications : parallélisme de droites et de plans, milieu d'un segment, centre de gravité d'un tétraèdre, sections de solides | fait |
| 17 | Statistique à une variable | `StatistiqueUneVariable` | 1. Vocabulaire et organisation des données : population, caractère, modalités, effectifs, fréquences, cumuls · 2. Regroupement en classes et représentations graphiques : histogramme, polygones · 3. Caractéristiques de position : mode, médiane, quartiles, moyenne · 4. Caractéristiques de dispersion : étendue, écart interquartile, écart moyen, variance, écart-type | fait |

Convention de nommage des scènes pour cette matière :
`Maths_<NomChapitre>_NN.py` (ex : `Maths_EquationsInequationsSecondDegre_01.py`).
Tag de rendu HD par chapitre : `chapitre__1ereC__Maths__<NomChapitre>`.
**Attention** : un fichier `scenes/Maths_Test_01.py` préexiste (scène de
test hors programme, PR #1/#2) — ne pas le supprimer ni le confondre avec
un chapitre réel.

Le découpage précis en scènes (une scène par notion, jamais fourre-tout —
voir CLAUDE.md) est affiné au moment d'écrire chaque chapitre, à partir de
la lecture intégrale de ses pages dans le PDF.

---

## 1ereC — Physique (`1ereC/Physique.pdf`, 141 pages, 13 chapitres)

| # | Titre officiel | NomChapitre | Sous-sections | Statut |
|---|---|---|---|---|
| 1 | Travail et puissance dans le cas d'un mouvement de translation | `TravailPuissanceTranslation` | 1. Travail d'une force constante en translation : définition, expression, travail moteur/résistant/nul, déplacement quelconque · 2. Travail du poids : W=±mgh, indépendance du chemin suivi · 3. Travail d'une force de frottement : dépendance du chemin suivi · 4. Puissance d'une force constante : moyenne et instantanée P=F⃗·v⃗ · 5. Unités et rendement | fait |
| 2 | Travail et puissance dans le cas d'un mouvement de rotation autour d'un axe fixe | `TravailPuissanceRotation` | 1. Rappels sur le mouvement de rotation (abscisse angulaire, vitesse angulaire, vitesse linéaire) · 2. Moment d'une force par rapport à un axe fixe, règle du tire-bouchon · 3. Moment d'un couple de forces · 4. Travail d'une force de moment constant (W=ℳΔθ) · 5. Puissance en rotation (P=ℳω) · 6. Théorème des moments (équilibre) · 7. Applications : treuil, pédalier, machines simples | fait |
| 3 | Énergie cinétique | `EnergieCinetique` | 1. Énergie cinétique de translation (½mv²) · 2. Énergie cinétique de rotation (½J_Δω²) et moment d'inertie · 3. Moments d'inertie usuels (cerceau, cylindre, sphère, tige) · 4. Théorème de l'énergie cinétique (translation et rotation) · 5. Applications : freinage, chute libre, pendule simple | fait |
| 4 | Énergie potentielle | `EnergiePotentielle` | 1. Notion d'énergie potentielle · 2. Énergie potentielle de pesanteur (Epp=mgz+Cte), choix de la référence, variation ΔEpp=−W(poids) · 3. Énergie potentielle élastique (Epe=½kx²), travail de la tension d'un ressort · 4. Forces conservatives et énergie potentielle associée (approche qualitative) | fait |
| 5 | Énergie mécanique | `EnergieMecanique` | 1. Rappels (énergie cinétique, potentielle de pesanteur, potentielle élastique, théorème de l'énergie cinétique) · 2. Énergie mécanique Em=Ec+Ep · 3. Conservation de l'énergie mécanique (forces conservatives) · 4. Non-conservation (ΔEm=W(frottements)) · 5. Applications : chute libre, pendule simple, mouvement sur piste, transferts d'énergie | fait |
| 6 | Champ électrostatique | `ChampElectrostatique` | 1. Les charges électriques : électrisation, quantification, conducteurs/isolants · 2. Loi de Coulomb · 3. Champ électrostatique, vecteur champ créé par une charge ponctuelle, principe de superposition · 4. Lignes de champ (charge seule, dipôle) · 5. Champ uniforme entre armatures (E=U/d) · 6. Force subie par une charge dans un champ | fait |
| 7 | Énergie potentielle électrostatique | `EnergiePotentielleElectrostatique` | 1. Potentiel électrique et différence de potentiel · 2. Travail de la force électrostatique dans un champ uniforme, force conservative · 3. Relation champ-potentiel (U=E·d), surfaces équipotentielles · 4. Énergie potentielle électrostatique Ep=qV, électronvolt · 5. Applications : condensateur plan, accélération de particules | fait |
| 8 | Puissance et énergie électriques | `PuissanceEnergieElectriques` | 1. Rappels : courant, tension, dipôles, conventions · 2. Énergie et puissance électriques d'un dipôle (W=UIt, P=UI) · 3. Effet Joule et loi d'Ohm · 4. Bilan énergétique d'un générateur (E, r, rendement) · 5. Bilan énergétique d'un récepteur (E', r', rendement) · 6. Loi de Pouillet · 7. Kilowattheure et facturation de l'énergie électrique | fait |
| 9 | Le condensateur | `Condensateur` | 1. Constitution et symbole d'un condensateur · 2. Charge à courant constant (q=It, u=q/C) · 3. Capacité, le farad, condensateur plan · 4. Association de condensateurs (série/parallèle) · 5. Énergie emmagasinée (E=½Cu²) · 6. Charge/décharge à travers un résistor, constante de temps τ=RC · 7. Applications : flash, lissage | à faire |
| 10 | L'amplificateur opérationnel | `AmplificateurOperationnel` | 1. Présentation de l'AO (bornes, alimentation, symbole) · 2. AO idéal : régimes linéaire et saturé (i+=i−=0, ε=0 en linéaire) · 3. Régime saturé : le comparateur · 4. Montages en régime linéaire : suiveur, inverseur, non inverseur (démonstrations des gains) · 5. Conditions de linéarité et applications | fait |
| 11 | Introduction à l'optique géométrique | `IntroductionOptiqueGeometrique` | 1. Sources et récepteurs de lumière (primaire/secondaire, ponctuelle/étendue) · 2. Milieux transparent/translucide/opaque · 3. Propagation rectiligne, rayons et faisceaux lumineux · 4. Ombre, pénombre et éclipses · 5. Célérité de la lumière · 6. Principe de réversibilité | à faire |
| 12 | Réflexion et réfraction de la lumière blanche | `ReflexionRefractionLumiere` | 1. Réflexion de la lumière (lois de Snell-Descartes) · 2. Le miroir plan (image, construction, démonstration) · 3. Réfraction (indice, lois de Snell-Descartes, n1sin i1=n2sin i2) · 4. Réflexion totale, angle limite, fibre optique, fontaine lumineuse · 5. Lame à faces parallèles (déplacement latéral) | à faire |
| 13 | Les lentilles minces | `LentillesMinces` | 1. Généralités : types de lentilles, symboles · 2. Caractéristiques (centre optique, foyers, distance focale, vergence, plans focaux, conditions de Gauss) · 3. Construction graphique (trois rayons particuliers) · 4. Relations de conjugaison (Descartes, Newton), grandissement · 5. Applications : loupe, appareil photographique, œil réduit | à faire |

Convention de nommage des scènes pour cette matière :
`Physique_<NomChapitre>_NN.py` (ex : `Physique_EnergieMecanique_01.py`).
Tag de rendu HD par chapitre : `chapitre__1ereC__Physique__<NomChapitre>`.

Le découpage précis en scènes (une scène par notion, jamais fourre-tout —
voir CLAUDE.md) est affiné au moment d'écrire chaque chapitre, à partir de
la lecture intégrale de ses pages dans le PDF.

---

## Autres matières/séries — à découper

Sommaire à extraire depuis le PDF source correspondant avant d'écrire la
moindre scène (voir CLAUDE.md, section "Pipeline de travail").

- `1ereD/Maths.pdf` (196 pages)
- `1ereD/Physique-Chimie.pdf` (293 pages)
