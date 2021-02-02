###  Bankamatik Uygulaması
##Veri yapısı oluşturmalıyız öncelikle;
MehmetHesap = {
    "ad": "Mehmetcan Yilmaz",
    "hesap no": "1234123",
    "bakiye": 3000,
    "ekHesap": 2000
}
MertHesap = {
    "ad": "Mert Yilmaz",
    "hesap no": "12341231",
    "bakiye": 2000,
    "ekHesap": 1000
}
def paraCek(hesap, miktar):
    print("*"*50)
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz..")
        bakiyeSorgu(hesap)
        print("*"*50)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if (toplam >= miktar):
            bakiyeSorgu(hesap)
            print("*"*50)
            ekHespKullnm = input("Bakiyeniz yetersiz, ekhesap kullanılsınmı (E/H) ?")
            if ekHespKullnm == "E":
                ekhspkllnm = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhspkllnm
                print("Paranızı alabilirsiniz.")
                bakiyeSorgu(hesap)
                print("*"*50)
            else:
                print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")    
        else:
            print("Bakiyeniz yetersiz...")
            bakiyeSorgu(hesap)
            print("*"*50)

def bakiyeSorgu(hesap):
    print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.Ekhesap limitinizse : {hesap['ekHesap']} kadardır. ")




# bakiyeSorgu(MehmetHesap)
paraCek(MehmetHesap,3400)
# print("*"*50)
# bakiyeSorgu(hesap)
paraCek(MehmetHesap,1400)
# print("*"*50)
# bakiyeSorgu(MehmetHesap)


####### PARA YATIRMA FONKSİYONU YAP BU KISMA !!!