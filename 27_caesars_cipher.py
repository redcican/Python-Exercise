# caesars cipher

def rot13(string):
    solved = ''

    for i in range(len(string)):
        asciiNum = ord(string[i])
        if(asciiNum >= 65 and asciiNum <= 77):
            solved += chr(asciiNum + 13)
        elif(asciiNum >= 78 and asciiNum <= 90):
            solved += chr(asciiNum -13)
        else:
            solved += string[i]
    return solved


print(rot13('A'))
print(rot13('SERR PBQR PNZC'))