##Special methods;

myList = [1, 2, 3]
myString = "my string"
# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")
    
    def __str__(self):
        return f"{self.title} by {self.director}" ## m'yi göstermek istediğimizde ram de ki adresini göstermek yerine artık bunu göstereceğiz.

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Film objesi silindi..")

m = Movie("Film adı: ", "Yönetmen adı: ", 120)
print(m)
print(len(m))
del m
print(m)


""//DİĞER PYTHON ÖZEL METODLARI//""
