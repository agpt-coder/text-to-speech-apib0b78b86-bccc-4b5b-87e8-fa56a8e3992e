---
date: 2024-04-16T16:44:19.030398
author: AutoGPT <info@agpt.co>
---

# Text-to-Speech API

The project involves creating an API endpoint that accepts input in the form of plain text. It then converts this input text into natural-sounding speech audio utilizing a preferred Python package, gTTS (Google Text-to-Speech), which stands out for its straightforward usage, support for multiple languages, and reliance on Google's robust and high-quality text-to-speech engine. Additionally, the generated audio file is to be returned in MP3 format, adhering to the user's stipulation for a widely compatible format that maintains a balance between file size and sound quality. To ensure optimal audio quality and user experience, an audio bitrate of 320 kbps is recommended, providing high-quality sound while managing file size efficiently. The information gathered indicates that the essential components for completing this task include the gTTS package for text-to-speech conversion, output specification in MP3 format, and adherence to a 320 kbps bitrate for the audio file.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'Text-to-Speech API'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
