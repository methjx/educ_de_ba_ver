# x = int(input("x.sayiyi gir kam: "))
# y = int(input("y.sayiyi gir kam: "))

# if x > y:
#     print("x y den büyüktür. ")
# elif x == y:                           ## elif ve if-else deki temel farklardan biri if ile her koşul eklediğimde bir alt girintide kaydırarak devame ediyorum ve else komutuda geliyor fakat;;; elif de aynı girintide istediğim kadar koşul ekleyebilirim ve aynı else 'e çıkarırım.
#     print("x ve y eşittir.")    
# else:
#     print("y x den büyüktür.")    

num = int(input("sayi: "))

if num > 0:
    print("sayi pozitif canim!")
elif num < 0:
    print("sayi negatif şekerim!")
else: 
    print("sayi sifirdir yagusuglu!")