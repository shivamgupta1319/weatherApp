import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def config():
        connection = psycopg2.connect(user = "weather",
                                    password = "shivam13",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "weatherdb")
        return connection



@app.route('/')
def index():
    conn = config()
    cur = conn.cursor()
    cur.execute('SELECT * FROM weather;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.js', data=data)