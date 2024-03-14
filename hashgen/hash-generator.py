from flask import Flask
import string
import random
import time

app = Flask(__name__)

def hash_generator(size=10, chars=string.ascii_lowercase + string.digits):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return timestamp + ' ' + ''.join(random.choice(chars) for i in range(size))

@app.get('/current-status')
def show_current():
    with open('data/pongs.txt', 'r') as file:
        pongs = (f'ping / pongs: {file.read()}')
    return hash_generator() + '<br>' + pongs


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7998)
