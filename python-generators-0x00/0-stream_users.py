#!/usr/bin/python3
def stream_users():
    """
    Stream users from the database.
    """
    import mysql.connector
    import csv

    # Connect to the database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='ALX_prodev'
    )

    cursor = connection.cursor()

    # Execute a query to select all users
    cursor.execute("SELECT * FROM user_data")

    # Fetch and print each row
    for row in cursor:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()
