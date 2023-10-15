import numpy as np
#For 0-D arrays we don't need square brackets:
# arr_1 = np.array(3)
# print(arr_1)


# Examples of 2-D and 3-D arrays:
# arr_1 = np.array([[1,5,2],[34,2,7]])
# arr_2 = np.array([[[5,3,8],[6,1,9]],[[5,3,8],[6,1,9]]])

# print(arr_1, arr_2)

# Examples of values extraction

# arr = np.array([[6, 5, 7, 8], [65, 2, 7, 9]])

# fourth_element = arr[0,3]
# first_line = arr[:1]
# first_column = arr[:,0]
# print(fourth_element)
# print(first_line)
# print(first_column)


#Negative indexes:

# arr = np.array([[[-4, 3, 1], [-4, 39, 8]], [[2, -4, 10], [15, 193, 8]]])

# print(arr[-1 , -2, -1])

# Flattening array:

# arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])

# new_arr = arr.flatten()
# print(new_arr)

