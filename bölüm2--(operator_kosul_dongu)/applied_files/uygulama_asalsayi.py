# """ Girilen bir sayinin asal olup olmadıgını bulun 
# ** asal sayi 1 ve kendisi hariç tam böleni olmayan sayılara denir.
# """
# gsayi = int(input("Bir sayi girin: "))
# sayac = 0
# for i in range(2,int(gsayi)):
#     if gsayi %i ==0:
#         sayac+=1
#         break
# if(sayac!=0):
#     print("sayi asal değildir.")
# else:
#     print("sayi asaldır.")        

#     ################################## ---Hocanın yöntemi;

sayi = int(input("sayi: "))
asalmi = True
if sayi == 1:
    asalmi = False

for i in range(2,sayi):                                              
    if sayi % i == 0:                       ### Şimdi ; buraya kadar geldiğimizde girdiğimi sayi i ye bölünürse bu asal olmayan bir sayidir.
        asalmi = False
if asalmi:
    print("girilen sayi asal")   
else:
    print("girilen sayi asal değildir.")     

###Fonksiyondan liste döndürme
# def asal(kaca_kadar):
#     """Asal sayı bulan fonksiyon
#     Girdi olarak bir sayı alır
#     Bu sayıya kadar olan asal sayıları ekrana basar.
#     """
#     asallar = [2]
#     if kaca_kadar < 2:
#         return None
#     elif kaca_kadar == 2:
#         return asallar
#     else:
#         for i in range(3,kaca_kadar):
#             bolundu = False
#             for j in range(2,i):
#                 if i % j == 0:
#                     bolundu=True
#                     break
#             if bolundu == False:
#                 asallar.append(i)
#     return asallar

# if __name__ == "__main__":
#     # join kullanmak için, listedekiler str olmalı.
#     print("\n".join([str(asal) for asal in asal(100)]))
#     """
#     Bu aşamada map() bilinmiyorsa, list comprehension veya for döngüsü kullanılır.
#     print "\n".join([str(asal) for asal in asal(1000)])
#     for asal in asal(1000)
#         print asal
# #     """