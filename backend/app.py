from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Backend ажиллаж байна</h1>
    <p>Flask backend Docker Compose дээр ажиллаж байна.</p>
    """

@app.route("/api")
def api():
    return {
        "message": "Backend API амжилттай ажиллаж байна",
        "db_host": os.getenv("DB_HOST"),
        "db_name": os.getenv("DB_NAME"),
        "db_user": os.getenv("DB_USER")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)