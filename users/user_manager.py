import sqlite3
from database.db_setup import get_db_connection

class UserManager:
    def __init__(self):
        pass  # No in-memory storage needed anymore

    def add_user(self, username, security_level, compartments):
        """Adds a new user to the database."""
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
            INSERT INTO users (username, security_level, compartments)
            VALUES (?, ?, ?)
            """, (username, security_level, ','.join(compartments)))
            conn.commit()
            print(f"User {username} added successfully.")
        except sqlite3.IntegrityError:
            print(f"User {username} already exists.")
        finally:
            conn.close()

    def get_user(self, username):
        """Fetches user information from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            return {
                "username": user["username"],
                "security_level": user["security_level"],
                "compartments": user["compartments"].split(',')
            }
        else:
            print(f"User {username} not found.")
            return None
