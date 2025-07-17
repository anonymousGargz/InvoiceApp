import sqlite3
connection = sqlite3.connect("invoicingApp.db")
cursor= connection.cursor()
def create ():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS rows (
    numbers INTEGER PRIMARY KEY AUTOINCREMENT
    );
    '''

    # Execute the SQL command
    cursor.execute(create_table_query)
    connection.commit()
    
def addRow():
    addQuery = '''INSERT INTO rows DEFAULT VALUES'''
    cursor.execute(addQuery)
    connection.commit()


def getLastRow():
    return cursor.lastrowid

