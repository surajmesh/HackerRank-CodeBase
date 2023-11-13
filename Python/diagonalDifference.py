#Given a square matrix, calculate the absolute difference between the sums of its diagonals. (left-to-right diagonal - right to left diagonal )

def diagonalDifference(arr):

    i = 0
    sum_1 = 0
    while i < n:
        sum_1 = sum_1 + arr[i][i]  # Access the left-to-right diagonal element
        i = i + 1

    i = 0
    sum_2 = 0
    while i < n:
        sum_2 = sum_2 + arr[i][-1-i]  # Access the right-to-left diagonal element
        i = i + 1
     
    diagDiff = sum_1 - sum_2
    
    return abs(diagDiff)


# Enter input 
n = int(input("Enter the matrix Number(n*n): "))
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().rstrip().split())))


print(diagonalDifference(matrix))
    
