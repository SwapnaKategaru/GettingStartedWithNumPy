# Import numpy library
import numpy as np

b = np.arange(11, 20)
print("b:", b)
""" RESULT
b: [11 12 13 14 15 16 17 18 19] """

# Mathematical operations with arange
array_list = np.arange(1, 10)
result = array_list * array_list
print("Multiples:", result)

""" RESULT
Multiples: [ 1  4  9 16 25 36 49 64 81] """


array_list = array_list - 1
print("Subtracts:", array_list)

""" RESULT
Subtracts: [0 1 2 3 4 5 6 7 8] """

array_list = np.arange(1, 10)
array_list = array_list + array_list
print("Add:", array_list)

""" RESULT
Add: [ 2  4  6  8 10 12 14 16 18] """

array_list = np.array([3, 6, 9, 12])
array_list = array_list / 3
print("Divide:", array_list)

""" RESULT
Divide: [1. 2. 3. 4.] """


array_list = np.arange(1, 10)
array_list += 5
print("Add_5:", array_list)

""" RESULT
Add_5: [ 6  7  8  9 10 11 12 13 14] """

array_list = np.array([1, 2, 3, 4])
array_list = array_list ** 2
print("Powers:", array_list)

""" RESULT
Powers: [ 1  4  9 16] """

arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([1, 0, 1, 0])
Add_array = arr_1 + arr_2
print("Sum:", Add_array)

""" RESULT
Sum: [2 2 4 4] """

array = np.array([1, 2, 3])

a = np.sqrt(array)
print("Sqrt: ", a)
""" RESULT 
Sqrt:  [1.         1.41421356 1.73205081] """

b = np.exp(array)
print("Exp: ", b)
""" RESULT 
Exp:  [ 2.71828183  7.3890561  20.08553692] """

c = np.sin(array)
print("Sin: ", c)
""" RESULT 
Sin:  [0.84147098 0.90929743 0.14112001] """

d = np.cos(array)
print("Cos: ", d)
""" RESULT 
Cos:  [ 0.54030231 -0.41614684 -0.9899925 ] """

e = np.log(array)
print("Log: ", e)
""" RESULT 
Log:  [0.         0.69314718 1.09861229] """

f = np.sum(array)
print("Sum: ", f)
""" RESULT 
Sum:  6 """

g = np.std(array)
print("Std: ", g)
""" RESULT
Std:  0.816496580927726 """


# Addition of 2D-Array
z1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
z1 = np.sum(z1, axis=0)
print("z1:", z1)
""" z1: [12 15 18] """

z2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
z2 = np.sum(z2, axis=1)
print("z2:", z2)
""" RESULT
z2: [ 6 15 24] """

z3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
z3 = np.sum(z3)
print("z3:", z3)
""" RESULT
z3: [45] """