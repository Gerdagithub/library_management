import psycopg2
from psycopg2 import sql
import os

from logging_db import logger

def create_admin_table(conn, cur):
    if conn is None:
        logger.error("Connection is not established")
        return 
    
    if cur is None:
        cur = conn.cursor()
    
    try:
        create_table_command = """
        CREATE TABLE IF NOT EXISTS Administrator (
            username VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        );
        """
        cur.execute(create_table_command)
        conn.commit()
        
        logger.info("Administrator table created successfully.\n")
    except psycopg2.DatabaseError as e:
        logger.error(f"An error occurred: {e}\n")
    
# -- Administrator Table
# CREATE TABLE Administrator (
#     username VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY,
#     password_hash VARCHAR(255) NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     last_login TIMESTAMP
# );


def create_reader_table(conn, cur):
    if conn is None:
        logger.error("Connection is not established")
        return 
    
    if cur is None:
        cur = conn.cursor()
    
    try:
        create_table_command = """
        CREATE TABLE IF NOT EXISTS Reader (
            reader_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100),
            phone_number VARCHAR(15)
        );
        """
        cur.execute(create_table_command)
        conn.commit()
        
        logger.info("Reader table created successfully.\n")
    except psycopg2.DatabaseError as e:
        logger.error(f"An error occurred: {e}\n")

# -- Readers Table
# CREATE TABLE Reader (
#     reader_id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100),
#     phone_number VARCHAR(15)
# );

def create_book_table(conn, cur):
    if conn is None:
        logger.error("Connection is not established")
        return 
    
    if cur is None:
        cur = conn.cursor()
    
    try:
        create_table_command = """
        CREATE TABLE IF NOT EXISTS Book (
            isbn VARCHAR(13) PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            publisher VARCHAR(255),
            publication_date DATE,
            genre VARCHAR(100),
            copies_in_stock INT DEFAULT 0 -- Number of copies available in the storage
        );
        """
        cur.execute(create_table_command)
        conn.commit()
        
        logger.info("Book table created successfully.\n")
    except psycopg2.DatabaseError as e:
        logger.error(f"An error occurred: {e}\n")

# -- Books Table
# CREATE TABLE Book (
#     isbn VARCHAR(13) PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     author VARCHAR(255) NOT NULL,
#     publisher VARCHAR(255),
#     publication_date DATE,
#     genre VARCHAR(100),
#     # availability_status BOOLEAN DEFAULT TRUE
#     copies_in_stock INT DEFAULT 0 -- Number of copies available in the storage
# );


def create_loan_table(conn, cur):
    if conn is None:
        logger.error("Connection is not established")
        return 
    
    if cur is None:
        cur = conn.cursor()
    
    try:
        create_table_command = """
        CREATE TABLE IF NOT EXISTS Loan (
            loan_id SERIAL PRIMARY KEY,
            isbn VARCHAR(13) REFERENCES Book(isbn),
            reader_id INTEGER REFERENCES Reader(reader_id),
            loan_date DATE DEFAULT CURRENT_DATE,
            due_date DATE,
            return_date DATE
        );
        """
        cur.execute(create_table_command)
        conn.commit()
        
        logger.info("Loan table created successfully.\n")
    except psycopg2.DatabaseError as e:
        logger.error(f"An error occurred: {e}\n")

# -- Loans Table
# CREATE TABLE Loan (
#     loan_id SERIAL PRIMARY KEY,
#     isbn VARCHAR(13) REFERENCES Book(isbn),
#     reader_id INTEGER REFERENCES Reader(reader_id),
#     loan_date DATE DEFAULT CURRENT_DATE,
#     due_date DATE,
#     return_date DATE
# );

