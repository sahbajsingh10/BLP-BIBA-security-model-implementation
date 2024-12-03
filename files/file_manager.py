import sqlite3
from database.db_setup import get_db_connection

class FileManager:
    def __init__(self):
        pass  # No in-memory storage needed

    def create_file(self, filename, security_level, compartments):
        """Adds a new file to the database."""
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
            INSERT INTO files (filename, security_level, compartments)
            VALUES (?, ?, ?)
            """, (filename, security_level, ','.join(compartments)))
            conn.commit()
            print(f"File {filename} created successfully.")
        except sqlite3.IntegrityError:
            print(f"File {filename} already exists.")
        finally:
            conn.close()

    def get_file(self, filename):
        """Fetches file information from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM files WHERE filename = ?", (filename,))
        file = cursor.fetchone()
        conn.close()

        if file:
            return {
                "filename": file["filename"],
                "security_level": file["security_level"],
                "compartments": file["compartments"].split(',')
            }
        else:
            print(f"File {filename} not found.")
            return None
