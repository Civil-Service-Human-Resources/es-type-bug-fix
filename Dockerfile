FROM python:3.10.14-slim-bullseye
RUN pip install elasticsearch
COPY . /client
WORKDIR /client