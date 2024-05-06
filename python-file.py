import os
import psycopg2
from psycopg2 import Error

def connect_to_postgresql(host, database, user, password):
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        
        # Create a cursor object to execute queries
        cursor = connection.cursor()
        
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("Connected to PostgreSQL version:", db_version[0])
        
        return connection, cursor
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None, None

def show_all_tables(cursor):
    try:
        # Execute a query to list all tables in the current database
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        
        # Fetch all rows from the result set
        rows = cursor.fetchall()
        
        # Print each table name
        print("Tables in the database:")
        for row in rows:
            print(row[0])
    
    except (Exception, Error) as error:
        print("Error while fetching table names from PostgreSQL:", error)

def main():
    # print(f"Current date and time: {datetime.datetime.now()}")
    conn, cursor = connect_to_postgresql(os.getenv('PG_URL'),os.getenv('PG_DB'),os.getenv('PG_USER'), os.getenv('PG_PASSWORD'))
    show_all_tables(cursor)
    

if __name__ == "__main__":
    main()

    # print(os.getenv('PG_USER'))
    # print(os.getenv('PG_DB'))
