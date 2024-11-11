import numpy as np

python_list = [0, 1, 2, 3, 4, 5, 6]

numpy_array = np.array([0, 1, 2, 3, 4, 5, 6])

print('python list : {}'.format(python_list))
print('numpy_array : {}'.format(numpy_array))

"""""

output : python list : [0, 1, 2, 3, 4, 5, 6]

output : numpy_array : [0 1 2 3 4 5 6]

"""""

numpy_array_dimension = numpy_array.ndim

print('numpy_array dimension is {}'.format(numpy_array_dimension))

numpy_array_shape = numpy_array.shape

print('numpy_array shape is {}'.format(numpy_array_shape))

"""""

output : numpy_array dimension is 1

output : numpy_array shape is (7,) 
(second index is empty bcs this array made up of only one dimension so it can't be have column and row, just argument)

"""""

numpy_array_shape_two = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]).shape

print('numpy_array_shape_two is : {}'.format(numpy_array_shape_two))

"""""

output : numpy_array_shape_two is : (1, 10)
(this array different is from other this array have row and column bcs dimension is bigger than one)

"""""
