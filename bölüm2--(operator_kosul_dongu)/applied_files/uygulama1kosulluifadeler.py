# #1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.Ehliyet alma koşulu en az 18 ve eğitim durumu lise yada üniversite olmalıdır.
# name = input("Lütfen isminizi giriniz: ")
# age = int(input("Yasinizi giriniz: "))
# educ = input("Eğitim durumunuz nedir: ")

# if age >= 18:
#     if educ == ("lise") or ("üniversite"):
#         print("Egitim durumu uygun, ehliyet alabilir.")
#     else:
#         print("Egitim durumu uygun değildir, ehliyet alamaz!")    
# else:
#     print("Yasınız ehliyet icin uygun degildir.")    



# #2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
# # 0-24 => 0
# # 25-44 => 1
# # 45-54 => 2
# # 55-69 => 3
# # 70-84 => 4
# # 85-100 =>5
# yaz1 = int(input("1.yazili sinav sonucunu giriniz: "))
# yaz2 = int(input("2.yazili sinav sonucunu giriniz: "))
# soz1 = int(input("1.sozlu sinav sonucunu giriniz: "))
# ortalama = (yaz1 + yaz2 + soz1)/3
# if (ortalama >= 0) and (ortalama < 25) :
#     print(f"Sınav not bilginiz : {ortalama} ve sınav notunuz: 0")
# elif (ortalama >= 25) and (ortalama < 45) :
#     print(f"Sinav not bilginiz: {ortalama} ve sınav notunuz: 1")
# elif (ortalama >= 45) and (ortalama < 55) :
#     print(f"Sinav not bilginiz: {ortalama} ve sınav notunuz: 2")       
# elif (ortalama >= 55) and (ortalama < 70) :
#     print(f"Sinav not bilginiz: {ortalama} ve sınav notunuz: 3")
# elif (ortalama >= 70) and (ortalama < 85) :
#     print(f"Sinav not bilginiz: {ortalama} ve sınav notunuz: 4")
# elif (ortalama >= 85) and (ortalama <= 100) :
#     print(f"Sinav not bilginiz: {ortalama} ve sınav notunuz: 5")
# else:
#     print("Sınav bilgileriniz girerken bir hata oluşmuş olmalı,Tekrar deneyiniz.!")    



# # 3- Trafiğe çıkış tarihi alınan bir aracın servis zamnını aşağıdaki bilgilere göre hesaplayınız.
# # 1.Bakım => 1.yıl
# # 2.Bakım => 2.yıl
# # 3.Bakım => 3.yıl
# # **Süre hesabını alınan gün,ay,yıl bilgisine göre gün bazlı hesaplayınız. 
# # ***datetime modülünü kullanmanız gerekiyor.                   #####BUNU TEKRAR BİR İNCELE !!!


# import datetime
# tarih = input("Aracin trafige cikis tarihi (2019/9/3)seklinde: ")
# tarih = tarih.split("/")

# trafikCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafikCikis
# aracTrafikcikis = fark.days
# if (aracTrafikcikis <= 365):
#     print(f"Araciniz {aracTrafikcikis} gündür trafiktedir ve 1.bakım tarihi gelmiştir. ")
# elif (aracTrafikcikis>365) and (aracTrafikcikis<= 365*2):
#     print(f"Araciniz {aracTrafikcikis} gündür trafiktedir ve 2.bakım tarihi gelmiştir. ")   
# elif (aracTrafikcikis>365*2) and (aracTrafikcikis<= 365*3):
#     print(f"Araciniz {aracTrafikcikis} gündür trafiktedir ve 3.bakım tarihi gelmiştir. ")
# else:
#     print("Bir yanlışlık mı oldu agam?")    