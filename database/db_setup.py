import sqlite3

def get_db_connection():
    """Establishes and returns a database connection."""
    conn = sqlite3.connect('access_control.db')
    conn.row_factory = sqlite3.Row  # Access rows like dictionaries
    return conn

def setup_database():
    """Creates tables for users and files if they don't already exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        security_level INTEGER NOT NULL,
        compartments TEXT NOT NULL
    )
    """)

    # Create files table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        filename TEXT PRIMARY KEY,
        security_level INTEGER NOT NULL,
        compartments TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Database initialized.")

if __name__ == "__main__":
    setup_database()
