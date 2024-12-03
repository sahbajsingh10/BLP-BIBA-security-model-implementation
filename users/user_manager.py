import sqlite3
from database.db_setup import get_db_connection  # Import database connection function

class UserManager:
    def __init__(self):
        pass  # Placeholder for initialization, no setup required

    def add_user(self, username, security_level, compartments):
        """Adds a new user to the database."""
        conn = get_db_connection()  # Establish database connection
        cursor = conn.cursor()

        try:
            # Insert new user into the users table
            cursor.execute("""
            INSERT INTO users (username, security_level, compartments)
            VALUES (?, ?, ?)
            """, (username, security_level, ','.join(compartments)))
            conn.commit()  # Save changes to the database
            print(f"User {username} added successfully.")
        except sqlite3.IntegrityError:
            # Handle case where user already exists
            print(f"User {username} already exists.")
        finally:
            conn.close()  # Close the database connection

    def get_user(self, username):
        """Fetches user information from the database."""
        conn = get_db_connection()  # Establish database connection
        cursor = conn.cursor()

        # Retrieve user details by username
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()  # Close the database connection

        if user:
            # Return user details as a dictionary
            return {
                "username": user["username"],
                "security_level": user["security_level"],
                "compartments": user["compartments"].split(',')  # Convert to list
            }
        else:
            # Notify if user is not found
            print(f"User {username} not found.")
            return None