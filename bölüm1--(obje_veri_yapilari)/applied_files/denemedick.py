
galeri = {}
arabaYili = input("Araba Yili: ")
arabaMarka = input("Arabanın Markası: ")
arabaModel = input("Araba Modeli: ")
arabaFiyat = input("Arabanın Piyasa Fiyatı: ")

galeri.update({
    arabaYili : {
        "Marka" : arabaMarka ,
        "Model" : arabaModel ,
        "Fiyat" : arabaFiyat ,

    }
})
arabaYili = input("Araba Yili: ")
arabaMarka = input("Arabanın Markası: ")
arabaModel = input("Araba Modeli: ")
arabaFiyat = input("Arabanın Piyasa Fiyatı: ")

galeri.update({
    arabaYili : {
        "Marka" : arabaMarka ,
        "Model" : arabaModel ,
        "Fiyat" : arabaFiyat ,

    }
})

XX="ISTEDIGINIZ ARABANIN YIL BILGISINI GİRİNİZ" + "\nLISTEYI GORMEK ICIN DEVAM EDİNİZ"
print(XX)

mBilgi = input("Araba Yili: ")  ## bunu galeri{} listesinin içine atmam lazım!
araba = galeri[mBilgi]
print(araba)

#####TEKRAR AMAÇLI YAPTIM 