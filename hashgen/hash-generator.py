import string
import random
import time

def hash_generator(size=8, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    hash = ''.join(random.choice(chars) for i in range(size))
    return hash

if __name__ == '__main__':
    while True:
        with open("data/status.txt", "r") as file:
            print(f"{file.read()}  {hash_generator()}")
        time.sleep(5)
