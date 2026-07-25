# Projet : Vidéos de cours animées — Séries 1ère C & 1ère D

## Contexte
Création de vidéos pédagogiques animées avec **Manim** à partir des supports
PDF officiels (`1ereC/` : Maths, Physique, Chimie, SVT — `1ereD/` : Maths,
Physique-Chimie, SVT). Public : lycéens ivoiriens, narration en français,
voix off masculine.

## ⚠️ Prochaine étape obligatoire (avant toute autre chose)

## Légende de contenu (couleur.pdf) — déjà intégrée
`couleur.pdf` définit le code couleur des 9 types de contenu pédagogique,
**partagé entre 1ereC et 1ereD** (confirmé). Les couleurs ont été mesurées
pixel par pixel sur le rendu rasterisé du PDF (pas de valeurs devinées) et
sont déjà intégrées dans `constants.py` (dict `BOX_STYLES`) et exposées via
`shapes/boxes.py` :

| Fonction              | Catégorie              | Bandeau (accent) | Fond      |
|------------------------|-------------------------|------------------|-----------|
| `definition_box()`     | DÉFINITION              | bleu `#1E5FA8`   | `#E3F3FF` |
| `theorem_box()`        | THÉORÈME                | violet `#74458C` | `#F0E7FA` |
| `property_box()`       | PROPRIÉTÉ               | vert sarcelle `#288073` | `#E0F5F6` |
| `example_box()`        | EXEMPLE                 | orange `#DE7C1F` | `#FDF0E0` |
| `method_box()`         | MÉTHODE                 | magenta `#A42A5A`| `#FFE6F5` |
| `warning_box()`        | REMARQUE (gris, pas de teinte) | `#595959` | `#F1F1F1` |
| `exercise_box()`       | EXERCICE                | rouge `#B42E41`  | `#FAE1E3` |
| `corrige_box()`        | CORRIGÉ                 | vert `#267540`   | `#DCF7E8` |
| `essentiel_box()`      | L'ESSENTIEL À RETENIR   | noir `#1B1B1B`   | `#F9F6EF` |

Chaque fonction prend un `Mobject` (texte, `MathTex`, schéma, etc.) en
paramètre et renvoie une `VGroup` (bandeau de titre + corps), dimensionnée
directement à la taille réelle du contenu (correctif 3 appliqué).

## Stack technique
- Python 3.12 dans un venv dédié (`.venv/`)
- **Manim Community Edition** (`manim`) pour l'animation
- **manim-voiceover** + service TTS maison `EdgeTTSService` (Microsoft Edge
  TTS, gratuit, voix `fr-FR-HenriNeural` — masculine, française)
- **MiKTeX** pour la compilation LaTeX (`MathTex`)
- **ffmpeg** pour l'assemblage final des vidéos de chapitre

### Installation (à faire une seule fois, en tout début de projet)
```bash
python -m venv .venv
./.venv/Scripts/pip install manim manim-voiceover edge-tts
```
Puis, **immédiatement après l'install de MiKTeX**, lancer :
```bash
miktex.exe packages update
```
> Sans cette étape, la compilation LaTeX échoue silencieusement en mode
> batchmode avec une erreur du type « not checked for updates », qui bloque
> TOUT rendu contenant une formule (`MathTex`). C'est la toute première
> chose à faire, avant d'écrire la moindre scène.

