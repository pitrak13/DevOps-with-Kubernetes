FROM python:alpine3.19

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
#    adduser --disabled-password --gecos "" --no-create-home appuser && \
#    mkdir data && \
#    chown -R appuser /usr/src/app

#USER appuser

CMD ["python3", "timestamp.py"]


