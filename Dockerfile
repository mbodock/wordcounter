FROM python:3.12.3-bookworm

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger

COPY . . 

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ]
