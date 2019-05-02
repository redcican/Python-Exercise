# confirm the ending of a string

def confirmEnding(str, target):
#    if(str.endswith(target)):
#        return True
#    return False
# using sub string
    if(str[-len(target):] == target):
        return True
    return False



print(confirmEnding('Bastian', 'n'))
print(confirmEnding('Bastian', 'on'))
