# Pure Bubble Sort Algorithm
# Written by: Derrick Minor
# Description: This is pure python implementation of bubble sort algorithm
# Date: Jan 19, 2017

from __future__ import print_function


def bubble_sort(collection):
    length = len(collection)
    for i in range(length-1, -1, -1):#range(length-1, -1, -1)
        for j in range(i):#range(1, i)
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]

    return collection


if __name__ == '__main__':
    import sys
    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted))
