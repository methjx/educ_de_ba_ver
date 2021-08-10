import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "mydatabase"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")

