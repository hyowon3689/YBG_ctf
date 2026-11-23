from flask import Flask, request, render_template
import sqlite3
from pathlib import Path
import os

app = Flask(__name__)

# Always use the database located next to app.py.
# This prevents the 'ctf.db not found / wrong database' problem
# when Flask is started from another working directory.
BASE_DIR = Path(__file__).resolve().parent
DB = BASE_DIR / "ctf.db"


def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        conn = db()

        # Safe: parameterized query.
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password),
        ).fetchone()

        conn.close()

        if user:
            message = "Login success!"
        else:
            message = "Login failed."

    return render_template("index.html", message=message, results=None)


@app.route("/search")
def search():
    q = request.args.get("q", "")

    conn = db()

    # INTENTIONALLY VULNERABLE FOR THE CTF.
    # User input is directly inserted into the SQL query.
    query = f"""
        SELECT title, content
        FROM posts
        WHERE title LIKE '%{q}%'
    """

    try:
        results = conn.execute(query).fetchall()
    except sqlite3.Error:
        # Do not reveal SQL errors to the player.
        results = []

    conn.close()

    return render_template(
        "index.html",
        message="",
        results=results,
        query=q,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
