name = "mehmetcan"
# name değerimiz global
def changeName(new_name):
    global name                                                ###global name -->yazarsak name bilgimizi güncelleyecektir
    #name değerimiz içeride local
    name = new_name
    print(name)
changeName("mert") ##local
print(name) ##global




"""-----içiçe fonk tanımlarsak---"""
###
# name = "global string"
# def greeting():
#     # name = "mehmetcan"

#     def hello():           ### 3- yine nameleri yorum yaparsak bu sefer en üstteki name değerini alır.
#         name = "mert"   ### 2- fakat burada name tanılaması yaparsak ,bunu yazdırırırz. local olarak!
#         print("hello " + name) ### 1- buradaki name değerimiz; bir üstte tanımladıgımız fonksiyonun LOCAL değeriyken; bu kısımda GLOBAL değeri oluyor.
#     hello()
# greeting()

"""--------Daha iyi anlamak için global-local-örnek--------"""
# x = 50
# def test():        ##---->Dışarıda global olarak tanımlanan bir değişkenin içerisini fonksiyon içerisinden değiştirmek istersen test(x) yerine--> global x;; line24 
#     global x
#     print(f"x : {x}")

#     x= 100
#     print(f"changed x to {x}")
# test()     
# print(x)    ##----> bu sekilde yine global değerimiz karşımıza gelicek