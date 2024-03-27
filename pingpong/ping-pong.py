import psycopg2
from os import environ
from flask import Flask

app = Flask(__name__)

def db_init():
    try:
        conn = psycopg2.connect(host="postgres-svc", user="postgres", dbname="postgres", 
                                password=environ.get("POSTGRES_PASSWORD"), port=5432)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE pong (count INT NOT NULL DEFAULT 0);
                    INSERT INTO pong DEFAULT VALUES""")
    except psycopg2.errors.DuplicateTable:
        print("pong counter already exists")
    except:
        print("Connection error")
    conn.commit()
    cur.close()
    return conn

@app.get("/pong")
def get_pongs():
    cur = conn.cursor()
    cur.execute("""SELECT count FROM pong""")
    pongs = cur.fetchone()
    cur.execute("""UPDATE pong
                    SET count = count + 1""")
    conn.commit()
    cur.close()
    return "pong " + str(pongs[0])

if __name__ == "__main__":
    conn = db_init()
    app.run(host="0.0.0.0", port=7999)
