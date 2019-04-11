# Find the longest word in a sentence

def longestWord(sentence):
    words = sentence.split(" ");
    longestWord = "";
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word

    return longestWord



print(longestWord("I woke up early today"))
print(longestWord("I went straight to the beach"))