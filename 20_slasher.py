# return the remaining elements of an array
# after chopping off `n` elements from the head


def slasher(arr, howMany):
    return arr[howMany:]




print(slasher([1,2,3],2))
print(slasher(["burgers", "fries", "shakes"],1))
print(slasher([1,2,23,434,43,2,32],4))