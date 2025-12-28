from flask import Flask, render_template, request, redirect
import mysql.connector
import hashlib
import base64
import re

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="url_shortener"
)

cursor = db.cursor()

def generate_short_code(url, length=6):
    sha256_hash = hashlib.sha256(url.encode()).digest()
    base64_encoded = base64.urlsafe_b64encode(sha256_hash).decode()
    base64_clean = re.sub(r'[^a-zA-Z0-9]', '', base64_encoded)
    return base64_clean[:length]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form["url"]
        short_code = generate_short_code(original_url)

        cursor.execute(
            "SELECT short_code FROM urls WHERE original_url=%s",
            (original_url,)
        )
        existing = cursor.fetchone()

        if not existing:
            cursor.execute(
                "INSERT INTO urls (original_url, short_code) VALUES (%s, %s)",
                (original_url, short_code)
            )
            db.commit()
        else:
            short_code = existing[0]

        short_url = request.host_url + short_code
        return render_template("result.html", short_url=short_url)

    return render_template("index.html")

@app.route("/<short_code>")
def redirect_url(short_code):
    cursor.execute(
        "SELECT original_url FROM urls WHERE short_code=%s",
        (short_code,)
    )
    result = cursor.fetchone()

    if result:
        return redirect(result[0])

    return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)