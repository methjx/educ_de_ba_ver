# liste = [1,2,3,4,5]

# iterator = iter(liste)
# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# """ Yani şimd iterator aynı for gibi fakat tek tek çağırılıp yine içeride gezinme yapabiliriz..."""
# for i in liste:
#     print(i)

liste = [1,2,3,4,5]   ###FOR UN YAPTIGI İS BU ASLINDA ,ALTYAPISI OLARAK DUSUNULEBİLİR..
iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

""" Peki bunu neden böyle kullanıyoruz,örneğin metodu kendimiz oluşturmak isteyebiliriz böyle bir durumda iteratore ihtiyacımız olacaktır.Örneklendirelim şöyle;;
"""

class MyNumbes:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbes(10,20)
# ##For olmadan şöyle yaparız;
my_iter = iter(list)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# """kaç kere tekrarlarsan o kadar devam eder"""
"""Ya da yukarıda yaptıgımız while döngüsünü buraya alırız"""
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break


# for x in list:
#     print(x)

