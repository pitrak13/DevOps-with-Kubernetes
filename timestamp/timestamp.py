import time

def timestamp():
    while True:
        with open("data/status.txt", "w") as file:
            current = time.strftime('%Y-%m-%d %H:%M:%S')
            file.write(current)
            print(f"Timestamp <{current}> generated and saved to {file.name}")
        time.sleep(5)

if __name__ == '__main__':
    timestamp()
