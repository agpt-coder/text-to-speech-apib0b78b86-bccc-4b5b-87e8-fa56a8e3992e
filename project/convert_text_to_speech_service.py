import tempfile
from typing import Optional

from gtts import gTTS
from pydantic import BaseModel


class TextToSpeechResponse(BaseModel):
    """
    Response model containing the link to the generated MP3 file.
    """

    success: bool
    errorMessage: Optional[str] = None
    audioFileLink: Optional[str] = None


def convert_text_to_speech(
    inputText: str,
    languageCode: str,
    speechRate: Optional[float],
    pauseLength: Optional[int],
) -> TextToSpeechResponse:
    """
    Converts submitted text into speech, returning an MP3 file.

    Args:
        inputText (str): The text to be converted into speech.
        languageCode (str): The language code for text-to-speech conversion.
        speechRate (Optional[float]): Optional. Custom speech rate for the conversion.
        pauseLength (Optional[int]): Optional. Custom pause length in milliseconds between sentences or clauses.

    Returns:
        TextToSpeechResponse: Response model containing the link to the generated MP3 file.
    """
    try:
        slow = False if speechRate is None else speechRate < 0.5
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tts = gTTS(text=inputText, lang=languageCode, slow=slow)
            tts.save(tmpfile.name)
            tmpfile_path = tmpfile.name
            audioFileLink = (
                f"File saved at {tmpfile_path} (this should be an uploaded file URL)"
            )
        return TextToSpeechResponse(success=True, audioFileLink=audioFileLink)
    except Exception as e:
        errorMessage = str(e)
        return TextToSpeechResponse(success=False, errorMessage=errorMessage)
