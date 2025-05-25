import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None, db_name="example.db"):
        self.query = query
        self.params = params if params else ()
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        # Establish connection and cursor
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Execute the query
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()

        # Return the result
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Clean up
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        return False  # Propagate any exception

# Example usage
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(query, params) as result:
    for row in result:
        print(row)
