## --- DECORATORS fonksiyonlari bir fonksiyona özellik ekleme istediğimizde kullanıyoruz...
##Decorators fonksiyonumuzu bir çok fonksiyonla ilişiklendirebiliriz.

# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki islemler....!")
#         func(name)
#         print("Fonksiyondan sonraki islemler...!")
#     return wrapper

# @my_decorator ## sayHello = my_decorator(sayHello) \nsayHello() --->yerine geçer..!
# def sayHello(name):
#     print("Hello",name)

# sayHello("Mert")

###diger ornek;

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()

        time.sleep(1)

        func(*args,**kwargs)

        finish = time.time()
        print("Fonksiyonu"+func.__name__ + str(finish-start) + "saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(2,3)
faktoriyel(9)





""""def usalma(a,b):
    start = time.time() ## Suanki saniye bilgisi

    time.sleep(1) ##İslemi 1 saniye uyutadabiliriz.

    print(math.pow(a,b))

    finish = time.time() ##Bitiş saniye bilgisi

    print("Usalma fonksiyonu" + str(finish-start) + "saniye sürdü.")

def faktoriyel(num):
    start = time.time()
    print(math.factorial(num))
    finish = time.time()
    print("Faktoriyel fonksiyonu" + str(finish-start) + "saniye sürdü.")

usalma(2,3)
faktoriyel(9)
"""" Burası İLK YAPTIGIMIZ KISIMDI SONRA DECORATOR EKLEDİK !!!"