## Structure du projet
```
video_cours/
├── CLAUDE.md
├── .github/
│   ├── workflows/
│   │   └── render-manim.yml   # pipeline autonome (voir "Pipeline autonome")
│   └── scripts/
│       └── detect_scenes.py   # logique de détection scène/mode/série/matière
├── 1ereC/                  # PDF sources (déjà présents)
│   ├── Maths.pdf
│   └── Maths/                 # créé automatiquement par le pipeline —
│       └── Chapitre_Derivation.mp4   # vidéo finale, à côté du PDF utilisé
├── 1ereD/                  # PDF sources (déjà présents)
├── constants.py            # palette + couleurs sémantiques — lecture seule pour les agents d'écriture
├── tts_service.py          # EdgeTTSService (SpeechService)
├── shapes/
│   ├── base_scene.py       # NotionScene (VoiceoverScene + fond + wait() sécurisé)
│   └── boxes.py            # definition_box, theorem_box, property_box,
│                           # example_box, method_box, warning_box,
│                           # exercise_box, corrige_box, essentiel_box,
│                           # scene_title (voir section "Légende de contenu")
├── scenes/                 # un fichier par chapitre : Matiere_NomChapitre_NN.py
├── media/                  # sortie Manim — ne pas versionner, ne jamais rm -rf en partagé
├── chapters/               # assemblage LOCAL (poste de travail) uniquement —
│                           # le pipeline cloud écrit dans <Serie>/<Matiere>/
└── PROGRAMME.md            # découpage complet des chapitres par matière/série
```
> Si les deux séries (C et D) ont des chartes graphiques différentes dans
> leurs PDF respectifs, dupliquer `constants.py` par série
> (`constants_1ereC.py` / `constants_1ereD.py`) plutôt que de forcer une
> palette unique — vérifier la 2ᵉ page de CHAQUE PDF avant de commencer.

⚠️ **La vidéo finale d'un chapitre est écrite automatiquement dans
`<Serie>/<Matiere>/`, au même endroit que le PDF source utilisé** (ex :
`1ereC/Maths/Chapitre_Derivation.mp4` à côté de `1ereC/Maths.pdf`) — voir
"Pipeline autonome" pour le mécanisme complet (tag git → écriture →
commit).

## Conventions de code
- Une classe `Scene` par notion pédagogique (jamais de scène fourre-tout)
- Nommage : `Matiere_NomChapitre_NN.py` (ex: `Maths_Derivation_06.py`).
  **`Matiere` doit être IDENTIQUE au nom du PDF source sans extension**
  (ex : `Maths` pour `1ereC/Maths.pdf`, `Physique` pour
  `1ereC/Physique.pdf`) — le pipeline autonome s'appuie sur cette
  correspondance exacte pour écrire la vidéo finale au bon endroit (voir
  "Pipeline autonome"). Une incohérence ici (ex: scène nommée `Math_...`
  pour un PDF `Maths.pdf`) fait échouer le rendu HD avec un message
  explicite plutôt que d'écrire au mauvais endroit.
- Chaque notion suit la structure : énoncé → animation du raisonnement →
  exemple traité → à retenir → pièges à éviter
- Texte à l'écran minimal, voix off pour porter l'explication
- Hériter de `NotionScene` (dans `shapes/base_scene.py`) pour chaque scène :
  donne accès à `self.voiceover(...)` et au fond de la charte sans rien
  reconfigurer
- Narration : bloc `with self.voiceover(text="...") as tracker:` suivi des
  animations, puis `self.wait(tracker.get_remaining_duration())` pour caler
  la durée sur l'audio réellement généré
- **Ne jamais écrire de LaTeX brut dans un `Text(...)`** (seul `MathTex`
  interprète le LaTeX) : pour Δ, α, β, etc. dans un `Text`, utiliser
  directement le caractère Unicode, pas `$\Delta$`
- Vérifier que les scènes voisines / variantes (ex: 3 mini-schémas Δ>0 /
  Δ=0 / Δ<0) utilisent bien des paramètres distincts — un copier-coller de
  formule entre scènes similaires produit facilement un rendu dupliqué
  identique sans qu'aucune erreur ne soit levée

## Bugs déjà rencontrés — correctifs à appliquer d'emblée
Ces bugs ont tous été rencontrés et corrigés sur le projet précédent. Les
correctifs ci-dessous doivent être appliqués dès le départ pour ne pas les
reproduire.

1. **MiKTeX batchmode fatal** → lancer `miktex.exe packages update` avant
   tout rendu contenant du LaTeX (voir Installation ci-dessus).

2. **Chemin court Windows (8.3, ex: `GOFCBB~1`)** → si le chemin absolu du
   projet ou du `--media_dir` contient un segment 8.3, pdfTeX échoue. Ne
   jamais rediriger `--media_dir` vers un chemin `%TEMP%` à nom court ;
   rester dans l'arborescence longue du projet.

