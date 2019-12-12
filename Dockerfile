FROM ubuntu:latest

FROM python:3.6

COPY . /app

RUN apt-get update -y

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
