# # 1- Kullanıcının girdiği 2 sayıdan hangisi daha büyüktür ?
# sayi1 = int(input("1.Sayiyi giriniz: "))
# sayi2 = int(input("2.Sayiyi giriniz: "))
# result = sayi1 > sayi2

# # 2- Kullanıcıdan 2 , vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# # Eğer ortalama 50 ve üstündeyse geçti , değilse kaldı yazdırın
# vize = int(input("Vize notunuzu giriniz: "))
# final = int(input("Final notunuzu giriniz: "))
# ortalama = (vize*(60/100) + final*(40/100))
# if ortalama>=50:
#     print("Tebrikler,Geçtiniz!")
# else:
#     print("Üzgünüm,Kaldınız.")

# result = ortalama

# # 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın
# sayi = int(input("Bir Sayi Giriniz: "))
# if (sayi%2==0):
#     print("Girilen sayi çifttir.")
# else:
#     print("Girilen sayi tektir.")



# # 4- Girilen bir sayının negatif , pozitif durumunu yazdırın
# sayi = int(input("Bir Sayi Giriniz: "))
# if (sayi>=1):
#     print("Girilen sayi pozitiftir.")
# else:
#     print("Girilen sayi negatiftir.")



# # 5-Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# #         (email: email@mehmetylmz.com parola:abc123)

email= input("email: ")
if email=="email@mehmetylmz.com":
    print("Kabul edildi,şimdi şifre giriniz.")
else:
    print("Sisteme kayıtlı böyle bir mail bulunmamaktadır.Lütfen kayıtlı bir mail giriniz.")
parola = input("parola: ")
if parola=="abc123":
    print("Şifre kabul edildi.")
else:
    print("Yanlış şifre girilmiştir.Geri sayım başlatılıyor...3...2...1\n...BOOOM")
# ##5.SORU İÇİN ALTERNATİF YÖNTEM if else kullanmadan!!!!
# email = "email@mehmetylmz.com"
# password = "abc123"
# girilenEmail = input("email: ")
# girilenPassword = input("parola: ")
# isEmail = (email == girilenEmail.lower().strip())  ###lower deme sebebim büyük küçük harf hassasiyetini ortadan kaldırmak istemem .strip ise kullancı yanlışlıkla bosluk bırakırsa basta veya sonda bunu ortadan kaldırmak istemem.!
# isPassword = (password ==girilenPassword)
# print(f"Email bilgisi doğrumudur?: {isEmail} ve parola doğru mudur?: {isPassword} ")




# print(result)