3. **Boîtes déformées (`SurroundingRectangle` étiré)** → utiliser
   `RoundedRectangle` dimensionné directement à la taille du contenu plutôt
   que d'étirer un `SurroundingRectangle` de façon anisotrope (voir
   `shapes/boxes.py`).

4. **Indexation d'un `Text(...)`** → les indices d'un `Text` correspondent
   aux glyphes visibles UNIQUEMENT, pas aux espaces. `Text("A B I D J A N")`
   ne compte que 7 caractères, pas 13. Vérifier tout accès `mobject[i]` sur
   un `Text` contenant des espaces.

5. **`\\` suivi de `[` dans un `MathTex`** (ex: environnement `array`) →
   LaTeX interprète `\\[` comme la forme optionnelle `\\[longueur]` et lève
   « Missing number, treated as zero ». Insérer `{}` juste après le `\\`
   pour désambiguïser :
   ```python
   r"... \\ {} [a;+\infty[ & ..."   # et non r"... \\ [a;+\infty[ & ..."
   ```

6. **`self.wait(tracker.get_remaining_duration())` avec durée 0** → quand
   les animations jouées ont déjà consommé toute la durée de l'audio, la
   durée restante peut être exactement `0.0`, et `Scene.wait()` refuse une
   durée `<= 0`. Corrigé une bonne fois dans `NotionScene.wait()`
   (`shapes/base_scene.py`) : toute durée `<= 0` est remplacée par une
   frame minimale (`1 / frame_rate`) au lieu de faire planter le rendu. À
   reporter tel quel dans ce projet :
   ```python
   def wait(self, duration=1, stop_condition=None, frozen_frame=None):
       if duration is None or duration <= 0:
           duration = 1 / self.camera.frame_rate
       return super().wait(duration, stop_condition=stop_condition, frozen_frame=frozen_frame)
   ```

7. **Assemblage ffmpeg avec perte de la voix off** → ne JAMAIS concaténer
   les scènes d'un chapitre avec `-c copy` (stream-copy) : l'AAC de clips
   encodés indépendamment donne un flux audio parfois illisible malgré des
   métadonnées correctes (ffprobe/volumedetect ne le détectent pas
   forcément). Toujours ré-encoder intégralement :
   ```bash
   ffmpeg -y -f concat -safe 0 -i liste.txt \
     -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k \
     "chapters/Chapitre_NN_Nom.mp4"
   ```
   (baisser à `-preset veryfast -crf 20` uniquement si un rendu Manim
   concurrent sature déjà le CPU et fait timeout le job ffmpeg).
   Le fichier `liste.txt` du concat demuxer doit contenir des chemins
   **Windows** (`C:\...`), pas des chemins MSYS — utiliser `pwd -W` pour les
   générer, car `ffmpeg.exe` est un binaire natif Windows.

8. **Dossier `media/` partagé** → ne jamais faire de `rm -rf` dessus : un
   autre agent peut être en train d'y écrire en parallèle. Pour un rendu de
   test isolé, toujours utiliser `--media_dir media_test_chNN` dédié et ne
   supprimer QUE ce dossier isolé après vérification.

9. **Fichier vidéo corrompu (« moov atom not found »)** → survient quand un
   process ffmpeg ou manim est interrompu en plein encodage (arrêt de
   session, tool call annulé). Correctif systématique : supprimer le
   fichier corrompu et relancer l'encodage jusqu'au bout (idéalement en
   arrière-plan avec log explicite du code de sortie).

10. **Jobs en arrière-plan tués par redémarrage de session/environnement**
    → ne jamais se fier uniquement au log d'un script de rendu pour
    connaître l'état réel. Après toute interruption suspecte, revérifier
    l'état sur disque (quelles scènes `.mp4` existent réellement dans
    `media/videos/.../1080p60/`) avant de décider quoi relancer.

11. **« Stall » apparent de plusieurs heures** → si la machine est un
    portable, une mise en veille suspend (sans planter) un rendu en cours ;
    ce n'est pas un bug de code, seulement un besoin de garder la machine
    éveillée pendant les rendus longs.

