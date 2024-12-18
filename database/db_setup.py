import sqlite3
import datetime

def get_db_connection():
    """Establishes and returns a database connection."""
    conn = sqlite3.connect('access_control.db')
    conn.row_factory = sqlite3.Row  # Access rows like dictionaries
    return conn

def setup_database():
    """Creates tables for users, files, and test results if they don't already exist."""
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

    # Create test_results table with timestamp
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        file TEXT NOT NULL,
        model TEXT NOT NULL,
        action TEXT NOT NULL,
        allowed BOOLEAN NOT NULL,
        timestamp TEXT NOT NULL  -- New timestamp column
    )
    """)

    conn.commit()
    conn.close()
    print("Database initialized.")

def log_test_result(user, file, model, action, allowed):
    """Logs a test result into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO test_results (user, file, model, action, allowed, timestamp)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (user, file, model, action, allowed, timestamp))

    conn.commit()
    conn.close()

def fetch_test_results():
    """Fetches and displays all test results from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT user, file, model, action, allowed, timestamp
    FROM test_results
    ORDER BY id ASC
    """)
    results = cursor.fetchall()

    conn.close()
    return results

if __name__ == "__main__":
    setup_database()