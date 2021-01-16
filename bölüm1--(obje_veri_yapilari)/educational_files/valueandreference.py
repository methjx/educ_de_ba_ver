## value typs => string, number
x = 5
y = 25

x = y

y= 10
# print(x,y)         ###### yani x üzerine y'yi kopyalamıs olduk ve sonrasında y'ede 10 atadık falan...y de yaptıgımız değişiklşik x i etkilemedi.



#### reference types => list,class 
a = ["apple", "banana"]
b = ["apple", "banana"]
a = b
b[0] = "grape"
print(b,a)          ### yani b de yaptıgım değişiklik a yıda etkiledi fakat value typelarda böyle bir şey söz konusu değildir.
###KISACA : : : : Value typeda ; verinin kendisiyle     --------- Reference Typeda ; Listenin adresiyle ilgileniyoruz. 