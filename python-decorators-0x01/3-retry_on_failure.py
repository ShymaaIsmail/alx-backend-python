import time
import sqlite3 
import functools

#### paste your with_db_decorator here
def with_db_connection(func):
    """Decorator to manage database connection for functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('db.users')
        try:
            print(f"Connecting to database at: {conn.execute('PRAGMA database_list').fetchall()}")
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

def retry_on_failure(retries=3, delay=1):
    """Decorator to retry a function on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay)
            raise Exception("All attempts failed")
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usesrs")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
