import sqlite3
import os
from modules.logger import Customlogger, Logger_type
from modules.variables import db_name , table_name

# Get database connection
def get_connection():
    try:
        conn = sqlite3.connect(db_name)
        return conn, conn.cursor()
    except sqlite3.Error as e:
        Customlogger(True, f"[-] Error connecting to the database: {e}", Logger_type.ERROR)
        raise

def create_db():
    try:
        if os.path.exists(db_name):
            Customlogger(True, f"[+] Database {db_name} already exists.", Logger_type.INFO)
            return

        conn, cursor = get_connection()

        # Create a table if not exists
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                title TEXT,
                link TEXT UNIQUE,
                authors TEXT,
                programs TEXT,
                bugs TEXT,
                bounty TEXT,
                publication_date TEXT,
                added_date TEXT
            )
        ''')

        conn.commit()
        conn.close()
        Customlogger(True, f"[+] Database {db_name} created.", Logger_type.INFO)
    except sqlite3.Error as e:
        Customlogger(True, f"Error creating the database: {e}", Logger_type.ERROR)
        raise


def check_existence_in_db(link):
    try:
        conn, cursor = get_connection()
        
        # Check if a record with the given link exists
        cursor.execute(f'SELECT EXISTS(SELECT 1 FROM {table_name} WHERE link = ?)', (link,))
        result = cursor.fetchone()[0]

        return bool(result)

    except sqlite3.Error as e:
        Customlogger(True, f"[-] Error checking existence in the database: {e}", Logger_type.ERROR)
        return False

    finally:
        conn.close()

def add_to_db(writeups):
    try:
        conn, cursor = get_connection()
        
        # Insert writeups into the table
        for writeup in writeups:
            cursor.execute(f'''
                INSERT INTO {table_name} 
                (title, link, authors, programs, bugs, bounty, publication_date, added_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                writeup['Links'][0]['Title'],
                writeup['Links'][0]['Link'],
                ', '.join(writeup['Authors']),
                ', '.join(writeup['Programs']),
                ', '.join(writeup['Bugs']),
                writeup['Bounty'],
                writeup['PublicationDate'],
                writeup['AddedDate']
            ))

        # Commit changes
        conn.commit()

    except sqlite3.Error as e:
        Customlogger(True, f"[-] Error adding writeups to the database: {e}", Logger_type.ERROR)
        
    finally:
        conn.close()