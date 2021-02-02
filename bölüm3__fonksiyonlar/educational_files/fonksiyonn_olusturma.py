# def changeName(n):
#     n ="ada"

# name = "yigit0"
# changeName(name)
# print(name)



# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara", "izmir"]
# # n = sehirler[:] ## slicing process
# change(sehirler[:])

# print(sehirler)
# # print(n)

# ##

# def add(a, b, c=0, d=0 ,e=0):          #şimdi bu kısımda belirlediğim 2 parametre var fakat ;ekle kısımında 3. bir parametre eklemek istiyorum o zaman parametreleri belirlerken c = 0 , d= 0 gibi parametre eklersem; hem ilk parametre hemde sonradan eklediklerim ekranda karşıma çıkabilir.
#     return sum((a,b,c,d))                      ###27.satıra dikkat! 5parametreden fazla kullanmak istersen;;

# print(add(10, 20, 30,44))
# ####
# def add(*params):                           ###33.satıra geç...
#     print(params) ### tuple listemizi görebiliriz..
#     return sum(params)
    
# print(add(10, 20, 30,40,50,60,70,33))
##
def add(*params):                 ### 1adet*--> tuple --liste için
    print(type(params))
    sum = 0
    for n in params:
        sum+=n
    return sum  
print(add(10,12,13))    
##
def displayUser(**args):        ### 2 adet** dictionary 
    for key, value in args.items():
        print(type(args))
        print("{} is {}".format(key,value))        
displayUser(name="mehmet", age=24, city="gircali")
displayUser(name="bilge", age=14, city="hasküy", phone="12341234")
displayUser(name="simge", age=24, city="selanik", phone="12341234", email="metcn@hotmail.com")
def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
# myfunc(3, 4, 5, 6, 7, key1 = "value1", key2 = " value2")    