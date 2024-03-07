from flask import Flask
import string
import random

app = Flask(__name__)

def hash_generator(size=16, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    hash = ''.join(random.choice(chars) for i in range(size))
    return hash[6:14]

if __name__ == '__main__':
#	app.run(host='0.0.0.0', port=7999)
	print(hash_generator())
