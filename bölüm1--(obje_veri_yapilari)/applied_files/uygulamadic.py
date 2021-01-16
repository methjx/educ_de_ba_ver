# """
#     ogrenciler = {
#         "120" : {
#             "ad" : "Ali",
#             "soyad" : "Yilmaz",
#             "telefon" : "532 000 00 01"
        
#         },
#         "125" : {
#             "ad" : "Can",
#             "soyad" : "Korkmaz",
#             "telefon" : "532 000 00 02"
#         },
#         "128" : {
#             "ad" : "Volkan",
#             "soyad" : "Yükselen",
#             "telefon" : "532 000 00 03"
#         },
#     }
#     1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız
        # 2- öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisine ulaşın.


ogrenciler = {}

ogrenciNo = input("Ogrenci no: ")
ogrenciAd = input("Ogrenci adi: ")
ogrenciSoyad = input("Ogrenci soyadi: ")
ogrenciTel = input("Ogrenci Tel no: ")

# ogrenciler[ogrenciNo] = {
#     "isim" : ogrenciAd,
#     "soyisim" : ogrenciSoyad,
#     "telefon" : ogrenciTel,
# }
ogrenciler.update({                                          #31.satırdaki sistemin aynısı fakat update kullandığımızda birden fazla veriyi aynı anda ekleyebiliriz.
    ogrenciNo : {
        "isim" : ogrenciAd,
        "soyisim" : ogrenciSoyad,
        "telefon" : ogrenciTel,
    }
})
ogrenciNo = input("Ogrenci no: ")
ogrenciAd = input("Ogrenci adi: ")
ogrenciSoyad = input("Ogrenci soyadi: ")
ogrenciTel = input("Ogrenci Tel no: ")

ogrenciler.update({                                          
    ogrenciNo : {
        "isim" : ogrenciAd,
        "soyisim" : ogrenciSoyad,
        "telefon" : ogrenciTel,
    }
})
ogrenciNo = input("Ogrenci no: ")
ogrenciAd = input("Ogrenci adi: ")
ogrenciSoyad = input("Ogrenci soyadi: ")
ogrenciTel = input("Ogrenci Tel no: ")

ogrenciler.update({                                          
    ogrenciNo : {
        "isim" : ogrenciAd,
        "soyisim" : ogrenciSoyad,
        "telefon" : ogrenciTel,
    }
})



print("*"*50)

okulNo = input("Ogrenci no: ")
ogrenci = ogrenciler[okulNo]
print(ogrenci)
print(f"Aradığınız {okulNo} nolu ogrencinin adi: {ogrenci['isim']} ,soyadi: {ogrenci['soyisim']} ve ogrenci telefon bilgisi: {ogrenci['telefon']} dir ")


