# from functools import reduce
# A = ["Veri","Bilimi","Okulu"]
# print(reduce(lambda a,b: a+b, list(map(lambda x: x[0], A))))

# """BUNU BİR İNCELE ANLAMADIM !!"""
# import numpy as np
# a = np.array([1,1,1])
# b = np.array([2])

# # a+b
# "" ""
# # print(list(map(lambda x: x.upper(), ["Ali","Veli","isik"])))


# liste = [1,2,3,4]
# A = []


# print(list(map(lambda x: x**2, liste)))

# a = [1,2,3]
# print(list(map(lambda x: x*2, a)))




# # ///////////////////////////BU IKISINI BIR KARSILASTIR NEDEN ???
# def yap(x,y,z):
#     try:
#         print(x/y*z)
#     except ZeroDivisionError:
#         print("gecersiz islem")

# yap(1,2,0)

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("sas")
fun = lambda x: x**2
print(fun(3))