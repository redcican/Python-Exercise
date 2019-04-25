# return first word with greatest number of repeated letters
from collections import Counter

def countLetters(str):
    tempArr = str.split(" ")
    tempItem = [item.lower().split() for item in tempArr]
    
    amount = 1
    letter = None

    for character in tempItem:
        for c in character:
            counter = Counter(x for x in c).most_common(1)
            count = counter[0][1]
            if count > amount:
                amount = count
                letter = character
    return letter




print(countLetters("Javascript is the greaaatest programming language"))