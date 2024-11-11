import numpy as np

numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

numpy_array_reshape = numpy_array.reshape(1, 10)

print('numpy_array : {}'.format(numpy_array))

print('numpy_array_reshape : {}'.format(numpy_array_reshape))

"""""

output : numpy_array : [0 1 2 3 4 5 6 7 8 9]

output : numpy_array_reshape : [[0 1 2 3 4 5 6 7 8 9]]
(difference is this in two array first one have not row and column bcs first array dimension is one, second array have row and column bcs second array dimension is bigger than one)

Warning : when trying shape the numpy arrays, old array size and new array size should be same otherwise code pissed off

"""""

numpy_array_size = numpy_array.size

print(numpy_array_size)

"""""

output : 10

"""""

reshape_example_one = numpy_array.reshape(5,2)

print(reshape_example_one)

"""""

output : 

[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]

"""""

