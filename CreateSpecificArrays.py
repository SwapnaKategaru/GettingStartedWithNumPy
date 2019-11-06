# Import numpy library
import numpy as np

# Create a specific array
a = np.zeros((2, 3))
print('np.zeros((2,3)= \n{}\n'.format(a))

""" RESULT
np.zeros((2,3)= 
[[0. 0. 0.]
 [0. 0. 0.]] """


b = np.ones((3, 3))
print('np.ones((3,3))= \n{}\n'.format(b))

""" RESULT
np.ones((2,3))= 
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]] """


c = np.empty((2, 3))
print('np.empty((2,3))= \n{}\n'.format(c))

""" RESULT
np.empty((2,3))= 
[[0. 0. 0.]
 [0. 0. 0.]] """


d = np.arange(1, 10, 2)
print('np.arange(1, 10, 2)= \n{}\n'.format(d))

""" RESULT
np.arange(1, 10, 2)= 
[1 3 5 7 9] """


e = np.linspace(1, 2, 7)
print('np.linspace(1, 2, 7)= \n{}\n'.format(e))

""" RESULT
np.linspace(1, 2, 7)= 
[1.         1.16666667 1.33333333 1.5        1.66666667 1.83333333
 2.        ] """


f = np.random.random((2, 3))
print('np.random.random((2, 3))= \n{}\n'.format(f))

""" RESULT
np.random.random((2, 3))= 
[[0.92225091 0.77018345 0.72397607]
 [0.87352043 0.60342509 0.38303005]] """


# Create array of specific range of numbers
random_num = np.random.randint(-1, 4, size=(3, 3))
print("random_num:", random_num)

""" RESULT
np.random.random((2, 3))= 
[[0.92225091 0.77018345 0.72397607]
 [0.87352043 0.60342509 0.38303005]] """


# Create a identity matrix
a = np.identity(4)
print("a:", a)

""" RESULT
a: [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]] """


# Repeat a matrix or array - (vector)
vector = np.array([1, 2, 3])
v = np.repeat(vector, 3)
print("v:", v)

""" RESULT
v: [1 1 1 2 2 2 3 3 3] """


# Repeat a matrix or array - (2D-Array)
dim2_array = np.array([[1, 2, 3]])
a = np.repeat(dim2_array, 3, axis=0)
print("a:", a)

""" RESULT
a: [[1 2 3]
 [1 2 3]
 [1 2 3]] """


dim2_array = np.array([[1, 2, 3]])
a = np.repeat(dim2_array, 3, axis=1)
print("a:", a)

""" RESULT
a: [[1 1 1 2 2 2 3 3 3]] """
