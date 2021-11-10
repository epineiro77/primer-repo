FROM python:3.8.10-slim-buster

WORKDIR /example-pythons

RUN cd/app/project

COPY . .

RUN pip3 install -r requierements.txt

CMD python3 app.py