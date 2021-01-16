numbers = [1, 22, 33, 12, 31, 41, 3, 95, 7]
letters = ["s" ,"ö" ,"b" ,"e" ,"g" ,"m" ,"t"]
val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)


# val = numbers[3:6]
# numbers[3] = 13 # tablo içindeki elemanı değiştirir. yani 3.indeksteki 12 yi 13 yaptık.
# print(numbers)
numbers.append(88)   #----> append komutu istediğin listenin sonuna istediğin veriyi ekler.
numbers.insert(2,11)  #---->insert komutu ile burada 2.indekse 11 sayısını ekledik ve önceden 2.indekste olan sayı bir sağa kaydı ve 3 oldu.
# # numbers.insert(-1,99) ##----> en sona eleman eklediğimizde de en daha önce burada olan sayı yine bir sağ kayar.
# numbers.pop() #----->Listedeki en son elemanı çıkarır ya da;
# numbers.pop(0) #----> seçtiğin indeks numarasındaki elemanı cıkarır
# numbers.remove(31) #----> bu ise direk liste içinde gördüğün elemanı (indeks numarasını saymadan) parantez içine yazarak listeden siler.
numbers.sort() #---->listeyi sıralar
letters.sort() #same beeetcha
numbers.reverse() #tersten yazar falan filan
letters.reverse() #kamasutra time
print(len(numbers))
print(len(letters))
# print(numbers.count(1)) #----> içinde kaç tane 1 var say demişiz burda

# numbers.clear() #--> numbers listesi içindeki verileri temizler.
print(letters)
print(numbers)