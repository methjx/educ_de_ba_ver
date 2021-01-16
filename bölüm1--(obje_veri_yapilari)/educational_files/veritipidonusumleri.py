#Farkedildiği üzere tek değişken "r" olduğundan input içerisinde değişkeni istiyorum.
#birden fazla değişkenim olsaydı input içerisinde değişebilen diğer verileride istemek zorundaydım.!

pi = 3.14
r = float(input("yari cap: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r
print ("alan :" , alan)
print ("cevre :" , cevre)
#Örneğin yan yana yazdırmak istersen  9.ve 10satırdaki sistemi şu şekilde yaparız;
#print("alan :" + str(alan) + " cevre :" + str(cevre)) ---> tek satır komutu gibi vs.