from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "bigus digus!"

count = -1
@app.get("/pingpong")
def get_pongs():
    global count
    count+=1
    return (f"ping / pongs: {count}")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7999)
