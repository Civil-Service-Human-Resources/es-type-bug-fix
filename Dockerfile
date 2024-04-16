FROM python:3.10.14-slim-bullseye
RUN pip install elasticsearch
COPY ./app /app
RUN echo "alias es-client='python main.py'" >> ~/.bashrc
WORKDIR /app