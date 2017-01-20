# Pure Quick Sort Algorithm
# Written by: Derrick Minor
# Description: This is pure python implementation of quick sort algorithm
# Date: Jan 19, 2017

from __future__ import print_function
from random import shuffle


def sort(collection):
    shuffle(collection)
    return quick_sort(collection)


def quick_sort(collection):
    total_elements = len(collection)

    if total_elements <= 1:
        return collection
    less = []
    equal = []
    greater = []
    pivot = collection[0]

    equal.append(pivot)
    
    for i in range(1, total_elements):
        element = collection[i]

        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    return quick_sort(less) + equal + quick_sort(greater)


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
    print(sort(unsorted))
