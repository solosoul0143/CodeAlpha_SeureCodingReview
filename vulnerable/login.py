
"""Secure local user login demonstration."""

import sqlite3
import bcrypt

DB_NAME = "secure.db"


def create_database():
    """Create the users table and add a demo account."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password_hash BLOB NOT NULL
            )
        """)

        row = conn.execute(
            "SELECT username FROM users WHERE username = ?",
            ("admin",)
        ).fetchone()

        if row is None:
            password_hash = bcrypt.hashpw(
                b"ChangeThisDemoPassword!",
                bcrypt.gensalt()
            )
            conn.execute(
                "INSERT INTO users (username, password_hash) "
                "VALUES (?, ?)",
                ("admin", password_hash)
            )


def login(username, password):
    """Authenticate a user using a parameterized query."""
    if not username or len(username) > 64:
        print("Invalid username or password")
        return False

    if not password or len(password) > 72:
        print("Invalid username or password")
        return False

    with sqlite3.connect(DB_NAME) as conn:
        row = conn.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            (username,)
        ).fetchone()

    if row is None:
        print("Invalid username or password")
        return False

    try:
        valid = bcrypt.checkpw(
            password.encode("utf-8"),
            row[0]
        )
    except (ValueError, TypeError):
        valid = False

    if valid:
        print("Login successful")
        return True

    print("Invalid username or password")
    return False


if __name__ == "__main__":
    create_database()
    entered_username = input("Username: ")
    entered_password = input("Password: ")
    login(entered_username, entered_password)
