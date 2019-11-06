# Importing numpy library
import numpy as np

# Creating an array of integers using array function
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("a:", a)
print("b:", b)

""" RESULT
a:  [1 2 3]
b:  [[1 2 3]
 [4 5 6]] """


# Creating an array of floats using array function
c = np.array([[9.0, 8.0, 7.0], [3.0, 2.0, 1.0]])
print("c:", c)

""" RESULT
c:  [[9. 8. 7.]
 [3. 2. 1.]] """


# Creating a 3D-Array
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("b:", b)

""" RESULT
b:  [[[1 2]
  [3 4]]
 [[5 6]
  [7 8]]] """


# Specifying storage type of values in an array
a = np.array([1, 2, 3], dtype='int16')
b = a.dtype
print("a:", a)
print("b:", b)

""" RESULT
a:  [1 2 3]
b:  int16 """

a = np.array([1, 2, 3], dtype='float32')
b = a.dtype
print("a:", a)
print("b:", b)

""" RESULT
a:  [1. 2. 3.]
b:  float32 """

c = np.array([[1, 2], [3, 4]], dtype='complex')
print("c:", c)

""" RESULT
c: [[1.+0.j 2.+0.j]
 [3.+0.j 4.+0.j]] """


# NumPy methods to get details of an array
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("a:", a)
print("b:", b)
""" RESULT 
[1 2 3] 
[[1 2 3]
 [4 5 6]] """

# Dimensions in array
print("Dimensions of a:", a.ndim)
print("Dimensions of b:", b.ndim)
""" RESULT 
a's ndim 1 
b's ndim 2 """

# Shape of array
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)
""" RESULT 
a's shape (3,)
b's shape (2, 3) """

# Size of array
print("Size of a:", a.size)
print("Size of b:", b.size)
""" RESULT 
a's size 3
b's size 6 """

# DataType of array
print("DataType of a:", a.dtype)
print("DataType of b:", b.dtype)
""" RESULT 
a's dtype int32
b's dtype int32 """

# Item-size of array
print("ItemSize of a:", a.itemsize)
print("ItemSize of b:", b.itemsize)
""" RESULT 
a's itemsize 4
b's itemsize 4 """

# Bytes in an array
print("No.of Bytes of a:", a.nbytes)
print("No.of Bytes of b:", b.nbytes)
""" RESULT 
a's nbytes 12
b's nbytes 24 """


# Matrix multiplication
a = np.array([[1, 1, 1], [1, 1, 1]])
b = np.array([[2, 2], [2, 2], [2, 2]])
c = np.matmul(a, b)
print("c:", c)
""" RESULT
c: [[6 6]
    [6 6]] """