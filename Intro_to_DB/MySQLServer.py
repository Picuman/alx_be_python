import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("Database 'alx_book_store' already exists.")
        else:
            print(f"Failed creating database: {err}")

def main():
    try:
        # Connect to the MySQL server
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost'
        )
        cursor = cnx.cursor()
        create_database(cursor)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Ensure the connection is closed
        if cnx.is_connected():
            cursor.close()
            cnx.close()

if __name__ == "__main__":
    main()
