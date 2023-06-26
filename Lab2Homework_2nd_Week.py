# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:10:57 2020

@author: AbdulrahmanTawfeeq
"""

# =============================================================================
# Q1: Create a new list, and put tupels with 3 values from the following list
# x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# result=> z=[(1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15)]
# =============================================================================
print("\n\n\n############################################################################\n---Answer of Q1---")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

z = []  # defining a new list
i = 0  # defining the i which represents the itration

for eachIndex in x:
    if i < len(x):
        z.append((x[i], x[i + 1], x[i + 2]))
        i += 3
print("\n", z, "\n############################################################################\n\n\n\n")

# =============================================================================
# Another solution for Q1
# x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# 
# new=[]
# i=0
# for num in x:
#     if i<len(x):
#         new.append( tuple(x[i:i+3]) )
#         i+=3
#         
# print(new)
# =============================================================================


# =============================================================================
# Q2: How to add value to tupel
# y=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# =============================================================================
print("\n\n\n############################################################################\n---Answer of Q2---")
y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# convert tupel to list
List = list(y)

# add values to the list
List.insert(0, 'First index')
List.insert(16, 'Last index')

# convert the list to tuple
Tuple = tuple(List)

print("Tupel Before: ", y, "\n")
print("Tupel After: ", Tuple, "\n############################################################################\n\n\n\n")

# =============================================================================
# Q3: From the following tupel, Create two functions one for odd and one for even
# t=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# =============================================================================
print("\n\n\n############################################################################\n---Answer of Q3---")
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)


def even_in_tupel():
    print("---Even numbers in the tupel---")
    for num in t:
        if num % 2 == 0:
            print(num)


def odd_in_tupel():
    print("---Odd numbers in the tupel---")
    for num in t:
        if num % 2 == 1:
            print(num)


even_in_tupel()  # calling the function
odd_in_tupel()  # calling the function

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# First, we should create a list z
z = []

# Second, we should devide the length of the x list (which is 15) by 3 to know howmany list we should
# add to the z list
number_of_lists = len(x) / 3

# the value of 'number_of_tuple' will be float, we should cast it to int to use it in the range method
for i in range(int(number_of_lists)):
    z.append([])

# now, we have this result [ [], [], [], [], [] ] :list with 5 empty lists

index = 0  # represents the indexes of x list(each one strating from 0)
for i in range(len(z)):
    num_of_itrations = 0  # to increase it 3 times in the loop

    # for each loop of (for loop) we loop 3 times in the while loop
    while num_of_itrations < 3:
        z[i].append(x[index])
        num_of_itrations = num_of_itrations + 1  # we increase it because we put it as condition if it is <3
        index = index + 1  # incease it to go for each index of x list

# now we have list of 5 lists '[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]'
# now lest cast to change those lists to tupels

# have a new list to append the tuples to it
result = []
for i in range(len(z)):
    result.append(tuple(z[i]))

print(result)
