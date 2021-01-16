#### ---- range metodu
# for item in range(10): ### 0-10 a kadar olan sayilari range ile kısıtlayıp yazdırıyorum
#     print(item)
# for item in range(2,10): ### 2 baslangic 10 bitis diyorum ve arasındaki sayilari istiyorum
#     print(item)
# for item in range(2,10,2):  ### 2 den 10 a kadar 2 ser atlayarak devam et diyorum.
#     print(item)        

# print(list(range(50,100,20))) ### direk olarak listeye aldım (mesafeyi belirledim o mesafe arasındaki verileri)

# # -------------------------

####-----enumerate metodu

# index = 0 ###---> for döngüsünde indeks numarasına ihtiyacımız olursa bu kullanılabilir.

# greeting = "Hello There. said obiwan"               ##enumeratesiz!
# for letter in greeting:
#     print(f"letter: {letter}, index:{index}")      ## fstringde index yazmanın alternatifide {greeting[index]} olabilir.
#     index += 1
###--------------------------------------

# greeting = "Hello"
# for index,letter in enumerate(greeting):   ### index,letter yerine item yazıp direk print(item) şeklindede yazabilirz böylelikle liste şeklinde elde edilebilir.key-value sistemi vardır.
#     print(f"letter: {letter}, index:{index}")      ## fstringde index yazmanın alternatifide {greeting[index]} olabilir.

####-----zip metodu ### bir kaç ayrı listeyi birleştirip tek liste olarak cıkartabiliriz.1-a-100,2-b-200 seklinde
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]
print(list(zip(list1,list2,list3)))


for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3): ### burda listelerin içindeki verileri göstermek istedik ! listeden çıkararak..
    print(a,b,c)

