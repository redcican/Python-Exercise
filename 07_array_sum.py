# check if all the numbers summed up
# are equal to a largest number 
# that we have in an list

def ArraySum(arr):
    tempArr = sorted(arr)
    largest = tempArr.pop()
    result = sum(tempArr)
    return largest == result


# return true
print(ArraySum([1,2,4,6,13]))
# return false
print(ArraySum([1,2,4,34,22]))