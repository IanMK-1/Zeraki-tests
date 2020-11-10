# 1)  Given an array K with N integers from 1 to N+1 such that the array 
#     has exactly one integer missing, writea Java function that returns the missing integer
#     .e.g. given K = [3,5,4,1], the function should return 2

def findMissingInteger(arr):
    max_number = max(arr)
    comparison_array = []
    for x in range(1, max_number):
        comparison_array.append(x)
    for x in comparison_array:
        if x not in arr:
            return x


print(findMissingInteger([3,5,4,1]))

