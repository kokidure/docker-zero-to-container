from flask import Flask, jsonify
import psycopg2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "demo_db"),
        user=os.getenv("DB_USER", "demo_username"),
        password=os.getenv("DB_PASS", "demo_password")
    )
    return conn

@app.route("/")
def home():
    return jsonify({"message": "Docker funcionando desde Flask!"})

@app.route("/db")
def db_time():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"db_time": str(result[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
