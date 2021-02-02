# def square(num): return num ** 2

# numbers = [1,3,5,9]

# result = list(map(square, numbers))  ### liste eklemediğimde bellekteki adres çıktılar.. o yüzde liste ekle canm
# print(result)


# """---alternatif--------"""

# for item in map(square,numbers):
#     print(item)
# """---"""
# ##################
# #     # lambda ile yaptıgımız işleme dikkat et//isimsiz fonk ile aynı işlemi yaptırdık
# numbers = [1,3,5,9]

# result = list(map(lambda num: num**2, numbers)) ### ismi olmayan bir fonksiyon tanımlayabilirim " lambda "

# print(result)

# """---"""####su sekilde değişkene atayıp yine aynı işlemi yapabilirim...
# numbers = [1,3,5,9]
# square = lambda num: num**2
# result = list(map(square, numbers))
# print(result)

# """---"""

# square = lambda num: num**2
# result = square(5)
# print(result)

"""-----"""
numbers = [1,3,5,9,10,4]
def check_even(num): return num%2 == 0
result = list(filter(check_even, numbers))
print(result)

# """----"""
check_even = lambda num : num%2 == 0
result = list(filter(check_even, numbers))
print(result)