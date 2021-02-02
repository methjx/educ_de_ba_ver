# ## Gönderilen bir kelimeyi belirtilen kez erkanda gösteren fonksiyonu yazın.
# def yazdir(kelime, adet):
#     print(kelime * adet)
# yazdir("mehmetcan\n", 10)

## Kendine gönderilen sayıdaki sınırsız parametreyi bir listeye çeviren fonksiyonu yazın
# def listeye_cevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)
#     return liste
# result= listeye_cevir(10,20,30,"s.a")
# print(result)

## Gönderilen 2 sayı arasındaki tüm asaln sayıları bulun
# def asalsayibul(sayi1, sayi2):
#     for sayi in range(sayi1,sayi2+1): ### +1 koyma sebebi rangefonksiyonunun o noktadaki sayıyı dahil etmemesi
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# sayi1 = int(input("sayi1: "))
# sayi2 = int(input("sayi2: "))
# # asalsayibul(sayi1,sayi2)

## Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.
def tambolenbul(sayi):
    tambolenler = []
    for i in range(2,sayi+1):
        if sayi % i == 0:
            tambolenler.append(i)
    return tambolenler
sayi = int(input("sayi : "))
print(f"İstenilen {sayi} sayisinin tam bölenleri : ",tambolenbul(sayi))   
"""----------YA DA ALTTAKİ GİBİ-----------"""
# def tambolenbul(sayi):
#     tambolenler = []
#     for i in range(2,sayi+1):
#         if sayi % i == 0:
#             tambolenler.append(i)
#     return tambolenler
# print("***TAM BOLEN BULMA PROGRAMI***")        
# while True:
#     print("Çıkmak için q basınız")
#     sayi = input("sayi : ")
#     if sayi=="q":
#         print("Program sonladırılıyor...")
#         break
#     else:
#         sayi = int(sayi)
#         print("Tam bolenler : ", tambolenbul(sayi))