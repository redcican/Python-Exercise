# return the second value of an array

def secondValue(arr):
    values = sorted(set(arr))
    
    if len(values) < 2:
        return f'{values[0]}'
    elif len(values) == 2:
        return f'{values[0]} {values[1]}'
    elif len(values) == 3:
        return f'{values[1]}'
    else:
        return f'{values[1]} {values[len(values)-2]}'






print(secondValue([1]))

print(secondValue([4,2]))

print(secondValue([11,44,22]))

print(secondValue([3,2,88,3,-11,67,7]))