# Import numpy library
import numpy as np

# Return new array of given shape & value
a = np.full((3, 2), 4)
print("a:", a)
""" RESULT 
a: [[4 4]
 [4 4]
 [4 4]] """

b = np.ones((2, 3))
print("b:", b)
""" RESULT 
b: [[1. 1. 1.]
 [1. 1. 1.]] """

# Copying an array
original = np.array([1, 2, 3])
copied = original.copy()
print("copied:", copied)
""" RESULT 
copied: [1 2 3] """

copied[0] = 100
print("original:", original)
print("copied:", copied)
""" RESULT 
original: [1 2 3]
copied: [100   2   3] """


# Boolean masking - using conditionals
data = np.array([[7, 13, 21, 41], [3, 42, 12, 33], [1, 22, 34, 49]])

data_1 = np.any(data > 30, axis=0)
print("data_1:", data_1)
""" RESULT 
data_1: [False  True  True  True] """

data_2 = np.any(data > 30, axis=1)
print("data_2:", data_2)
""" RESULT 
data_2: [ True  True  True] """


data_3 = np.all(data > 30, axis=0)
print("data_3:", data_3)
""" RESULT 
data_3: [False False False  True] """

data_4 = np.all(data > 30, axis=1)
print("data_4:", data_4)
""" RESULT 
data_4: [False False False] """

# Boolean with AND operator
data_5 = ((data > 30) & (data < 50))
print("data_5:", data_5)
""" RESULT 
data_5: [[False False False  True]
         [False  True False  True]
         [False False  True  True]] """

# Obtain opposite of the above result
data_6 = (~((data > 30) & (data < 50)))
print("data_6:", data_6)
""" RESULT 
data_6: [[ True  True  True False]
         [ True False  True False]
         [ True  True False False]] """

data_7 = data[data > 30]
print("data_7:", data_7)
""" RESULT 
data_7: [41 42 33 34 49] """

# List indexing with numPy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a = a[[1, 3, 8]]
print("a:", a)
""" RESULT
a: [2 4 9] """

# Get specific element
b = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
b1 = b[1, 5]
b2 = b[1, -2]
print("b1:", b1)
print("b2:", b2)
""" RESULT
b1: 13 
b2: 13 """

# Get specific row
b3 = b[0, :]
print("b3:", b3)
""" RESULT
b3: [1 2 3 4 5 6 7] """

# Get specific column
b4 = b[:, 2]
print("b4:", b4)
""" RESULT
b4: [3 10] """

# Get specific range of values
b5 = b[0, 1: 6: 2]
print("b5:", b5)
""" RESULT
b5: [2 4 6] """

# Replacing values at defined indices
b[1, 5] = 20
print("c1:", b)
""" RESULT
c1: [[ 1  2  3  4  5  6  7]
    [ 8  9 10 11 12 20 14]] """

b[:, 2] = [1, 2]
print("c2:", b)
""" RESULT
c2: [[ 1  2  1  4  5  6  7]
     [ 8  9  2 11 12 20 14]] """

c3 = b[1, 1: -1: 2]
print("c3:", c3)
""" RESULT
c3: [ 9 11 20] """
