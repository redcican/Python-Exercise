# chunky monkey split a array into two sub arrays

def chunkyMonkey(arr,size):
    groups = []
    while len(arr) > 0:
        groups.append(arr[0:size])
        arr = arr[size:]
    return groups



print(chunkyMonkey(['a','b','c','d'],2))
print(chunkyMonkey(['d','e','f','g','h'],4))
