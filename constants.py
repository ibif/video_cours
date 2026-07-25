"""
constants.py — Palette de couleurs sémantiques du cours
Extraite de couleur.pdf (légende officielle du code couleur des supports),
mesurée pixel par pixel sur le rendu rasterisé du PDF (pas de valeurs
devinées). Palette PARTAGÉE entre 1ereC et 1ereD (confirmé par l'utilisateur
— une seule légende de contenu pour les deux séries).

⚠️ Lecture seule pour les agents d'écriture de scènes (voir CLAUDE.md).
Seule une session dédiée ou l'utilisateur modifie ce fichier.

⚠️ Ce fichier couvre UNIQUEMENT la légende sémantique (définition/théorème/
etc.). Il ne fournit PAS la couleur de fond général des slides ni les
couleurs de titre de scène hors catégories — voir la note en bas de fichier.
"""

from manim import ManimColor

# --- Couleurs sémantiques par type de contenu (couleur.pdf) ---------------
# "accent" = couleur du bandeau de titre (texte du bandeau en blanc, sauf
# indication contraire) ; "fill" = fond clair du corps de la boîte.

DEFINITION_ACCENT = ManimColor("#1E5FA8")   # DÉFINITION — bleu
DEFINITION_FILL   = ManimColor("#E3F3FF")

THEOREME_ACCENT   = ManimColor("#74458C")   # THÉORÈME — violet
THEOREME_FILL     = ManimColor("#F0E7FA")

PROPRIETE_ACCENT  = ManimColor("#288073")   # PROPRIÉTÉ — vert sarcelle
PROPRIETE_FILL    = ManimColor("#E0F5F6")

EXEMPLE_ACCENT    = ManimColor("#DE7C1F")   # EXEMPLE — orange
EXEMPLE_FILL      = ManimColor("#FDF0E0")

METHODE_ACCENT    = ManimColor("#A42A5A")   # MÉTHODE — rose / magenta foncé
METHODE_FILL      = ManimColor("#FFE6F5")

REMARQUE_ACCENT   = ManimColor("#595959")   # REMARQUE — gris (pas de teinte !)
REMARQUE_FILL     = ManimColor("#F1F1F1")

EXERCICE_ACCENT   = ManimColor("#B42E41")   # EXERCICE — rouge
EXERCICE_FILL     = ManimColor("#FAE1E3")

CORRIGE_ACCENT    = ManimColor("#267540")   # CORRIGÉ — vert
CORRIGE_FILL      = ManimColor("#DCF7E8")

# L'ESSENTIEL À RETENIR : bandeau noir (pas une teinte de catégorie, un noir
# quasi pur), fond crème, texte du bandeau blanc, texte du corps noir.
ESSENTIEL_ACCENT  = ManimColor("#1B1B1B")
ESSENTIEL_FILL    = ManimColor("#F9F6EF")

WHITE_TEXT = ManimColor("#FFFFFF")
BLACK_TEXT = ManimColor("#1A1A1A")

# --- Mapping pratique pour shapes/boxes.py ---------------------------------

BOX_STYLES = {
    "definition": {"title": "DÉFINITION",           "accent": DEFINITION_ACCENT, "fill": DEFINITION_FILL, "title_text": WHITE_TEXT},
    "theoreme":   {"title": "THÉORÈME",              "accent": THEOREME_ACCENT,   "fill": THEOREME_FILL,   "title_text": WHITE_TEXT},
    "propriete":  {"title": "PROPRIÉTÉ",             "accent": PROPRIETE_ACCENT,  "fill": PROPRIETE_FILL,  "title_text": WHITE_TEXT},
    "exemple":    {"title": "EXEMPLE",                "accent": EXEMPLE_ACCENT,    "fill": EXEMPLE_FILL,    "title_text": WHITE_TEXT},
    "methode":    {"title": "MÉTHODE",                "accent": METHODE_ACCENT,    "fill": METHODE_FILL,    "title_text": WHITE_TEXT},
    "remarque":   {"title": "REMARQUE",               "accent": REMARQUE_ACCENT,   "fill": REMARQUE_FILL,   "title_text": WHITE_TEXT},
    "exercice":   {"title": "EXERCICE",                "accent": EXERCICE_ACCENT,   "fill": EXERCICE_FILL,   "title_text": WHITE_TEXT},
    "corrige":    {"title": "CORRIGÉ",                 "accent": CORRIGE_ACCENT,    "fill": CORRIGE_FILL,    "title_text": WHITE_TEXT},
    "essentiel":  {"title": "L'ESSENTIEL À RETENIR",  "accent": ESSENTIEL_ACCENT,  "fill": ESSENTIEL_FILL,  "title_text": WHITE_TEXT},
}

# --- ⚠️ Ce qui N'EST PAS couvert par couleur.pdf ---------------------------
# Ce fichier ne donne QUE la légende sémantique des 9 catégories de contenu.
# Il ne fournit PAS :
#   - la couleur de fond général des slides (canvas)
#   - la couleur des titres de scène (scene_title) hors catégories
# → Étape encore obligatoire avant les scènes (voir CLAUDE.md, "Prochaine
#   étape obligatoire") : comparer la 2ᵉ page de CHAQUE PDF de cours
#   (1ereC/ et 1ereD/) pour ces couleurs de base. La palette de ce fichier,
#   elle, est confirmée partagée entre les deux séries.
