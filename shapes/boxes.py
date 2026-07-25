"""
shapes/boxes.py — Boîtes de contenu pédagogique (définition, théorème,
propriété, exemple, méthode, remarque, exercice, corrigé, essentiel).

Couleurs importées depuis constants.py (lecture seule, voir CLAUDE.md).

Correctif 3 appliqué partout : les boîtes sont des RoundedRectangle
dimensionnés DIRECTEMENT à la taille du contenu (largeur/hauteur calculées
à partir du Mobject réel), jamais un SurroundingRectangle étiré de façon
anisotrope.
"""

from manim import (
    VGroup,
    RoundedRectangle,
    Rectangle,
    Text,
    Mobject,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    ORIGIN,
    WHITE,
)

from constants import BOX_STYLES

# --- Paramètres de mise en page communs ------------------------------------

DEFAULT_BOX_WIDTH = 11.5          # largeur par défaut d'une boîte (unités Manim)
TITLE_BAR_HEIGHT = 0.55
CONTENT_PADDING = 0.35
CORNER_RADIUS = 0.12
TITLE_FONT_SIZE = 26
CONTENT_FONT_SIZE = 28


def _make_box(
    content: Mobject,
    style_key: str,
    box_width: float = DEFAULT_BOX_WIDTH,
) -> VGroup:
    """
    Construit une boîte à deux bandes : un bandeau de titre coloré (couleur
    "accent") au-dessus d'un corps rempli d'une teinte claire ("fill"),
    contenant le Mobject `content` fourni par l'appelant.

    Le contenu peut être n'importe quel Mobject (Text, MathTex, VGroup
    d'équations, schéma, etc.) — la boîte s'adapte à sa hauteur réelle.
    """
    style = BOX_STYLES[style_key]

    content.set(width=min(content.width, box_width - 2 * CONTENT_PADDING))
    content_height = content.height + 2 * CONTENT_PADDING

    # Corps de la boîte : RoundedRectangle dimensionné directement au
    # contenu (jamais de SurroundingRectangle étiré — correctif 3).
    body = RoundedRectangle(
        width=box_width,
        height=content_height,
        corner_radius=CORNER_RADIUS,
        fill_color=style["fill"],
        fill_opacity=1.0,
        stroke_color=style["accent"],
        stroke_width=2,
    )
    content.move_to(body.get_center())

    # Bandeau de titre : même largeur que le corps, coins arrondis
    # seulement en haut (on superpose un rectangle droit sur la moitié
    # basse pour carrer les coins inférieurs du bandeau contre le corps).
    title_bar = RoundedRectangle(
        width=box_width,
        height=TITLE_BAR_HEIGHT,
        corner_radius=CORNER_RADIUS,
        fill_color=style["accent"],
        fill_opacity=1.0,
        stroke_width=0,
    )
    square_mask = Rectangle(
        width=box_width,
        height=TITLE_BAR_HEIGHT / 2,
        fill_color=style["accent"],
        fill_opacity=1.0,
        stroke_width=0,
    )
    square_mask.align_to(title_bar, DOWN)
    title_bar_group = VGroup(title_bar, square_mask)

    title_text = Text(
        style["title"],
        font_size=TITLE_FONT_SIZE,
        color=style["title_text"],
        weight="BOLD",
    )
    title_text.move_to(title_bar.get_center())
    title_text.align_to(title_bar, LEFT).shift(RIGHT * 0.3)

    title_bar_group.add(title_text)
    title_bar_group.next_to(body, UP, buff=0)
    title_bar_group.align_to(body, LEFT)

    return VGroup(body, content, title_bar_group)


# --- Une fonction par catégorie (API publique pour les scènes) -------------

def definition_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    return _make_box(content, "definition", box_width)


def theorem_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    return _make_box(content, "theoreme", box_width)


def property_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    return _make_box(content, "propriete", box_width)


def example_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    return _make_box(content, "exemple", box_width)


def method_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    return _make_box(content, "methode", box_width)


def warning_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    """Alias historique : REMARQUE fait office de boîte de mise en garde."""
    return _make_box(content, "remarque", box_width)


def exercise_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    return _make_box(content, "exercice", box_width)


def corrige_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    return _make_box(content, "corrige", box_width)


def essentiel_box(content: Mobject, box_width: float = DEFAULT_BOX_WIDTH) -> VGroup:
    return _make_box(content, "essentiel", box_width)


def scene_title(text: str, font_size: int = 40) -> Text:
    """
    Titre de scène générique, hors catégories de couleur.pdf.
    ⚠️ Couleur provisoire (BLANC) en attendant l'extraction de la charte de
    base (fond/titre) depuis la 2ᵉ page des PDF 1ereC/1ereD — voir la note
    en bas de constants.py. À remplacer dès que cette charte est validée.
    """
    return Text(text, font_size=font_size, color=WHITE, weight="BOLD")
