# Given an array of integers, return indices of 
# the two numbers such that they add up to a specific target.
# the first index should smaller than second
# the smallest index is 1 instead of 0
# example: numbers = [2,7,11,25] target = 9.
# then return [0,1]

def two_sum(arr,target):
    
    hash_map = {k: v for v, k in enumerate(arr)}
    
    for index, value in enumerate(arr):
        if target - value in hash_map:
            index2 = hash_map[target - value]
            if index != index2:
                return index, index2


# another method

def two_sum_another(arr, target):
    for i in range(len(arr)):
        left = arr[i+1:]
        for j in range(len(left)):
            if (arr[i] + left[j] == target):
                return i, j+i+1


print(two_sum([2,25,11,7,2],9))
print(two_sum_another([2,25,11,7,2],9))

