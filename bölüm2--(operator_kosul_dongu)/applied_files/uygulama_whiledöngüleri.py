# sayilar = [1,3,5,7,9,12,19,21]

# # # # 1- sayilar listesini while ile ekrana yazdırın.
# length = len(sayilar)
# i = 0                                                      ######## bitiş/baslangıc noktası BURASI COK ONEMLİ
# while i < length:
#     print(sayilar[i])
#     i += 1                          ### i yerinde sayıp döngüye girmemesi için yapıyoruz!!!
    
# # 2-başlangıç ve bitiş değerlerinin kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın

# firstV = int(input("Bir başlangıç değeri girin: "))
# secV = int(input("Bir bitiş değeri girin: "))
# x = secV
# while x<firstV:
#     if x%2==1:
#         print(x)
#     x +=1
# print("Girdiğiniz değerler arasındaki tek sayılar yukarıdadır!!!")

# #########HOCANIN YAPTIGI YÖNTEM İSE;#############

# baslangic = int(input("Bir başlangıç değeri girin: "))
# bitis = int(input("Bir bitiş değeri girin: "))

# i = baslangic
# while i < bitis:
#     i += 1
#     if (i % 2 ==1):
#         print(i)




# # # 3-1-100 arasındaki sayıları azalan şekilde yazdırın.
# i = 100    ####baslangıc değerim 100
# while i >= 1:
#     print(i)
#     i -=1


# # # 4-kullanıcıdan alacağınız 5sayiyi ekranda sıralı bir şekilde yazdirin.
# a = int(input("Birinci sayiyi giriniz: "))
# b = int(input("İkinci sayiyi giriniz: "))
# c = int(input("Üçüncü sayiyi giriniz: "))
# d = int(input("Dördüncü sayiyi giriniz: "))
# e = int(input("Beşinci sayiyi giriniz: "))
# i=0
# liste = [a,b,c,d,e]
# while i < (1):
#     liste.sort()
#     print(liste)
#     i +=1

# ######## HOCANIN YAPTIĞI YÖNTEM #########
# numbers = []
# i=0
# while i<5:
#     sayi = int(input("Bir sayi: "))
#     numbers.append(sayi)
#     i+=1
#     numbers.sort()
# print(numbers)    




# # # 5-kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız.
# # # a-)**ürün sayısını kullanıcıya sorun 
# # # b-)**dictionary listesi yapısı (name,price) şeklinde olsun
# # # c-)** ürün ekleme işlemi bittiğinde ürünleri ekran while ile listeleyin.

ürünler = []

ürünsayisi = int(input("Kaç ürün eklemek istersiniz? : "))          ### ürünü kullanıcıdan istedim devamında while ile (i<ürünsayisi kadar programı devam ettirdim i+=1 ide unutmadım.)
i=0
while(i<ürünsayisi):
    name = input("ürün ismi: ")             ###name ve price değişkenleri atadım çünkü bunları dictionary lise yapısında kullanıcam 
    price = input("ürün fiyatı: ")
    ürünler.append({                        ###ürünler.append({}) diyerek key:value değeri şeklinde ürünler listesine eklettim.
        "name" : name,
        "price": price,
    })
    i+=1
for urun in ürünler:                            ### ürünler listesindeki elemanlarıda for döngüsü ile görüntüledim
    print(f'ürün adi: {urun["name"]} ürün fiyatı: {urun["price"]}')


