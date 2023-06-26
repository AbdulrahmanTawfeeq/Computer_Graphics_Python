# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 00:40:04 2020

@author: Ahmad
"""


# method to return the diagonal of 4 x 4 matrix
def diagonal_of_4x4_matrix():
    mtrx = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    result = []  # empty list to be filled with the values of the diagonal
    # loop to ask the user to input the values of the matrix from keyboard
    for r in range(4):  # each row
        for c in range(4):  # each value in the row
            index = r, c  # variable to inform the user which index he is filling out
            value = input("Enter the value of the index " + str(index) + ": ")  # to ask the user to input the value
            mtrx[r][c] = int(
                value)  # assign the intered value to the index in the matrix to create the 4x4 matrix at the end of those loops
            # cast the string to int
            if r == c:  # in case the row and the column are equal, condition to get the values of the diagonal
                result.append(mtrx[r][c])  # append the value to the empty list
    return result  # this method will return the list that contains the diagonal of the matrix


print(diagonal_of_4x4_matrix())  # calling for the method and printing the diagonal result

print("#" * 50)

x = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for r in range(len(x)):  # first loop for each row
    for c in range(len(x[r])):  # second loop to go inside the values of each row
        index = r, c  # variable to inform the user which index he is filling out
        value = input("Enter the value of the index " + str(index) + ": ")  # to ask the user to input the value
        x[r][c] = int(value)  # assign the intered value to the index in the matrix , cast the string to int
        if c == 1:  # in case we are at the first column
            temp = x[r][c - 1]  # temprory variable to save the first value in the row
            x[r][c - 1] = x[r][c]  # first value will be equal to the second value
            x[r][c] = temp  # second value will have the value of the first which is saved in the temp variable

        # prinying the matrix that we swapped the first and second colimn of it
for i in x:
    print(i)
