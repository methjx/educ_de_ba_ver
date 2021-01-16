# # #1- Girilen bir sayının 0-100 arasında olup olmadıgını kontrol ediniz.

# sayi1 = int(input("Bir sayi giriniz: "))
# result = (sayi1 >= 0) and (sayi1 <= 100)
# print(f"Sayi 0 ile 100 arasındamı? : {result}")

# # #2- Girilen bir sayının pozitif çift sayı olup olmadıgını kontrol ediniz.

# sayi2 = int(input("Bir sayi giriniz: "))
# result = (sayi2 > 0) and (sayi2%2==0)
# print(f"Girilen sayi pozitif çift sayimidir? : {result}")

# # #3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# emailUser = "mcy@hot.com"
# passwordUser = "ab1234"
# user2 = input("Bir mail girin: ")
# user3 = input("Bir şifre girin: ")
# result = (emailUser==user2) and (passwordUser==user3)      #######DAAAAAAYUM IM GOOOD
# print(f"Uygulamaya giriş başarılı oldu mu? : {result}")


# # # 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input("1.sayiyi giriniz: "))                                 
# b = int(input("2.sayiyi giriniz: "))
# c = int(input("3.sayiyi giriniz: "))

# result = (a > b) and (a > c)
# print(f"A en büyük sayımıdır? {result}")
# result = (b>a) and (b>c)
# print(f"B en büyük sayımıdır? {result}")
# result = (c>a) and (c>b)
# print(f"C en büyük sayımıdır? {result}")





# # #5-Kullanıcıdan 2vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız
# # # Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# # # a- ortalama 50 olsa bile final notu en az 50 olmalıdır.
# # # b- finalden 70 alındıgında ortalamanın önemi olmasın                 (ortalama >= 50) or (final >= 70)

# vize1 = int(input("1.Vizenizi girin: "))                        ##### MEMO eğer else-if gibi komutlar kullanmıyorsan yazdırmak için fstring ya da .format falan kullan bunu unutma bu önemli !!!
# vize2 = int(input("2.Vizenizi girin: "))
# final = int(input("Final notunuzu girin: "))
# ortalama = (vize1*30/100 + vize2*30/100) + (final*40/100)
# print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {((ortalama >= 50) and (final >= 50)) or (final >= 70)}")
#a koşulu için;
# result = (ortalama >= 50) and (final >= 50)
# #b koşulu için;
# result = ((ortalama >= 50) and (final >= 50)) or (final >= 70)                  ####### NAAAAAYYYSSS XD



# # #6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# # #Formül: (Kilo / boy uzunluğunun karesi)
# # #Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# # #0-18.4 => zayıf
# # #18.5-24.9 => normal
# # #25.0-29.9 => fazla kilolu
# # #30.0-34.9 => şişman

name = input ("İsminizi cisminizi giriniz: ")
kg = float(input("Kaç okka çekiyon: "))
hg = float(input("Boy kaç yiğeen: "))
formula = (kg) / (hg**2)

zayif = (formula >= 0) and (formula <= 18.4)
normal = (formula > 18.4) and (formula <= 24.9)
fazlakilo = (formula > 24.9) and (formula <= 29.9)
obez = (formula > 29.9) and (formula <= 34.9)

print(f"{name} isimli kişinin kilo indeksi: {formula} ve kilo değerlendirmen: {zayif}")
print(f"{name} isimli kişinin kilo indeksi: {formula} ve kilo değerlendirmen: {normal}")
print(f"{name} isimli kişinin kilo indeksi: {formula} ve kilo değerlendirmen: {fazlakilo}")
print(f"{name} isimli kişinin kilo indeksi: {formula} ve kilo değerlendirmen: {obez}")