import mysql.connector
from mysql.connector import Error
import csv
import uuid

# Database connection
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='yourpassword'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Create database
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        connection.commit()
    except Error as e:
        print(f"Error creating database: {e}")

# Connect to ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='yourpassword',
            database='ALX_prodev'
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None

# Create table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3,0) NOT NULL,
                INDEX(email)
            )
        ''')
        connection.commit()
    except Error as e:
        print(f"Error creating table: {e}")

# Insert data
def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        query = '''
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
        '''
        cursor.execute("SELECT email FROM user_data WHERE email = %s", (data[1],))
        existing = cursor.fetchone()
        if not existing:
            cursor.execute(query, (str(uuid.uuid4()), data[0], data[1], data[2]))
            connection.commit()
    except Error as e:
        print(f"Error inserting data: {e}")

# Populate database from CSV
def populate_from_csv(csv_file):
    connection = connect_to_prodev()
    if connection:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                insert_data(connection, row)
        connection.close()

# Generator to stream user ages
def stream_user_ages():
    connection = connect_to_prodev()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")
        for (age,) in cursor:
            yield float(age)
        connection.close()

# Calculate average age
def calculate_average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    average_age = total_age / count if count > 0 else 0
    print(f"Average age of users: {average_age}")

if __name__ == "__main__":
    main_connection = connect_db()
    if main_connection:
        create_database(main_connection)
        main_connection.close()

    prodev_connection = connect_to_prodev()
    if prodev_connection:
        create_table(prodev_connection)
        populate_from_csv('user_data.csv')
        calculate_average_age()
        prodev_connection.close()
