from flask import Flask
from os import environ
import string
import random
import requests
import time

app = Flask(__name__)
message = environ.get('MESSAGE', 'No MESSAGE env.var found')

def hash_generator(size=10, chars=string.ascii_lowercase + string.digits):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return timestamp + ' ' + ''.join(random.choice(chars) for i in range(size))

@app.get('/current-status')
async def show_current():
    pongs = requests.get("http://pingpong-svc/pingpong")
    return message + '<br>' + hash_generator() + '<br>' + pongs.text


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7998)
