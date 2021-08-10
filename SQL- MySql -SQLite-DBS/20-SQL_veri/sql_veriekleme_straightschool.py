import mysql.connector

def insertProduct(name,surname,StudentNumber,gender,birthdate):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "mysql1234",database = "schooldatabase")
    cursor = connection.cursor()

    sql = "INSERT INTO students(name,surname,StudentNumber,gender,birthdate) VALUES(%s,%s,%s,%s,%s)"
    values = (name,surname,StudentNumber,gender,birthdate)
    
    cursor.execute(sql,values)

    try:

        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"son eklenen kayıtın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print('Hata:',err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.!")

def insertProducts(List):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "mysql1234",database = "schooldatabase")
    cursor = connection.cursor()

    sql = "INSERT INTO students(name,surname,StudentNumber,gender,birthdate) VALUES(%s,%s,%s,%s,%s)"
    values = List
    
    cursor.executemany(sql,values)

    try:

        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"son eklenen kayıtın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print('Hata:',err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.!")


List = []
while True:
    name = input('Öğrenci İsmi: ')
    surname = input('Öğrenci Soyismi: ')
    StudentNumber = int(input('Öğrenci Numarası: '))
    gender = input('Öğrenci Cinsiyeti: ')
    birthdate = input('Öğrenci Doğumyılı: ')
    
    List.append((name,surname,StudentNumber,gender,birthdate))

    result = input("Kayıt yapmaya devam etmek istiyormusunuz? Y/N")
    if result == "N" or "n":
        print("Kayıtlar veritabanına aktarılıyor...")
        insertProducts(List)
        break
    

# insertProduct(name,surname,StudentNumber,gender,birthdate)