###Returning
# def usalma(number):

#     def inner(power):
#         return number ** power
    
#     return inner

# two = usalma(2) ##number yerine geçecek ve inner ı döndürecek
# print(two(4)) ###geriye dönen fonksiyona yeni parametre gönderirsek üs(power) gönderm,ş oluruz.
# three = usalma(3)
# print(three(4))


# # # Örnek yetki sayfası
# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolünün {1} sayfasina ulaşım izni vardır.".format(role,page)
#         else:
#             return "{0} rolünün {1} sayfasina ulaşım izni yoktur..".format(role,page)
#     return inner
# user1 = yetki_sorgula("Product Edit")
# print(user1("User"))

###
def islem(islem_adi):
    def toplam(*args): ###sınırsız argüman aldıralım..!
        toplam= 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim #####
    
    if islem_adi == "toplama":
        return toplam
    elif islem_adi == "carpma":
        return carpma
    else:
        print("İslem adini yanlis girdiniz.")

        
    
toplama = islem("toplama")
print(toplama(1,2,3,4,5,6))

carpma = islem("carpma")
print(carpma(1,2,3,4,5))



