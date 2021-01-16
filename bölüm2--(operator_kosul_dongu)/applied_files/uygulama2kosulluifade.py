""" else-if-elif kullan bu sefer!
1-Girilen bir sayının 0-100 arasında olup olmadıgını kontrol ediniz.

2-Girilen bir sayının pozitif çift sayı olup olmadıgını kontrol ediniz.

3-Email ve parola bilgileri ile giriş kontrolü yapınız.

4-Girilen 3 sayıyı büyüklük oranı olarak karşılaştırınız.

5-Kullanıcıdan 2vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız
 Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
 a- ortalama 50 olsa bile final notu en az 50 olmalıdır.
 b- finalden 70 alındıgında ortalamanın önemi olmasın      

6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# # #Formül: (Kilo / boy uzunluğunun karesi)
# # #Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# # #0-18.4 => zayıf
# # #18.5-24.9 => normal
# # #25.0-29.9 => fazla kilolu
# # #30.0-34.9 => şişman"""


# #1.Soru;
# user = int(input("Bir sayi giriniz: "))
# if user>0 and user<=100:
#     print(f"Girilen sayi {user} 0-100 arasindadir.")
# else:
#     print(f"Girilen sayi {user} 0-100 arasinda değildir.")    

# #2.soru;
# user = int(input("Bir sayi giriniz: "))
# if user>0 and user%2==0:
#     print(f"Girilen sayi pozitif çift sayidir.")
# elif user>0 and user%2==1:
#     print(f"Girilen sayi pozitif tek sayidir.")
# elif user<0 and user%2==0:
#     print(f"Girilen sayi negatif çift sayidir.")
# elif user<0 and user%2==1:
#     print(f"Girilen sayi negatif tek sayidir.")    
# else:
#     print("Girilen sayi 0'dir.")    

# #3.soru;
# username = input("Kullanici adi: ")
# password = input("Şifre: ")
# emailUser = "mcy@hot.com"
# passwordUser = "ab1234"
# if username == emailUser:
#     print(f"Girmiş oldugunuz mail; kabul edilmiştir.")
#     if password == passwordUser:
#         print("Şifre doğru,giriş başarılı.")
#     else:
#         print("Şifre yanlış girildi.")        
# else:
#     print("Girmiş oldugunuz username sisteme kayıtlı değildir.")    

#4.soru;
# a = int(input("1.sayiyi giriniz: "))                                 
# b = int(input("2.sayiyi giriniz: "))
# c = int(input("3.sayiyi giriniz: "))
# if a>b and a>c :
#     print("a en büyük sayidir.")
# elif b>a and b>c:
#     print("b en büyük sayidir.")
# elif c>a and c>b:
#     print("c en büyük sayidir.") 
# else:
#     print("Bir yanlıslık yaptınız , kontrol ediniz.")           

# # #5.soru;
# vize1 = int(input("1.Vizenizi girin: "))                        
# vize2 = int(input("2.Vizenizi girin: "))
# final = int(input("Final notunuzu girin: "))
# ortalama = (vize1*30/100 + vize2*30/100) + (final*40/100)
# ## A KISMI;
# # if (ortalama >= 50):
# #     if (final>=50):
# #         print(f"Ogrencinin not ortalaması {ortalama} ve Ogrenci geçti.")
# #     else:
# #         print(f"Ogrencinin not ortalaması {ortalama} fakat 50 barajından kaldı.")
# # else:
# #     print(f"Ogrencinin not ortalaması: {ortalama} ve kaldı.")
# ## B KISMI;
# # if (ortalama >= 50):
# #     print(f"Ogrenci not ortalaması: {ortalama} ve ogrenci geçti. ")
# # else:
# #     if (final >= 70):
# #         print(f"Ogrenci not ortalaması: {ortalama} dir. Finalden 70 üzeri aldıgından ogrencı geçti")
# #     else:
# #         print(f"Ogrenci not ortalaması: {ortalama} dir. Ogrenci kaldi.")        







# #6.soru;
# name = input ("İsminizi cisminizi giriniz: ")
# kg = float(input("Kaç okka çekiyon: "))
# hg = float(input("Boy kaç yiğeen (1.78cm seklınde yaz):  "))
# formula = (kg) / (hg**2)

# if (formula >= 0) and (formula <= 18.4):
#     print(f"Zayifsiniz ve indeksiniz {formula}")
# elif (formula > 18.4) and (formula <= 24.9):
#     print(f"Normalsiniz ve indeksiniz {formula}")
# elif (formula > 24.9) and (formula <= 29.9):
#     print(f"Fazla kilonuz var {formula}")
# elif (formula > 29.9) and (formula <= 34.9):
#     print(f"Obezsiniz indeksiniz {formula}")
# else:
#     print("Yanlıslık yapmıs olabilirsiniz kontrol edin.")    
