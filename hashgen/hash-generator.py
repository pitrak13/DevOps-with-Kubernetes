from flask import Flask
import string
import random
import requests
import time

app = Flask(__name__)

def hash_generator(size=10, chars=string.ascii_lowercase + string.digits):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return timestamp + ' ' + ''.join(random.choice(chars) for i in range(size))

@app.get('/current-status')
async def show_current():
    pongs = requests.get("http://pingpong-svc/pingpong")
    return hash_generator() + '<br>' + pongs.text


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7998)
