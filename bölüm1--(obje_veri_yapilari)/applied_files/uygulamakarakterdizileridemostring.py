website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sına Python Programlama Rehberiniz (40saat)"
#1- "course" karakter dizisinde kaç karakter bulunmaktadır?
print(len(course)) #ya da result = len(course) tanımlanır ve alta print(result) yaz aynı şeydir.

#2- "website" içinden www karakterlerini alın.
print(website[7:10])

#3- "website" içinden com karakterlerini alın.
#print(len(website)) 25 karakterse son 3 karakter com olacaktır yani 22:
print(website[22:]) #ya da result = website[length-3:length]

#4- "course içinden ilk 15 ve son 15 karakterlerini alın"
print(course[0:15])
print(course[49:])

#5- "course" ifadesindeki karakterleri tersten yazdırın.
print(course[::-1]) # :: komutu ifadeyi bize yazdırır ::1dersek 1er 1er düz yazdırır ::2 dersek 2ser 2ser alır buna göre !!!-->::-1 dersek tersten 1er er yazdırır.

name , surname , age , job = "Mehmetcan" , "Yılmaz" , 24 ,"engineering"

#6 yukarida verilen değişkenler ile ekrana aşapıdaki ifadeyi yazdırın.
print("My name is {0} {1} , I am {2} years old and my job is {3}.".format(name , surname ,age ,job))
#result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job

# 7 Hello world ifadesindeki w harfini W ile değiştirin
s = "Hello world"
s = s[0:6] +"W" + s[-4:]              #kısa yöntemi ise s.replace("w","W")
print(s)

#8 "abc" ifadesini yan yana 3 defa yazdırın. 
# s = "abc"*3 ve print(s)
x = "abc"
print(f"{x} {x} {x}")
#print(result)
