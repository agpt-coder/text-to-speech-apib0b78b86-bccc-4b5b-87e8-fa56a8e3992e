import logging
from contextlib import asynccontextmanager
from typing import Optional

import project.convert_text_to_speech_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="Text-to-Speech API",
    lifespan=lifespan,
    description="The project involves creating an API endpoint that accepts input in the form of plain text. It then converts this input text into natural-sounding speech audio utilizing a preferred Python package, gTTS (Google Text-to-Speech), which stands out for its straightforward usage, support for multiple languages, and reliance on Google's robust and high-quality text-to-speech engine. Additionally, the generated audio file is to be returned in MP3 format, adhering to the user's stipulation for a widely compatible format that maintains a balance between file size and sound quality. To ensure optimal audio quality and user experience, an audio bitrate of 320 kbps is recommended, providing high-quality sound while managing file size efficiently. The information gathered indicates that the essential components for completing this task include the gTTS package for text-to-speech conversion, output specification in MP3 format, and adherence to a 320 kbps bitrate for the audio file.",
)


@app.post(
    "/text-to-speech/convert",
    response_model=project.convert_text_to_speech_service.TextToSpeechResponse,
)
async def api_post_convert_text_to_speech(
    inputText: str,
    languageCode: str,
    speechRate: Optional[float],
    pauseLength: Optional[int],
) -> project.convert_text_to_speech_service.TextToSpeechResponse | Response:
    """
    Converts submitted text into speech, returning an MP3 file.
    """
    try:
        res = project.convert_text_to_speech_service.convert_text_to_speech(
            inputText, languageCode, speechRate, pauseLength
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
