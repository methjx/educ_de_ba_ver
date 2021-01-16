
sayilar = [1,3,5,7,9,12,19,21]


#1- Sayilar listesindeki hangi sayılar 3'ün katıdır?
for say in sayilar:
    if say%3 == 0 :
        print(f"{say} --->Sayisi 3ün katıdir.")
    else:
        print(f"{say} --->3'ün katı değildir.")
    


#2- Sayilar listesinde sayilarin toplamı kaçtır?
toplam = 0

for say in sayilar:
    toplam += say ##toplam = toplam + say
print("toplam: ",toplam)

#3- Sayilar listesindeki tek sayıların karesini alınız.
for sayi in sayilar:
    if sayi %2 == 1:
        x = sayi**2
        
print(x,sayi%2==1)    
    
    
"---------------------------------------------------------------------"

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?

for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)

urunler = [
    {"name" : "samsung s6", "price" : "3000"},
    {"name" : "samsung s7", "price" : "4000"},
    {"name" : "samsung s8", "price" : "5000"},
    {"name" : "samsung s9", "price" : "6000"},
    {"name" : "samsung s10", "price" : "7000"}
]

# 5-Ürünlerin fiyatlarının toplamı  nedir?
toplam = 0
for urun in urunler:
    toplam += int(urun["price"])
print("toplam fiyat: ",toplam)   

#6-Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz?
for urun in urunler :
    if int(urun["price"]) <= 5000:
        print(urun["name"],urun["price"])
    
