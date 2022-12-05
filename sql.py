import sqlite3

def create_data_table():
    '''
    Meant to be called once 
    '''
    #Connecting to sqlite
    conn = sqlite3.connect('Central.db')

    cursor = conn.cursor()

    #Doping BETS table if already exists
    cursor.execute("DROP TABLE IF EXISTS DATA")

    sql ='''CREATE TABLE DATA(
    ID INTEGER PRIMARY KEY,
    date INTEGER, 
    email text,
    password text
    )'''
    cursor.execute(sql)
    print("Table created successfully........")

    conn.commit()

    conn.close()

def insert_initial_data(date, email, password):
    conn = sqlite3.connect('Central.db')

    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a bet into the database.
    cursor.execute('''INSERT OR IGNORE INTO DATA(
    DATE, EMAIL, PASSWORD) VALUES 
    (?, ?, ?)''', (date, email, password))

    conn.commit()
    print("record inserted........")

    conn.close()

def show_all():
    conn = sqlite3.connect('Central.db')

    cursor = conn.cursor()

    cursor.execute('''SELECT * from DATA''')

    #Fetching 1st row from the table
    # result = cursor.fetchone()
    # print(result)

    result = cursor.fetchall()
    conn.commit()

    conn.close() 
    
    return result

