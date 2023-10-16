
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.

# make function for PlusMinus

def plusMinus(arr):
    positive_numbers = []   # store pos number 
    negative_numbers = []   # store neg Number
    zeros = []              # store zeros Number

    for index in range(len(arr)):
        if arr[index] > 0 :
           positive_numbers.append(arr[index])
           ratio_of_positive = (round(len(positive_numbers)/n,6))

        elif arr[index] < 0 :
            negative_numbers.append(arr[index])
            ratio_of_negative = ( len(negative_numbers)/n )
        else :
            zeros.append(arr[index])
            ratio_of_zeros = (len(zeros)/n)
        
    return "{:6f}".format(ratio_of_positive) ,"{:6f}".format(ratio_of_negative),"{:6f}".format(ratio_of_zeros)

# excute function and print Result

n = int(input().strip())
arr = [1, 1, 0, -1, -1]

result =  plusMinus(arr)
print(result[0])
print(result[1])
print(result[2])
