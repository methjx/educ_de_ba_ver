#Inheritance (Kalıtım): Miras Alma
#Person => name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person) gibi class tanımlarsam üstteki görevleri bu classda olmasını isterim

#Animal = > Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.isim = fname
        self.soyisim = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person..")
    
    def eat(self):
        print("Im eating right now...")

class Student(Person):
    def __init__(self, fname, lname, stunum):
        Person.__init__(self, fname, lname) ### Bunu yaparak persondaki özellikleri de miras aldım 
        print("Student Created")
        self.numara = stunum

    #override
    def who_am_i(self):
        print("Im student....")
    def sayHello(self):
        print("Hello student!!!")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)   #Person.__init__(self, fname, lname) ^^ e alternatif olarak...
        self.branch = branch
    def who_am_i(self):
        print(f"Iam {self.branch}teacher")    


p1 = Person("Ali", "Yılmaz")
s1 = Student("Mehmet", "Yılmaz", 4379)
t1 = Teacher("Serkan","Yilmaz","Math")
print(f"p1--> name: {p1.isim} and lastname: {p1.soyisim}")
print(s1.isim + " " + s1.soyisim + " " + str(s1.numara))
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
t1.who_am_i()