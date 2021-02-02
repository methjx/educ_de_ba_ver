# def fonk(n):
#     if n < 0 :
#         return "Negatif değer olmamalı!"
#     else:
#         return n
# f = fonk(6)
# print(f)               
# """
# """
# def sistem_bilgisi():
#     import sys
#     print("\nSistemde kurulu Pythonın: ")
#     print("\nAna sürüm nosu: ",sys.version_info.major)
#     print("\nAlt sürüm nosu: ",sys.version_info.minor)
#     print("\nMinik sürüm nosu: ",sys.version_info.micro)
#     print("\nKullanılan işletim sisteminin;")
#     print("\tAdi: ",sys.platform)

# sistem_bilgisi() 

# """----Kayıt oluşturma Fonksiyonu;
# """
# def kayit_olustur(isim, soyisim, sehir):
#     print("-"*15,"YilmazAilesi"*1, "-"*15)
#     print("isim          :", isim)
#     print("soyisim       :", soyisim)
#     print("sehir         :", sehir)
#     print("-"*30)
# kayit_olustur("Mehmetcan","Yilmaz","Kırcaali")
# kayit_olustur("Mert","Yilmaz","Kırcaali")
# kayit_olustur("Bircan","Yilmaz","Kırcaali")
# kayit_olustur("Hayrettin","Yilmaz","Kırcaali")

# """Kare bulma ve karekök bulma fonksiyonu;
# """
# def kare_bul():
#     sayi = int(input("sayi : "))
#     cikti = f"---{sayi}---sayisinin;\n---Karesi---> {sayi**2}\n---Karekökü--->{sayi**0.5} ..."
#     print(cikti)
# kare_bul()   
 
# """Kendi len() komutumuzu yapalım;
# """
# def uzunluk(oge):
#     c = 0
#     for s in oge:
#         c+=1
#     print(c) ## oge dersem yazıyı cıkarıcak
# uzunluk("memo")

# liste = ["ankara","istanbul","izmir"] ### oluşturudugumuz fonksiyon sadece karakter dizilerinin değil diğer veri tiplerininde uzunlugunu hesaplayabilir.
# uzunluk(liste)

# # """dosya kopyalama fonksiyonum;
# # """((((BU KISMI TAM ANLAMADIM!!!))))
# def kopyala(kaynak_dosya, hedef_dizin):
#     cikti = f"{kaynak_dosya}isimli dosya --->{hedef_dizin}isimli dizin içine kopyalandı!"
# kopyala("/Users/mehme/Desktop/buradan/cekicen.txt","/Users/mehme/Desktop/buraya")
