#!/usr/bin/python3

def stream_users_in_batches(batch_size):
    """
    Stream users from the database in batches.
    """
    
        



def batch_processing(batch_size):
    """
    Process users in batches.
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

    while True:
        # Fetch a batch of rows
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        for row in rows:
            print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()        
