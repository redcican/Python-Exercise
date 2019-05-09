# Remove all falsy value in Python
# Falsy value in Python includes 'None', 'False'
# 0, 0.0, [], {}, (), '', set()

def bounce(arr):
    truthies = []

    for element in arr:
        if element:
            truthies.append(element)
    return truthies


# filter function

def bounceFilter(arr):
    truthies = list(filter(lambda x : x, arr))
    return truthies

# list compresension
def bounceList(arr):
    return [arr[i] for i in range(len(arr)) if arr[i]]

print(bounce([7, 'ate', '', False, 0]))
print(bounceFilter([7, 'ate', '', False, 0, {}, set(), 9]))
print(bounceList([7, 'ate', '', False, 0, {}, set(), 9]))
print(bounceList([0, '', 1,'apple', None, False]))
