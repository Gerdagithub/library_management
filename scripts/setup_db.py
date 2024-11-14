from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql
import os

from logging_db import logger

from create_db import create_db   
from create_db_entities import \
    create_admin_table, create_reader_table, \
    create_book_table, create_loan_table
    
load_dotenv()

status_msg = ""
conn = None

try:
    create_db(os.getenv('DB_NAME'))
    
    # Reconnect to the new database to grant privileges
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    # Create a new cursor for this connection
    cur = conn.cursor()

    # Grant privileges to the user
    cur.execute(sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(
        sql.Identifier(os.getenv('DB_NAME')), sql.Identifier(os.getenv('DB_USER'))))

    conn.commit()
    logger.info(f"Database {os.getenv('DB_NAME')} created and privileges granted to user '{os.getenv('DB_USER')}'.\n")

    
    # create_admin_table(conn, cur)
    # create_reader_table(conn, cur)
    # create_book_table(conn, cur)
    # create_loan_table(conn, cur)
    
    cur.close()
    conn.close()
except Exception as e:
    logger.error(f"An error occurred: {e}\n")
finally:
    if conn is not None:
        conn.close()