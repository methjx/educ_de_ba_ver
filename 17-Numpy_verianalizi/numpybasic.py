import numpy as np

#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])
print(type(np_array))
print(type(py_list))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)
print(py_multi)
print(np_multi)

print(np_array.ndim) #1boyutlu
print(np_multi.ndim) #2boyutlu

print(np_array.shape) # tekboyutlu 9 eleman
print(np_multi.shape) # 2boyutlu 3/3 matris