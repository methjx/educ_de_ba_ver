import numpy as np
numbers = np.random.randint(10,100,6)

numbers2 = np.random.randint(10,100,6)
# print(numbers,numbers2)
# result = numbers + numbers2

# result = np.sin(numbers)
# result = np.cos(numbers2)
# result =np.sqrt(numbers)

mnumbers1 = numbers.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)
result = np.vstack((mnumbers1,mnumbers2)) #iki matrisi dikey birleştir.
result = np.hstack((mnumbers1,mnumbers2)) #iki matrisi yatay birleştir.


result = numbers >= 50  #hepsi büyükmü sorgusu
result = numbers %2 == 0 # hepsi çiftmi sorgusu
print(numbers[result])





print(result)
