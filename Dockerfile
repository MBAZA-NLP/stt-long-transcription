FROM nvcr.io/nvidia/nemo:23.06
RUN apt-get clean all
RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y libsndfile1 espeak-ng git git-lfs ffmpeg
RUN pip install --upgrade pip

WORKDIR /code/stt-api
COPY requirements.txt /code/stt-api/ 
RUN pip install -r requirements.txt
COPY . /code/stt-api
CMD ["gradio","app.py"]