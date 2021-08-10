import numpy as np

numbers = np.array([0,5,10,15,25,50,75])

result = numbers[5]


numbers2 = np.array([[0,5,10],[15,25,50],[75,85,90]])
print(numbers2[1][0])
result = numbers2[0:,2] #tümsatırlardan 3.indeksleri aldım

result = numbers2[:,0:2] #0.indekle 3.indeks arasını getir
result = numbers2[-1,:] # son satırdaki tüm sütunları getir.
result = numbers2[:2,:2]
# print(result)

arr1  = np.arange(0,10)
# arr2 = arr1 #referans
arr2 = arr1.copy() #referans kopyalama yaptıgımızda ikiside aynı adreste tutuluyor yani herhangi bir arrayde yapılan değişiklik diğerini etkiliyor .copy() ile ise ikisi farklı adreslerde tutuluyor


arr2[0] = 20
print(arr1)
print(arr2)