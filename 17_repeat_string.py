# repeat a string num times

def repeatStringNumTimes(string, num):
    if num < 0:
        return ""
    return string * num


# using for loop
def repeatStringForLoop(string, num):
    if num < 0:
        return ""
    final = ""
    for i in range(num):
         final += string
    return final

# using recuision method
def repeatStringRecuision(string, num):
    if num < 0:
        return ""
    elif num == 1:
        return string
    else:
        return string + repeatStringRecuision(string, num-1)


print(repeatStringNumTimes("abc", 3))
print(repeatStringForLoop("abc", 4))
print(repeatStringRecuision("a bc", 5))