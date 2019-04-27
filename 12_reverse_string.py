# reverse a string

def reverseString(string):
    strArr = list(reversed(string))
    reverseStrArr = ''.join(strArr)
    return reverseStrArr



def anotherReverseString(string):
    final = ""
    for i in reversed(range(len(string))):
        final += string[i]
    return final


print(reverseString("hello"))
print(anotherReverseString("hello"))