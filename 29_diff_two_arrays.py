# Difference bwtween two arrays

def diffArray(arr1, arr2):
    result = []

    for i in range(len(arr1)):
        if not arr1[i] in arr2:
            result.append(arr1[i])

    for j in range(len(arr2)):
        if not arr2[j] in arr1:
            result.append(arr2[j])

    return result

# using list comprehensions
def diffArrayList(arr1, arr2):
    combo = arr1 + arr2
    return [x for x in combo if combo.count(x) == 1]



print(diffArray([1,2,3,5],[1,2,3,4,5]))
print(diffArray([1,2,3],[4,3,6]))
print(diffArrayList([1,2,3,5],[1,2,3,4,5]))
print(diffArrayList([1,2,3],[4,3,6]))

