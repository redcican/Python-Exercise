# return the largest number of a Two-dimensions Array

def largestOfFour(arr):
    maxes = []
    for i in range(len(arr)):
        tempMax = arr[i][0]
        for j in range(len(arr[i])):
            currentElement = arr[i][j]
            if(currentElement > tempMax):
                tempMax = currentElement
        maxes.append(tempMax)
    return maxes


def effectiveLargestOfFour(arr):
    maxes = []
    for i in range(len(arr)):
        tempMax = max(arr[i])
        maxes.append(tempMax)
    return maxes


print(largestOfFour([[4,5,1,3],[13,27,18,26],[32,35,37,39],[1000, 1001,857,1]]))
print(effectiveLargestOfFour([[4,5,1,3],[13,27,18,26],[32,35,37,39],[1000, 1001,857,1]]))