def findMedian(arr):
    sorted_arr = sorted(arr)
    
    if len(sorted_arr) % 2 == 0:
        median_2 = (sorted_arr[len(sorted_arr) // 2 - 1] + sorted_arr[len(sorted_arr) // 2]) / 2
        return median_2
    else:
        median = sorted_arr[len(sorted_arr) // 2]
        return median

n = int(input())
arr = list(map(int, input().rstrip().split()))

median = findMedian(arr)
print(median)
