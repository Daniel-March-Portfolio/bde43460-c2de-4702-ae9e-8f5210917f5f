FROM python:3.12-alpine

COPY requirements/common.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY requirements/testing.txt testing_requirements.txt
COPY app app
WORKDIR /app
