#Not uygulaması;
def not_hesapla(satir):
    satir = satir[:-1] ### Liste olusumunda aralarda oluşan boşlukları alıyorum çünkü her satır benim için bir bilgi olmalıdır.
    liste = satir.split(":") ### split ile satırı : dan ayırıyorum çünkü ilgilendiğim kısım notlar...
    # print(liste)
    ogrenciAdi = liste[0]
    ogrenciNot = liste[1].split(",") ## burada notları tekrar bölmeliyim.! Çünkü her notu ayrı toplattırmak istiyorum mantıken

    not1 = int(ogrenciNot[0])
    not2 = int(ogrenciNot[1])
    not3 = int(ogrenciNot[2])

    ortalama = (not1+not2+not3)/3

    if ortalama >= 90 and ortalama<=100:
        harf = "AA"
    elif ortalama>=85 and ortalama <= 89:
        harf = "BA"
    elif ortalama>=80 and ortalama <= 84:
        harf = "BB"
    elif ortalama>=75 and ortalama <= 79:
        harf = "CB"
    elif ortalama>=70 and ortalama <= 74:
        harf = "CC"
    elif ortalama>=65 and ortalama <= 69:
        harf = "DC"
    elif ortalama>=60 and ortalama <= 64:
        harf = "DD"
    elif ortalama>=50 and ortalama <= 59:
        harf = "FD"
    else:
        harf = "FF"
    return ogrenciAdi + ": " + harf + "\n"


def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input("Öğrenci adi : ")
    soyad = input("Öğrenci soyadi : ")
    not1 = input("Öğrenci 1.NOT : ")
    not2 = input("Öğrenci 2.NOT : ")
    not3 = input("Öğrenci 3.NOT : ")
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+ ":"+not1+","+not2+","+not3+"\n")

def not_kayit():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = [] ##Okunan sonuçları liste içine almalıyız bu sebeple tanımladık

        for i in file:      
            liste.append(not_hesapla(i))
        
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1- NOTLARI OKU\n2- NOT GIR\n3- NOTLARI KAYIT ET\n4- ÇIKIŞ\n")
    if islem == "1":
        ortalamalari_oku()
    elif islem =="2":
        not_gir()
    elif islem == "3":
        not_kayit()
    else:
        break