# return true only if all values are unique. ohterwise false
# using Array, object, no set data structure

def unique(string):
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j:
                if string[i] == string[j]:
                    return False
    return True


# en effective way
from collections import Counter

def effectiveUnique(string):
    counter = Counter(string)
    for values in counter.values():
        if values > 1:
            return False
    return True


print(unique("abced"))
print(unique("abacdefb"))
print("###############################")
print(effectiveUnique("abced"))
print(effectiveUnique("abacdefb"))
