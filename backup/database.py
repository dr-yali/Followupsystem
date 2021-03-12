import mysql.connector
db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123123",
        database="SCR"
)
def sql(execute):
    sql = db.cursor()