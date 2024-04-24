FROM python:alpine

RUN pip install nltk

WORKDIR /wadah

COPY . /wadah
CMD ["python", "counter.py"]