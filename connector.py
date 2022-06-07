import mariadb
import sys

#instance:
#Simple connection made with Python and MariaDB, using HTML and CSS
#for creating the interface
#root
#pw:abc

def connect_main(user_id, user_pw, db_select):
    try:
        conn = mariadb.connect (
            user = user_id,
            password = user_pw ,
            host = '127.0.0.1',
            port = 3306,
            database = db_select,
        )
        cur = conn.cursor()
    except mariadb.Error as Error:
        print('Error while connecting.')
        sys.exit(1)

def show_databases(user_id, user_pw):
    try:
        conn = mariadb.connect (
            user = user_id,
            password = user_pw ,
            host = '127.0.0.1',
            port = 3306,

         )
         
        cursor = conn.cursor() 
        databases = []
        cursor.execute("SHOW DATABASES")
        for (database,) in cursor.fetchall():
            databases.append(database)
        return databases
    except mariadb.Error as Error:
        print('Error while connecting.')
        sys.exit(1)

def use_database(db_select):
    try:
        conn = mariadb.connect (
            user = 'root',
            password = 'abc' ,
            host = '127.0.0.1',
            port = 3306,
            database = db_select,
        )
        cur = conn.cursor()
        cur.execute("USE " + db_select)
        #loading the tables
        tables = []
        cur.execute("SHOW TABLES")
        for (table,) in cur.fetchall():
            tables.append(table)
        conn.close()
        return tables

    except mariadb.Error as Error:
        print('Error while connecting:',Error)
        sys.exit(1)
