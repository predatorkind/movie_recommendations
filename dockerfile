# syntax=docker/dockerfile:1

FROM python:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_md
COPY . .
CMD python semantic.py