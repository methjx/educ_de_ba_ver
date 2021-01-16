# def sayilarinkatlari(liste=[],katsayisi=0,katlistesi=[]):
    
#     sayi = int(input("Katlarını bulmak istediğiniz sayıyı giriniz."))
    
#     print("{} Sayısını katı sorgulanacak sayı olarak seçtiniz!".format(sayi))
    
#     sinirlayici = int(input("""Katını alacağınız sayıyı sınırlamak istediğiniz
# bir sayı belirleyiniz(girilen sayıya kadar katını 
# almak istediğiniz sayının katı alınacak)"""))
                    
#     print("{} sayısını sınırlayıcı olarak belirlediniz !".format(sinirlayici))
    
    
#     i = sayi
#     while i!= sinirlayici:
#         liste.append(i)
#         i+=1
    
#     for j in liste:
#         if j % sayi == 0:
#             katsayisi+=1
#             katlistesi.append(j)
#     l = 0
#     for k in katlistesi:
#         if k % 3 == 0:
#             katlistesi.pop(l)
#         l+=1
            
#     return(""" Girdiğiniz {} sayısının, {} sayıya kadar olan {} tane katı vardır. 
#            Bunlar: {}""".format(sayi,sinirlayici,katsayisi,katlistesi))
           
           
# print(sayilarinkatlari())

###------------------------------------------------------------------------------------###
# 9. liste = [[1,4,18],[2,7,13],[9,6,14],[8,21,27]] şeklinde bir listemizin olduğunu düşünelim. Bu liste içindeki tek ve çift sayıları gruplandırmak istiyoruz nasıl bir kod yazmalıyız?
# liste = [[1,4,18],[2,7,13],[9,6,14],[8,21,27]]
# tekSayilar = []
# ciftSayilar = []
# for i in liste:
#     for j in i:
#         if j %2 == 0:
#             ciftSayilar.append(j)
#         else:
#             tekSayilar.append(j)
# print(f"Tek sayilar listesi: {tekSayilar}")
# print(f"Cift sayilar listesi: {ciftSayilar} ")

###----------------------------------------------------------------------###
# # Soru 1) 10 den 100 a kadar olan sayıları while döngüsünü kullanarak yazdırınız
# i=10
# while i<100:
#     i+=1
#     print(i)
# # Soru 2) 20 den 0 a kadar sayıları azalan şekilde yazan programı while döngüsünü kullanarak yazınız.
# i=21
# while i>0:
#     i-=1
#     print(i)
# # # Soru 3) while döngüsünü kullanarak girilen metni 10 defa yazdıran kodları yazınız
# i=0
# metin = "Selam,canim!"
# while i<10:
#     i+=1
#     print(metin)



