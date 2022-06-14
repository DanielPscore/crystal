FROM orgoro/dlib-opencv-python:latest
COPY .  /crystal
WORKDIR /crystal
CMD mkdir Data
RUN apt-get upgrade && apt-get update
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python test.py