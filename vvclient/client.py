# vvclient - client.py

from typing import Optional

from .http import HTTPClient
from .audio_query import AudioQuery


class Client:
    """VOICEVOX Engine client
    
    Parameters
    ----------
    base_uri : str
        Base URI of the VOICEVOX Engine"""
    def __init__(self, base_uri: str = "http://localhost:50021") -> None:
        self.http = HTTPClient(base_uri)

    async def close(self) -> None:
        await self.http.close()

    async def create_audio_query(
        self, text: str, speaker: int, *, core_version: Optional[str] = None
    ) -> AudioQuery:
        """
        Create audio query

        Parameters
        ----------
        text: str
            Voice text
        speaker: int
            speaker type
        core_version: Optional[str]
            voicevox_core version

        Returns
        -------
        audio_query: AudioQuery
            Audio query
        """
        params = {"text": text, "speaker": speaker}
        if core_version:
            params["core_version"] = core_version
        await self.http.create_audio_query(params)
