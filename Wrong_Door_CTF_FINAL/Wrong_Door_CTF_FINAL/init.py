import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB = BASE_DIR / "ctf.db"

conn = sqlite3.connect(DB)

conn.executescript("""
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS secret;

CREATE TABLE users (
    id INTEGER,
    username TEXT,
    password TEXT
);

CREATE TABLE posts (
    id INTEGER,
    title TEXT,
    content TEXT
);

CREATE TABLE secret (
    flag TEXT
);

INSERT INTO users VALUES
(1, 'guest', 'guest');

INSERT INTO posts VALUES
(1, 'Welcome', 'Welcome to our website!');
INSERT INTO posts VALUES
(2, 'Notice', 'Nothing interesting here.');

INSERT INTO secret VALUES
('FLAG{wrong_door}');
""")

conn.commit()
conn.close()

print(f"Database created: {DB}")
