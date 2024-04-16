import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="",
        database="master_python"
    )
    
    cursor = database.cursor(buffered=True)
    
    return [database, cursor]