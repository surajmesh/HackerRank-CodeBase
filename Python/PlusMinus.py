
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the



import math
import os
import random
import re
import sys

# Make a function for PlusMinus

def plusMinus(arr, n):
    positive_numbers = []   # store pos number 
    negative_numbers = []   # store neg Number
    zeros = []              # store zeros Number

    for index in range(len(arr)):
        if arr[index] > 0:
            positive_numbers.append(arr[index])
        elif arr[index] < 0:
            negative_numbers.append(arr[index])
        else:
            zeros.append(arr[index])

    ratio_of_positive = round(len(positive_numbers) / n, 6) if n != 0 else 0
    ratio_of_negative = round(len(negative_numbers) / n, 6) if n != 0 else 0
    ratio_of_zeros = round(len(zeros) / n, 6) if n != 0 else 0

    return ratio_of_positive, ratio_of_negative, ratio_of_zeros

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr, n)
    print(result[0])
    print(result[1])
    print(result[2])

 
