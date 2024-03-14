FROM python:alpine3.19

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    mkdir data

CMD ["python3", "ping-pong.py"]


