# STT long transcription
This is a gradio app design to facilitate the transcription of long files. It is advised to use the wav format but we currently support .mp3, .webm and .wmv

# Installation process
## Requirements
```
RAM         : +10GB
Storage     : +15GB
NVIDIA GPU  : Prefered but not required
Docker      : Advised
```
## Installation
1. Clone the repository
```
   $ git clone https://github.com/MBAZA-NLP/stt-long-transcription.git
   $ cd stt-long
```
2. Install [Docker](https://docs.docker.com/get-docker/) on your machine
3. Deploy the container
```
docker compose build
docker compose up -d
```
4. open localhost:7860 and upload the audio


# Author
Developed by [Digital Umuganda](https://digitalumuganda.com/)

# Request support
You can raise an issue on this repository
