FROM python:3-alpine

ENV DEVELOPER="Andres Bolaños"

ADD / home

WORKDIR /home

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "bio.py"]