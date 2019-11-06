# Import numpy library
import numpy as np

# Reorganising arrays
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
after_1 = before.reshape(2, 2, 2)
print("after_1: ", after_1)
""" RESULT
after_1:  [[[1 2]
  [3 4]]
 [[5 6]
  [7 8]]] """

after_2 = before.reshape(4, 2)
print("after_2: ", after_2)
""" RESULT
after_2:  [[1 2]
 [3 4]
 [5 6]
 [7 8]] """

# Set (5 x 5) matrix
data1 = np.arange(1, 26)
print("data1:", data1)

data2 = data1.reshape(5, -1)
print("data2:", data2)
""" RESULT
data1: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25]
data2: [[ 1  2  3  4  5]
        [ 6  7  8  9 10]
        [11 12 13 14 15]
        [16 17 18 19 20]
        [21 22 23 24 25]] """

# Vertical stacking of vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
v_stack = np.vstack([v1, v2])
print("Ver_stack:", v_stack)
""" RESULT
Ver_stack: [[1 2 3 4]
            [5 6 7 8]] """

# Obtain multiple copies
v_stack = np.vstack([v1, v1, v2, v2])
print("Ver_stack:", v_stack)
""" RESULT
Ver_stack: [[1 2 3 4]
            [1 2 3 4]
            [5 6 7 8]
            [5 6 7 8]] """


# Horizontal stacking of vectors
h1 = np.array([1, 2, 3, 4])
h2 = np.array([5, 6, 7, 8])
horz_stack = np.hstack([h1, h2])
print("Horz_stack1:", horz_stack)
""" RESULT
Hor_stack: [1 2 3 4 5 6 7 8] """

h1 = np.ones([2, 4])
h2 = np.zeros([2, 2])
horz_stack = np.hstack([h1, h2])
print("Horz_stack2:", horz_stack)
""" RESULT
Hor_stack: [[1. 1. 1. 1. 0. 0.]
            [1. 1. 1. 1. 0. 0.]] """

# Splitting the array horizontally
h = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
h = np.hsplit(h, 2)
print("h:", h)
""" RESULT
h: [array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])] """

# Splitting the array vertically
v = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
v = np.vsplit(v, 2)
print("v:", v)
""" RESULT
v: [array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])"""


# Aggregation functions on array
stats = np.array([[1, 2, 3], [4, 5, 6]])
print("stats:", stats)
""" RESULT 
stats: [[1 2 3]
 [4 5 6]] """

Min_1 = np.min(stats)
print("Min_1:", Min_1)
""" RESULT  
Min_1: 1 """

Min_2 = np.min(stats, axis=1)
print("Min_2:", Min_2)
""" RESULT
Min_2: [1 4] """

Max_1 = np.max(stats)
print("Max_1:", Max_1)
""" RESULT
 Max_1: 6 """

Sum_1 = np.sum(stats)
print("Sum_1:", Sum_1)
""" RESULT
Sum_1: 21 """

Sum_2 = np.sum(stats, axis=0)
print("Sum_2:", Sum_2)
""" RESULT 
Sum_2: [5 7 9] """
