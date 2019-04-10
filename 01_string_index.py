# return the first index of serach string in the source string

def findFirstMatch(searchString, sourceString):
    length = len(searchString)
    for index in range(len(sourceString)):
        possibleMatch = sourceString[index:index+length]
        if possibleMatch == searchString:
            return index
    return -1


testStr = "abcdefghiyes"
searchStr = "yes"
print(findFirstMatch(searchStr, testStr))