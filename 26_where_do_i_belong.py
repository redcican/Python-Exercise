# where do I belong

def getIndexToIns(arr, num):

    for i in range(len(sorted(arr))):
        if num <= arr[i]:
            return i+1
    return len(arr)



def getIndexToInsAnother(arr, num):
    x = arr
    arr.append(num)
    return sorted(x).index(num)

print(getIndexToIns([40,60,5],50))
print(getIndexToIns([2,5,10],15))
print(getIndexToInsAnother([40,60,5],50))
print(getIndexToInsAnother([2,5,10],15))