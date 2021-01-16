"""
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukaru ifadeleri ile buldurmaya çalışın.
** "random modülü" için "python random" şeklinde arama yapın
** 100 üzerinden puanlama yapın her soru 20 puan.
** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""

# import random
# sayi = random.randint(0,100)

# hak_sayisi = int(input("Soruları bilmek için kaç hakkınız olsun?:(En az 5 giriniz!) "))
# print(f"Hak sayınızı {hak_sayisi} olarak belirlediniz.")

# for i in range(hak_sayisi):
#     cevap = input("1.Sorunuz Türkiyenin başkenti neresidir? : ")
#     if cevap == "ankara":
#         print(f"Verdiğiniz cevap doğru 2.soruya geçebilirsiniz.")
#         break
#     else:
#         hak = (hak_sayisi-1) - i
#         print(f"Verdiğiniz cevap yanlış {hak} hakkınız kaldı.")
# -------------------------------------------------------------------------------------
import random
sayi = random.randint(1,30)
sayac = 0
hak_sayisi = int(input("Soruları bilmek için kaç hakkınız olsun? "))
can = hak_sayisi
print(f"Doğru cevabı bulabilmek için {hak_sayisi} hakkınız var...")
print(sayi)
while hak_sayisi>0:
    hak_sayisi-=1
    sayac+=1
    sayig = int(input("1-100 arasında bir sayi giriniz (0'oyundan çıkar): "))
    if sayig==0:
        print("Oyunu iptal ettiniz.")
        break
    elif sayig < sayi:
        print("Girdiğin sayi daha aşağıda...Yukarı")
        continue
    elif sayi == sayig:
        print(f"Tebrikler...{100 - (100/hak_sayisi) * (sayac+1)}")
        break
    else:
        print("Girdiğin sayi daha yukarıda...Aşağı")
        continue

print(f"Maalesef hakkınız bitti... {sayac} kere denediniz.")
       