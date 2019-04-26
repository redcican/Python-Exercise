# return number with most repeates
# if two numbes the repeated the same return first
# if none repeated return -1

def testRepeat(arr):
    amount = {i: arr.count(i) for i in arr}

    if max(amount.values()) == 1:
        return -1
    for k, v in amount.items():
        maxNumber = max(amount.values())
        if v == maxNumber:
            return k


print(testRepeat([5,2,2,1,5]))
print(testRepeat([6,5,5,10,10,10]))
print(testRepeat([3,4,1,6,10]))
print(testRepeat([1,1,1,3,3,3,2,5]))


