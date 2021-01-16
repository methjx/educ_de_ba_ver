names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998, 2000, 1998, 1987]

#1- "Cenk" ismini listenin sonuna ekleyiniz.
result = names.append("Cenk")
result = names

#2- "Sena" değerini listenin başına ekleyiniz.
result = names.insert(0,"Sena")
result = names

#3- "Deniz" ismini listeden siliniz.
result = names.remove("Deniz")
result = names

#4- "Deniz" isminin indeksini nedir?
# result = names.index("Deniz")

#5- "Ali" listenin bir elemanımıdır ?
result = "Ali" in names

#6- "Liste elemanlarını ters çeirin"
# names.reverse()
# print(names)
# years.reverse()
# print(years)

#7- Liste elemanlarını alfabetik olarak sıralayın.
# names.sort()
# print(names)
# years.sort()
# print(years)

#8- years listesini rakamsal büyüklüğe göre sıralayın
# years.sort()
# years.reverse()
# print(years)

#9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
# model = ["Şevo", "Dacia"]     # str = "Chevrolet,Dacia"
# print(model)                  #result = str.split(",")   

#10- years dizisinin en büyük ve en küçük elemanı nedir
# max = max(years)
# min = min(years)
# print(max , min)

# #11 -years dizisinde kaç tane 1998 değeri vardır
# result = years.count(1998)

#12- years dizisinin tüm elemanlarını siliniz.
# years.clear()
# print(years)

# #13- kullanıcıdan alacağını 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("Marka adi: ")                 ### 3kere ekledim cunku henuz döngü kısmına gelmedim.!!
markalar.append(marka)                         #şimdi burda mantık şu markalar boş listesi oluşturdun ; kullanıcıdan istediğim için input ile marka ismi aldım ve kullanıcının verdiğini markalar listesine ekledim tekrar marka'ya döndüm aynı işlem devam ettikçe istenilen sayıda marka oluşturdum.
marka = input("Marka adi: ")
markalar.append(marka)
marka = input("Marka adi: ")
markalar.append(marka)

print(markalar)


print(result)