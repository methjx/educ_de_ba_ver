import mysql.connector
from datetime import datetime
from schoolconnectorWithOOP import connection

##BU CALISMADI BİR KONTROL ET BAKEM
class Student:
    connection = connection
    mycursor = connection.cursor()


    def __init__(self,name,surname,StudentNumber,gender,birthdate):
        self.name = name
        self.surname = surname
        self.StudentNumber = StudentNumber
        self.gender = gender
        self.birthdate = birthdate
    
    def saveStudent(self):
        sql = "INSERT INTO students(name,surname,StudentNumber,gender,birthdate) VALUES(%s,%s,%s,%s,%s)" 
        value = (self.name,self.surname,self.StudentNumber,self.gender,self.birthdate)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
            print(f"son eklenen kayıtın id: {Student.mycursor.lastrowid}")
        except mysql.connector.Error as err:
            print('Hata:',err)
        finally:
            Student.connection.close()
            print("database bağlantısı kapandı.!")

mehmet = Student("Mehmetcan","Yılmaz",7349,"e",datetime(1996,8,17))
mehmet.saveStudent