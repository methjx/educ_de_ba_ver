# # for ve while döngüsüne alternatif olarak kullanabileceğimz bir yöntem
# for x in range(10):
#     print(x)
# ##-----------------------------------
# numbers = [x for x in range(10)]
# print(numbers)
# ##-----------------------------------
# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(numbers) 
#                                ###-------yukarıda ki işlemi comprehensionsla yapınca;
# numbers = [x for x in range(10)]
# print(numbers)
# ##---------
# for x in range (10):
#     print(x**2)
#                                 ###----------------
# numbers = [x**2 for x in range(10)] 
# print(numbers)  
#                                  ###-------------
# numbers = [x*x for x in range(10) if x%3==0]
# print(numbers)

# ##-----
# myString = "hello"
# myList = []
# for letter in myString:
#     myList.append(letter)
# print(myList)
# ###-------yukarıda ki işlemi comprehensionsla yapınca;
# myList = [letter for letter in myString]
# print(myList)
# ####--------
# years = [1983,1999,2008,1956,1996]
# ages = [2021-year for year in years]
# print(ages)
# ##-------------
# results = [x if x%2==0 else "Teksayi" for x in range(1,10)]
# print(results)
# ##-------------
# result = [] #####sunu acıklayayım ilk döngü ikinci döngüyü döndürcek ve ikinci döngü tamamlandıgında birinci döngü 1 kademe atlıcak ve tekrar y döngüsünü döndürcek işlem bitene kadar
# for x in range (3):
#     for y in range(3):
#         result.append((x,y))
# print(result)
# ###---------aynı işlemi comprehensionsla yapmak istersek;;
# numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range (3)]
# print(numbers)