FROM python:3.9.12-slim

ADD app /app

RUN pip install -r /app/requirements.txt

WORKDIR /app
CMD [ "python", "/app/main.py"]

EXPOSE 8080/tcp