"""
tts_service.py — Service TTS maison pour manim-voiceover, basé sur
Microsoft Edge TTS (gratuit). Voix par défaut : fr-FR-HenriNeural
(masculine, française), voir CLAUDE.md.
"""

import asyncio
from pathlib import Path

import edge_tts

from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import PathLike, SpeechService, path_to_string


class EdgeTTSService(SpeechService):
    """SpeechService pour Microsoft Edge TTS (`edge-tts`)."""

    def __init__(self, voice: str = "fr-FR-HenriNeural", **kwargs: object) -> None:
        self.voice = voice
        super().__init__(**kwargs)

    def generate_from_text(
        self,
        text: str,
        cache_dir: PathLike | None = None,
        path: PathLike | None = None,
        **kwargs: object,
    ) -> dict:
        if cache_dir is None:
            cache_dir = self.cache_dir

        input_text = remove_bookmarks(text)
        input_data = {"input_text": input_text, "service": "edge-tts", "voice": self.voice}

        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_audio_basename(input_data) + ".mp3"
        else:
            audio_path = path_to_string(path)

        full_path = str(Path(cache_dir) / audio_path)
        communicate = edge_tts.Communicate(input_text, voice=self.voice)
        asyncio.run(communicate.save(full_path))

        return {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }
