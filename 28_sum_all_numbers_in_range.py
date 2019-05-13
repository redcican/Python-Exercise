# Sum all numbers in a range

def sumAll(arr):
    start = min(arr)
    end = max(arr)
    total = 0

    for i in range(start, end+1):
        total += i
    return total

# Another simple method

def sumAllSimple(arr):
    return sum(range(min(arr), max(arr)+1))

print(sumAll([1,4]))
print(sumAll([5,1]))
print("There is a simple way below..........")
print(sumAllSimple([1,4]))
print(sumAllSimple([5,1]))
print(sumAllSimple([0,100]))