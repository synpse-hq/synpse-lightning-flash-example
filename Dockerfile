FROM python:3.8.5-slim-buster

WORKDIR /server

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "image_classifier.py"]
