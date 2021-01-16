numbers = [1, 2, 3, 4, 5]

for num in numbers:                      ## yazım formatı fordan sonra kisaltma in numbers listesi
    print(num)           ## bu örnekte iki sekilde kullanabilirim num değişkeni içindeki sayıları öğrenmek için  yada print("Hello") yazsam program 5 kere döner ve 5 kere hello yazar.


names = ["mehmet","mert","bilge"]
for name in names:
    print(f"my name is {name}")

name = "Mehmetcan Yilmaz" ##string ifade tanımlarsak; her bir karakteri tek tek yazar çünkü string de her bir elemean bir dizi elemanı olarak algılanır.
for n in name:
    print(n)

tuple = [(1,2),(1,3),(3,5)]
for t in tuple:
    print(t)

d = {"k1" : 1, "k2" : 2, "k3" : 3}      #d.items() ; direk "d:" diyip çalıştırdıgımızda sadece key bilgilerini veriyordu bu sebeple bir ekstra yapıp ".items" kullanmalıyız.
for key,value in d.items():             ##
    print(value)