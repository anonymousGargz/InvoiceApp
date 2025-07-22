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
    addRow= '''SELECT MAX(numbers) FROM rows'''
    cursor.execute(addRow)
    results = cursor.fetchone()
    return results[0]


def delete():
    delete = '''DROP TABLE IF EXISTS rows'''
    cursor.execute(delete)
    connection.commit() ## MUTIPLE TEMPLATESSSSS
