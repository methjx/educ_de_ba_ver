##Class ---Ana anlatım : Class
class Person:
     # yer tutucu olarak 
    # Attributes (class kavramı içerisinde tanımlayacağımız ifadeler;)
        #Class attributes
    address = "No information.."
        ##-----
        #Costructor (yapıcı metod---->"def __init__(self, name, year):)" ---> init metodu oluşturulan her bir obje için çalıştırılabilir.
    def __init__(self, name, year): ##(self'in anlamı: class'dan türettiğimiz p1 ya da p2 objesi olarak düşünülebilir.)
        #Object attributes (Constructor içerisinde tanımlarız.(Yapıcı metod))
        self.name = name
        self.birthyear = year
        print("init metodu çalıştı")
    
    # Methods   (class kavramı içerisinde tanımlayacağımız ifadeler;)


## Object (instance)
p1 = Person("ali",1990)
p2 = Person(name="yağmur",year=1996)

#Updating;
p1.name = "Mehmetcan"
p1.address = "Ankara"

###Accessing object attributes
print(f"name: {p1.name} ,,, birthyear: {2021 - (p1.birthyear)} address: {p1.address}")
print(f"name: {p2.name} ,,, birthyear: {2021 - (p2.birthyear)}")

# print(p1)
# print(p2)
# print(type(p1))
# print(p1 == p2)