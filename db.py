import mysql.connector
import os

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get("MYSQLHOST"),
        user=os.environ.get("MYSQLUSER"),
        password=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE"),
        port=int(os.environ.get("MYSQLPORT", 3306))
    )
    return connection

# Run only once to create the users table
def initialize_database():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Create users table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
        """)

        conn.commit()
        print("✅ 'users' table created successfully.")
    except mysql.connector.Error as err:
        print(f"❌ Database initialization error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the initializer when this file is imported
