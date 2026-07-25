"""
shapes/base_scene.py — Scène de base commune à toutes les scènes du cours.

Fournit `NotionScene`, dont chaque scène du projet doit hériter (voir
CLAUDE.md, "Conventions de code") : accès à `self.voiceover(...)`
(manim-voiceover + EdgeTTSService), fond de la charte, et un `wait()`
sécurisé (correctif 6 : une durée <= 0 ne fait plus planter le rendu).

⚠️ Couleur de fond provisoire (BLACK, cohérente avec le blanc provisoire de
`scene_title()` dans shapes/boxes.py) en attendant l'extraction de la
charte de base depuis la 2ᵉ page des PDF 1ereC/1ereD — voir la note en bas
de constants.py.
"""

from manim import BLACK
from manim_voiceover import VoiceoverScene

from tts_service import EdgeTTSService


class NotionScene(VoiceoverScene):
    """Scène de base : fond de la charte + service TTS déjà configurés."""

    def setup(self) -> None:
        super().setup()
        self.camera.background_color = BLACK
        self.set_speech_service(EdgeTTSService())

    def wait(self, duration=1, stop_condition=None, frozen_frame=None):
        # Correctif 6 : une durée <= 0 (audio déjà entièrement consommé par
        # les animations jouées) fait planter Scene.wait() ; on la remplace
        # par une frame minimale au lieu de laisser l'exception remonter.
        if duration is None or duration <= 0:
            duration = 1 / self.camera.frame_rate
        return super().wait(duration, stop_condition=stop_condition, frozen_frame=frozen_frame)