## Pipeline de travail (ordre à respecter)
1. Palette de couleurs sémantiques de contenu (définition, théorème,
   propriété, exemple, méthode, remarque, exercice, corrigé, essentiel) →
   déjà extraite de `couleur.pdf` et intégrée dans `constants.py` en
   conséquence (voir section "Légende de contenu" ci-dessus).
2. `shapes/boxes.py` est déjà écrit (les 9 boîtes + `scene_title()`
   provisoire). Reste à écrire `shapes/base_scene.py` (voir correctifs 3 et
   6 ci-dessus intégrés dès le départ).
3. Découper le programme complet en chapitres/scènes → `PROGRAMME.md`.
4. Écrire l'intégralité des scènes de tous les chapitres, narration
   comprise (`self.voiceover(...)`), et les faire **auto-relire par
   l'agent** (checklist ci-dessous, section "Pipeline autonome") —
   **avant** de pousser le moindre commit. Depuis la mise en place du
   pipeline autonome, il n'y a plus de relecture humaine à cette étape :
   c'est l'agent lui-même qui atteste que le chapitre est prêt.
5. Une fois un chapitre écrit et auto-relu : pousser un tag
   `chapitre__<Serie>__<Matiere>__<NomChapitre>` (ex :
   `chapitre__1ereC__Maths__Derivation` — voir section "Pipeline
   autonome") — cela déclenche automatiquement le rendu HD, l'écriture de
   la vidéo dans `<Serie>/<Matiere>/` (à côté du PDF source correspondant)
   et sa publication, sans action manuelle.
   - **En local** (mode dégradé si le cloud est indisponible) : par
     défaut, un seul rendu à la fois (plus simple à diagnostiquer en cas
     d'erreur). **Si la vitesse prime**, il est possible de lancer **2 à 3
     process `manim -qh -a` en parallèle** (sur des chapitres différents)
     — décision validée explicitement par l'utilisateur sur ce type de
     projet. Accepter dans ce cas le risque de contention CPU déjà observé
     (ralentissement des rendus, timeout d'un job `ffmpeg` concurrent —
     voir correctif 7, baisser vers `-preset veryfast` si besoin) : ne pas
     dépasser 3 process simultanés, et toujours confirmer avec
     l'utilisateur avant de dépasser le mode solo puisque cela reste une
     dérogation à la règle par défaut, pas la norme.
   - **En cloud** (voie normale désormais, voir « Pipeline autonome »
     ci-dessous) : la contention CPU ne s'applique plus, chaque chapitre
     tournant sur sa propre VM isolée — le parallélisme y est la norme, pas
     une dérogation.
6. Pour chaque chapitre entièrement rendu : assembler les scènes avec
   ffmpeg (correctif 7), puis vérifier :
   ```bash
   ffprobe -show_entries stream=codec_type,codec_name -of default=nw=1 chapters/Chapitre_NN.mp4
   ffmpeg -i chapters/Chapitre_NN.mp4 -af volumedetect -f null - 2>&1 | grep mean_volume
   ```
   (présence de flux `h264`+`aac`, et `mean_volume` nettement au-dessus du
   silence, typiquement autour de -20 à -30 dB).

## Exécution cloud (GitHub Actions)

En complément du rendu local (Windows), les rendus peuvent être délégués à
un workflow GitHub Actions (`.github/workflows/render-manim.yml`). Ce mode
est utile pour paralléliser massivement sans contention CPU (chaque
chapitre tourne sur sa propre VM Ubuntu) ou pour libérer le poste local
pendant l'écriture des scènes suivantes.

**⚠️ Dépôt unique autorisé : `https://github.com/ibif/video_cours`.** Le
workflow ne doit tourner que sur ce dépôt (`github.repository ==
'ibif/video_cours'`), jamais sur un fork ou un clone. Cette restriction est
imposée dans le workflow lui-même (voir `.github/workflows/render-manim.yml`
: condition `if` en tête de chaque job) — ce n'est pas qu'une convention
documentée ici, un fork qui tenterait de lancer le workflow verrait ses
jobs s'arrêter immédiatement.

### Prérequis avant tout lancement cloud
1. **Tout ce dont Manim a besoin doit être versionné dans git** :
   `1ereC/`, `1ereD/`, `constants.py` (ou `constants_1ereC.py` /
   `constants_1ereD.py`), `shapes/`, `scenes/`. Le workflow clone le repo à
   froid — il n'a **aucun accès au disque local**, contrairement à un
   agent qui reprendrait une session existante sur le poste.
2. `media/` reste dans `.gitignore` (jamais versionné, comme en local).
3. Si les PDF sources ou les vidéos assemblées dépassent quelques dizaines
   de Mo, activer **Git LFS** pour éviter un clone trop lent côté runner.
   **Ce point devient important dès la mise en place du pipeline
   autonome** : les vidéos finales sont désormais committées directement
   dans le dépôt (`git lfs track "*.mp4"`), pas seulement publiées en
   Release.

### Ce qui ne se transpose PAS du mode local au mode cloud
Les runners GitHub Actions tournent sous Linux (Ubuntu) : certains
correctifs de la section « Bugs déjà rencontrés » sont spécifiques à
Windows et ne s'appliquent plus :
- **Correctif 2** (chemin court 8.3 Windows, `GOFCBB~1`) : n'existe pas
  sous Linux, aucune précaution à prendre sur les chemins.
- **Correctif 7** (chemins Windows `C:\...` via `pwd -W` pour le concat
  ffmpeg) : sous Linux, utiliser directement des chemins POSIX standards.
- **Correctifs 10 et 11** (jobs tués par redémarrage de session locale,
  mise en veille d'un portable) : sans objet, un runner GitHub Actions est
  une VM éphémère dédiée qui tourne jusqu'à la fin du job ou jusqu'au
  timeout défini.
- **MiKTeX** (Installation) : remplacé par **TeX Live**
  (`texlive`, `texlive-latex-extra`, `texlive-science`, `texlive-xetex` —
  packages `apt`), pas de `miktex.exe packages update` à lancer.

Les autres correctifs (1 en substance via TeX Live à jour, 3, 4, 5, 6, 8,
9) restent valables tels quels : ce sont des bugs de code Manim/LaTeX
indépendants de l'OS.

### Pipeline autonome (écriture + rendu par l'IA, sans intervention humaine)

⚠️ **Changement de politique explicitement demandé par l'utilisateur** :
la version précédente de ce fichier exigeait une relecture humaine avant
tout rendu. Ce n'est plus le cas — l'agent qui écrit les scènes est aussi
responsable de leur validation, et le pipeline est déclenché
automatiquement à deux niveaux, sans aucun clic ni validation manuelle :

1. **Push sur `main`** → `detect-scenes` calcule le diff git ; si des
   scènes ont changé, déclenche automatiquement un *smoke-test* cloud
   (`-ql`, rapide, peu coûteux) des scènes modifiées/ajoutées uniquement.
   Objectif : détecter une erreur de compilation ou de rendu dès le
   commit, sans attendre. (Aucune saisie manuelle : la détection se fait
   par script, voir `.github/scripts/detect_scenes.py`.)
2. **Push d'un tag au format `chapitre__<Serie>__<Matiere>__<NomChapitre>`**
   (ex : `chapitre__1ereC__Maths__Derivation`) → déclenche automatiquement
   le rendu HD (`-qh`) de toutes les scènes de ce chapitre, l'assemblage
   ffmpeg, puis :
   - **écriture de la vidéo dans `<Serie>/<Matiere>/`** — c'est-à-dire
     dans le même répertoire que le PDF source utilisé (ex :
     `1ereC/Maths/Chapitre_Derivation.mp4`, à côté de `1ereC/Maths.pdf`) —
     avec **commit + push automatique dans le dépôt** ;
   - **et publication en GitHub Release** en plus (lien de téléchargement
     permanent indépendant du dépôt).

   C'est l'agent lui-même qui pousse ce tag quand il estime le chapitre
   terminé — c'est cette action qui remplace l'ancienne relecture humaine.

   ⚠️ **`<Matiere>` dans le tag doit être EXACTEMENT le nom du PDF source
   sans extension** (ex : `Maths` pour `1ereC/Maths.pdf`), pas une
   abréviation différente du préfixe de nom de scène — sinon le workflow
   échoue explicitement (`::error::`) plutôt que d'écrire au mauvais
   endroit.

`workflow_dispatch` reste disponible en secours pour un relancement
manuel ponctuel (ex. après un correctif), mais n'est plus la voie normale.

**Checklist d'auto-relecture que l'agent doit exécuter avant de committer
un chapitre et de pousser le tag `chapitre__<Serie>__<Matiere>__<NomChapitre>` :**
- [ ] `py_compile` sur chaque scène du chapitre (aucune erreur de syntaxe).
- [ ] Rendu `-ql` local réussi sur chaque scène (aucune erreur LaTeX,
  `IndexError`, ni `wait(0)` — voir correctifs 4, 5, 6).
- [ ] Chaque scène suit la structure imposée : énoncé → animation du
  raisonnement → exemple traité → à retenir → pièges à éviter.
- [ ] Aucune notion mélangée dans une seule scène (règle "Ce qu'il ne faut
  PAS faire").
- [ ] Aucun Mobject dupliqué qui existe déjà dans `constants.py` ou
  `shapes/`.
- [ ] Narration (`self.voiceover(...)`) présente et cohérente avec
  l'animation de chaque scène.
- [ ] Nommage des fichiers conforme (`Matiere_NomChapitre_NN.py`, avec
  `Matiere` identique au nom du PDF source correspondant — voir plus haut).

Si un de ces points échoue, l'agent corrige et recommence la checklist
avant de committer — il ne pousse jamais de tag `chapitre__...` sur un
chapitre qui échoue à un seul de ces points.

**Risque assumé** : cette checklist est une auto-évaluation de l'agent, pas
une revue humaine indépendante. Une erreur de jugement de l'agent peut donc
aller jusqu'au rendu HD, à l'écriture dans le dépôt et à la publication en
Release avant d'être détectée. Si ce risque devient problématique en
pratique (erreurs publiées trop souvent), réintroduire un point de
contrôle humain avant le tag `chapitre__...` plutôt que de complexifier
davantage la checklist automatique.

### Étapes du workflow
0. **Job `detect-scenes`** : détecte automatiquement quelles scènes traiter
   — via le diff git du push (mode smoke-test), via le nom du tag
   `chapitre__<Serie>__<Matiere>__<NomChapitre>` (mode rendu HD final, avec
   extraction de la série et de la matière), ou via la saisie manuelle
   (secours `workflow_dispatch`) — et détermine le mode. Logique dans
   `.github/scripts/detect_scenes.py` (échoue explicitement avec un
   message clair si le tag ne suit pas le format attendu, ou si aucune
   scène ne correspond au motif `Matiere_NomChapitre_*.py`).
1. **Job `render`** (matrix, une VM par scène) : checkout + setup Python
   3.12, installation TeX Live + `manim`/`manim-voiceover`/`edge-tts`/
   `ffmpeg`, `py_compile` de la scène, rendu Manim à la qualité déterminée
   par le mode (`-ql` en smoke-test, `-qh` en rendu final), vérification
   `ffprobe` des flux vidéo/audio (équivalent cloud du correctif 7), upload
   des vidéos brutes en artifact.
2. **Job `assemble-et-publier`** (uniquement en mode `rendu-hd-final`,
   jamais pour un smoke-test) :
   - téléchargement de tous les rendus du chapitre ;
   - assemblage ffmpeg **avec ré-encodage complet** (jamais `-c copy`,
     correctif 7 toujours valable) ;
   - **vérification que `<Serie>/<Matiere>.pdf` existe**, puis écriture de
     la vidéo assemblée dans `<Serie>/<Matiere>/Chapitre_<NomChapitre>.mp4`
     (échec explicite si le PDF correspondant n'existe pas — protection
     contre une faute de frappe dans le tag) ;
   - **commit + push automatique sur `main`** (avec retry en cas de push
     concurrent d'un autre chapitre) ;
   - **publication en GitHub Release** en plus, taguée
     `chapitre__<Serie>__<Matiere>__<NomChapitre>` — lien de téléchargement
     permanent indépendant du dépôt.

### Limites à garder en tête
- Les artifacts GitHub Actions (rendus bruts intermédiaires uniquement,
  pas les vidéos finales qui sont en Release) ont une rétention limitée
  (14 jours dans le workflow actuel) : ce n'est pas grave puisqu'ils ne
  sont qu'un intermédiaire vers la Release, mais un chapitre qui échoue
  entre le rendu et l'assemblage doit être re-tagué avant l'expiration.
- Les runners standards GitHub ont des limites de temps d'exécution (6h
  par job par défaut) et de ressources (CPU/RAM modestes) : pour un
  chapitre très long ou beaucoup de `MathTex`, surveiller le temps de
  rendu réel avant de généraliser ce mode à tout le programme.
- Le pipeline est autonome de bout en bout : la checklist d'auto-relecture
  de l'agent (ci-dessus) est le seul point de contrôle avant publication —
  il n'y a plus de relecture humaine ni de rendu local intermédiaire à
  attendre.

## Travail en équipe d'agents
- Un agent par chapitre maximum — jamais un agent unique pour tout un livre
- Équipes petites : 2-4 agents actifs en parallèle, pas plus
- `constants.py` et `shapes/` en lecture seule pour les agents d'écriture
  (seule une session dédiée ou l'utilisateur les modifie)
- Modèle par défaut : Sonnet pour l'écriture ; Opus seulement si un
  chapitre pose un vrai problème de conception pédagogique
- Chaque agent doit, avant de conclure : `py_compile` son fichier, puis
  faire un rendu de test isolé (`--media_dir media_test_chNN`, voir
  correctif 8) pour vérifier qu'il n'y a ni erreur LaTeX, ni `IndexError`,
  ni `wait(0)`, ni bug d'indexation `Text`
- Anticiper les limites de session : si plusieurs agents échouent en même
  temps avec un message de type "session limit", ne pas essayer de les
  faire reprendre automatiquement via un scheduler cloud (celui-ci n'a pas
  accès aux fichiers locaux) — attendre le reset ou reprendre
  manuellement les derniers agents en échec

## Ce qu'il ne faut PAS faire
- Ne jamais pousser un tag `chapitre__<Serie>__<Matiere>__<NomChapitre>`
  (déclencheur du rendu HD + écriture dans le dépôt + publication) tant
  que la checklist d'auto-relecture de l'agent (section "Pipeline
  autonome") n'est pas intégralement validée
- Ne jamais utiliser un nom de `<Matiere>` dans le tag qui ne correspond
  pas exactement au nom du PDF source (`<Serie>/<Matiere>.pdf`)
- Ne pas générer de rendu HD (`-qh`) pour un simple test — utiliser `-ql`
  (ou un `media_test_chNN` isolé, voir correctif 8) ; en cloud, c'est
  automatique via le mode `smoke-test` sur un simple push de scène
- Ne pas dupliquer des Mobjects déjà définis dans `constants.py` ou
  `shapes/`
- Ne pas mélanger plusieurs notions dans une seule scène
- Ne jamais concaténer les vidéos de chapitre avec `-c copy` (correctif 7)
- Ne jamais `rm -rf` le dossier `media/` partagé (correctif 8)

## Commandes utiles
```bash
# Preview rapide d'une scène
manim -pql scenes/Maths_Derivation_06.py NomDeLaScene

# Rendu final HD d'une scène précise
manim -qh scenes/Maths_Derivation_06.py NomDeLaScene

# Rendu final HD de toutes les scènes d'un chapitre
manim -qh -a scenes/Maths_Derivation_06.py

# Génération de la liste ffmpeg (chemins Windows, requis pour concat demuxer)
# puis assemblage avec ré-encodage complet (voir correctif 7)
```
