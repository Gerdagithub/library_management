from dotenv import load_dotenv
import psycopg2
import sys
import os
from psycopg2 import sql
from logging_db import logger

load_dotenv()
    
def create_db(db_name: str):
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DEFAULT_DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        # Check if the database exists
        cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [db_name])
        exists = cur.fetchone()

        if exists:
            logger.info(f"Database {db_name} already exists. Deleting it.\n")
            cur.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(db_name)))
            conn.commit()

        # Ensure the database was deleted by checking it no longer exists
        cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [db_name])
        if cur.fetchone():
            raise Exception("Failed to delete existing database.\n")

        # Create the database
        logger.info(f"Creating database {db_name}.\n")
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        conn.commit()  # Commit might be redundant here due to autocommit but ensures finality in some setups

        conn.close()
        logger.info(f"Database {db_name} created successfully.\n")

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}\n")