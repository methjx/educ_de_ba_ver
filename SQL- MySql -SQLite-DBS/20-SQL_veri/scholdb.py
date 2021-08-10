import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "schooldatabase"
)


mycursor = mydb.cursor()



# mycursor.execute("Show databases")
# for i in mycursor:
#     print(i)



