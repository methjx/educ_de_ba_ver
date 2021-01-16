# #Identity Operator: is

# x  = y = [1, 2, 3]
# z = [1, 2, 3]
# print(x==y)
# print(x==z)                 ### 5 ve 6.satırda eşitlik operatörleriyle değerlerine bakılıyor.
# print(x is y)            ########### fakat "is" komutu ile yaptıgımızda ; adreslere bakılıyor. x ve y aynı adrese sahip bu yüzden true
# print(x is z)                   #### burda ise x'in ve z'nin (referansı)adresleri farklı oldugundan false bilgisi alacağız.objelerin aynı olup olmadıgına bakıyoruz.

# x = [1, 2, 3]       ### 10'dan 16' ya karşılaştırma yapıyoruz. 15.kısımda az önce bahsettiğimiz değerlerin aynı oldugu görülüyor ve true veriyor fakat değerler aynı olmasına ragmen adresler farklı oldugundan is ile sordugumuzda bize false veriyor.
# y = [2, 4]
# del x[2]
# y[1] = 1
# y.reverse()
# print(x==y)
# print(x is y)
# print(x is not y)

# #Membership Operator: in

x = ["apple","banana"]
print("banana" in x)           

name = "Mehmet"
print("e" in name)
print("e" not in name)