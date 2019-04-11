# Find the longest word in a sentence

def longestWord(sentence):
    words = sentence.split(" ")
    longestWord = ""
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word

    return longestWord

def efficentLongestWord(sentence):
    words = sentence.split(" ")
    longestWord = max(words, key=len)
    return longestWord

print(longestWord("I woke up early today"))
print(longestWord("I went straight to the beach"))
print("#####################################")
print(efficentLongestWord("I woke up early today"))
print(efficentLongestWord("I went straight to the beach"))