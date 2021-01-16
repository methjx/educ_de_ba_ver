name = "Mehmet"
surname = "Yilmaz"
age = 24
#print("My name is "+ name + " "+ surname + " and \nI am " + str(age) + " years old." )  # \n eklediğimiz zaman "and" kısmından itibaren olan yazıyı 2.satıra yazdırır.
greeting = "My name is "+ name + " "+ surname + " and \nI am " + str(age) + " years old." 
print(greeting)
print(type(greeting))
length = len(greeting)

#print(greeting[0]) # [] print greeting yazıp koseli parantez içerisine 0.karakterini yazdırırsak greetin içerisindeki ilk bilgiyi yani M bilgisini verir.
#print(greeting[6]) 
#print(len(greeting)) #len komutu length ile aynı anlamda yani kaç karakter olduğunu bize söyler.
#print(greeting[length -1]) # en sonuncu karakteri gösterir bize !
#print(greeting[-1]) # yine aynı şekilde en sonuncu karakteri bize verir.
#print(greeting[3:7]) # 3(3dahil) ile 7 arasındaki karakterlere ulaşabiliriz.
#print(greeting[3:]) # 3den itibaren al yaz
#print(greeting[:16]) #son karakteri 16 belirle o kısıma kadar al yaz
#print(greeting[2:40:2]) # 2den basla 40 a kadar git fakat 2ser karakter atlayarak git




