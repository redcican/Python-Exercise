# mutations


def mutation(arr):
    firstWord = arr[0].lower()
    secondWord = arr[1].lower()

    for i in secondWord:
        if i not in firstWord:
            return False
    return True

# find Method

def mutationFind(arr):
    firstWord = arr[0].lower()
    secondWord = arr[1].lower()

    for i in secondWord:
        if firstWord.find(i) == -1:
            return False
    return True


print(mutation(["hello", "hey"]))
print(mutation(["helloyy", "hey"]))
print("#####################")
print(mutationFind(["hello", "hey"]))
print(mutationFind(["helloyy", "hey"]))

