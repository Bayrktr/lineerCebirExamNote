import math

import numpy as np


def sarrus_method_det(array):
    array_column_lenght = array.shape[1]
    array_row_lenght = array.shape[0]

    if array_column_lenght != 3:
        print('Sarrus method cannot be applied')
        return

    extended_array = array.copy()

    extend_size = array_column_lenght - 1

    for j in range(extend_size):
        extended_array = np.vstack([extended_array, array[j]])

    print(extended_array)

    extended_array_column_lenght = extended_array.shape[0]
    extended_array_row_lenght = extended_array.shape[1]

    total_list_number = (extended_array_column_lenght - extended_array_row_lenght) + 1

    positive_total_numbers_list = []

    for x in range(total_list_number):
        total_index = x
        numbers_list = []
        for y in range(extended_array_column_lenght):
            if (y + x) >= extended_array_column_lenght:
                break

            row = extended_array[y + x]

            for z in range(extended_array_row_lenght):
                item = row[z]
                if (x + z) == total_index:
                    total_index += (extended_array_row_lenght - 2)
                    numbers_list.append(int(item))
                    break
        positive_total_numbers_list.append(numbers_list)

    print(positive_total_numbers_list)

    negative_total_numbers_list = []

    for x in range(total_list_number):
        total_index = x
        numbers_list = []
        for y in range(extended_array_column_lenght):
            if (y + x) >= extended_array_column_lenght:
                break

            row = extended_array[y + x]

            for z in range(extended_array_row_lenght - 1, -1, -1):
                item = row[z]
                if (x + (extended_array_row_lenght - 1 - z)) == total_index:
                    total_index += (extended_array_row_lenght - 2)
                    numbers_list.append(int(item))
                    break
        negative_total_numbers_list.append(numbers_list)

    total_sum_positive = sum(math.prod(sublist) for sublist in positive_total_numbers_list)

    total_sum_negative = sum(math.prod(sublist) for sublist in negative_total_numbers_list)

    det = (total_sum_positive - total_sum_negative)

    return det


def cramer_method_result(array, array2, determinant):
    result_list = []
    array_column_lenght = array.shape[1]
    array_row_lenght = array.shape[0]

    new_array_list = []

    for x in range(array_row_lenght):
        array_copy = array.copy()
        array_copy[:, x] = array2[:, 0]
        new_array_list.append(array_copy)

    print(new_array_list)

    for y in range(len(new_array_list)):
        item = new_array_list[y]
        result = sarrus_method_det(item) / determinant
        result_list.append(result)

    return result_list


cramer_array = np.array([[1, 3, 5],
                         [2, 6, 7],
                         [3, 6, 4]])

cramer_result_array = np.array([
    [2], [4], [6]

],
)

if cramer_array.shape[0] != cramer_array.shape[1]:
    print('not a square matrix')

det = sarrus_method_det(cramer_array)

print(det)  # -9 result

result = cramer_method_result(cramer_array, cramer_result_array, det)

print(result) # [2.0, -0.0, -0.0] result