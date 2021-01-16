#1 den 100 e kadar sayıları ekranda yazdırmak istiyorsam bir liste tanımlarım

x = 5
while x<10:
    if x%2==0:
        print(x)
    x +=1
print("bitti")

#### örneğin kullanıcıdan bir değer isteyelim kullanıcı bu değeri girene kadar sormaya devam edelim

# name = "" ##Burası false olarak değerlendiriliyor.
# while not name: ##== YANİ TRUE İKEN ###bonus: eğer boşluk karakteri girilmesini istemiyorsan name.strip() metodunu kullan ve boşluk karakteri girse dahi sormaya devam etsin.!
#     name = input("isminizi giriniz: ")

# print(f"Merhaba, {name}")    #########KISACA PROGRAMI CALISTIRDIGINDA BİR DEĞER GİRMEZSEN PROGRAM SUREKLİ İSİM SORMAYA DEVAM EDECEK

