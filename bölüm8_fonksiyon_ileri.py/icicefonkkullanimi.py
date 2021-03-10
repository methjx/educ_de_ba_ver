def greeting(name):
    print("hello",name)
# greeting("ali")
# print(greeting)

sayHello = greeting
# print(sayHello)
# print(greeting)

# print(greeting("ali"))
# print(sayHello("ali"))

# del sayHello
# print(greeting)  ##yinede 1 adres alırız çünkü sadece say hello ya tanımladıgımızı siliyoruz ,datayı değil.

# print(sayHello) ## sildiğimiziçin nameerror alırız çğnkü bi tanımlaması yok sildik.

### --- ENCAPSULATION
# def outer(num1):
#     print("outer")
#     def inner_inc(num1):
#         print("inner")
#         return num1 +1
#     num2 = inner_inc(num1)
#     print(num1,num2)

# outer(10)
# inner_inc(10) ### Inner çağırmak istediğimizde çağıramayız çünkü bunu fonk içinde ayrı fonk olarak tanımladık!!!


def factorial(number):      ##"""BUNU YANLIŞYORUMLAMISOLABİLİRİM"""###Sistemi kendimce şöyle yorumladım; 5*4=20 (number=20) ve innenfacnumber -1 yani 20*3=60 number=60 , 60*2=120, 120*1=120
    if not isinstance(number,int):          ### FİLTRELEME
        raise TypeError("Number must be an integer")

    if not number >= 0:                     ### FİLTRELEME
        raise ValueError("Number must be zero or positive")

    def inner_fac(number):
        if number <=1:
            return 1
        
        return number*inner_fac(number-1)
    return inner_fac(number)
try:  
    print(factorial("3"))
except Exception as ex:    ##Direk hatayı göstermek için ...!
    print(ex)