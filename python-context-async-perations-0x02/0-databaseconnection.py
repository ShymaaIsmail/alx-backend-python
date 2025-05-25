import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        # Establish the database connection and return the cursor
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit changes if no exception, otherwise rollback
        if exc_type is None:
            self.connection.commit()
        else:
            self.connection.rollback()
            print(f"An error occurred: {exc_value}")
        # Close the cursor and connection
        self.cursor.close()
        self.connection.close()

# Usage example:
if __name__ == "__main__":
    # First, ensure the 'users' table exists and has some data (for demonstration)
    with DatabaseConnection("example.db") as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie')")

    # Use the custom context manager to query the database
    with DatabaseConnection("example.db") as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
